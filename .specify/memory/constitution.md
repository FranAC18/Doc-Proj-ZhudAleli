<!--
Sync Impact Report — 2026-10-20
Version change: 0.2.0 → 1.0.0 (MAJOR: se redefine la puerta de cierre administrativo del sprint).
Modified principles: III. Calidad demostrable; VII. Control humano, privacidad y cambios reversibles.
Modified sections: Puertas del flujo; Gobierno.
Added guidance: autoridad exclusiva del tesista para cerrar/reabrir periodos, registro mínimo
de estado y pendientes, y separación entre cierre del periodo y finalización del trabajo.
Removed rule: fallar una puerta de calidad ya no impide cerrar administrativamente el sprint.
✅ Sincronización: templates base plan/tasks; overrides constitution/plan/tasks/README;
AGENTS.md; agents/tesis/OBSIDIAN_POLICY.md y PROJECT_CONTEXT.md;
docs/context/context-index.md y feature-index.md; docs/traceability/MATRIZ-TRAZABILIDAD.md;
docs/bitacora/ESTADO-ACTIVO.md.
✅ Revisión de templates spec/checklist y skills/comandos Spec Kit: no añaden una aprobación
al cierre; la autoridad de la constitución prevalece sobre los ejemplos genéricos.
Decision: docs/decisions/ADR-0007-autoridad-del-tesista-para-cierre-de-sprints.md.
Approval: solicitud explícita del tesista del 2026-10-20.
No follow-up approval is required for administrative sprint closure. No placeholders deferred.
This amendment does not claim unfinished tasks, criteria or product validations are complete.
-->

# Constitución de ingeniería de Zhud Alelí

- **Estado**: Aprobada por el tesista
- **Versión**: 1.0.0
- **Propuesta**: 2026-07-21
- **Ratificación**: 2026-07-21 por el tesista
- **Última enmienda**: 2026-10-20, solicitud explícita del tesista registrada en ADR-0007.

## Principios centrales

### I. Valor validado antes que volumen de código

Cada funcionalidad debe resolver un problema identificado para un actor real y enlazar una
fuente. Una propuesta de IA no se convierte en requisito ni en alcance aprobado. No se
implementan reglas organizativas, fórmulas, permisos o reportes que dependan de decisiones de
campo pendientes. Cuando falte una decisión material, la funcionalidad permanece en borrador
o bloqueada.

### II. Portabilidad del proceso, no dependencia del modelo

Requisitos, especificaciones, decisiones, tareas, pruebas y evidencias deben ser Markdown,
código o datos abiertos versionados en Git. Ningún comportamiento esencial depende del
historial privado de un proveedor. `AGENTS.md` es el contrato común; los directorios de cada
motor solo lo adaptan a su interfaz. Cambiar de Codex a Kimi o GLM no puede cambiar el alcance
aprobado ni la definición de terminado.

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
se actualiza durante el desarrollo, no al final. Obsidian visualiza los mismos archivos del
repositorio; no crea una segunda fuente de verdad.

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

1. **Puerta de requisito**: fuente, actor, alcance, criterios y dudas materiales resueltas.
2. **Puerta de plan**: datos, permisos, interfaz, pruebas, riesgos y trazabilidad definidos.
3. **Puerta de implementación**: tareas con rutas y un escritor asignado.
4. **Puerta de revisión**: pruebas pasan, diff revisado y hallazgos críticos resueltos.
5. **Cierre administrativo del sprint**: lo decide exclusivamente el tesista, en la fecha
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
- Los agentes deben señalar una contradicción en vez de escoger silenciosamente una fuente.
- Las enmiendas usan versión semántica: MAJOR para cambios incompatibles de principios,
  MINOR para ampliación material y PATCH para ajustes no semánticos. La revisión de planes
  comprueba la constitución vigente y registra impacto, pruebas y ADR de excepciones.
- ADR-0006 registra el monolito modular. ADR-0007 registra la autoridad del tesista sobre el
  cierre administrativo; ninguno aprueba automáticamente requisitos futuros, specs,
  infraestructura ni acciones Git/publicación.

**Versión**: 1.0.0 | **Propuesta**: 2026-07-21 | **Última modificación**: 2026-10-20
