from __future__ import annotations

from datetime import date
from pathlib import Path

from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor


ROOT = Path(r"F:\Tesis\App Tesis")
REFERENCE = Path(r"F:\Software\8vo Semestre\Aplicaciones Informaticas II\7402_alcance.docx")
OUTPUT = ROOT / "documentacion" / "sprints" / "plan_incremental_y_sprints_v1.1_2026-10-13.docx"


def shade(cell, color: str) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    element = tc_pr.find(qn("w:shd"))
    if element is None:
        element = OxmlElement("w:shd")
        tc_pr.append(element)
    element.set(qn("w:fill"), color)


def format_cell(cell) -> None:
    tc_pr = cell._tc.get_or_add_tcPr()
    borders = tc_pr.find(qn("w:tcBorders"))
    if borders is None:
        borders = OxmlElement("w:tcBorders")
        tc_pr.append(borders)
    for side in ("top", "left", "bottom", "right"):
        element = borders.find(qn(f"w:{side}"))
        if element is None:
            element = OxmlElement(f"w:{side}")
            borders.append(element)
        element.set(qn("w:val"), "single")
        element.set(qn("w:sz"), "4")
        element.set(qn("w:color"), "D9D9D9")
    margins = tc_pr.find(qn("w:tcMar"))
    if margins is None:
        margins = OxmlElement("w:tcMar")
        tc_pr.append(margins)
    for side, amount in (("top", 85), ("bottom", 85), ("left", 100), ("right", 100)):
        element = margins.find(qn(f"w:{side}"))
        if element is None:
            element = OxmlElement(f"w:{side}")
            margins.append(element)
        element.set(qn("w:w"), str(amount))
        element.set(qn("w:type"), "dxa")
    cell.vertical_alignment = WD_CELL_VERTICAL_ALIGNMENT.CENTER


def no_split(row) -> None:
    row._tr.get_or_add_trPr().append(OxmlElement("w:cantSplit"))


def repeat_header(row) -> None:
    row._tr.get_or_add_trPr().append(OxmlElement("w:tblHeader"))


def write_cell(cell, value: str, *, bold: bool = False, white: bool = False,
               align: WD_ALIGN_PARAGRAPH = WD_ALIGN_PARAGRAPH.LEFT,
               size: float = 8.0) -> None:
    cell.text = ""
    format_cell(cell)
    for index, line in enumerate(value.split("\n")):
        paragraph = cell.paragraphs[0] if index == 0 else cell.add_paragraph()
        paragraph.alignment = align
        paragraph.paragraph_format.space_before = Pt(0)
        paragraph.paragraph_format.space_after = Pt(2 if index < len(value.split("\n")) - 1 else 0)
        paragraph.paragraph_format.line_spacing = 1.12
        run = paragraph.add_run(line)
        run.font.name = "Century Gothic"
        run.font.size = Pt(size)
        run.font.color.rgb = RGBColor(255, 255, 255) if white else RGBColor(0, 0, 0)
        run.bold = bold


def add_table(doc, headers: list[str], rows: list[list[str]], widths: list[float],
              size: float = 8.0, trailing_space: bool = True) -> None:
    assert len(headers) == len(widths)
    table = doc.add_table(rows=1, cols=len(headers))
    table.autofit = False
    for col, width in zip(table.columns, widths):
        col.width = Cm(width)
    for cell, text, width in zip(table.rows[0].cells, headers, widths):
        cell.width = Cm(width)
        write_cell(cell, text, bold=True, white=True, size=size)
        shade(cell, "404040")
    repeat_header(table.rows[0])
    no_split(table.rows[0])
    for index, values in enumerate(rows):
        assert len(values) == len(headers)
        row = table.add_row()
        for cell, value, width in zip(row.cells, values, widths):
            cell.width = Cm(width)
            write_cell(cell, value, size=size)
            if index % 2:
                shade(cell, "F7F7F7")
        no_split(row)
    if trailing_space:
        doc.add_paragraph().paragraph_format.space_after = Pt(2)


