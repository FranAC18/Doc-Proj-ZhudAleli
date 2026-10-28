---
titulo: Historias de usuario en fichas
version: "2.6"
fecha: 2026-10-27
autor: Tesista
estado: propuesta-interna-pendiente-de-validacion
historias: 56
historias_base: 51
historias_propuestas_adicionales: 5
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Historias de usuario

Esta propuesta conserva las 51 historias de la edición [v2.5](../../../documentacion/historias/usuario/historias_usuario_v2.5_2026-10-13.md) y añade un anexo candidato para refinar HU-ACC-002/003 e incorporar HU-ACC-005 a HU-ACC-009. El número y las fichas de línea base no acreditan implementación ni validación. El tesista decidió el 2026-10-27 que S1 define documentalmente el acceso y la superadministración; S2 implementa acceso, cuentas y estructura de permisos, mientras las operaciones de cada módulo se desarrollan en S3–S5. Las historias nuevas siguen propuestas y sin prioridad ni estimación.

## Definición documental de login y superadministración asignada a S1

El tesista indicó el 2026-10-27 que S1 termina el 2026-10-27 y que S2 comenzó el
2026-10-14. El cierre anterior del 2026-10-29 quedó reemplazado por una propuesta de
cierre el 2026-11-08. La capacidad comunicada es 16–25 horas semanales; las estimaciones
por historia están pendientes. Esta asignación establece el
alcance documental; no declara completas las tareas ni aprueba por sí sola los requisitos.

La definición completa de S1 debe producir y validar requisitos, historias, especificación,
matriz de permisos y diseño de pantallas para el proceso de acceso; cada validación se registra
por separado y con su alcance. El desarrollo de acceso corresponde a S2 y las funciones
organizacionales y productivas a S3–S5. El tesista declaró
que la presidenta validó expresamente el rol de superadministradora
con autoridad para gestionar todo el sistema. Estado: «validado por la presidenta (según el
tesista)». Evidencia: pendiente de adjuntar; se solicitó la referencia. La autoridad se
concreta mediante las operaciones administrativas definidas para el sistema y los módulos.

### Proceso de login y sesión

- Mantener los mensajes de acceso específicos aprobados de SPEC-001 por decisión del tesista.
- Definir conteo de intentos fallidos, bloqueo temporal, consulta del estado de bloqueo y
  desbloqueo administrativo.
- Definir duración de sesión, expiración por inactividad y cierre de sesiones activas cuando
  se desactive una cuenta o se revoquen sus permisos.
- No hay autorregistro: la Superadministradora crea cuentas después del alta inicial;
  durante la instalación el tesista designa la primera con autorización de la presidenta
  registrada.
- Definir credencial inicial, cambio obligatorio en el primer acceso, expiración y uso único.
- Definir el restablecimiento administrado: canal, verificación de identidad, expiración, uso
  único, revocación y auditoría. El sistema nunca muestra una contraseña existente.
- Una cuenta desactivada no puede iniciar sesión y no conserva sesiones activas.
- Documentar la constancia de autorización presidencial y el arranque seguro de la
  primera Superadministradora, sin exponer credenciales ni introducir puertas traseras.
- Mantener como valores por defecto de SPEC-001, hasta que se valide un cambio, tres fallos en
  tres minutos, bloqueo durante tres minutos y expiración por 30 minutos de inactividad.
- La propuesta de mensajes genéricos queda descartada por decisión del tesista; los
  criterios diferenciados CA-ACC-001-02/03 de SPEC-001 permanecen vigentes.

### Capacidades de superadministración

- Crear usuarios; activar y desactivar cuentas.
- Asignar y retirar módulos por usuario, indicando qué cuenta accede a cada módulo.
- Conceder y revocar roles y permisos, con autoridad para gestionar el sistema conforme a la
  validación reportada y a las operaciones administrativas definidas.
- Consultar intentos fallidos por cuenta y estado de bloqueo, y desbloquear cuentas.
- Permitir configurar desde la interfaz el umbral de intentos fallidos, la duración del
  bloqueo y el tiempo de inactividad. Definir rangos mínimo y máximo, validación y registro
  histórico de cada cambio con actor, fecha, valor anterior, valor nuevo y motivo. No se fijan
  aquí valores numéricos de rangos no comunicados.
- Gestionar fórmulas de pesaje (incluida merma y rendimiento), tipos de plantas y otros
  catálogos o parámetros que cada módulo declare configurables, sin acceso directo a la base
  de datos.
- Tratar fórmulas como expresiones restringidas, validadas, versionadas y con vigencia; ofrecer
  prueba previa y prohibir código arbitrario. Los registros históricos conservan el cálculo y
  la versión que se les aplicó; no se recalculan retroactivamente por una nueva fórmula.
- Consultar y gestionar datos de todos los módulos mediante operaciones administrativas
  ofrecidas por cada módulo, con auditoría. La profundidad de alta, modificación, baja o
  corrección histórica se define módulo por módulo. En S1 se cierra la definición del acceso y
  de la configuración base; la profundidad operativa restante se especifica por módulo.

## Sprint 2

### Historia 1 — Entrar y salir de la parte privada

| Campo | Dato |
|---|---|
| **Número** | 1 |
| **Código de referencia** | `HU-ACC-001` |
| **Usuario** | usuaria interna con cuenta activa |
| **Nombre de la historia** | Entrar y salir de la parte privada |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna con cuenta activa, quiero iniciar y cerrar sesión, para proteger mi información organizacional. |
| **Criterios de aceptación** | 1. Dada una cuenta activa, cuando ingresa con credenciales correctas, entonces accede solo a información autorizada.<br>2. Dada una cuenta inactiva o credenciales incorrectas, cuando intenta entrar, entonces no obtiene acceso ni información privada.<br>3. Dada una sesión activa, cuando la usuaria la cierra, entonces deja de poder acceder a información privada con esa sesión. |
| **Requisito de origen** | `RF-ACC-001` |
| **Dependencias** | HT-GEN-001, HT-GEN-002 |
| **Observaciones** | Posición propuesta en la pila: 6/60. Revisión académica pendiente. |

### Historia 2 — Usar funciones según responsabilidades

| Campo | Dato |
|---|---|
| **Número** | 2 |
| **Código de referencia** | `HU-ACC-003` |
| **Usuario** | usuaria interna |
| **Nombre de la historia** | Usar funciones según responsabilidades |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna, quiero realizar solo operaciones permitidas por mi perfil, cargo o encargo, para respetar las responsabilidades de la organización. |
| **Criterios de aceptación** | 1. Dado un encargo vencido o un cargo sin autorización, cuando la usuaria intenta una operación restringida, entonces esta se rechaza sin cambiar datos. |
| **Requisito de origen** | `RF-ACC-003` |
| **Dependencias** | HU-ACC-001, HT-GEN-002 |
| **Observaciones** | Posición propuesta en la pila: 8/60. Revisión académica pendiente. |

### Historia 3 — Administrar membresías

| Campo | Dato |
|---|---|
| **Número** | 3 |
| **Código de referencia** | `HU-ACC-002` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Administrar membresías |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero activar o desactivar cuentas de socias, para mantener vigentes los accesos sin perder la historia. |
| **Criterios de aceptación** | 1. Dada una cuenta de socia, cuando la Directiva la desactiva, entonces cesan los nuevos accesos y se conservan sus registros.<br>2. Dada una socia sin permiso, cuando intenta cambiar una membresía, entonces el sistema rechaza el cambio. |
| **Requisito de origen** | `RF-ACC-002` |
| **Dependencias** | HU-ACC-001, HT-GEN-002 |
| **Observaciones** | Posición propuesta en la pila: 7/60. Revisión académica pendiente. |

### Historia 4 — Ver mis opciones disponibles

