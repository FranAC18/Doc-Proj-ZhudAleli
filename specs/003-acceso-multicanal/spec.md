---
id: SPEC-003
title: Acceso multicanal y recuperación de cuentas internas
status: confirmed
plan_status: approved-by-tesista
implementation_status: pending
date: 2026-10-28
sprint: S2
module: accounts
approved_by: Tesista
validation_source: EVID-ACC-2026-10-28
organization_validation: pending
academic_review: pending
---

# Acceso multicanal y recuperación

## Decisión del tesista — 2026-10-28

El tesista aceptó el plan de acceso por passkeys y código por correo, con WhatsApp configurable, tras solicitar expresamente «con biometria y con correo, wpp se implementa». Su respuesta fue: «documentalo, me convence, recuerda cada cambio siempre documentar en requisitos, backlog, pilas, historias y http://127.0.0.1:55478/ que es el gestor de tesis agil».

La aceptación confirma este alcance y el plan por incrementos. No constituye validación de campo, revisión académica, implementación, autorización de gasto ni publicación. Telegram queda fuera del incremento elegido. El acceso usuario/contraseña existente se conserva como respaldo durante la transición.


## Fuente y relación con SPEC-001

La evidencia es [[../../docs/evidence/requirements/2026-10-28-aceptacion-acceso-multicanal|EVID-ACC-2026-10-28]]. Los requisitos RF-ACC-006 a RF-ACC-009 están confirmados por el tesista; su implementación y validación con usuarias están pendientes. SPEC-001 conserva la entrega y decisiones históricas del acceso existente. Esta ampliación gobierna los métodos alternativos y la recuperación. La cuenta activa, permisos backend, logout POST con CSRF, 30 minutos de inactividad, exclusión de caché privada y cambio inicial obligatorio se conservan para todos los métodos.

El objetivo nuevo usa mensajes públicos genéricos y límites por cuenta e IP. Reemplaza la excepción anterior de mensajes «Usuario incorrecto»/«Contraseña incorrecta» al ejecutar la transición; no describe el estado actual del código. El login por OTP es una alternativa de ingreso, no un segundo factor obligatorio en cada acceso. El correo no se convierte automáticamente en identificador de la contraseña de respaldo.

## Requisitos y criterios

### RF-ACC-006 — Ingresar mediante código por correo

- **Actor:** usuaria interna con cuenta activa y correo verificado.
- **Regla:** Una usuaria con cuenta interna activa puede iniciar sesión con un código enviado a su correo previamente asociado y verificado.
- **Historia:** `HU-ACC-010`; **estado:** `confirmed` por el tesista, implementación pendiente.

1. **CA-ACC-006-01:** La solicitud pública responde de forma genérica exista o no la cuenta; solo una cuenta activa y un correo previamente verificado reciben un código utilizable.
2. **CA-ACC-006-02:** El código tiene seis dígitos, vence a los cinco minutos, admite como máximo cinco intentos de validación y solo puede consumirse una vez, incluso ante solicitudes concurrentes.
3. **CA-ACC-006-03:** Hay al menos 60 segundos entre reenvíos, un máximo por hora definido antes de activar el canal y límites por cuenta y origen sin revelar la existencia de cuentas.
4. **CA-ACC-006-04:** El código se genera con CSPRNG y se almacena protegido mediante hash con sal o HMAC con secreto fuera de la base de datos; se verifica en tiempo constante y no aparece en logs.
5. **CA-ACC-006-05:** Una validación correcta abre una sesión Django con las mismas restricciones, vencimiento y permisos del acceso existente; una cuenta inactiva nunca obtiene sesión.

### RF-ACC-007 — Registrar y utilizar passkeys

- **Actor:** usuaria interna con cuenta activa y acceso recientemente verificado.
- **Regla:** Una usuaria activa puede registrar, utilizar, consultar y revocar passkeys mediante WebAuthn, con verificación local del dispositivo por biometría o PIN.
- **Historia:** `HU-ACC-011`; **estado:** `confirmed` por el tesista, implementación pendiente.

1. **CA-ACC-007-01:** El registro exige sesión de la cuenta y una verificación reciente mediante un canal previamente asociado; escribir un correo o conocer solo la contraseña no vincula una passkey.
2. **CA-ACC-007-02:** El servidor valida desafío de un solo uso, expiración, tipo de operación, origen, RP ID, firma y verificación de usuario; no acepta una credencial de otra cuenta.
3. **CA-ACC-007-03:** Se almacenan identificador de credencial, clave pública y metadatos necesarios; no se reciben ni almacenan huellas, imágenes faciales ni claves privadas.
4. **CA-ACC-007-04:** La usuaria puede mantener varias passkeys y revocarlas tras reautenticarse; se notifica el registro y la revocación por un canal verificado.
5. **CA-ACC-007-05:** El dispositivo elige huella, rostro o PIN; la interfaz detecta compatibilidad y ofrece correo como alternativa. Se usa HTTPS y dominio estable; localhost sirve para desarrollo.
6. **CA-ACC-007-06:** Una passkey revocada, una cuenta inactiva o un desafío reutilizado no permiten acceso; los permisos y el cambio inicial pendiente se aplican igualmente.