def add_record(doc, title: str, rows: list[tuple[str, str]]) -> None:
    table = doc.add_table(rows=1, cols=2)
    table.autofit = False
    table.columns[0].width = Cm(3.1)
    table.columns[1].width = Cm(11.9)
    merged = table.rows[0].cells[0].merge(table.rows[0].cells[1])
    write_cell(merged, title, bold=True, white=True, size=8.5)
    shade(merged, "404040")
    repeat_header(table.rows[0])
    no_split(table.rows[0])
    for index, (label, value) in enumerate(rows):
        row = table.add_row()
        row.cells[0].width = Cm(3.1)
        row.cells[1].width = Cm(11.9)
        write_cell(row.cells[0], label, bold=True)
        write_cell(row.cells[1], value)
        if index % 2:
            for cell in row.cells:
                shade(cell, "F7F7F7")
        no_split(row)
    for row in table.rows[:-1]:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                paragraph.paragraph_format.keep_with_next = True
    doc.add_paragraph().paragraph_format.space_after = Pt(2)


def heading(doc, title: str, level: int = 1) -> None:
    paragraph = doc.add_paragraph(title, style=f"Heading {level}")
    paragraph.paragraph_format.keep_with_next = True


def body(doc, text: str, keep_next: bool = False) -> None:
    paragraph = doc.add_paragraph(text, style="Normal")
    paragraph.paragraph_format.space_after = Pt(8)
    paragraph.paragraph_format.keep_with_next = keep_next


def sprint(doc, number: int, dates: str, objective: str, nucleus: str,
           dependencies: str, proof: str, docs: str, limit: str) -> None:
    heading(doc, f"SPRINT {number}", 2)
    add_record(doc, f"Incremento {number}  |  {dates}", [
        ("Objetivo", objective),
        ("Trabajo candidato", nucleus),
        ("Antes de iniciar", dependencies),
        ("Cierre verificable", proof),
        ("Documentos", docs),
        ("Límite", limit),
    ])


