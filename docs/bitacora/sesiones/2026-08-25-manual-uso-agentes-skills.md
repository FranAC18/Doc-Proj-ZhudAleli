---
title: Manual operativo de agentes, skills, comandos y contexto
type: manual
status: active
project: tesis-zhud-aleli
date: 2026-08-25
task_id: HARNESS-ARCH-001
phase: pre_commit
commit: pending
verified_against:
  branch: opencode/spec-001-fase-1-diseno
  head: 73e3c0f68cbb7539aaec5478a83c9e288b80e617
related:
  - "../../../AGENTS.md"
  - "../../context/context-index.md"
  - "../../context/feature-index.md"
  - "../ESTADO-ACTIVO.md"
  - "../../../tools/agent-routes.toml"
tags:
  - proyecto/tesis
  - tipo/manual
  - modulo/transversal
  - estado/activo
---

# Manual operativo de agentes, skills, comandos y contexto

## Alcance y ubicación

Este manual describe la implementación que existe en el repositorio al 2026-08-25. No
define una arquitectura futura ni convierte una propuesta en una decisión aceptada. Antes
de ejecutar una tarea, vuelve a comprobar el estado vivo de Git y
[`docs/bitacora/ESTADO-ACTIVO.md`](../ESTADO-ACTIVO.md), porque el snapshot de este documento
puede quedar obsoleto.

La ubicación preferida solicitada, `docs/00-inicio/`, no se usa aquí porque el contrato del
agente `documenter` prohíbe escribir automáticamente en esa carpeta. La nota se conserva
en `docs/bitacora/sesiones/`, una ruta permitida para documentación operativa persistente.
No se modificaron el dashboard ni los MOCs para enlazarla; por ahora este enlace directo es
la entrada estable del manual.

## Guía rápida: si quiero hacer X, hago Y

| Objetivo | Comando o invocación | Agente esperado | ¿Puede modificar? | Qué revisar |
|---|---|---|---|---|
| No sé por dónde empezar | `/route <solicitud>` | `plan` para clasificar | No | `DECISION`, `NEXT ACTION`, fase y autorización |
| Diseñar o revisar arquitectura | `/route` y después `/architect <decisión>` | `architect` | Solo propuestas en rutas autorizadas | Constitución, ADR y alcance |
| Implementar una tarea autorizada | `/route` y después `/implement <tarea>` | `implementer` | Solo la tarea y rutas asignadas | `tasks.md`, spec, código, pruebas |
| Hacer una tarea de interfaz | `/route` y después `/frontend <tarea>` | `frontend` | Solo UI asignada | Reglas UI, componentes, accesibilidad |
| Investigar sin editar | `/research <pregunta>` | `researcher` | No por defecto | Fuentes necesarias, hechos e inferencias |
| Revisar cambios | `/review <alcance>` | `reviewer` | No | Diff, criterios, pruebas y riesgos |
| Registrar sesión, checkpoint o evidencia | Invocar el agente `documenter` con la skill correspondiente | `documenter` | Solo documentación operativa permitida | Estado, evidencia real, `commit: pending` en `pre_commit` |
| Preparar un commit | Invocar `git-manager` | `git-manager` | Índice/commit solo con autorización explícita | Diff, pruebas y autorización del tesista |

Regla práctica: `/route` orienta; no ejecuta el trabajo. Si su decisión no es `READY`, no
se activa el agente ejecutor.

## 1. Conceptos básicos

### Agente

Un agente es el rol que ejecuta o revisa el trabajo. En este proyecto el contrato común vive
en `agents/tesis/roles/`. Los adaptadores de cada host describen cómo ese rol se presenta en
Codex u OpenCode, pero no deben ampliar sus permisos.

Ejemplos:

- `architect` revisa límites, datos, RBAC, transacciones, migraciones y pruebas; solo
  registra propuestas arquitectónicas autorizadas.
- `implementer` implementa una sola tarea asignada y entrega pruebas; no cambia el alcance.
- `reviewer` es read-only y reporta hallazgos; no los corrige.
- `documenter` registra sesiones, checkpoints y evidencias operativas; no aprueba requisitos
  ni decisiones.

### Skill

Una skill es un procedimiento o conocimiento especializado que el host puede cargar cuando
se selecciona. Vive en un archivo `SKILL.md`, normalmente bajo `.agents/skills/<nombre>/`.
La existencia del archivo no significa que su contenido haya sido leído en la sesión.

En este proyecto, `zhud-aleli-context` prepara el contexto mínimo de Zhud Alelí y
`zhud-aleli-documenter` define cómo registrar documentación operativa. Las skills `speckit-*`
describen flujos de especificación, planificación, tareas y análisis.

### Comando

Un comando es una plantilla invocable por nombre. Los comandos nativos de OpenCode están en
`.opencode/commands/` y reciben la solicitud mediante `$ARGUMENTS`. Un comando puede fijar un
agente y limitar el flujo, pero no convierte por sí mismo una tarea bloqueada en autorizada.

### Perfil de modelo

