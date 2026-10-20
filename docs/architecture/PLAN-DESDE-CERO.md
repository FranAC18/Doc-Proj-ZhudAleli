---
title: Plan maestro de implementación modular y PWA
type: roadmap
status: proposed
date: 2026-09-22
updated: 2026-10-08
approved_by: tesista
approved: 2026-09-22
director_review: pending
architecture: "[[../decisions/ADR-0006-monolito-modular-y-entrega-incremental]]"
historical_architecture: "[[../decisions/proposals/2026-09-22-arquitectura-modular-desacoplada]]"
related:
  - "[[ARQUITECTURA-OBJETIVO]]"
  - "[[MODULOS-DETALLADOS]]"
  - "[[../decisions/ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[../../specs/001-acceso-usuarias-internas/plan]]"
tags:
  - proyecto/tesis
  - tipo/plan
  - estado/proposed
  - modulo/transversal
---

# Plan maestro de implementación modular y PWA

## Estado, alcance y gobernanza

Este documento reemplaza la hoja de ruta técnica anterior y traduce el Plan Maestro entregado
por el tesista a las convenciones canónicas del repositorio. El tesista autorizó su ejecución
planificada el 2026-09-22. Permanece `proposed` porque la constitución exige revisión de la
directora cuando una decisión de metodología o alcance afecta el anteproyecto.

La aplicación es una PWA para la gestión organizacional y productiva del Comité de Mujeres
Indígenas «Tránsito Amaguaña» de Zhud y su unidad productiva Zhud Alelí. El horizonte es de 16
semanas, con un desarrollador único, validación progresiva con usuarias y despliegue de bajo
costo. No se crea código ni se cambian requisitos confirmados desde este roadmap; cada módulo
funcional deberá tener su propia spec, plan, tareas y puerta de aprobación.

La arquitectura vigente se confirma en [[../decisions/ADR-0006-monolito-modular-y-entrega-incremental|ADR-0006]]:
**monolito modular Django con capas internas pragmáticas, alta cohesión y bajo acoplamiento**.
La reconciliación del 2026-10-08 sustituye las restricciones de aislamiento de septiembre;
no promueve todo este roadmap ni sus políticas pendientes. Guardar y sincronizar asistencia y
pesajes es una necesidad obligatoria del diseño solicitado el 2026-09-28; falta concretar
las políticas operativas, no decidir si se incorpora esa capacidad. No se usarán
microservicios, SPA independiente ni gRPC en la primera entrega.

## 1. Principios de implementación

1. **Un solo despliegue, límites explícitos.** Django y PostgreSQL se despliegan como una
   aplicación integrada, pero cada bounded context posee sus modelos, migraciones, invariantes,
   servicios y pruebas.
2. **Propiedad y dependencias explícitas.** Las escrituras usan operaciones del propietario.
   Las lecturas autorizadas y FK/JOIN justificados se conservan; se documentan consumidores
   y dirección de dependencias sin ciclos. No se impone HTTP/eventos entre apps.
3. **Capas pragmáticas.** Se separa HTTP de reglas y datos con mecanismos nativos. Servicios,
   consultas y adaptadores aparecen cuando existe comportamiento requerido, sin interfaces
   abstractas, repositorios genéricos o capas vacías para CRUDs simples.
4. **Integridad transaccional.** Las operaciones críticas usan PostgreSQL y `transaction.atomic`.
   Inventario, pesajes, secado, lotes, despachos y cuentas por cobrar conservan movimientos,
   actor, instante y motivo de corrección cuando el requisito lo exige.
5. **Offline verificable.** La interfaz informa si un dato está guardado localmente, pendiente,
   sincronizado o rechazado. Cada operación offline usa `client_operation_id` UUID v4 y el
   servidor debe ser idempotente.
6. **Fuentes de verdad separadas.** Este roadmap organiza la ejecución; las reglas de negocio
   aprobadas viven en specs y requisitos; el código y las pruebas demuestran lo implementado.
7. **Iteración con puertas.** Cada fase termina con pruebas, revisión del diff, evidencia y
   validación humana. Una capacidad pendiente de campo no se implementa por conveniencia.

