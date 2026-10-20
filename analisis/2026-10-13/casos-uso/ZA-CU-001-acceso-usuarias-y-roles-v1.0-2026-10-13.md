---
codigo: ZA-CU-001
titulo: Casos de uso detallados del módulo de acceso de usuarias y roles
modulo: Acceso de usuarias y roles
fase: Fase 2 — Especificación de casos de uso
version: 1.0
fecha: 2026-10-13
autor: Franklin Acero (tesista)
analista: Codex (asistencia de redacción)
estado: propuesta-para-revision
requisitos_base: CAT-REQ-001 v1.2; requisitos_generales_v2.0; priorizacion_requisitos_v1.3
alcance_base: ZA-ALC-001 v1.1
sprint: S1
module: acceso
related:
  - "[[../../../docs/requirements/CAT-REQ-001]]"
  - "[[../alcances-modulos/ZA-ALC-001-acceso-usuarias-y-roles-v1.1-2026-10-13]]"
  - "[[../../../docs/context/feature-index]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - sprint/s1
  - modulo/acceso
publicacion: no-preparado
---

<table style="width:100%;border-collapse:collapse;font-family:'Heebo Light',Heebo,Arial,sans-serif;">
<tr><td colspan="2" style="background:#642138;color:#F0EAC8;padding:14px;font-family:'Mallong Regular',Georgia,serif;font-size:22px;"><strong>[LOGO: Isotipo floral de 4 pétalos - ZHUD ALELÍ Productos Naturales]</strong><br>ZA-CU-001 · Casos de uso detallados del módulo de acceso de usuarias y roles</td></tr>
<tr><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Control documental</th><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Valor</th></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Módulo</td><td style="padding:7px;border:1px solid #AC6E40;">Acceso de usuarias y roles (<code>accounts</code>)</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Fase / entregable</td><td style="padding:7px;border:1px solid #AC6E40;">Fase 2 — Especificación de casos de uso</td></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Versión / fecha</td><td style="padding:7px;border:1px solid #AC6E40;">v1.0 / 13 de octubre de 2026</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Autor / analista</td><td style="padding:7px;border:1px solid #AC6E40;">Franklin Acero (tesista) / Codex (asistencia de redacción)</td></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Estado</td><td style="padding:7px;border:1px solid #AC6E40;">Propuesta interna para revisión del tesista; no aprobada ni publicada</td></tr>
</table>

**Historial de revisiones**

| Versión | Fecha | Descripción | Responsable |
|---|---|---|---|
| v1.0 | 2026-10-13 | Primera propuesta de cinco casos de uso para los requisitos confirmados del módulo. | Franklin Acero; redacción asistida por Codex |

## 1. Propósito y límites

Este documento convierte en recorridos verificables los requisitos confirmados de acceso de usuarias y roles. Cubre inicio y cierre de sesión, administración de membresías, autorización de operaciones protegidas e inicio privado. Cada caso conserva el actor, las precondiciones, el flujo principal, sus alternativas, los resultados esperados y la trazabilidad.

Los valores de **importancia** proceden de la priorización aprobada v1.3. La **complejidad** es una estimación inicial de análisis, no una prioridad aprobada ni una estimación de esfuerzo. Las reglas con prefijo `RN-CU-ACC-*` son reglas locales propuestas para organizar estos casos; no agregan requisitos a CAT-REQ-001.

## 2. Actores

| Actor | Participación en estos casos |
|---|---|
| Socia operaria | Inicia/cierra sesión, intenta operaciones autorizadas y consulta su inicio privado. |
| Directiva | Usa las funciones privadas y administra la vigencia de membresías según la autorización organizacional aplicable. |
| Módulo consumidor | Solicita al módulo de acceso una decisión para una operación protegida; no escribe directamente las cuentas o membresías. |
| Servicio de autenticación del sistema | Valida las credenciales y el estado vigente de la cuenta/membresía. Es parte del sistema, no un actor humano. |

