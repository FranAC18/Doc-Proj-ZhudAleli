---
id: SPEC-001
title: Acceso de usuarias internas
type: feature-spec
status: confirmed
created: 2026-07-25
source:
  - CAT-REQ-001
  - ACT-REQ-001
  - D-011
sprint: S1
module: acceso
actors:
  - Directiva
  - Socia operaria
validated_by:
  - Tesista
related:
  - "[[../../docs/requirements/CAT-REQ-001]]"
  - "[[../../docs/evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0]]"
  - "[[../../docs/evidence/fase-i/2026-07-25-confirmacion-spec-001]]"
  - "[[../../docs/00-inicio/01-decisiones-pendientes]]"
  - "[[../../docs/decisions/ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[../../docs/traceability/MATRIZ-TRAZABILIDAD]]"
---

# Especificación: Acceso de usuarias internas

- **Rama propuesta**: `codex/001-acceso-usuarias-internas`
- **Entrada del usuario**: preparar la especificación 001 a partir de `RF-ACC-001`, la
  opción A aprobada y las aclaraciones registradas en ACT-REQ-001.

## Control de validación

| Elemento | Valor |
|---|---|
| Estado | `confirmed`; habilita planificación, no implementación |
| Fuente primaria | [[../../docs/requirements/CAT-REQ-001\|CAT-REQ-001 v1.0]] y [[../../docs/evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0\|ACT-REQ-001]] |
| Preparó | Codex, bajo instrucciones del tesista |
| Debe validar | Tesista; representantes de las usuarias internas en la validación de recorridos |
| Fecha de validación | 2026-07-25 por el tesista |
| Evidencia | [[../../docs/evidence/fase-i/2026-07-25-confirmacion-spec-001\|Confirmación de SPEC-001 y ADR-0003]] |

## Problema, valor y alcance

- **Actor afectado**: integrantes de la Directiva y socias operarias que necesitan ingresar
  a la parte privada del sistema.
- **Problema observable**: todavía no existe un acceso privado que permita reconocer a una
  usuaria interna, proteger la información organizacional y terminar una sesión de forma
  segura.
- **Valor esperado**: una usuaria con cuenta activa puede identificarse, entrar a un espacio
  privado comprensible, cambiar su contraseña y cerrar la sesión; una persona no autenticada,
  una cuenta inactiva o credenciales incorrectas no obtienen acceso ni información sensible.
- **Incluye**: acceso con nombre de usuario y contraseña, cierre de sesión, protección de
  contenido privado, rechazo no revelador de intentos inválidos, cambio de contraseña,
  primera cuenta y dashboard privado de bienvenida con opciones realmente disponibles.
- **No incluye**: administración de membresías (`RF-ACC-002`), matriz definitiva de cargos y
  operaciones (`RF-ACC-003`), actividades, pendientes o encargos (`RF-ACC-004`), recuperación
  de contraseña mediante canales externos, contenido público final ni operaciones de negocio.

## Escenarios de usuario y pruebas (User Scenarios & Testing)

### HU-01 — Iniciar y cerrar una sesión interna (P1)

**Como** usuaria interna con cuenta activa, **quiero** iniciar sesión con mi nombre de usuario
y contraseña y poder cerrarla, **para** entrar al espacio privado sin dejar mi acceso abierto
al terminar.

**Prueba independiente**: con una cuenta activa conocida, completar el acceso, observar el
dashboard de bienvenida, cerrar la sesión e intentar volver a una dirección privada.

**Criterios de aceptación**:

1. **CA-ACC-001-01 — Dado** un nombre de usuario y contraseña válidos para una cuenta activa, **cuando** la
   usuaria inicia sesión, **entonces** accede al dashboard privado de bienvenida.
2. **CA-ACC-001-05 — Dado** que la usuaria tiene una sesión activa, **cuando** elige cerrar sesión,
   **entonces** vuelve al acceso y cualquier intento posterior de abrir contenido privado le
   exige autenticarse nuevamente.
