---
title: Evidencia de revisión de monolito modular con capas internas
type: evidence
id: EVID-ARCH-002
status: partially-complete
date: 2026-10-07
task_id: ARCH-REVIEW-002
phase: pre_commit
commit: pending
commit_hash: null
branch: opencode/spec-001-fase-1-diseno
head: c2654519b041d8f96a2028482608c93ac9d8ea0b
sprint: S1
project_phase: Fase-II-diseno
module: transversal
objective: Registrar el análisis y la revisión de capas internas por módulo sin aceptar la arquitectura.
decision_status: pending-tesista-agreement
technical_review: completed-no-open-findings
director_review: pending
constitution_current: 0.1.0
constitution_candidate: 0.2.0
universal_final_validation: passed-with-inherited-warnings
requirement_ids:
  - RF-ACC-001
  - RF-PWA-002
  - RF-PWA-003
  - RNF-SEC-001
  - RNF-AUD-001
  - RNF-DAT-001
  - RNF-PRV-001
changed_files:
  - docs/decisions/proposals/2026-10-07-monolito-modular-con-capas.md
  - docs/bitacora/ESTADO-ACTIVO.md
  - docs/evidence/architecture/2026-10-07-revision-monolito-capas.md
  - docs/bitacora/checkpoints/2026-10-07-revision-arquitectura-monolito-capas.md
related:
  - "[[../../decisions/proposals/2026-10-07-monolito-modular-con-capas]]"
  - "[[../../bitacora/checkpoints/2026-10-07-revision-arquitectura-monolito-capas]]"
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[../../decisions/proposals/2026-09-22-arquitectura-modular-desacoplada]]"
  - "[[../../decisions/ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[../../sprints/ROADMAP-ANTEPROYECTO]]"
  - "[[../../../specs/001-acceso-usuarias-internas/plan]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
  - sprint/s1
---

# Evidencia de revisión de monolito modular con capas internas

## Resultado y alcance

Se registra la evaluación [[../../decisions/proposals/2026-10-07-monolito-modular-con-capas|PRO-ARCH-002]]
solicitada por el tesista tras la observación de su profesor. El tesista aclaró que busca
capas dentro de cada módulo para crecer en funciones con bajo acoplamiento y alta cohesión.
Autorizó análisis especializado y documentación; condicionó modificar la constitución a
estar de acuerdo con la arquitectura.

La recomendación revisada es **monolito modular Django con capas internas pragmáticas**.
La revisión técnica está cerrada sin hallazgos accionables pendientes según el handoff del
coordinador. La aceptación del tesista y la revisión académica permanecen pendientes.
La constitución sigue en 0.1.0; 0.2.0 es una candidata con texto concreto en la propuesta.
La fase es `pre_commit`, con `commit: pending`: HEAD identifica la base local y no un commit
de esta revisión.

La tarea corresponde a Fase II, con alcance transversal y continuidad de la preparación
de S1. No existe una nota independiente de Sprint 1 en `docs/sprints/`; se enlaza el
[[../../sprints/ROADMAP-ANTEPROYECTO|roadmap vigente]] y el plan de SPEC-001, sin crear un sprint
ni cambiar sus puertas.

## Trabajo y participación especializada

| Participación | Resultado registrado |
|---|---|
| Tesista | Solicitud y aclaración de capas por módulo; autorización condicionada para enmendar la constitución. |
| Coordinador | Recuperación selectiva, contraste con fuentes oficiales, propuesta, mapa de sincronización constitucional y actualización del estado operativo. |
| Arquitecto especializado | Contraste local de alternativas, responsabilidades, dependencias, integridad y coste; recomendó monolito modular con capas internas. |
| Reviewer independiente | Revisó la propuesta, detectó el hallazgo P2 de reintentos y cerró la revisión tras corregirlo. |
| Documenter | Creó esta evidencia y su checkpoint a partir de la propuesta revisada, del handoff y de verificaciones locales. |

Las skills usadas en la tarea fueron `zhud-aleli-context`, `speckit-constitution` y
`zhud-aleli-documenter`. El trabajo con `speckit-constitution` preparó la enmienda y su
impacto; no aplicó ni propagó una constitución nueva. La participación especializada no
equivale a aprobación humana.

## Alternativas y recomendación documentada

