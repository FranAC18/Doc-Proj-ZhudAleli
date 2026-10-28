<!--
Sync Impact Report — 2026-10-20
Version change: 1.0.0 → 2.0.0 (MAJOR: se elimina la dependencia obligatoria de
spec/plan/tasks como trámite previo a todo desarrollo y se separan los repositorios).
Modified principles: I. Valor validado antes que volumen de código;
II. Portabilidad del proceso, no dependencia del modelo;
VI. Trazabilidad académica continua; VII. Control humano, privacidad y cambios reversibles.
Modified sections: Puertas del flujo; Gobierno.
Added section: Repositorios y Git.
Removed rule: la ausencia de spec, plan, tareas o checklist bloquea por sí sola un
commit de código vinculado a un requisito y sprint vigentes.
✅ Sincronización: AGENTS.md, README.md, roles/adaptadores de implementer, documenter y
git-manager; skills locales relevantes; templates base y overrides plan/tasks;
docs/context/context-index.md, feature-index.md, PLAN-DESDE-CERO.md,
OBSIDIAN_POLICY.md y matriz de trazabilidad.
Decision: docs/decisions/ADR-0008-separacion-repositorios-y-flujo-git.md.
Approval: plan confirmado expresamente por el tesista el 2026-10-20.
No placeholders deferred. Esta enmienda no declara implementada la aplicación ni cerrados
los criterios pendientes del Sprint 1.
-->

# Constitución de ingeniería de Zhud Alelí

- **Estado**: Aprobada por el tesista
- **Versión**: 2.0.0
- **Propuesta**: 2026-07-21
- **Ratificación**: 2026-07-21 por el tesista
- **Última enmienda**: 2026-10-20, separación de repositorios registrada en ADR-0008.

## Principios centrales

### I. Valor validado antes que volumen de código

Cada funcionalidad debe resolver un problema identificado para un actor real y enlazar una
fuente. Una propuesta de IA no se convierte en requisito ni en alcance aprobado. No se
implementan reglas organizativas, fórmulas, permisos o reportes que dependan de decisiones de
campo pendientes. Cuando falte una decisión material, la funcionalidad permanece en borrador
o bloqueada.

Para iniciar una porción de código basta como base documental un requisito vigente con
fuente, alcance y criterios verificables, y el sprint al que pertenece. Las specs, planes,
tareas y checklists aprobados se respetan cuando existen; su ausencia no exige producir
documentos adicionales antes de programar o registrar un commit. Si el requisito no permite
determinar con seguridad el comportamiento, se aclara esa decisión concreta antes de
implementarla, sin bloquear otras porciones independientes.

### II. Portabilidad del proceso, no dependencia del modelo

Requisitos, especificaciones, decisiones, tareas, pruebas y evidencias deben ser Markdown,
código o datos abiertos versionados en los repositorios que les corresponden. Ningún
comportamiento esencial depende del historial privado de un proveedor. `AGENTS.md` del
repositorio general es el contrato común; los directorios de cada motor solo lo adaptan a
su interfaz. Cambiar de Codex a Kimi o GLM no puede cambiar el alcance aprobado ni la
definición de terminado. El código consulta el requisito y sprint vigentes en el repositorio
general; esos documentos no se duplican en el repositorio de la aplicación.

### III. Calidad demostrable

Toda tarea funcional debe tener criterios de aceptación y pruebas proporcionales al riesgo.
Los permisos requieren casos positivos y negativos. Los cambios de esquema incluyen
migraciones y verificación. “El agente dijo que funciona” no es evidencia. Marcar una tarea,
funcionalidad o criterio como terminado exige su verificación y evidencia correspondiente.
La falta de esa evidencia determina un resultado parcial o pendiente, pero no impide que el
tesista cierre administrativamente el periodo del sprint.

### IV. Arquitectura modular, cohesión e integridad de datos

La aplicación será un monolito modular Django con PostgreSQL, una unidad de entrega y límites
de dominio explícitos. Cada módulo agrupa reglas, datos, operaciones y pruebas de su
responsabilidad para mantener alta cohesión. Se separan presentación HTTP, casos de uso/reglas
y persistencia con mecanismos nativos; se crean servicios o consultas cuando existe
comportamiento que los justifica, sin capas vacías ni repositorios genéricos sobre el ORM.

Cada módulo posee sus escrituras. La colaboración usa operaciones públicas explícitas y
lecturas autorizadas; las dependencias se documentan y se evitan ciclos y acceso arbitrario
a detalles internos. Se conservan claves foráneas y relaciones justificadas. Las operaciones
con varias entidades que deban confirmar juntas usan una transacción común y control de
concurrencia según sus invariantes. Inventario, pesajes, secado y lotes conservan movimientos
e historial; no se sustituyen por totales sin respaldo.