3. **CA-ACC-001-09 — Dado** que la usuaria ya inició sesión, **cuando** abre el dashboard,
   **entonces** ve una bienvenida y únicamente las opciones disponibles en esta porción.

### HU-02 — Proteger el acceso privado (P1)

**Como** organización, **quiero** que los intentos inválidos o no autorizados se rechacen sin
revelar información interna, **para** proteger las cuentas y los datos organizacionales.

**Prueba independiente**: intentar acceder con contraseña incorrecta, nombre de usuario
inexistente, cuenta inactiva y sin sesión, y comprobar que ninguna variante muestra contenido
privado ni permite distinguir qué dato de la cuenta existe.

**Criterios de aceptación**:

1. **CA-ACC-001-02 — Dado** un nombre de usuario inexistente o una contraseña incorrecta,
   **cuando** se intenta iniciar sesión, **entonces** se rechaza el acceso con un mismo
   mensaje comprensible que no confirma cuál dato fue incorrecto.
2. **CA-ACC-001-03 — Dado** un nombre de usuario correspondiente a una cuenta inactiva, **cuando** se intenta
   iniciar sesión, **entonces** se rechaza con el mismo nivel de información que un intento
   inválido y no se abre una sesión.
3. **CA-ACC-001-04 — Dado** que una persona no tiene una sesión activa, **cuando** solicita
   directamente una dirección privada, **entonces** no ve contenido interno y se le ofrece
   iniciar sesión.
4. **RNF-UX-002 — Dado** un error de acceso, **cuando** la usuaria corrige sus datos,
   **entonces** puede volver a intentar sin perder el nombre de usuario ya escrito ni recibir
   instrucciones técnicas.

### HU-03 — Cambiar la contraseña propia (P2)

**Como** usuaria interna autenticada, **quiero** cambiar mi contraseña, **para** mantener el
control de mi cuenta y reemplazar una credencial temporal.

**Prueba independiente**: iniciar sesión, presentar la contraseña actual y una contraseña
nueva válida, confirmar el cambio y comprobar que la anterior deja de permitir acceso.

**Criterios de aceptación**:

1. **CA-ACC-001-06 — Dado** que la usuaria está autenticada y conoce su contraseña actual,
   **cuando** registra y confirma una contraseña nueva válida, **entonces** recibe
   confirmación y la contraseña anterior deja de permitir nuevos accesos.
2. **CA-ACC-001-07 — Dado** que la contraseña actual es incorrecta o las nuevas no coinciden,
   **cuando** la usuaria intenta guardar el cambio, **entonces** la contraseña no cambia y el
   formulario indica cómo corregir el problema.
3. **CA-ACC-001-08 — Dado** que la primera cuenta utiliza una credencial temporal, **cuando**
   se produce su primer acceso, **entonces** debe cambiar la contraseña antes de poder
   utilizar el dashboard.
4. **CA-ACC-001-10 — Dado** que el recorrido está funcional y existe una representante
   designada por la Directiva, **cuando** se entrega la primera cuenta, **entonces** la
   credencial temporal se comunica presencialmente y no se registra en documentación,
   capturas ni mensajes.

### Excepciones y bordes

- Los nombres de usuario se comparan de forma consistente y no se crean cuentas duplicadas
  que solo difieran por mayúsculas o espacios accidentales.
- Un formulario enviado dos veces no debe crear dos sesiones ni aplicar dos cambios de
  contraseña.
- Una interrupción de conectividad muestra un resultado comprensible y permite reintentar sin
  asumir que el acceso o el cambio se completó.
- Volver atrás después de cerrar sesión no revela contenido privado almacenado por la
  navegación anterior.
- Si la sesión deja de ser válida mientras la usuaria está en una pantalla privada, se le
  solicita autenticarse de nuevo sin exponer información adicional.
- **CA-ACC-001-11**: después de 30 minutos sin actividad, la sesión deja de permitir acceso
  privado y solicita autenticación nuevamente.

## Requisitos (Requirements)

### Requisitos funcionales

