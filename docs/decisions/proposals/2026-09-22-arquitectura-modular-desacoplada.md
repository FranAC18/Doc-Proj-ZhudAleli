---
title: Propuesta ADR — Arquitectura modular desacoplada por dominios
type: decision
status: proposed
date: 2026-09-22
decision_id: PRO-ADR-004
task_id: HARNESS-ARCH-001
accepted_by: null
accepted: null
approved_for_implementation_by: tesista
approved_for_implementation: 2026-09-22
module: transversal
related:
  - "[[../ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[../../architecture/ARQUITECTURA-OBJETIVO]]"
  - "[[../../architecture/PLAN-DESDE-CERO]]"
  - "[[../../../specs/001-acceso-usuarias-internas/spec]]"
  - "[[../../../.specify/memory/constitution]]"
tags:
  - proyecto/tesis
  - tipo/decision
  - estado/proposed
  - modulo/transversal
---

# Propuesta ADR — Arquitectura modular desacoplada por dominios

## Estado y alcance de la propuesta

Esta nota continúa siendo una propuesta arquitectónica y no un ADR formalmente aceptado. El
tesista autorizó planificar e implementar la arquitectura el 2026-09-22. Refinará ADR-0003 sin
cambiar su decisión de ubicar el proyecto Django en la raíz. La revisión de la directora y la
promoción a ADR aceptado siguen pendientes.

La solicitud se clasifica como arquitectura, planificación y documentación. La constitución
vigente ya exige un monolito modular Django; por tanto, «desacoplada» se interpreta como
desacoplamiento de módulos y contratos, no como una migración automática a microservicios.

## 1. Contexto

El dominio es la gestión organizacional y la trazabilidad productiva del Comité de Mujeres
Indígenas «Tránsito Amaguaña» de Zhud y su unidad productiva Zhud Alelí. La fuente de alcance
entregada por el tesista delimita cinco módulos funcionales, desarrollo en 16 semanas, enfoque
mobile-first y una PWA con continuidad limitada ante interrupciones de conectividad.

El stack base validado en los artefactos del proyecto es Python 3.12, Django 5.2 LTS,
PostgreSQL, plantillas Django, Bootstrap 5 y JavaScript progresivo mínimo. Supabase y Vercel
figuran en la factibilidad y presupuesto actuales como infraestructura prevista: Supabase
para PostgreSQL y Vercel para los componentes compatibles. Su ejecución real de Django,
respaldos y límites necesitan validación; no son servicios desplegados y probados todavía.

La arquitectura monolítica acoplada queda prohibida: ningún dominio puede importar modelos,
consultar tablas o modificar datos pertenecientes directamente a otro dominio. A la vez, el
proyecto no justifica todavía el costo operativo de varios servicios, redes internas, colas,
observabilidad distribuida y despliegues independientes.

### Hechos verificados

- La constitución 0.1.0 exige un monolito modular Django con PostgreSQL y límites de dominio.
- ADR-0003 acepta la raíz del repositorio como ubicación del proyecto y prevé las apps
  `core`, `accounts`, `planning`, `attendance`, `traceability`, `reports` y `public_site`.
- `SPEC-001` está confirmada, pero solo cubre el acceso de usuarias internas y mantiene la
  aplicación Django sin código de producción.
- La fuente de alcance pegada por el tesista describe cinco módulos, PWA y validación
  incremental en 16 semanas.
- La línea base de julio excluía sincronización, pero el tesista la exige el 2026-09-28.
  Guardar y sincronizar registros esenciales forma parte obligatoria de esta propuesta. La
  revisión v1.1 documenta el cambio; las políticas y specs pendientes condicionan su
  implementación, no vuelven opcional la necesidad ni la sustituyen por comprobantes.

### Decisiones aún no aprobadas

- Si ventas, gastos y cuentas por cobrar pertenecen a `traceability` o a un contexto comercial
  separado.
- Política de retención, desactivación y borrado por dominio.
- Infraestructura final, respaldos y comportamiento ante pérdida prolongada de conectividad.
- Catálogos, unidades, reglas de formación de lotes y conciliación detallada.
- La activación de sincronización offline por módulo, sus conflictos y evidencia de idempotencia.

