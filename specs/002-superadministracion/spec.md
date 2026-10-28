---
id: SPEC-002
title: Administración organizacional y configuración por módulos
type: feature-spec
status: proposed
created: 2026-10-27
source:
  - "Solicitud reportada por el tesista el 2026-10-27, citando a la presidenta; validación directa pendiente"
  - CAT-REQ-001 v1.2 y candidata v1.3
  - SPEC-001
  - "Constitución Zhud Alelí 2.0.0 y arquitectura modular aprobada"
sprint: "Definición candidata para S2; operaciones de negocio por módulo en S3-S5"
module: "acceso y módulos propietarios; límites pendientes de detalle"
actors:
  - "Superadministradora organizacional (rol propuesto)"
  - "Delegante con autoridad vigente (responsable por definir)"
  - "Usuaria interna"
  - "Presidenta del Comité (fuente reportada; validación y autoridad de delegación pendientes)"
validated_by: []
related:
  - "../../docs/requirements/proposals/2026-10-27-CAT-REQ-001-v1.3-superadmin.md"
  - "../../docs/requirements/proposals/2026-10-27-historias-usuario-v2.6-superadmin.md"
  - "../../docs/decisions/proposals/2026-10-27-plan-implementacion-superadmin-v1.0.md"
  - "../001-acceso-usuarias-internas/spec.md"
---

# Especificación candidata: Administración organizacional y configuración por módulos

- **Rama propuesta**: `feature/RF-ACC-005-superadministracion` (solo sugerencia; no creada)
- **Entrada del usuario**: definir criterios para la superadministración y preparar en S2 la estructura y los permisos de los módulos; sus funciones se desarrollan en S3-S5.

## Control de validación

| Elemento | Valor |
|---|---|
| Estado | `proposed`; incompleta para aprobación e implementación |
| Fuente primaria | Solicitud reportada por el tesista el 2026-10-27, citando a la presidenta; evidencia directa pendiente |
| Requisito | `RF-ACC-005` candidato en CAT-REQ-001 v1.3 propuesta; código sujeto a confirmación del tesista |
| Preparó | Codex, bajo instrucción del tesista |
| Debe validar | Tesista y presidenta del Comité; validar requisitos organizacionales con las representantes que correspondan |
| Fecha de validación | Pendiente |
| Evidencia | Pendiente; la conversación no se trata como aprobación de requisito por parte de la presidenta |
| Aprobación técnica | Pendiente; esta propuesta no modifica SPEC-001 ni autoriza código |

## Problema, valor y alcance

- **Actor afectado**: la persona a quien la organización otorgue autoridad administrativa para mantener cuentas y configurar capacidades habilitadas.
- **Problema reportado**: la presidenta pidió, según relata el tesista, una autoridad para administrar cuentas, módulos y datos del sistema. La evidencia directa del alcance organizacional y la regla de delegación siguen pendientes.
- **Precisión posterior del tesista**: la Superadministradora puede realizar todas las acciones de una usuaria normal en todos los módulos y, desde un panel propio, gestionar accesos, registros, valores de campos existentes y opciones configurables. La frase anterior que excluía una autoridad transversal de negocio queda sustituida por esta decisión. No se solicita crear columnas o campos físicos desde el panel.
- **Valor esperado**: gestionar cuentas, accesos, acciones ordinarias y configuraciones de cada módulo desde un panel unificado, con reglas de negocio, autorización en servidor y conservación de historia.
- **Incluye como propuesta**: todas las acciones ordinarias que el sistema ofrezca en cada módulo; alta/baja lógica o activación/desactivación de cuentas; asignación y retiro de accesos; concesión/revocación de autoridad a otras personas con reglas por definir; captura o corrección de asistencia, cantidades y valores por el flujo del módulo; consulta limitada de intentos recientes; parámetros de bloqueo tras actualizar SPEC-001; edición de valores y opciones de campos existentes que cada módulo declare configurables; fórmulas seguras con prueba, versión y vigencia. Los mensajes específicos de SPEC-001 se conservan por decisión del tesista.
- **No incluye**: alterar el esquema o crear columnas desde el panel; consultas o escrituras directas a la base de datos; alterar o borrar auditoría; sobrescribir movimientos históricos; editar o mostrar contraseñas, tokens o secretos; código arbitrario como fórmula; recalcular registros históricos de manera retroactiva; recuperación de cuentas todavía no diseñada; declarar implementada o comprometida una operación solo por ubicarla en un sprint.
- **Incremento utilizable de S2**: acceso y administración de cuentas con permisos comprobables; navegación y contratos de los módulos futuros solo cuando correspondan a un recorrido real. Su resultado sigue pendiente de implementación y verificación.
- **Capacidades anteriores afectadas**: SPEC-001 conserva su alcance de acceso propio, comportamiento de login y vencimiento de sesión. No se altera su regla vigente por esta propuesta.

