# AGENTS.md — Zhud Alelí

## Misión

Construir una aplicación web funcional, clara y verificable para la gestión organizacional
y la trazabilidad productiva del Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud.
Este archivo es el contrato corto que Codex y otros hosts descubren automáticamente; la
documentación detallada se recupera bajo demanda.

## Inicio de una tarea

1. Confirma que la raíz contiene este archivo y `.specify/memory/constitution.md` y que
   también es la raíz del vault de Obsidian.
2. Lee [`docs/context/context-index.md`](docs/context/context-index.md).
3. Lee [`docs/bitacora/ESTADO-ACTIVO.md`](docs/bitacora/ESTADO-ACTIVO.md) y confirma rama,
   `HEAD`, tarea y rutas permitidas antes de escribir.
4. Clasifica la solicitud según `task_types` en `tools/agent-routes.toml`.
5. Carga solamente el contexto indicado por esa clasificación. No leas todo `docs/`, todo
   `.specify/` ni todo el directorio de una funcionalidad por defecto.

## Recuperación selectiva

- Arquitectura o planificación: constitución, índice, arquitectura/ADR relevantes y la
  funcionalidad activa indicada por `docs/context/feature-index.md`.
- Implementación: `tasks.md`, secciones relevantes de `spec.md`, código y pruebas; contratos
  y modelo de datos únicamente cuando la tarea los toca.
- Frontend: reglas UI, componentes, archivos visuales y criterios de accesibilidad relevantes.
- Investigación: solo las fuentes necesarias para la pregunta.
- Revisión: diff, archivos modificados, contratos, pruebas y reglas aplicables.
- Documentación: la plantilla o fuente concreta y las rutas autorizadas del documenter.

Las skills completas se leen únicamente cuando se seleccionan. Los MOCs, auditorías antiguas,
propuestas e historial son referencias, no contexto inicial.

## Fuentes de verdad

En caso de conflicto, aplica este orden y muestra la discrepancia:

1. requisitos validados y evidencia de campo;
2. especificaciones y ADR aprobados;
3. código, migraciones y pruebas;
4. documentación oficial vigente;
5. propuestas e historial;
6. conversación o memoria como contexto auxiliar.

Una conversación, inferencia o propuesta de IA nunca aprueba un requisito.

## Gobernanza y límites

- La constitución es obligatoria para decisiones de arquitectura, permisos, seguridad,
  planificación y puertas de implementación.
- Los roles canónicos viven en `agents/tesis/roles/`; `.codex/agents/` y `.opencode/agents/`
  son adaptadores del host, no fuentes paralelas.
- Un solo escritor por archivo y por worktree. Los agentes hijos reciben tarea, requisito,
  rutas permitidas y prueba esperada; no hay delegación recursiva.
- `reviewer` es read-only. `architect` solo puede registrar propuestas en rutas autorizadas.
  `implementer` modifica únicamente una tarea asignada.
- No se aprueban requisitos, decisiones ni alcance desde una conversación.
- No hagas `commit`, `push`, `merge`, `rebase`, `reset`, `clean` ni cambies la identidad Git
  sin autorización explícita del tesista.
- No guardes secretos, datos personales innecesarios ni bases locales en Git.
- No ejecutes `speckit-implement` sobre una especificación no aprobada.

## Arquitectura de producto

La aplicación futura usa Python, Django, PostgreSQL, Bootstrap 5 y plantillas MTV en un
monolito modular. La aplicación Django todavía no existe; los artefactos de diseño o laboratorio
no deben presentarse como aplicación funcional. Las reglas de autorización viven en backend y
las operaciones con varias entidades usan transacciones.

## Documentación y continuidad

- El vault es la raíz del repositorio; los documentos estables van en `docs/` y las specs en
  `specs/<id>/`.
- El estado operativo se conserva en `docs/bitacora/ESTADO-ACTIVO.md`; el detalle de pausas y
  handoffs va en `docs/bitacora/checkpoints/`.
- No sobrescribas notas aprobadas. Las propuestas usan estado `proposed` y sus rutas autorizadas.
- Antes de cerrar una tarea ejecuta verificaciones proporcionales, revisa el diff y ejecuta
  `git diff --check` cuando exista un repositorio Git.

## Host

Codex, OpenCode, Kimi, Antigravity y OpenChamber comparten estos artefactos versionados.
OpenChamber es únicamente una interfaz sobre OpenCode; agentes, comandos, permisos y perfiles
de modelo pertenecen a los mecanismos nativos de Codex/OpenCode.
