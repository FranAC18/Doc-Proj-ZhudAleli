---
titulo: Historias de usuario en fichas
version: "2.8"
actualizacion_diseno: "UI-01 a UI-08; instruccion del tesista; cumplimiento pendiente"
fecha: 2026-10-28
autor: Franklin Acero
estado: alcance-multicanal-aceptado-por-tesista-revision-academica-pendiente
historias: 60
historias_acceso_multicanal_aceptadas: 4
historias_base: 51
historias_superadmin_candidatas: 5
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-transferencia
---

## Precisión transversal de diseño — 2026-10-28

Esta edición conserva íntegro el alcance de la edición anterior y añade la instrucción
expresa del tesista sobre interfaces coherentes: UI-01 carga, UI-02 adaptación, UI-03
jerarquía, UI-04 tokens, UI-05 componentes, UI-06 accesibilidad, UI-07 estados y UI-08
interacción. Los criterios y su comprobación están en [Criterios de diseño v1.1](../../diseno/criterios_diseno_v1.1_2026-10-28.md).
Precisan RNF-UX-001 a 003 y RNF-CON-001, HT-GEN-004 y las HU con interfaz. Se aplican
a la porción nueva o modificada; SB-S1-04 conserva su historial y SB-S2-02 su avance.
No cambian los IDs, conteos, prioridades, fechas, estimaciones ni estados de terminación.
La identidad visual sigue provisional. Registrar reglas no acredita implementación,
pruebas de interfaz, validación con usuarias ni aprobación académica.

Edición anterior conservada: [historias_usuario_v2.7_2026-10-28.md](historias_usuario_v2.7_2026-10-28.md).



# Historias de usuario

Esta edición conserva las 51 fichas de la [v2.5](historias_usuario_v2.5_2026-10-13.md) y mantiene cinco historias candidatas de superadministración; incorpora cuatro historias de acceso aceptadas, para un total de 60 fichas. Cada historia tiene ficha propia; el **código HU** conserva la trazabilidad con requisitos, pila y pruebas. Las prioridades de la línea base proceden de [la clasificación de requisitos](../../requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13.md). Puntos, riesgo y responsables siguen pendientes de estimación o asignación. La organización por S2–S6 de las 51 fichas conservadas refleja el corte anterior: el [plan de sprints v1.6](../../sprints/plan_sprints_v1.6_2026-10-27.md) propone ahora S2–S5; ningún traslado de historia implica compromiso ni finalización.

La Superadministradora podrá realizar las acciones ordinarias de todos los módulos y gestionar desde su panel accesos, registros, asistencia, cantidades, valores de campos existentes y opciones publicadas. Esta decisión del tesista define el alcance de trabajo; `RF-ACC-005` y las cinco historias nuevas siguen propuestos mientras se completan criterios y validación por módulo.

## Actualización de acceso del 2026-10-28