### RF-ACC-008 — Ingresar mediante código por WhatsApp

- **Actor:** usuaria interna con cuenta activa y teléfono verificado.
- **Regla:** Una usuaria activa puede solicitar un código a su teléfono E.164 previamente asociado y verificado, mediante un proveedor oficial configurable.
- **Historia:** `HU-ACC-012`; **estado:** `confirmed` por el tesista, implementación pendiente.

1. **CA-ACC-008-01:** El teléfono está asociado y verificado con consentimiento antes de usarlo para acceder; un número escrito en el formulario no modifica la cuenta ni crea una usuaria.
2. **CA-ACC-008-02:** El OTP aplica los mismos controles de generación, almacenamiento, expiración de cinco minutos, cinco intentos, uso único, cooldown y límites de RF-ACC-006.
3. **CA-ACC-008-03:** Existe un adaptador para Meta Cloud API y un mock aislado de desarrollo y pruebas; los secretos y la selección del proveedor se configuran por entorno.
4. **CA-ACC-008-04:** El modo mock no entrega mensajes reales ni se habilita como mecanismo de autenticación de producción; la interfaz no ofrece un canal real sin configurar.
5. **CA-ACC-008-05:** La activación real exige cuenta y número emisor, plantilla de autenticación aprobada, consentimiento, comprobación del costo y prueba de entrega; desarrollar el adaptador no acredita entrega real.
6. **CA-ACC-008-06:** Las respuestas públicas son genéricas; se distinguen solicitud aceptada por el proveedor, entrega confirmada y fallo, sin registrar códigos ni datos de contacto completos.

### RF-ACC-009 — Recuperar el acceso y proteger la cuenta

- **Actor:** usuaria interna que perdió el dispositivo o sus credenciales.
- **Regla:** Una usuaria activa puede recuperar acceso mediante un canal previamente verificado, revocar credenciales perdidas y completar el cambio inicial antes de acceder a funciones privadas.
- **Historia:** `HU-ACC-013`; **estado:** `confirmed` por el tesista, implementación pendiente.

1. **CA-ACC-009-01:** El correo verificado permite recuperar acceso al perder el dispositivo y revocar passkeys previas tras reautenticación; no se cambia el destino de recuperación desde una solicitud pública.
2. **CA-ACC-009-02:** La recuperación de usuario envía su nombre solo al correo asociado y la respuesta pública permanece genérica; recuperar acceso no crea cuentas ni amplía permisos.
3. **CA-ACC-009-03:** Para la contraseña del acceso de respaldo se usa un enlace con token aleatorio almacenado como hash, válido durante 20 minutos y consumido una sola vez; se valida la política de contraseñas existente.
4. **CA-ACC-009-04:** Al restablecer la contraseña se invalidan los tokens pendientes, se cierran las sesiones activas y se envía un aviso; las passkeys perdidas se revocan de forma explícita.
5. **CA-ACC-009-05:** Si must_change_password está pendiente, todos los métodos dejan acceso restringido: solicitar y validar código por canal disponible, definir nueva contraseña y recién entonces habilitar funciones privadas.
6. **CA-ACC-009-06:** La ausencia de canales verificados no habilita una recuperación insegura: el procedimiento asistido requiere definir responsable y comprobación de identidad antes de implementarlo.

## Arquitectura y datos afectados

`accounts` posee contactos verificados, desafíos de OTP/recuperación y credenciales públicas WebAuthn. Se reutilizan las sesiones Django y la cuenta personalizada. No se añade JWT, microservicio, cola ni biblioteca de criptografía propia. Los adaptadores de envío se crean dentro del módulo cuando exista esa responsabilidad. Las pantallas pertenecen a `apps/accounts/frontend/accounts/<pantalla>/`; se aplica la convención de código legible y descubrimiento de recursos existente.

Las migraciones deben preservar cuentas y credenciales actuales. Antes de imponer unicidad al correo o teléfono se identifican vacíos, duplicados y destinos compartidos, sin fusionar cuentas ni inventar verificaciones. Registrar o cambiar un contacto exige acreditar control de la cuenta y del nuevo destino. No hay alta pública ni vinculación automática por coincidencia de correo.

