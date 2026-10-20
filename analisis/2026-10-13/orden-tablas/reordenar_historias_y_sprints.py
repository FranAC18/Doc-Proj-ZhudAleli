from __future__ import annotations

import re
from collections import Counter
from pathlib import Path


ROOT = Path(r"F:\Tesis\App Tesis")
DOCS = ROOT / "documentacion"
OLD_HU = DOCS / "historias/usuario/historias_usuario_v2.3_2026-10-13.md"
NEW_HU = DOCS / "historias/usuario/historias_usuario_v2.4_2026-10-13.md"
OLD_SB = DOCS / "sprints/sprint_backlog_v1.0_2026-10-13.md"
NEW_SB = DOCS / "sprints/sprint_backlog_v1.1_2026-10-13.md"
PRIORITY_FILE = DOCS / "requisitos/priorizacion/priorizacion_requisitos_v1.2_2026-10-13.md"


def split_row(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def priority_map() -> dict[str, str]:
    text = PRIORITY_FILE.read_text(encoding="utf-8")
    return dict(re.findall(r"^\| `(RF-[A-Z]+-\d+)` \| (Esencial|Alta|Complementaria) \|", text, re.M))


def build_hu() -> tuple[dict[str, str], Counter]:
    old = OLD_HU.read_text(encoding="utf-8")
    mapped = priority_map()
    sprint_names = [
        "## Sprint 2 — acceso y administración",
        "## Sprint 3 — planificación",
        "## Sprint 4 — asistencia y participación",
        "## Sprint 5 — producción, inventario y rendición",
        "## Sprint 6 — reportes y sitio público",
        "## Continuidad transversal",
    ]
    body = [
        "---",
        "titulo: Historias de usuario de Zhud Alelí",
        'version: "2.4"',
        "fecha: 2026-10-13",
        "autor: Tesista",
        "estado: final-documental-con-prioridad-propuesta",
        "fuente_requisitos: CAT-REQ-001 v1.1",
        "fuente_prioridad: priorizacion_requisitos_v1.2_2026-10-13.md",
        "historias: 51",
        "estimacion: pendiente-del-equipo",
        "revision_directora: pendiente",
        "publicacion: pendiente-de-confirmacion",
        "---",
        "",
        "# Historias de usuario",
        "",
        "Esta edición presenta primero una **tabla breve por bloque** y después los criterios de cada historia. "
        "La importancia propuesta deriva del requisito funcional de origen: **Esencial**, **Alta** o **Complementaria**. "
        "El número de la pila es una **posición de trabajo**, no una medida de importancia. "
        "Dentro de cada tabla se muestran primero las historias esenciales y luego las altas y complementarias; "
        "la ejecución respeta también dependencias y capacidad real.",
        "",
        "| Importancia | Sentido para esta edición |",
        "|---|---|",
        "| Esencial | Sin la capacidad, un recorrido central falla o hay un riesgo grave de acceso o integridad. |",
        "| Alta | Necesaria para completar los procesos acordados de la primera versión. |",
        "| Complementaria | Mejora consulta, comunicación o presentación dentro del alcance aprobado. |",
        "",
        "La clasificación sigue siendo una **propuesta analítica**: no cambia los 51 RF, "
        "no acredita validación académica y no declara trabajo implementado. Estimaciones y responsables siguen pendientes. "
        "S1 cubre requisitos y diseño; estas historias se agrupan en S2–S6 y continuidad transversal.",
        "",
    ]
    all_levels: dict[str, str] = {}
    counts: Counter = Counter()
    rank = {"Esencial": 0, "Alta": 1, "Complementaria": 2}
    for index, heading in enumerate(sprint_names):
        start = old.index(heading)
        next_heading = sprint_names[index + 1] if index + 1 < len(sprint_names) else "## Condiciones de la edición"
        section = old[start:old.index(next_heading, start)]
        records = []
        for line in section.splitlines():
            if not line.startswith("| **`HU-"):
                continue
            fields = split_row(line)
            assert len(fields) == 4, (heading, fields)
            match = re.search(r"`(HU-[A-Z]+-\d+)` — (.+?)\*\*<br>Origen: `(RF-[A-Z]+-\d+)`", fields[0])
            assert match, fields[0]
            hu_id, title, rf_id = match.groups()
            order = re.search(r"Prioridad propuesta: (\d+)/60", fields[3])
            deps = re.search(r"Dependencias: (.*)$", fields[3])
            assert order and deps and rf_id in mapped, hu_id
            level = mapped[rf_id]
            all_levels[hu_id] = level
            counts[level] += 1
            criteria = [re.sub(r"^\d+\. ", "", c.strip()) for c in fields[2].split("<br>")]
            records.append((level, int(order.group(1)), hu_id, title, rf_id, fields[1], criteria, deps.group(1)))
        records.sort(key=lambda row: (rank[row[0]], row[1]))
        body.extend([heading, "", "| Importancia | Historia | Necesidad resumida | Orden en pila |", "|---|---|---|---:|"])
        for level, order, hu_id, title, _rf_id, need, _criteria, _deps in records:
            summary = re.sub(r"^Como ([^,]+), quiero ", "", need).split(", para ")[0]
            summary = summary[0].upper() + summary[1:] if summary else title
            body.append(f"| **{level}** | `{hu_id}` · {title} | {summary} | {order}/60 |")
        body.append("")
        body.append("### Criterios y dependencias")
        body.append("")
        for level, order, hu_id, title, rf_id, need, criteria, deps in records:
            body.extend([
                f"#### {hu_id} — {title}",
                "",
                f"**Origen:** `{rf_id}` · **Importancia:** {level} · **Pila:** {order}/60 · "
                "**Estimación:** pendiente del equipo.",
                "",
                need,
                "",
                "**Aceptación:**",
                "",
            ])
            body.extend(f"{n}. {criterion}" for n, criterion in enumerate(criteria, 1))
            body.extend(["", f"**Dependencias:** {deps}.", ""])
    assert len(all_levels) == 51, len(all_levels)
    tail = old[old.index("## Condiciones de la edición"):]
    tail = tail.replace("## Historial de cambios", "## Historial de cambios")
    tail = tail.rstrip() + "\n| 2.4 | 2026-10-13 | Se separa importancia de posición en pila; se ordenan tablas por importancia y se conservan criterios, RF y dependencias. | Preparado; revisión académica pendiente |\n"
    body.append(tail)
    NEW_HU.write_text("\n".join(body).rstrip() + "\n", encoding="utf-8")
    return all_levels, counts


def build_sprint_backlog() -> None:
    old = OLD_SB.read_text(encoding="utf-8")
    old = old.replace('version: "1.0"', 'version: "1.1"', 1)
    old = old.replace("HU v2.3; HT v1.4; pila de producto v1.3; plan de sprints v1.1", "HU v2.4; HT v1.4; pila de producto v1.4; plan de sprints v1.2", 1)
    old = old.replace("pila_producto_v1.3_2026-10-13.md", "pila_producto_v1.4_2026-10-13.md")
    old = old.replace("pila de producto v1.3", "pila de producto v1.4")
    old = old.replace("plan_sprints_v1.1_2026-10-13.md", "plan_sprints_v1.2_2026-10-13.md")
    old = old.replace("La [pila de producto v1.3]", "La [pila de producto v1.4]")
    old = old.replace("## Criterio para seleccionar y cerrar trabajo", "La columna **prioridad de planificación** ordena la atención a la tarea; es propuesta y no sustituye la importancia de cada HU, visible en [historias de usuario v2.4](../historias/usuario/historias_usuario_v2.4_2026-10-13.md). Los IDs de tarea conservan la secuencia de dependencias.\n\n## Criterio para seleccionar y cerrar trabajo", 1)
    priorities = {
        "S1": ["Alta", "Esencial", "Alta", "Alta", "Alta"],
        "S2": ["Esencial", "Esencial", "Alta", "Alta"],
        "S3": ["Alta", "Alta", "Alta"],
        "S4": ["Esencial", "Esencial", "Alta", "Esencial"],
        "S5": ["Esencial", "Esencial", "Esencial", "Alta", "Alta", "Alta"],
        "S6": ["Alta", "Complementaria", "Complementaria", "Esencial", "Alta"],
    }
    lines = old.splitlines()
    output = []
    current = None
    in_table = False
    seen: dict[str, int] = {}
    for line in lines:
        heading = re.match(r"^## S([1-6])  ", line)
        if heading:
            current = f"S{heading.group(1)}"
            in_table = False
            seen[current] = 0
        elif line.startswith("## "):
            current = None
            in_table = False
        if current and line.startswith("| Tarea candidata |"):
            output.append("| Prioridad | Tarea y vínculos | Cierre verificable |")
            in_table = True
            continue
        if in_table and line.startswith("|---"):
            output.append("|---|---|---|")
            continue
        if in_table and line.startswith(f"| `SB-{current}-"):
            fields = split_row(line)
            assert len(fields) == 4, (current, fields)
            seen[current] += 1
            priority = priorities[current][seen[current] - 1]
            if current == "S1":
                task, ht, result, status = fields
                relation = ht
                evidence = f"{result}<br>Estado: {status.split(';')[0]}."
            else:
                task, hu, ht, result = fields
                relation = f"HU: {hu}<br>HT: {ht}"
                evidence = result
            output.append(f"| **{priority}** | {task}<br>{relation} | {evidence} |")
            continue
        if in_table and not line.startswith("|"):
            in_table = False
        output.append(line)
    assert seen == {"S1": 5, "S2": 4, "S3": 3, "S4": 4, "S5": 6, "S6": 5}, seen
    new = "\n".join(output).rstrip() + "\n"
    new += "| 1.1 | 2026-10-13 | Se ordenan tablas con prioridad visible, tarea y vínculos HU/HT en una sola columna y cierre separado. | Preparado; sin estimación ni compromiso. |\n"
    NEW_SB.write_text(new, encoding="utf-8")


def build_backlog(levels: dict[str, str], counts: Counter) -> None:
    old_path = DOCS / "pila_producto/pila_producto_v1.3_2026-10-13.md"
    new_path = DOCS / "pila_producto/pila_producto_v1.4_2026-10-13.md"
    old = old_path.read_text(encoding="utf-8")
    old = old.replace('version: "1.3"', 'version: "1.4"', 1)
    old = old.replace("orden-preliminar-por-validar", "orden-y-nivel-preliminares-por-validar", 1)
    old = old.replace("La posición 1 es el primer lugar en la secuencia", "Cada HU conserva la importancia propuesta de su RF de origen: Esencial, Alta o Complementaria. La posición 1 es el primer lugar en la secuencia", 1)
    marker = "## Nivel de prioridad de las nueve HT existentes"
    summary = (
        "## Importancia propuesta de las 51 historias de usuario\n\n"
        "Esta clasificación reproduce la [priorización de requisitos v1.2](../requisitos/priorizacion/priorizacion_requisitos_v1.2_2026-10-13.md). "
        "La tabla de cada sprint en [historias de usuario v2.4](../historias/usuario/historias_usuario_v2.4_2026-10-13.md) "
        "muestra el nivel de cada HU por separado de su posición en esta pila.\n\n"
        "| Nivel | HU | Lectura |\n|---|---:|---|\n"
        f"| Esencial | {counts['Esencial']} | Recorrido central, acceso o integridad. |\n"
        f"| Alta | {counts['Alta']} | Proceso acordado para la primera versión. |\n"
        f"| Complementaria | {counts['Complementaria']} | Consulta o comodidad dentro del alcance. |\n\n"
        "El orden 1–60 sigue siendo una propuesta de secuencia que también considera dependencias. "
        "No convierte una HU complementaria en esencial por aparecer antes ni aprueba cambios de alcance.\n\n"
    )
    old = old.replace(marker, summary + marker, 1)
    old = old.rstrip() + "\n| 1.4 | 2026-10-13 | Se añade la importancia cualitativa de HU separada del orden 1–60 y se enlazan las tablas por sprint. | Preparado; revisión pendiente. |\n"
    new_path.write_text(old, encoding="utf-8")


def build_sprint_plan() -> None:
    old_path = DOCS / "sprints/plan_sprints_v1.1_2026-10-13.md"
    new_path = DOCS / "sprints/plan_sprints_v1.2_2026-10-13.md"
    old = old_path.read_text(encoding="utf-8")
    old = old.replace('version: "1.1"', 'version: "1.2"', 1)
    old = old.replace("pila de producto v1.3", "pila de producto v1.4")
    start = old.index("## Hitos y documentación")
    end = old.index("Las pruebas parciales", start)
    replacement = """## Sprints y resultados previstos

Esta tabla sirve para ubicar el trabajo. La prioridad de cada tarea y sus HU/HT
se consultan en el [sprint backlog v1.1](sprint_backlog_v1.1_2026-10-13.md);
la importancia de cada HU se consulta en [historias de usuario v2.4](../historias/usuario/historias_usuario_v2.4_2026-10-13.md).

| Etapa | Fechas | Trabajo principal | Evidencia prevista al cierre |
|---|---|---|---|
| S1 | 15 sep–12 oct | Requisitos, decisiones, arquitectura, interfaz y pila. | Fuentes, catálogo, diseño y pendientes con estado real; revisión aún por registrar. |
| S2 | 13–26 oct | Acceso privado, cuentas y permisos. | Pruebas de entrada y denegación, revisión y retrospectiva. |
| S3 | 27 oct–9 nov | Actividades, responsables y encargos. | Flujo probado, permisos y regresión de S2. |
| S4 | 10–23 nov | Asistencia, participación y continuidad aprobada. | Historial, pruebas de corte y reintento solo con decisiones cerradas. |
| S5 | 24 nov–7 dic | Materia prima, secado, lotes y existencias; comercio según capacidad. | Conciliación de movimientos, cifras y regresión; alcance real registrado. |
| S6 | 8–21 dic | Reportes, contenido autorizado e integración. | Pruebas funcionales y de uso, defectos, manuales y preparación de validación. |
| Cierre | 22–23 dic | Validación y entrega según resultado real. | Acta, capacitación si ocurre, versión final y pendientes explícitos. |

"""
    old = old[:start] + replacement + old[end:]
    old = old.replace("El [sprint backlog v1.0](sprint_backlog_v1.0_2026-10-13.md)", "El [sprint backlog v1.1](sprint_backlog_v1.1_2026-10-13.md)")
    old = old.rstrip() + "\n| 1.2 | 2026-10-13 | Se separan fechas, trabajo y evidencia en la tabla; se enlazan prioridades y tareas vigentes. | Preparado; revisión pendiente. |\n"
    new_path.write_text(old, encoding="utf-8")


if __name__ == "__main__":
    levels, counts = build_hu()
    build_sprint_backlog()
    build_backlog(levels, counts)
    build_sprint_plan()
    print("HU", len(levels), dict(counts))
    print("archivos", NEW_HU, NEW_SB)
