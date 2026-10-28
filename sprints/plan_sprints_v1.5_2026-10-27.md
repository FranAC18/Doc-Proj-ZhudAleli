---
titulo: Plan de fases y sprints hasta el 23 de diciembre de 2026
version: "1.5"
fecha: 2026-10-27
autor: Franklin Acero
estado: preparado-para-revision-academica
fuentes: "Decisiones del tesista del 2026-10-27; CAT-REQ-001 v1.2; plan_sprints v1.4; hoja de ruta operativa del 2026-10-27"
revision_directora: pendiente
publicacion: pendiente-de-transferencia
---

# Plan de fases y sprints hasta el 23 de diciembre de 2026

## Objetivo y reglas de planificación

El resultado prioritario para el **23 de diciembre de 2026** es avanzar el objetivo
específico 2: módulos de gestión organizacional, trazabilidad productiva y control de
acceso mediante un enfoque ágil basado en Scrum. El tesista y Codex forman el equipo de
desarrollo. La disponibilidad comunicada por el tesista es de **16 a 25 horas por semana**;
la capacidad efectiva y la estimación de cada historia se comprueban durante el trabajo.

Una historia pasa al compromiso del sprint solo cuando tiene actor, resultado, criterio
verificable, dependencia y capacidad identificados. Estar en la pila o en este mapa no
significa estar comprometida ni terminada. Las pruebas, permisos, integridad de datos y
documentación afectada acompañan cada incremento. Al cierre se registra el resultado real
y lo pendiente, sin convertir el fin del periodo en aprobación de una funcionalidad.

## Calendario revisado

S1 conserva documentación y aspectos técnicos. El tesista extendió su periodo hasta el
**27 de octubre de 2026**; su cierre por calendario no da por completados los entregables
parciales. S2 comenzó mientras S1 seguía en curso, según el registro anterior. Las fechas
intermedias siguientes son **propuestas de trabajo**, sujetas a capacidad y revisión del
tesista. La fecha objetivo del 23 de diciembre, el término del periodo S1 y la distribución
funcional S1–S5 fueron comunicados como decisiones.

| Periodo | Fechas | Resultado priorizado | Evidencia de salida |
|---|---|---|---|
| S1 | 15 sep–27 oct; periodo concluido | Requisitos, fuentes, arquitectura, diseño, decisiones de acceso y mapa conceptual de datos. | Estado de cada entregable con evidencia; pendientes conservados. |
| S2 | En curso; cierre propuesto 8 nov | Login, cuentas, autoridad y permisos de superadministración validados; estructura de acceso de módulos futuros. | Recorridos permitidos y denegados, migraciones y pruebas del acceso; sin declarar funciones futuras construidas. |
| S3 | 9–19 nov, propuesta | Planificación organizacional: actividades, responsables y encargos en un recorrido usable. | Crear, asignar y consultar con autorización y pruebas. |
| S4 | 20–30 nov, propuesta | Asistencia, participación y correcciones con historial; continuidad sin red solo según reglas aprobadas. | Registro, denegación, prevención de duplicados y evidencia de corrección. |
| S5 | 1–20 dic, propuesta | Primera cadena de trazabilidad productiva: catálogo, acopio, secado, lotes y existencias; comercio y rendición según capacidad y reglas aprobadas. | Seguir un lote y conciliar movimientos; alcance adicional explícito. |
| Integración y entrega | 21–23 dic, propuesta | Regresión entre recorridos, evidencia de uso, documentación y pendientes. | Resultado comprobado del objetivo 2 y límites de lo entregado. |

Las 23 historias antes agrupadas en S5 no se prometen por el mero calendario. Reportes
útiles se construyen con los módulos que producen sus datos, sin reservar un S6 separado.
Las ediciones anteriores S2–S6 quedan como historial de planificación y sus códigos se
conservan para trazabilidad, sin mover automáticamente tareas a otro sprint. El sprint
backlog v1.4 refleja compromisos y estados del corte anterior; se actualizará por tareas
concretas conforme se seleccionen, sin reescribir logros ni completar pendientes.

## Capacidad orientativa desde el 27 de octubre

| Periodo restante | Horas orientativas del tesista | Complejidad relativa |
|---|---:|---|
| S2, 27 oct–8 nov | 30–46 | Alta: identidad, autorización y configuración sensible. |
| S3, 9–19 nov | 25–39 | Media: planificación y asignaciones. |
| S4, 20–30 nov | 25–39 | Alta: asistencia, correcciones y política sin red. |
| S5, 1–20 dic | 46–71 | Muy alta: datos productivos, lotes y existencias. |
| Integración, 21–23 dic | 7–11 | Regresión, evidencia y entrega. |

El total aproximado es **130–205 horas** antes de contingencias, validación con usuarias
y otras obligaciones. No es una estimación de esfuerzo de las historias ni una promesa
de que toda la pila entre en diciembre.

## Modelo de datos por incrementos

En S1 se identifica el significado de las entidades, el dueño de sus escrituras, sus
relaciones esenciales y reglas de integridad. En S2 se consolida el modelo físico de
identidad, cuentas, membresía y autoridad con migraciones reproducibles. En S3–S5 cada
recorrido añade las tablas, restricciones e historial que necesita su módulo, con pruebas
de integridad y compatibilidad. Los cálculos, fórmulas y reglas económicas pendientes
requieren validación antes de generar o transformar datos reales.

## Superadministración y límites de S2

S2 prepara la estructura y los permisos de los módulos previstos; las funciones de
gestión organizacional y trazabilidad se desarrollan en S3–S5. Para aceptar una
operación administrativa se prueba una solicitud autorizada y otra denegada en el
servidor, sin mutación en el caso denegado. Las altas y cambios de cuentas, la
asignación o retiro de acceso y los cambios de política conservan actor, fecha,
recurso, resultado y valores pertinentes. El panel no permite cambiar datos de un
módulo mediante edición genérica ni mostrar contraseñas o secretos.

El rol de superadministradora fue comunicado por el tesista como validado por la
presidenta; la referencia de evidencia sigue pendiente. `RF-ACC-005` y su detalle
operativo continúan propuestos. Antes de habilitar el panel se deben resolver la
designación inicial, la delegación, el efecto de revocaciones sobre sesiones y los
límites de consulta. Los parámetros actuales de login permanecen vigentes hasta
validar cualquier cambio. Las operaciones sobre datos, catálogos y fórmulas se
especificarán con cada módulo propietario.

## Seguimiento y fuentes

La pila ordena valor y dependencias; el sprint backlog registra solo compromisos y
estado verificable. Los cambios en historias y requisitos se documentan en su fuente
interna y se incorporan a la edición académica en hitos revisados. Este plan actualiza
el calendario de [v1.4](plan_sprints_v1.4_2026-10-21.md), conservada como antecedente;
la revisión de la directora y la transferencia al repositorio documental siguen
pendientes.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.4 | 2026-10-21 | Plan S1–S6 y aceptación de las historias técnicas de preparación asignadas a S1. | Edición anterior conservada. |
| 1.5 | 2026-10-27 | Se distribuyen los resultados S2–S5 hasta el 23 de diciembre, se incorpora capacidad comunicada y diseño de datos incremental; se separan decisiones de alcance de fechas intermedias propuestas. | Preparado para revisión académica; no publicado. |