Visitante es un actor del sitio público, no de estos casos privados. Soporte técnico no recibe autoridad organizacional implícita.

## 3. Resumen y orden de importancia

| Caso | Objetivo | Importancia confirmada | Complejidad inicial | Requisitos principales |
|---|---|---|---|---|
| ZA-CU-ACC-001 | Iniciar sesión | Esencial | Media | RF-ACC-001; RNF-SEC-001; RNF-PRV-001 |
| ZA-CU-ACC-002 | Cerrar sesión | Esencial, parte de RF-ACC-001 | Baja | RF-ACC-001; RNF-SEC-001 |
| ZA-CU-ACC-003 | Activar o desactivar una membresía | Alta | Media | RF-ACC-002; RNF-AUD-001; RNF-DAT-001 |
| ZA-CU-ACC-004 | Autorizar una operación protegida | Esencial | Alta | RF-ACC-003; RNF-SEC-001; RNF-PRV-001 |
| ZA-CU-ACC-005 | Consultar el inicio privado | Complementaria | Media | RF-ACC-004; RNF-UX-001/002/003; RNF-PRV-001 |

La complejidad deberá revisarse al decidir detalles de credenciales, sesiones, permisos por operación y contratos entre módulos. No equivale a puntos de historia.

## 4. Casos de uso detallados

### ZA-CU-ACC-001 — Iniciar sesión

| Campo | Especificación |
|---|---|
| ID y nombre | ZA-CU-ACC-001 — Iniciar sesión |
| Actor primario | Socia operaria o integrante de Directiva con cuenta interna |
| Actor secundario | Servicio de autenticación del sistema |
| Descripción | Autenticar a una usuaria interna y permitirle entrar únicamente a contenido autorizado. |
| Importancia / complejidad | Esencial / Media (estimación inicial) |
| Disparador | La usuaria abre una dirección privada o solicita iniciar sesión. |
| Precondiciones | Existe una cuenta interna provisionada; está activa y asociada a una membresía habilitada; la usuaria dispone de credenciales emitidas por un procedimiento que deberá especificarse. |
| Reglas asociadas | `RN-CU-ACC-01`, `RN-CU-ACC-02`, `RN-CU-ACC-06` |
| Requisitos asociados | RF-ACC-001; RNF-SEC-001; RNF-PRV-001 |

**Flujo principal**

| Paso | Acción del actor | Respuesta del sistema |
|---:|---|---|
| 1 | Abre una dirección privada o selecciona «Iniciar sesión». | Presenta el formulario de acceso sin mostrar información privada. |
| 2 | Ingresa las credenciales disponibles y envía el formulario. | Valida las credenciales y vuelve a comprobar en el servidor que la cuenta y la membresía permitan un acceso nuevo. |
| 3 | Espera el resultado. | Si la validación es correcta, establece el contexto autenticado y dirige al recurso originalmente solicitado o al inicio privado. |
| 4 | Solicita una función privada. | Verifica autorización en backend para esa función; la autenticación por sí sola no concede todos los permisos. |

**Flujos alternativos y de excepción**

| Flujo | Referencia | Acción / resultado |
|---|---|---|
| 1a | Paso 2 | Si las credenciales no son válidas, el sistema rechaza el acceso con un mensaje que no revela si una cuenta existe ni cuál dato falló; no crea una sesión autenticada. |
| 1b | Paso 2 | Si la cuenta está inactiva o la membresía no está habilitada, el sistema rechaza el nuevo acceso sin revelar datos sensibles y no crea una sesión autenticada. |
| 1c | Paso 3 | Si no puede establecer el contexto autenticado, el sistema no presenta el acceso como exitoso y ofrece un resultado recuperable sin exponer datos privados. |

**Postcondiciones**

- Éxito: existe un contexto autenticado para la usuaria; los recursos privados todavía se someten a autorización por operación.
- Fallo: no queda creada una sesión autenticada ni se entrega contenido privado.

### ZA-CU-ACC-002 — Cerrar sesión