La autorización se verifica en backend, también desde entradas alternativas y sincronización.
Cada incremento conserva compatibilidad de datos y contratos y prueba los recorridos anteriores
afectados antes de publicar la versión conjunta. Una unidad de entrega admite varios workers
o instancias; no exige un único proceso. La capacidad de carga se justifica con escenarios,
objetivos y mediciones. Microservicios, SPA, colas de servidor, proyecciones persistidas e
aislamiento genérico adicional requieren necesidad comprobada y ADR; las capacidades offline
aprobadas conservan sus propias specs y políticas de seguridad.

### V. Experiencia digna y accesible

La interfaz se diseña para móvil, conectividad limitada y distintos niveles de alfabetización
digital. Debe ser consistente, clara, responsiva, navegable por teclado y con contraste AA.
Los estados usan texto además de color; los formularios explican errores y recuperación. La
interfaz principal no será el Django Admin y se validarán recorridos con usuarias reales.

### VI. Trazabilidad académica continua

Cada requisito aprobado enlaza objetivo específico, fuente, sprint, diseño, código, prueba,
evidencia y resultado de evaluación ISO/IEC 25010:2023 cuando corresponda. La documentación
se actualiza durante el desarrollo sin convertirse en una barrera para cada commit de código.
La matriz del repositorio general enlaza requisito, sprint, PR y tag de la aplicación cuando
exista una entrega de código. Obsidian visualiza los archivos del repositorio general; no
crea una segunda fuente de verdad.

### VII. Control humano, privacidad y cambios reversibles

El tesista conserva control total y exclusivo sobre el cierre, reapertura y avance entre
sprints. Puede cerrar un periodo cuando lo decida, aunque existan tareas o criterios
pendientes, sin permiso de agentes, revisores, directora u organización, y sin acta ni
aprobación adicional. Para continuidad se anota sprint, fecha, resultado y pendientes en el
estado activo, backlog o checkpoint ya usado; el apunte no es requisito previo ni solicitud de
aprobación. Ningún agente ni otra puerta puede vetar esa decisión.

El cierre del periodo no declara terminado el trabajo, no aprueba requisitos ni decisiones,
no sustituye validaciones específicas de un entregable y no cambia el alcance por sí solo.
Los pendientes conservan su estado y se trasladan al trabajo posterior. La aceptación
académica u organizacional que exija un requisito o entregable se aplica a ese entregable,
no al cierre administrativo del sprint.

El tesista también conserva control de alcance, aprobación, Git y publicación. Ningún agente
hace `commit`, `push`, `merge`, reescritura de historia ni acciones irreversibles sin solicitud
explícita. No se versionan credenciales ni datos personales innecesarios. Las afirmaciones de
cumplimiento normativo necesitan fuente oficial y validación humana.

## Repositorios y Git

- **Repositorio general `ZhudAleli`**: contiene `.specify/`, `specs/`, `docs/`,
  `documentacion/` revisada, `agents/`, `.agents/`, adaptadores de agentes, plantillas,
  requisitos, sprints y herramientas del proceso. Excluye `/app/` mediante `.gitignore`.
  Nunca recibe commits de código de la aplicación, migraciones Django ni pruebas de producto.
- **Repositorio de aplicación `FranAC18/App-zhudaleli`**: contiene únicamente código Django,
  migraciones, pruebas de producto, plantillas y estáticos fuente, dependencias,
  configuración de ejecución/CI, `.gitignore` y un README técnico breve. No contiene
  agentes, skills, specs, requisitos, bitácoras, matriz ni documentación de proceso.
- Todo commit y push de código se hace desde la raíz Git de la aplicación. Antes de cada
  push se comprueban la ruta actual, `git rev-parse --show-toplevel`, `git remote -v`, la
  URL de push, rama y archivos incluidos. Está prohibido usar `git add .` desde la raíz
  del workspace general y hacer force push a `main`.
- Los commits de la aplicación usan Conventional Commits y referencias reales:
  `tipo(scope): descripción [RF-XXX][SPRINT-N]`. `RF-XXX` representa el ID completo
  vigente, por ejemplo `RF-ACC-001`; `N` es el sprint de ejecución del cambio,
  que puede diferir del sprint originalmente planificado. No se inventan IDs.
- `main` de la aplicación se protege en GitHub. El desarrollo usa ramas
  `feature/RF-XXX-descripcion` y entra a `main` mediante PR. Las operaciones iniciales
  necesarias para establecer un repositorio vacío se documentan como bootstrap; después
  se configura protección con PR requerido y force push deshabilitado.