## 2. Contexto técnico y decisiones de plataforma

| Área | Decisión de planificación | Límite o pendiente |
|---|---|---|
| Runtime | Python 3.12 y Django 5.2 LTS | Se conserva la arquitectura MTV y plantillas Django. |
| Persistencia | PostgreSQL en desarrollo y producción | SQLite solo para pruebas unitarias que no oculten diferencias relevantes. |
| UI | Django Templates, Bootstrap 5 local y JavaScript progresivo | No se crea una SPA independiente. |
| PWA | `manifest.json`, Service Worker, Cache Storage e IndexedDB | La cola offline se activa por módulo solo después de aprobar su spec y conflicto. |
| API de sincronización | HTTP JSON versionado (`/api/v1/sync/outbox/`) | Es un adaptador; los casos de uso siguen dentro del módulo propietario. |
| Infraestructura | Supabase para PostgreSQL y Vercel en la factibilidad/presupuesto aportados | Verificar ubicación real de ejecución Django, conexiones, archivos, HTTPS, costos y respaldos. La selección prevista no acredita un despliegue probado ni tarifas garantizadas. |
| Dependencias | `pyproject.toml` y archivo de bloqueo | La herramienta concreta debe quedar aprobada en el plan de la primera porción. |
| Calidad | `manage.py check`, migraciones, pytest/Django TestCase, pruebas de contrato y CI | La evidencia debe quedar en el vault y no contener datos reales. |

La [[../requirements/proposals/2026-09-28-catalogo-v1-1|revisión v1.1]] contiene la reconciliación
con la línea base que excluía sincronización. La capacidad offline es obligatoria en el diseño
solicitado; P-13/P-14 precisan aceptación temporal, identidad y conflictos. La existencia de
una puerta no resuelve por sí sola la contradicción ni valida esos parámetros.

Referencia actual: [[../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack|16 semanas y USD 2.869]].
Este roadmap conserva aprobación de planificación del 22/09, revisión de la directora pendiente
y cambios documentales del 28/09; no atribuye aprobación funcional a la arquitectura propuesta.

## 3. Módulos y bounded contexts canónicos

Los nombres del Plan Maestro se normalizan a los nombres ya establecidos por la constitución y
ADR-0003. `authentication` se implementa como `accounts`, `production` como `traceability` y
`dashboard` como `reports`; no se renombrarán las apps canónicas sin un ADR adicional.

| App | Propiedad | Dependencias permitidas | Contratos principales |
|---|---|---|---|
| `core` | Utilidades realmente compartidas, solo cuando se necesitan | Ninguna regla de dominio | IDs/reloj o auditoría técnica sin autoridad de negocio; no outbox obligatorio |
| `accounts` | Usuario personalizado, membresía, roles, permisos, sesiones y credenciales | Utilidades compartidas solo si necesarias | Identidad y consultas de autorización; alcance según cada spec |
| `planning` | Jornadas, actividades, asignaciones, fechas y estados | `accounts` por identidad y permisos | Consultas/operaciones de agenda y asignaciones |
| `attendance` | Asistencia, entrada/salida, participación y correcciones | `accounts`, `planning` por identidad y relaciones explícitas | Registro autorizado, resumen y sincronización cuando su spec esté aprobada |
| `traceability` | Catálogo, acopio, pesaje, secado, formulación, lotes, mermas, inventario, despachos y cuentas por cobrar | Identidad/autorización y actividad cuando aplique | Operaciones productivas/comerciales, movimientos y consultas de saldos |
| `reports` | Dashboard, filtros y PDFs mediante lecturas autorizadas | Consultas públicas o ORM explícito revisado; no escritura operativa | Reportes derivados, exportaciones y métricas con fórmula/periodo/fuente |
| `public_site` | Contenido público aprobado y navegación externa | Lecturas públicas delimitadas, sin datos privados | Páginas públicas y estado de publicación |

