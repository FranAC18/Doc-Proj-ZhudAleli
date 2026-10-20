---
title: Cierre de Sprint 1 con resultado parcial
type: checkpoint
status: partially-complete
date: 2026-10-20
sprint: S1
module: transversal
phase: pre_commit
commit: pending
timebox_status: closed
completion_status: partially-complete
authorized_by: tesista
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - sprint/s1
  - estado/partially-complete
related:
  - "[[docs/evidence/requirements/2026-10-20-reporte-aprobaciones-verbales-s1]]"
  - "[[docs/evidence/requirements/2026-10-13-reporte-revision-docente-en-clase]]"
  - "[[documentacion/seguimiento/cierre_sprint_1_y_vistos_buenos_v1.0_2026-10-20]]"
  - "[[documentacion/seguimiento/pendientes_trazabilidad_v1.0_2026-10-19]]"
  - "[[specs/001-acceso-usuarias-internas/tasks]]"
  - "[[docs/00-inicio/00-dashboard]]"
---

# Cierre de Sprint 1 con resultado parcial

## Decisión registrada

Por solicitud del tesista, el timebox de Sprint 1 se cierra administrativamente el
2026-10-20. Su ventana planificada fue del 15 de septiembre al 12 de octubre de 2026.
El resultado se conserva como `partially-complete`: cerrar el periodo permite continuar
el plan y registrar el trabajo pendiente, pero no acredita que las tareas hayan terminado
ni sustituye las revisiones académica y organizacional.

La autorización cubre el cierre del timebox. No aprueba por sí sola requisitos, criterios
de aceptación, decisiones abiertas, revisión de la directora, validación de la
organización ni trabajo de desarrollo sin evidencia.

## Aclaración sobre autorizaciones verbales - 2026-10-20

El tesista reporta que Maria Camas, encargada de la organización, autorizó verbalmente,
y que Julio Santillan, profesor de Aplicaciones Informáticas 2, dio el visto bueno durante
una presentación del proyecto. No hay actas ni constancias. La fecha exacta, versión y
alcance de cada visto bueno no fueron precisados; por tanto, no se asignan a requisitos,
criterios o tareas específicas sin ese cotejo. El reporte se conserva como tal y no convierte
las tareas incompletas en completadas.

## Numeración de sprints

En el calendario vigente, S1 corresponde a requisitos y diseño; S2 corresponde a acceso
y administración. La etiqueta histórica `S1` de SPEC-001 y su plan técnico describe
acceso y se interpreta como trabajo del S2 del calendario. El dashboard local ya registra
el cierre del timebox S1; su indicador no significa que el resultado sea completo.

## Resultado de las tareas de S1

El backlog Word v1.7 conserva cinco tareas de S1 y sus estados:

| Código | Historia técnica | Estado registrado |
|---|---|---|
| SB-S1-01 | HT-PRE-001 | Evidencia parcial |
| SB-S1-02 | HT-PRE-002 | Validación académica pendiente |
| SB-S1-03 | HT-PRE-003 | Diseño por verificar |
| SB-S1-04 | HT-PRE-004 | Validación de interfaz pendiente |
| SB-S1-05 | HT-PRE-005, HT-GEN-008 | Estimación pendiente |

Las cinco fichas dejan puntos y responsables pendientes. S1 usa todas las HU como insumo
de revisión y destaca HU-PWA-001 para los recorridos móviles; esa relación no marca
historias ni tareas como completadas. HT-GEN-008 permanece en exploración.

El seguimiento local del Gantt registra las cinco tareas como `verificada`, con Franklin
como revisor y rutas locales de evidencia. El backlog canónico v1.7 mantiene los estados
parciales y pendientes de la tabla. Se conserva intacto el seguimiento local, pero sus
marcas no sustituyen los criterios de cada ficha: queda pendiente cotejar esas rutas y
registrar cualquier resultado nuevo en una edición autorizada del backlog.

En la actualización de SB-S1-05, el Gantt muestra fecha de verificación 2026-10-12,
mientras la evidencia citada es el plan/backlog Word v1.7, fechado 2026-10-14. La
cronología queda señalada para aclaración; no se corrige la fecha ni se reemplaza el
documento sin confirmar cuál dato es correcto.

## Trabajo que sigue abierto

- Incorporar historias y referencias de los siete RF sin referencia en HU/pila:
  RF-DOC-001, RF-AST-001, RF-INV-005, RF-INV-006, RF-PUB-003, RF-VEN-009 y RF-NOT-002.
- Cotejar las ampliaciones de RF-ASI-006, RF-PLA-003, RF-NOT-001, RF-TRA-005,
  RF-GAS-001 y RF-REP-005, manteniendo abiertas las decisiones de detalle.
- Ratificar la asignación de responsables de RF-DOC-001 y RF-AST-001 en las fuentes
  correspondientes.
- Precisar fecha, versión, material y alcance del visto bueno verbal de Julio Santillan;
  confirmar qué entregables académicos de S1 cubrió.
- Precisar fecha, material y alcance de la autorización verbal de Maria Camas para
  registrar qué novedades organizacionales cubrió; no existe acta ni constancia escrita.
- Revisar el alcance general v1.3, las propuestas modulares y las decisiones abiertas
  aplicables, incluida P-03.
- Mantener la puerta T012 de SPEC-001 cerrada hasta completar y validar sus entregables
  de diseño T001-T011. Esto corresponde a la etiqueta técnica histórica S1/acceso,
  planificada como S2 del calendario.

No se reasignan tareas a otro sprint ni se modifican las fechas del calendario en este
cierre. El remanente se conserva como trabajo pendiente para planificación posterior.

## Fuentes revisadas

- [[../../../documentacion/sprints/plan_sprints_v1.3_2026-10-14|Plan de sprints v1.3]].
- [[../../../documentacion/sprints/sprint_backlog_v1.3_2026-10-14|Sprint backlog v1.3]].
- [[../../../documentacion/sprints/plan_incremental_y_sprint_backlog_v1.7_2026-10-14.docx|Plan y sprint backlog Word v1.7]].
- [[../../../documentacion/seguimiento/pendientes_trazabilidad_v1.0_2026-10-19|Registro de cobertura y pendientes]].
- [[../../../docs/evidence/requirements/2026-10-13-reporte-revision-docente-en-clase|Reporte de revisión docente en clase]].
- [[../../../specs/001-acceso-usuarias-internas/tasks|Tareas de SPEC-001]].
- [[../../../cronograma-interactivo/proyecto-local/estado/seguimiento_sprints_zhud_aleli.json|Estado local del dashboard]].
- [[../ESTADO-ACTIVO|Estado activo de continuidad]].

## Paquete pre_commit

El commit interno solicitado incluye unicamente este checkpoint y el reporte de evidencia:

- `docs/bitacora/checkpoints/2026-10-20-cierre-sprint-1-parcial.md`
- `docs/evidence/requirements/2026-10-20-reporte-aprobaciones-verbales-s1.md`

La carpeta `documentacion/` esta excluida del repositorio del proyecto y se reserva para
la edicion destinada al docente. El informe de S1, su indice y el registro de cambios se
prepararon alli; no se agregan a este commit. Su transferencia al repositorio documental
del docente queda pendiente de cotejo y vista previa en el clon separado.

La revision del conjunto interno exacto, sus enlaces y `git diff --check` se completa antes
de ejecutar el commit.