## Escenarios candidatos y verificación

Los siguientes escenarios son propuestas de verificación, no criterios validados. Cada operación debe tener una prueba permitida y otra denegada. La corrección no elimina el dato original cuando pertenece a una historia de eventos.

**Regla transversal del rol propuesta:** una cuenta activa con autoridad de Superadministradora
dispone de las acciones ordinarias de todos los módulos y de sus acciones administrativas
publicadas, sin necesitar una asignación individual de módulo. Cada petición comprueba esa
autoridad en backend. El módulo propietario conserva sus validaciones, restricciones,
aprobaciones que correspondan y escritura de datos. Los campos editables son datos o
parámetros de campos ya definidos por el módulo; crear un campo físico, una tabla o una
operación nueva exige desarrollo y migración, fuera del panel.

### Corte de aceptación propuesto para S2

Este corte separa la base administrativa del trabajo de negocio de S3-S5. Los criterios
de `RF-ACC-005` permanecen candidatos hasta validar el requisito; `RF-ACC-002/003` y
SPEC-001 conservan sus reglas vigentes.

| ID | Resultado observable y comprobación | Estado de decisión |
|---|---|---|
| SA-S2-01 | Una persona autorizada crea una cuenta interna sin autorregistro; se comprueba unicidad, estado inicial y que una persona sin permiso recibe denegación sin crear cuenta. | Candidato; el alta inicial de autoridad sigue el procedimiento de SA-S2-08. |
| SA-S2-02 | Una persona autorizada activa o desactiva otra cuenta; una cuenta inactiva no inicia sesión y el cambio conserva sus registros relacionados. Al desactivarla se cierran de inmediato todas sus sesiones abiertas; se comprueba con dos sesiones y una petición denegada. | Decisión expresa del tesista sobre sesiones; autorización de la operación aún candidata. |
| SA-S2-03 | Una autoridad vigente concede o retira acceso a un módulo concreto de otra cuenta; cada petición posterior verifica el permiso actual en backend. Al revocar acceso administrativo se cierran de inmediato todas las sesiones abiertas de esa cuenta. Se comprueba con dos sesiones y auditoría del cambio. | Decisión expresa del tesista sobre sesiones; definir emisión y revocación de autoridad. |
| SA-S2-04 | El panel de la Superadministradora prepara acceso transversal a los módulos previstos y muestra las acciones ya publicadas. Una URL o petición directa sin autoridad se deniega en backend sin filtrar datos privados ni mutar registros. | Candidato; las operaciones disponibles se definen al construir cada módulo. |
| SA-S2-05 | Toda alta, cambio de estado, concesión y retiro registra actor, fecha, acción, recurso, resultado y motivo cuando corresponda; la auditoría no se edita desde el panel. | Candidato; precisar retención y acceso de lectura. |
| SA-S2-06 | La configuración de umbral, bloqueo y sesión muestra el valor vigente y rechaza cambios sin permiso, fuera de límites aprobados o sin motivo; cada cambio aceptado conserva valor anterior, nuevo, actor y vigencia. | Condicionado a validar rangos y actualizar SPEC-001; valores actuales siguen vigentes mientras tanto. |
| SA-S2-07 | El restablecimiento de acceso no muestra ni devuelve la contraseña anterior. Un flujo de recuperación solo se considera aceptado con verificación de identidad, caducidad, uso único y auditoría probados. | Pendiente de canal y autoridad; no forma parte del incremento hasta validarlo. |
| SA-S2-08 | Durante la instalación, el tesista designa la primera superadministradora solo con autorización de la presidenta registrada; el procedimiento es reproducible, no concede autoridad organizacional por `is_staff`/`is_superuser` y deja evidencia de quién habilitó la cuenta. | Procedimiento decidido por el tesista; formato y constancia de autorización presidencial pendientes antes de ejecutarlo. |