Un perfil de modelo es un alias de capacidad, no un identificador concreto de proveedor. Los
perfiles se declaran en `tools/agent-routes.toml`; el host selecciona el modelo real en tiempo
de ejecución. Por ejemplo, `coding_efficient` expresa capacidad de programación y uso de
herramientas, pero no significa automáticamente un modelo específico.

### `/route`

`/route` es el comando de clasificación y control previo. Su plantilla actual procesa la
solicitud en este orden:

```text
INTENT → STATE → AUTHORIZATION → ROUTING
```

No edita, no implementa, no selecciona skills automáticamente y no selecciona modelos
automáticamente. Devuelve el perfil declarado, si corresponde, con `selected: none` y
`SKILLS.selected: none`.

## 2. Mapa de configuración real

| Elemento | Para qué sirve | Quién lo usa | Descubrimiento/carga actual | Fuente canónica o adaptador | Cuándo tocarlo |
|---|---|---|---|---|---|
| `AGENTS.md` | Contrato corto de reglas, gobierno, límites y recuperación selectiva | Codex y otros hosts que descubren `AGENTS.md` | Descubrimiento automático del host en la raíz; sus enlaces se leen según la tarea | Fuente común de instrucciones del repositorio | Solo mediante cambio deliberado del contrato del proyecto |
| `agents/tesis/roles/` | Responsabilidades, límites de escritura y handoffs | Todos los hosts que implementan el arnés | Se lee cuando se activa el rol correspondiente | Fuente canónica de roles | Cuando cambia el contrato universal del rol |
| `.codex/agents/*.toml` | Adaptadores de los roles para Codex | Codex | Descubiertos por la configuración del agente; se activa el rol seleccionado, no todos como contexto de tarea | Adaptador de Codex | Cuando Codex necesita una adaptación del contrato; sin redefinir el rol |
| `.codex/config.toml` | Configuración compartida del proyecto: hilos y profundidad máxima | Codex | La consulta el host Codex | Adaptador/configuración del host | Solo al cambiar límites operativos, con revisión de seguridad |
| `.opencode/agents/*.md` | Adaptadores de agentes, permisos y modo para OpenCode | OpenCode; OpenChamber los presenta mediante su interfaz | OpenCode los descubre; el contenido del agente seleccionado entra en su ejecución | Adaptador de OpenCode | Cuando cambia la forma de ejecutar un rol en OpenCode |
| `.opencode/commands/*.md` | Plantillas de `/route`, `/architect`, `/implement`, `/frontend`, `/review` y `/research` | OpenCode | OpenCode descubre los comandos del proyecto; solo se usa la plantilla invocada | Adaptador de comandos OpenCode | Cuando cambia el flujo de invocación, no para aprobar alcance |
| `.agents/rules/` | Reglas de contexto y continuidad para hosts que soportan esta convención | Principalmente el adaptador de reglas de Antigravity | Se cargan según el host; el repositorio no demuestra que Codex/OpenCode las inyecten automáticamente como reglas nativas | Adaptador de host | Solo al adaptar un host, manteniendo la precedencia de `AGENTS.md` |
| `.agents/skills/` | Procedimientos especializados y skills Spec Kit/Zhud Alelí | Hosts que descubren skills | El catálogo puede estar disponible; el `SKILL.md` completo se lee cuando la skill es seleccionada | Procedimiento compartido, no fuente de requisitos | Cuando se crea o actualiza una skill, con alcance explícito |
| `tools/agent-routes.toml` | Mapea tipo de tarea → agente → perfil de capacidad → revisión | `/route`, agentes y validadores | Es contexto operativo requerido; no contiene una automatización que ejecute el agente | Fuente ejecutable del routing declarativo | Al cambiar categorías, agentes, perfiles o nivel de revisión |
| `docs/context/context-index.md` | Define el contexto mínimo y lo que es referencia | Coordinador y agentes | Se lee al inicio según el contrato; funciona como índice, no como cargador mágico | Índice operativo | Cuando cambia la estrategia de recuperación |
| `docs/context/feature-index.md` | Indica feature activa, fase, artefactos y recuperación por tipo de tarea | `/route` y tareas de la feature | Se consulta antes de abrir artefactos de una spec | Índice de funcionalidad | Cuando cambia la feature activa o su fase |
| `docs/bitacora/ESTADO-ACTIVO.md` | Puntero de continuidad: tarea, fase, rama, `HEAD`, rutas y próximo paso | Todos los hosts antes de trabajar | Se lee como estado operativo mínimo; no debe editarse para forzar una tarea | Fuente de estado operativo | Solo para registrar estado real, nunca para autorizar artificialmente |
| `.specify/memory/constitution.md` | Principios obligatorios de ingeniería y puertas de decisión | Arquitectura, planificación, permisos, seguridad y skills Spec Kit aplicables | Se recupera según el tipo de tarea; no se debe leer todo `.specify/` por defecto | Fuente normativa del proyecto | Solo mediante proceso explícito de constitución |
| `docs/00-inicio/` y MOCs | Navegación humana, dashboard y referencias | Personas y agentes bajo demanda | No forman parte del contexto inicial normal según `context-index.md` | Referencia/navegación | No usarlos para sustituir el estado o las fuentes canónicas |
| `specs/<id>/` | Requisitos, plan, tareas y artefactos de una funcionalidad | Agente según tarea | Se abre selectivamente después de `feature-index.md` | Fuente de diseño de la feature, según estado | Solo en la tarea y fase autorizadas |
| `tools/agent-lab/` | Laboratorio separado para modelos, memoria, herramientas y persistencia | Pruebas del laboratorio | No carga automáticamente agentes TOML ni skills del repositorio | Laboratorio, no memoria de Codex/OpenCode | Solo al trabajar específicamente en el laboratorio |
| `.obsidian/` | Estado visual de Obsidian: grafo, workspace y vistas | Obsidian | No es contexto operativo normal | Configuración visual, no fuente de verdad | Solo para la interfaz de Obsidian |

