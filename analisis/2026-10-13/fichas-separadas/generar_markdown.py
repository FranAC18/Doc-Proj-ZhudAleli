from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(r"F:\Tesis\App Tesis")
DOC = ROOT / "documentacion"


def read(path: str) -> str:
    return (DOC / path).read_text(encoding="utf-8")


def write(path: str, lines: list[str]) -> None:
    dest = DOC / path
    dest.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def plain(value: str) -> str:
    return value.replace("**", "").replace("`", "").strip()


def cell(value: str) -> str:
    return value.replace("|", "\\|").replace("\n", "<br>").strip()


@dataclass
class UserStory:
    number: int
    code: str
    title: str
    sprint: str
    actor: str
    need: str
    priority: str
    position: str
    origin: str
    criteria: list[str]
    dependencies: str


@dataclass
class TechStory:
    number: int
    code: str
    title: str
    priority: str
    sprint: str
    description: str
    related: str
    exit: str
    status: str
    kind: str = "Trabajo técnico"
    tasks: str = "Pendiente de desglosar"
    test: str = "Pendiente de ejecución"
    dependencies: str = "Por confirmar"


@dataclass
class Task:
    number: int
    code: str
    title: str
    sprint: str
    priority: str
    user_stories: str
    tech_stories: str
    result: str
    status: str


def user_stories() -> list[UserStory]:
    source = read("historias/usuario/historias_usuario_v2.4_2026-10-13.md")
    matches = list(re.finditer(r"^#### (HU-[A-Z]+-\d+) — (.+)$", source, re.M))
    result = []
    for n, match in enumerate(matches, 1):
        code, title = match.groups()
        chunk = source[match.end():matches[n].start() if n < len(matches) else source.index("## Condiciones de la edición")]
        preceding = source[:match.start()]
        section = re.findall(r"^## (Sprint [2-6].*|Continuidad transversal)$", preceding, re.M)[-1]
        sprint = "S4–S5 (transversal)" if section == "Continuidad transversal" else "S" + re.search(r"Sprint (\d)", section).group(1)
        origin = re.search(r"\*\*Origen:\*\* `(RF-[A-Z]+-\d+)`", chunk).group(1)
        priority = re.search(r"\*\*Importancia:\*\* (Esencial|Alta|Complementaria)", chunk).group(1)
        position = re.search(r"\*\*Pila:\*\* (\d+/60)", chunk).group(1)
        need = re.search(r"^(Como .+)$", chunk, re.M).group(1)
        actor = re.search(r"^Como (.+?), quiero ", need).group(1)
        criteria = re.findall(r"^\d+\. (.+)$", chunk, re.M)
        dependencies = re.search(r"\*\*Dependencias:\*\* (.+)$", chunk, re.M).group(1).rstrip(".")
        result.append(UserStory(n, code, title, sprint, actor, need, priority, position, origin, criteria, dependencies))
    assert len(result) == 51
    assert len({x.code for x in result}) == 51
    return result


def tech_stories() -> list[TechStory]:
    base = read("historias/tecnicas/historias_tecnicas_v1.3_2026-10-12.md")
    current = read("historias/tecnicas/historias_tecnicas_v1.4_2026-10-13.md")
    priority_by_code = {}
    for line in current.splitlines():
        match = re.match(r"^\| \d+ \| `(HT-GEN-\d+)` .+? \| (Crítica|Alta|Media|Baja) \| (.+?) \| (.+?) \|$", line)
        if match:
            priority_by_code[match.group(1)] = (match.group(2), match.group(3), match.group(4))
    criteria_by_code = {}
    for line in base.splitlines():
        if re.match(r"^\| `HT-GEN-\d+` \|", line):
            parts = [part.strip() for part in line.strip().strip("|").split("|")]
            assert len(parts) == 4
            criteria_by_code[plain(parts[0])] = parts[1:]
    stories = []
    for line in base.splitlines():
        if not line.startswith("| **`HT-GEN-"):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        assert len(parts) == 4
        match = re.search(r"`(HT-GEN-\d+)` — (.+?)\*\*", parts[0])
        assert match
        code, title = match.groups()
        kind_raw, detail = plain(parts[1]).split("<br>", 1)
        kind = kind_raw.removeprefix("Tipo:").strip().rstrip(".")
        dep = plain(parts[3])
        criteria, tasks, test = criteria_by_code[code]
        priority, sprint, relation = priority_by_code[code]
        stories.append(TechStory(len(stories)+1, code, title, priority, sprint, detail.strip(), relation, plain(criteria).replace("<br>", "\n"), "Línea base", kind, plain(tasks), plain(test), dep))
    assert len(stories) == 9
    proposal_section = current.split("## Diez historias técnicas nuevas para estudiar y estimar", 1)[1].split("## Condiciones para pasar", 1)[0]
    for line in proposal_section.splitlines():
        if not re.match(r"^\| \d+ \| `HT-", line):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        assert len(parts) == 5
        match = re.search(r"`(HT-[A-Z0-9-]+)` · (.+?) · (Crítica|Alta|Media|Baja)", parts[1])
        assert match, parts[1]
        code, sprint, priority = match.groups()
        stories.append(TechStory(len(stories)+1, code, parts[2], priority, sprint, parts[2], parts[3], parts[4], "Propuesta"))
    assert len(stories) == 19
    return stories