| Alternativa evaluada | Resultado de la evaluación |
|---|---|
| Monolito modular con convenciones Django actuales | Viable, con límites explícitos para evitar duplicar reglas en vistas. |
| Monolito modular con capas internas pragmáticas | Recomendada: presentación, casos de uso/reglas, consultas cuando se justifican y persistencia nativa. |
| Dominio independiente de Django con puertos y adaptadores | Mayor aislamiento tecnológico a cambio de interfaces y mapeos; exige una necesidad concreta. |
| Servicios desplegables independientemente | Introducen red, contratos remotos y coordinación de datos; no hay mediciones que justifiquen adoptarlos en esta entrega. |

El razonamiento y las fuentes están en las secciones 3–8 de PRO-ARCH-002. Monolito describe
la unidad de entrega y las capas describen responsabilidades internas; pueden coexistir.
Cada módulo conserva sus escrituras y reglas. La colaboración usa operaciones públicas
explícitas, consultas autorizadas y relaciones justificadas. Las operaciones que deben
confirmarse juntas comparten una transacción y control de concurrencia según sus invariantes.

La propuesta conserva ORM, modelos, restricciones y migraciones Django. Servicios y consultas
propios aparecen solo cuando contienen comportamiento requerido. SPEC-001 puede mantener
autenticación, vistas y formularios nativos sin introducir capas vacías ni ampliar su alcance.

La separación se concreta en dependencias revisables: un caso de uso recibe actor y datos
explícitos, aplica reglas y devuelve resultados o errores de negocio; la vista o adaptador
construye la respuesta HTTP. Los casos de uso no reciben la solicitud HTTP completa ni
renderizan plantillas, y los modelos no importan presentación. El reviewer también confirmó
este párrafo final de la sección 5 sin abrir nuevos hallazgos, según el coordinador.

## Hallazgos, corrección y riesgos

**P2 corregido: autorización de resultados idempotentes.** La propuesta precisaba la
revalidación al sincronizar, pero faltaba explicitarla al devolver un resultado de un reintento
sin una nueva escritura. La sección 8 ahora exige comprobar sesión, identidad/origen y
permisos vigentes antes de devolver el resultado; impide consultar colas o resultados privados
de otra cuenta. El reviewer confirmó el cierre sin hallazgos accionables pendientes. Esta
corrección es documental: no existe código de sincronización probado en esta tarea.

La [[../../decisions/proposals/2026-09-22-arquitectura-modular-desacoplada|propuesta del 2026-09-22]]
conserva estado `proposed`. Su autorización histórica para planificar e implementar no
equivale a un ADR aceptado. PRO-ARCH-002 documenta estos riesgos antes de adoptarla:

| Riesgo de la propuesta anterior | Tratamiento propuesto |
|---|---|
| Prohibición general de FK y JOIN entre apps | Conservar integridad relacional y lecturas autorizadas; justificar excepciones individualmente. |
| Outbox y proyecciones persistidas como base obligatoria | Exigir necesidad y ADR propios; reportes consultan datos operativos por defecto. |
| Modelos y migraciones solo bajo `infrastructure/` | Mantener descubrimiento nativo o documentar y probar registro/configuración alternativos. |
| Definición del monolito como un único proceso | Una entrega conjunta puede ejecutarse con varios workers o réplicas. |

Son riesgos de diseño, no fallos observados en una aplicación en ejecución. No se borró ni
se promovió la propuesta anterior. El plan aprobado de SPEC-001 conserva prioridad sobre
árboles propuestos incompatibles.

## Verificaciones reales

El handoff del coordinador entrega las verificaciones previas. El documenter comprobó
rama, HEAD, raíz/vault, destinos libres, ausencia de aplicación y constitución intacta.

| Verificación | Resultado y procedencia |
|---|---|
| `git status --short --branch` y `git rev-parse HEAD` | Comprobados: rama y HEAD del YAML; existen cambios locales previos y cambios documentales de esta tarea. |
| `git rev-parse --show-toplevel`, contrato y `.obsidian/` | Raíz `F:/Tesis/App Tesis` confirmada como repositorio y vault. |
| `Test-Path` de `manage.py`, `apps` y `config` | Los tres devolvieron `False`; la aplicación Django todavía no existe. |
| `git diff --exit-code -- .specify/memory/constitution.md` | Exit 0; constitución intacta. Comprobación del reviewer recibida en el handoff y repetida por documenter. |
| SHA-256 de la constitución | `0E45B53EFCC32E154D8B54FF09DA24A4A6C46403C9328E74E54E6D919CA09C63`, coincidente con el handoff. |
| `git diff --check` dirigido a docs y constitución | Pasó según el handoff; también pasó su comprobación directa de espacios en la propuesta nueva. |
| `git diff --check -- docs .specify/memory/constitution.md`, documenter | Exit 0 después de crear las notas; aviso de conversión LF/CRLF del estado activo. |
| Comprobación directa de whitespace de las dos notas nuevas | Pasó: 0 líneas con espacios o tabuladores finales; cubre los documentos aún no rastreados por Git. |
| `python tools/validate-universal.py --json`, primera ejecución | Falló con exit 1 por HEAD antiguo `a6e842f` en estado activo frente a `c265451`; resultado comunicado por el coordinador. |
| `python tools/validate-universal.py --json`, ejecución final del coordinador | Exit 0, `ok: true`, `missing: []`, `errors: []`; rama, HEAD y ARCH-REVIEW-002 sincronizados. Mantiene cuatro advertencias heredadas. |
| Comprobación directa con Python estándar, coordinador | Exit 0; 41 enlaces Markdown/Wikilinks locales de los cuatro documentos de la tarea comprobados, sin destinos faltantes ni espacios finales. |
| `git diff --check` global, repetido por el coordinador | Exit 1 exclusivamente por espacios sobrantes preexistentes en `design/style-guide/tokens.html:19` y `:75`; fuera del alcance. |