| Campo | Dato |
|---|---|
| **Número** | 4 |
| **Código de referencia** | `HU-ACC-004` |
| **Usuario** | usuaria interna |
| **Nombre de la historia** | Ver mis opciones disponibles |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna, quiero consultar mis actividades, pendientes y encargos disponibles, para saber qué puedo hacer ahora. |
| **Criterios de aceptación** | 1. Dada una sesión válida, cuando la usuaria consulta su inicio privado, entonces encuentra únicamente actividades y acciones que le corresponden. |
| **Requisito de origen** | `RF-ACC-004` |
| **Dependencias** | HU-ACC-001, HU-ACC-003 |
| **Observaciones** | Posición propuesta en la pila: 15/60. Revisión académica pendiente. |

## Sprint 3

### Historia 5 — Programar una actividad

| Campo | Dato |
|---|---|
| **Número** | 5 |
| **Código de referencia** | `HU-PLA-001` |
| **Usuario** | integrante de la Directiva |
| **Nombre de la historia** | Programar una actividad |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S3 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante de la Directiva, quiero registrar jornadas y eventos, para coordinar el trabajo de la organización. |
| **Criterios de aceptación** | 1. Dados fecha, hora, lugar y responsable válidos, cuando la Directiva registra una actividad, entonces esta queda asociada a sus participantes y estado. |
| **Requisito de origen** | `RF-PLA-001` |
| **Dependencias** | HU-ACC-003 |
| **Observaciones** | Posición propuesta en la pila: 9/60. Revisión académica pendiente. |

### Historia 6 — Asignar participantes y responsables

| Campo | Dato |
|---|---|
| **Número** | 6 |
| **Código de referencia** | `HU-PLA-002` |
| **Usuario** | integrante de la Directiva |
| **Nombre de la historia** | Asignar participantes y responsables |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S3 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante de la Directiva, quiero asignar personas a una actividad, para clarificar quién participa y quién responde por ella. |
| **Criterios de aceptación** | 1. Dada una actividad existente, cuando se asigna una cuenta activa dentro del alcance autorizado, entonces la persona queda vinculada a esa actividad.<br>2. Dada una cuenta inactiva, cuando se intenta asignarla, entonces la asignación se rechaza. |
| **Requisito de origen** | `RF-PLA-002` |
| **Dependencias** | HU-PLA-001, HU-ACC-003 |
| **Observaciones** | Posición propuesta en la pila: 10/60. Revisión académica pendiente. |

### Historia 7 — Crear un encargo temporal

| Campo | Dato |
|---|---|
| **Número** | 7 |
| **Código de referencia** | `HU-PLA-003` |
| **Usuario** | integrante de la Directiva |
| **Nombre de la historia** | Crear un encargo temporal |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S3 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante de la Directiva, quiero asignar una responsabilidad de producción o feria por un periodo, para delegar tareas con límites claros. |
| **Criterios de aceptación** | 1. Dados tipo, actividad, periodo y alcance válidos, cuando se asigna un encargo, entonces solo habilita las operaciones correspondientes mientras esté vigente. |
| **Requisito de origen** | `RF-PLA-003` |
| **Dependencias** | HU-PLA-001, HU-PLA-002 |
| **Observaciones** | Posición propuesta en la pila: 11/60. Revisión académica pendiente. |

### Historia 8 — Planificar producción semanal

| Campo | Dato |
|---|---|
| **Número** | 8 |
| **Código de referencia** | `HU-PLA-005` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Planificar producción semanal |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S3 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero definir productos, objetivos, insumos y responsables de la semana, para coordinar la producción prevista. |
| **Criterios de aceptación** | 1. Dados producto, cantidad objetivo y responsables válidos, cuando se registra el plan semanal, entonces queda disponible para las asignadas sin crear existencias anticipadas. |
| **Requisito de origen** | `RF-PLA-005` |
| **Dependencias** | HU-PLA-001, HU-CAT-001 |
| **Observaciones** | Posición propuesta en la pila: 14/60. Revisión académica pendiente. |

### Historia 9 — Consultar mis actividades

| Campo | Dato |
|---|---|
| **Número** | 9 |
| **Código de referencia** | `HU-PLA-004` |
| **Usuario** | socia |
| **Nombre de la historia** | Consultar mis actividades |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S3 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia, quiero consultar actividades y pendientes que me corresponden, para organizar mi participación. |
| **Criterios de aceptación** | 1. Dadas actividades asignadas, cuando la socia consulta sus pendientes, entonces ve sus propios registros y no información privada ajena. |
| **Requisito de origen** | `RF-PLA-004` |
| **Dependencias** | HU-PLA-001, HU-PLA-002 |
| **Observaciones** | Posición propuesta en la pila: 12/60. Revisión académica pendiente. |

## Sprint 4

### Historia 10 — Registrar entrada y salida

| Campo | Dato |
|---|---|
| **Número** | 10 |
| **Código de referencia** | `HU-ASI-001` |
| **Usuario** | socia |
| **Nombre de la historia** | Registrar entrada y salida |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia, quiero registrar por separado mi entrada y salida, para contar con asistencia verificable. |
| **Criterios de aceptación** | 1. Dada una actividad habilitada, cuando se registra una entrada o salida en línea, entonces queda el tipo de evento, la hora del servidor y su origen.<br>2. Dada una captura sin red habilitada, cuando se conserva localmente, entonces queda provisional y diferencia hora declarada de recepción. |
| **Requisito de origen** | `RF-ASI-001` |
| **Dependencias** | HU-PLA-001, HU-ACC-003; HU-PWA-002 solo para captura sin red |
| **Observaciones** | Posición propuesta en la pila: 22/60. Revisión académica pendiente. |

### Historia 11 — Evitar asistencia duplicada

| Campo | Dato |
|---|---|
| **Número** | 11 |
| **Código de referencia** | `HU-ASI-002` |
| **Usuario** | socia |
| **Nombre de la historia** | Evitar asistencia duplicada |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia, quiero conservar un solo evento de cada tipo por actividad, para evitar registros contradictorios. |
| **Criterios de aceptación** | 1. Dado un evento de asistencia ya registrado, cuando se intenta repetirlo para la misma socia y actividad, entonces no se crea otro y se informa el registro existente. |
| **Requisito de origen** | `RF-ASI-002` |
| **Dependencias** | HU-ASI-001 |
| **Observaciones** | Posición propuesta en la pila: 23/60. Revisión académica pendiente. |

### Historia 12 — Corregir asistencia con historial

| Campo | Dato |
|---|---|
| **Número** | 12 |
| **Código de referencia** | `HU-ASI-003` |
| **Usuario** | integrante de la Directiva o encargada autorizada |
| **Nombre de la historia** | Corregir asistencia con historial |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante de la Directiva o encargada autorizada, quiero corregir un registro sensible con motivo, para resolver errores sin borrar la historia. |
| **Criterios de aceptación** | 1. Dado un registro de asistencia y autorización vigente, cuando se corrige con motivo, entonces se conservan actor, fecha, valor anterior y nuevo valor.<br>2. Dada una persona sin permiso, cuando intenta corregir, entonces no cambia el registro. |
| **Requisito de origen** | `RF-ASI-003` |
| **Dependencias** | HU-ASI-001, HT-GEN-003 |
| **Observaciones** | Posición propuesta en la pila: 24/60. Revisión académica pendiente. |

### Historia 13 — Resolver una inconsistencia de asistencia

| Campo | Dato |
|---|---|
| **Número** | 13 |
| **Código de referencia** | `HU-ASI-006` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Resolver una inconsistencia de asistencia |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero registrar el acuerdo de la asamblea sobre una inconsistencia, para conservar una decisión justa y rastreable. |
| **Criterios de aceptación** | 1. Dada una inconsistencia pendiente, cuando se registra una decisión de la asamblea, entonces quedan acuerdo, actor, fecha y motivo sin sanción automática. |
| **Requisito de origen** | `RF-ASI-006` |
| **Dependencias** | HU-ASI-001, HU-ASI-003 |
| **Observaciones** | Posición propuesta en la pila: 27/60. Revisión académica pendiente. |

