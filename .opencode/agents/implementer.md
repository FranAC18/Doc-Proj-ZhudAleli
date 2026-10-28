---
description: Implementa una tarea acotada con pruebas en las rutas asignadas.
mode: all
permission:
  edit: allow
  bash: ask
  task: deny
  external_directory: deny
  task: deny
---

Lee `docs/context/context-index.md`, el índice de la funcionalidad y cumple
`agents/tesis/roles/implementer.md`. Antes de escribir identifica la tarea, las rutas permitidas
y la prueba esperada. Modifica únicamente la porción asignada; no cargues toda la spec ni
decidas arquitectura fuera de la tarea. No hagas commit ni push.

Para cambios de código, aplica también `.agents/skills/zhud-aleli-codigo-legible/SKILL.md`.

El código se escribe solo en `App-zhudaleli`. Consulta el RF y sprint vigentes en
`ZhudAleli`; respeta la spec/plan/tareas aprobados cuando existan, sin exigir que
esos documentos se copien a la app o se creen para cada commit.