El contexto comercial permanece dentro de `traceability` para la primera planificación porque
ventas, gastos y cuentas por cobrar forman parte del alcance confirmado. Si su complejidad o
reglas de autorización requieren separación, se abrirá una spec y un ADR antes de crear otra app.

### Contratos inter-módulo

- **Dentro de la aplicación:** funciones/servicios y consultas del propietario cuando se
  requieren; entradas, resultados, errores y garantías explícitos. Los contratos internos
  no requieren serialización o versionado HTTP si no hay consumidores independientes.
- **Eventos de servidor:** no son parte del mínimo. Dispatcher, outbox y proyecciones necesitan
  necesidad demostrada y ADR específico. Si se adoptan, deben conservar integridad y recuperación.
- **HTTP/JSON:** se concreta para PWA/integraciones en sus specs; `/api/v1/sync/outbox/` es una
  ruta propuesta, no aprobada por ADR-0006. Una entrada delega operaciones a sus propietarios
  sin duplicar reglas o autorización.
- **REST interno:** no se usa para llamadas entre apps del mismo proceso; la serialización
  obligatoria añadiría complejidad sin una frontera de despliegue.
- **gRPC:** queda fuera de v1 porque no existe una frontera de red independiente.

## 4. Estructura física del repositorio

La aplicación se ubicará en la raíz ya aceptada por ADR-0003. Se comienza con archivos simples
cuando la app sea pequeña y se promueve a paquetes internos cuando una regla real lo requiera.

```text
F:/Tesis/App Tesis/
├── manage.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── config/
│   ├── settings/{base.py,development.py,test.py,production.py}
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── accounts/
│   │   ├── models.py
│   │   ├── forms.py
│   │   ├── views.py
│   │   ├── urls.py
│   │   ├── migrations/
│   │   ├── templates/accounts/
│   │   └── tests/{unit,integration,contract}/
│   ├── planning/
│   ├── attendance/
│   ├── traceability/
│   ├── reports/
│   └── public_site/
├── templates/{base.html,components/}
├── static/{css,js,pwa,manifest.json,vendor/}
├── tests/{architecture,contract,integration}/
├── specs/
├── docs/
├── agents/
├── .agents/
├── .codex/
└── tools/
```

La primera implementación solo crea `config`, `apps/accounts` y los recursos globales que
`SPEC-001` necesite. Las apps futuras no se crean vacías para anticipar el alcance.
Modelos y migraciones mantienen descubrimiento nativo. `core`, servicios, consultas y paquetes
se añaden cuando el plan los necesita; el archivo de bloqueo lo define el plan aprobado.

## 5. PWA offline-first y patrón outbox

### Flujo operativo

```text
Usuaria registra asistencia o pesaje
        │
        ├─ conexión disponible ──> POST al contrato del módulo ──> PostgreSQL
        │                            respuesta confirmada
        │
        └─ sin conexión ──> IndexedDB: {client_operation_id, payload, status: PENDING}
                              indicador textual «Guardado en dispositivo»
                                      │ evento online / reintento explícito
                                      ▼
                              POST /api/v1/sync/outbox/
                                      │
                              validación + transaction.atomic()
                                      │
                              CONFIRMED o REJECTED con código recuperable
```

### Componentes

- `manifest.json`: instalación `standalone`, orientación móvil y colores validados por UX.
- `sw.js`: Cache-First para app shell y recursos locales; Network-First con fallback para
  páginas públicas visitadas. Se excluyen autenticación y respuestas privadas de SPEC-001.
  Los formularios offline tendrán un shell específico; la precarga mínima privada, si es
  necesaria, se define y protege en P-14, sin cachear HTML privado de forma indiscriminada.
- `idb-manager.js`: almacenes `catalogo_cache` y `transacciones_outbox`, sin contraseñas ni
  datos personales innecesarios.
- `sync-engine.js`: reintento explícito o por evento `online`, backoff y deduplicación por UUID.
- Endpoint de sincronización: autentica, valida versión de contrato, limita el lote, procesa
  por módulo y devuelve resultado individual; nunca informa éxito antes de confirmar la
  transacción.