## 2. Decisión propuesta

Adoptar una **arquitectura modular desacoplada dentro de un único despliegue Django**,
organizada por bounded contexts y slices verticales. Cada módulo posee su dominio, casos de
uso, persistencia, interfaces y pruebas; los demás módulos solo lo utilizan mediante contratos
de aplicación o eventos versionados.

Se descarta tanto el monolito acoplado como los microservicios para la primera entrega:

- Un solo proceso y una sola base PostgreSQL mantienen bajo el costo operativo, simplifican la
  depuración y permiten entregar un incremento funcional completo por sprint.
- Los límites de importación, persistencia y comunicación hacen que un módulo pueda probarse,
  versionarse y extraerse más adelante sin reescribir todo el sistema.
- Una frontera de red solo se añade cuando exista un consumidor independiente, una necesidad de
  escalado o una restricción de despliegue demostrada.

### Reglas no negociables

1. Un módulo es propietario de sus entidades, tablas, migraciones y reglas invariantes.
2. Ningún módulo importa `models` de otro módulo para ejecutar lógica de negocio.
3. Ningún módulo hace `JOIN`, SQL directo o escritura sobre tablas de otro módulo.
4. La entrada a un módulo se realiza mediante un caso de uso explícito (command/query) o un
   evento documentado; las vistas Django son adaptadores, no contratos de dominio.
5. La unidad transaccional la define la operación de negocio. Si afecta varios contextos,
   sus servicios participan en una transacción explícita de la misma base PostgreSQL cuando
   la regla exige todo o nada. La idempotencia y los eventos no sustituyen esa atomicidad.
6. `core` contiene solo capacidades transversales estables (identificadores, reloj, auditoría,
   envoltura de eventos); no se convierte en un cajón de reglas compartidas.
7. Los reportes consultan proyecciones de lectura o contratos de consulta; no duplican ni
   mutan las tablas operativas.
8. La sincronización offline se implementa únicamente en los módulos y operaciones cuya spec la
   apruebe. Encola comandos con identificador idempotente y nunca escribe directamente en
   PostgreSQL desde el navegador. Las operaciones pendientes de validación no se declaran
   implementadas; el comprobante manual sigue limitado a la contingencia aprobada.

## 3. Bounded contexts y contratos

| Contexto / app | Responsabilidad y propiedad | Consume | Publica / expone |
|---|---|---|---|
| `accounts` | Identidad, estado de cuenta, membresía, roles, permisos y sesiones. | Identificador de organización y comandos de acceso. | `UserActivated`, `UserDeactivated`, consultas de autorización y comandos de cambio de credencial. |
| `planning` | Jornadas, actividades, asignaciones, estados y observaciones de planificación. | `accounts` mediante `UserId` y consulta de autorización. | `ActivityScheduled`, `AssignmentChanged`, consultas de agenda. |
| `attendance` | Entrada, salida, participación y correcciones autorizadas de asistencia. | `ActivityId`, `UserId` y políticas de `accounts`. | `AttendanceRecorded`, `AttendanceCorrected`, consultas de historial. |
| `traceability` | Acopio, secado, lotes, mermas, inventario y movimientos productivos. | Identidades autorizadas y referencias de actividad cuando aplique. | `LotCreated`, `ProcessRecorded`, `InventoryMoved`, consultas de trazabilidad. |
| `reports` | Proyecciones de lectura, filtros, exportaciones y dashboard. | Eventos y contratos de consulta versionados. | Consultas y exportaciones; no publica escrituras operativas. |
| `public_site` | Navegación y contenido público aprobado. | Proyección pública de contenido y estado de publicación. | Páginas públicas; no consume datos personales internos. |
| `core` / integración | IDs, reloj, auditoría, sobre de evento, outbox y políticas técnicas comunes. | Ninguna regla de negocio. | Infraestructura compartida y contratos de integración. |

