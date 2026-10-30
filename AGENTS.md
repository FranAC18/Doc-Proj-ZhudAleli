# AGENTS.md — Zhud Alelí

## Misión

Construir una aplicación web funcional, clara y verificable para la gestión organizacional
y la trazabilidad productiva del Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud.
Este archivo es el contrato corto que Codex y otros hosts descubren automáticamente; la
documentación detallada se recupera bajo demanda.

## Inicio de una tarea

1. Confirma si estás en el repositorio general (`AGENTS.md`, constitución y vault) o en
   el repositorio de la aplicación (`App-zhudaleli`). Para cambios de código, comprueba
   ambas raíces Git antes de escribir.
2. Lee [`docs/context/context-index.md`](docs/context/context-index.md) en el repositorio general.
3. Lee [`docs/bitacora/ESTADO-ACTIVO.md`](docs/bitacora/ESTADO-ACTIVO.md) en el general; antes de
   escribir, confirma rama, `HEAD`, tarea y las rutas del archivo indicado por `scope_file`.
4. Clasifica la solicitud según `task_types` en `tools/agent-routes.toml`.
5. Carga solamente el contexto indicado por esa clasificación. No leas todo `docs/`, todo
   `.specify/` ni todo el directorio de una funcionalidad por defecto.

## Recuperación selectiva

- Arquitectura o planificación: constitución, índice, arquitectura/ADR relevantes y la
  funcionalidad activa indicada por `docs/context/feature-index.md`.
- Implementación: requisito y sprint vigentes, código y pruebas; `tasks.md` y secciones
  relevantes de `spec.md` cuando existan. Contratos y modelo de datos solo si el cambio
  los toca.
- Frontend: aplicar siempre [`docs/ui/REGLAS-DISENO-INTERFACES.md`](docs/ui/REGLAS-DISENO-INTERFACES.md)
  y consultar el sistema de diseño, componentes y archivos visuales relevantes. Sus ocho reglas
  son obligatorias al diseñar, modificar o revisar interfaces; registrar lo verificado y pendiente.
- Investigación: solo las fuentes necesarias para la pregunta.
- Revisión: diff, archivos modificados, contratos, pruebas y reglas aplicables.
- Documentación: la plantilla o fuente concreta y las rutas autorizadas del documenter.

Las skills completas se leen únicamente cuando se seleccionan. Los MOCs, auditorías antiguas,
propuestas e historial son referencias, no contexto inicial.

Reutiliza lo ya leído en el mismo chat mientras siga vigente. Tras un cambio de tarea, host,
compactación o archivos, revalida Git y recupera solo el contexto faltante o afectado. Busca
con `rg` y lee secciones; si una salida se trunca, acota la consulta. Para clasificar, basta
el bloque `task_types.<tipo>` de `tools/agent-routes.toml`, sin cargar todas las rutas.
Una consulta sobre la herramienta o cuota no requiere abrir requisitos, sprints ni specs
de producto. El ahorro no reduce verificaciones, evidencia, controles de seguridad ni
sincronizaciones exigidas. Los perfiles de rutas orientan; no cambian el modelo del host.
Para implementar, buscar por ID la tarea y sus RF/HU/HT; leer solo criterios, arquitectura
y evidencia pertinentes. Sin fichas nuevas ni auditoría global previa. La [guía de lectura](docs/context/recorrido-tarea.md)
es una referencia si hay dudas, no otra lectura obligatoria en cada tarea.

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
- No se infieren aprobaciones de requisitos, decisiones, alcance ni acciones externas a partir
  de una conversación. Una instrucción explícita del tesista autoriza solo el cambio o la acción
  que nombra; los requisitos conservan su evidencia de validación.
- El tesista puede cerrar o reabrir cualquier sprint y avanzar cuando lo decida, sin acta ni
  aprobación adicional. La continuidad se anota en el estado operativo existente, sin que el
  apunte sea precondición. El cierre del periodo no marca trabajo pendiente como completado.
- No hagas `commit`, `push`, `merge`, `rebase`, `reset`, `clean` ni cambies la identidad Git
  sin autorización explícita del tesista. Para programación de la app rige la autorización
  permanente del 2026-10-29 descrita en «Repositorios y Git»; no requiere confirmación por tarea.
