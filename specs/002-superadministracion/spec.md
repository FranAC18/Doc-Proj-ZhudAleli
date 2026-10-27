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
sprint: "Sin asignación; posterior al trabajo de acceso activo solo como propuesta"
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
- **Entrada del usuario**: preparar una propuesta para un panel administrativo sin autoridad universal de edición.

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
- **Problema reportado**: la presidenta pidió, según relata el tesista, una autoridad para administrar cuentas, módulos y datos del sistema. El alcance de «cualquier dato» y la regla de delegación no constan validados.
- **Precisión del tesista**: se requiere un superpanel administrativo, pero la Superadministradora no debe tener una autoridad universal que le permita cambiar cualquier dato.
- **Valor esperado**: gestionar cuentas, accesos por módulo y configuraciones expuestas desde un panel unificado, y resolver correcciones dentro de los procedimientos responsables, con permisos verificables y conservación de historia.
- **Incluye como propuesta**: alta/baja lógica o activación/desactivación de cuentas; asignación y retiro de módulos; concesión/revocación de autoridad a otras personas con reglas por definir; consulta limitada de intentos recientes; parámetros de bloqueo tras actualizar SPEC-001; configuraciones que los módulos declaren administrables; fórmulas seguras con prueba, versión y vigencia; consultas y correcciones autorizadas mediante operaciones explícitas del módulo propietario.
- **No incluye**: permiso global implícito para leer o modificar todo; CRUD genérico; consultas o escrituras directas a la base de datos; alterar o borrar auditoría; sobrescribir movimientos históricos; editar o mostrar contraseñas, tokens o secretos; código arbitrario como fórmula; recalcular el pasado al cambiar una fórmula; recuperación de cuentas todavía no diseñada; incorporar funcionalidad a un sprint.
- **Incremento utilizable**: pendiente. No se identifica un módulo completo implementado para este alcance; `App-zhudaleli` tiene el acceso propio de SPEC-001 en una rama sin integración confirmada.
- **Capacidades anteriores afectadas**: SPEC-001 conserva su alcance de acceso propio, comportamiento de login y vencimiento de sesión. No se altera su regla vigente por esta propuesta.

## Escenarios candidatos y verificación

Los siguientes escenarios son propuestas de verificación, no criterios validados. Cada operación debe tener una prueba permitida y otra denegada. La corrección no elimina el dato original cuando pertenece a una historia de eventos.

### HU-01 — Asignar un módulo a otra cuenta

**Como** Superadministradora con autoridad vigente, **quiero** habilitar un módulo concreto para otra cuenta, **para** limitarla a las funciones que necesita.

**Prueba independiente**: asignar un módulo disponible mediante la operación del propietario, confirmar el nuevo acceso, intentar la misma operación sin permiso y comprobar que la segunda solicitud no cambia datos.

**Criterios candidatos**:

1. **Dado** un actor y un módulo permitidos, **cuando** solicita la asignación, **entonces** el backend valida alcance y estado, ejecuta la operación pública y deja una auditoría del cambio.
2. **Dado** un actor sin permiso, **cuando** envía la misma solicitud directamente, **entonces** el backend la deniega sin mutación.
3. **Dada** una asignación revocada, **cuando** se realiza una operación posterior, **entonces** se comprueba el permiso vigente; el tratamiento de sesiones abiertas queda pendiente.

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
4. La revocación de permiso impide cambios posteriores al revalidarse en backend; la invalidación de una sesión existente sigue pendiente de decisión.

### HU-04 — Probar y poner en vigencia una configuración del módulo

**Como** administradora autorizada por el módulo propietario, **quiero** probar una fórmula o cambio de catálogo antes de activarlo, **para** revisar el efecto sin modificar resultados históricos.

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

1. El acceso a cada categoría y campo se verifica en backend; el término «cualquier dato» no concede lectura automática.
2. El módulo ejecuta sus validaciones e invariantes y es responsable de sus escrituras y migraciones.
3. Una corrección histórica crea un evento/rectificación relacionado con el original; no reemplaza ni borra el evento base.
4. Toda modificación registra actor, fecha, resultado, motivo y campos cambiados, dentro de la misma transacción que el cambio cuando aplique.
5. Las acciones sensibles de varias entidades confirman juntas o no dejan cambios parciales.

## Requisitos (Requirements)

### Requisito funcional candidato

- **RF-ACC-005**: El sistema permite administrar cuentas, accesos por módulo y configuraciones administrativas que cada módulo exponga, y consultar o corregir datos únicamente mediante acciones y permisos explícitos; cada operación verifica autorización en backend y conserva una auditoría no editable.
  - **Fuente**: solicitud reportada por el tesista el 2026-10-27, citando a la presidenta; validación directa pendiente.
  - **Actor/permiso**: rol Superadministradora propuesto, con asignaciones puntuales por actor, operación, recurso y módulo; el origen de la autoridad todavía no está definido.
  - **Criterios candidatos**: los escenarios HU-01 a HU-05 y la matriz de permisos de esta spec.