El contexto comercial (ventas, gastos y cuentas por cobrar) permanece como decisión pendiente.
Mientras no exista una spec validada, no se crea una app ni se incorporan tablas por anticipado.
El dashboard es una capacidad de `reports`, no un dominio adicional.

### Contrato de comunicación elegido

1. **Dentro del proceso**: cada app ofrece funciones de aplicación o protocolos Python
   estables (`commands`, `queries` y `ports`). Las vistas, formularios y el adaptador PWA
   llaman esos contratos, nunca el ORM de otra app.
2. **Eventos de dominio**: los hechos relevantes se publican en un outbox transaccional
   propiedad de la integración. Los consumidores son idempotentes y pueden reconstruir sus
   proyecciones. En la primera entrega el transporte puede ser un dispatcher interno; no se
   introduce un broker sin requisito.
3. **REST/HTTP**: solo se crea una frontera HTTP cuando exista un cliente independiente,
   integración externa o necesidad de despliegue separado. Ese adaptador invoca los mismos casos
   de uso internos y no contiene una segunda lógica de negocio.
4. **gRPC**: no se selecciona para v1; no hay todavía una frontera de red ni un beneficio que
   compense su complejidad operativa.
5. **Offline/PWA por puerta**: la planificación incluye una cola local y un endpoint de
   sincronización, pero cada módulo debe aprobar su operación offline, conflicto y prueba antes
   de activarla. Cada comando lleva `client_operation_id`, versión de contrato y marca de tiempo,
   con reintento idempotente resuelto por el módulo propietario.

## 4. Estructura de directorios propuesta

La raíz es la aceptada en ADR-0003. La siguiente estructura profundiza las apps por dominio y
permite comenzar con archivos simples (`models.py`, `views.py`) mientras la complejidad sea baja;
los paquetes se separan cuando una regla real lo justifique.

```text
F:/Tesis/App Tesis/
├── manage.py
├── config/
│   ├── settings/{base.py,development.py,test.py,production.py}
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── core/
│   │   ├── domain/{ids.py,clock.py,audit.py}
│   │   ├── application/{events.py,outbox.py}
│   │   └── infrastructure/{models.py,migrations/}
│   ├── accounts/
│   │   ├── domain/{entities.py,policies.py,events.py}
│   │   ├── application/{commands.py,queries.py,ports.py}
│   │   ├── infrastructure/{models.py,migrations/}
│   │   ├── interfaces/{http.py,forms.py,urls.py}
│   │   ├── templates/accounts/
│   │   ├── static/accounts/
│   │   └── tests/{unit,integration,contract}/
│   ├── planning/
│   ├── attendance/
│   ├── traceability/
│   ├── reports/
│   └── public_site/
├── templates/                  # layout y componentes globales mínimos
├── static/                     # tokens y recursos globales versionables
├── tests/{architecture,contract,integration}/
├── specs/
├── docs/
├── agents/
├── .agents/
├── .codex/
├── scripts/
└── tools/
```

Cada app repite el patrón de `accounts`. `infrastructure/repositories.py` o un adaptador
equivalente se agrega solo si una app necesita aislar una consulta compleja, una fuente externa
o una futura extracción; no se crea un repositorio genérico encima del ORM por defecto.

Las pruebas de `unit` no requieren Django cuando prueban reglas puras; `integration` valida
persistencia propia; `contract` valida la interfaz pública del módulo; `tests/architecture`
comprueba que las importaciones no crucen capas prohibidas.

## 5. Estrategia de persistencia y datos

### Propiedad y aislamiento

- PostgreSQL sigue siendo una única base transaccional en v1, con tablas y migraciones
  propiedad de una sola app. Los nombres incluyen el contexto (`accounts_*`, `planning_*`, etc.)
  para hacer visible la propiedad.
- Las relaciones internas del mismo contexto pueden usar claves foráneas y restricciones
  PostgreSQL. Las referencias a otro contexto se guardan como IDs estables (preferiblemente
  UUID) y se validan mediante un contrato de aplicación; no se crean claves foráneas cruzadas.
- Un esquema PostgreSQL separado por módulo es una opción de endurecimiento para una fase
  posterior, si la segregación de permisos o una extracción lo justifica. No se impone en v1
  porque añade operaciones de migración y configuración que no están validadas.