def tasks() -> list[Task]:
    source = read("sprints/sprint_backlog_v1.1_2026-10-13.md")
    result = []
    for line in source.splitlines():
        if not re.match(r"^\| \*\*(Esencial|Alta|Complementaria)\*\* \| `SB-S", line):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        assert len(parts) == 3
        priority = plain(parts[0])
        chunks = parts[1].split("<br>")
        match = re.match(r"`(SB-S([1-6])-\d+)` (.+)$", chunks[0])
        assert match, chunks[0]
        code, sprint_num, title = match.groups()
        links = " ".join(chunks[1:])
        hu = ", ".join(dict.fromkeys(re.findall(r"HU-[A-Z]+-\d+", links)))
        ht = ", ".join(dict.fromkeys(re.findall(r"HT-[A-Z0-9]+-\d+", links)))
        if not hu:
            hu = "Referencia a todas las HU" if sprint_num == "1" else plain(links.split("HT:", 1)[0]) or "Por seleccionar"
        if not ht:
            ht = "Por seleccionar"
        status = "Candidata; sin estimación ni responsable"
        evidence = plain(parts[2]).replace("<br>", " ")
        if sprint_num == "1" and "Estado: " in evidence:
            evidence, detail = evidence.split("Estado: ", 1)
            status = detail.strip().rstrip(".")
        result.append(Task(len(result)+1, code, title.rstrip("."), "S" + sprint_num, priority, hu, ht, evidence.strip(), status))
    assert len(result) == 27
    return result


def two_col(title: str, fields: list[tuple[str, str]]) -> list[str]:
    out = [f"### {title}", "", "| Campo | Dato |", "|---|---|"]
    out.extend(f"| **{label}** | {cell(value)} |" for label, value in fields)
    out.append("")
    return out


def make_users(stories: list[UserStory]) -> None:
    out = [
        "---", "titulo: Historias de usuario en fichas", 'version: "2.5"', "fecha: 2026-10-13", "autor: Tesista",
        "estado: final-documental-con-prioridad-propuesta", "historias: 51", "estimacion: pendiente-del-equipo",
        "revision_directora: pendiente", "publicacion: pendiente-de-confirmacion", "---", "",
        "# Historias de usuario", "",
        "Cada historia tiene su propia ficha, con los campos separados como en el formato de referencia aportado por el tesista. "
        "El **número** facilita leerlas; el **código HU** conserva la trazabilidad con requisitos, pila y pruebas. "
        "La prioridad es una propuesta tomada de [la clasificación de requisitos](../../requisitos/priorizacion/priorizacion_requisitos_v1.2_2026-10-13.md). "
        "Los puntos, el riesgo y el responsable se dejan pendientes porque todavía no hay una estimación o asignación validada.", "",
    ]
    current = None
    for story in stories:
        if story.sprint != current:
            current = story.sprint
            out.extend([f"## Sprint {current.removeprefix('S')}" if current.startswith("S") and "–" not in current else "## Trabajo transversal", ""])
        out.extend(two_col(f"Historia {story.number} — {story.title}", [
            ("Número", str(story.number)), ("Código de referencia", f"`{story.code}`"),
            ("Usuario", story.actor), ("Nombre de la historia", story.title),
            ("Prioridad en negocio", story.priority + " (propuesta)"),
            ("Riesgo en desarrollo", "Pendiente de evaluar"), ("Puntos estimados", "Pendiente de estimar"),
            ("Sprint propuesto", story.sprint), ("Responsable", "Pendiente de asignar"),
            ("Descripción", story.need),
            ("Criterios de aceptación", "\n".join(f"{i}. {criterion}" for i, criterion in enumerate(story.criteria, 1))),
            ("Requisito de origen", f"`{story.origin}`"),
            ("Dependencias", story.dependencies),
            ("Observaciones", f"Posición propuesta en la pila: {story.position}. Revisión académica pendiente."),
        ]))
    out.extend(["## Condiciones", "", "Las 51 historias proceden de RF confirmados. Los nueve temas de la entrevista permanecen como exploración en la [edición anterior](historias_usuario_v2.4_2026-10-13.md); no tienen estimación ni sprint comprometido. Ninguna ficha acredita implementación o prueba.", "", "## Historial de cambios", "", "| Versión | Fecha | Cambio |", "|---|---|---|", "| 2.4 | 2026-10-13 | Tablas resumidas por prioridad y criterios por sección. |", "| 2.5 | 2026-10-13 | Ficha individual por historia, con campos separados como la referencia visual. |", ""])
    write("historias/usuario/historias_usuario_v2.5_2026-10-13.md", out)