### Requisitos no funcionales y reglas transversales

- **RNF-SEC-001** (confirmado en CAT-REQ-001 v1.2): aplicar autorización en backend y proteger datos y operaciones. Los controles visibles en UI no son una regla de autorización.
- **RNF-AUD-001** (confirmado en CAT-REQ-001 v1.2): conservar la auditoría conforme al requisito canónico; esta propuesta añade los campos de cambio reportados como candidatos, sujetos a confirmar retención y visibilidad.
- **RNF-PRV-001** (confirmado en CAT-REQ-001 v1.2): minimizar y restringir el acceso a información personal. No se infiere visibilidad completa de expedientes para la Superadministradora.
- **RN-RBAC-001 (candidata)**: `is_staff` y `is_superuser` son atributos técnicos de Django; no otorgan autoridad organizacional.
- **RN-MOD-001 (candidata)**: cada módulo conserva escrituras, reglas, validaciones, invariantes y migraciones; el panel coordina operaciones administrativas públicas, sin modificar tablas de forma genérica.
- **RN-AUD-001 (candidata)**: auditoría de cambios no editable desde la aplicación. Las rectificaciones son eventos nuevos relacionados, no sobrescrituras.
- **RN-CFG-001 (candidata)**: fórmulas/catálogos versionados y con vigencia; cualquier fórmula se valida, prueba y activa mediante el módulo responsable; los resultados históricos conservan la versión aplicada.
- **RN-SEC-002 (candidata)**: no editar ni devolver contraseñas existentes, tokens, secretos de despliegue o contenido de auditoría como si fueran datos ordinarios.
- **RN-PWA-001 (candidata, alineada a RF-PWA-001/002/003 confirmados)**: páginas administrativas y datos privados quedan fuera de cachés PWA y no se ofrecen sin sesión y permiso vigentes.

### Matriz actor → acción → recurso → resultado

Todos los resultados siguientes son candidatos hasta que la presidenta y el tesista validen reglas y alcance. «Permitido» describe solo el caso limitado propuesto; la matriz no define ni activa permisos en el producto.

| Actor | Acción | Recurso | Resultado candidato | Denegación / pendiente |
|---|---|---|---|---|
| Superadministradora con permiso vigente | Asignar o retirar acceso | Cuenta y módulo habilitado | Operación pública de acceso valida el cambio y lo audita | Sin permiso, cuenta/módulo no disponible o solicitud malformada: denegar en backend |
| Superadministradora con permiso vigente | Activar/desactivar cuenta | Estado de cuenta | Cambio de estado con historial conservado | Efecto en sesiones abiertas pendiente; no borrar registros asociados |
| Delegante explícitamente autorizado | Conceder/revocar autoridad | Autoridad de otra cuenta | Cambio acotado, con vigencia y auditoría | Asignador inicial, transferencia y doble aprobación pendientes; autoelevación denegada |
| Usuaria interna con permiso específico | Consultar datos de negocio | Categoría, campos y módulo permitidos | Lectura limitada a su permiso y propósito | Alcance de «cualquier dato», datos personales y exportación pendientes; no conceder lectura global |
| Usuaria interna autorizada | Corregir registro | Recurso expuesto por su módulo | El propietario valida y añade rectificación; conserva original | Sin autorización, fuera del flujo del módulo o borrado del histórico: denegar |
| Superadministradora autorizada por el propietario | Editar catálogo | Catálogo que el módulo declara configurable | Operación propia del módulo crea versión/historial | No se permite CRUD genérico ni afectar otros módulos |
| Superadministradora autorizada por el propietario | Probar/activar fórmula | Fórmula/cálculo de ese módulo | Expresión segura validada, vista previa, versión y fecha de vigencia | Código arbitrario o falta de aprobación: denegar; recalcular historia: excluido |
| Administradora de acceso con permiso de seguridad | Consultar intentos recientes | Estado temporal de bloqueo asociado a cuenta | Muestra conteo/estado actualmente retenido y minimizado | Historial completo, retención, identidad visible y búsqueda por cuenta pendientes |
| Administradora de acceso con permiso de seguridad | Cambiar umbral y duración | Política de login en SPEC-001 | Solo después de aprobación, rango y versión efectiva | Antes de revisar/validar SPEC-001: conservar 3 fallos/3 minutos/bloqueo 3 minutos |
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

- Un panel administrativo unificado muestra únicamente acciones asignadas; el selector de módulo delimita la operación y no representa acceso universal.
- Cada acción confirma el recurso y el resultado esperado; las correcciones muestran el dato original y la nueva rectificación, con motivo obligatorio pendiente de validar.
- Deben existir estados vacío, cargando, guardado, error recuperable, denegación, permiso revocado y conflicto de vigencia.
- La búsqueda no revela existencia de cuentas a personas no autorizadas. La visibilidad de datos personales requiere una regla por categoría.
- Debe funcionar desde móvil y escritorio, con teclado, foco visible, mensajes textuales y contraste accesible según RNF-UX vigentes.
- El panel privado no entra al caché offline; no conserva datos privados en el dispositivo compartido.