**Criterio de cierre de S2:** se muestran recorridos permitidos y denegados para las
operaciones habilitadas, pruebas de acceso y regresión de SPEC-001, migraciones reproducibles
en PostgreSQL y evidencia de permisos. Un criterio condicionado no se marca cumplido por
haber creado una pantalla o tabla.

Las configuraciones, fórmulas, consultas y rectificaciones de datos productivos u
organizacionales de HU-04/HU-05 se aceptan con el módulo dueño en S3-S5, después de validar
sus reglas. S2 prepara la autoridad transversal, el mapa de acciones y los permisos que esos
recorridos necesitarán.

### Criterios transversales para cada módulo en S3-S5

| ID | Criterio candidato | Verificación |
|---|---|---|
| SA-MOD-01 | La Superadministradora puede ejecutar cada acción ordinaria disponible para una usuaria del módulo, desde su panel o interfaz de trabajo, sin asignación individual al módulo. | Caso positivo de Superadministradora y caso denegado de cuenta sin acceso; ambos por petición directa al servidor. |
| SA-MOD-02 | Puede crear o corregir registros operativos, como asistencia, cantidades y valores, mediante el flujo propio del módulo. Las restricciones de unicidad, cortes, unidades, aprobaciones e historia siguen aplicando. | Registro válido, solicitud inválida y corrección con original y rectificación visibles. |
| SA-MOD-03 | Puede editar opciones, catálogos, parámetros y valores de campos existentes que el módulo declare configurables desde el panel; cada cambio conserva actor, fecha, valor anterior, valor nuevo y vigencia cuando aplique. | Cambio permitido, valor fuera de rango denegado y reconstrucción del historial. |
| SA-MOD-04 | Si se necesita un campo, cálculo u operación que el módulo aún no ofrece, el panel no modifica el esquema: se especifica e implementa un incremento del módulo con migración y pruebas. | La interfaz solo presenta opciones publicadas; un intento de alterar estructura o ejecutar código arbitrario se rechaza. |

El catálogo exacto de acciones, campos, opciones y reglas se completa al desarrollar cada
módulo; este criterio transversal no declara que los módulos de S3-S5 ya existan.

### HU-01 — Asignar un módulo a otra cuenta

**Como** Superadministradora con autoridad vigente, **quiero** habilitar un módulo concreto para otra cuenta, **para** limitarla a las funciones que necesita.

**Prueba independiente**: asignar un módulo disponible mediante la operación del propietario, confirmar el nuevo acceso, intentar la misma operación sin permiso y comprobar que la segunda solicitud no cambia datos.

**Criterios candidatos**:

1. **Dado** un actor y un módulo permitidos, **cuando** solicita la asignación, **entonces** el backend valida alcance y estado, ejecuta la operación pública y deja una auditoría del cambio.
2. **Dado** un actor sin permiso, **cuando** envía la misma solicitud directamente, **entonces** el backend la deniega sin mutación.
3. **Dada** una autoridad administrativa revocada, **cuando** se confirma el cambio, **entonces** se cierran de inmediato todas las sesiones abiertas de la cuenta y ninguna petición posterior usa el permiso anterior.

### HU-02 — Conceder autoridad administrativa a otra persona

**Como** delegante autorizado, **quiero** conceder o revocar una autoridad delimitada a otra cuenta, **para** mantener la administración organizacional.

**Prueba independiente**: conceder un permiso a otra cuenta, denegar una elevación propia y probar el procedimiento cuando cambia la presidencia.

**Criterios candidatos**:

1. **Dado** que el actor tiene permiso explícito de delegación, **cuando** concede o revoca autoridad a otra cuenta, **entonces** quedan registrados el alcance, vigencia, actor, motivo y resultado.
2. **Dado** que el actor intenta otorgar autoridad a sí mismo, **cuando** se procesa la solicitud, **entonces** se deniega sin cambios.
3. **Dado** un cambio de presidencia o la ausencia del delegante, **cuando** se necesita transferir autoridad, **entonces** la operación espera el procedimiento y número de aprobaciones que la organización valide.

### HU-03 — Ajustar y consultar la política de intentos fallidos

**Como** administradora autorizada para seguridad de acceso, **quiero** revisar el conteo reciente disponible y proponer un umbral de fallos y tiempo de bloqueo, **para** ajustar la protección con límites aprobados.