La configuración canónica de responsabilidades está en `agents/tesis/roles/`. `.codex/agents/`
y `.opencode/agents/` son adaptadores. OpenChamber no es un tercer origen de configuración:
es una interfaz sobre el runtime de OpenCode.

## 3. Agente frente a skill: ejemplos del proyecto

| Elemento | Responde a | Ejemplo | Error que se debe evitar |
|---|---|---|---|
| AGENT | ¿Quién ejecuta o revisa? | `implementer` implementa T013 si está autorizada | Pedir a `reviewer` que arregle un hallazgo |
| SKILL | ¿Qué procedimiento especializado se aplica? | `zhud-aleli-documenter` registra evidencia pre-commit | Confundir la existencia de `SKILL.md` con carga efectiva |
| COMMAND | ¿Cómo invoco el flujo? | `/route` o `/review` | Suponer que un comando encadena automáticamente todos los agentes |
| MODEL PROFILE | ¿Qué capacidad debe tener el modelo? | `reasoning_max` para revisión de alto riesgo | Tratar el alias como un modelo concreto |
| ROUTE | ¿Qué intención, estado, autorización y agente corresponden? | `INTENT → STATE → AUTHORIZATION → ROUTING` | Enrutar antes de comprobar la fase |

## 4. Comandos disponibles hoy

### `/route`

Archivo: `.opencode/commands/route.md`.

Se invoca con `/route <solicitud>`. Consulta `tools/agent-routes.toml`, los índices de
contexto, el estado activo y, cuando hace falta, la feature. Su salida tiene estas secciones:

```text
INTENT
STATE
AUTHORIZATION
ROUTING
CONTEXT
DECISION
NEXT ACTION
BLOCKER
```

`requested_agent` es el ejecutor que realizaría la acción si estuviera autorizada.
`recommended_agent` es quien debe actuar ahora. Si hay bloqueo de fase o autorización, el
ejecutor no se activa y `execution` debe ser `prohibited`.

### `/architect`

Archivo: `.opencode/commands/architect.md`; agente: `architect`.

Produce análisis o propuestas arquitectónicas. No implementa código ni convierte una
recomendación en decisión aceptada. Solo puede registrar propuestas en las rutas autorizadas
por el contrato del rol.

### `/implement`

Archivo: `.opencode/commands/implement.md`; agente: `implementer`.

Ejecuta una tarea previamente especificada. Antes de editar debe identificar ID de tarea,
requisito, rutas permitidas, archivos relevantes y prueba esperada. No cambia arquitectura,
alcance, dashboard, matriz ni estado global. No hace commit ni push.

### `/frontend`

Archivo: `.opencode/commands/frontend.md`; agente: `frontend`.

Ejecuta una tarea de interfaz ya asignada. Puede escribir únicamente en `design/`,
`templates/`, `static/` o las rutas de plantilla/static de la app asignada. Revisa móvil,
teclado, foco, contraste AA, estados y mensajes recuperables. No cambia backend, modelos,
permisos ni rutas de negocio sin reasignación explícita.

### `/research`

Archivo: `.opencode/commands/research.md`; agente: `researcher`.

Investiga una pregunta concreta y separa hechos, inferencias, limitaciones y preguntas
abiertas. Es read-only por defecto. Solo registra una propuesta documental si el coordinador
lo solicita y la ruta es autorizada.

### `/review`

Archivo: `.opencode/commands/review.md`; agente: `reviewer`.

Revisa diff, archivos modificados, criterios, contratos, pruebas y reglas relevantes. Reporta
hallazgos por severidad, pruebas no ejecutadas, dudas y riesgos residuales. No edita y el
adaptador actual tampoco le permite ejecutar shell.

### Agentes sin comando de proyecto equivalente

El inventario actual no contiene `.opencode/commands/documenter.md`,
`.opencode/commands/requirements.md`, `.opencode/commands/ux.md` ni
`.opencode/commands/git-manager.md`. Esos roles existen en `agents/tesis/roles/`,
`.opencode/agents/` y/o `.codex/agents/`, pero se invocan seleccionando el agente en el host
correspondiente o mediante el coordinador. No se debe inventar un slash command que el
repositorio no define.

