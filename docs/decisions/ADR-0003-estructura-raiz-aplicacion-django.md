---
title: ADR-0003 — Estructura raíz de la aplicación Django y agentes
type: decision
status: accepted
date: 2026-07-25
decision_id: ADR-0003
accepted_by: tesista
accepted: 2026-07-25
sprint: s1
module: transversal
related:
  - "[[proposals/2026-07-25-estructura-raiz-aplicacion-django]]"
  - "[[../architecture/ARQUITECTURA-OBJETIVO]]"
  - "[[../architecture/PLAN-DESDE-CERO]]"
  - "[[../architecture/FLUJO-MULTIAGENTE]]"
  - "[[../../specs/001-acceso-usuarias-internas/spec]]"
  - "[[../evidence/fase-i/2026-07-25-confirmacion-spec-001]]"
  - "[[../../AGENTS]]"
tags:
  - proyecto/tesis
  - tipo/decision
  - sprint/s1
  - modulo/transversal
---

# ADR-0003 — Estructura raíz de la aplicación Django y agentes

## Estado

Aceptada por el tesista el 2026-07-25.

## Contexto

El repositorio es al mismo tiempo la base del proyecto, el vault de Obsidian y la fuente
común para agentes, especificaciones, código, pruebas y evidencia académica. La aplicación
Django todavía no existe y debe ubicarse sin crear una segunda fuente de verdad ni mezclar
el código de producción con la configuración de los agentes.

## Decisión

La aplicación se desarrollará directamente en la raíz:

`F:\Tesis\App Tesis`

No se añadirá una raíz intermedia `app/`, `backend/` o `src/`. El proyecto Django tendrá
`manage.py`, `config/` y `apps/` en el mismo repositorio donde ya viven `specs/`, `docs/` y
los contratos de agentes.

```text
F:\Tesis\App Tesis\
├── manage.py
├── pyproject.toml
├── .env.example
├── config/
│   └── settings/
├── apps/
│   ├── core/
│   ├── accounts/
│   ├── planning/
│   ├── attendance/
│   ├── traceability/
│   ├── reports/
│   └── public_site/
├── templates/
├── static/
├── tests/
├── specs/
├── docs/
├── agents/
├── .agents/
├── .codex/
├── scripts/
├── tools/
├── evals/
└── AGENTS.md
```

## Límites de responsabilidad

- `config/` contiene arranque, rutas y configuración por entorno; no reglas de negocio.
- `apps/` contiene las capacidades del monolito modular.
- `templates/` y `static/` contienen únicamente recursos globales; cada app conserva sus
  plantillas y recursos propios bajo su namespace.
- `tests/` contiene recorridos entre módulos; cada app conserva pruebas específicas cerca de
  su código.
- `specs/` contiene spec, plan, contratos y tareas antes del código.
- `docs/` conserva Obsidian, decisiones, evidencia y trazabilidad.
- `AGENTS.md` es el contrato común; `agents/tesis/` conserva conocimiento estable del dominio.
- `.agents/skills/` conserva flujos portables y `.codex/agents/` adapta roles a Codex.
- `tools/agent-lab/` permanece aislado y no forma parte de la aplicación.

La primera app será `accounts`; debe incluir el usuario personalizado antes de la primera
migración estable. `core` permanecerá mínimo y no concentrará reglas de todos los dominios.
El árbol completo representa el objetivo del monolito: la primera implementación creará
únicamente `config/`, `apps/accounts/` y las carpetas compartidas que SPEC-001 utilice. Las
apps de sprints posteriores no se crearán vacías para adelantar trabajo.

El gestor de dependencias y su archivo de bloqueo se seleccionarán explícitamente en el plan.
`pyproject.toml` será la fuente declarativa, pero ADR-0003 no aprueba por sí solo `uv`, Poetry
ni otra herramienta.

## Organización multiagente

No se crearán agentes por cada app. Los roles se mantienen por especialidad:
`requirements`, `architect`, `ux`, `implementer` y `reviewer`. Cada tarea delegada tendrá ID
de requisito, rutas permitidas, prueba esperada y un único escritor. El agente coordinador es
el único que actualiza dashboard, sprint y matriz global durante una ejecución multiagente.

## Alternativas descartadas

- `backend/` o `app/`: añade profundidad sin separar otro servicio.
- `src/`: aporta aislamiento útil para bibliotecas distribuibles, pero aumenta configuración
  sin beneficio suficiente para este monolito Django.
- repositorios separados para documentación y código: debilita la trazabilidad y duplica
  fuentes de verdad.

## Consecuencias

- Django se ejecutará desde la raíz del repositorio.
- Obsidian continuará abriendo la misma raíz.
- Código, documentación y agentes compartirán Git, pero no responsabilidades.
- Los secretos, bases locales, `media/` y `staticfiles/` no se versionarán.
- La estructura concreta de settings, dependencias y pruebas se detallará en el plan de
  SPEC-001.
- Esta decisión no autoriza crear la aplicación: la implementación requiere plan, tareas,
  análisis y aprobación de sus puertas.

## Evidencia

- Confirmación del tesista: “Confirmo SPEC-001 y acepto la estructura propuesta.”
- Fecha: 2026-07-25.
- Registro:
  [[../evidence/fase-i/2026-07-25-confirmacion-spec-001|EVID-SPEC-001]].
- Antecedente:
  [[proposals/2026-07-25-estructura-raiz-aplicacion-django|propuesta de estructura raíz]].
