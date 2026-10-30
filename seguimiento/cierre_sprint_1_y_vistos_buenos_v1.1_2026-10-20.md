---
titulo: Cierre de Sprint 1 y registro de vistos buenos verbales
codigo: ZA-SEG-003
version: "1.1"
fecha: 2026-10-20
autor: Franklin Acero
elaboracion: Asistencia de Codex a solicitud del tesista
estado: preparado-para-revision
publicacion: pendiente-de-transferencia
sprint: S1
timebox: cerrado
resultado: parcialmente-completo
---

# Cierre de Sprint 1 y registro de vistos buenos verbales

## Propósito y corte de información

Esta edición conserva el cierre administrativo del Sprint 1 y actualiza la conciliación
de su seguimiento local. El plan fija S1 para requisitos y diseño, del 15 de septiembre al
12 de octubre de 2026. El tesista solicitó cerrar administrativamente el timebox el 20 de
octubre. El resultado es **parcialmente completo**. Esta edición está preparada para
revisión académica; no declara terminado el sprint ni cambia retroactivamente el backlog
Word v1.7.

La etiqueta `S1` histórica de SPEC-001 y su plan técnico se refiere a acceso y corresponde
al S2 del calendario vigente. El estado de T012 de SPEC-001 no cambia.

## Resultado de la conciliación

El backlog Word v1.7 mantiene los estados canónicos de las cinco tareas. El Gantt local
había marcado las cinco como `verificada`, con referencias generales a carpetas y sin
vincular los criterios de cada ficha a evidencia concreta. El 20 de octubre se cotejaron
las fichas y sus fuentes y se actualizaron las marcas locales: se retiraron los cinco
estados `verificada` y los datos de verificador/fecha asociados. La bitácora del Gantt
conserva el motivo de cada cambio. El resumen del sprint en el Gantt también quedó
actualizado para reflejar el cierre administrativo parcial del 20 de octubre.

| Código | Estado canónico del backlog v1.7 | Estado local conciliado | Resultado del cotejo |
|---|---|---|---|
| SB-S1-01 | Evidencia parcial | `en_curso` | El registro de entrevista es una fuente concreta. Aún falta el cotejo documentado de actor, fecha, necesidad, dudas y catálogo contra el criterio de la ficha. |
| SB-S1-02 | Validación académica pendiente | `bloqueada` | El visto bueno verbal de Julio Santillan fue reportado por el tesista, pero no se identificaron fecha, versión ni alcance y no hay acta. No acredita esta validación. |
| SB-S1-03 | Diseño por verificar | `en_curso` | Existe arquitectura detallada v1.1, pero siguen pendientes la cobertura de siete RF, el cotejo de seis ampliaciones y la ratificación de propietarios de RF-DOC-001/RF-AST-001. |
| SB-S1-04 | Validación de interfaz pendiente | `bloqueada` | Hay criterios documentales de diseño; no hay evidencia de validación con usuarias de recorridos móviles, errores y límites de datos locales. |
| SB-S1-05 | Estimación pendiente | `en_curso` | Estimación, responsables y capacidad siguen pendientes. El Gantt consignaba 2026-10-12 como fecha de verificación y citaba el Word v1.7 fechado 2026-10-14. Se retiró la fecha del campo activo; su origen aún requiere aclaración. |

Los estados del Gantt son categorías operativas generales y no sustituyen la redacción
canónica del backlog. Las categorías `bloqueada` indican que la validación correspondiente
requiere evidencia o participación externa antes de poder verificarse; no suponen rechazo.
La fecha 2026-10-14 del Word v1.7 demuestra cuándo está fechada esa edición, pero por sí
sola no demuestra cuándo se completó el trabajo de SB-S1-05. Por eso no se afirma una fecha
de cumplimiento. Ninguna tarea está marcada como verificada después de la conciliación.

El reporte interno detallado está en el
[checkpoint de conciliación del Gantt](../../docs/bitacora/checkpoints/2026-10-20-reconciliacion-gantt-sprint-1.md).

## Vistos buenos verbales reportados

El tesista informó el 20 de octubre de 2026 que Maria Camas, encargada de la organización,
autorizó verbalmente y que Julio Santillan, profesor de Aplicaciones Informáticas 2, dio
el visto bueno durante una presentación del proyecto. Según el tesista, no hay actas ni
constancias. La fecha exacta, los archivos/versiones revisados y el alcance de cada visto
bueno no se precisaron. Esta edición atribuye el reporte al tesista; no representa
confirmación directa de las personas mencionadas ni asigna esos vistos buenos a tareas
concretas.

## Discrepancias resueltas y pendientes

- **Resuelta en el seguimiento local:** la contradicción entre cinco marcas `verificada`
  y los estados incompletos del backlog. El Gantt ahora registra tres tareas `en_curso`,
  dos `bloqueada` y ninguna `verificada`.
- **Parcialmente aclarada:** SB-S1-05 ya no presenta 2026-10-12 como fecha de verificación
  activa. La fecha originalmente escrita permanece identificada como no confirmada, a la
  espera de precisar su origen.
- **Abiertos:** siete RF sin referencia en historias/pila; seis ampliaciones por cotejar;
  propietarios de RF-DOC-001/RF-AST-001 por ratificar; vistos buenos sin fecha, versión o
  alcance; validaciones académica y de interfaz; y estimación, responsables y capacidad.

No se cambiaron las fechas del calendario, la asignación de sprints ni el estado de SPEC-001.
La revisión académica, la validación organizacional y las estimaciones requieren evidencia
de sus responsables; no se completan por inferencia.

## Fuentes consultadas

- [Plan de sprints v1.3](../sprints/plan_sprints_v1.3_2026-10-14.md).
- [Sprint backlog v1.3](../sprints/sprint_backlog_v1.3_2026-10-14.md).
- [Plan incremental y sprint backlog Word v1.7](../sprints/plan_incremental_y_sprint_backlog_v1.7_2026-10-14.docx).
- [Registro de entrevista v1.1](../levantamiento/registro_entrevista_v1.1_2026-10-13.md).
- [Arquitectura detallada v1.1](../arquitectura/arquitectura_v1.1_2026-10-19.md).
- [Criterios de diseño v1.0](../diseno/criterios_diseno_v1.0_2026-10-12.md).
- [Registro de cobertura y pendientes v1.0](pendientes_trazabilidad_v1.0_2026-10-19.md).
- [Reporte del tesista sobre vistos buenos verbales](../../docs/evidence/requirements/2026-10-20-reporte-aprobaciones-verbales-s1.md).
- Seguimiento del Gantt local: `cronograma-interactivo/proyecto-local/estado/seguimiento_sprints_zhud_aleli.json`.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| [1.0](cierre_sprint_1_y_vistos_buenos_v1.0_2026-10-20.md) | 2026-10-20 | Cierre administrativo parcial de S1 y reporte atribuido al tesista de vistos buenos verbales; discrepancias de Gantt/backlog aún sin conciliar. |
| 1.1 | 2026-10-20 | Se cotejan los cinco estados con el backlog v1.7, se corrigen las marcas locales del Gantt y se mantiene pendiente la aclaración de la fecha original de SB-S1-05. Preparado para revisión; transferencia pendiente. |