**Prueba independiente**: consultar el estado temporal de una cuenta autorizada, denegar una cuenta sin permiso y rechazar parámetros fuera del rango aprobado.

**Criterios candidatos**:

1. Hasta revisar y validar SPEC-001, se mantienen tres fallos dentro de tres minutos, bloqueo de tres minutos y expiración por 30 minutos de inactividad.
2. La consulta no muestra contraseñas ni tokens; no presenta un historial más amplio del que realmente se conserve.
3. Un cambio de parámetros requiere autorización, validación de límites, registro de actor/motivo/fecha y versión efectiva. El cambio de SPEC-001 es prerrequisito para activar valores nuevos.
4. La revocación de acceso administrativo cierra de inmediato todas las sesiones abiertas de la cuenta e impide cambios posteriores; la verificación se hace también en backend.

### HU-04 — Probar y poner en vigencia una configuración del módulo

**Como** Superadministradora, **quiero** probar una fórmula o cambio de catálogo ofrecido por el módulo antes de activarlo, **para** revisar el efecto sin modificar resultados históricos.

**Prueba independiente**: enviar expresión malformada o código arbitrario y comprobar que no se ejecuta; probar una expresión permitida y comparar la vista previa con el cálculo conocido del módulo.

**Criterios candidatos**:

1. El módulo propietario declara las configuraciones, unidades, entradas, límites y responsables de aprobación que admite.
2. Las fórmulas son expresiones en una gramática restringida; no se ejecutan Python, SQL, plantillas ni código arbitrario.
3. Una fórmula debe pasar validación de sintaxis, variables, unidades, límites y resultado de prueba antes de activarse.
4. Cada versión conserva fecha de vigencia y referencia en las operaciones calculadas. Una versión nueva no recalcula movimientos ni informes históricos automáticamente.
5. Una persona sin permiso de esa configuración no puede leer campos privados ni activar cambios.

### HU-05 — Consultar o corregir un dato de negocio

**Como** persona con permiso para una operación concreta, **quiero** consultar o solicitar la corrección del registro a través de su módulo propietario, **para** corregir errores sin borrar el origen ni perder trazabilidad.

**Prueba independiente**: intentar lectura permitida, lectura fuera de alcance, corrección autorizada y escritura genérica no autorizada; comparar original, rectificación y auditoría.

**Criterios candidatos**:

1. La autoridad de Superadministradora permite consultar y operar los datos que cada módulo ofrece a sus usuarias y administradoras; el backend comprueba el rol y el módulo aplica sus reglas de privacidad y propósito.
2. El módulo ejecuta sus validaciones e invariantes y es responsable de sus escrituras y migraciones.
3. Una corrección histórica crea un evento/rectificación relacionado con el original; no reemplaza ni borra el evento base.
4. Toda modificación registra actor, fecha, resultado, motivo y campos cambiados, dentro de la misma transacción que el cambio cuando aplique.
5. Las acciones sensibles de varias entidades confirman juntas o no dejan cambios parciales.

## Requisitos (Requirements)

### Requisito funcional candidato

- **RF-ACC-005**: Una Superadministradora activa puede ejecutar las funciones ordinarias de todos los módulos y, desde un panel administrativo, gestionar cuentas, accesos, registros, valores y opciones configurables que esos módulos expongan. Cada operación verifica autoridad en backend, respeta las reglas del módulo y conserva auditoría e historia. El panel no modifica el esquema de datos.
  - **Fuente**: solicitud reportada por el tesista el 2026-10-27, citando a la presidenta; validación directa pendiente.
  - **Actor/permiso**: rol Superadministradora propuesto, con acceso transversal a las operaciones publicadas de cada módulo sin asignaciones individuales; la primera designación la realiza el tesista durante la instalación con autorización registrada de la presidenta.
  - **Criterios candidatos**: escenarios HU-01 a HU-05, SA-S2-01 a SA-S2-08, SA-MOD-01 a SA-MOD-04 y matriz de permisos de esta spec.

### Requisitos no funcionales y reglas transversales