def make_tech(stories: list[TechStory]) -> None:
    out = [
        "---", "titulo: Historias técnicas en fichas", 'version: "1.5"', "fecha: 2026-10-13", "autor: Tesista",
        "estado: final-documental-con-propuestas-identificadas", "historias_base: 9", "historias_nuevas_propuestas: 10",
        "estimacion: pendiente-del-equipo", "revision_directora: pendiente", "publicacion: pendiente-de-confirmacion", "---", "",
        "# Historias técnicas", "",
        "Cada historia técnica se presenta en una ficha separada. Las nueve historias de línea base conservan sus criterios de la [edición detallada v1.3](historias_tecnicas_v1.3_2026-10-12.md). Las diez nuevas siguen siendo **propuestas**; su presencia aquí no cambia los requisitos aprobados. Prioridades, riesgos, puntos y responsables se revisan al preparar cada sprint.", "",
    ]
    current = None
    for story in stories:
        if story.status != current:
            current = story.status
            out.extend(["## Historias técnicas de la línea base" if current == "Línea base" else "## Historias técnicas propuestas", ""])
        out.extend(two_col(f"Historia técnica {story.number} — {story.title}", [
            ("Número", str(story.number)), ("Código de referencia", f"`{story.code}`"),
            ("Nombre", story.title), ("Tipo", story.kind),
            ("Prioridad técnica", story.priority + " (propuesta)"),
            ("Riesgo en desarrollo", "Pendiente de evaluar"), ("Puntos estimados", "Pendiente de estimar"),
            ("Sprint propuesto", story.sprint), ("Responsable", "Pendiente de asignar"),
            ("Descripción", story.description), ("Relación con HU o fuentes", story.related),
            ("Criterios de salida", story.exit), ("Tareas", story.tasks),
            ("Prueba prevista", story.test), ("Dependencias", story.dependencies),
            ("Estado", story.status),
        ]))
    out.extend(["## Historial de cambios", "", "| Versión | Fecha | Cambio |", "|---|---|---|", "| 1.4 | 2026-10-13 | Clasificación y relación con S1–S6. |", "| 1.5 | 2026-10-13 | Ficha individual con campos separados para 9 HT de base y 10 propuestas. |", ""])
    write("historias/tecnicas/historias_tecnicas_v1.5_2026-10-13.md", out)


def make_tasks(items: list[Task]) -> None:
    out = [
        "---", "titulo: Sprint backlog en fichas", 'version: "1.2"', "fecha: 2026-10-13", "autor: Tesista",
        "estado: plan-preliminar-sin-compromiso-de-capacidad", "tareas: 27", "estimacion: pendiente-del-equipo",
        "revision_directora: pendiente", "publicacion: pendiente-de-confirmacion", "---", "",
        "# Sprint backlog", "",
        "**Qué significa el código:** `SB-S3-01` es la referencia interna de la tarea 01 del backlog del Sprint 3. "
        "En las fichas se muestra primero **Tarea 1, Tarea 2…**; el código queda en un campo aparte para mantener la trazabilidad. "
        "Cada campo ocupa su propia fila. La prioridad de la tarea es propuesta y distinta de la prioridad de cada HU.", "",
        "Las fechas y objetivos generales están en el [plan de sprints](plan_sprints_v1.2_2026-10-13.md). "
        "Las HU y HT completas están en las [historias de usuario](../historias/usuario/historias_usuario_v2.5_2026-10-13.md) y [técnicas](../historias/tecnicas/historias_tecnicas_v1.5_2026-10-13.md). "
        "Antes de comprometer tareas faltan estimación, responsable, decisiones materiales y capacidad disponible.", "",
    ]
    current = None
    local_number = 0
    for task in items:
        if task.sprint != current:
            current = task.sprint
            local_number = 0
            out.extend([f"## Sprint {current.removeprefix('S')}", ""])
        local_number += 1
        out.extend(two_col(f"Tarea {local_number} — {task.title}", [
            ("Número de tarea", str(local_number)), ("Código de referencia", f"`{task.code}`"),
            ("Sprint", task.sprint), ("Nombre", task.title),
            ("Prioridad de planificación", task.priority + " (propuesta)"),
            ("Historia de usuario relacionada", task.user_stories),
            ("Historia técnica relacionada", task.tech_stories),
            ("Resultado o prueba esperada", task.result),
            ("Estimación", "Pendiente del equipo"), ("Responsable", "Pendiente de asignar"),
            ("Estado", task.status),
        ]))
    out.extend(["## Condiciones de cierre", "", "Una tarea se cierra únicamente con el resultado o prueba realizado y registrado. S1 tiene documentación parcial y decisiones pendientes. Ningún sprint de desarrollo está demostrado como terminado; las tareas de S2–S6 son candidatas sujetas a capacidad, estimación y reglas aprobadas.", "", "## Historial de cambios", "", "| Versión | Fecha | Cambio |", "|---|---|---|", "| 1.1 | 2026-10-13 | Tablas de tareas con prioridad, vínculos y cierre. |", "| 1.2 | 2026-10-13 | Ficha individual por tarea; código interno trasladado a campo secundario. |", ""])
    write("sprints/sprint_backlog_v1.2_2026-10-13.md", out)


