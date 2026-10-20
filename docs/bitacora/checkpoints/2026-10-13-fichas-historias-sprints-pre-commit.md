---
title: Fichas individuales de historias y sprints
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
  - "[[2026-10-13-tablas-prioridades-documentales-pre-commit]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/transversal
---

# Fichas individuales de historias y sprints

## Solicitud y criterio editorial

El tesista rechazó la presentación de las tablas porque mezclaba campos y
aportó una imagen de fichas de historia de usuario como referencia. Preguntó
por `SB-S3-01`: significa tarea 01 del sprint backlog del Sprint 3. En las
ediciones nuevas el número y nombre de la tarea son visibles; el código queda
como dato de trazabilidad secundario. No se elimina ningún identificador que
enlace historias, pila y planificación.

## Archivos preparados

| Archivo | Cambio |
|---|---|
| `documentacion/historias/usuario/historias_usuario_v2.5_2026-10-13.md` | 51 fichas HU con campos independientes. |
| `documentacion/historias/tecnicas/historias_tecnicas_v1.5_2026-10-13.md` | 9 fichas HT de base y 10 propuestas. |
| `documentacion/historias/historias_usuario_tecnicas_pila_v1.1_2026-10-13.docx` | Compendio Word en formato de ficha y pila de producto. |
| `documentacion/pila_producto/pila_producto_v1.5_2026-10-13.md` | 60 posiciones base con una columna por dato y diez HT propuestas aparte. |
| `documentacion/sprints/sprint_backlog_v1.2_2026-10-13.md` | 27 tareas candidatas en fichas individuales. |
| `documentacion/sprints/plan_incremental_y_sprint_backlog_v1.4_2026-10-13.docx` | Calendario y fichas de tarea en Word. |
| `documentacion/sprints/plan_sprints_v1.2_2026-10-13.md` | Referencias a las fichas vigentes. |
| `documentacion/README.md` y `documentacion/control_de_cambios/registro_v2.5_2026-10-13.md` | Índice y control actualizados. |

Las ediciones anteriores permanecen conservadas. El trabajo interno y los
PDF/PNG de revisión están en `analisis/2026-10-13/fichas-separadas/`, fuera de
la carpeta publicable.

## Verificaciones

- Se cotejaron las 51 HU, 19 HT y 27 tareas por código en Markdown y Word.
  Permanecen las 60 posiciones de la pila base y las diez HT propuestas fuera
  de esa base. Los criterios de las 51 HU y las salidas de las HT se conservan.
- Los enlaces locales de los Markdown vigentes resuelven; no se encontraron
  caracteres de reemplazo ni espacios finales en esos archivos.
- El renderizador de la skill de documentos no encontró LibreOffice. Se usó
  Microsoft Word como alternativa para convertir los documentos: 33 páginas
  de historias, técnicas y pila; 11 páginas del plan de sprints. Se
  inspeccionaron visualmente las páginas y se amplió la columna de prioridad
  de la pila para evitar cortes en «Complementaria».
- Puntos, riesgo y responsable permanecen como pendientes. No se inventaron
  estimaciones, resultados de pruebas ni aprobación de reglas nuevas.

## Pendiente

Revisión editorial y académica, estimación real y confirmación de las
prioridades propuestas. **Commit y publicación de esta edición: pendientes.**
La publicación eventual usa únicamente archivos revisados de `documentacion/`
en el clon separado del repositorio del docente y requiere confirmación
específica del tesista.