- **RNF-SEC-001** (confirmado en CAT-REQ-001 v1.2): aplicar autorización en backend y proteger datos y operaciones. Los controles visibles en UI no son una regla de autorización.
- **RNF-AUD-001** (confirmado en CAT-REQ-001 v1.2): conservar la auditoría conforme al requisito canónico; esta propuesta añade los campos de cambio reportados como candidatos, sujetos a confirmar retención y visibilidad.
- **RNF-PRV-001** (confirmado en CAT-REQ-001 v1.2): el acceso transversal de la Superadministradora se ejerce en las vistas y operaciones publicadas de cada módulo, con propósito y auditoría; los secretos y datos que una regla validada excluya siguen protegidos.
- **RN-RBAC-001 (candidata)**: `is_staff` y `is_superuser` son atributos técnicos de Django; no otorgan autoridad organizacional.
- **RN-MOD-001 (candidata)**: cada módulo conserva escrituras, reglas, validaciones, invariantes y migraciones; el panel coordina operaciones administrativas públicas, sin modificar tablas de forma genérica.
- **RN-AUD-001 (candidata)**: auditoría de cambios no editable desde la aplicación. Las rectificaciones son eventos nuevos relacionados, no sobrescrituras.
- **RN-CFG-001 (candidata)**: fórmulas/catálogos versionados y con vigencia; cualquier fórmula se valida, prueba y activa mediante el módulo responsable; los resultados históricos conservan la versión aplicada.
- **RN-SEC-002 (candidata)**: no editar ni devolver contraseñas existentes, tokens, secretos de despliegue o contenido de auditoría como si fueran datos ordinarios.
- **RN-PWA-001 (candidata, alineada a RF-PWA-001/002/003 confirmados)**: páginas administrativas y datos privados quedan fuera de cachés PWA y no se ofrecen sin sesión y permiso vigentes.

### Matriz actor → acción → recurso → resultado

Todos los resultados siguientes son candidatos hasta que la presidenta y el tesista validen reglas y alcance. «Permitido» describe la autoridad transversal propuesta para las operaciones publicadas; la matriz no define ni activa permisos en el producto.

| Actor | Acción | Recurso | Resultado candidato | Denegación / pendiente |
|---|---|---|---|---|
| Superadministradora activa | Asignar o retirar acceso | Cuenta y módulo habilitado | Operación pública de acceso valida el cambio y lo audita | Sin autoridad, cuenta/módulo no disponible o solicitud malformada: denegar en backend |
| Superadministradora activa | Activar/desactivar cuenta | Estado de cuenta | Cambio de estado con historial conservado; desactivación cierra sesiones abiertas de inmediato | No borrar registros asociados; petición sin autoridad denegada |
| Superadministradora activa | Ejecutar acciones ordinarias | Todos los módulos que existan | Puede realizar lo que realiza una usuaria normal, sin asignación individual a cada módulo | Reglas, validaciones y aprobaciones del módulo siguen vigentes |
| Superadministradora activa | Crear o corregir asistencia, cantidades y valores | Registros y campos existentes del módulo | Operación del módulo registra el dato o una rectificación trazable | No omitir cortes, duplicados, unidades ni controles aprobados |
| Superadministradora activa | Editar opciones de formulario, catálogos y parámetros | Opciones existentes declaradas configurables por el módulo | Cambio validado y auditado desde el panel | No crear campos físicos ni ejecutar código desde el panel |
| Delegante explícitamente autorizado | Conceder/revocar autoridad | Autoridad de otra cuenta | Cambio acotado, con vigencia y auditoría | Asignador inicial, transferencia y doble aprobación pendientes; autoelevación denegada |
| Usuaria interna con permiso específico | Consultar datos de negocio | Categoría, campos y módulo permitidos | Lectura limitada a su permiso y propósito | La Superadministradora accede transversalmente a las vistas publicadas, con reglas de privacidad vigentes |
| Usuaria interna autorizada | Corregir registro | Recurso expuesto por su módulo | El propietario valida y añade rectificación; conserva original | Sin autorización, fuera del flujo del módulo o borrado del histórico: denegar |
| Superadministradora activa | Editar catálogo | Catálogo que el módulo declara configurable | Operación propia del módulo crea versión/historial | No crear estructura nueva ni alterar otro módulo fuera de su operación |
| Superadministradora activa | Probar/activar fórmula | Fórmula/cálculo de ese módulo | Expresión segura validada, vista previa, versión y fecha de vigencia | Código arbitrario o falta de aprobación de negocio: denegar; recalcular historia: excluido |
| Superadministradora activa | Consultar intentos recientes | Estado temporal de bloqueo asociado a cuenta | Muestra conteo/estado actualmente retenido y minimizado | Historial completo, retención, identidad visible y búsqueda por cuenta pendientes |
| Superadministradora activa | Cambiar umbral y duración | Política de login en SPEC-001 | Solo después de aprobación, rango y versión efectiva | Antes de revisar/validar SPEC-001: conservar 3 fallos/3 minutos/bloqueo 3 minutos |
| Soporte técnico | Operar una función organizacional | Cuenta, módulo o dato de negocio | Ninguna autoridad de negocio implícita | Denegar salvo permiso organizacional independiente que se valide expresamente |
| Persona sin sesión/permiso | Cualquier operación privada | Cuenta, datos, configuración o historial | Sin resultado de negocio; mensaje de acceso denegado | No revelar si existe la cuenta ni campos privados |