Para `documenter`, además, se debe cargar la skill `zhud-aleli-documenter` y especificar la
fase documental. En `pre_commit` se registra `commit: pending`; en `post_commit` se exige el
hash real devuelto por `git-manager`.

## 5. Cómo funciona `/route`: INTENT → STATE → AUTHORIZATION → ROUTING

### INTENT

Identifica la acción, objetivo, feature, requisito o tarea y el `task_type` de
`tools/agent-routes.toml`. Si no se puede saber qué debe hacerse, devuelve
`NEEDS_CLARIFICATION` y no finge que existe una tarea autorizada.

### STATE

Separa dos estados:

- Estado operativo: `task_id`, fase de la tarea, rama, `HEAD`, rutas permitidas y próximos
  pasos en `ESTADO-ACTIVO.md`.
- Estado de la feature: estado de spec, plan, tareas, fase y dependencias en
  `docs/context/feature-index.md` y sus artefactos.

Si Git, el estado documentado, un checkpoint o el índice de feature se contradicen, la
decisión es `STATE_DRIFT`. No se corrige el drift editando el puntero a conveniencia.

### AUTHORIZATION

Comprueba spec, plan, dependencias, constitución y validaciones humanas. Una solicitud puede
ser técnicamente válida y seguir bloqueada por fase. Una conversación no aprueba requisitos,
decisiones ni alcance.

### ROUTING

Solo después de Intent, State y Authorization se consulta el tipo de tarea en
`tools/agent-routes.toml`. El archivo indica agente, riesgo, perfil declarado, contexto,
revisión y delegación. Si `tasks.md` identifica explícitamente al escritor, esa asignación
prevalece para la tarea concreta.

### Decisiones actuales

| Decisión | Cuándo aparece | ¿Ejecutar? |
|---|---|---|
| `READY` | Intención clara, tarea existente, fase abierta, dependencias satisfechas y autorización suficiente | Sí, después de revisar el contexto mínimo |
| `BLOCKED_BY_PHASE` | La acción pertenece a una fase posterior o falta una dependencia de fase | No; desbloquear primero |
| `BLOCKED_BY_AUTHORIZATION` | Falta aprobación humana, decisión confirmada o validación organizacional | No; registrar la aprobación real |
| `STATE_DRIFT` | Estado documentado y estado real no coinciden | No; reconciliar fuentes y volver a enrutar |
| `NEEDS_CLARIFICATION` | Falta objetivo, tarea, alcance o acción identificable | No; aclarar la solicitud |
| `OUT_OF_SCOPE` | No existe requisito, spec o tarea que autorice la acción | No; solicitar definición formal, no improvisar |
| `SOURCE_CONFLICT` | No es un token de decisión implementado en la plantilla actual de `/route` | No; reportar la discrepancia según la jerarquía de fuentes |

`SOURCE_CONFLICT` merece atención especial: `AGENTS.md` ordena mostrar las discrepancias y
`context-index.md` ordena detener la decisión si dos fuentes difieren, pero la salida actual
de `/route` no enumera `SOURCE_CONFLICT`. Por tanto, no debe describirse como una decisión
automática existente. El operador debe parar, identificar las fuentes enfrentadas y dirigir
la aclaración a `requirements`, `architect` o al coordinador según el tema.

### Qué devuelve cuando una acción válida está bloqueada

Ejemplo conceptual para una implementación de fase posterior:

```text
INTENT:
  action: implementar T013
  task_type: implementation

AUTHORIZATION:
  result: blocked
  gate: validación de Fase 1 pendiente
  missing_condition: completar T007/T011 y confirmar T012

ROUTING:
  requested_agent: implementer
  recommended_agent: coordinator
  model_profile:
    declared: coding_efficient
    selected: none
  skills:
    selected: none
  execution: prohibited

DECISION:
  blocked_by_phase

NEXT ACTION:
  Registrar las validaciones de diseño exigidas, confirmar T012, conservar la evidencia en
  el checkpoint autorizado y volver a ejecutar /route para T013.

BLOCKER:
  La fase actual todavía no habilita la inicialización de Django.
```

`NEXT ACTION` debe ser concreta, verificable e incluir la evidencia que falta. “Esperar
aprobación” sin decir quién, qué se valida, dónde se registra y cuándo volver a enrutar no
es una respuesta operativa suficiente.

## 6. Contexto: qué se carga y qué se descubre

### Contexto mínimo obligatorio

| Fuente | Momento | Qué aporta |
|---|---|---|
| `AGENTS.md` | Inicio de una tarea en un host que lo descubre | Reglas no negociables y límites |
| `docs/bitacora/ESTADO-ACTIVO.md` | Inicio y comprobación de continuidad | Tarea, fase, rama, `HEAD`, rutas y próximo paso |
| `tools/agent-routes.toml` | Clasificación/routing | Tipo de tarea, agente, perfil, revisión y delegación |
| `docs/context/context-index.md` | Recuperación contextual | Qué leer siempre, por tipo y solo como referencia |
| `docs/context/feature-index.md` | Cuando existe una feature activa | Estado y puerta de la funcionalidad antes de abrir specs |
| Constitución | Arquitectura, planificación, permisos, seguridad y skills que la exijan | Principios obligatorios |

