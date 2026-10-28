---
titulo: "Plan de definición e implementación de acceso y superadministración"
version: "1.2"
fecha: 2026-10-27
autor: Tesista
estado: "aprobado-por-el-tesista; preparado-para-revision-academica"
aprobado_por: Tesista
fecha_aprobacion: 2026-10-27
evidencia_aprobacion: "Instrucción explícita del tesista en la sesión del 2026-10-27"
alcance_aprobacion: "Plan y secuencia S1/S2; no aprueba RF-ACC-005, SPEC-002 ni implementación de código por sí solos"
validacion_presidencial_rol: "validado por la presidenta (según el tesista)"
evidencia_validacion_presidencial: "pendiente de adjuntar"
publicacion: pendiente-de-transferencia
fuente_interna: "Plan de implementación de superadministración v1.1, 2026-10-27, aprobado por el tesista"
---

# Plan de definición e implementación de acceso y superadministración

## Propósito y estado

Este plan organiza la definición documental del proceso de acceso y del rol de
superadministradora, y la implementación posterior de lo definido. El tesista aprobó el plan
el 2026-10-27 y pidió incorporarlo a `documentacion/`. La edición está preparada localmente
para revisión académica; no se ha transferido ni publicado.

La aprobación cubre el plan y la secuencia de trabajo S1/S2. No confirma `RF-ACC-005`, no
aprueba SPEC-002 ni modifica SPEC-001. Tampoco registra como terminados los entregables de S1
o las verificaciones de S2.

## Validación reportada del rol

El tesista declaró el 2026-10-27 que la presidenta validó expresamente el rol de
superadministradora con autoridad para gestionar todo el sistema. El estado se registra como
«validado por la presidenta (según el tesista)». La evidencia queda «pendiente de adjuntar»;
se solicitó al tesista la referencia.

La autoridad comprende la administración del sistema mediante las operaciones autorizadas
que ofrece cada módulo. Los criterios de cada operación, el alcance de consulta y la
profundidad de cambios por módulo siguen sujetos a definición. Este reporte no aprueba por sí
solo todos los requisitos ni sus criterios.

## Alcance funcional que se define en S1

### Login, cuenta y sesión

- Definir inicio y cierre de sesión con mensajes de error comunes que no revelen si la cuenta
  existe.
- Definir conteo de intentos fallidos, bloqueo temporal, consulta de estado y desbloqueo
  administrativo.
- Definir duración y expiración de sesión por inactividad, y cierre de sesiones activas al
  desactivar una cuenta o revocar sus permisos.
- No habrá autorregistro de usuarias. La superadministradora crea las cuentas.
- Definir la credencial inicial, el cambio obligatorio en el primer acceso, su expiración y
  uso único.
- Definir el restablecimiento administrado: canal, verificación de identidad, expiración, uso
  único, revocación y auditoría. Nunca se muestra una contraseña existente.
- Una cuenta desactivada no inicia sesión ni conserva sesiones activas.
- Definir y validar el arranque seguro: cómo se crea la primera superadministradora sin
  exponer credenciales ni introducir puertas traseras.

SPEC-001 conserva como valores por defecto tres fallos dentro de tres minutos, bloqueo de tres
minutos y expiración por 30 minutos de inactividad, hasta que se valide un cambio. Los mensajes
genéricos solicitados para no revelar la existencia de una cuenta difieren de los criterios
vigentes CA-ACC-001-02/03, que distinguen errores de cuenta inexistente y contraseña. La
definición de S1 debe resolver la discrepancia y documentar la validación antes de cambiar la
especificación confirmada.

### Capacidades administrativas

- Crear usuarios; activar y desactivar cuentas.
- Asignar y retirar módulos por usuario.
- Conceder y revocar roles y permisos.
- Consultar intentos fallidos por cuenta y estado de bloqueo; desbloquear cuentas.
- Configurar desde la interfaz el umbral de intentos, minutos de bloqueo y tiempo de
  inactividad. Definir rangos mínimo y máximo, validación y un historial de cambios con actor,
  fecha, valor anterior, valor nuevo y motivo. Los límites numéricos siguen pendientes de
  definición y validación.
- Gestionar fórmulas de pesaje, incluidos merma y rendimiento, tipos de plantas y otros
  catálogos o parámetros que cada módulo declare configurables, sin acceso directo a la base
  de datos.
- Representar fórmulas como expresiones restringidas, validadas, versionadas y con vigencia;
  permitir prueba previa, prohibir código arbitrario y conservar los cálculos históricos sin
  recálculo retroactivo por una fórmula nueva.