El outbox del navegador contiene comandos todavía pendientes de aceptación; el outbox de
servidor, si se adopta mediante ADR, contiene eventos de cambios ya confirmados. Son dos
responsabilidades distintas: un registro local no prueba que la transacción remota ocurrió.
Los campos, UUID y ruta HTTP de esta sección son diseño propuesto, no contrato aprobado.

### Criterios de seguridad e idempotencia

- `client_operation_id` es único por módulo y operación; una repetición devuelve el resultado
  anterior en lugar de duplicar el registro.
- El servidor usa una restricción de unicidad y un estado de procesamiento auditable.
- Las operaciones rechazadas permanecen visibles en el dispositivo con un mensaje comprensible
  y opción de corregir o descartar según la regla del módulo.
- La sincronización no permite saltarse RBAC: el servidor vuelve a evaluar el permiso al recibir
  el comando.
- La cola local no se considera respaldo; el sistema informa que un dato no sincronizado puede
  perderse si se borra el almacenamiento del dispositivo.

## 6. Persistencia e integridad de datos

1. PostgreSQL es la fuente operativa. Cada app posee sus tablas, migraciones, índices y reglas.
2. Las relaciones dentro o entre apps usan FK y restricciones justificadas. Las lecturas
   cruzadas son explícitas y autorizadas; las escrituras mantienen un propietario.
3. `traceability` conserva el flujo acopio → pesaje → secado → formulación/lote → inventario →
   despacho → cuenta por cobrar. Cada transición registra entradas y salidas, no solo totales.
4. Los reportes usan consultas autorizadas. No mantienen una segunda copia operativa ni
   escriben tablas de producción; materialización requiere necesidad y ADR.
5. El almacenamiento local PWA conserva pendientes; no es un outbox de eventos del servidor.
   Un outbox de servidor, si se adopta en otro ADR, debe garantizar integridad/idempotencia.
6. Las operaciones críticas delimitan `transaction.atomic`, aplican restricciones y bloqueos de
   fila solo donde exista una regla de concurrencia demostrada. La frontera de app no divide
   una operación que debe ser atómica: venta, líneas, movimientos y efectos monetarios se
   confirman juntos o se revierten juntos. Los eventos no justifican saldos parciales.
7. Un esquema PostgreSQL por app queda como endurecimiento futuro; no se impone antes de validar
   las migraciones Django y la necesidad de segregación de permisos.
8. Los respaldos, retención, borrado y recuperación se definen antes del despliegue productivo;
   Supabase o cualquier proveedor debe demostrar estas capacidades.

## 7. RBAC y experiencia móvil

La matriz de permisos se deriva de requisitos confirmados y no de esta nota. La traducción
inicial del Plan Maestro es:

| Perfil | Acceso previsto | Validación necesaria |
|---|---|---|
| Directiva (presidenta, secretaria, tesorera) | Gestión autorizada, supervisión y reportes según cargo | Confirmar operación por cargo en la matriz de permisos. |
| Socia operaria | Perfil propio, tareas, asistencia y entregas permitidas | Confirmar qué registros puede crear/corregir. |
| Visitante | Sitio público | No debe recibir datos internos. |

Las pantallas serán mobile-first, táctiles, comprensibles sin vocabulario técnico, con contraste
AA, teclado, zoom al 200 % y estados expresados por texto además de color. La «regla de tres
toques» se mantiene como objetivo UX a validar, no como requisito aprobado hasta medirla con
usuarias.

## 8. Fases e hitos de 16 semanas

Las fases técnicas se alinean con los cinco sprints del anteproyecto. F1 y F2 son diseño y
fundación; no sustituyen los sprints académicos.

