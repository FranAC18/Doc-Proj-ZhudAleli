"""Prepara un HTML autónomo desde las ediciones documentales vigentes."""

from __future__ import annotations

import importlib.util
import json
import re
import sys
from collections import defaultdict
from pathlib import Path


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
DOC = ROOT / "documentacion"
SOURCE_MODEL = ROOT / "analisis/2026-10-13/fichas-separadas/generar_markdown.py"
LOCAL_DATA = HERE / "proyecto-local" / "web" / "datos-proyecto.json"

spec = importlib.util.spec_from_file_location("gantt_source", SOURCE_MODEL)
assert spec and spec.loader
model = importlib.util.module_from_spec(spec)
sys.modules["gantt_source"] = model
spec.loader.exec_module(model)

SPRINTS = [
    {"id": "S1", "start": "2026-09-15", "end": "2026-10-12", "title": "Requisitos y diseño", "goal": "Fuentes, alcance, requisitos y diseño preparados para revisión"},
    {"id": "S2", "start": "2026-10-13", "end": "2026-10-26", "title": "Acceso y administración", "goal": "Acceso privado, cuentas y permisos verificables"},
    {"id": "S3", "start": "2026-10-27", "end": "2026-11-09", "title": "Actividades y encargos", "goal": "Actividades, responsables y encargos vinculados"},
    {"id": "S4", "start": "2026-11-10", "end": "2026-11-23", "title": "Asistencia y continuidad", "goal": "Asistencia y participación; continuidad según decisiones abiertas"},
    {"id": "S5", "start": "2026-11-24", "end": "2026-12-07", "title": "Producción y rendición", "goal": "Producción, existencias y rendición según capacidad"},
    {"id": "S6", "start": "2026-12-08", "end": "2026-12-21", "title": "Reportes e integración", "goal": "Reportes, contenido autorizado e integración"},
    {"id": "Cierre", "start": "2026-12-22", "end": "2026-12-23", "title": "Validación y entrega", "goal": "Entrega de lo efectivamente completado y pendientes explícitos"},
]
WINDOW = {item["id"]: item for item in SPRINTS}


def source_link(relative: str) -> str:
    return "../documentacion/" + relative


def document_rows(relative: str, prefix: str) -> list[tuple[str, str, str]]:
    lines = (DOC / relative).read_text(encoding="utf-8").splitlines()
    pattern = re.compile(rf"^\| ((?:{prefix})-[A-Z]+-\d+) \| (.*?) \| (.*?) \|$")
    return [match.groups() for line in lines if (match := pattern.match(line))]


def priorities() -> dict[str, str]:
    source = (DOC / "requisitos/priorizacion/priorizacion_requisitos_v1.2_2026-10-13.md").read_text(encoding="utf-8")
    return dict(re.findall(r"^\| `(R(?:N)?F-[A-Z]+-\d+)` \| (Esencial|Alta|Complementaria) \|", source, re.M))


def pile_positions() -> dict[str, int]:
    source = (DOC / "pila_producto/pila_producto_v1.5_2026-10-13.md").read_text(encoding="utf-8")
    base = source.split("## Línea base ordenada", 1)[1].split("## Diez historias técnicas en propuesta", 1)[0]
    positions = {code: int(number) for number, code in re.findall(r"^\| (\d+) \| `((?:HU|HT)-[A-Z0-9]+-\d+)` \|", base, re.M)}
    assert len(positions) == 60
    return positions


def date_window(label: str) -> tuple[str, str]:
    if label.startswith("S1;"):
        return WINDOW["S1"]["start"], WINDOW["S1"]["end"]
    if "Transversal desde S2" in label or "S2–S6" in label:
        return WINDOW["S2"]["start"], WINDOW["S6"]["end"]
    digits = [int(value) for value in re.findall(r"S([1-6])", label)]
    assert digits, label
    return WINDOW[f"S{min(digits)}"]["start"], WINDOW[f"S{max(digits)}"]["end"]