### Historia 14 — Registrar asistencia con QR o alternativa

| Campo | Dato |
|---|---|
| **Número** | 14 |
| **Código de referencia** | `HU-ASI-007` |
| **Usuario** | socia |
| **Nombre de la historia** | Registrar asistencia con QR o alternativa |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia, quiero usar un QR temporal o código alternativo para mi asistencia, para registrarla por un medio disponible y auditable. |
| **Criterios de aceptación** | 1. Dado un QR válido para la fase habilitada, cuando la socia registra su evento, entonces queda identificado como autorregistro.<br>2. Dado un token vencido, repetido o para otra acción, cuando se intenta registrar asistencia, entonces no se modifica el evento.<br>3. Dado un registro delegado autorizado, cuando se confirma, entonces quedan identificadas la socia, la persona delegada y el motivo. |
| **Requisito de origen** | `RF-ASI-007` |
| **Dependencias** | HU-ASI-001, HU-ACC-003 |
| **Observaciones** | Posición propuesta en la pila: 28/60. Revisión académica pendiente. |

### Historia 15 — Consultar historial de asistencia

| Campo | Dato |
|---|---|
| **Número** | 15 |
| **Código de referencia** | `HU-ASI-004` |
| **Usuario** | socia |
| **Nombre de la historia** | Consultar historial de asistencia |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia, quiero consultar mi asistencia por periodo, para conocer mis registros y sus estados. |
| **Criterios de aceptación** | 1. Dado un periodo consultado, cuando la socia solicita su historial, entonces ve sus eventos y estados sin acceso a los de otra socia. |
| **Requisito de origen** | `RF-ASI-004` |
| **Dependencias** | HU-ASI-001, HT-GEN-002 |
| **Observaciones** | Posición propuesta en la pila: 25/60. Revisión académica pendiente. |

### Historia 16 — Registrar participación adicional

| Campo | Dato |
|---|---|
| **Número** | 16 |
| **Código de referencia** | `HU-ASI-005` |
| **Usuario** | responsable autorizada de una actividad |
| **Nombre de la historia** | Registrar participación adicional |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como responsable autorizada de una actividad, quiero registrar una participación distinta de la asistencia cuando se necesite, para reflejar el aporte real de las socias. |
| **Criterios de aceptación** | 1. Dada una actividad que exige participación adicional, cuando se registra ese dato, entonces queda vinculado a la socia y actividad.<br>2. Dada una actividad simple, cuando se confirma la asistencia, entonces no se exige participación adicional. |
| **Requisito de origen** | `RF-ASI-005` |
| **Dependencias** | HU-PLA-001, HU-ASI-001 |
| **Observaciones** | Posición propuesta en la pila: 26/60. Revisión académica pendiente. |

## Sprint 5

### Historia 17 — Mantener catálogo productivo

| Campo | Dato |
|---|---|
| **Número** | 17 |
| **Código de referencia** | `HU-CAT-001` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Mantener catálogo productivo |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero distinguir materias primas, insumos, productos y unidades, para usar datos coherentes en producción y venta. |
| **Criterios de aceptación** | 1. Dado un elemento de catálogo activo, cuando se usa en una operación permitida, entonces conserva su tipo y unidad.<br>2. Dado un elemento desactivado, cuando se intenta usarlo en una operación nueva, entonces se rechaza sin borrar su historia. |
| **Requisito de origen** | `RF-CAT-001` |
| **Dependencias** | HU-ACC-003 |
| **Observaciones** | Posición propuesta en la pila: 13/60. Revisión académica pendiente. |

### Historia 18 — Conservar valores comerciales históricos

| Campo | Dato |
|---|---|
| **Número** | 18 |
| **Código de referencia** | `HU-INV-001` |
| **Usuario** | Tesorera autorizada |
| **Nombre de la historia** | Conservar valores comerciales históricos |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Tesorera autorizada, quiero mantener precios y valor base con vigencia, para explicar cada venta según los valores de su momento. |
| **Criterios de aceptación** | 1. Dado un cambio de valor comercial, cuando se aplica a operaciones nuevas, entonces una venta anterior conserva el valor histórico utilizado. |
| **Requisito de origen** | `RF-INV-001` |
| **Dependencias** | HU-CAT-001, HU-ACC-003 |
| **Observaciones** | Posición propuesta en la pila: 29/60. Revisión académica pendiente. |

### Historia 19 — Registrar acopio de materia

| Campo | Dato |
|---|---|
| **Número** | 19 |
| **Código de referencia** | `HU-TRA-001` |
| **Usuario** | socia encargada de producción |
| **Nombre de la historia** | Registrar acopio de materia |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de producción, quiero registrar materia recibida, cantidad y origen, para conocer quién entregó cada insumo. |
| **Criterios de aceptación** | 1. Dados origen, unidad, responsable y peso positivo, cuando se registra acopio, entonces queda trazable la entrega.<br>2. Dado un peso no positivo, cuando se intenta registrar, entonces la operación se rechaza. |
| **Requisito de origen** | `RF-TRA-001` |
| **Dependencias** | HU-CAT-001, HU-PLA-003 |
| **Observaciones** | Posición propuesta en la pila: 30/60. Revisión académica pendiente. |

### Historia 20 — Registrar secado

| Campo | Dato |
|---|---|
| **Número** | 20 |
| **Código de referencia** | `HU-TRA-002` |
| **Usuario** | socia encargada de producción |
| **Nombre de la historia** | Registrar secado |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de producción, quiero registrar pesos, temperatura e inicio y fin del secado, para seguir cada proceso productivo. |
| **Criterios de aceptación** | 1. Dados peso inicial y temperatura válidos, cuando se inicia el secado, entonces se conservan sus datos y el momento correspondiente.<br>2. Dados peso final y cierre válidos, cuando termina el secado, entonces queda el cierre sin exigir humedad opcional. |
| **Requisito de origen** | `RF-TRA-002` |
| **Dependencias** | HU-TRA-001, HU-PLA-003 |
| **Observaciones** | Posición propuesta en la pila: 31/60. Revisión académica pendiente. |

### Historia 21 — Seguir la procedencia de lotes

| Campo | Dato |
|---|---|
| **Número** | 21 |
| **Código de referencia** | `HU-TRA-004` |
| **Usuario** | responsable de producción |
| **Nombre de la historia** | Seguir la procedencia de lotes |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como responsable de producción, quiero relacionar un lote con sus orígenes y derivados, para reconstruir la procedencia de un producto. |
| **Criterios de aceptación** | 1. Dada una mezcla física permitida, cuando se crea un lote derivado, entonces sus lotes de origen permanecen identificables.<br>2. Dado un lote cerrado, cuando aún tiene existencias, entonces no se confunde cierre productivo con stock agotado. |
| **Requisito de origen** | `RF-TRA-004` |
| **Dependencias** | HU-TRA-001, HU-TRA-002 |
| **Observaciones** | Posición propuesta en la pila: 33/60. Revisión académica pendiente. |

### Historia 22 — Registrar transformación

| Campo | Dato |
|---|---|
| **Número** | 22 |
| **Código de referencia** | `HU-TRA-005` |
| **Usuario** | socia encargada de producción |
| **Nombre de la historia** | Registrar transformación |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de producción, quiero registrar insumos consumidos y producto resultante, para conservar la composición y cantidad de cada lote. |
| **Criterios de aceptación** | 1. Dados insumos y composición válidos, cuando se confirma la transformación, entonces el producto resultante queda vinculado a consumos, versión y lote. |
| **Requisito de origen** | `RF-TRA-005` |
| **Dependencias** | HU-TRA-004, HU-CAT-001 |
| **Observaciones** | Posición propuesta en la pila: 34/60. Revisión académica pendiente. |