| Campo | Especificación |
|---|---|
| ID y nombre | ZA-CU-ACC-002 — Cerrar sesión |
| Actor primario | Usuaria interna autenticada |
| Actor secundario | — |
| Descripción | Finalizar el acceso autenticado de la usuaria en el dispositivo actual. |
| Importancia / complejidad | Esencial como parte de RF-ACC-001 / Baja (estimación inicial) |
| Disparador | La usuaria selecciona «Cerrar sesión». |
| Precondiciones | Hay un contexto autenticado activo. |
| Reglas asociadas | `RN-CU-ACC-02`, `RN-CU-ACC-06` |
| Requisitos asociados | RF-ACC-001; RNF-SEC-001; RNF-PRV-001 |

**Flujo principal**

| Paso | Acción del actor | Respuesta del sistema |
|---:|---|---|
| 1 | Selecciona «Cerrar sesión». | Recibe la solicitud de salida asociada al contexto autenticado actual. |
| 2 | Espera la confirmación. | Invalida el contexto autenticado en el servidor y limpia la vista privada activa según el mecanismo implementado. |
| 3 | Vuelve a una dirección privada o usa el botón Atrás. | Revalida el acceso y solicita autenticación antes de entregar contenido privado. |

**Flujos alternativos y de excepción**

| Flujo | Referencia | Acción / resultado |
|---|---|---|
| 2a | Paso 2 | Si el contexto ya no es válido, el sistema lleva a la pantalla de acceso y no afirma que la usuaria conserva una sesión activa. |
| 2b | Paso 2 | Si falla la solicitud de salida, el sistema no confirma el cierre hasta completar la invalidación; presenta un error recuperable y no muestra la vista como cerrada exitosamente. |

**Postcondiciones**

- Éxito: las nuevas solicitudes privadas requieren una sesión autenticada y autorización vigentes.
- Fallo: el sistema comunica que no pudo confirmar la salida y evita presentar falsamente el cierre como completado.

### ZA-CU-ACC-003 — Activar o desactivar una membresía

| Campo | Especificación |
|---|---|
| ID y nombre | ZA-CU-ACC-003 — Activar o desactivar una membresía |
| Actor primario | Integrante de Directiva autorizada para administrar membresías |
| Actor secundario | Servicio de auditoría del sistema |
| Descripción | Cambiar el estado de una membresía sin eliminar la historia de la socia ni sus operaciones previas. |
| Importancia / complejidad | Alta / Media (estimación inicial) |
| Disparador | La Directiva selecciona una membresía y solicita activarla o desactivarla. |
| Precondiciones | La usuaria está autenticada y autorizada para administrar membresías; la membresía objetivo existe; se ingresa el motivo del cambio. |
| Reglas asociadas | `RN-CU-ACC-03`, `RN-CU-ACC-04`, `RN-CU-ACC-05`, `RN-CU-ACC-07` |
| Requisitos asociados | RF-ACC-002; RNF-SEC-001; RNF-AUD-001; RNF-DAT-001 |

**Flujo principal**

| Paso | Acción del actor | Respuesta del sistema |
|---:|---|---|
| 1 | Abre la administración de membresías. | Comprueba en el servidor que puede acceder a esa función y muestra solo la información necesaria para gestionarla. |
| 2 | Selecciona una socia, el nuevo estado y registra el motivo. | Comprueba que la membresía existe y que el estado solicitado está permitido por la operación. |
| 3 | Confirma el cambio. | Vuelve a validar autorización y datos actuales para evitar aplicar un cambio con permisos o estado obsoletos. |
| 4 | — | Actualiza el estado sin borrar membresía, operaciones o evidencias históricas; registra el valor anterior y nuevo, actor, fecha, autorización y motivo en la misma operación. |
| 5 | Revisa el resultado. | Confirma el cambio. Si se desactiva la membresía, un nuevo inicio de sesión debe ser rechazado conforme a RF-ACC-001. |

**Flujos alternativos y de excepción**