## Criterios de éxito candidatos

- **SC-001**: cada operación administrativa documentada tiene un caso permitido y un caso denegado que verifica autorización en backend antes de mutar.
- **SC-002**: una corrección aprobada permite comparar el original y su rectificación y reconstruir el actor, fecha, resultado, motivo y campos cambiados.
- **SC-003**: una fórmula no puede activarse si falla la validación o prueba; la operación histórica sigue usando la versión original.
- **SC-004**: un permiso revocado no permite nuevas acciones protegidas una vez consultada la autoridad vigente; los requisitos de invalidación de sesión se definen antes de activar el panel.
- **SC-005**: una usuaria representativa puede asignar un módulo, entender una denegación y corregir un registro autorizado con teclado y en pantalla móvil durante pruebas con usuarias.

## Supuestos y dependencias

- «Superadministradora» es una etiqueta de rol propuesta; la presidenta, el tesista y la organización deben definir si existe una sola persona o varias y su ámbito exacto.
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
| P-SUP-01 | ¿«Cualquier dato» significa lectura, altas, modificaciones, bajas, eliminación, corrección histórica, expedientes personales, cuentas o parámetros? ¿Qué campos y finalidades cubre cada permiso? | Presidenta, organización y tesista | No habilitar consulta amplia ni edición global |
| P-SUP-02 | ¿Quién crea la primera Superadministradora y quién puede asignar, delegar, revocar o transferir autoridad cuando cambie la presidencia? | Presidenta y tesista | No implementar la emisión inicial de autoridad |
| P-SUP-03 | ¿La entrega o transferencia de autoridad requiere dos personas, segunda aprobación o alguna evidencia formal? | Presidenta y tesista | No habilitar delegación sin regla |
| P-SUP-04 | ¿Qué límites mínimos/máximos se validan para intentos fallidos y minutos de bloqueo? ¿Se confirma la ventana de observación de 3 minutos? | Tesista y presidenta; revisar seguridad | SPEC-001 permanece con parámetros actuales hasta actualización aprobada |
| P-SUP-05 | ¿Una revocación termina todas las sesiones activas, solo bloquea próximas operaciones o requiere volver a autenticar? ¿Cómo se propaga a PWA? | Tesista y presidenta | Definir consistencia temporal antes de operar |
| P-SUP-06 | ¿Qué dato de intentos por cuenta se puede consultar: solo contador de ventana y bloqueo actual o también historial? ¿Por cuánto tiempo y quién lo ve? | Tesista, presidenta y responsable de privacidad | Modelo, minimización y retención; el diseño actual no ofrece historial completo |
| P-SUP-07 | ¿Qué catálogos/parámetros declara cada módulo administrables y quién los aprueba? | Responsable de cada módulo y organización | Especificación por módulo; no crear configurador genérico |
| P-SUP-08 | Para cada fórmula, ¿quién valida variables, unidades, precisión, redondeo, rangos, ejemplos de prueba y fecha de vigencia? | Responsable del módulo y persona designada por la organización | No activar cálculo nuevo sin regla acordada |
| P-SUP-09 | ¿Qué recorrido de recuperación/restablecimiento de cuenta se autoriza (canal, identidad, expiración, un solo uso, revocación y auditoría)? | Tesista y presidenta | Se excluye recuperación de esta propuesta hasta aprobación |
| P-SUP-10 | ¿Puede la Superadministradora consultar todos los datos personales o solo los necesarios para una acción? ¿Qué campos son sensibles? | Presidenta y responsables de datos | Aplicar permisos por categoría/campo y minimización |
| P-SUP-11 | ¿Qué autorización y evidencia requiere una corrección financiera, de asistencia, pesaje, inventario u otro dato con historia? | Responsable del módulo y organización | Definir rectificación, efectos derivados y revisión |
| P-SUP-12 | ¿Cuál es la prioridad de este incremento respecto al plan vigente de S1–S6 y a `SB-S2-02`/`SB-S2-03`? | Tesista | No asignar ni iniciar sprint hasta decisión |

## Trazabilidad académica

| Elemento | Enlace/ID |
|---|---|
| Objetivos específicos | Pendiente de cotejar en el anteproyecto vigente |
| Sprint | Ninguno asignado; decisión pendiente |
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

## Historial de cambios

| Versión | Fecha | Estado | Cambio |
|---|---|---|---|
| 0.1 | 2026-10-27 | `proposed` | Primera especificación exploratoria con matriz actor→acción→recurso→resultado; no sustituye SPEC-001 ni autoriza implementación. |