### Historia 23 — Reconstruir existencias

| Campo | Dato |
|---|---|
| **Número** | 23 |
| **Código de referencia** | `HU-INV-002` |
| **Usuario** | responsable de inventario |
| **Nombre de la historia** | Reconstruir existencias |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como responsable de inventario, quiero consultar existencias derivadas de movimientos, para evitar saldos sin respaldo. |
| **Criterios de aceptación** | 1. Dadas entradas, consumos, ventas y devoluciones confirmadas, cuando se calcula la existencia, entonces coincide con sus movimientos.<br>2. Dado un ajuste autorizado, cuando se confirma con motivo, entonces el cambio queda registrado íntegramente. |
| **Requisito de origen** | `RF-INV-002` |
| **Dependencias** | HU-CAT-001, HT-GEN-003 |
| **Observaciones** | Posición propuesta en la pila: 35/60. Revisión académica pendiente. |

### Historia 24 — Registrar una venta

| Campo | Dato |
|---|---|
| **Número** | 24 |
| **Código de referencia** | `HU-VEN-001` |
| **Usuario** | socia encargada de feria |
| **Nombre de la historia** | Registrar una venta |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de feria, quiero registrar varios productos y su forma de pago, para conocer el total sin vender más de lo disponible. |
| **Criterios de aceptación** | 1. Dado stock autorizado suficiente, cuando se confirma una venta de varios productos, entonces se registra completa con total calculado.<br>2. Dado stock insuficiente, cuando se intenta confirmar, entonces no se registra ninguna parte de la venta. |
| **Requisito de origen** | `RF-VEN-001` |
| **Dependencias** | HU-INV-002, HU-INV-003, HT-GEN-003 |
| **Observaciones** | Posición propuesta en la pila: 38/60. Revisión académica pendiente. |

### Historia 25 — Conocer valor base y excedente

| Campo | Dato |
|---|---|
| **Número** | 25 |
| **Código de referencia** | `HU-VEN-003` |
| **Usuario** | socia encargada de venta |
| **Nombre de la historia** | Conocer valor base y excedente |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de venta, quiero conocer valor base, precio aplicado y excedente bruto de la venta, para rendir cuentas sin confundir excedente con utilidad neta. |
| **Criterios de aceptación** | 1. Dada una venta confirmada, cuando se consulta su resultado, entonces conserva valor base y precio aplicado históricos y calcula excedente bruto. |
| **Requisito de origen** | `RF-VEN-003` |
| **Dependencias** | HU-VEN-001, HU-INV-001 |
| **Observaciones** | Posición propuesta en la pila: 40/60. Revisión académica pendiente. |

### Historia 26 — Autorizar venta bajo valor base

| Campo | Dato |
|---|---|
| **Número** | 26 |
| **Código de referencia** | `HU-VEN-004` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Autorizar venta bajo valor base |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero decidir una excepción de precio bajo el valor base, para proteger y explicar el resultado comercial. |
| **Criterios de aceptación** | 1. Dada una venta bajo valor base sin autorización, cuando se intenta confirmar, entonces se rechaza.<br>2. Dada una excepción autorizada con motivo, cuando se confirma, entonces quedan responsable, diferencia y razón registrados. |
| **Requisito de origen** | `RF-VEN-004` |
| **Dependencias** | HU-VEN-001, HU-VEN-003 |
| **Observaciones** | Posición propuesta en la pila: 41/60. Revisión académica pendiente. |

### Historia 27 — Distinguir deudas y custodia

| Campo | Dato |
|---|---|
| **Número** | 27 |
| **Código de referencia** | `HU-CXC-001` |
| **Usuario** | Tesorera |
| **Nombre de la historia** | Distinguir deudas y custodia |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Tesorera, quiero distinguir deuda de socia, cuenta por cobrar externa y custodia física, para evitar cargos monetarios incorrectos. |
| **Criterios de aceptación** | 1. Dado un retiro individual impago, cuando se registra, entonces genera deuda con valor base histórico.<br>2. Dada custodia de stock compartido, cuando se registra la entrega, entonces no crea deuda individual. |
| **Requisito de origen** | `RF-CXC-001` |
| **Dependencias** | HU-INV-003, HU-VEN-001, HU-INV-001 |
| **Observaciones** | Posición propuesta en la pila: 47/60. Revisión académica pendiente. |

### Historia 28 — Registrar un abono

| Campo | Dato |
|---|---|
| **Número** | 28 |
| **Código de referencia** | `HU-CXC-002` |
| **Usuario** | Tesorera |
| **Nombre de la historia** | Registrar un abono |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Tesorera, quiero registrar pagos parciales sobre un saldo identificado, para conocer cuánto queda pendiente. |
| **Criterios de aceptación** | 1. Dado un saldo y un abono válido, cuando se aplica el pago, entonces quedan monto, fecha, forma y responsable y se reduce solo ese saldo. |
| **Requisito de origen** | `RF-CXC-002` |
| **Dependencias** | HU-CXC-001 |
| **Observaciones** | Posición propuesta en la pila: 48/60. Revisión académica pendiente. |

### Historia 29 — Conocer duración y merma

| Campo | Dato |
|---|---|
| **Número** | 29 |
| **Código de referencia** | `HU-TRA-003` |
| **Usuario** | responsable de producción |
| **Nombre de la historia** | Conocer duración y merma |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como responsable de producción, quiero conocer la duración y pérdida de peso de un secado, para evaluar el resultado del proceso. |
| **Criterios de aceptación** | 1. Dado un secado con inicio, fin y pesos válidos, cuando se consulta su resultado, entonces se muestran duración y merma absoluta con unidad y fórmula.<br>2. Dado un peso final mayor que el inicial, cuando se calcula el resultado, entonces queda pendiente de revisión o excepción autorizada. |
| **Requisito de origen** | `RF-TRA-003` |
| **Dependencias** | HU-TRA-002 |
| **Observaciones** | Posición propuesta en la pila: 32/60. Revisión académica pendiente. |

### Historia 30 — Entregar productos para feria

| Campo | Dato |
|---|---|
| **Número** | 30 |
| **Código de referencia** | `HU-INV-003` |
| **Usuario** | socia encargada de feria |
| **Nombre de la historia** | Entregar productos para feria |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de feria, quiero recibir productos identificados por lote y modalidad, para rendir cuentas de lo que quedó bajo mi custodia. |
| **Criterios de aceptación** | 1. Dado stock suficiente y un encargo vigente, cuando se confirma una entrega, entonces quedan producto, lote, cantidad, socia y origen individual o compartido.<br>2. Dada cantidad superior al stock, cuando se intenta entregar, entonces se rechaza. |
| **Requisito de origen** | `RF-INV-003` |
| **Dependencias** | HU-INV-002, HU-PLA-003 |
| **Observaciones** | Posición propuesta en la pila: 36/60. Revisión académica pendiente. |

### Historia 31 — Conciliar productos de feria

| Campo | Dato |
|---|---|
| **Número** | 31 |
| **Código de referencia** | `HU-INV-004` |
| **Usuario** | socia encargada de feria |
| **Nombre de la historia** | Conciliar productos de feria |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de feria, quiero comparar productos recibidos, vendidos y devueltos, para explicar diferencias físicas. |
| **Criterios de aceptación** | 1. Dado un encargo con movimientos, cuando se realiza la conciliación, entonces se distinguen recibidos, transferidos, vendidos, devueltos y sobrantes.<br>2. Dada una diferencia, cuando se cierra el recuento, entonces permanece visible sin generar stock negativo silencioso. |
| **Requisito de origen** | `RF-INV-004` |
| **Dependencias** | HU-INV-003, HU-INV-002 |
| **Observaciones** | Posición propuesta en la pila: 37/60. Revisión académica pendiente. |