| Flujo | Referencia | Acción / resultado |
|---|---|---|
| 3a | Paso 1 | Si la usuaria no tiene permiso vigente, el sistema deniega la acción sin modificar el estado. |
| 3b | Paso 2 | Si la membresía no existe o no puede verificarse, el sistema no guarda el cambio ni revela información a una usuaria no autorizada. |
| 3c | Paso 4 | Si falla el cambio o su registro de auditoría, el sistema revierte la operación completa y no confirma éxito parcial. |

**Postcondiciones**

- Éxito: el estado nuevo queda guardado, el historial permanece y el cambio es reconstruible.
- Fallo: no cambia el estado; no se borra historia ni queda un cambio sin auditoría.

### ZA-CU-ACC-004 — Autorizar una operación protegida

| Campo | Especificación |
|---|---|
| ID y nombre | ZA-CU-ACC-004 — Autorizar una operación protegida |
| Actor primario | Usuaria interna que solicita la operación |
| Actor secundario | Módulo de negocio consumidor que presenta la solicitud protegida |
| Descripción | Resolver en el servidor si la usuaria puede acceder a una operación específica según su perfil, cargo, encargo vigente y permiso definido para la operación. |
| Importancia / complejidad | Esencial / Alta (estimación inicial) |
| Disparador | La usuaria intenta entrar a una función, enviar una petición directa o completar una operación protegida. |
| Precondiciones | Hay identidad verificable; el módulo consumidor identifica la operación; la especificación propietaria define el permiso requerido. Si el permiso no está definido, el sistema no lo infiere ni concede. |
| Reglas asociadas | `RN-CU-ACC-03`, `RN-CU-ACC-06` |
| Requisitos asociados | RF-ACC-003; RNF-SEC-001; RNF-PRV-001 |

**Flujo principal**

| Paso | Acción del actor | Respuesta del sistema |
|---:|---|---|
| 1 | Selecciona una operación o envía una solicitud directa. | El módulo consumidor identifica usuaria, operación y recurso solicitado, y consulta el contrato de autorización del módulo de acceso. |
| 2 | — | Valida en el servidor identidad y estado vigente de la cuenta/membresía; consulta perfil, cargo, encargo vigente y permiso concreto de esa operación. |
| 3 | — | Si todos los criterios definidos para la operación se cumplen, responde «permitido» al módulo consumidor; no ejecuta por sí mismo la regla de negocio. |
| 4 | Continúa con la operación. | El módulo propietario vuelve a validar sus reglas de negocio y aplica su propia autorización de escritura antes de modificar datos. |

**Flujos alternativos y de excepción**

| Flujo | Referencia | Acción / resultado |
|---|---|---|
| 4a | Paso 2 | Si no hay identidad autenticada o la cuenta/membresía no está habilitada, el sistema deniega la solicitud sin entregar contenido protegido ni modificar datos. |
| 4b | Paso 2 | Si el cargo no corresponde o el encargo no está vigente para la operación, el sistema deniega la solicitud sin cambiar datos. |
| 4c | Paso 2 | Si el permiso requerido no está definido en la especificación de la operación, el sistema no concede acceso por defecto; comunica la falta de política como configuración pendiente al flujo responsable. |
| 4d | Paso 2 | Si soporte técnico solicita autoridad organizacional por su rol técnico, el sistema no le concede permisos de negocio implícitos. |
| 4e | Paso 3 | Si la autorización es denegada, el módulo consumidor no ejecuta la operación y presenta un mensaje comprensible sin exponer datos privados. |

**Postcondiciones**

- Éxito: el módulo consumidor puede continuar solo con la operación consultada, según la política vigente; el módulo de acceso no cambia datos de negocio.
- Fallo: se deniega el acceso sin cambios de negocio ni exposición de datos no autorizados.

### ZA-CU-ACC-005 — Consultar el inicio privado