def pending_items() -> list[dict[str, str]]:
    text = (DOC / "requisitos/priorizacion/priorizacion_requisitos_v1.2_2026-10-13.md").read_text(encoding="utf-8")
    decisions = text.split("## Decisiones abiertas, ordenadas por urgencia de aclaración", 1)[1].split("## Relación con la pila de producto", 1)[0]
    interview = text.split("## Prioridad de aclaración de la entrevista", 1)[1].split("## Historial de cambios", 1)[0]
    result: list[dict[str, str]] = []
    for line in decisions.splitlines():
        match = re.match(r"^\| (\d+) \| `(P-\d+)` — (.*?) \| (.*?) \| (.*?) \|$", line)
        if match:
            order, code, title, urgency, detail = match.groups()
            result.append({"id": code, "type": "Decisión abierta", "title": title, "priority": urgency, "detail": detail, "order": int(order)})
    for line in interview.splitlines():
        match = re.match(r"^\| (\d+) \| (.*?) \| (.*?) \| (.*?) \|$", line)
        if match:
            order, title, urgency, detail = match.groups()
            result.append({"id": f"ENT-{order}", "type": "Tema de entrevista", "title": title, "priority": urgency, "detail": detail, "order": int(order)})
    result.extend([
        {"id": "RNF-OPS-001", "type": "Requisito propuesto", "title": "Copias protegidas y restauración demostrable", "priority": "Alta", "detail": "Depende de P-11; fuera de los nueve RNF confirmados.", "order": 1},
        {"id": "RF-COS-001", "type": "Requisito propuesto", "title": "Costo completo", "priority": "Media", "detail": "Depende de P-06; fuera de los 51 RF confirmados.", "order": 2},
    ])
    assert len([item for item in result if item["type"] == "Decisión abierta"]) == 13
    assert len([item for item in result if item["type"] == "Tema de entrevista"]) == 9
    return result