- Consultar y gestionar datos de todos los módulos mediante sus operaciones administrativas,
  con auditoría. Cada módulo define la profundidad permitida para altas, modificaciones,
  bajas y correcciones históricas.

En S1 se define y valida el acceso y la configuración base de acceso. Se identifican las
configuraciones y operaciones administrativas de cada módulo; la profundidad de los datos,
catálogos y fórmulas específicos se define módulo por módulo.

## Secuencia y fechas acordadas

| Sprint | Alcance | Fechas comunicadas | Estado |
|---|---|---|---|
| S1 | Definición y validación documental: requisitos, historias, especificación, matriz de permisos y diseño de pantallas para login y superadministración. | El plan de sprints v1.4 inicia el 2026-09-15; el tesista indicó que S1 culmina el 2026-10-27. | Periodo concluido por calendario al 2026-10-27; el cumplimiento de cada entregable requiere cotejo y evidencia. Capacidad y estimaciones pendientes. |
| S2 | Implementación de lo definido para login y superadministración. | 2026-10-14 a 2026-10-29, según el tesista. | `SB-S2-02` permanece activo; las verificaciones no se declaran completas. |

Los intervalos comunicados se superponen del 2026-10-14 al 2026-10-27. Se registran tal como
fueron indicados. No se asignan puntos ni disponibilidad sin los datos de capacidad pendientes.

Esta asignación reemplaza, para el acceso y la superadministración, la nota anterior de no
alterar S1–S6 y posponer la administración hasta después del trabajo activo de acceso. Las
notas anteriores se conservan como historial.

La definición de operaciones específicas de datos y configuración por módulo no habilita su
implementación automática en S2: cada operación requiere alcance, validación, responsable y
sprint definidos para el módulo propietario.

## Criterios de diseño e implementación

1. Cada solicitud sensible valida en el servidor la cuenta activa, la sesión, el permiso, el
   módulo, el recurso y la operación.
2. El panel utiliza operaciones públicas del módulo propietario; no ejecuta escrituras
   genéricas ni ofrece acceso directo a tablas.
3. El módulo dueño valida y registra los cambios. Las operaciones con varias entidades usan
   una transacción; las correcciones históricas conservan el original y crean una rectificación
   trazable cuando corresponda.
4. Los cambios de política de acceso registran actor, fecha, valor anterior, valor nuevo y
   motivo. Los límites aprobados se validan en el servidor.
5. Las fórmulas no ejecutan Python, SQL ni código arbitrario. Cada versión conserva expresión,
   pruebas, unidades, vigencia y relación con los cálculos producidos.
6. Las sesiones y permisos revocados se invalidan conforme a la regla definida; una sesión
   previa no omite la comprobación de permisos vigente.
7. La interfaz contempla uso móvil, teclado y tecnologías de asistencia; las vistas privadas
   no se incorporan a cachés compartidas de la PWA.

## Decisiones y validaciones pendientes

- Adjuntar la referencia de evidencia de la validación presidencial reportada por el tesista.
- Definir el alta inicial de la superadministradora, la delegación, revocación y transferencia
  de autoridad.
- Acordar el canal y los controles de verificación para restablecimiento de contraseña.
- Definir rangos mínimo y máximo para intentos y bloqueos; cualquier cambio de valores requiere
  revisión y validación de SPEC-001.
- Resolver la discrepancia entre los mensajes genéricos solicitados y los mensajes vigentes de
  SPEC-001.
- Definir para cada módulo los catálogos, fórmulas, permisos, operaciones, auditoría y alcance
  de corrección histórica.
- Confirmar la capacidad y las estimaciones de S1/S2 sin dar por completadas tareas pendientes.
- Completar las revisiones funcionales, de seguridad, accesibilidad y PWA antes de declarar
  implementado el alcance.

## Aprobación y control de cambios

| Fecha | Autoridad | Decisión | Fuente | Alcance |
|---|---|---|---|---|
| 2026-10-27 | Tesista | Aprueba el plan de superadministración y solicita documentarlo en `documentacion/`. | Instrucción explícita del tesista en la sesión del 2026-10-27. | Plan y secuencia S1/S2; no confirma RF-ACC-005 ni SPEC-002. |

| Versión | Fecha | Estado | Cambio |
|---|---|---|---|
| 1.1 | 2026-10-27 | Fuente interna aprobada | Plan técnico de superadministración aprobado por el tesista. |
| 1.2 | 2026-10-27 | Aprobado por el tesista; preparado para revisión académica | Se incorpora el alcance funcional de acceso solicitado, la secuencia S1/S2, el cierre de S1 por calendario y el estado reportado de la validación presidencial, conservando la evidencia pendiente y los requisitos no aprobados. |