Este conjunto no significa que todo el repositorio se copie al prompt. El índice define una
recuperación selectiva: se leen secciones y archivos relevantes, no todas las specs, todos
los MOCs ni todas las skills.

### Contexto bajo demanda

- Arquitectura/planning: constitución, requisitos validados, arquitectura/ADR relevantes y
  la feature activa.
- Implementación: `tasks.md`, tarea asignada, secciones relevantes de `spec.md`, código y
  pruebas; `data-model.md` y contratos solo si la tarea los toca.
- Frontend: reglas UI, sistema de diseño, componentes, assets y tarea asignada.
- Investigación: solo las fuentes necesarias para la pregunta.
- Revisión: diff, archivos modificados, criterios, contratos, pruebas y reglas aplicables.
- Documentación: fuente concreta, plantilla, estado operativo y skill seleccionada.

### Referencia, no contexto normal

`README.md`, `ONBOARDING-IA.md`, notas antiguas, auditorías fechadas, checkpoints
completados, MOCs, configuración visual de `.obsidian/` y el laboratorio
`tools/agent-lab/` sirven para navegación o consulta, pero `context-index.md` no los incluye
en el contexto inicial normal.

### Cómo comprobar qué contexto intervino

No hay un registro único en el repositorio que enumere automáticamente todos los tokens o
todos los archivos efectivamente enviados al modelo. La comprobación práctica es:

1. Leer la salida de `/route` y revisar `CONTEXT.required` y `CONTEXT.excluded`.
2. Confirmar que el agente nombró o consultó la tarea, la spec, las reglas y las pruebas que
   corresponden al tipo de trabajo.
3. En OpenCode, ejecutar `opencode --pure agent list` para comprobar agentes descubiertos y
   `opencode --pure debug config` para comprobar comandos, plantillas y permisos registrados.
4. No interpretar `debug config` como prueba de que cada documento entró en el prompt: valida
   configuración, no la recuperación completa de contexto de una ejecución.
5. Para una skill, verificar el nombre seleccionado y la lectura de su `SKILL.md`. Un nombre
   visible en el catálogo solo demuestra descubrimiento, no carga del contenido.
6. Comparar rama y `HEAD` actuales con `ESTADO-ACTIVO.md`; si difieren, detenerse con
   `STATE_DRIFT`.

## 7. Skills disponibles y uso correcto

### Dónde están

Las skills del proyecto están en `.agents/skills/`. Actualmente se observan:

- Spec Kit: `speckit-analyze`, `speckit-checklist`, `speckit-clarify`, `speckit-constitution`,
  `speckit-converge`, `speckit-implement`, `speckit-plan`, `speckit-specify`, `speckit-tasks`
  y `speckit-taskstoissues`.
- Zhud Alelí: `zhud-aleli-context`, `zhud-aleli-documenter`, `zhud-aleli-git-manager` y
  `zhud-aleli-handoff`.

Cada una tiene un `SKILL.md`. El catálogo de skills puede ser descubierto por el host, pero
la instrucción completa se debe leer únicamente cuando esa skill fue seleccionada. Esto
reduce contexto innecesario y mantiene separado el procedimiento del rol ejecutor.

### Cuándo se cargan

- `zhud-aleli-context`: al iniciar una sesión o cambiar de host/modelo, según su contrato.
- `zhud-aleli-documenter`: al registrar documentación operativa después de pruebas y
  revisión, con fase `pre_commit` o `post_commit`.
- `zhud-aleli-git-manager`: al revisar o preparar un commit; exige autorización explícita.
- `zhud-aleli-handoff`: al persistir estado para cambiar de Codex, OpenCode, Antigravity u
  OpenChamber.
- `speckit-*`: solo cuando el flujo concreto de especificación, plan, tareas, análisis o
  implementación se selecciona.

### Qué no ocurre hoy

`/route` no selecciona ni ejecuta skills. Su salida exige `SKILLS: selected: none`. El usuario
o el agente coordinador debe decidir la skill apropiada y cargar su `SKILL.md`. No se debe
afirmar “se ejecutó la skill” solo porque el directorio existe o aparece en un catálogo.

## 8. Perfiles de modelo

Los cinco perfiles están definidos en `tools/agent-routes.toml`:

| Perfil | Capacidad declarada | Usos de routing actuales |
|---|---|---|
| `reasoning_max` | razonamiento, contexto largo, salida estructurada | arquitectura, planificación y revisión |
| `coding_efficient` | programación, uso de herramientas, salida estructurada | implementación y debugging |
| `frontend_strong` | programación, revisión UI y accesibilidad | frontend |
| `research_efficient` | investigación, contexto largo y citas | research y requirements |
| `documentation_economy` | escritura y salida estructurada | documentation |