### Historia 32 — Identificar comprador según la venta

| Campo | Dato |
|---|---|
| **Número** | 32 |
| **Código de referencia** | `HU-VEN-002` |
| **Usuario** | socia encargada de venta |
| **Nombre de la historia** | Identificar comprador según la venta |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de venta, quiero registrar los datos de comprador necesarios, para conservar un cobro rastreable sin pedir datos de más. |
| **Criterios de aceptación** | 1. Dada una venta a crédito o institucional, cuando se intenta confirmar sin comprador identificado, entonces se rechaza.<br>2. Dada una venta al contado ordinaria, cuando se registra, entonces puede usar Público general sin pedir datos personales innecesarios. |
| **Requisito de origen** | `RF-VEN-002` |
| **Dependencias** | HU-VEN-001 |
| **Observaciones** | Posición propuesta en la pila: 39/60. Revisión académica pendiente. |

### Historia 33 — Distinguir stock individual y compartido

| Campo | Dato |
|---|---|
| **Número** | 33 |
| **Código de referencia** | `HU-VEN-006` |
| **Usuario** | socia encargada de feria |
| **Nombre de la historia** | Distinguir stock individual y compartido |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de feria, quiero identificar el origen de cada línea vendida, para separar resultados individuales y compartidos. |
| **Criterios de aceptación** | 1. Dada una venta de feria, cuando se confirma una línea, entonces conserva si el producto procede de stock individual o compartido.<br>2. Dado excedente de stock compartido, cuando se presenta el resultado, entonces no se reparte automáticamente. |
| **Requisito de origen** | `RF-VEN-006` |
| **Dependencias** | HU-INV-003, HU-VEN-001 |
| **Observaciones** | Posición propuesta en la pila: 43/60. Revisión académica pendiente. |

### Historia 34 — Registrar venta institucional

| Campo | Dato |
|---|---|
| **Número** | 34 |
| **Código de referencia** | `HU-VEN-007` |
| **Usuario** | Tesorera |
| **Nombre de la historia** | Registrar venta institucional |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Tesorera, quiero registrar una venta desde stock general, para rendir cuentas sin atribuir excedente a una socia. |
| **Criterios de aceptación** | 1. Dado stock general y una compradora institucional identificada, cuando se confirma la venta, entonces quedan su tipo y responsable sin asignar excedente individual. |
| **Requisito de origen** | `RF-VEN-007` |
| **Dependencias** | HU-VEN-001, HU-VEN-002 |
| **Observaciones** | Posición propuesta en la pila: 44/60. Revisión académica pendiente. |

### Historia 35 — Conciliar comprobante manual de feria

| Campo | Dato |
|---|---|
| **Número** | 35 |
| **Código de referencia** | `HU-VEN-008` |
| **Usuario** | socia encargada de feria |
| **Nombre de la historia** | Conciliar comprobante manual de feria |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de feria, quiero incorporar una venta respaldada por comprobante de contingencia, para evitar pérdidas y duplicados durante fallos. |
| **Criterios de aceptación** | 1. Dado un comprobante manual con folio único, cuando se incorpora después de la contingencia, entonces se conserva su origen y momento declarado.<br>2. Dado un folio ya registrado, cuando se intenta incorporarlo de nuevo, entonces no descuenta stock dos veces. |
| **Requisito de origen** | `RF-VEN-008` |
| **Dependencias** | HU-VEN-001, HU-INV-004 |
| **Observaciones** | Posición propuesta en la pila: 45/60. Revisión académica pendiente. |

### Historia 36 — Registrar gasto operativo

| Campo | Dato |
|---|---|
| **Número** | 36 |
| **Código de referencia** | `HU-GAS-001` |
| **Usuario** | Tesorera |
| **Nombre de la historia** | Registrar gasto operativo |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Tesorera, quiero registrar un gasto con categoría, monto y periodo, para conocer los egresos vinculados al trabajo. |
| **Criterios de aceptación** | 1. Dado monto positivo y datos válidos, cuando se confirma un gasto, entonces quedan concepto, periodo o lote, responsable y fecha.<br>2. Dado monto inválido, cuando se intenta registrar, entonces se rechaza. |
| **Requisito de origen** | `RF-GAS-001` |
| **Dependencias** | HU-ACC-003 |
| **Observaciones** | Posición propuesta en la pila: 46/60. Revisión académica pendiente. |

### Historia 37 — Rendir cuentas de la feria

| Campo | Dato |
|---|---|
| **Número** | 37 |
| **Código de referencia** | `HU-CXC-003` |
| **Usuario** | socia encargada de feria |
| **Nombre de la historia** | Rendir cuentas de la feria |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia encargada de feria, quiero comparar productos, dinero y diferencias, para cerrar mi encargo con cifras explicables. |
| **Criterios de aceptación** | 1. Dado un encargo de feria con ventas y devoluciones, cuando se presenta la rendición, entonces se distinguen recibido, vendido, devuelto, sobrante, dinero, base y excedente.<br>2. Dada una discrepancia, cuando se revisa, entonces el encargo permanece por conciliar y explica lo faltante. |
| **Requisito de origen** | `RF-CXC-003` |
| **Dependencias** | HU-INV-004, HU-VEN-001, HU-CXC-001 |
| **Observaciones** | Posición propuesta en la pila: 49/60. Revisión académica pendiente. |

### Historia 38 — Configurar descuento por volumen

| Campo | Dato |
|---|---|
| **Número** | 38 |
| **Código de referencia** | `HU-VEN-005` |
| **Usuario** | Tesorera |
| **Nombre de la historia** | Configurar descuento por volumen |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Tesorera, quiero definir descuentos con umbral, valor y vigencia, para aplicar reglas comerciales aprobadas de forma consistente. |
| **Criterios de aceptación** | 1. Dada una política con datos incompletos, cuando una venta cumple la cantidad indicada, entonces no se aplica descuento.<br>2. Dada una política completa y vigente, cuando se cumplen sus condiciones, entonces se aplica el valor configurado respetando excepciones bajo base. |
| **Requisito de origen** | `RF-VEN-005` |
| **Dependencias** | HU-CAT-001, HU-INV-001, HU-VEN-001 |
| **Observaciones** | Posición propuesta en la pila: 42/60. Revisión académica pendiente. |

### Historia 39 — Consultar resumen económico

| Campo | Dato |
|---|---|
| **Número** | 39 |
| **Código de referencia** | `HU-GAS-002` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Consultar resumen económico |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero consultar ingresos, gastos y pendientes, para comprender los resultados del periodo. |
| **Criterios de aceptación** | 1. Dado un periodo con operaciones, cuando se consulta el resumen, entonces cada total indica su fuente y fórmula sin presentarse como balance certificado. |
| **Requisito de origen** | `RF-GAS-002` |
| **Dependencias** | HU-GAS-001, HU-VEN-001, HU-CXC-001 |
| **Observaciones** | Posición propuesta en la pila: 50/60. Revisión académica pendiente. |

## Sprint 6

### Historia 40 — Consultar reporte de asistencia

| Campo | Dato |
|---|---|
| **Número** | 40 |
| **Código de referencia** | `HU-REP-001` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Consultar reporte de asistencia |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero consultar asistencia por periodo, actividad y socia, para conocer participación e inconsistencias. |
| **Criterios de aceptación** | 1. Dado un periodo consultado, cuando se obtiene el reporte de asistencia, entonces sus totales coinciden con registros y correcciones autorizadas. |
| **Requisito de origen** | `RF-REP-001` |
| **Dependencias** | HU-ASI-001, HU-ASI-003 |
| **Observaciones** | Posición propuesta en la pila: 52/60. Revisión académica pendiente. |