- **RF-ACC-001**: una cuenta interna activa debe poder iniciar y cerrar sesión y acceder solo
  al espacio privado permitido por esta porción.
  - **Fuente**: CAT-REQ-001, ACT-REQ-001 y D-011.
  - **Actor/permiso**: Directiva o Socia operaria con cuenta activa; se deniega a cuentas
    inactivas y personas sin sesión.
  - **Criterios**: CA-ACC-001-01 a CA-ACC-001-11.
- **RF-ACC-001.1**: el inicio de sesión debe solicitar nombre de usuario y contraseña.
  - **Criterio**: CA-ACC-001-01 — credenciales válidas de una cuenta activa abren el dashboard.
- **RF-ACC-001.2**: credenciales inválidas, nombres inexistentes y cuentas inactivas deben
  rechazarse sin revelar cuál dato o estado provocó el rechazo.
  - **Criterios**: CA-ACC-001-02 y CA-ACC-001-03.
- **RF-ACC-001.3**: una persona sin sesión activa no debe ver contenido privado, incluso si
  intenta abrir su dirección directamente.
  - **Criterio**: CA-ACC-001-04.
- **RF-ACC-001.4**: cerrar sesión debe impedir que la sesión cerrada vuelva a utilizarse para
  acceder al espacio privado.
  - **Criterio**: CA-ACC-001-05.
- **RF-ACC-001.5**: una usuaria autenticada debe poder cambiar su contraseña al demostrar que
  conoce la actual y confirmar una nueva válida.
  - **Criterios**: CA-ACC-001-06 y CA-ACC-001-07.
- **RF-ACC-001.5a**: una usuaria que accede con una credencial temporal debe cambiarla antes
  de utilizar el dashboard.
  - **Criterio**: CA-ACC-001-08 — mientras el cambio inicial no se complete, la cuenta solo
    puede acceder al recorrido de cambio de contraseña y cierre de sesión.
- **RF-ACC-001.6**: el dashboard debe mostrar una bienvenida y solo las opciones ya
  disponibles: cambiar contraseña y cerrar sesión.
  - **Criterio**: CA-ACC-001-09.
- **RF-ACC-001.7**: la primera cuenta debe quedar almacenada como cuenta activa y entregarse
  únicamente cuando el sistema esté funcional.
  - **Criterio**: CA-ACC-001-10 — la cuenta permite el recorrido aprobado y su credencial no
    aparece en pantallas públicas, documentación ni mensajes de diagnóstico.
  - **Entrega aprobada**: una representante designada por la Directiva recibe la credencial
    temporal de forma presencial.
- **RF-ACC-001.8**: una sesión sin actividad debe dejar de permitir acceso privado después de
  30 minutos y solicitar autenticación nuevamente.
  - **Criterio**: CA-ACC-001-11.

### Requisitos no funcionales

- **RNF-UX-001**: los recorridos de acceso, cambio de contraseña y cierre deben funcionar
  desde 360 px sin desplazamiento horizontal accidental y con formularios breves.
  - **Método de verificación**: revisión en móvil real o representativo desde 360 px.
- **RNF-UX-002**: las pantallas deben conservar contraste AA, etiquetas visibles, foco
  identificable, navegación completa por teclado, zoom al 200 %, errores recuperables y
  acciones principales de al menos 44 × 44 px.
  - **Método de verificación**: revisión de contraste, teclado, foco, zoom y mensajes en cada
    estado del recorrido, además de medición de los controles principales.
- **RNF-UX-003**: la interfaz debe usar lenguaje cotidiano, evitar términos técnicos y no
  exigir que la usuaria elija roles o permisos para acceder.
  - **Método de verificación**: prueba de comprensión con usuarias representativas.
- **RNF-CON-001**: el recorrido debe ser ligero, no depender de recursos remotos obligatorios
  y explicar qué hacer cuando una interrupción impide confirmar el resultado.
  - **Método de verificación**: prueba con conexión limitada e interrupción durante envíos.