- Cada cierre de sprint con código integrado identifica el commit de la app mediante un
  tag `sprint-N` y actualiza en el repositorio general la matriz requisito → sprint →
  PR/tag. Si no hubo entrega de código, la matriz declara `sin entrega de código`; no
  se crea un tag que sugiera una versión inexistente.
- La ausencia de documentos del proceso en la app nunca bloquea un commit. Para desarrollar
  se consulta en el repositorio general el requisito y sprint vigentes; las pruebas,
  revisión de permisos y seguridad siguen siendo proporcionales al cambio.

## Restricciones técnicas

- Python 3.12 y Django 5.2 LTS como base propuesta para iniciar la aplicación.
- PostgreSQL en desarrollo integrado y producción; SQLite solo puede usarse en pruebas
  unitarias que no oculten diferencias relevantes.
- Bootstrap 5, plantillas Django y JavaScript progresivo mínimo.
- Apps de dominio previstas: `accounts`, `planning`, `attendance`, `traceability`, `reports`
  y `public_site`, más un `core` transversal pequeño.
- Usuario Django personalizado antes de la primera migración estable.
- Modelos y migraciones conservan el descubrimiento nativo de Django; excepciones requieren
  diseño y verificación explícitos. Solo se crean archivos/apps exigidos por el plan vigente.
- Dependencias, operaciones públicas, dueño de datos y puntos transaccionales se registran
  por funcionalidad. `core` contiene únicamente utilidades realmente compartidas.
- Cada publicación incremental entrega código, migraciones y recursos compatibles, con
  verificación y recuperación previstas; el versionado Git no sustituye el despliegue.
- Configuración por entorno y secretos fuera de Git.
- CI con comprobación Django, migraciones, pruebas, lint y revisión de artefactos cuando
  existan esas herramientas.

## Puertas del flujo

1. **Base para desarrollo**: requisito y sprint vigentes, alcance y criterios verificables;
   decisiones materiales del comportamiento resueltas. No exige un archivo adicional.
2. **Preparación proporcional**: rutas, escritor, datos, permisos y verificación esperada
   definidos para el cambio. Puede registrarse en una tarea, PR o handoff; no obliga a
   crear `plan.md` o `tasks.md` cuando no existen.
3. **Revisión del trabajo**: pruebas proporcionales, diff revisado y hallazgos críticos
   resueltos antes de declarar terminado o publicar un incremento. Un commit intermedio
   puede conservar trabajo incompleto con su estado indicado con veracidad.
4. **Cierre administrativo del sprint**: lo decide exclusivamente el tesista, en la fecha
   que elija. No requiere aprobación externa, acta, revisión previa de todas las evidencias ni
   completar las puertas anteriores. La decisión se anota brevemente en el estado activo,
   backlog o checkpoint existente, al cerrar o después; el apunte no es una condición previa,
   y no se exige un documento nuevo.

El resultado del trabajo se informa con veracidad: tareas, criterios y entregables sin
verificación permanecen `blocked`, `partially-complete` o pendientes, aunque el periodo se
cierre y comience el siguiente. El cierre administrativo no cambia esos estados ni aprueba
automáticamente requisitos, decisiones o entregables.

## Gobierno

- Esta constitución guía los planes y revisiones una vez aprobada.
- Un cambio de principio requiere ADR, motivo, impacto y aprobación del tesista. Esta enmienda
  fue solicitada explícitamente por el tesista y queda registrada en ADR-0007.
- Los cambios de alcance o metodología que afecten el anteproyecto también requieren revisión
  de la directora. El cierre administrativo del periodo no altera por sí solo el alcance, los
  requisitos aprobados ni la metodología académica, y no requiere esa revisión.
- Una puerta de calidad puede impedir declarar terminado el trabajo afectado, pero no puede
  exigir permiso o trámite adicional para que el tesista cierre un sprint o continúe al siguiente.
- La separación de repositorios y la base documental mínima de desarrollo se registran en
  ADR-0008. El repositorio de aplicación no se usa para suplir decisiones de requisitos.
- Los agentes deben señalar una contradicción en vez de escoger silenciosamente una fuente.
- Las enmiendas usan versión semántica: MAJOR para cambios incompatibles de principios,
  MINOR para ampliación material y PATCH para ajustes no semánticos. La revisión de planes
  comprueba la constitución vigente y registra impacto, pruebas y ADR de excepciones.
- ADR-0006 registra el monolito modular. ADR-0007 registra la autoridad del tesista sobre el
  cierre administrativo; ninguno aprueba automáticamente requisitos futuros, specs,
  infraestructura ni acciones Git/publicación.

**Versión**: 2.0.0 | **Propuesta**: 2026-07-21 | **Última modificación**: 2026-10-20