Los desafíos se ligan a cuenta, propósito y flujo pendiente; OTP de ingreso, verificación de contacto, primer cambio y recuperación no son intercambiables. Su consumo y la apertura de sesión se coordinan para impedir reuso concurrente. Se mantienen los validadores de contraseñas actuales; la app usa PBKDF2 de Django y no se declara migrada a Argon2 por esta aceptación.

## Plan por incrementos aprobado

| Fase | Tarea | Dependencia | Resultado verificable |
|---|---|---|---|
| 1 | `SB-S2-05` — Preparar identidad, desafíos y seguridad común | SB-S2-02 | Migraciones compatibles; asociación/verificación de contactos y resolución de duplicados; consumo atómico; límites por cuenta e IP; bloqueo de funciones privadas con cambio inicial pendiente; auditoría sin secretos. |
| 2 | `SB-S2-06` — Implementar y verificar ingreso por correo | SB-S2-05 | Ingreso completo con mock y pruebas de OTP, enumeración, expiración, reuso, intentos y límites; configuración SMTP local y prueba real de envío registrada por separado. |
| 3 | `SB-S2-07` — Implementar registro, ingreso y revocación de passkeys | SB-S2-06 | Registro con verificación reciente; acceso y revocación; pruebas criptográficas negativas; comprobación en teléfono y computador con dominio HTTPS estable. |
| 4 | `SB-S2-08` — Implementar WhatsApp configurable con Meta y mock | SB-S2-05 | Adaptador de Meta, teléfono verificado y flujo completo con mock; timeouts, fallos y reintentos acotados. Registrar por separado entrega real, plantilla aprobada y costo antes de activar. |
| 5 | `SB-S2-09` — Completar recuperación y verificar el acceso multicanal | SB-S2-06, SB-S2-07, SB-S2-08 | Recuperación de usuario y contraseña; pérdida de dispositivo; cambio inicial con verificación; cierre de sesiones; avisos; regresión de permisos y caché; revisión móvil, teclado y foco. Actualizar RF, HU, HT, pila, backlog y gestor con resultados reales. |

La fase WhatsApp puede avanzar tras la seguridad común sin esperar la prueba en dispositivos de passkeys. El orden correo → passkeys prioriza un canal de recuperación antes de vincular dispositivos. S2 es el destino aceptado; no se fijan puntos, responsables ni nuevas fechas de terminación sin estimación. El avance previo de SB-S2-02 y de otras tareas se conserva.

## Verificación y condiciones externas

- Automatizadas: OTP vencido/reutilizado, intentos y reenvíos, límites por cuenta/origen, respuestas genéricas, cuenta inactiva, consumo concurrente y todas las guardas con cambio pendiente.
- WebAuthn: desafío vencido o ajeno, origen y RP ID erróneos, firma inválida, ausencia de verificación de usuario, credencial revocada y vinculación sin autorización; recorridos válidos con biblioteca mantenida.
- Recuperación: token de 20 minutos, uso único, validadores de contraseña, invalidación de tokens/sesiones y avisos; pérdida de dispositivo y revocación explícita.
- Integración: PostgreSQL, migraciones, controles Django y Ruff, regresión de entrada/salida y PWA sin caché de formularios, OTP, sesiones o páginas privadas.
- Manuales: teléfono y computador compatibles; HTTPS y dominio estable para passkeys reales; correo entregado; WhatsApp entregado cuando se active; teclado, foco, errores y móvil.

La aceptación de código con mock no acredita entrega SMTP o WhatsApp. Los costos de Meta, número y alojamiento se comprueban antes de activar el canal real. El mock no registra ni muestra OTP en producción. Los dispositivos compartidos exigen registro voluntario y advertencia comprensible; el diseño no promete biometría exclusiva ni funcionamiento del ingreso sin conexión.

## Detalles que siguen abiertos

Máximo de reenvíos por hora; política concreta de direcciones compartidas/duplicadas; biblioteca WebAuthn y versiones; dominio definitivo y equipos de prueba; cuenta/plantilla/costo de Meta; credencial SMTP local. La recuperación asistida sin canales verificados requiere decidir responsable y verificación de identidad; no se implementa por inferencia. Estos puntos no detienen la documentación ni las porciones independientes.

## Sincronización obligatoria

Cada cambio relevante de alcance, criterio, prioridad o estado se registra en requisitos, historias HU/HT afectadas, pila de producto, sprint backlog y gestor local `http://127.0.0.1:55478/`, además de evidencia y estado operativo. Se conserva la versión anterior y se informa si un destino queda pendiente. La sincronización local no autoriza publicación, Git ni gasto.