def build() -> None:
    assert (date(2026, 12, 23) - date(2026, 10, 13)).days + 1 == 72
    spans = [
        (date(2026, 10, 13), date(2026, 10, 26)),
        (date(2026, 10, 27), date(2026, 11, 9)),
        (date(2026, 11, 10), date(2026, 11, 23)),
        (date(2026, 11, 24), date(2026, 12, 7)),
        (date(2026, 12, 8), date(2026, 12, 21)),
    ]
    assert all((end - start).days + 1 == 14 for start, end in spans)
    assert all(spans[i][1].toordinal() + 1 == spans[i + 1][0].toordinal() for i in range(4))

    doc = Document(REFERENCE)
    for paragraph in list(doc.paragraphs)[15:]:
        paragraph._element.getparent().remove(paragraph._element)
    doc.paragraphs[6].text = "Plan incremental y cronograma de sprints"
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

    doc.add_page_break()
    title = doc.add_paragraph("Plan incremental y cronograma de sprints", style="Title")
    title.paragraph_format.space_after = Pt(12)
    body(doc, "Versión 1.1 · 13 de octubre de 2026 · Historial: adaptación del Gantt de 16 semanas al plazo confirmado · Estado: revisión académica pendiente")

    heading(doc, "INTRODUCCIÓN")
    body(doc, "Este plan adapta el Gantt de 16 semanas aportado por el tesista al periodo confirmado de desarrollo, del 13 de octubre al 23 de diciembre de 2026. Conserva la secuencia de cinco módulos, las pruebas durante el desarrollo y los hitos de cierre. Fija cinco periodos de dos semanas y dos días finales para entregar evidencia.")
    body(doc, "Las fechas fueron comunicadas por el tesista. Los objetivos y la distribución de historias son propuestas de planificación sujetas a estimación, dependencias y revisión. Al 13 de octubre no existe una aplicación Django funcional; tampoco consta la revisión de la directora para los ajustes documentales más recientes. No se declara cerrada la fase de diseño por el solo inicio del calendario.")

    heading(doc, "CALENDARIO GENERAL")
    add_table(doc, ["Etapa", "Fechas de 2026", "Duración", "Hito previsto"], [
        ["Requisitos y diseño", "Hasta el 13 de octubre", "Cierre por verificar", "Línea base, decisiones y revisión de diseño"],
        ["Sprint 1", "13 al 26 de octubre", "14 días", "Acceso y base técnica verificables"],
        ["Sprint 2", "27 de octubre al 9 de noviembre", "14 días", "Actividades y encargos verificables"],
        ["Sprint 3", "10 al 23 de noviembre", "14 días", "Asistencia y continuidad habilitada"],
        ["Sprint 4", "24 de noviembre al 7 de diciembre", "14 días", "Trazabilidad e inventario; comercio según capacidad"],
        ["Sprint 5", "8 al 21 de diciembre", "14 días", "Reportes, sitio público e integración"],
        ["Cierre", "22 y 23 de diciembre", "2 días", "Evaluación, evidencia y entrega documental"],
    ], [2.6, 4.1, 1.8, 6.5])
    body(doc, "Los cinco sprints suman 70 días calendario; el cierre añade dos días. El periodo completo tiene 72 días calendario, equivalentes a 10 semanas y 2 días. No se han descontado feriados, ausencias ni tiempo disponible de las representantes; por ello los días calendario no son horas de trabajo comprometidas.")

    heading(doc, "ADAPTACIÓN DEL GANTT ENTREGADO")
    body(doc, "El Gantt original expresa semanas relativas: requisitos en las semanas 1 y 2; diseño, arquitectura, base de datos, interfaz y preparación PWA en las semanas 3 y 4; cinco módulos en las semanas 5 a 12; integración y pruebas finales en las semanas 13 y 14; validación, capacitación y manuales en las semanas 15 y 16. Sus hitos son las semanas 2, 4, 12 y 16. El calendario confirmado tiene 40 días calendario menos que esas 16 semanas; esta adaptación no demuestra que el mismo volumen de trabajo quepa sin cambios.")
    add_table(doc, ["Bloque del Gantt", "Ubicación en este plan", "Condición de cierre"], [
        ["Semanas 1 y 2  Requisitos", "Antes del 13 de octubre", "Línea base identificada; decisiones y validación pendientes registradas."],
        ["Semanas 3 y 4  Diseño y PWA", "Antes de cada implementación; base técnica en Sprint 1", "Diseño y puertas verificadas por función; no se presume diseño terminado."],
        ["Semanas 5 a 12  Módulos 1 a 5", "Sprints 1 a 5, del 13 de octubre al 21 de diciembre", "Incremento demostrable y pruebas parciales en cada cierre."],
        ["Semanas 13 y 14  Integración y pruebas", "Integración progresiva desde Sprint 2; tramo final de Sprint 5", "Pruebas funcionales, de uso y de continuidad aprobada con resultados reales."],
        ["Semanas 15 y 16  Validación y entrega", "Sprint 5 y cierre del 22 y 23 de diciembre", "Sesión con usuarias, correcciones críticas, capacitación y manuales sujetos a agenda y capacidad."],
    ], [4.0, 5.1, 5.9])
    body(doc, "Los solapamientos de módulos del Gantt se traducen en tareas preparatorias y pruebas que pueden avanzar dentro de sprints consecutivos; para un solo tesista no se declaran sprints simultáneos. Las funciones con reglas pendientes se mantienen en la pila hasta cerrar su puerta de requisito.")

    heading(doc, "VISTA TEMPORAL ADAPTADA")
    body(doc, "En la tabla, «Base» significa trabajo previo por verificar, «●» trabajo previsto y «—» sin trabajo principal previsto. Las fechas de cada columna figuran en el calendario general; el símbolo muestra distribución, no avance real.", keep_next=True)
    add_table(doc, ["Actividad", "Previo", "S1", "S2", "S3", "S4", "S5", "Cierre"], [
        ["Requisitos y decisiones", "Base", "●", "●", "●", "●", "●", "—"],
        ["Arquitectura, datos, interfaz y PWA", "Base", "●", "●", "●", "●", "●", "—"],
        ["Módulo 1  Administración y acceso", "—", "●", "—", "—", "—", "—", "—"],
        ["Módulo 2  Planificación", "—", "—", "●", "—", "—", "—", "—"],
        ["Módulo 3  Asistencia", "—", "—", "—", "●", "—", "—", "—"],
        ["Módulo 4  Trazabilidad", "—", "—", "—", "—", "●", "—", "—"],
        ["Módulo 5  Reportes e información", "—", "—", "—", "—", "—", "●", "—"],
        ["Pruebas parciales y regresión", "—", "●", "●", "●", "●", "●", "—"],
        ["Integración, uso y continuidad", "—", "—", "●", "●", "●", "●", "●"],
        ["Correcciones y validación con usuarias", "—", "—", "—", "—", "●", "●", "●"],
        ["Manuales, capacitación y cierre", "—", "—", "—", "—", "—", "●", "●"],
    ], [5.7, 1.3, 1.15, 1.15, 1.15, 1.15, 1.15, 1.25], size=7.2)
    body(doc, "Se reserva trabajo de cierre dentro del Sprint 5, porque dos días finales por sí solos no bastan para comenzar pruebas finales, validar con usuarias, corregir, capacitar y redactar manuales. Las fechas exactas de las sesiones deben acordarse con las participantes.")

    heading(doc, "LÓGICA DE ENTREGA INCREMENTAL")
    body(doc, "Cada incremento incorpora un recorrido útil sobre la misma aplicación y conserva lo ya comprobado. La versión siguiente integra datos, permisos y pruebas de las anteriores. Preparar código, completar pruebas y publicar una versión operativa son momentos distintos.")
    add_table(doc, ["Incremento", "Resultado que se puede demostrar", "Se conserva al avanzar"], [
        ["1  Acceso", "Entrar, salir y denegar acciones no autorizadas en un recorrido móvil.", "Identidad, permisos y base de datos"],
        ["2  Planificación", "Crear una actividad y asignar responsables con estado visible.", "Acceso y autorización"],
        ["3  Asistencia", "Registrar y consultar asistencia; ensayar captura sin red solo para acciones autorizadas.", "Acceso, actividades y trazabilidad de cambios"],
        ["4  Producción", "Seguir materia prima, secado y lote hasta existencias; ampliar a comercio si cabe y está definido.", "Recorridos anteriores e integridad de datos"],
        ["5  Información", "Consultar reportes y contenido público aprobado; verificar la integración completa.", "Todos los recorridos afectados por los cambios"],
    ], [2.7, 6.9, 5.4])
    body(doc, "La pila actual reúne 51 historias de usuario y 9 técnicas sin estimación del equipo. Esta secuencia no afirma que las 60 entradas cabrán en el plazo. Antes de comprometer cada sprint se eligen historias con criterios, dependencias y tamaño conocidos; las demás permanecen visibles en la pila.")

    heading(doc, "PLAN DE SPRINTS")
    body(doc, "Los objetivos siguientes expresan el orden de trabajo propuesto. Un incremento se considera terminado solo cuando existe un recorrido funcional, permisos comprobados, pruebas con resultado real y documentación actualizada. Una maqueta, una tabla de tareas o una fecha cumplida no bastan.", keep_next=True)

    sprint(doc, 1, "13 al 26 de octubre de 2026",
           "Establecer un primer recorrido privado verificable sobre Django y PostgreSQL, usable en móvil y con autorización en el servidor.",
           "Núcleo: HU-ACC-001 y porción aprobada de SPEC-001. Candidatos según estimación: HU-ACC-002 a 004 y HT-GEN-001, 002, 004 y 009. HT-GEN-008 explora despliegue y recuperación sin declarar aprobada una política de respaldo.",
           "Comprobar la puerta de diseño e implementación de SPEC-001; definir tareas, rutas y pruebas. La revisión académica pendiente se registra y no se presume realizada.",
           "Inicio y cierre de sesión, cuenta inactiva y acceso denegado; migraciones PostgreSQL; recorrido móvil y prueba de permisos. Guardar resultados y regresión del acceso.",
           "Plan del sprint, especificación y diseño de acceso, matriz requisito-historia-prueba, resultados, revisión y retrospectiva.",
           "No dar por terminado todo el módulo de administración si solo funciona la primera porción de acceso.")

    sprint(doc, 2, "27 de octubre al 9 de noviembre de 2026",
           "Permitir que la Directiva registre actividades y asigne personas o encargos, reutilizando el acceso y los permisos del incremento anterior.",
           "Núcleo candidato: HU-PLA-001 a 004. HU-PLA-005 y el catálogo mínimo HU-CAT-001 se refinan juntos porque la planificación semanal necesita identificar productos. El alcance final depende de la capacidad real.",
           "Definir actores, fechas, estados, vigencia de encargos y permisos; completar las especificaciones del recorrido elegido antes de implementarlo.",
           "Crear y consultar actividad, asignar cuenta activa, rechazar cuenta inactiva o usuaria sin permiso, y comprobar que el acceso del Sprint 1 sigue funcionando.",
           "Historias y pila refinadas, diseño de actividades/encargos, pruebas de permisos, revisión con representantes y retrospectiva.",
           "No ampliar el catálogo productivo más allá de lo necesario para el recorrido aprobado sin estimar su efecto en Sprint 4.")

    sprint(doc, 3, "10 al 23 de noviembre de 2026",
           "Registrar asistencia y correcciones con historial; incorporar continuidad sin conexión solo en operaciones definidas y seguras.",
           "Núcleo candidato: HU-ASI-001 a 007. La continuidad HU-PWA-001 a 003 y HT-GEN-003, 005 y 006 se integra desde los recorridos habilitados, no se deja para el final. La selección se ajusta a la estimación.",
           "Resolver P-02, P-13 y P-14 para QR, tiempos, dispositivo y conflictos. P-03 debe aclarar justificativos, autoridad, redondeo y cobro antes de cualquier consecuencia automática.",
           "Entrada y salida separadas, duplicado rechazado, corrección con actor/motivo, acceso privado, corte de red y reintento sin duplicación cuando esa captura esté aprobada.",
           "Especificación de asistencia y sincronización, decisiones P resueltas, casos de prueba, resultados de corte/reintento, revisión y retrospectiva.",
           "La regla comunicada de USD 0,01 por minuto y USD 10 desde la primera falta no autoriza sanciones automáticas mientras P-03 siga abierta.")

    sprint(doc, 4, "24 de noviembre al 7 de diciembre de 2026",
           "Demostrar una cadena productiva coherente y verificable desde la materia prima hasta el inventario; incorporar ventas y rendición según capacidad y decisiones cerradas.",
           "Secuencia candidata: catálogo, acopio, secado, procedencia/lote, transformación, movimientos y existencias (HU-CAT, HU-TRA, HU-INV). Después: feria, ventas, gastos y cuentas por cobrar (HU-VEN, HU-GAS, HU-CXC) si el tamaño medido lo permite.",
           "Resolver P-04 y P-05 para unidades y lotes; P-07 a P-10 para funciones comerciales afectadas. Definir propietarios de datos, transacciones y permisos antes de operaciones monetarias.",
           "Conciliar pesos, mermas, lotes y existencias; evitar saldo negativo y cambios parciales. Si se incorporan ventas, probar totales, valores históricos, devoluciones y saldos con casos reales.",
           "Modelo y reglas de datos versionados, historias seleccionadas, pruebas de integridad/concurrencia, diferencias de inventario, revisión y retrospectiva.",
           "Es el bloque más cargado. No se promete completar producción, inventario y comercio sin estimación; cualquier brecha se eleva para decidir alcance, recursos o fecha.")

    sprint(doc, 5, "8 al 21 de diciembre de 2026",
           "Producir información verificable, cerrar la integración y preparar validación, capacitación y entrega sobre los incrementos realmente terminados.",
           "Candidatos: HT-GEN-007, HU-REP-001 a 006, HU-NOT-001 y HU-PUB-001/002. Los reportes se limitan a datos y recorridos confirmados; el contenido público depende de P-12.",
           "Confirmar permisos de cada reporte, filtros, unidades y datos fuente. Resolver P-12 antes de publicar contenido; disponer de entorno y estrategia de recuperación verificables para una versión piloto.",
           "Conciliar PDF y pantalla con registros fuente; probar acceso indebido, móvil, accesibilidad, sincronización aprobada y regresión de Sprints 1 a 4. Programar la sesión de validación con usuarias y registrar hallazgos y correcciones críticas.",
           "Diseño de reportes, resultados de integración y uso, acta de validación cuando ocurra, borradores de manuales y capacitación, registro de cambios, revisión y retrospectiva.",
           "Si faltan recorridos previos, el reporte solo refleja lo comprobado. Validación y capacitación dependen de la agenda de participantes; no se declaran realizadas por estar programadas.")

    heading(doc, "CADENCIA DE TRABAJO Y CONTROL DE TIEMPO")
    body(doc, "La siguiente cadencia es una guía para cada bloque de 14 días calendario. Las reuniones y jornadas reales se fijan con la disponibilidad del tesista, la Directiva y las socias; el plan no supone dedicación diaria ni valida feriados.", keep_next=True)
    add_table(doc, ["Momento", "Trabajo y evidencia", "Decisión"], [
        ["Inicio del sprint", "Revisar capacidad disponible, estimar y elegir historias; fijar objetivo, responsables y pruebas.", "Solo entran elementos con puertas y dependencias suficientes."],
        ["Mitad del periodo", "Comprobar recorrido parcial, bloqueos, esfuerzo restante y cambios necesarios.", "Si el pronóstico no cabe, actualizar pila y elevar la decisión."],
        ["Tramo final", "Ejecutar pruebas, resolver fallos críticos, revisar con usuarias cuando sea posible y preparar evidencia.", "No cerrar una historia sin resultado real y regresión afectada."],
        ["Último día", "Revisión, retrospectiva, estado de historias, versión documental y plan del siguiente sprint.", "Registrar completado, parcial o bloqueado sin ocultar pendientes."],
    ], [2.5, 8.0, 4.5])

    heading(doc, "HITOS DE ENTREGA")
    add_table(doc, ["Fecha", "Hito", "Evidencia exigida"], [
        ["13 de octubre", "Inicio de desarrollo; cierre de diseño por verificar", "Estado de requisitos, revisión académica y puertas pendientes"],
        ["26 de octubre", "Revisión del incremento 1", "Acceso demostrado, pruebas y lista de pendientes"],
        ["9 de noviembre", "Revisión del incremento 2", "Actividad y asignación comprobadas; regresión del acceso"],
        ["23 de noviembre", "Revisión del incremento 3", "Asistencia y continuidad aprobada probadas; decisiones abiertas visibles"],
        ["7 de diciembre", "Revisión del incremento 4", "Cadena productiva y partes comerciales realmente verificadas"],
        ["21 de diciembre", "Revisión del incremento 5 y preparación del cierre", "Reportes, pruebas integradas, hallazgos de usuarias si hubo sesión y manuales preparados"],
        ["22 y 23 de diciembre", "Cierre y entrega", "Correcciones críticas, validación acordada, capacitación, manuales, matriz y estado final verificable"],
    ], [2.9, 4.2, 7.9])

    heading(doc, "CAPACIDAD Y REPLANIFICACIÓN")
    body(doc, "Se estiman historias y disponibilidad real al inicio de cada sprint, reservando tiempo para pruebas, integración, correcciones y documentos. Las 60 entradas aún no tienen estimación; no puede calcularse una brecha fiable. Al inicio, mitad y cierre se compara trabajo restante con capacidad, se registran pendientes y se autorizan cambios de fecha, recursos o alcance; si afectan el anteproyecto, requieren revisión de la directora.")

    heading(doc, "RIESGOS TEMPORALES")
    add_table(doc, ["Riesgo", "Efecto", "Comprobación temprana"], [
        ["Gantt de 16 semanas frente a 10 semanas y 2 días", "Hay 40 días calendario menos; la carga puede superar el plazo.", "Estimar historias y capacidad desde Sprint 1; comparar cada cierre."],
        ["Diseño y revisión académica aún pendientes", "Retrabajo o bloqueo de implementación.", "Registrar aprobación y puerta de cada función antes de construirla."],
        ["Sprint 4 concentra producción y comercio", "Poco tiempo para pruebas e integración.", "Elegir cadena mínima verificable y pronosticar el resto con datos."],
        ["Validación, correcciones y formación al final", "La agenda de usuarias y dos días de cierre pueden ser insuficientes.", "Acordar sesiones antes del Sprint 5, redactar manuales durante ese sprint y reservar tiempo de corrección."],
        ["P-02 a P-14 abiertas", "Reglas incompletas en QR, offline, lotes, dinero y sitio público.", "Cerrar cada decisión antes de la porción que depende de ella."],
        ["Entorno y restauración sin demostración", "La versión piloto podría no operar o recuperarse.", "Probar despliegue mínimo y política de respaldo antes de prometer publicación."],
    ], [4.5, 4.0, 6.5])

    heading(doc, "DOCUMENTACIÓN POR INCREMENTO")
    body(doc, "En cada sprint se actualizan las historias seleccionadas, la pila, el diseño afectado, la matriz requisito-historia-prueba, resultados, revisión y retrospectiva. Cada edición final lleva versión, fecha, autor, estado, fuentes e historial. El control de cambios identifica qué se preparó y qué se publicó.")
    body(doc, "La entrega documental de cada incremento se prepara con las ediciones revisadas y su control de cambios. La publicación en el repositorio del docente requiere confirmación del tesista.")

    heading(doc, "FUENTES E HISTORIAL")
    body(doc, "Fuentes: Gantt aportado por el tesista y plan de sprints v1.0 (secuencia y fechas); pila de producto v1.2 (51 historias de usuario y 9 técnicas sin estimar); factibilidad v1.3 (riesgo temporal); CAT-REQ-001 v1.1, plan de pruebas v1.0, constitución 0.2.0 y ADR-0006 (alcance, pruebas y entregas).")
    body(doc, "Historial: v1.0, cinco incrementos iniciales; v1.1, correspondencia con el Gantt, pruebas continuas y cierre adaptado. Revisión académica y capacidad pendientes.")
    # Word needs a final paragraph after a table; keep it small enough to stay on this page.
    final_paragraph = doc.add_paragraph()
    final_paragraph.paragraph_format.space_before = Pt(0)
    final_paragraph.paragraph_format.space_after = Pt(0)
    final_paragraph.paragraph_format.line_spacing = Pt(1)
    final_paragraph.add_run(" ").font.size = Pt(1)

    doc.core_properties.title = "Plan incremental y cronograma de sprints"
    doc.core_properties.subject = "Zhud Alelí"
    doc.core_properties.author = "Franklin Acero"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    doc.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    build()