- No guardes secretos, datos personales innecesarios ni bases locales en Git.
- Si usas `speckit-implement` con una spec, esta debe estar aprobada. El desarrollo
  directo puede avanzar con el requisito y sprint vigentes sin exigir spec, plan,
  tareas ni checklist adicionales.

## Ritmo de trabajo del tesista y Codex

- Una idea se contrasta primero con el requisito vigente. Si precisa un comportamiento ya
  validado, se implementa una porción verificable y se actualiza solo la documentación
  afectada. No se exige rehacer pila, historias, spec y plan antes de cada cambio de código.
- Si la idea cambia un requisito, permiso o regla de negocio, se identifica la decisión
  concreta, su fuente y su impacto. Las propuestas y tareas antiguas no implementadas se
  ajustan al requisito nuevo; no bloquean por sí solas el avance. Si el cambio contradice
  una regla validada, se registra la discrepancia y se valida esa regla específica antes
  de implementarla. El resto del trabajo independiente continúa.
- La pila ordena valor y dependencias; el sprint backlog contiene solo compromisos y estado
  verificable del sprint. Las historias detallan criterios cuando cambian, sin duplicar
  el mismo texto en todos los artefactos. La edición académica se sincroniza desde las
  fuentes internas en hitos revisados, respetando su control de versiones y publicación.
- Codex implementa, prueba y revisa el diff de cada porción. La revisión por otro agente
  se reserva para decisiones o cambios de riesgo alto; la clasificación de tareas no obliga
  a convocar varios agentes para un ajuste ordinario.
- El modelo de datos se construye por módulo: mapa conceptual, propietarios y relaciones
  esenciales desde S1; tablas, restricciones y migraciones del recorrido activo en S2 y
  los sprints siguientes. Cada cambio verifica integridad y compatibilidad de datos.

## Repositorios y Git

- **Autorización permanente del tesista — 2026-10-29:** después de cada porción coherente
  de programación de la app que pase las pruebas y verificaciones aplicables y la revisión
  del diff, hacer `commit` descriptivo y `push` a su rama de trabajo en
  `FranAC18/App-zhudaleli`, sin pedir nueva confirmación. Preparar solo los cambios de esa
  tarea; excluir cambios ajenos o previos no verificados. Si no hay cambios, no crear commit.
  El mensaje explica qué se hizo y la validación, con RF y sprint reales. Si falla una
  verificación, no publicar; si falla el push, conservar el commit e informar el pendiente.
  Esta autorización no cubre Git del vault/documentación, push directo a `main`, merge,
  tags, rebase, reset, clean, force push, identidad Git ni despliegue. Una instrucción
  puntual del tesista puede suspenderla para una tarea.
- `ZhudAleli` es el repositorio general y vault: constitución, `specs/`, requisitos,
  sprints, `docs/`, `documentacion/` revisada, agentes, skills, plantillas y herramientas
  de proceso. `/app/` está ignorada y nunca se commitea aquí.
- `FranAC18/App-zhudaleli` contiene el código de producto: Django, migraciones,
  pruebas, plantillas, estáticos fuente, dependencias, configuración de ejecución/CI,
  `.gitignore` y README técnico breve. No recibe agentes, specs ni docs de proceso.
- Todo commit y push de código ocurre únicamente en la raíz Git de la app. Antes de
  cada push se verifican ruta actual, `git rev-parse --show-toplevel`, `git remote -v`,
  URL de push, rama y archivos preparados. Nunca uses `git add .` en la raíz general
  ni force push a `main`.
- Los commits de código siguen `tipo(scope): descripción [RF-XXX][SPRINT-N]` con ID
  real; se trabaja en `feature/RF-XXX-descripcion` y se integra por PR a `main`
  protegida. El cierre de un sprint con código integrado lleva tag `sprint-N` en la
  app y enlace requisito → sprint → PR/tag en la matriz general.
- Para desarrollar basta consultar en el repo general el requisito y sprint vigentes.
  La falta de documentos de proceso dentro de la app nunca bloquea un commit.
  Las decisiones materiales, permisos, pruebas y evidencias de terminación conservan
  sus controles de calidad.