- **RNF-SEC-001**: cada contenido privado debe comprobar que existe una sesión autorizada; las
  denegaciones no deben alterar cuentas ni revelar credenciales o estados internos.
  - **Método de verificación**: pruebas positivas y negativas por cada operación y acceso
    directo.
- **RNF-PRV-001**: el acceso debe solicitar y mostrar solo los datos personales necesarios;
  una persona no autenticada no debe recibir datos de cuentas ni contenido organizacional.
  - **Método de verificación**: revisión de pantallas, mensajes, registros de evidencia y
    respuestas ante accesos anónimos.

### Datos y entidades clave

| Concepto | Significado para el negocio | Datos mínimos | Reglas/retención pendientes |
|---|---|---|---|
| Cuenta interna | Identidad que permite a una integrante acceder al espacio privado | Nombre de usuario, estado activo/inactivo y credencial protegida | La administración posterior pertenece a `RF-ACC-002` |
| Sesión | Acceso temporal reconocido después de una autenticación válida | Cuenta asociada, vigencia y finalización | Vence después de 30 minutos sin actividad |
| Dashboard de bienvenida | Punto de entrada privado de esta porción | Mensaje de bienvenida y opciones disponibles | Contenido personalizado por actividades pertenece a `RF-ACC-004` |
| Credencial temporal | Secreto inicial entregado para habilitar la primera cuenta | Valor conocido solo por receptora y responsable de entrega | Entrega presencial a representante designada por la Directiva; cambio obligatorio |

### Matriz mínima de permisos

| Operación | Directiva | Socia operaria | Visitante/persona anónima | Evidencia/fuente |
|---|---|---|---|---|
| Iniciar sesión | Permitir con cuenta activa y credenciales válidas | Permitir con cuenta activa y credenciales válidas | Denegar como cuenta interna | RF-ACC-001; ACT-REQ-001 |
| Ver dashboard privado | Permitir con sesión activa | Permitir con sesión activa | Denegar | RF-ACC-001; RNF-SEC-001 |
| Cambiar contraseña propia | Permitir con sesión activa y contraseña actual | Permitir con sesión activa y contraseña actual | Denegar | ACT-REQ-001 |
| Cerrar sesión propia | Permitir con sesión activa | Permitir con sesión activa | No aplica; no obtiene contenido privado | RF-ACC-001 |
| Administrar otras cuentas o permisos | Fuera de alcance | Denegar en esta porción | Denegar | `RF-ACC-002`, `RF-ACC-003` y P-01 |

## Interfaz y experiencia

- El recorrido ordinario de acceso debe completarse en una pantalla de credenciales y llevar
  directamente al dashboard.
- El dashboard inicial muestra bienvenida, “Cambiar contraseña” y “Cerrar sesión”; no muestra
  actividades, encargos ni opciones simuladas.
- Los estados contemplados son: formulario inicial, envío en progreso, acceso correcto,
  credenciales rechazadas, sesión vencida, cambio correcto, error corregible y acceso
  denegado.
- El nombre de usuario conserva una etiqueta visible; la contraseña puede mostrarse u
  ocultarse mediante un control con texto comprensible.
- Los errores se anuncian cerca del campo correspondiente y mediante un resumen cuando haya
  varios; no se comunican únicamente con color.
- Todas las acciones están disponibles con teclado, conservan foco visible y mantienen orden
  comprensible con zoom al 200 %.

## Criterios de éxito (Success Criteria)

- **SC-001**: el 100 % de los criterios CA-ACC-001-01 a CA-ACC-001-11 tiene al menos una
  prueba aprobada, incluidos intentos inválidos, cuenta inactiva y acceso anónimo.
- **SC-002**: al menos el 80 % de las usuarias representativas completa el recorrido de
  iniciar sesión, reconocer el dashboard, cambiar la contraseña y cerrar sesión sin ayuda en
  un máximo de 3 minutos.
- **SC-003**: el 100 % de las pantallas del recorrido se usa desde 360 px y con zoom al
  200 % sin pérdida de información, acciones inaccesibles ni desplazamiento horizontal
  accidental.