| Campo | Especificación |
|---|---|
| ID y nombre | ZA-CU-ACC-005 — Consultar el inicio privado |
| Actor primario | Usuaria interna autenticada |
| Actor secundario | Módulos de planificación y encargos, mediante lecturas autorizadas |
| Descripción | Presentar a la usuaria sus actividades, pendientes y encargos relevantes, con acciones disponibles según su situación vigente. |
| Importancia / complejidad | Complementaria / Media (estimación inicial) |
| Disparador | La usuaria entra al inicio privado después de autenticarse o selecciona «Inicio». |
| Precondiciones | Hay una sesión autenticada; las fuentes de actividades y encargos proporcionan lecturas autorizadas. |
| Reglas asociadas | `RN-CU-ACC-06`, `RN-CU-ACC-07` |
| Requisitos asociados | RF-ACC-004; RNF-UX-001; RNF-UX-002; RNF-UX-003; RNF-PRV-001 |

**Flujo principal**

| Paso | Acción del actor | Respuesta del sistema |
|---:|---|---|
| 1 | Abre el inicio privado. | Revalida en servidor el contexto autenticado y las lecturas autorizadas. |
| 2 | Espera que cargue el resumen. | Obtiene actividades, pendientes y encargos correspondientes a esa usuaria; excluye información privada de otras personas que no le corresponde consultar. |
| 3 | Revisa el contenido y las acciones disponibles. | Presenta estados y acciones comprensibles según la situación actual, con navegación accesible y sin depender solo del color. |
| 4 | Selecciona una acción disponible. | Comprueba nuevamente autorización en el servidor antes de entregar o modificar información mediante el módulo propietario. |

**Flujos alternativos y de excepción**

| Flujo | Referencia | Acción / resultado |
|---|---|---|
| 5a | Paso 2 | Si no hay actividades, pendientes ni encargos, el sistema muestra un estado vacío claro sin presentar error. |
| 5b | Paso 2 | Si una fuente no está disponible, el sistema comunica que el contenido no pudo actualizarse; no inventa resultados ni muestra información ajena como alternativa. |
| 5c | Paso 4 | Si la autorización dejó de ser válida, el sistema deniega la acción y mantiene sin cambios los datos de negocio. |

**Postcondiciones**

- Éxito: la usuaria visualiza solo información autorizada y pertinente a su situación actual.
- Fallo: no se revela información no autorizada ni se presenta información no cargada como actual.

## 5. Reglas de negocio locales propuestas

| ID propuesto | Regla derivada | Fuente base |
|---|---|---|
| RN-CU-ACC-01 | Solo una cuenta interna activa asociada a una membresía habilitada puede iniciar un nuevo acceso privado. | RF-ACC-001; RF-ACC-002 |
| RN-CU-ACC-02 | Iniciar y cerrar sesión no sustituye la autorización de cada operación protegida. | RF-ACC-001; RF-ACC-003; RNF-SEC-001 |
| RN-CU-ACC-03 | Cada decisión de autorización se resuelve en backend según identidad, estado, perfil, cargo, encargo vigente y permiso específico definido para la operación. | RF-ACC-003; RNF-SEC-001 |
| RN-CU-ACC-04 | La Directiva autorizada puede activar o desactivar membresías; el cambio no borra registros históricos y una denegación no altera datos. | RF-ACC-002; RNF-SEC-001; RNF-DAT-001 |
| RN-CU-ACC-05 | El cambio sensible conserva valor anterior/nuevo, actor, fecha, autorización y motivo en la operación que confirma el cambio. | RNF-AUD-001 |
| RN-CU-ACC-06 | El inicio privado consulta y presenta solo actividades, pendientes, encargos y acciones autorizadas para la usuaria actual. | RF-ACC-004; RNF-PRV-001; RNF-UX-001/002/003 |
| RN-CU-ACC-07 | Los módulos de negocio consultan el acceso mediante el contrato público definido; no escriben directamente en cuentas o membresías. | RF-ACC-003; ZA-ALC-001 v1.1; arquitectura vigente |

Los identificadores `RN-CU-ACC-*` son auxiliares de esta propuesta y no reemplazan requisitos o reglas históricas del catálogo.

## 6. Matriz de trazabilidad