## Arquitectura de producto

Al crear, modificar o revisar código, plantillas o recursos de la app, selecciona y aplica
[`zhud-aleli-codigo-legible`](.agents/skills/zhud-aleli-codigo-legible/SKILL.md).
Esta skill concreta la organización aprobada por módulo, las responsabilidades del backend,
el frontend por pantalla y las verificaciones de transición, sin autorizar traslados ajenos
a la tarea ni cambiar requisitos de negocio.

La aplicación usa Python, Django, PostgreSQL, Bootstrap 5 y plantillas MTV en un
monolito modular. Se construye por incrementos: una base técnica o laboratorio aún no
acredita funcionalidad de negocio entregada. Las reglas de autorización viven en backend y
las operaciones con varias entidades usan transacciones.

ADR-0006 y la constitución 0.2.0 confirman capas internas proporcionales: cada módulo agrupa
su responsabilidad y posee escrituras, invariantes y migraciones. La colaboración usa
operaciones públicas y lecturas autorizadas; se evitan ciclos y se conservan FK/relaciones
justificadas. `core` sigue pequeño y no se crean apps/capas vacías. Las versiones se entregan
conjuntamente por incrementos verificables, con compatibilidad y regresión de lo afectado.
La guía canónica es [`docs/architecture/ARQUITECTURA-OBJETIVO.md`](docs/architecture/ARQUITECTURA-OBJETIVO.md).
Los ejemplos genéricos de comandos/templates no rebajan las pruebas ni autorizaciones de la
constitución. Confirmar arquitectura no aprueba nuevas funcionalidades, Git ni despliegue.

## Documentación y continuidad

- Por instrucción del tesista del 2026-10-28, cada cambio relevante de alcance, criterios, prioridad o estado sincroniza requisitos, historias de usuario/técnicas afectadas, pila de producto, sprint backlog y el gestor local de tesis ágil en `http://127.0.0.1:55478/`. Conserva versiones, IDs, avances y evidencia; indica cualquier destino pendiente. Esta sincronización local no autoriza Git, gasto ni publicación al docente.

- El vault es la raíz del repositorio general. Las fuentes internas, evidencia y notas estables
  permanecen en `docs/`; las specs técnicas permanecen en `specs/<id>/`.
- `documentacion/` contiene ediciones para la entrega académica. Se versiona en el
  repositorio general solo cada archivo revisado e incorporado explícitamente.
  Cada edición identifica fecha, autor, estado, historial y fuentes aprobadas.
  Se prepara desde las fuentes internas; una copia pública no cambia por sí sola un
  requisito, decisión o spec. `analisis/` conserva trabajo interno por fecha y tema.
  `_archivo/` recibe material sustituido solo con motivo, origen y reemplazo registrados.
- Solo el contenido revisado de `documentacion/` se versiona en el repositorio general y
  puede sincronizarse con el repositorio documental del docente, mediante un clon separado
  y una vista previa de diferencias.
  Todo cambio relevante actualiza versión y control de cambios. `commit` se hace cuando
  el tesista lo solicite expresamente; publicación requiere su confirmación específica.
  Nunca se incluyen código, agentes, skills, secretos, `.env` ni evidencia interna.
- El estado operativo se conserva en `docs/bitacora/ESTADO-ACTIVO.md`; el detalle de pausas y
  handoffs va en `docs/bitacora/checkpoints/`. Mantén el estado breve: resultado vigente,
  pendientes y siguiente acción con enlaces. Un checkpoint puede servir también de resumen
  de sesión; no dupliques el relato ni generes notas por cada lectura o comando.
- No sobrescribas notas aprobadas. Las propuestas usan estado `proposed` y sus rutas autorizadas.
- Antes de cerrar una tarea ejecuta verificaciones proporcionales, revisa el diff y ejecuta
  `git diff --check` cuando exista un repositorio Git.

## Host

Codex, OpenCode, Kimi, Antigravity y OpenChamber comparten estos artefactos versionados.
OpenChamber es únicamente una interfaz sobre OpenCode; agentes, comandos, permisos y perfiles
de modelo pertenecen a los mecanismos nativos de Codex/OpenCode.
