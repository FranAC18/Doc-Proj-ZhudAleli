---
title: Cronograma Gantt interactivo de planificación
type: checkpoint
status: prepared-pending-review
date: 2026-10-13
task_id: DOC-ORG-001
phase: pre_commit
branch: opencode/spec-001-fase-1-diseno
commit: pending
publication: not-requested
module: planificacion
related:
  - "[[../ESTADO-ACTIVO]]"
  - "[[2026-10-13-resumen-tablas-sprint-backlog-pre-commit]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/planificacion
---

# Cronograma Gantt interactivo de planificación

El tesista pidió un HTML interactivo que relacione requisitos, historias,
sprints y comprobación del trabajo. Se preparó una herramienta autónoma en
`analisis/2026-10-13/gantt-interactivo/`, fuera de `documentacion/` porque
incluye código de interfaz y datos de seguimiento locales. La ventana abarca
del 15 de septiembre al 23 de diciembre de 2026.

El Gantt muestra seis sprints, cierre, 27 tareas candidatas, 51 HU, 19 HT,
51 RF y nueve RNF. Otra vista enumera 13 decisiones abiertas, dos requisitos
propuestos y nueve temas de entrevista por aclarar. Las barras de tareas
representan la ventana de su sprint; no se inventaron fechas individuales.

Todas las tareas aparecen inicialmente sin verificar. La herramienta exige
evidencia para marcar una tarea como realizada y, para marcarla verificada,
también fecha y persona que revisó. El avance se guarda en el navegador y
puede exportarse o importarse como JSON. No se sincroniza con los documentos
ni constituye prueba oficial de ejecución.

## Verificación

- Se comprobó la correspondencia de 157 elementos del cronograma, 24
  pendientes y ocho enlaces a documentos fuente existentes.
- Una prueba de navegador verificó las 27 tareas, 51 HU, 19 HT, 60 requisitos,
  24 pendientes, filtros, Gantt, validación de evidencia, persistencia local,
  contenido exportable, importación y vista móvil.
- Se inspeccionaron capturas de escritorio y móvil; el HTML no depende de
  servicios o bibliotecas externas.
- `git diff --check` para las rutas afectadas no informó errores de contenido.

No se hizo commit ni push. No se modificó ni publicó `documentacion/`.
