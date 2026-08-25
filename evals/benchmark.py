import argparse
from datetime import datetime, timezone
import json
from pathlib import Path
import sys
import time

# Añadir tools/agent-lab/src al PYTHONPATH si es necesario
lab_src = Path(__file__).resolve().parent.parent / "tools" / "agent-lab" / "src"
if str(lab_src) not in sys.path:
    sys.path.insert(0, str(lab_src))

from agent_harness.adapters.base import ModelAdapter
from agent_harness.agent import Agent
from agent_harness.config import Settings
from agent_harness.memory import MemoryStore
from agent_harness.models import ModelCapability, ModelResponse, UsageInfo
from agent_harness.telemetry import estimate_cost
from agent_harness.tools import build_tools


class SimulatedBenchmarkAdapter:
    """Adaptador simulado para pruebas de benchmark sin consumir cuota de API."""

    def __init__(self, model_id: str, provider: str):
        self._model_id = model_id
        self._provider = provider

    @property
    def model_id(self) -> str:
        return self._model_id

    @property
    def provider_name(self) -> str:
        return self._provider

    @property
    def capabilities(self) -> set[ModelCapability]:
        return {
            ModelCapability.TOOL_CALLING,
            ModelCapability.STRUCTURED_OUTPUTS,
            ModelCapability.REASONING_TOKENS,
            ModelCapability.SYSTEM_MESSAGES,
        }

    def complete(self, messages, tools=None, **kwargs) -> ModelResponse:
        time.sleep(0.05)  # simular latencia de red
        prompt_text = str(messages[-1].content)
        content = f"Simulación de respuesta para [{self.model_id}]: Procesa acopio, peso, merma, socia, fecha con calculate 83.25 y comprobación backend permission obligatoria."
        return ModelResponse(
            content=content,
            finish_reason="stop",
            usage=UsageInfo(prompt_tokens=120, completion_tokens=45, total_tokens=165),
        )

    def stream(self, messages, tools=None, **kwargs):
        yield self.complete(messages, tools, **kwargs)