### Historia 41 — Consultar reporte de actividades

| Campo | Dato |
|---|---|
| **Número** | 41 |
| **Código de referencia** | `HU-REP-002` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Consultar reporte de actividades |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero consultar actividades y encargos por estado y responsable, para dar seguimiento al trabajo planificado. |
| **Criterios de aceptación** | 1. Dado un periodo y filtro válidos, cuando se obtiene el reporte, entonces aparecen las actividades y encargos permitidos con sus estados. |
| **Requisito de origen** | `RF-REP-002` |
| **Dependencias** | HU-PLA-001, HU-PLA-003 |
| **Observaciones** | Posición propuesta en la pila: 53/60. Revisión académica pendiente. |

### Historia 42 — Consultar reporte productivo

| Campo | Dato |
|---|---|
| **Número** | 42 |
| **Código de referencia** | `HU-REP-003` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Consultar reporte productivo |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero consultar acopio, secado, lotes y merma, para seguir la producción y sus orígenes. |
| **Criterios de aceptación** | 1. Dados movimientos productivos de un periodo, cuando se obtiene el reporte, entonces conserva unidades, orígenes y totales vinculados a sus registros. |
| **Requisito de origen** | `RF-REP-003` |
| **Dependencias** | HU-TRA-001, HU-TRA-002, HU-TRA-004, HU-TRA-005 |
| **Observaciones** | Posición propuesta en la pila: 54/60. Revisión académica pendiente. |

### Historia 43 — Consultar reporte de inventario

| Campo | Dato |
|---|---|
| **Número** | 43 |
| **Código de referencia** | `HU-REP-004` |
| **Usuario** | integrante autorizada de la Directiva |
| **Nombre de la historia** | Consultar reporte de inventario |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la Directiva, quiero consultar existencias y movimientos por producto y lote, para explicar la cantidad disponible. |
| **Criterios de aceptación** | 1. Dado un producto y periodo, cuando se obtiene el reporte, entonces la existencia concilia con movimientos y distingue ajustes. |
| **Requisito de origen** | `RF-REP-004` |
| **Dependencias** | HU-INV-002, HU-INV-004 |
| **Observaciones** | Posición propuesta en la pila: 55/60. Revisión académica pendiente. |

### Historia 44 — Consultar reporte de ventas y saldos

| Campo | Dato |
|---|---|
| **Número** | 44 |
| **Código de referencia** | `HU-REP-005` |
| **Usuario** | Tesorera |
| **Nombre de la historia** | Consultar reporte de ventas y saldos |
| **Prioridad en negocio** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Tesorera, quiero consultar ventas, pagos y deudas separadas, para identificar pendientes sin mezclar saldos. |
| **Criterios de aceptación** | 1. Dado un periodo consultado, cuando se obtiene el reporte comercial, entonces deuda de socias, deuda externa, pagos y ventas aparecen por separado con fórmulas visibles. |
| **Requisito de origen** | `RF-REP-005` |
| **Dependencias** | HU-VEN-001, HU-CXC-001, HU-CXC-002 |
| **Observaciones** | Posición propuesta en la pila: 56/60. Revisión académica pendiente. |

### Historia 45 — Consultar mi resumen privado

| Campo | Dato |
|---|---|
| **Número** | 45 |
| **Código de referencia** | `HU-REP-006` |
| **Usuario** | socia |
| **Nombre de la historia** | Consultar mi resumen privado |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia, quiero consultar mi actividad, productos y valores pendientes, para comprender mi situación organizacional. |
| **Criterios de aceptación** | 1. Dada una sesión de socia, cuando consulta su resumen, entonces ve solo sus datos y el excedente bruto no aparece como ganancia neta. |
| **Requisito de origen** | `RF-REP-006` |
| **Dependencias** | HU-ASI-004, HU-PLA-004, HU-CXC-001 |
| **Observaciones** | Posición propuesta en la pila: 57/60. Revisión académica pendiente. |

### Historia 46 — Recibir recordatorios internos

| Campo | Dato |
|---|---|
| **Número** | 46 |
| **Código de referencia** | `HU-NOT-001` |
| **Usuario** | usuaria interna |
| **Nombre de la historia** | Recibir recordatorios internos |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna, quiero recibir avisos sobre actividades y registros pendientes, para atender tareas a tiempo. |
| **Criterios de aceptación** | 1. Dada una actividad o rendición pendiente que me corresponde, cuando se genera un recordatorio interno, entonces identifica el elemento permitido sin requerir correo o mensajería. |
| **Requisito de origen** | `RF-NOT-001` |
| **Dependencias** | HU-PLA-004, HU-ACC-003 |
| **Observaciones** | Posición propuesta en la pila: 58/60. Revisión académica pendiente. |

### Historia 47 — Gestionar contenido público

| Campo | Dato |
|---|---|
| **Número** | 47 |
| **Código de referencia** | `HU-PUB-002` |
| **Usuario** | integrante autorizada de la organización |
| **Nombre de la historia** | Gestionar contenido público |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como integrante autorizada de la organización, quiero preparar, aprobar, publicar o retirar contenido, para mantener vigente la información visible. |
| **Criterios de aceptación** | 1. Dado contenido preparado, cuando una persona autorizada lo aprueba y publica, entonces se vuelve visible con su estado registrado.<br>2. Dada una persona sin permiso, cuando intenta publicar, entonces el contenido no cambia de estado. |
| **Requisito de origen** | `RF-PUB-002` |
| **Dependencias** | HU-ACC-003, HT-GEN-002 |
| **Observaciones** | Posición propuesta en la pila: 59/60. Revisión académica pendiente. |

### Historia 48 — Conocer información pública aprobada

