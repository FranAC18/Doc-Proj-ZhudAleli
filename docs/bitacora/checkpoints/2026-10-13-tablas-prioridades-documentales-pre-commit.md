---
title: Tablas de sprints e historias ordenadas
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
  - "[[2026-10-13-sprint-backlog-documental-pre-commit]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/transversal
---

# Tablas de sprints e historias ordenadas

## Motivo y resultado

El tesista observó que las tablas de sprints e historias de usuario mostraban
la prioridad de forma desacomodada. Se prepararon nuevas ediciones que
separan **importancia cualitativa de HU** (Esencial, Alta, Complementaria),
**posición en la pila** (1–60) y **prioridad de planificación de tareas**.
Las primeras proceden de la clasificación documental de sus RF de origen.
Todas siguen siendo propuestas hasta la revisión correspondiente.

| Edición preparada | Resultado |
|---|---|
| `documentacion/historias/usuario/historias_usuario_v2.4_2026-10-13.md` | Tabla breve por bloque, ordenada por importancia, y criterios completos debajo. |
| `documentacion/pila_producto/pila_producto_v1.4_2026-10-13.md` | Resumen de importancia de HU separado del orden de 60 posiciones. |
| `documentacion/sprints/plan_sprints_v1.2_2026-10-13.md` | Fechas, trabajo y evidencia en columnas independientes. |
| `documentacion/sprints/sprint_backlog_v1.1_2026-10-13.md` | Prioridad de tarea, vínculos HU/HT y cierre en tres columnas. |
| `documentacion/sprints/plan_incremental_y_sprint_backlog_v1.3_2026-10-13.docx` | Tablas académicas reorganizadas y anexo de 51 HU con importancia y posición. |
| `documentacion/README.md` y `documentacion/control_de_cambios/registro_v2.4_2026-10-13.md` | Índice y registro de versiones actualizados. |

Las ediciones previas se conservan. Los scripts y la copia PDF usados para
preparar y revisar el Word están en `analisis/2026-10-13/orden-tablas/`; no
forman parte de la carpeta de entrega al docente.

## Comprobaciones reales

- Se cotejaron las 51 HU de v2.3 con v2.4: ID, necesidad, todos los criterios
  de aceptación y dependencias presentes. La importancia de las 51 coincide
  con su RF en la clasificación v1.2: 20 Esencial, 21 Alta y 10 Complementaria.
- Permanecen los 27 IDs de tareas del sprint backlog anterior y las 60
  posiciones de la pila base. El Word contiene los 51 IDs HU y las 27 tareas.
- Los enlaces locales de los seis Markdown afectados resuelven; no hay
  caracteres de reemplazo ni espacios finales en esos archivos.
- Se ejecutó el renderizador de la skill de documentos; no encontró
  LibreOffice. Como alternativa, Microsoft Word convirtió la edición v1.3 a
  PDF de ocho páginas y se inspeccionaron sus páginas en PNG. Las tablas no
  muestran celdas cortadas ni texto superpuesto.

## Pendientes

Las estimaciones del equipo, la revisión académica y la aprobación de las
prioridades propuestas no constan realizadas. Ningún sprint ni prueba de la
aplicación se declara terminado. **Commit y publicación de esta edición:
pendientes.** Antes de publicar, preparar en el clon separado una vista previa
del conjunto exacto y solicitar confirmación específica del tesista. Solo se
sincroniza `documentacion/`; este checkpoint y `analisis/` permanecen internos.
