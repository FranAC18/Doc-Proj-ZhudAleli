---
title: Cronograma Gantt como proyecto local
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
  - "[[2026-10-13-gantt-archivo-local-pre-commit]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/planificacion
---

# Cronograma Gantt como proyecto local

El tesista pidió convertir el HTML autónomo en un proyecto pequeño con acceso
de doble clic, servidor local y puerto que no interfiera con otros proyectos.
Se preparó `analisis/2026-10-13/gantt-interactivo/proyecto-local/` con
`Abrir cronograma.cmd`, `servidor.py`, pantalla, estilos, interacción y datos
documentales separados. El servidor escucha en `127.0.0.1` y el sistema elige
un puerto disponible en cada inicio. Una segunda apertura del mismo seguimiento
reutiliza la instancia activa.

El avance se guarda en `estado/seguimiento_sprints_zhud_aleli.json` mediante
escritura temporal y sustitución atómica. `estado/` se excluye de Git. Al
reiniciar, la interfaz lee el archivo. Se conservó Importar para trasladar un
JSON del HTML autónomo anterior y Exportar para obtener una copia. Las
ediciones autónomas previas siguen intactas como antecedentes. El proyecto
local no es la aplicación Django de la asociación.

## Verificación

- La prueba de navegador abrió dos servidores con archivos distintos y comprobó
  que usaron puertos diferentes; una segunda apertura del mismo archivo usó la
  instancia original.
- Se guardó una tarea en un archivo temporal, se cerró y reinició el servidor,
  y se recuperó el estado en el navegador.
- Se verificaron exportación, importación, enlace a una fuente documental y
  rechazo de una solicitud de escritura sin origen local.
- La sintaxis de Python y JavaScript pasó; ocho enlaces documentales generados
  apuntan a archivos existentes.

No se hizo commit ni push. No se modificó ni publicó `documentacion/`.