def make_pile(users: list[UserStory], tech: list[TechStory]) -> None:
    old = read("pila_producto/pila_producto_v1.4_2026-10-13.md")
    user_map = {s.code: s for s in users}
    tech_map = {s.code: s for s in tech}
    rows = []
    for line in old.splitlines():
        if not re.match(r"^\| \d+ \|", line):
            continue
        parts = [part.strip() for part in line.strip().strip("|").split("|")]
        if len(parts) != 6:
            continue
        order = int(parts[0])
        code_match = re.search(r"(?:HU|HT)-[A-Z]+-\d+", parts[1])
        if code_match is None:
            continue
        code = code_match.group()
        name = parts[2]
        stage = parts[3]
        kind = "Usuario" if code.startswith("HU-") else "Técnica"
        priority = user_map[code].priority if kind == "Usuario" else tech_map[code].priority
        rows.append((order, code, kind, name, priority, stage))
        if len(rows) == 60:
            break
    assert [r[0] for r in rows] == list(range(1, 61)), [r[0] for r in rows]
    out = [
        "---", "titulo: Pila de producto con campos separados", 'version: "1.5"', "fecha: 2026-10-13", "autor: Tesista",
        "estado: final-documental-con-prioridades-propuestas", "elementos_base: 60", "historias_usuario: 51",
        "historias_tecnicas: 9", "estimacion: pendiente-del-equipo", "revision_directora: pendiente",
        "publicacion: pendiente-de-confirmacion", "---", "", "# Pila de producto", "",
        "La pila contiene 51 historias de usuario y 9 técnicas de la línea base. Cada columna muestra **un solo dato**. "
        "El número es el orden propuesto, mientras que la prioridad expresa importancia (HU) o urgencia técnica (HT); son medidas distintas. "
        "Los detalles y dependencias están en las fichas de [HU](../historias/usuario/historias_usuario_v2.5_2026-10-13.md) y [HT](../historias/tecnicas/historias_tecnicas_v1.5_2026-10-13.md). Ninguna fila equivale a trabajo comprometido o terminado.", "",
        "## Línea base ordenada", "", "| N.º | Código | Tipo | Nombre | Prioridad propuesta | Sprint previsto |", "|---:|---|---|---|---|---|",
    ]
    out.extend(f"| {order} | `{code}` | {kind} | {cell(name)} | {priority} | {cell(stage)} |" for order, code, kind, name, priority, stage in rows)
    out.extend(["", "## Diez historias técnicas en propuesta", "", "Estas historias ayudan a planificar levantamiento, diseño, integración y cierre. **No forman parte de las 60 posiciones** ni se incorporan como aprobadas por figurar aquí.", "", "| N.º | Código | Nombre | Prioridad propuesta | Sprint previsto | Estado |", "|---:|---|---|---|---|---|"])
    for i, story in enumerate(tech[9:], 1):
        out.append(f"| {i} | `{story.code}` | {cell(story.title)} | {story.priority} | {story.sprint} | Propuesta |")
    out.extend(["", "## Pendientes para planificar", "", "Las reglas P-02 a P-14, la revisión académica, la estimación y la capacidad se registran antes de comprometer una historia. Las necesidades adicionales de entrevista permanecen en la [edición anterior](pila_producto_v1.4_2026-10-13.md) hasta que se validen. El orden puede cambiar con una decisión humana registrada.", "", "## Historial de cambios", "", "| Versión | Fecha | Cambio |", "|---|---|---|", "| 1.4 | 2026-10-13 | Nivel cualitativo de HU separado de posición en pila. |", "| 1.5 | 2026-10-13 | Columnas independientes y lista aparte para las diez HT propuestas. |", ""])
    write("pila_producto/pila_producto_v1.5_2026-10-13.md", out)


if __name__ == "__main__":
    users = user_stories()
    tech = tech_stories()
    sprint_tasks = tasks()
    make_users(users)
    make_tech(tech)
    make_tasks(sprint_tasks)
    make_pile(users, tech)
    print("HU", len(users), "HT", len(tech), "tareas", len(sprint_tasks))