Todos tienen `selection = "host-selected"` y `fallback = "host-selected"`. Las entradas
`routes.*` conservan compatibilidad declarativa entre Codex y OpenCode, pero solo transportan
perfiles; no fijan IDs concretos de modelos ni convierten a OpenChamber en host.

Por eso `/route` puede decir `declared: coding_efficient`, pero debe decir también
`selected: none`. La selección del modelo real, la disponibilidad, cuota y proveedor siguen
siendo una decisión del runtime/usuario. El laboratorio `tools/agent-lab/` tiene su propia
configuración y no representa la selección de modelos de Codex/OpenCode.

## 9. OpenChamber y OpenCode

La separación operativa es:

```text
OpenChamber = interfaz visual
OpenCode    = runtime y orquestación de agentes/comandos
Repositorio = fuente versionada de contratos, adaptadores, rutas y contexto
```

OpenChamber puede mostrar o ejecutar una sesión de OpenCode, pero no es fuente de verdad para
roles, permisos, comandos, modelos ni estado. La configuración que debe permanecer en el
repositorio está en `AGENTS.md`, `agents/tesis/roles/`, `.opencode/`, `.codex/`, `.agents/`,
`tools/`, `docs/context/` y la bitácora según el tipo de información.

El cambio entre Codex, OpenCode, Antigravity y OpenChamber no depende del historial privado
de la conversación. Se conserva mediante archivos versionados y checkpoints. El host que
continúa debe leer el último estado persistido y comprobar rama, `HEAD` y rutas.

## 10. Flujo completo y estado real

```text
PROMPT
  ↓ [IMPLEMENTADO: si el usuario invoca /route]
INTENT
  ↓ [IMPLEMENTADO en la plantilla de /route]
STATE
  ↓ [IMPLEMENTADO en la plantilla de /route]
AUTHORIZATION
  ↓ [IMPLEMENTADO en la plantilla de /route]
ROUTING
  ↓ [IMPLEMENTADO como recomendación declarativa]
AGENT
  ↓ [ACTIVACIÓN MANUAL: comando o selección del host]
CONTEXT
  ↓ [RECUPERACIÓN SELECTIVA POR PROTOCOLO; no hay cargador universal de todo el vault]
EXECUTION
  ↓ [MANUAL Y SUJETA A PERMISOS, FASE Y TAREA]
REVIEW
  ↓ [ROL Y REVISIÓN DEFINIDOS; invocación separada]
HANDOFF/COMMIT
    [MANUAL; documenter y git-manager tienen puertas distintas]
```

La presencia de una etapa en el diseño no implica automatización. En particular, el routing
actual no activa automáticamente al agente, no carga automáticamente una skill elegida, no
elige automáticamente el modelo real, no delega recursivamente y no encadena ejecución y
revisión sin una nueva invocación.

## 11. Ejemplos de uso

### 1. “Quiero diseñar una arquitectura”

- Prompt: `Quiero decidir los límites de accounts y su autorización backend.`
- Comando recomendado: `/route Quiero decidir los límites de accounts...`; después
  `/architect Quiero revisar los límites...`.
- Agente esperado: `architect`.
- Contexto mínimo: constitución, `AGENTS.md`, `context-index.md`, `feature-index.md`, spec y
  ADR relevantes.
- ¿Se puede ejecutar?: Sí para producir una propuesta; no para modificar código o aprobar
  una decisión.
- Observar: `task_type: architecture`, perfil declarado `reasoning_max`, revisión requerida y
  rutas de propuesta autorizadas.
- Después: entregar la propuesta al coordinador y solicitar decisión humana si corresponde.

### 2. “Quiero implementar una tarea autorizada”

- Prompt: `Implementa T013 de SPEC-001, solo en las rutas asignadas, con la prueba indicada.`
- Comando recomendado: ejecutar `/route` primero y solo con `READY` usar
  `/implement T013 ...`.
- Agente esperado: `implementer`.
- Contexto mínimo: `tasks.md`, T013, spec relevante, archivos relacionados y prueba esperada.
- ¿Se puede ejecutar?: Solo si `/route` confirma fase abierta, dependencias y autorización.
- Observar: `execution: allowed`, `requested_agent: implementer`, rutas y criterios exactos.
- Después: ejecutar pruebas proporcionales, invocar `/review` y documentar el resultado.

### 3. “Quiero hacer una tarea frontend”

- Prompt: `Construye la pantalla de acceso de la tarea asignada con el sistema visual actual.`
- Comando recomendado: `/route ...`; después `/frontend ...`.
- Agente esperado: `frontend`.
- Contexto mínimo: tarea asignada, `docs/ui/SISTEMA-DISENO.md`, componentes/assets relevantes,
  criterios de accesibilidad y feature index.
- ¿Se puede ejecutar?: Sí solo con tarea UI asignada y rutas permitidas.
- Observar: que no se incluyan modelos, permisos, rutas backend ni toda la spec.
- Después: revisar móvil, teclado, foco, contraste, estados y pasar a `reviewer`.

### 4. “Quiero investigar algo sin modificar archivos”

