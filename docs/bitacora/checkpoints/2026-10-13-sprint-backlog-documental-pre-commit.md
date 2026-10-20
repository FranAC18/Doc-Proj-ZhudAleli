---
title: Preparación documental de S1–S6 y sprint backlog
type: checkpoint
status: prepared-pending-review
date: 2026-10-13
task_id: DOC-ORG-001
phase: pre_commit
branch: opencode/spec-001-fase-1-diseno
commit: pending
publication: pending
module: transversal
sprint: S1-S6
related:
  - "[[../ESTADO-ACTIVO]]"
  - "[[2026-10-13-publicacion-documental-verificada]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/transversal
---

# Preparación documental de S1–S6 y sprint backlog

## Alcance registrado

Este checkpoint registra los cambios **documentales de la entrega actual**.
No declara revisados ni documentados los demás cambios locales del repositorio.
El punto de partida del repositorio general es
`09f4318106fd85d10c3095d592c177c33972c1ff` en
`opencode/spec-001-fase-1-diseno`. La publicación documental anterior fue
`20f42279a769b3aefc6d52a0efde79e4c707e498` en el repositorio del
docente. Estos hashes son antecedentes, no commits de esta entrega.

## Ediciones preparadas

El detalle de versión y motivo de cada edición está en
`documentacion/control_de_cambios/registro_v2.3_2026-10-13.md`. El índice
`documentacion/README.md` señala las ediciones vigentes. Se comprobó la
existencia de los siguientes once archivos:

| Área | Archivo preparado |
|---|---|
| Alcance | `documentacion/alcance/alcance_v1.2_2026-10-13.md` |
| Requisitos | `documentacion/requisitos/priorizacion/priorizacion_requisitos_v1.2_2026-10-13.md` |
| Historias de usuario | `documentacion/historias/usuario/historias_usuario_v2.3_2026-10-13.md` |
| Historias técnicas | `documentacion/historias/tecnicas/historias_tecnicas_v1.4_2026-10-13.md` |
| Pila de producto | `documentacion/pila_producto/pila_producto_v1.3_2026-10-13.md` |
| Plan de sprints | `documentacion/sprints/plan_sprints_v1.1_2026-10-13.md` |
| Sprint backlog | `documentacion/sprints/sprint_backlog_v1.0_2026-10-13.md` |
| Plan académico Word | `documentacion/sprints/plan_incremental_y_sprint_backlog_v1.2_2026-10-13.docx` |
| Factibilidad | `documentacion/factibilidad/factibilidad_v1.4_2026-10-13.md` |
| Índice | `documentacion/README.md` |
| Control de cambios | `documentacion/control_de_cambios/registro_v2.3_2026-10-13.md` |

La organización temporal acordada es S1 del 15 de septiembre al 12 de
octubre de 2026, S2 desde el 13 de octubre y desarrollo S2–S6 hasta el
21 de diciembre, seguido del cierre el 22 y 23 de diciembre. El backlog
relaciona tareas con historias de usuario, historias técnicas y pila. Las
diez historias técnicas añadidas están marcadas como **propuestas** y no
se incorporan como aprobadas a la base de 60 elementos.

## Evidencia de revisión y verificaciones

- El documento Word v1.2 se convirtió a PDF de seis páginas A4 con Microsoft
  Word y se inspeccionó visualmente; la copia de revisión está en
  `analisis/2026-10-13/sprint-backlog/plan-y-backlog-v1_2.pdf`.
- En la revisión de contenido se comprobaron 51 HU únicas, nueve HT de base,
  diez HT propuestas, 60 filas de la pila base y 27 tareas del Word. Las 51 HU
  aparecen en el sprint backlog y el Word; las diez HT propuestas aparecen
  en la pila, el sprint backlog y el Word.
- Se comprobaron los enlaces Markdown de las ediciones afectadas, sin enlaces
  locales rotos. La sección económica de factibilidad v1.4 conserva los
  cálculos de v1.3.
- La comprobación actual confirmó que existen los once archivos de la tabla
  y que `documentacion/README.md` está excluido del repositorio general.
- `git diff --check` global señaló únicamente espacios finales en
  `design/style-guide/tokens.html`, líneas 19 y 75, fuera de esta entrega.
  Los archivos documentales afectados se revisaron sin espacios finales.

## Pendientes y próximo paso

El plan y el sprint backlog son una propuesta de planificación: faltan la
revisión académica y la validación de las nuevas HT. La aplicación, los
sprints y las pruebas de producto no se presentan como terminados.
**Commit de esta entrega: pendiente. Publicación al repositorio del docente:
pendiente.** Antes de cualquiera de esos pasos, revisar el conjunto exacto
en el clon documental separado y solicitar la autorización correspondiente.
Solo se sincronizarán archivos de `documentacion/`; este checkpoint y los
archivos internos no se publican al docente.