| Campo | Dato |
|---|---|
| **Número** | 48 |
| **Código de referencia** | `HU-PUB-001` |
| **Usuario** | visitante |
| **Nombre de la historia** | Conocer información pública aprobada |
| **Prioridad en negocio** | Complementaria (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como visitante, quiero consultar información pública de Zhud Alelí, para conocer sus actividades y productos. |
| **Criterios de aceptación** | 1. Dado contenido aprobado, cuando una visitante consulta el sitio público, entonces ve solo información autorizada.<br>2. Dado contenido sin aprobación, cuando se consulta el sitio, entonces esa información permanece oculta. |
| **Requisito de origen** | `RF-PUB-001` |
| **Dependencias** | HU-PUB-002, HT-GEN-002 |
| **Observaciones** | Posición propuesta en la pila: 60/60. Revisión académica pendiente. |

## Trabajo transversal

### Historia 49 — Abrir tareas habilitadas sin conexión

| Campo | Dato |
|---|---|
| **Número** | 49 |
| **Código de referencia** | `HU-PWA-001` |
| **Usuario** | socia con dispositivo preparado |
| **Nombre de la historia** | Abrir tareas habilitadas sin conexión |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4–S5 (transversal) |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia con dispositivo preparado, quiero acceder a los flujos esenciales habilitados durante un corte, para continuar una tarea posible sin Internet. |
| **Criterios de aceptación** | 1. Dado un dispositivo previamente preparado, cuando se pierde la red, entonces se mantienen disponibles los recursos y acciones habilitados.<br>2. Dado un dispositivo sin preparación inicial, cuando no hay red, entonces se informa la limitación sin mostrar datos privados guardados indebidamente. |
| **Requisito de origen** | `RF-PWA-001` |
| **Dependencias** | HT-GEN-005 |
| **Observaciones** | Posición propuesta en la pila: 19/60. Revisión académica pendiente. |

### Historia 50 — Conservar registros pendientes sin conexión

| Campo | Dato |
|---|---|
| **Número** | 50 |
| **Código de referencia** | `HU-PWA-002` |
| **Usuario** | socia autorizada |
| **Nombre de la historia** | Conservar registros pendientes sin conexión |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4–S5 (transversal) |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia autorizada, quiero guardar localmente asistencia y pesajes habilitados, para no perder datos mientras vuelve Internet. |
| **Criterios de aceptación** | 1. Dada una operación sin conexión habilitada, cuando se guarda localmente, entonces persiste como pendiente al recargar y conserva su origen.<br>2. Dada otra cuenta en el mismo dispositivo, cuando intenta acceder a la cola ajena, entonces no ve sus datos. |
| **Requisito de origen** | `RF-PWA-002` |
| **Dependencias** | HU-PWA-001, HT-GEN-005 |
| **Observaciones** | Posición propuesta en la pila: 20/60. Revisión académica pendiente. |

### Historia 51 — Sincronizar registros pendientes

| Campo | Dato |
|---|---|
| **Número** | 51 |
| **Código de referencia** | `HU-PWA-003` |
| **Usuario** | socia autorizada |
| **Nombre de la historia** | Sincronizar registros pendientes |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4–S5 (transversal) |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como socia autorizada, quiero enviar mis operaciones pendientes al volver la red, para conocer cuáles fueron aceptadas sin duplicados. |
| **Criterios de aceptación** | 1. Dada una operación pendiente, cuando vuelve la red, entonces el servidor revalida sesión, permiso y reglas antes de aceptarla.<br>2. Dada una respuesta perdida, cuando se reintenta la misma operación, entonces se obtiene un solo registro y el conflicto se informa sin cambios parciales. |
| **Requisito de origen** | `RF-PWA-003` |
| **Dependencias** | HU-PWA-002, HT-GEN-006 |
| **Observaciones** | Posición propuesta en la pila: 21/60. Revisión académica pendiente. |

## Anexo propuesto — Administración organizacional por módulos

**Estado común:** las historias y sus criterios siguen propuestos. El tesista declaró el
2026-10-27 que la presidenta validó expresamente el rol de superadministradora con autoridad
para gestionar todo el sistema. Estado: «validado por la presidenta (según el tesista)»;
evidencia: pendiente de adjuntar. Esta declaración no aprueba automáticamente todas las
historias ni sus criterios. El rol organizacional no equivale a `is_staff` o `is_superuser` de
Django; el tesista decidió que pueda ejecutar todas las acciones ordinarias de cada
módulo y editar registros, valores de campos existentes y opciones publicadas desde
su panel, sin asignación individual a cada módulo. Sus operaciones conservan las
validaciones y la auditoría del módulo propietario.

### Refinamiento candidato de HU-ACC-002 — Administrar membresías y acceso por módulo

| Campo | Dato |
|---|---|
| **Código de referencia** | `HU-ACC-002` (refinamiento propuesto de la ficha de v2.5) |
| **Usuario** | persona con autoridad organizacional vigente, pendiente de definir |
| **Descripción** | Como persona autorizada, quiero activar o desactivar una cuenta y asignar o retirar el acceso a módulos concretos, para mantener accesos organizacionales vigentes y limitados. |
| **Prioridad / sprint / responsable** | La definición completa se asigna a S1 y la implementación a S2 por decisión del tesista del 2026-10-27. Prioridad, estimación y responsable siguen pendientes. |
| **Criterios candidatos** | 1. Dada una autoridad y un módulo vigentes, cuando la persona autorizada asigna o retira acceso mediante la operación del módulo de acceso, entonces el cambio queda limitado a esa cuenta y módulo y se audita. 2. Dada una solicitud sin permiso vigente o sobre un módulo no disponible, cuando se intenta el cambio, entonces se deniega en backend y no cambia el acceso. 3. Dada una cuenta desactivada, cuando intenta iniciar una sesión nueva, entonces no obtiene acceso y conserva sus registros organizacionales. 4. Dada una cuenta desactivada o con acceso administrativo revocado, entonces se cierran de inmediato todas sus sesiones abiertas y una petición posterior no usa el permiso anterior. |
| **Requisito de origen** | `RF-ACC-002` confirmado para membresías; `RF-ACC-005` candidato para asignación de módulos |
| **Dependencias** | HU-ACC-001, HU-ACC-003, HT-GEN-002 |

### Refinamiento candidato de HU-ACC-003 — Usar funciones según permisos de operación y recurso

| Campo | Dato |
|---|---|
| **Código de referencia** | `HU-ACC-003` (refinamiento propuesto de la ficha de v2.5) |
| **Usuario** | usuaria interna; Superadministradora con acceso transversal a las operaciones publicadas de todos los módulos |
| **Descripción** | Como usuaria interna, quiero que cada operación se limite a los módulos, recursos y acciones que me fueron concedidos, para proteger los registros y respetar las responsabilidades de la organización. |
| **Prioridad / sprint / responsable** | La base de autorización se prepara en S2; las operaciones y correcciones de cada módulo se implementan en S3–S5 con su módulo propietario. Prioridad, estimación y responsable siguen pendientes. |
| **Criterios candidatos** | 1. Dada una usuaria con permiso para consultar un recurso, cuando solicita una acción no concedida sobre ese recurso, entonces el backend la deniega sin modificar datos. 2. Dada una persona sin autoridad administrativa, cuando intenta asignar módulos, delegar autoridad o configurar un módulo, entonces se deniega aunque conozca la dirección de la operación. 3. Dada la Superadministradora activa, cuando ejecuta una acción ordinaria o administrativa de cualquier módulo, entonces el backend reconoce su autoridad transversal sin asignación individual y el módulo valida y audita el cambio. 4. Dada una corrección de registro histórico, cuando el módulo la acepta, entonces crea una rectificación auditable en vez de reescribir el evento original. 5. Dada una opción o valor de campo existente declarado configurable, cuando la Superadministradora lo cambia desde el panel, entonces quedan valor anterior, nuevo, actor y vigencia cuando aplique. |
| **Requisito de origen** | `RF-ACC-003` confirmado; `RF-ACC-005` candidato |
| **Dependencias** | HU-ACC-001, HT-GEN-002, HT-GEN-003 |

### Historia 52 — Asignar o retirar acceso a módulos

| Campo | Dato |
|---|---|
| **Código de referencia** | `HU-ACC-005` |
| **Usuario** | Superadministradora organizacional (rol reportado como validado por la presidenta según el tesista; evidencia pendiente de adjuntar) |
| **Descripción** | Como persona con autoridad vigente, quiero asignar o retirar módulos por cuenta para limitar el acceso a las funciones necesarias. |
| **Prioridad / sprint** | Base de asignación de accesos en S2; las acciones de cada módulo se entregan en S3–S5 según reglas y capacidad. |
| **Criterios de aceptación** | 1. Dada una asignación permitida, cuando se agrega un módulo mediante la operación pública de acceso, entonces queda asociada a la cuenta correcta y se registra quién, cuándo y por qué la cambió. 2. Dada una solicitud fuera de la autoridad o de una lista de módulos habilitados, cuando se presenta, entonces el backend la rechaza sin cambios. 3. Dado que se retira un módulo, cuando la persona intenta acceder a una operación del módulo, entonces se vuelve a verificar la asignación vigente. Si se revoca acceso administrativo, se cierran de inmediato todas las sesiones abiertas de esa cuenta. |
| **Requisito de origen** | `RF-ACC-005` candidato |
| **Dependencias** | HU-ACC-001, HU-ACC-003, HT-GEN-002 |

### Historia 53 — Conceder o revocar autoridad administrativa

| Campo | Dato |
|---|---|
| **Código de referencia** | `HU-ACC-006` |
| **Usuario** | persona que ya tenga permiso expreso para delegar autoridad; la primera Superadministradora la designa el tesista durante instalación con autorización registrada de la presidenta |
| **Descripción** | Como delegante autorizado, quiero conceder o retirar a otra cuenta una autoridad delimitada, para mantener el control del panel cuando cambien responsabilidades. |
| **Prioridad / sprint** | Definición en S1; emisión inicial en S2 conforme a la autorización presidencial registrada. Delegación posterior solo cuando se valide su regla; prioridad y estimación pendientes. |
| **Criterios de aceptación** | 1. Dada una delegación permitida, cuando se concede o revoca autoridad a otra cuenta, entonces se guarda el alcance, vigencia, actor, motivo y resultado. 2. Dado un intento de conceder autoridad a la propia cuenta, cuando se procesa, entonces se deniega y no cambia ningún permiso. 3. Dada una persona sin permiso de delegación, cuando intenta transferir la autoridad, entonces se deniega en backend. 4. Dado un cambio de presidencia o ausencia de la persona delegante, cuando se necesita transferir la autoridad, entonces se aplica el procedimiento que se acuerde antes de habilitar esa operación; el procedimiento actual está pendiente de definición. |
| **Requisito de origen** | `RF-ACC-005` candidato |
| **Dependencias** | HU-ACC-003, HT-GEN-002, HT-GEN-003 |

### Historia 54 — Consultar intentos recientes y configurar bloqueo de acceso

| Campo | Dato |
|---|---|
| **Código de referencia** | `HU-ACC-007` |
| **Usuario** | administradora con permiso de seguridad de acceso |
| **Descripción** | Como administradora autorizada, quiero consultar el conteo disponible de intentos fallidos recientes por cuenta y proponer límites de bloqueo acotados, para proteger el acceso sin exponer credenciales. |
| **Prioridad / sprint** | Definición en S1; consulta y configuración de acceso candidatas para S2 según criterios validados, capacidad y actualización de SPEC-001. |
| **Criterios de aceptación** | 1. Dado un permiso válido, cuando se consulta una cuenta, entonces se muestra solo el conteo y estado temporal que el sistema conserva, sin contraseña, token ni supuesto historial no almacenado. 2. Dado un umbral o duración fuera de los rangos aprobados, cuando se intenta guardar, entonces se rechaza. 3. Dada una política propuesta, cuando se guarda con autorización y validación, entonces queda auditada y versionada; la política nueva no toma efecto hasta la validación y actualización requeridas de SPEC-001. 4. Dado un usuario sin permiso de seguridad, cuando solicita esa vista o el cambio, entonces se deniega. |
| **Requisito de origen** | `RF-ACC-005` candidato; `SPEC-001` confirmado requiere revisión antes de cambiar sus valores |
| **Dependencias** | HU-ACC-001, HT-GEN-002, HT-GEN-003 |

### Historia 55 — Gestionar catálogos y fórmulas expuestos por los módulos

| Campo | Dato |
|---|---|
| **Código de referencia** | `HU-ACC-008` |
| **Usuario** | Superadministradora activa con autoridad transversal de configuración sobre opciones publicadas por el módulo |
| **Descripción** | Como Superadministradora, quiero editar desde el panel los valores y opciones de campos existentes, catálogos y fórmulas que cada módulo expone, para mantener la configuración sin cambiar el esquema de la base de datos. |
| **Prioridad / sprint** | Límites generales y permisos en S2; catálogos y fórmulas se implementan con cada módulo propietario en S3–S5, según reglas y capacidad validadas. |
| **Criterios de aceptación** | 1. Dado un módulo que expone un catálogo editable, cuando una persona autorizada guarda un cambio válido, entonces el módulo propietario valida y conserva la versión anterior. 2. Dada una fórmula, cuando se prueba antes de activarla, entonces el módulo muestra entradas, unidades y resultado de prueba para revisión. 3. Dada una fórmula válida, cuando se activa con aprobación y vigencia definidas, entonces obtiene una versión y fecha de vigencia; cálculos históricos conservan la versión previamente aplicada. 4. Dado código arbitrario, una fórmula inválida o una usuaria sin permiso, cuando se intenta guardar, entonces se rechaza sin ejecutar ni cambiar registros. |
| **Requisito de origen** | `RF-ACC-005` candidato; reglas productivas existentes que correspondan, por confirmar módulo a módulo |
| **Dependencias** | HU-ACC-003, HT-GEN-002, HT-GEN-003 y operaciones futuras de cada módulo propietario |

### Historia 56 — Consultar y corregir registros mediante el módulo propietario

| Campo | Dato |
|---|---|
| **Código de referencia** | `HU-ACC-009` |
| **Usuario** | Superadministradora activa; otras personas solo con permiso explícito para el dato y la operación |
| **Descripción** | Como Superadministradora, quiero crear, consultar y corregir desde el panel registros como asistencia, cantidades y valores que cada módulo ofrezca, para resolver el trabajo operativo y los errores sin borrar su origen ni alterar la historia. |
| **Prioridad / sprint** | S1 define los límites generales de acceso y configuración base. La profundidad, prioridad, capacidad, estimación e implementación de cada operación se asignan módulo por módulo. |
| **Criterios de aceptación** | 1. Dada una consulta dentro del alcance concedido, cuando se solicita, entonces se muestran únicamente campos autorizados y el propósito de uso se conserva pendiente de validar por categoría sensible. 2. Dada una corrección permitida, cuando el módulo la acepta, entonces conserva el original y registra una rectificación con actor, fecha, resultado, motivo y campos cambiados. 3. Dada una edición directa genérica, eliminación de auditoría o cambio a un dato fuera del permiso, cuando se solicita, entonces se deniega sin mutación. 4. Dada una corrección que afecta varias entidades, cuando falla una validación, entonces no queda una operación parcial; las reglas transaccionales pertenecen al módulo propietario. |
| **Requisito de origen** | `RF-ACC-005` candidato; RNF-AUD-001 y RNF-SEC-001 confirmados, según corresponda |
| **Dependencias** | HU-ACC-003, HT-GEN-002, HT-GEN-003 y operación de corrección del módulo propietario |

Los valores de bloqueo heredados de SPEC-001 siguen vigentes: tres fallos dentro de una ventana
de tres minutos, bloqueo de tres minutos y expiración por 30 minutos de inactividad. Como rango
de trabajo para validar, se propone conservar una ventana de tres minutos y permitir un umbral
de 3–10 intentos y un bloqueo de 3–15 minutos. Es solo una propuesta; no cambia SPEC-001. OWASP
advierte el riesgo de denegación de servicio por bloqueos y NIST SP 800-63B-4 establece un máximo
de 100 intentos en el contexto específico que describe, no una recomendación para este proyecto.
Fuentes: [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html),
[NIST SP 800-63B-4, §3.2.2](https://pages.nist.gov/800-63-4/sp800-63b.html).

## Condiciones

Las 51 historias de línea base proceden de RF confirmados. Los nueve temas de la entrevista permanecen como exploración en la [edición anterior](../../../documentacion/historias/usuario/historias_usuario_v2.4_2026-10-13.md); no tienen estimación ni sprint comprometido. Las cinco historias adicionales HU-ACC-005 a HU-ACC-009 son candidatas, no están confirmadas y no pertenecen a la línea base de 51 historias. La base de acceso y permisos se ubica en S2; las operaciones de negocio de HU-ACC-008/009 se distribuyen con sus módulos en S3–S5. Ninguna ficha acredita implementación o prueba.

## Historial de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 2.4 | 2026-10-13 | Tablas resumidas por prioridad y criterios por sección. |
| 2.5 | 2026-10-13 | Ficha individual por historia, con campos separados como la referencia visual. |
| 2.6 | 2026-10-27 | Candidata interna: se refinan HU-ACC-002/003, se añaden historias de administración y alcance de definición para S1 e implementación en S2 por decisión del tesista. La validación presidencial del rol se atribuye al tesista; evidencia pendiente de adjuntar. Requisitos detallados, prioridad, capacidad y estimación permanecen pendientes. |