### Datos y conceptos clave

| Concepto | Significado | Dueño propuesto | Reglas/retención pendientes |
|---|---|---|---|
| Cuenta y estado | Identidad de usuaria y condición para iniciar sesión | `accounts` / acceso | Baja lógica, reactivación, sesiones y retención |
| Asignación de módulo | Concesión acotada para módulos habilitados | `accounts` / acceso, sujeto a modelo aprobado | Cardinalidad, origen y efecto inmediato de revocación |
| Delegación de autoridad | Permiso para que otra persona administre acciones delimitadas | `accounts` / acceso | Alta inicial, presidencia, transferencia, expiración, doble aprobación |
| Política de login | Umbral y bloqueo, sin modificar vencimiento por inactividad | `accounts` / acceso | Rango, aprobación, vigencia y compatibilidad con SPEC-001 |
| Estado temporal de intentos | Contador temporal observado durante login | `accounts` / acceso | Consulta por cuenta, visibilidad, auditoría y retención; no afirmar historial que no existe |
| Configuración de módulo | Catálogo/fórmula controlada por el módulo que la expone | Módulo propietario de la regla y dato | Unidades, validación, aprobación, vigencia y migración |
| Versión de fórmula | Expresión validada usada por una operación calculada | Módulo productivo propietario | Gramática, funciones, precisión, redondeo, insumos y coexistencia |
| Rectificación | Evento que corrige o aclara un registro anterior | Módulo propietario | Quién puede aceptar corrección, evidencia y efectos posteriores |
| Evento de auditoría | Actor, tiempo, acción, recurso, resultado, motivo y campos cambiados | Mecanismo definido por arquitectura, fuente en el módulo propietario | Retención, acceso de lectura, anonimización y respaldo |

## Interfaz y experiencia

- Un panel administrativo unificado muestra a la Superadministradora todas las acciones ordinarias y administrativas que cada módulo haya publicado. El selector de módulo organiza el trabajo; no concede escritura directa sobre tablas.
- Cada acción confirma el recurso y el resultado esperado; las correcciones muestran el dato original y la nueva rectificación, con motivo obligatorio pendiente de validar.
- Deben existir estados vacío, cargando, guardado, error recuperable, denegación, permiso revocado y conflicto de vigencia.
- La búsqueda no revela existencia de cuentas a personas no autorizadas. La visibilidad de datos personales requiere una regla por categoría.
- Debe funcionar desde móvil y escritorio, con teclado, foco visible, mensajes textuales y contraste accesible según RNF-UX vigentes.
- El panel privado no entra al caché offline; no conserva datos privados en el dispositivo compartido.

## Criterios de éxito candidatos

- **SC-001**: cada operación administrativa documentada tiene un caso permitido y un caso denegado que verifica autorización en backend antes de mutar.
- **SC-002**: una corrección aprobada permite comparar el original y su rectificación y reconstruir el actor, fecha, resultado, motivo y campos cambiados.
- **SC-003**: una fórmula no puede activarse si falla la validación o prueba; la operación histórica sigue usando la versión original.
- **SC-004**: al desactivar una cuenta o revocar su acceso administrativo, sus sesiones abiertas se cierran de inmediato; ninguna petición posterior desde esas sesiones permite una acción protegida.
- **SC-005**: una usuaria representativa puede asignar un módulo, entender una denegación y corregir un registro autorizado con teclado y en pantalla móvil durante pruebas con usuarias.

## Supuestos y dependencias