- Prompt: `Investiga qué alternativa satisface la restricción técnica X y cita las fuentes.`
- Comando recomendado: `/research Investiga ...`.
- Agente esperado: `researcher`.
- Contexto mínimo: pregunta y solo las fuentes necesarias.
- ¿Se puede ejecutar?: Sí; es read-only por defecto.
- Observar: separación entre hechos, inferencias, limitaciones y preguntas abiertas.
- Después: usar el informe como insumo; no convertirlo automáticamente en requisito o ADR.

### 5. “Quiero revisar cambios”

- Prompt: `Revisa el diff de la tarea actual sin modificar archivos.`
- Comando recomendado: `/review Revisa el diff ...`.
- Agente esperado: `reviewer`.
- Contexto mínimo: diff, archivos modificados, criterios, contratos, pruebas y reglas
  relevantes.
- ¿Se puede ejecutar?: Sí; no modifica archivos.
- Observar: hallazgos por severidad, evidencia, pruebas no ejecutadas y riesgos residuales.
- Después: el coordinador decide las correcciones; el reviewer no las aplica.

### 6. “Quiero implementar algo que actualmente está bloqueado”

- Prompt: `Implementa T013, inicializar Django para SPEC-001.`
- Comando recomendado: `/route Implementa T013 ...`.
- Agente esperado: `requested_agent: implementer`; `recommended_agent: coordinator` mientras
  falte la puerta de fase.
- Contexto mínimo: `feature-index.md`, `tasks.md` (T007, T011, T012, T013), estado activo y
  evidencias de validación.
- ¿Se puede ejecutar?: No en el estado documentado de este manual. SPEC-001 sigue en diseño
  sin Django y T013 depende de T007/T011 → T012.
- Observar: `BLOCKED_BY_PHASE`, `execution: prohibited`, `skills.selected: none` y
  `model_profile.selected: none`.
- Después: registrar las validaciones humanas y el checkpoint exigido, confirmar T012 y volver
  a ejecutar `/route`. No activar `implementer` para saltarse la puerta.

### 7. “Hay dos fuentes de verdad contradictorias”

- Prompt: `La spec y el estado activo describen fases distintas; determina qué hacer.`
- Comando recomendado: `/route ...` para detectar el problema, seguido de aclaración a
  `requirements`, `architect` o el coordinador según el contenido.
- Agente esperado: no ejecutar un implementer; `recommended_agent` debe resolver la fuente
  aplicable.
- Contexto mínimo: las dos fuentes completas en la sección conflictiva, jerarquía de
  `AGENTS.md`, estado y evidencia relacionada.
- ¿Se puede ejecutar?: No hasta reconciliar el conflicto.
- Observar: la salida actual no tiene `SOURCE_CONFLICT` como decisión formal; debe reportarse
  la discrepancia sin resolverla silenciosamente y puede terminar en `STATE_DRIFT` o
  `NEEDS_CLARIFICATION`.
- Después: registrar la aclaración o decisión por el mecanismo autorizado y volver a enrutar.

### 8. “No sé qué agente debería usar”

- Prompt: `No sé qué agente usar; quiero saber si esta tarea es de diseño, implementación o
  revisión.`
- Comando recomendado: `/route No sé qué agente usar...`.
- Agente esperado: `plan` para clasificar y luego el agente asociado al `task_type`.
- Contexto mínimo: objetivo, feature, requisito/tarea si existe y fase actual.
- ¿Se puede ejecutar?: `/route` sí; la acción final solo si la decisión queda `READY`.
- Observar: `task_type`, `requested_agent`, `recommended_agent`, contexto requerido y exclusiones.
- Después: seguir únicamente `NEXT ACTION`; no elegir el agente por intuición si existe un
  bloqueo de fase o autorización.

## 12. Continuidad entre sesiones

### Qué se conserva

1. `docs/bitacora/ESTADO-ACTIVO.md` conserva el puntero corto: tarea activa, fase, rama,
   `HEAD`, rutas permitidas, pruebas, bloqueos y próximo paso.
2. `docs/bitacora/checkpoints/` conserva detalle de pausas, handoffs y validaciones. La skill
   `zhud-aleli-handoff` está diseñada para persistir el estado entre Codex, OpenCode,
   Antigravity y OpenChamber.
3. `docs/bitacora/sesiones/` conserva objetivos, contexto revisado, trabajo realizado,
   propuestas, errores y próximo paso.
4. `docs/evidence/` conserva pruebas y validaciones reproducibles o anonimizadas.
5. Git conserva archivos y commits, pero no reemplaza el estado operativo ni decide qué
   cambios pertenecen a una tarea.

### Qué no se debe asumir que se conserva

- La conversación privada o la memoria interna del modelo no es fuente de verdad.
- Un cambio de host no transfiere automáticamente el prompt anterior.
- Un checkpoint completado no entra automáticamente en el contexto inicial.
- Que una skill o agente aparezca en el catálogo no significa que se haya cargado.
- Que un perfil aparezca en `agent-routes.toml` no significa que el modelo real haya sido
  seleccionado.

