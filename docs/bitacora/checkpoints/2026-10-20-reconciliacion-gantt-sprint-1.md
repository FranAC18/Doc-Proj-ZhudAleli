---
title: Conciliación del seguimiento local de Sprint 1
type: checkpoint
status: partially-complete
date: 2026-10-20
task_id: DOC-ORG-001
sprint: S1
phase: pre_commit
commit: pending
---

# Conciliación del seguimiento local de Sprint 1

## Alcance

Se cotejaron las cinco marcas locales `verificada` del Gantt con los criterios y estados
del sprint backlog Word v1.7 y sus fuentes relacionadas. El timebox ya estaba cerrado
administrativamente; este cotejo no reabre el periodo ni cambia su resultado parcial.

## Resultado por tarea

| Tarea | Estado canónico en v1.7 | Estado local conciliado | Hallazgo y trabajo pendiente |
|---|---|---|---|
| SB-S1-01 | Evidencia parcial | `en_curso` | Se identificó el registro de entrevista como fuente concreta. Falta documentar el cotejo criterio por criterio de actor, fecha, necesidad, dudas y catálogo. |
| SB-S1-02 | Validación académica pendiente | `bloqueada` | El reporte del tesista sobre un visto bueno verbal no precisa fecha, versión ni alcance y no hay acta. No acredita validación de esta tarea. |
| SB-S1-03 | Diseño por verificar | `en_curso` | Existe arquitectura detallada v1.1; siguen abiertas la cobertura de siete RF en historias/pila, seis ampliaciones y la ratificación de propietarios de RF-DOC-001/RF-AST-001. |
| SB-S1-04 | Validación de interfaz pendiente | `bloqueada` | Hay criterios documentales de diseño, pero no evidencia de validación de los recorridos móviles, errores y límites de datos locales con las usuarias. |
| SB-S1-05 | Estimación pendiente | `en_curso` | La estimación, responsables y capacidad siguen pendientes. El Gantt consignaba 2026-10-12 como fecha de verificación y citaba el Word v1.7 fechado 2026-10-14; la fecha anterior no queda demostrada por esa referencia. |

Los estados del Gantt son categorías locales generales; la columna de estado del backlog
conserva la formulación canónica. Ninguna tarea se declara completada. En el registro local
se retiraron la marca `verificada` y sus datos de verificador/fecha para las cinco tareas.
La fecha original de SB-S1-05 se conservó en la observación como dato no confirmado, sin
presentarla como fecha de cumplimiento. Las notas y la bitácora local registran el motivo
de cada cambio.

## Discrepancias conciliadas y límites

- **Cinco marcas de finalización frente al backlog:** conciliadas en el seguimiento local;
  tres tareas figuran `en_curso`, dos `bloqueada` y ninguna `verificada`.
- **Resumen de S1 en el Gantt:** actualizado para reflejar el cierre administrativo del
  2026-10-20 y el resultado parcial; se retiró el texto anterior que decía que no había
  cierre formal registrado.
- **Fecha de SB-S1-05:** se retiró del campo activo de verificación, pero su origen sigue
  pendiente de aclaración. La fecha del archivo citado no demuestra cuándo se realizó el
  trabajo subyacente.
- **Vistos buenos verbales:** se mantiene el reporte atribuido al tesista. Fecha, versión,
  alcance y constancia siguen sin evidencia; no se asignan a tareas específicas.
- **Sprint 1:** permanece `partially-complete`. La corrección del seguimiento no satisface
  las validaciones, decisiones o estimaciones pendientes.

## Trabajo pendiente

1. Completar referencias de historias y pila para RF-DOC-001, RF-AST-001, RF-INV-005,
   RF-INV-006, RF-PUB-003, RF-VEN-009 y RF-NOT-002.
2. Cotejar RF-ASI-006, RF-PLA-003, RF-NOT-001, RF-TRA-005, RF-GAS-001 y RF-REP-005.
3. Ratificar los propietarios de RF-DOC-001 y RF-AST-001 con el tesista.
4. Precisar, si existe esa información, fecha, versión y alcance de los vistos buenos
   verbales de Maria Camas y Julio Santillan.
5. Obtener la validación académica y de interfaz que requieren las fichas; completar
   estimación, asignación de responsables y revisión de capacidad.
6. Aclarar la fecha de verificación originalmente registrada para SB-S1-05.

Estos puntos no se completan mediante inferencia del asistente. El trabajo futuro debe
registrarse como nueva evidencia y no cambiar retroactivamente la línea base publicada.

## Fuentes

- [Plan y sprint backlog Word v1.7](../../../documentacion/sprints/plan_incremental_y_sprint_backlog_v1.7_2026-10-14.docx).
- [Sprint backlog Markdown v1.3](../../../documentacion/sprints/sprint_backlog_v1.3_2026-10-14.md).
- [Registro de entrevista v1.1](../../../documentacion/levantamiento/registro_entrevista_v1.1_2026-10-13.md).
- [Arquitectura detallada v1.1](../../../documentacion/arquitectura/arquitectura_v1.1_2026-10-19.md).
- [Criterios de diseño v1.0](../../../documentacion/diseno/criterios_diseno_v1.0_2026-10-12.md).
- [Reporte de vistos buenos verbales informado por el tesista](../../evidence/requirements/2026-10-20-reporte-aprobaciones-verbales-s1.md).
- `cronograma-interactivo/proyecto-local/estado/seguimiento_sprints_zhud_aleli.json` (seguimiento local).

## Paquete

Revisión y conciliación internas, sin commit ni publicación. La edición académica de
seguimiento v1.1 queda preparada para revisión y la transferencia al repositorio del docente
permanece fuera de este cambio.