| Fase | Semanas | Objetivo | Entregable / puerta |
|---|---:|---|---|
| F1. Requisitos | 1–2 | Levantar, analizar y validar necesidades, alcance y pendientes, incluida continuidad offline. | Catálogo revisado y prioridades; identificar políticas que debe cerrar cada spec. |
| F2. Diseño y entorno PWA | 3–4 | Diseñar arquitectura, base de datos, UX y continuidad; preparar configuración PWA y entorno. | Modelo, wireframes y contratos revisados. Crear base Django solo tras puertas de diseño de SPEC-001; registrar por separado verificaciones de entorno y funcionales. |
| F3. Administración y acceso | 5–6 | Acceso básico de SPEC-001 y porciones posteriores de membresía/permisos/inicio según specs propias. | SPEC-001 cubre RF-ACC-001; RF-ACC-002/003/004 necesitan sus propias puertas. Completar SPEC-001 no completa todo S1. |
| F4. Planificación | 6–7 | Registrar jornadas, actividades, responsables, fechas y estados. | Vertical slice de `planning`, contrato con `accounts`, pruebas de permisos y estados. |
| F5. Asistencia y primer offline | 7–8 | Registrar mingas/asambleas, participación y correcciones; habilitar outbox solo para el flujo aprobado. | `attendance`, IndexedDB, sincronización idempotente, corte de red y validación con usuarias. |
| F6. Trazabilidad y gestión comercial | 9–10 | Catálogos, acopio, secado, rendimiento, transformación, lotes, inventario, entregas, ventas, gastos, pagos y rendición. | 23 RF confirmados con sus specs; transacciones, pesajes offline y conciliación. Bruto/tara/neto solo si la spec los define; no son campos nuevos aprobados aquí. |
| F7. Dashboard y reportes | 11–12 | Consolidar métricas simples y PDFs comprensibles para la asamblea. | `reports` y `public_site`, consultas autorizadas, fórmulas, periodos, permisos y salida imprimible. |
| F8. Integración y evaluación técnica | 13–14 | Probar módulos, sincronización concurrente, recuperación, seguridad, accesibilidad y calidad funcional. | Suite de sistema, pruebas de red intermitente, respaldo/restauración y resultados ISO/IEC 25010:2023. |
| F9. Territorio y cierre | 15–16 | Validar recorridos reales, capacitar, documentar y transferir. | Talleres, manuales, evidencia anonimizada, decisión de despliegue y aprobación de cierre. |

### Puertas de avance

- **F1 → F2:** necesidades y alcance identificados; arquitectura, contratos y políticas
  detalladas se diseñan en F2, antes de la implementación afectada.
- **F2 → F3:** diseño de la porción aprobado y entorno reproducible; no se presenta
  PWA funcional como terminada solo por configurar el entorno.
- **Cada sprint:** demo independiente, casos positivos/negativos y revisión con usuarias.
- **F7 → F8:** reportes explican fórmula, periodo y fuente y no duplican totales operativos.
- **F8 → F9:** no existen hallazgos críticos abiertos y las pruebas de recuperación tienen
  evidencia.
- **Cierre:** matriz requisito → diseño → código → prueba → evidencia actualizada y aprobación
  humana.

## 9. Estrategia de pruebas y CI

- **Unitarias:** reglas de dominio, normalización, cálculos de merma, UUID e idempotencia.
- **Integración:** ORM, migraciones, `transaction.atomic`, restricciones y PostgreSQL real.
- **Contratos:** payloads de servicios, respuestas HTTP, códigos de rechazo y compatibilidad
  entre productor y consumidor.
- **Arquitectura:** imports permitidos, ausencia de joins cruzados y ownership de migraciones.
- **PWA:** app shell sin red, cache, almacenamiento local, reintento, duplicados, orden y
  conflicto de lotes.
- **Seguridad:** RBAC positivo/negativo, CSRF, sesión, no filtración, no caché y logs seguros.
- **UX:** 360 px, zoom 200 %, teclado, contraste AA, comprensión y regla de tres toques como
  objetivo medido.
- **CI:** `manage.py check`, migraciones, tests, lint, análisis de imports y artefactos; no se
  ejecutan datos reales ni secretos.

## 10. Migración y reversión

Aunque la aplicación actual es greenfield, si aparece código acoplado se aplicará una migración
strangler:

1. Capturar pruebas de caracterización y congelar nuevos accesos cruzados.
2. Introducir una fachada de aplicación y un adaptador anticorrupción.
3. Extraer un slice completo a su bounded context y comparar lecturas.
4. Activar la nueva ruta con una bandera reversible; solo usar escritura paralela con
   reconciliación y ventana de retiro definida.
