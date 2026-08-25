---
description: Clasifica una solicitud separando intención, estado, autorización de fase y routing sin implementar.
agent: plan
---

Clasifica la solicitud siguiente usando `tools/agent-routes.toml`,
`docs/context/context-index.md`, `docs/context/feature-index.md` y
`docs/bitacora/ESTADO-ACTIVO.md`.

Tu responsabilidad termina en clasificar, comprobar autorización y recomendar el siguiente
paso. No edites archivos, no ejecutes comandos de modificación, no selecciones skills, no
selecciones modelos y no comiences la implementación. Puedes hacer inspecciones read-only de
Git o leer archivos relevantes si son necesarias para comprobar el estado.

Solicitud: $ARGUMENTS

Procesa la solicitud estrictamente en este orden:

1. **INTENT**: identifica la acción, objetivo, feature, requisito o tarea y clasifica el
   `task_type` usando las categorías existentes. Si faltan datos para identificar el objetivo,
   devuelve `NEEDS_CLARIFICATION` y no continúes como si existiera una tarea.
2. **STATE**: determina el estado operativo y el estado de la feature por separado. Usa el
   `task_id`, fase, rama y `HEAD` documentados; si Git contradice el estado o no existe una
   confirmación suficiente, devuelve `STATE_DRIFT`.
3. **AUTHORIZATION**: comprueba si la acción está permitida por el estado de la spec, el plan,
   las dependencias y las puertas de la constitución. Una acción puede ser válida y aun así
   estar bloqueada por fase o aprobación. Nunca conviertas una conversación en aprobación.
4. **ROUTING**: solo después de evaluar autorización, determina el agente recomendado según
   `tools/agent-routes.toml` y el escritor explícito de `tasks.md` cuando exista.

Distingue siempre:

- `requested_agent`: agente que ejecutaría la acción solicitada si estuviera autorizada.
- `recommended_agent`: agente que debe actuar ahora.

Cuando la acción esté bloqueada, el `requested_agent` puede ser `implementer` o `frontend`,
pero el `recommended_agent` debe ser normalmente `coordinator`, `architect`, `ux` o
`requirements`, según la condición que falte. El agente ejecutor no debe activarse.

Usa estas decisiones:

- `READY`: intención identificable, tarea existente, fase abierta, dependencias satisfechas y
  autorización suficiente.
- `BLOCKED_BY_PHASE`: intención válida, pero la tarea pertenece a una fase posterior o una
  dependencia de fase aún no está completa.
- `BLOCKED_BY_AUTHORIZATION`: falta aprobación humana, decisión confirmada o validación de la
  organización.
- `STATE_DRIFT`: estado documentado, Git, checkpoint o feature no coinciden.
- `NEEDS_CLARIFICATION`: no se puede identificar acción, objetivo, tarea o alcance.
- `OUT_OF_SCOPE`: no existe requisito, spec o tarea aprobada que autorice la solicitud.

Para `BLOCKED_BY_PHASE` o `BLOCKED_BY_AUTHORIZATION`, `NEXT ACTION` debe ser una acción concreta
de desbloqueo, incluir la evidencia que debe registrarse y ordenar volver a ejecutar `/route`
después de cumplirla. No debe decir simplemente “esperar aprobación”.

No implementes todavía selección automática de skills ni modelos. En `MODEL PROFILE` informa,
si corresponde, únicamente el perfil declarado en `tools/agent-routes.toml`; indica siempre
`selected: none`. En `SKILLS` indica siempre `selected: none`.

Devuelve exactamente estas secciones y no agregues otras:

INTENT:
  action:
  target:
  feature:
  task_type:

STATE:
  project_task:
  feature_status:
  phase:
  branch:
  head:
  state_status:

AUTHORIZATION:
  result: ready | blocked
  gate:
  evidence:
  missing_condition:

ROUTING:
  requested_agent:
  recommended_agent:
  model_profile:
    declared:
    selected: none
  skills:
    selected: none
  execution: allowed | prohibited
  review:
  delegation:

CONTEXT:
  required:
  excluded:

DECISION:
  ready | blocked_by_phase | blocked_by_authorization |
  state_drift | needs_clarification | out_of_scope

NEXT ACTION:
  acción concreta y verificable

BLOCKER:
  motivo preciso o none

Regla final: si la decisión no es `READY`, `execution` debe ser `prohibited`; no propongas
activar el agente ejecutor como siguiente paso inmediato. Si la solicitud mezcla tipos, elige
el tipo dominante, explica la secuencia en `NEXT ACTION` y detente.