### Escrituras, concurrencia y auditoría

- Cada caso de uso delimita su `transaction.atomic` al módulo propietario y usa restricciones
  (`UniqueConstraint`, validaciones y bloqueos de fila) solo donde la regla lo requiera.
- Inventario, lotes, secado y correcciones conservan movimientos o historial; nunca se actualiza
  un saldo sin registrar el hecho que lo explica.
- Los cambios sensibles almacenan actor, instante, valor anterior, valor nuevo y motivo cuando
  el requisito lo confirme. Los logs no incluyen credenciales ni datos personales innecesarios.
- El outbox se escribe en la misma transacción que el cambio del módulo. Un publicador posterior
  marca el evento como entregado; los consumidores deduplican por `event_id`.
- `reports` mantiene proyecciones derivadas con versión y fecha de reconstrucción. Si una
  proyección queda desactualizada, se puede reconstruir desde eventos o una consulta de lectura
  autorizada sin modificar el dato operativo.

### Límites de consulta

El código de dominio no hace consultas cruzadas. Una consulta que necesite datos de varios
contextos se implementa en `reports` como proyección o en un servicio de lectura explícitamente
documentado. Se prohíbe resolver el problema agregando imports directos, joins ocultos o una
tabla de totales sin fuente.

## 6. Roadmap iterativo de refactorización y entrega

Cada fase termina con pruebas, revisión del diff, validación con usuarias cuando corresponda y
una decisión de avance. Las semanas son una guía compatible con las 16 semanas de la fuente; no
autorizan alcance que todavía esté pendiente.

| Fase | Semanas orientativas | Resultado y puerta |
|---|---:|---|
| 0. Contrato y línea base | 1–2 | Confirmar bounded contexts, reglas de importación, IDs, riesgos de PWA y decisiones pendientes. Puerta: tesista valida límites y no quedan ambigüedades críticas. |
| 1. Diseño y entorno | 3–4 | Arquitectura, modelo de datos, UX y configuración PWA/entorno. La creación de Django respeta las puertas de diseño de SPEC-001; configuración no equivale a capacidad offline funcional. |
| 2. Administración y acceso | 5–6 | Acceso básico de SPEC-001 y porciones de membresía/permisos/inicio con specs propias. SPEC-001 por sí sola no completa los cuatro RF de administración. |
| 3. Planificación | 6–7 | Implementar `planning`, publicar eventos de agenda y validar asignaciones con usuarias. Puerta: una jornada puede crearse, consultarse y corregirse según reglas aprobadas. |
| 4. Asistencia | 7–8 | Implementar `attendance` consumiendo `ActivityId`, con duplicados, correcciones e historial. Puerta: recorrido móvil y auditoría verificados. |
| 5. Trazabilidad y comercial | 9–10 | Catálogo, acopio, secado, lotes, inventario, entregas, ventas, gastos, pagos y rendición; pesajes offline. Puerta: specs y pruebas de los 23 RF; esfuerzo pendiente de estimación. |
| 6. Reportes y público | 11–12 | Construir proyecciones de `reports`, exportaciones priorizadas y `public_site`; no consultar tablas operativas desde plantillas. Puerta: fórmulas, periodos y permisos validados. |
| 7. Endurecimiento | 13–14 | Probar sincronización PWA aprobada, concurrencia, respaldos, seguridad, accesibilidad y recuperación de operaciones rechazadas. Puerta: pruebas de sistema y recuperación ejecutadas. |
| 8. Evaluación y entrega | 15–16 | Validación con usuarias, ISO/IEC 25010:2023 según alcance, manuales, diccionario de datos y decisión de despliegue. Puerta: evidencia completa y aprobación humana. |

### Ruta de migración si aparece código acoplado

Si durante la implementación se descubre una base de código tradicional, se aplica un
strangler incremental sin interrumpir la operación:

1. Capturar pruebas de caracterización y métricas del flujo existente.
2. Colocar una fachada de aplicación delante del código acoplado y congelar nuevos accesos
   directos al ORM ajeno.