El estado actual verificado para este manual es: tarea `HARNESS-ARCH-001`, fase operativa
`implementation-and-validation`, branch `opencode/spec-001-fase-1-diseno`, `HEAD`
`73e3c0f68cbb7539aaec5478a83c9e288b80e617`, y `last_handoff: null`. Para la feature activa,
`SPEC-001` está `confirmed`, el plan está `approved`, las tareas están `planned` y la fase
continúa siendo diseño del sistema, todavía sin Django.

## 13. Reglas de “no hacer”

- No invocar `implementer` o `frontend` cuando `/route` indique bloqueo.
- No modificar `ESTADO-ACTIVO.md` para hacer parecer que una fase ya está autorizada.
- No resolver en silencio una contradicción entre spec, estado, ADR, evidencia o código.
- No asumir que una skill se cargó solo porque existe en `.agents/skills/`.
- No asumir que un perfil de modelo equivale a un modelo o proveedor concreto.
- No usar OpenChamber como fuente de verdad de configuración.
- No hacer que todos los agentes lean todo el vault; seguir `context-index.md` y
  `feature-index.md`.
- No leer automáticamente todos los artefactos de una spec cuando la tarea no los necesita.
- No hacer commit, push, merge, rebase, reset o clean sin la autorización que corresponda.
- No usar una conversación, inferencia o propuesta de IA como aprobación de requisito,
  decisión o alcance.
- No presentar un diseño, laboratorio o artefacto de spec como si fuera la aplicación Django
  funcional; la aplicación todavía no existe.

## 14. Automatizaciones todavía NO implementadas

Estas capacidades no deben describirse como actuales ni implementarse desde este manual:

1. Selección automática de skills según la intención.
2. Selección automática del modelo concreto a partir del perfil.
3. Delegación automática entre agentes y encadenamiento recursivo.
4. Transferencia automática de una sesión entre OpenCode, Codex y Antigravity.
5. Recuperación automática avanzada de contexto basada en relevancia o memoria semántica.
6. Ejecución automática de `/route → agente → review`.
7. Resolución automática de conflictos entre fuentes de verdad.

Hoy esas funciones se realizan mediante invocaciones explícitas, permisos del host, índices
versionados, revisión humana y checkpoints.

## 15. Fuentes verificadas y límites de verificación

La redacción se contrastó con:

- [`AGENTS.md`](../../../AGENTS.md), contrato corto y jerarquía de fuentes.
- [`agents/tesis/roles/`](../../../agents/tesis/roles/), contratos canónicos de roles.
- [`.codex/agents/`](../../../.codex/agents/) y [`.codex/config.toml`](../../../.codex/config.toml),
  adaptadores y límites de Codex.
- [`.opencode/agents/`](../../../.opencode/agents/) y
  [`.opencode/commands/`](../../../.opencode/commands/), agentes y comandos registrados para
  OpenCode.
- [`.agents/rules/`](../../../.agents/rules/) y [`.agents/skills/`](../../../.agents/skills/),
  reglas y procedimientos disponibles.
- [`tools/agent-routes.toml`](../../../tools/agent-routes.toml), routing declarativo y perfiles.
- [`docs/context/context-index.md`](../../context/context-index.md) y
  [`docs/context/feature-index.md`](../../context/feature-index.md), recuperación selectiva.
- [`docs/bitacora/ESTADO-ACTIVO.md`](../ESTADO-ACTIVO.md), estado operativo.
- [`docs/00-inicio/moc-agentes-y-skills.md`](../../00-inicio/moc-agentes-y-skills.md),
  mapa de navegación y relación entre capas.
- [`docs/architecture/CONTRATO-UNIVERSAL-ORQUESTADORES.md`](../../architecture/CONTRATO-UNIVERSAL-ORQUESTADORES.md)
  y [`docs/architecture/RUTAS-MODELOS-IA.md`](../../architecture/RUTAS-MODELOS-IA.md),
  separación de hosts, rutas y perfiles.

Verificaciones realizadas para este manual:

- `opencode --version` y `opencode --pure agent list`: OpenCode reconoce los agentes del
  proyecto.
- `opencode --pure debug config`: los comandos del proyecto, la plantilla vigente de
  `/route` y sus permisos se registran en la configuración efectiva.
- Inspección read-only de rutas, índices, estado, roles, adaptadores y skills.
- Comprobación de que `SOURCE_CONFLICT` no aparece como decisión en la plantilla actual de
  `/route`; se documenta como protocolo de parada, no como automatización.

No se verificó un registro de tokens del prompt ni una traza universal que permita demostrar
qué archivos exactos entraron en cada ejecución concreta. Por eso este manual distingue
“descubierto”, “requerido por protocolo”, “seleccionado” y “efectivamente cargado”.

## Próximo paso operativo

Mantener este manual como referencia de uso mientras se conserve la implementación descrita.
Si cambian comandos, agentes, perfiles, índices o reglas de carga, actualizar esta nota en
una nueva revisión documental con evidencia real; no usarla para introducir esas
automatizaciones.