Esta edición conserva la [historias_usuario_v2.6_2026-10-27.md](historias_usuario_v2.6_2026-10-27.md) y registra el plan de acceso por correo, passkeys y WhatsApp aceptado expresamente por el tesista. RF-ACC-006 a 009, HU-ACC-010 a 013 y SB-S2-05 a 09 identifican la ampliación. Su implementación está pendiente; no se atribuyen pruebas, validación con usuarias ni publicación al docente. RF-ACC-005 conserva estado propuesto. La aceptación no fija puntos ni fechas nuevas.


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
| **Usuario** | usuaria interna; Superadministradora con autoridad transversal para las operaciones publicadas de todos los módulos |
| **Nombre de la historia** | Usar funciones según responsabilidades |
| **Prioridad en negocio** | Esencial (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna, quiero realizar solo operaciones permitidas por mi perfil, cargo o encargo, para respetar las responsabilidades de la organización. |
| **Criterios de aceptación** | 1. Dado un encargo vencido o un cargo sin autorización, cuando una usuaria normal intenta una operación restringida, entonces se rechaza sin cambiar datos.<br>2. Dada una Superadministradora activa, cuando ejecuta una operación ordinaria publicada por cualquier módulo, entonces se verifica su autoridad transversal en servidor sin exigir asignación individual a ese módulo; las reglas de negocio siguen aplicando. |
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
| **Criterios de aceptación** | 1. Dada una cuenta de socia, cuando una persona autorizada la desactiva, entonces cesan los nuevos accesos, se cierran de inmediato todas sus sesiones abiertas y se conservan sus registros.<br>2. Dada una socia sin permiso, cuando intenta cambiar una membresía, entonces el sistema rechaza el cambio.<br>3. Dada una Superadministradora activa, cuando administra una membresía, entonces el servidor acepta su autoridad transversal y audita el resultado. |
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

## Historias candidatas de superadministración

Estas cinco fichas se añaden fuera de las 51 historias de la línea base aprobada. El
tesista comunicó que la presidenta validó el rol de Superadministradora; falta la
referencia de evidencia. El alcance transversal fue precisado por el tesista el
2026-10-27. Los criterios detallados por módulo y el requisito `RF-ACC-005` siguen
propuestos. Los refinamientos de `HU-ACC-002/003` constan en sus fichas de S2.

### Historia 52 — Asignar o retirar acceso a módulos

| Campo | Dato |
|---|---|
| **Número** | 52 |
| **Código de referencia** | `HU-ACC-005` |
| **Usuario** | Superadministradora activa |
| **Nombre de la historia** | Asignar o retirar acceso a módulos |
| **Prioridad en negocio** | Pendiente de validar |
| **Riesgo en desarrollo** | Alto: permisos y sesiones |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | Base de accesos S2; operaciones de cada módulo S3–S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Superadministradora, quiero asignar o retirar el acceso de otras cuentas a módulos concretos para mantener sus funciones vigentes. Mi propio rol accede a todos los módulos sin asignación individual. |
| **Criterios de aceptación** | 1. Un cambio autorizado afecta solo a la cuenta y módulo indicados y registra actor, fecha y motivo.<br>2. Una petición sin autoridad se deniega sin modificar accesos.<br>3. Al revocar acceso administrativo se cierran de inmediato todas las sesiones abiertas de la cuenta; el servidor rechaza nuevas operaciones protegidas. |
| **Requisito de origen** | `RF-ACC-005` propuesto; `RF-ACC-002/003` confirmados para cuentas y permisos existentes |
| **Dependencias** | HU-ACC-001/002/003 y definición de autoridad inicial |
| **Observaciones** | Candidata; no acredita implementación ni validación del detalle. |

### Historia 53 — Conceder o revocar autoridad administrativa

| Campo | Dato |
|---|---|
| **Número** | 53 |
| **Código de referencia** | `HU-ACC-006` |
| **Usuario** | Persona autorizada para delegar; primera designación a cargo del tesista durante la instalación |
| **Nombre de la historia** | Conceder o revocar autoridad administrativa |
| **Prioridad en negocio** | Pendiente de validar |
| **Riesgo en desarrollo** | Alto: elevación de privilegios |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | Primera designación S2; delegación posterior sujeta a regla validada |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como delegante autorizado, quiero conceder o retirar autoridad administrativa a otra cuenta para mantener la administración cuando cambien las responsabilidades. |
| **Criterios de aceptación** | 1. El tesista designa la primera Superadministradora durante la instalación solo con autorización registrada de la presidenta.<br>2. Una delegación futura registra alcance, actor, fecha, motivo y resultado; la autoelevación se rechaza.<br>3. Revocar autoridad cierra de inmediato las sesiones abiertas de la cuenta. |
| **Requisito de origen** | `RF-ACC-005` propuesto |
| **Dependencias** | Procedimiento de autorización presidencial y regla de delegación aún pendientes |
| **Observaciones** | La constancia de autorización y la transferencia ante cambio de presidencia requieren definición. |

### Historia 54 — Consultar intentos y configurar acceso

| Campo | Dato |
|---|---|
| **Número** | 54 |
| **Código de referencia** | `HU-ACC-007` |
| **Usuario** | Superadministradora activa |
| **Nombre de la historia** | Consultar intentos y configurar acceso |
| **Prioridad en negocio** | Pendiente de validar |
| **Riesgo en desarrollo** | Alto: seguridad de acceso |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2, solo con límites validados y actualización de SPEC-001 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Superadministradora, quiero ver el estado de intentos disponible y ajustar parámetros de bloqueo desde el panel para administrar el acceso sin exponer credenciales. |
| **Criterios de aceptación** | 1. La consulta muestra solo datos de intentos realmente conservados, sin contraseñas ni tokens.<br>2. Un valor fuera de límites aprobados o una petición sin autoridad se rechaza.<br>3. Un cambio aceptado conserva valor anterior, nuevo, actor, motivo y vigencia; no toma efecto antes de la actualización validada de SPEC-001. |
| **Requisito de origen** | `RF-ACC-005` propuesto; SPEC-001 vigente para valores y mensajes |
| **Dependencias** | Validación de límites, retención y regla de consulta |
| **Observaciones** | Se mantienen los mensajes específicos de acceso y los valores vigentes hasta una decisión validada. |

### Historia 55 — Editar opciones y valores configurables de módulos

| Campo | Dato |
|---|---|
| **Número** | 55 |
| **Código de referencia** | `HU-ACC-008` |
| **Usuario** | Superadministradora activa |
| **Nombre de la historia** | Editar opciones y valores configurables de módulos |
| **Prioridad en negocio** | Pendiente de validar |
| **Riesgo en desarrollo** | Alto si afecta cálculos o historia |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S3–S5 con el módulo propietario |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Superadministradora, quiero editar desde el panel los valores de campos existentes, opciones, catálogos y fórmulas que cada módulo ofrezca para mantener la configuración aprobada. |
| **Criterios de aceptación** | 1. Un valor u opción válida se guarda con actor, fecha, valor anterior y nuevo y vigencia cuando aplique.<br>2. Un valor fuera de rango o código arbitrario se rechaza sin cambios.<br>3. Una fórmula se prueba y versiona antes de activarse; cálculos históricos conservan su versión.<br>4. El panel no crea campos físicos ni altera tablas. |
| **Requisito de origen** | `RF-ACC-005` propuesto y reglas del módulo correspondiente |
| **Dependencias** | Módulo propietario, catálogo de opciones y valores aprobados |
| **Observaciones** | El detalle se define al construir cada módulo; no es un configurador genérico del esquema. |

### Historia 56 — Crear y corregir registros de cualquier módulo

| Campo | Dato |
|---|---|
| **Número** | 56 |
| **Código de referencia** | `HU-ACC-009` |
| **Usuario** | Superadministradora activa |
| **Nombre de la historia** | Crear y corregir registros de cualquier módulo |
| **Prioridad en negocio** | Pendiente de validar |
| **Riesgo en desarrollo** | Alto: integridad e historia |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S3–S5 con cada módulo implementado |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como Superadministradora, quiero realizar las acciones normales y crear o corregir desde el panel asistencia, cantidades, valores y otros registros ofrecidos por cada módulo para resolver el trabajo y los errores. |
| **Criterios de aceptación** | 1. La Superadministradora ejecuta una operación ordinaria de cualquier módulo sin asignación individual; una cuenta sin permiso recibe denegación.<br>2. El módulo aplica sus validaciones y aprobaciones a la captura o corrección.<br>3. Una corrección histórica conserva el original y añade rectificación auditable; un fallo no deja cambios parciales. |
| **Requisito de origen** | `RF-ACC-005` propuesto; requisitos de negocio y auditoría del módulo |
| **Dependencias** | Operaciones, datos y reglas del módulo propietario |
| **Observaciones** | No se declaran funciones de módulos futuros como implementadas por esta ficha. |

## Condiciones

Las 51 historias de la línea base proceden de RF confirmados; las historias 52–56 proceden de `RF-ACC-005` propuesto y no están aprobadas por esta edición. Los nueve temas de la entrevista permanecen como exploración en la [edición anterior](historias_usuario_v2.4_2026-10-13.md). La ubicación por sprint de las fichas anteriores es histórica y se contrasta con el plan v1.6; las cinco historias de superadministración conservan sus condiciones pendientes. Las cuatro historias de acceso de esta edición pertenecen a S2 por aceptación del tesista y siguen sin estimación. Ninguna ficha acredita implementación o prueba.

## Ampliación de Sprint 2 aceptada — acceso multicanal

### Historia 57 — Ingresar mediante código por correo

| Campo | Dato |
|---|---|
| **Número** | 57 |
| **Código de referencia** | HU-ACC-010 |
| **Usuario** | usuaria interna con cuenta activa y correo verificado |
| **Nombre de la historia** | Ingresar mediante código por correo |
| **Prioridad en negocio** | Alta; orden de ejecución por dependencias |
| **Riesgo en desarrollo** | Alto: autenticación y recuperación |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint** | S2, alcance aceptado |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna con cuenta activa y correo verificado, quiero recibir e introducir un código en mi correo verificado, para ingresar sin depender de recordar una contraseña. |
| **Criterios de aceptación** | 1. La solicitud pública responde de forma genérica exista o no la cuenta; solo una cuenta activa y un correo previamente verificado reciben un código utilizable.<br>2. El código tiene seis dígitos, vence a los cinco minutos, admite como máximo cinco intentos de validación y solo puede consumirse una vez, incluso ante solicitudes concurrentes.<br>3. Hay al menos 60 segundos entre reenvíos, un máximo por hora definido antes de activar el canal y límites por cuenta y origen sin revelar la existencia de cuentas.<br>4. El código se genera con CSPRNG y se almacena protegido mediante hash con sal o HMAC con secreto fuera de la base de datos; se verifica en tiempo constante y no aparece en logs.<br>5. Una validación correcta abre una sesión Django con las mismas restricciones, vencimiento y permisos del acceso existente; una cuenta inactiva nunca obtiene sesión. |
| **Requisito de origen** | RF-ACC-006; RNF-SEC-001; RNF-PRV-001 |
| **Tareas** | SB-S2-05, SB-S2-06, SB-S2-09 |
| **Estado** | Alcance aceptado por el tesista el 2026-10-28; implementación y validación pendientes |

### Historia 58 — Registrar y utilizar passkeys

| Campo | Dato |
|---|---|
| **Número** | 58 |
| **Código de referencia** | HU-ACC-011 |
| **Usuario** | usuaria interna con cuenta activa y acceso recientemente verificado |
| **Nombre de la historia** | Registrar y utilizar passkeys |
| **Prioridad en negocio** | Alta; orden de ejecución por dependencias |
| **Riesgo en desarrollo** | Alto: autenticación y recuperación |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint** | S2, alcance aceptado |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna con cuenta activa y acceso recientemente verificado, quiero registrar y usar una passkey en mi dispositivo, para ingresar de forma sencilla mediante huella, rostro o PIN. |
| **Criterios de aceptación** | 1. El registro exige sesión de la cuenta y una verificación reciente mediante un canal previamente asociado; escribir un correo o conocer solo la contraseña no vincula una passkey.<br>2. El servidor valida desafío de un solo uso, expiración, tipo de operación, origen, RP ID, firma y verificación de usuario; no acepta una credencial de otra cuenta.<br>3. Se almacenan identificador de credencial, clave pública y metadatos necesarios; no se reciben ni almacenan huellas, imágenes faciales ni claves privadas.<br>4. La usuaria puede mantener varias passkeys y revocarlas tras reautenticarse; se notifica el registro y la revocación por un canal verificado.<br>5. El dispositivo elige huella, rostro o PIN; la interfaz detecta compatibilidad y ofrece correo como alternativa. Se usa HTTPS y dominio estable; localhost sirve para desarrollo.<br>6. Una passkey revocada, una cuenta inactiva o un desafío reutilizado no permiten acceso; los permisos y el cambio inicial pendiente se aplican igualmente. |
| **Requisito de origen** | RF-ACC-007; RNF-SEC-001; RNF-PRV-001 |
| **Tareas** | SB-S2-05, SB-S2-07, SB-S2-09 |
| **Estado** | Alcance aceptado por el tesista el 2026-10-28; implementación y validación pendientes |

### Historia 59 — Ingresar mediante código por WhatsApp

| Campo | Dato |
|---|---|
| **Número** | 59 |
| **Código de referencia** | HU-ACC-012 |
| **Usuario** | usuaria interna con cuenta activa y teléfono verificado |
| **Nombre de la historia** | Ingresar mediante código por WhatsApp |
| **Prioridad en negocio** | Alta; orden de ejecución por dependencias |
| **Riesgo en desarrollo** | Alto: autenticación y recuperación |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint** | S2, alcance aceptado |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna con cuenta activa y teléfono verificado, quiero recibir e introducir un código por WhatsApp, para acceder con un canal que tenga disponible. |
| **Criterios de aceptación** | 1. El teléfono está asociado y verificado con consentimiento antes de usarlo para acceder; un número escrito en el formulario no modifica la cuenta ni crea una usuaria.<br>2. El OTP aplica los mismos controles de generación, almacenamiento, expiración de cinco minutos, cinco intentos, uso único, cooldown y límites de RF-ACC-006.<br>3. Existe un adaptador para Meta Cloud API y un mock aislado de desarrollo y pruebas; los secretos y la selección del proveedor se configuran por entorno.<br>4. El modo mock no entrega mensajes reales ni se habilita como mecanismo de autenticación de producción; la interfaz no ofrece un canal real sin configurar.<br>5. La activación real exige cuenta y número emisor, plantilla de autenticación aprobada, consentimiento, comprobación del costo y prueba de entrega; desarrollar el adaptador no acredita entrega real.<br>6. Las respuestas públicas son genéricas; se distinguen solicitud aceptada por el proveedor, entrega confirmada y fallo, sin registrar códigos ni datos de contacto completos. |
| **Requisito de origen** | RF-ACC-008; RNF-SEC-001; RNF-PRV-001 |
| **Tareas** | SB-S2-05, SB-S2-08, SB-S2-09 |
| **Estado** | Alcance aceptado por el tesista el 2026-10-28; implementación y validación pendientes |

### Historia 60 — Recuperar el acceso y proteger la cuenta

| Campo | Dato |
|---|---|
| **Número** | 60 |
| **Código de referencia** | HU-ACC-013 |
| **Usuario** | usuaria interna que perdió el dispositivo o sus credenciales |
| **Nombre de la historia** | Recuperar el acceso y proteger la cuenta |
| **Prioridad en negocio** | Alta; orden de ejecución por dependencias |
| **Riesgo en desarrollo** | Alto: autenticación y recuperación |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint** | S2, alcance aceptado |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Como usuaria interna que perdió el dispositivo o sus credenciales, quiero recuperar mi acceso y retirar las credenciales que ya no controlo, para volver a usar la aplicación sin dejar expuesta mi cuenta. |
| **Criterios de aceptación** | 1. El correo verificado permite recuperar acceso al perder el dispositivo y revocar passkeys previas tras reautenticación; no se cambia el destino de recuperación desde una solicitud pública.<br>2. La recuperación de usuario envía su nombre solo al correo asociado y la respuesta pública permanece genérica; recuperar acceso no crea cuentas ni amplía permisos.<br>3. Para la contraseña del acceso de respaldo se usa un enlace con token aleatorio almacenado como hash, válido durante 20 minutos y consumido una sola vez; se valida la política de contraseñas existente.<br>4. Al restablecer la contraseña se invalidan los tokens pendientes, se cierran las sesiones activas y se envía un aviso; las passkeys perdidas se revocan de forma explícita.<br>5. Si must_change_password está pendiente, todos los métodos dejan acceso restringido: solicitar y validar código por canal disponible, definir nueva contraseña y recién entonces habilitar funciones privadas.<br>6. La ausencia de canales verificados no habilita una recuperación insegura: el procedimiento asistido requiere definir responsable y comprobación de identidad antes de implementarlo. |
| **Requisito de origen** | RF-ACC-009; RNF-SEC-001; RNF-PRV-001 |
| **Tareas** | SB-S2-05, SB-S2-09 |
| **Estado** | Alcance aceptado por el tesista el 2026-10-28; implementación y validación pendientes |

## Historial de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 2.4 | 2026-10-13 | Tablas resumidas por prioridad y criterios por sección. |
| 2.5 | 2026-10-13 | Ficha individual por historia, con campos separados como la referencia visual. |
| 2.6 | 2026-10-27 | Conserva 51 historias de base, refina HU-ACC-002/003 y añade cinco historias candidatas de Superadministración, con alcance transversal y criterios por módulo. Preparada para revisión; no publicada. |

| 2.7 | 2026-10-28 | Añade HU-ACC-010 a 013 aceptadas para acceso multicanal; conserva 51 de base y cinco candidatas de superadministración, sin marcar criterios cumplidos. |


## Control editorial de esta edición

2.7 → 2.8, 2026-10-28: precisión de criterios UI-01 a UI-08; fuentes y fichas previas conservadas. Revisión académica y publicación pendientes.