def build_data() -> dict:
    users = model.user_stories()
    technical = model.tech_stories()
    tasks = model.tasks()
    functional_path = "requisitos/funcionales/requisitos_funcionales_v1.1_2026-10-12.md"
    nonfunctional_path = "requisitos/no_funcionales/requisitos_no_funcionales_v1.1_2026-10-12.md"
    user_path = "historias/usuario/historias_usuario_v2.5_2026-10-13.md"
    technical_path = "historias/tecnicas/historias_tecnicas_v1.5_2026-10-13.md"
    task_path = "sprints/sprint_backlog_v1.2_2026-10-13.md"
    priority = priorities()
    positions = pile_positions()
    task_records = []
    tasks_by_hu: dict[str, list[str]] = defaultdict(list)
    tasks_by_ht: dict[str, list[str]] = defaultdict(list)
    for task in tasks:
        hu = list(dict.fromkeys(re.findall(r"HU-[A-Z]+-\d+", task.user_stories)))
        ht = list(dict.fromkeys(re.findall(r"HT-[A-Z0-9]+-\d+", task.tech_stories)))
        for code in hu:
            tasks_by_hu[code].append(task.code)
        for code in ht:
            tasks_by_ht[code].append(task.code)
        window = WINDOW[task.sprint]
        task_records.append({
            "id": task.code, "kind": "task", "title": task.title, "sprint": task.sprint,
            "start": window["start"], "end": window["end"], "priority": task.priority,
            "description": task.result, "sourceState": task.status, "hu": hu, "ht": ht,
            "source": source_link(task_path),
        })
    user_records = []
    for story in users:
        start, end = date_window(story.sprint)
        user_records.append({
            "id": story.code, "kind": "hu", "title": story.title, "sprint": story.sprint,
            "start": start, "end": end, "priority": story.priority,
            "description": story.need, "sourceState": "Historia de línea base; avance no verificado",
            "rf": [story.origin], "tasks": tasks_by_hu[story.code], "pilePosition": positions[story.code],
            "criteria": story.criteria, "source": source_link(user_path),
        })
    technical_records = []
    for story in technical:
        start, end = date_window(story.sprint)
        technical_records.append({
            "id": story.code, "kind": "ht", "title": story.title, "sprint": story.sprint,
            "start": start, "end": end, "priority": story.priority,
            "description": story.description, "sourceState": story.status,
            "tasks": tasks_by_ht[story.code], "related": story.related,
            "pilePosition": positions.get(story.code),
            "source": source_link(technical_path),
        })
    functional = []
    for code, need, check in document_rows(functional_path, "RF"):
        linked = [story for story in users if story.origin == code]
        assert len(linked) == 1, code
        story = linked[0]
        start, end = date_window(story.sprint)
        functional.append({
            "id": code, "kind": "rf", "title": need, "sprint": story.sprint,
            "start": start, "end": end, "priority": priority[code],
            "description": need, "criteria": [check], "sourceState": "Confirmado como requisito; avance no verificado",
            "hu": [story.code], "tasks": tasks_by_hu[story.code], "source": source_link(functional_path),
        })
    nonfunctional = []
    for code, need, check in document_rows(nonfunctional_path, "RNF"):
        nonfunctional.append({
            "id": code, "kind": "rnf", "title": need, "sprint": "Transversal S2–S6",
            "start": WINDOW["S2"]["start"], "end": WINDOW["S6"]["end"],
            "priority": priority[code], "description": need, "criteria": [check],
            "sourceState": "Confirmado como requisito; sin relación uno a uno con tareas",
            "tasks": [], "source": source_link(nonfunctional_path),
        })
    assert (len(functional), len(nonfunctional), len(user_records), len(technical_records), len(task_records)) == (51, 9, 51, 19, 27)
    return {
        "title": "Zhud Alelí — cronograma integral",
        "edition": "1.1 · 13 de octubre de 2026",
        "window": {"start": "2026-09-15", "end": "2026-12-23"},
        "sprints": SPRINTS,
        "items": task_records + user_records + technical_records + functional + nonfunctional,
        "pending": pending_items(),
        "sources": [
            {"label": "Plan de sprints v1.2", "url": source_link("sprints/plan_sprints_v1.2_2026-10-13.md")},
            {"label": "Sprint backlog v1.2", "url": source_link(task_path)},
            {"label": "Historias de usuario v2.5", "url": source_link(user_path)},
            {"label": "Historias técnicas v1.5", "url": source_link(technical_path)},
            {"label": "Pila de producto v1.5", "url": source_link("pila_producto/pila_producto_v1.5_2026-10-13.md")},
            {"label": "Requisitos funcionales v1.1", "url": source_link(functional_path)},
            {"label": "Requisitos no funcionales v1.1", "url": source_link(nonfunctional_path)},
            {"label": "Prioridades y decisiones v1.2", "url": source_link("requisitos/priorizacion/priorizacion_requisitos_v1.2_2026-10-13.md")},
        ],
    }


def main() -> None:
    data = build_data()
    local_data = json.loads(json.dumps(data, ensure_ascii=False))
    local_data["edition"] = "2.0 · 13 de octubre de 2026"
    for item in local_data["items"]:
        if item.get("source"):
            item["source"] = item["source"].replace("../documentacion/", "/fuentes/")
    for item in local_data["sources"]:
        item["url"] = item["url"].replace("../documentacion/", "/fuentes/")
    LOCAL_DATA.parent.mkdir(parents=True, exist_ok=True)
    LOCAL_DATA.write_text(json.dumps(local_data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(LOCAL_DATA)
    print("Sprints: 6 + cierre; tareas: 27; HU: 51; HT: 19; RF: 51; RNF: 9; pendientes: 24")
    from generar_dashboard import main as build_local_dashboard
    build_local_dashboard()


if __name__ == "__main__":
    main()