3. Extraer un slice completo a su bounded context, con adaptador anticorrupción para traducir
   nombres y estados heredados.
4. Comparar lecturas y, solo si el riesgo lo exige, ejecutar una escritura paralela controlada
   con reconciliación; no mantener dos fuentes indefinidas.
5. Cambiar el enrutamiento al módulo nuevo, conservar auditoría y retirar el camino antiguo
   después de una ventana de observación acordada.

## 7. Consecuencias, riesgos y mitigaciones

### Beneficios esperados

- Entrega y prueba por módulo sin esperar a que todo el sistema esté terminado.
- Menor riesgo de que una regla de asistencia, inventario o acceso contamine otro dominio.
- Posibilidad de extraer un módulo a servicio en el futuro usando contratos ya definidos.
- Un único despliegue, una sola sesión Django y una operación compatible con el presupuesto y
  el tiempo de la tesis.

### Costos y riesgos

- Los contratos internos, eventos y proyecciones requieren disciplina documental y pruebas de
  arquitectura.
- La ausencia de claves foráneas cruzadas desplaza parte de la validación al código de casos de
  uso y a procesos de reconciliación.
- Un outbox mal operado puede retrasar reportes; se mitiga con idempotencia, reintentos y una
  pantalla de salud técnica.
- La PWA y la sincronización offline pueden introducir conflictos; solo se habilitan para
  comandos confirmados y con política de resolución validada.
- La separación de ventas y cuentas por cobrar no debe decidirse por conveniencia técnica; se
  mantiene abierta hasta que la spec de negocio la confirme.

## 8. Alternativas consideradas

| Alternativa | Resultado | Motivo |
|---|---|---|
| Monolito Django acoplado | Rechazada | Permite iniciar rápido, pero mezcla reglas, tablas y permisos; hace costosa la prueba y la migración. |
| Microservicios desde el inicio | Rechazada para v1 | Añade despliegues, red, observabilidad, consistencia eventual y costos sin una necesidad demostrada. |
| Arquitectura de servicios internos con REST/gRPC obligatorio | Rechazada para v1 | Duplica serialización y operación dentro del mismo proceso; se conserva como adaptador futuro. |
| Modular monolith por bounded contexts | Recomendada | Mantiene la factibilidad de 16 semanas y deja límites verificables para iterar o extraer. |

## 9. Validación requerida antes de aceptación formal

La autorización del tesista del 2026-09-22 cubre la planificación e implementación por fases.
Antes de promover esta propuesta a ADR aceptado aún se requiere:

- revisión de la directora por el cambio metodológico y la incorporación de offline-first;
- specs y tareas para cada bounded context y para cada operación offline activada;
- confirmación de la regla de referencias por IDs sin claves foráneas cruzadas;
- política de conflictos, retención, respaldos, recuperación y publicación;
- validación del proveedor de infraestructura y actualización de los planes afectados.

Mientras estas puertas no estén satisfechas, el estado correcto es `proposed`; no se ejecuta
`speckit-implement` para módulos futuros ni se crean apps fuera de las tareas aprobadas.

## Actualización de coherencia — 2026-09-28

Esta propuesta se lee con la [[../../requirements/proposals/2026-09-28-catalogo-v1-1|revisión v1.1]]
y el [[../../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack|Gantt, presupuesto y stack actuales]].
PWA con guardado/sincronización es obligatoria en el diseño solicitado. Las decisiones de
cola, aislamiento y payload siguen propuestas; el cambio no aprueba automáticamente un ADR.
El cronograma detallado actualizado está en [[../../architecture/PLAN-DESDE-CERO|plan maestro]]:
diseño en S3–S4, y S9–S10 incluye ventas, gastos y cuentas por cobrar, no solo producción.

La atomicidad de una operación multi-entidad prevalece sobre límites de app: no se permite
confirmar parcialmente venta, inventario y saldos. Outbox local de comandos y outbox de
servidor para eventos confirmados son mecanismos diferentes. Supabase proporciona la BD
prevista; la ejecución Django con la infraestructura presupuestada requiere verificación.