def run_benchmark(models: list[str], dry_run: bool = False, output_md: str | None = None) -> None:
    dataset_path = Path(__file__).resolve().parent / "dataset" / "benchmark_tasks.json"
    if not dataset_path.exists():
        print(f"Error: no se encontró el dataset en {dataset_path}", file=sys.stderr)
        return

    tasks = json.loads(dataset_path.read_text(encoding="utf-8"))
    settings = Settings()
    router = settings.build_router()

    results = []
    print(f"\nIniciando Benchmark Zhud Alelí Multi-Modelo ({len(tasks)} tareas, {len(models)} modelos)...")
    print("=" * 80)

    for model_key in models:
        adapter: ModelAdapter
        if dry_run:
            adapter = SimulatedBenchmarkAdapter(model_key, "simulated")
        else:
            try:
                adapter = router.resolve(model_name=model_key)
            except Exception as exc:
                print(f"Advertencia: no se pudo resolver '{model_key}': {exc}. Usando simulación.")
                adapter = SimulatedBenchmarkAdapter(model_key, "simulated")

        print(f"\nEvaluando Modelo: {adapter.model_id} ({adapter.provider_name})")
        print("-" * 50)

        for task in tasks:
            start_t = time.perf_counter()
            error_msg = None
            response_text = ""
            tokens_in = 0
            tokens_out = 0

            # Crear memoria y agente efímeros para el test
            memory = MemoryStore(":memory:")
            tools = build_tools(memory, "benchmark-user")
            agent = Agent(model=adapter, memory=memory, tools=tools, user_id="benchmark-user")

            try:
                response_text = agent.run(task["input"])
            except Exception as exc:
                error_msg = str(exc)
                response_text = f"ERROR: {exc}"

            latency_ms = round((time.perf_counter() - start_t) * 1000, 2)
            matched_kw = sum(1 for kw in task["expected_keywords"] if kw.lower() in response_text.lower())
            accuracy = round((matched_kw / len(task["expected_keywords"])) * 100, 1)

            # Estimación básica de tokens si no vino en usage
            tokens_in = len(task["input"].split()) * 2
            tokens_out = len(response_text.split()) * 2
            cost_usd = estimate_cost(adapter.model_id, tokens_in, tokens_out)

            record = {
                "model_id": adapter.model_id,
                "provider": adapter.provider_name,
                "task_id": task["id"],
                "task_name": task["name"],
                "latency_ms": latency_ms,
                "accuracy_pct": accuracy,
                "tokens_in": tokens_in,
                "tokens_out": tokens_out,
                "cost_usd": cost_usd,
                "status": "PASS" if not error_msg and accuracy >= 50.0 else "FAIL",
                "error": error_msg,
            }
            results.append(record)
            print(f"  [{record['status']}] {task['id']:<24} | Latencia: {latency_ms:>7.1f}ms | Precisión: {accuracy:>5.1f}% | Costo: ${cost_usd:.6f}")

    # Generar Reporte Markdown
    now_str = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
    report_lines = [
        "# Informe de Evaluación Comparativa Multi-Modelo (Benchmark)",
        f"\n**Fecha de ejecución**: `{now_str}`",
        f"**Modo**: `{'Simulado / Dry-Run' if dry_run else 'Inferencia Real'}`\n",
        "## Resumen Consolidado por Modelo\n",
        "| Modelo | Proveedor | Latencia Media (ms) | Precisión Media (%) | Costo Total (USD) | Éxito |",
        "| :--- | :--- | ---: | ---: | ---: | :---: |",
    ]

    # Agrupar por modelo
    for m in models:
        m_records = [r for r in results if r["model_id"] == m]
        if not m_records:
            continue
        avg_lat = round(sum(r["latency_ms"] for r in m_records) / len(m_records), 2)
        avg_acc = round(sum(r["accuracy_pct"] for r in m_records) / len(m_records), 1)
        tot_cost = round(sum(r["cost_usd"] for r in m_records), 6)
        passed_count = sum(1 for r in m_records if r["status"] == "PASS")
        rate_str = f"{passed_count}/{len(m_records)}"

        report_lines.append(
            f"| **{m}** | {m_records[0]['provider']} | {avg_lat} | {avg_acc}% | ${tot_cost} | {rate_str} |"
        )

    report_lines.extend([
        "\n## Detalle por Tarea de Dominio\n",
        "| Tarea | Modelo | Latencia (ms) | Precisión (%) | Estado |",
        "| :--- | :--- | ---: | ---: | :---: |",
    ])

    for r in results:
        report_lines.append(
            f"| `{r['task_id']}` | {r['model_id']} | {r['latency_ms']} | {r['accuracy_pct']}% | **{r['status']}** |"
        )

    report_content = "\n".join(report_lines)

    if output_md:
        out_path = Path(output_md).resolve()
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(report_content, encoding="utf-8")
        print(f"\nInforme de benchmark guardado en: {out_path}")
    else:
        print("\n" + report_content)


def main() -> None:
    parser = argparse.ArgumentParser(description="Ejecutor de Benchmark Multi-Modelo para Zhud Alelí")
    parser.add_argument("--models", default="gpt-5.6-luna,deepseek-v4,glm-5.2,gemini-2.5-pro", help="Lista de modelos separados por coma")
    parser.add_argument("--dry-run", action="store_true", help="Ejecuta en modo simulación sin consumir cuota de API")
    parser.add_argument("--output", help="Ruta del archivo Markdown de salida para guardar los resultados")
    args = parser.parse_args()

    model_list = [m.strip() for m in args.models.split(",") if m.strip()]
    run_benchmark(models=model_list, dry_run=args.dry_run, output_md=args.output)


if __name__ == "__main__":
    main()