- **SC-004**: en el 100 % de los intentos con cuenta inexistente, contraseña incorrecta o
  cuenta inactiva, la persona recibe una respuesta equivalente y no accede a contenido
  privado.
- **SC-005**: tras cerrar sesión, el 100 % de los intentos de reutilizarla o volver a una
  dirección privada exige autenticación nuevamente.

## Trazabilidad académica

| Elemento | Enlace/ID |
|---|---|
| Objetivo específico | OE-02 — desarrollar módulos y control de acceso |
| Sprint | S1 — Administración y acceso |
| Requisitos | `RF-ACC-001`; `RNF-UX-001`; `RNF-UX-002`; `RNF-UX-003`; `RNF-CON-001`; `RNF-SEC-001`; `RNF-PRV-001` |
| ADR | [[../../docs/decisions/ADR-0003-estructura-raiz-aplicacion-django\|ADR-0003 — Estructura raíz de Django y agentes]] |
| Casos de prueba | Estrategia CA-ACC-001-01 a CA-ACC-001-11 definida en el [[../../specs/001-acceso-usuarias-internas/plan\|plan aprobado]] |
| Evidencia | [[../../docs/evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0\|ACT-REQ-001]] |
| ISO/IEC 25010:2023 | Adecuación funcional: completitud, corrección y pertinencia; interacción: operabilidad y accesibilidad; seguridad: confidencialidad |

## Supuestos y dependencias (Assumptions)

- La usuaria recuerda su nombre de usuario; la recuperación externa de credenciales no forma
  parte de esta spec.
- Directiva y Socia operaria comparten los mismos recorridos básicos de cuenta propia. Sus
  operaciones de negocio y permisos diferenciados se definirán en specs posteriores.
- La primera cuenta se crea por un procedimiento controlado fuera de la interfaz pública y se
  entrega presencialmente a una representante designada por la Directiva solo cuando el
  recorrido de esta spec sea funcional y verificable.
- La credencial temporal debe cambiarse antes de utilizar el dashboard.
- Una sesión sin actividad vence después de 30 minutos.
- El sistema funciona principalmente en línea; una interrupción no habilita acceso sin
  autenticar ni confirma un cambio cuyo resultado sea desconocido.
- La matriz definitiva de cargos P-01 no bloquea este acceso básico porque ninguna usuaria
  administra otras cuentas ni ejecuta operaciones de negocio en esta porción.
- El plan deberá resolver los mecanismos de almacenamiento protegido de credenciales,
  sesiones, primera cuenta, pruebas y configuración por entorno sin ampliar esta spec.

## Preguntas pendientes

No quedan preguntas materiales para confirmar esta spec. P-01 continúa abierta para
`RF-ACC-002` y `RF-ACC-003`, pero no bloquea el acceso básico de cuenta propia.

## Registro de validación

| Fecha | Participantes/rol | Decisión | Cambios | Evidencia |
|---|---|---|---|---|
| 2026-07-25 | Tesista | Autorizó preparar SPEC-001 con la opción A | Alcance limitado a `RF-ACC-001` y RNF aplicables | [[../../docs/evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0\|ACT-REQ-001]] |
| 2026-07-25 | Tesista | Resolvió Q1=A, Q2=A y Q3=A | Cambio inicial obligatorio; 30 minutos de inactividad; entrega presencial a representante designada por la Directiva | [[../../docs/evidence/fase-i/2026-07-25-confirmacion-spec-001\|EVID-SPEC-001]] |
| 2026-07-25 | Tesista | Confirma integralmente SPEC-001 | Estado cambia a `confirmed`; se autoriza preparar el plan | [[../../docs/evidence/fase-i/2026-07-25-confirmacion-spec-001\|EVID-SPEC-001]] |
| Pendiente | Representantes de usuarias internas | Validar recorridos durante pruebas representativas | Comprensión, operabilidad y accesibilidad | Pendiente de plan y ejecución |