5. Retirar el camino antiguo después de pruebas, auditoría y aprobación.

Las migraciones de esquema se ejecutan hacia adelante con respaldo verificable. No se hace
`reset`, borrado ni reescritura de historia. Una fase bloqueada continúa con diseño, pruebas o
documentación no dependiente, y queda registrada en un checkpoint.

## 11. Riesgos y decisiones pendientes

| Riesgo / decisión | Mitigación o puerta |
|---|---|
| Offline-first aumenta conflictos y soporte | Implementar primero un único flujo, UUID/idempotencia y pruebas de corte; ampliar solo con evidencia. |
| Roles del Plan Maestro no coinciden exactamente con matriz aprobada | Mantener `Directiva` como perfil agrupador y confirmar permisos por cargo antes de codificar. |
| Supabase/Vercel no ejecutan el despliegue Django esperado | Validar proveedor con smoke test, SSL, backups, logs y rollback antes de seleccionarlo. |
| Reportes requieren datos cruzados | Consultas públicas u ORM explícito autorizado; no consultas de negocio desde plantillas. |
| Ventas/cuentas por cobrar cambian de dominio | Mantenerlas en `traceability` durante la planificación y abrir ADR si la spec demuestra otra cohesión. |
| Cambios de metodología del anteproyecto | Revisión de la directora antes de presentar el plan como definitivo. |

## 12. Documentación y cierre

- Cada fase actualiza su spec, plan, tareas, contrato y evidencia sin sobrescribir notas aprobadas.
- Las decisiones se registran como ADR o propuesta con estado visible.
- La matriz de trazabilidad enlaza requisito, actor, sprint, módulo, prueba, evidencia y resultado.
- El manual técnico describe instalación, configuración por entorno, migraciones, sincronización,
  respaldo y recuperación.
- El manual de usuaria usa pasos visuales, mensajes de estado y recuperación ante conectividad.
- Antes de presentar el proyecto se revisa la coherencia entre anteproyecto, fuente de campo,
  arquitectura, código, pruebas y evaluación ISO/IEC 25010:2023.

## Regla de avance

Este roadmap está aprobado para planificación por el tesista, pero ninguna fase puede saltar
la puerta de requisito, plan, implementación, revisión o cierre. `SPEC-001` continúa siendo la
única porción confirmada para implementación inmediata; las fases de planificación, asistencia,
trazabilidad, PWA offline y reportes requieren sus specs y tareas antes de escribir código.

## Control de coherencia del 2026-09-28

El Gantt permite solapamientos S6/S7 con dependencias satisfechas. Pruebas parciales S5–S12;
integración S13; funcional/usabilidad y offline S13–S14; correcciones S14; validación final
S15; capacitación/manuales S15–S16. La construcción offline acompaña asistencia/pesajes.
Documentar continuamente sigue siendo obligatorio. Fechas absolutas no aportadas.

**Riesgo temporal abierto:** 23 RF de trazabilidad/comercial más pesajes offline en S9–S10,
y RF-ACC-002/003/004 aún sin spec en S5–S6, requieren estimación por tareas. El Gantt expresa
la planificación aportada, no una demostración de suficiencia ni permiso para omitir alcance.
Los límites estrictos de imports/FK/eventos de septiembre quedan parcialmente superados por
ADR-0006. Se conservan las puertas, integridad y plan aprobado de SPEC-001.

## Aprobación de requisitos fuente — 2026-09-28

[[../requirements/CAT-REQ-001|CAT-REQ-001 v1.1]] está confirmado por el tesista, con
[[../evidence/casos-de-uso/2026-09-28-aprobacion-requisitos-v1-1|evidencia de aceptación]].
Queda resuelta la exclusión offline de la línea base anterior. P-13/P-14 y las specs siguen
pendientes; la aprobación de requisitos no promueve automáticamente esta propuesta técnica
ni sustituye la revisión académica, la estimación de trabajo o la prueba de despliegue.
