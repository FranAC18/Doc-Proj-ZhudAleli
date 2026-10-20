from __future__ import annotations

import importlib.util
from pathlib import Path

from docx import Document
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.shared import Cm
from docx.shared import Pt, RGBColor


ROOT = Path(r"F:\Tesis\App Tesis")
MODULE = ROOT / "analisis/2026-10-13/fichas-separadas/generar_markdown.py"
HELPERS = ROOT / "analisis/2026-10-13/plan-incremental-docx/build_plan_v1_1.py"
OUTPUT_STORIES = ROOT / "documentacion/historias/historias_usuario_tecnicas_pila_v1.2_2026-10-13.docx"
OUTPUT_SPRINTS = ROOT / "documentacion/sprints/plan_incremental_y_sprint_backlog_v1.6_2026-10-13.docx"


def module_from(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    import sys
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


model = module_from(MODULE, "separated_cards")
helpers = module_from(HELPERS, "academic_helpers")


def start(title: str) -> Document:
    doc = Document(helpers.REFERENCE)
    for paragraph in list(doc.paragraphs)[15:]:
        paragraph._element.getparent().remove(paragraph._element)
    doc.paragraphs[6].text = title
    doc.paragraphs[8].text = "Aplicación web para la gestión organizacional del Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud"
    doc.paragraphs[14].text = "13 de octubre de 2026"
    for index in (6, 8, 14):
        paragraph = doc.paragraphs[index]
        paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in paragraph.runs:
            run.bold = True
            run.font.name = "Century Gothic"
            run.font.size = Pt(9 if index == 8 else 10)
            run.font.color.rgb = RGBColor(0, 0, 0)
    # La plantilla de referencia incluye un segundo estudiante que no es autor.
    for paragraph in list(doc.paragraphs):
        if "Jordy Caranqui" in paragraph.text:
            paragraph._element.getparent().remove(paragraph._element)
    doc.add_page_break()
    paragraph = doc.add_paragraph(title, style="Title")
    paragraph.paragraph_format.space_after = Pt(10)
    return doc


def add_card(doc: Document, title: str, fields: list[tuple[str, str]]) -> None:
    values = dict(fields)
    if title.startswith("Historia de usuario"):
        layout = [
            ("Número", "Usuario"), ("Código", "Requisito"), ("Nombre",),
            ("Prioridad", "Riesgo"), ("Puntos", "Sprint"),
            ("Responsable",), ("Descripción",), ("Aceptación",),
            ("Dependencias",), ("Observaciones",),
        ]
    elif title.startswith("Historia técnica"):
        layout = [
            ("Número", "Código"), ("Nombre",), ("Tipo", "Estado"),
            ("Prioridad", "Riesgo"), ("Puntos", "Sprint"),
            ("Responsable",), ("Descripción",), ("Relación",),
            ("Criterio de salida",), ("Tareas",), ("Prueba prevista",),
            ("Dependencias",),
        ]
    else:
        layout = [
            ("Número", "Código"), ("Sprint", "Prioridad"),
            ("Nombre",), ("Historia de usuario",),
            ("Historia técnica",), ("Resultado o prueba",),
            ("Puntos", "Responsable"), ("Estado",),
        ]
    table = doc.add_table(rows=1, cols=4)
    table.autofit = False
    widths = [2.25, 5.25, 2.25, 5.25]
    for column, width in zip(table.columns, widths):
        column.width = Cm(width)
    header = table.rows[0].cells[0].merge(table.rows[0].cells[3])
    helpers.write_cell(header, title, bold=True, white=True, size=8.2)
    helpers.shade(header, "404040")
    helpers.no_split(table.rows[0])
    for labels in layout:
        row = table.add_row()
        helpers.no_split(row)
        if len(labels) == 2:
            ordered = [(0, labels[0], True), (1, values[labels[0]], False),
                       (2, labels[1], True), (3, values[labels[1]], False)]
        else:
            merged = row.cells[1].merge(row.cells[3])
            ordered = [(0, labels[0], True), (1, values[labels[0]], False)]
            row.cells[0].width = Cm(widths[0])
            merged.width = Cm(sum(widths[1:]))
        for index, value, bold in ordered:
            target = row.cells[index]
            helpers.write_cell(target, value, bold=bold, size=7.8)
            tc_mar = target._tc.get_or_add_tcPr().find(qn("w:tcMar"))
            for side, amount in (("top", 45), ("bottom", 45), ("left", 75), ("right", 75)):
                tc_mar.find(qn(f"w:{side}")).set(qn("w:w"), str(amount))
        if len(table.rows) % 2:
            for cell in row.cells:
                helpers.shade(cell, "F7F7F7")
    for row in table.rows[:-1]:
        for table_cell in row.cells:
            for paragraph in table_cell.paragraphs:
                paragraph.paragraph_format.keep_with_next = True
    spacer = doc.add_paragraph()
    spacer.paragraph_format.space_after = Pt(1)


def build_stories() -> None:
    users = model.user_stories()
    tech = model.tech_stories()
    pile = model.read("pila_producto/pila_producto_v1.5_2026-10-13.md")
    doc = start("Historias de usuario, técnicas y pila de producto")
    helpers.body(doc, "Versión 1.2 · 13 de octubre de 2026 · Autor: Franklin Acero · Estado: revisión académica pendiente")
    helpers.heading(doc, "INTRODUCCIÓN")
    helpers.body(doc, "Esta edición reúne 51 historias de usuario, 9 historias técnicas de línea base, 10 técnicas propuestas y la pila de producto. Cada historia ocupa una ficha propia con un campo por fila, siguiendo el formato mostrado por el tesista. Los códigos HU y HT quedan como referencias secundarias para relacionar requisitos y pruebas.")
    helpers.body(doc, "Las prioridades son propuestas. El riesgo, los puntos y el responsable aparecen como pendientes porque no existe una evaluación o asignación validada. Una ficha no acredita implementación. Las diez técnicas nuevas están fuera de las 60 posiciones de la pila base.")
    helpers.heading(doc, "HISTORIAS DE USUARIO")
    current = None
    for story in users:
        if story.sprint != current:
            current = story.sprint
            helpers.heading(doc, "TRABAJO TRANSVERSAL" if "–" in current else f"SPRINT {current.removeprefix('S')}", 2)
        add_card(doc, f"Historia de usuario {story.number}  {story.title}", [
            ("Número", str(story.number)), ("Código", story.code),
            ("Usuario", story.actor), ("Nombre", story.title),
            ("Prioridad", story.priority + "  propuesta"),
            ("Riesgo", "Pendiente de evaluar"), ("Puntos", "Pendiente de estimar"),
            ("Sprint", story.sprint), ("Responsable", "Pendiente de asignar"),
            ("Descripción", story.need),
            ("Aceptación", "\n".join(f"{i}. {criterion}" for i, criterion in enumerate(story.criteria, 1))),
            ("Requisito", story.origin), ("Dependencias", story.dependencies),
            ("Observaciones", f"Posición de pila: {story.position}. Revisión académica pendiente."),
        ])
    helpers.heading(doc, "HISTORIAS TÉCNICAS")
    current = None
    for story in tech:
        if story.status != current:
            current = story.status
            helpers.heading(doc, "LÍNEA BASE" if current == "Línea base" else "PROPUESTAS PARA REVISIÓN", 2)
        add_card(doc, f"Historia técnica {story.number}  {story.title}", [
            ("Número", str(story.number)), ("Código", story.code),
            ("Nombre", story.title), ("Tipo", story.kind),
            ("Prioridad", story.priority + "  propuesta"),
            ("Riesgo", "Pendiente de evaluar"), ("Puntos", "Pendiente de estimar"),
            ("Sprint", story.sprint), ("Responsable", "Pendiente de asignar"),
            ("Descripción", story.description), ("Relación", story.related),
            ("Criterio de salida", story.exit), ("Tareas", story.tasks),
            ("Prueba prevista", story.test), ("Dependencias", story.dependencies),
            ("Estado", story.status),
        ])
    helpers.heading(doc, "PILA DE PRODUCTO")
    helpers.body(doc, "El número indica orden de trabajo propuesto, y la prioridad indica importancia de negocio para HU o urgencia técnica para HT. Los elementos 1–60 forman la base; los diez técnicos adicionales permanecen en propuesta.")
    base_rows = []
    proposal_rows = []
    active = False
    for line in pile.splitlines():
        if line == "## Línea base ordenada":
            active = True
            continue
        if line == "## Diez historias técnicas en propuesta":
            active = False
        if not line.startswith("| ") or not line[2:3].isdigit():
            continue
        parts = [x.strip().replace("`", "") for x in line.strip().strip("|").split("|")]
        if active and len(parts) == 6:
            base_rows.append([parts[0], parts[1], parts[3], parts[4], parts[5]])
        elif not active and len(parts) == 6 and parts[1].startswith("HT-"):
            proposal_rows.append([parts[0], parts[1], parts[2], parts[3], parts[4]])
    assert len(base_rows) == 60 and len(proposal_rows) == 10
    helpers.add_table(doc, ["N.º", "Código", "Nombre", "Prioridad", "Sprint"], base_rows, [1.0, 2.6, 6.6, 2.8, 2.0], size=7.7)
    helpers.heading(doc, "TÉCNICAS AÚN PROPUESTAS", 2)
    helpers.add_table(doc, ["N.º", "Código", "Nombre", "Prioridad", "Sprint"], proposal_rows, [1.0, 2.6, 6.6, 2.8, 2.0], size=7.7)
    helpers.heading(doc, "FUENTES E HISTORIAL")
    helpers.body(doc, "Fuentes: CAT-REQ-001 v1.1; clasificación de requisitos v1.2; HU v2.5; HT v1.5; pila v1.5; Gantt y fechas aportados por el tesista. Formato visual basado en 7402_alcance.docx y la ficha de historia aportada posteriormente.")
    helpers.body(doc, "Historial: v1.0, primer compendio Word con numeración anterior. v1.1, fichas individuales y calendario S1–S6, con campos separados y prioridades propuestas. v1.2, corrección de autoría. Publicación pendiente de confirmación.")
    doc.core_properties.title = "Historias de usuario, técnicas y pila de producto"
    doc.core_properties.author = "Franklin Acero"
    doc.save(OUTPUT_STORIES)
    print(OUTPUT_STORIES)


def build_sprints() -> None:
    tasks = model.tasks()
    doc = start("Plan incremental y sprint backlog")
    helpers.body(doc, "Versión 1.6 · 13 de octubre de 2026 · Autor: Franklin Acero · Estado: revisión académica pendiente")
    helpers.heading(doc, "INTRODUCCIÓN")
    helpers.body(doc, "El plan mantiene S1 para requisitos y diseño del 15 de septiembre al 12 de octubre, S2–S6 para desarrollo desde el 13 de octubre y cierre el 22 y 23 de diciembre. Las 27 tareas son candidatas. Cada tarea tiene una ficha con prioridad, historia de usuario, historia técnica, resultado y estado en filas independientes.")
    helpers.body(doc, "SB-S3-01 significa tarea 01 del sprint backlog del Sprint 3. Es un código de trazabilidad; en las fichas el número de tarea y su nombre son lo principal. Puntos, responsable y capacidad siguen pendientes. El documento compañero de historias contiene las 51 HU, 19 HT y pila detallada.")
    helpers.heading(doc, "RESUMEN DE SPRINTS")
    helpers.body(doc, "Cada fila resume el trabajo candidato del sprint. El número cuenta tareas del sprint backlog, no historias terminadas. S1 corresponde a requisitos y diseño; S2 inicia el desarrollo el 13 de octubre. Las fechas completas suman 100 días hasta el cierre del 23 de diciembre.")
    summary = [
        ["S1", "15 sep–12 oct", "5", "Requisitos, decisiones y diseño preparados para revisión"],
        ["S2", "13–26 oct", "4", "Acceso privado, cuentas y permisos verificables"],
        ["S3", "27 oct–9 nov", "3", "Actividades, responsables y encargos vinculados"],
        ["S4", "10–23 nov", "4", "Asistencia y participación; continuidad según decisiones"],
        ["S5", "24 nov–7 dic", "6", "Producción, existencias y rendición según capacidad"],
        ["S6", "8–21 dic", "5", "Reportes, contenido autorizado e integración"],
        ["Cierre", "22–23 dic", "—", "Validación y entrega de lo efectivamente completado"],
    ]
    assert [sum(t.sprint == f"S{i}" for t in tasks) for i in range(1, 7)] == [5, 4, 3, 4, 6, 5]
    helpers.add_table(doc, ["Sprint", "Fechas de 2026", "Tareas", "Resultado previsto"], summary, [1.55, 3.2, 1.55, 8.7], size=8.1)
    helpers.heading(doc, "RELACIÓN CON HISTORIAS Y PILA", 2)
    helpers.body(doc, "Los códigos permiten localizar cada historia en la pila de producto y en las fichas siguientes. Los intervalos incluyen todos los números entre sus extremos. Las historias HT-PRE y HT-S3 a HT-S6 son propuestas técnicas; requieren revisión antes de comprometerse.")
    helpers.add_table(doc, ["Sprint", "Historias de usuario relacionadas", "Historias técnicas relacionadas"], [
        ["S1", "Todas las HU; HU-PWA-001 de forma explícita", "HT-PRE-001–005; HT-GEN-008"],
        ["S2", "HU-ACC-001–004", "HT-GEN-001, 002, 004, 009"],
        ["S3", "HU-PLA-001–005; HU-CAT-001", "HT-GEN-002, 009; HT-S3-001"],
        ["S4", "HU-ASI-001–007; HU-PWA-001–003", "HT-GEN-002, 003, 005, 006, 009; HT-S4-001"],
        ["S5", "HU-CAT-001; HU-INV-001–004; HU-TRA-001–005; HU-VEN-001–008; HU-GAS-001–002; HU-CXC-001–003", "HT-GEN-003; HT-S5-001"],
        ["S6", "HU-REP-001–006; HU-NOT-001; HU-PUB-001–002; recorridos entregados de S2–S5", "HT-GEN-002, 004, 007, 008, 009; HT-S6-001, 002"],
    ], [1.55, 8.2, 5.25], size=7.8)
    helpers.heading(doc, "EVIDENCIA Y CONDICIONES DE CIERRE", 2)
    helpers.add_table(doc, ["Sprint", "Qué se comprobaría al terminar", "Condición pendiente"], [
        ["S1", "Fuentes, catálogo, decisiones y diseño con estado real", "Revisión académica y estimación"],
        ["S2", "Entrada, salida, denegación y permisos probados", "Capacidad y responsables"],
        ["S3", "Actividades y encargos probados; regresión de S2", "Reglas y permisos del flujo"],
        ["S4", "Asistencia, participación y reintentos comprobados", "P-03 y, para trabajo sin red, P-13/P-14"],
        ["S5", "Movimientos y cifras conciliados; regresión", "Capacidad y reglas comerciales"],
        ["S6", "Reportes, uso e integración probados; defectos registrados", "Contenido autorizado y usuarias disponibles"],
        ["Cierre", "Acta, capacitación si ocurre y pendientes explícitos", "Validación de la entrega real"],
    ], [1.55, 7.3, 6.15], size=7.8)
    helpers.body(doc, "Estas tablas orientan la planificación. La selección real se fija cuando se revisen estimaciones, dependencias, capacidad y decisiones abiertas. Una fecha o una historia vinculada no acredita implementación.")
    current = None
    local_number = 0
    for task in tasks:
        if task.sprint != current:
            current = task.sprint
            local_number = 0
            helpers.heading(doc, f"SPRINT {current.removeprefix('S')}")
        local_number += 1
        add_card(doc, f"Tarea {local_number}  {task.title}", [
            ("Número", str(local_number)), ("Código", task.code),
            ("Sprint", task.sprint), ("Nombre", task.title),
            ("Prioridad", task.priority + "  propuesta"),
            ("Historia de usuario", task.user_stories),
            ("Historia técnica", task.tech_stories),
            ("Resultado o prueba", task.result),
            ("Puntos", "Pendiente de estimar"),
            ("Responsable", "Pendiente de asignar"),
            ("Estado", task.status),
        ])
    helpers.heading(doc, "CONDICIONES DE CIERRE")
    helpers.body(doc, "Las decisiones abiertas, la estimación y la capacidad limitan la selección real. S1 tiene documentación parcial; ningún sprint de desarrollo se declara terminado. S4 no presupone multas automáticas mientras P-03 siga abierta; las operaciones sin red dependen de P-13 y P-14. S5 se ajusta a la capacidad y a las reglas comerciales resueltas. La validación con usuarias y capacitación se registran cuando ocurran.")
    helpers.heading(doc, "FUENTES E HISTORIAL")
    helpers.body(doc, "Fuentes: Gantt y fechas confirmadas; plan de sprints v1.2; sprint backlog v1.2; historias de usuario v2.5; historias técnicas v1.5; pila v1.5. Formato visual basado en 7402_alcance.docx y la ficha aportada por el tesista.")
    helpers.body(doc, "Historial: v1.3, tabla de tareas y anexo de prioridad de HU. v1.4, ficha individual por tarea. v1.5, corrección de autoría. v1.6, tablas de resumen de sprints, vínculos con historias y evidencia prevista. Revisión académica y publicación pendientes.")
    doc.core_properties.title = "Plan incremental y sprint backlog"
    doc.core_properties.author = "Franklin Acero"
    doc.save(OUTPUT_SPRINTS)
    print(OUTPUT_SPRINTS)


if __name__ == "__main__":
    build_stories()
    build_sprints()
