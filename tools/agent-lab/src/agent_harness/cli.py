import argparse
import sys

from .agent import Agent
from .config import Settings
from .memory import MemoryStore
from .obsidian import ObsidianStore
from .tools import build_tools


def main() -> None:
    parser = argparse.ArgumentParser(description="Agente con arnés multi-modelo agnóstico y memoria SQLite")
    parser.add_argument("--once", help="Ejecuta una consulta y termina")
    parser.add_argument("--model", help="Nombre o clave del modelo a utilizar (ej. gpt-5.6-luna, deepseek-v4, glm-5.2, gemini-3.1-pro)")
    parser.add_argument("--agent-name", default="thesis-agent", help="Nombre lógico del agente para resolver MODEL_AGENT_<NOMBRE>")
    parser.add_argument("--list-models", action="store_true", help="Lista los modelos registrados y sus capacidades")
    parser.add_argument("--telemetry", action="store_true", help="Muestra el resumen de telemetría y costos acumulados")
    parser.add_argument("--list-lessons", action="store_true", help="Lista lecciones pendientes de aprobación")
    parser.add_argument("--approve-lesson", type=int, help="Aprueba una lección pendiente por ID")
    args = parser.parse_args()

    settings = Settings()
    router = settings.build_router()

    if args.list_models:
        print("\nModelos registrados en el Model Router:")
        print("-" * 65)
        for m in router.get_registered_models():
            caps = ", ".join(m["capabilities"])
            print(f"• Clave: {m['key']:<22} | Proveedor: {m['provider']:<8} | Modelo: {m['model_id']}")
            print(f"  Capacidades: {caps}\n")
        return

    if args.telemetry:
        memory = MemoryStore(settings.db_path)
        try:
            summary = memory.get_telemetry_summary()
            print("\nResumen de Telemetría y Costos por Modelo:")
            print("-" * 75)
            if not summary:
                print("No hay registros de telemetría aún.")
            else:
                for row in summary:
                    print(
                        f"• {row['provider'].upper():<8} | {row['model_name']:<18} | Llamadas: {row['total_calls']:<4} | "
                        f"Latencia Media: {row['avg_latency_ms']}ms | Costo: ${row['total_cost_usd']}"
                    )
        finally:
            memory.close()
        return

    if args.list_lessons or args.approve_lesson is not None:
        memory = MemoryStore(settings.db_path)
        try:
            if args.approve_lesson is not None:
                ok = memory.approve_lesson(settings.user_id, args.approve_lesson)
                print("Lección aprobada." if ok else "No se encontró una lección pendiente con ese ID.")
            else:
                for lesson in memory.pending_lessons(settings.user_id):
                    print(f"[{lesson['id']}] {lesson['trigger']} → {lesson['lesson']}")
        finally:
            memory.close()
        return

    memory = MemoryStore(settings.db_path)
    obsidian = ObsidianStore(settings.obsidian_vault_dir, project_root=settings.project_root)

    try:
        model = router.resolve(model_name=args.model, agent_name=args.agent_name)
    except Exception as exc:
        print(f"Error de inicialización de modelo: {exc}", file=sys.stderr)
        raise SystemExit(2)

    agent = Agent(
        model=model,
        memory=memory,
        tools=build_tools(memory, settings.user_id, obsidian),
        user_id=settings.user_id,
        max_steps=settings.max_steps,
        profile_dir=settings.agent_profile_dir,
        project_root=settings.project_root,
    )

    try:
        if args.once:
            print(agent.run(args.once))
            return
        print(f"Agente listo con modelo '{model.model_id}' ({model.provider_name}). Escribe 'salir' para terminar.")
        while True:
            try:
                text = input("\nTú> ").strip()
            except (EOFError, KeyboardInterrupt):
                break
            if text.lower() in {"salir", "exit", "quit"}:
                break
            if text:
                try:
                    print(f"\nAgente> {agent.run(text)}")
                except Exception as exc:
                    print(f"\nError controlado: {exc}", file=sys.stderr)
    finally:
        memory.close()


if __name__ == "__main__":
    main()