| Requisito confirmado | Casos de uso | Cobertura resumida |
|---|---|---|
| RF-ACC-001 | ZA-CU-ACC-001, ZA-CU-ACC-002 | Acceso de una cuenta habilitada y cierre del acceso autenticado. |
| RF-ACC-002 | ZA-CU-ACC-003 | Gestión de membresías sin borrar historia; la desactivación impide nuevos accesos. |
| RF-ACC-003 | ZA-CU-ACC-004; comprobación en ZA-CU-ACC-001 y ZA-CU-ACC-005 | Permisos en backend, cargo/encargo vigentes, denegación segura y separación del soporte técnico. |
| RF-ACC-004 | ZA-CU-ACC-005 | Inicio privado con actividades, pendientes, encargos y acciones disponibles. |
| RNF-SEC-001 | ZA-CU-ACC-001 a ZA-CU-ACC-005 | Verificación en servidor; las denegaciones no modifican datos. |
| RNF-AUD-001 | ZA-CU-ACC-003 | Historial verificable de cambios de membresía. |
| RNF-DAT-001 | ZA-CU-ACC-003 | Cambio de membresía y auditoría atómicos. |
| RNF-PRV-001 | ZA-CU-ACC-001, ZA-CU-ACC-004, ZA-CU-ACC-005 | No exposición de datos privados a personas no autorizadas. |
| RNF-UX-001/002/003 | ZA-CU-ACC-005 | Inicio móvil, comprensible, accesible y recuperable. |

## 7. Decisiones de detalle que permanecen abiertas

| Tema | Límite de esta propuesta | Cuándo resolver |
|---|---|---|
| Alta de cuenta, entrega/recuperación/cambio de credenciales y campos del formulario | No se define el procedimiento ni política de contraseñas. | Antes de especificar la provisión de cuentas o esos flujos. |
| Duración, expiración y revocación inmediata de sesiones | No se fija tiempo ni tratamiento de sesiones ya abiertas después de desactivar una membresía. | Antes de diseño técnico de sesiones. |
| Permisos por cargo, encargo y operación de negocio | P-01 se cerró para acceso básico; no concede una matriz universal. | En cada especificación propietaria de planificación, asistencia, producción, ventas y reportes. |
| Motivos y datos mínimos del cambio de membresía | El motivo y la trazabilidad provienen de RNF-AUD-001; el catálogo final de motivos no está decidido. | Durante el diseño del formulario, sin reducir los datos de auditoría requeridos. |
| Inicio y almacenamiento local offline | No se autentica offline ni se prolongan permisos en el dispositivo. Los detalles de sincronización se deciden según RF-PWA-003 y P-13/P-14. | En la especificación PWA y de cada operación sincronizable. |

## Fuentes y estado

- [[../../../docs/requirements/CAT-REQ-001|CAT-REQ-001 v1.2]], fuente interna de requisitos confirmados.
- [[../../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13|Requisitos generales v2.0]], tabla completa y vigente.
- [[../../../documentacion/requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13|Priorización v1.3]], importancia confirmada de RF-ACC-001..004 y RNF asociados.
- [[../alcances-modulos/ZA-ALC-001-acceso-usuarias-y-roles-v1.1-2026-10-13|Alcance ZA-ALC-001 v1.1]], base del módulo.
- [[../../../docs/context/feature-index|Índice de funcionalidades activas]], estado y límites de SPEC-001.
- [[../../../.specify/memory/constitution|Constitución 0.2.0]] y [[../../../docs/decisions/ADR-0006-monolito-modular-y-entrega-incremental|ADR-0006]], propiedad de escrituras y contratos modulares.

**Estado:** propuesta interna `proposed`, pendiente de revisión del tesista. La instrucción «siguiente» se tomó como autorización para elaborar este documento de Fase 2; no se interpreta como aprobación de cada regla candidata, decisión de detalle o especificación técnica. No modifica CAT-REQ-001 ni reemplaza SPEC-001. No está preparada para publicar al repositorio docente.
