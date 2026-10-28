---
titulo: Cierre de Sprint 1 y registro de vistos buenos verbales
codigo: ZA-SEG-003
version: "1.0"
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

Este informe registra el cierre administrativo del Sprint 1 del calendario vigente,
concilia las diferencias observadas entre el Gantt local y el backlog documentado, y
recoge los vistos buenos verbales reportados por el tesista. Se prepara para revisión
académica. La fecha del informe es 20 de octubre de 2026; no equivale a la fecha de las
autorizaciones verbales, que no fue precisada.

## Resultado de Sprint 1

El Sprint 1 del plan de sprints v1.3 corresponde a requisitos y diseño, con periodo
planificado del 15 de septiembre al 12 de octubre de 2026. El tesista solicitó cerrar el
timebox el 20 de octubre. El periodo queda **cerrado administrativamente con resultado
parcial**. Esto permite continuar el calendario y trasladar el trabajo remanente; no
declara terminados todos los criterios del sprint.

| Criterio | Resultado al corte |
|---|---|
| Periodo del S1 del calendario | 15 sep-12 oct 2026; cierre administrativo registrado el 20 oct 2026. |
| Resultado | Parcialmente completo; se conservan brechas de evidencia, cotejo de criterios y trazabilidad. |
| S1 técnico de SPEC-001 | Etiqueta histórica para acceso; corresponde al S2 de acceso en el calendario vigente. |
| Aplicación Django | No implementada como aplicación del proyecto; el S1 del calendario es de requisitos y diseño. |

## Vistos buenos verbales reportados

El tesista informó el 20 de octubre de 2026 que:

- **Maria Camas**, encargada de la organización, autorizó verbalmente.
- **Julio Santillan**, profesor de Aplicaciones Informáticas 2, dio el visto bueno durante
  una presentación del proyecto.

El tesista indicó que no hay actas ni constancias. No se registraron la fecha exacta de
cada autorización, los archivos/versiones revisados ni el alcance preciso. En consecuencia,
este informe atribuye la declaración al tesista y no afirma que cada visto bueno cubra todos
los requisitos, criterios o tareas de S1. Tampoco constituye confirmación directa de las
personas mencionadas ni reemplaza una constancia institucional si fuera requerida.

## Discrepancias verificadas

| Código | Estado del backlog Word v1.7 | Estado del Gantt local (exportado 20-10) | Conciliación |
|---|---|---|---|
| SB-S1-01 | Evidencia parcial | `verificada`; reviewer Franklin; fecha 2026-10-19; referencia a carpeta de levantamiento. | La carpeta contiene documentos de entrevista, pero el Gantt no identifica cuál satisface cada criterio de la ficha. |
| SB-S1-02 | Validación académica pendiente | `verificada`; reviewer Franklin; fecha 2026-10-19; referencia a carpeta de alcance. | El visto bueno verbal de Julio y la autorización de Maria se reportan, pero no se especificó qué versión o criterios cubrieron. |
| SB-S1-03 | Diseño por verificar | `verificada`; reviewer Franklin; fecha 2026-10-19; referencia a carpeta de arquitectura. | Existe arquitectura detallada v1.1, pero el enlace local no traza su contenido a los criterios de aceptación ni identifica la versión presentada. |
| SB-S1-04 | Validación de interfaz pendiente | `verificada`; reviewer Franklin; fecha 2026-10-19; referencia a carpeta de diseño. | No se indicó que la presentación aprobada incluyera los recorridos móviles o criterios de interfaz de esta tarea. |
| SB-S1-05 | Estimación pendiente | `verificada`; reviewer Franklin; fecha de verificación 2026-10-12; referencia al plan/backlog Word v1.7. | El archivo v1.7 tiene fecha 2026-10-14, posterior a la fecha de verificación consignada. No se corrigen datos hasta confirmar si se usó una edición previa o si una fecha está equivocada. |

Las cinco fichas del backlog Word v1.7 también dejan puntos y responsables pendientes.
El seguimiento local no registra una correspondencia por criterio entre cada ficha y sus
rutas de evidencia. Se preserva el Gantt; sus marcas no sustituyen el estado de aceptación
del backlog hasta completar ese cotejo.

| Tema | Discrepancia | Conciliación |
|---|---|---|
| Numeración | SPEC-001 y su plan técnico conservan `S1` para acceso. | En el plan de calendario v1.3, S1 es requisitos y diseño y S2 es acceso. Se mantienen diferenciadas ambas referencias. |
| Cierre del periodo | El Gantt registra S1 como cerrado y las cinco tareas verificadas. | Se confirma el cierre administrativo del timebox el 20-10-2026; el resultado sigue parcial mientras las discrepancias de tarea estén abiertas. |
| Vistos buenos | Antes del 20-10, el índice y reportes decían pendientes por falta de información. | Se incorpora el reporte del tesista sobre los vistos buenos verbales de Julio Santillan y Maria Camas. Fecha, versión y alcance siguen sin identificar; no se presume cobertura total. |

La verificación del Gantt y el estado del backlog describen niveles de seguimiento distintos.
Para declarar una tarea completa, las rutas locales deben cotejarse contra sus criterios y
el resultado debe registrarse en una edición revisada del backlog. Este informe no modifica
retroactivamente los documentos v1.3 o v1.7.

## Trabajo que continúa después del timebox

1. Incorporar referencias en historias y pila para RF-DOC-001, RF-AST-001, RF-INV-005,
   RF-INV-006, RF-PUB-003, RF-VEN-009 y RF-NOT-002.
2. Cotejar las ampliaciones de RF-ASI-006, RF-PLA-003, RF-NOT-001, RF-TRA-005,
   RF-GAS-001 y RF-REP-005.
3. Ratificar los propietarios de RF-DOC-001 y RF-AST-001.
4. Precisar fecha, material y alcance de los vistos buenos verbales; aclarar la fecha y
   evidencia de SB-S1-05.
5. Revisar el alcance general v1.3, propuestas modulares y decisiones abiertas aplicables,
   incluida P-03.
6. Mantener cerrada la puerta T012 de SPEC-001 hasta completar y validar T001-T011.

No se reasignan tareas ni se modifican las fechas del calendario en este informe. Los
pendientes se conservan para su planificación posterior.

## Fuentes consultadas

- [Plan de sprints v1.3](../sprints/plan_sprints_v1.3_2026-10-14.md).
- [Sprint backlog v1.3](../sprints/sprint_backlog_v1.3_2026-10-14.md).
- [Plan incremental y sprint backlog Word v1.7](../sprints/plan_incremental_y_sprint_backlog_v1.7_2026-10-14.docx).
- [Registro de cobertura y pendientes v1.0](pendientes_trazabilidad_v1.0_2026-10-19.md).
- Reporte verbal del tesista recibido el 20-10-2026; no hay actas ni constancias.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-20 | Cierre administrativo parcial de S1, conciliación del Gantt con el backlog y registro atribuido al tesista de los vistos buenos verbales. Preparado para revisión. |