La primera validación universal conservó cuatro advertencias heredadas: referencia del MOC
a HEAD `73e3c0f` y enlaces de ejemplo a `RF-001-autenticacion`, `Tarea-configurar-rbac` y
`SPRINT-01-acceso` en `ESTADOS-Y-PROGRESO`. El coordinador corrigió el estado activo a
ARCH-REVIEW-002 y al HEAD real. La validación final posterior a la creación de estas notas
pasó con exactamente esas cuatro advertencias y sin nuevos errores. Se conserva el fallo
inicial como resultado histórico, con su causa y corrección.

No se ejecutaron pruebas funcionales Django, migraciones ni pruebas de carga. No hay
mediciones de concurrencia, latencia o recursos ni verificación del proveedor de despliegue.
El antecedente de 12 socias legales y 6 activas no es una medida de concurrencia ni un techo
de crecimiento. Bajo acoplamiento y capas facilitan evolución; no acreditan capacidad.

## Fuentes y evidencia usada

Fuentes locales: propuesta PRO-ARCH-002 revisada, constitución 0.1.0, CAT-REQ-001 v1.1,
plan de SPEC-001, arquitectura objetivo, ADR-0003 y propuesta del 2026-09-22. El handoff
del coordinador aporta el cierre del reviewer y las verificaciones anteriores; esta nota
no inventa una ejecución independiente de esos comandos.

Las fuentes oficiales consultadas por el coordinador y citadas en la propuesta incluyen
[filosofías Django 5.2](https://docs.djangoproject.com/en/5.2/misc/design-philosophies/),
[transacciones](https://docs.djangoproject.com/en/5.2/topics/db/transactions/),
[sesiones](https://docs.djangoproject.com/en/5.2/topics/http/sessions/),
[optimización de datos](https://docs.djangoproject.com/en/5.2/topics/db/optimization/),
[despliegue](https://docs.djangoproject.com/en/5.2/howto/deployment/),
[carga de aplicaciones](https://docs.djangoproject.com/en/5.2/ref/applications/#how-applications-are-loaded),
[MIGRATION_MODULES](https://docs.djangoproject.com/en/5.2/ref/settings/#migration-modules),
[arquitecturas web de Microsoft](https://learn.microsoft.com/en-us/dotnet/architecture/modern-web-apps-azure/common-web-application-architectures)
y [principios de escalado](https://learn.microsoft.com/en-us/azure/architecture/guide/design-principles/scale-out).
Las fuentes conceptuales de Microsoft no proponen cambiar Django por .NET ni el proveedor.

## Pendientes y próximo paso condicionado

1. Obtener acuerdo explícito del tesista sobre la alternativa B y el texto candidato del
   principio IV, o registrar los ajustes solicitados.
2. Solo después del acuerdo, registrar aceptación y ADR reales, aplicar la enmienda y
   sincronización de `speckit-constitution` con fecha efectiva; las fuentes vigentes no se
   modifican desde este handoff documental.
3. Conservar revisión académica, P-13/P-14, specs futuras, dimensionamiento y despliegue
   como pendientes propios. Esta revisión no ejecuta las 37 tareas de SPEC-001.
4. Un eventual commit requiere validación de git-manager y autorización explícita del
   tesista. La evidencia `post_commit` exige hash real, rama, archivos incluidos y validación.

El [[../../bitacora/checkpoints/2026-10-07-revision-arquitectura-monolito-capas|checkpoint]]
conserva el handoff para continuar. No hubo conflicto de destino al iniciar la documentación.