- «Superadministradora» es una etiqueta de rol propuesta con alcance transversal de negocio por decisión del tesista; el tesista designará la primera durante la instalación con autorización registrada de la presidenta. La cantidad de titulares posteriores y la delegación requieren validación.
- La interfaz común no implica una app `admin` que posea datos de otros dominios ni un CRUD genérico.
- Cada módulo futuro tendrá que identificar qué catálogos/fórmulas permite administrar y exponer su operación con contrato explícito.
- No se habilita configuración hasta aprobar la fórmula/valores de negocio por la persona que la organización defina.
- La app contiene `accounts`; los módulos de negocio y sus operaciones administrativas no deben presumirse implementados por el estado actual del repositorio.
- SPEC-001 sigue confirmada: 3 fallos del mismo identificador normalizado en 3 minutos, bloqueo de 3 minutos y vencimiento tras 30 minutos de inactividad. Cambiar umbral/bloqueo exige nueva revisión validada de SPEC-001.
- Propuesta de rango, no requisito ni estándar: umbral de 3–10 intentos dentro de la ventana de observación actual de 3 minutos y bloqueo de 3–15 minutos; el valor actual de inicio seguiría 3/3. La recomendación requiere validar riesgo de denegación de servicio y recuperación.
- La implementación local observada de `LoginThrottle` guarda una huella HMAC y estado temporal, no un historial de eventos con nombre de usuaria. El historial detallado por cuenta no se supone disponible y requeriría decisiones propias de privacidad y retención.
- NIST SP 800-63B-4 fija un límite máximo de 100 intentos en el contexto de autenticadores descrito y permite límites inferiores; no determina el rango de este proyecto. OWASP señala riesgo de denegación de servicio por bloqueo de cuentas. Fuentes: [NIST SP 800-63B-4, §3.2.2](https://pages.nist.gov/800-63-4/sp800-63b.html) y [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).

## Preguntas pendientes — no resueltas por esta propuesta

| ID | Pregunta | Responsable de validar | Consecuencia |
|---|---|---|---|
| P-SUP-01 | El tesista decidió que la Superadministradora ejecuta todas las funciones ordinarias y edita registros, valores y opciones publicadas por cada módulo. ¿Qué datos sensibles y finalidades requieren restricciones adicionales según la organización? | Presidenta, organización y tesista | Aplicar privacidad aprobada por categoría; no limitar por defecto las acciones ordinarias del rol |
| P-SUP-02 | El tesista designa la primera Superadministradora durante la instalación con autorización de la presidenta. ¿Cómo se documenta esa autorización y quién puede delegar, revocar o transferir autoridad después? | Presidenta y tesista | Documentar autorización antes del alta inicial; no habilitar delegación ni transferencia sin regla |
| P-SUP-03 | ¿La entrega o transferencia de autoridad requiere dos personas, segunda aprobación o alguna evidencia formal? | Presidenta y tesista | No habilitar delegación sin regla |
| P-SUP-04 | ¿Qué límites mínimos/máximos se validan para intentos fallidos y minutos de bloqueo? ¿Se confirma la ventana de observación de 3 minutos? | Tesista y presidenta; revisar seguridad | SPEC-001 permanece con parámetros actuales hasta actualización aprobada |
| P-SUP-05 | El tesista decidió cerrar de inmediato todas las sesiones abiertas al desactivar una cuenta o revocar su acceso administrativo. ¿Cómo se refleja el cierre en un dispositivo PWA sin conexión y cómo se impide reutilizar su estado privado? | Tesista y responsable técnico | Probar cierre en sesiones en línea; definir manejo del estado sin conexión antes de habilitar administración PWA |
| P-SUP-06 | ¿Qué dato de intentos por cuenta se puede consultar: solo contador de ventana y bloqueo actual o también historial? ¿Por cuánto tiempo y quién lo ve? | Tesista, presidenta y responsable de privacidad | Modelo, minimización y retención; el diseño actual no ofrece historial completo |
| P-SUP-07 | ¿Qué catálogos/parámetros declara cada módulo administrables y quién los aprueba? | Responsable de cada módulo y organización | Especificación por módulo; no crear configurador genérico |
| P-SUP-08 | Para cada fórmula, ¿quién valida variables, unidades, precisión, redondeo, rangos, ejemplos de prueba y fecha de vigencia? | Responsable del módulo y persona designada por la organización | No activar cálculo nuevo sin regla acordada |
| P-SUP-09 | ¿Qué recorrido de recuperación/restablecimiento de cuenta se autoriza (canal, identidad, expiración, un solo uso, revocación y auditoría)? | Tesista y presidenta | Se excluye recuperación de esta propuesta hasta aprobación |
| P-SUP-10 | ¿Qué datos personales o secretos deben quedar excluidos incluso del panel y con qué finalidad se consultan los demás? | Presidenta y responsables de datos | Mantener acceso transversal a vistas publicadas, con excepciones sensibles validadas |
| P-SUP-11 | ¿Qué autorización y evidencia requiere una corrección financiera, de asistencia, pesaje, inventario u otro dato con historia? | Responsable del módulo y organización | Definir rectificación, efectos derivados y revisión |
| P-SUP-12 | ¿Cuál es la prioridad de este incremento respecto a `SB-S2-02`/`SB-S2-03` y qué porción cabe en S2? | Tesista | La ubicación S2 y la estructura para S3-S5 están decididas; el compromiso concreto se limita por capacidad y criterios validados |

## Trazabilidad académica

| Elemento | Enlace/ID |
|---|---|
| Objetivos específicos | Pendiente de cotejar en el anteproyecto vigente |
| Sprint | S2 para acceso, cuentas y estructura de permisos; operaciones de negocio en S3-S5. Fechas intermedias propuestas en la hoja de ruta. |
| Requisito | `RF-ACC-005` candidato; CAT-REQ-001 v1.3 propuesta |
| Historias | HU-ACC-002/003 refinadas y HU-ACC-005–009 candidatas |
| Arquitectura | Constitución 2.0.0, ADR-0006 y ARQUITECTURA-OBJETIVO; no se propone excepción |
| Casos de prueba | Pendientes; se deriva matriz de permisos y criterios cuando los requisitos se validen |
| Evidencia | Pendiente; validación organizacional no recibida |
| ISO/IEC 25010:2023 | Candidata: seguridad, confiabilidad, interacción y completitud funcional; evaluación pendiente |

## Registro de validación

| Fecha | Participantes/rol | Decisión | Cambios | Evidencia |
|---|---|---|---|---|
| 2026-10-27 | Tesista solicita preparar borradores; solicitud de la presidenta reportada por el tesista | `proposed`; el tesista precisa que el superpanel no debe editar universalmente cualquier dato | Se separa alcance del panel de privilegio universal; validación directa pendiente | Esta propuesta; no constituye evidencia de validación de la presidenta |
| 2026-10-27 | Tesista | Conservar mensajes específicos aprobados de SPEC-001; designar durante instalación la primera Superadministradora con autorización registrada de la presidenta | Se acota el arranque y se descarta el cambio de mensajes propuesto, sin aprobar RF-ACC-005 completo | Decisión explícita del tesista en esta conversación; constancia de autorización presidencial pendiente |
| 2026-10-27 | Tesista | Cerrar de inmediato todas las sesiones abiertas al desactivar una cuenta o revocar su acceso administrativo | Se añade criterio de invalidación de sesión y prueba con dos sesiones | Decisión explícita del tesista en esta conversación |
| 2026-10-27 | Tesista | La Superadministradora realiza todas las acciones de una usuaria normal en todos los módulos y además edita registros, valores de campos existentes y opciones configurables desde el panel | Sustituye la restricción anterior de alcance transversal; cada módulo conserva validaciones, historia y escrituras; no se crean campos físicos desde el panel | Decisión explícita del tesista en esta conversación; detalle por módulo pendiente |

## Historial de cambios

| Versión | Fecha | Estado | Cambio |
|---|---|---|---|
| 0.1 | 2026-10-27 | `proposed` | Primera especificación exploratoria con matriz actor→acción→recurso→resultado; no sustituye SPEC-001 ni autoriza implementación. |
| 0.2 | 2026-10-27 | `proposed` | Se separan criterios verificables de S2 y trabajo de módulos S3-S5; se actualiza la ubicación decidida por el tesista sin aprobar RF-ACC-005 ni resolver decisiones pendientes. |
| 0.3 | 2026-10-27 | `proposed` | Se incorpora autoridad transversal de Superadministradora sobre acciones ordinarias y configuraciones publicadas por todos los módulos; se conserva la separación S2/S3-S5 y el esquema fuera del panel. |
