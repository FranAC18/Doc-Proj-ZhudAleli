---
title: Estructura raíz para la aplicación Django y los agentes
type: decision
status: superseded
date: 2026-07-25
sprint: s1
module: transversal
decision_id: PRO-ADR-003
accepted_by: tesista
accepted: 2026-07-25
superseded_by: ADR-0003
related:
  - "[[../ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[../../architecture/ARQUITECTURA-OBJETIVO]]"
  - "[[../../architecture/PLAN-DESDE-CERO]]"
  - "[[../../architecture/FLUJO-MULTIAGENTE]]"
  - "[[../../../specs/001-acceso-usuarias-internas/spec]]"
  - "[[../../../AGENTS]]"
tags:
  - proyecto/tesis
  - tipo/decision
  - sprint/s1
  - modulo/transversal
---

# Propuesta: estructura raíz para la aplicación Django y los agentes

> [!success] Resultado
> El tesista aceptó esta propuesta el 2026-07-25. La decisión vigente se conserva en
> [[../ADR-0003-estructura-raiz-aplicacion-django|ADR-0003]]; este archivo permanece como
> antecedente histórico.

## Pregunta

¿En qué carpeta debe desarrollarse la aplicación y cómo se separan el código, los agentes,
las especificaciones y la documentación académica?

## Recomendación

Desarrollar la aplicación **directamente en la raíz del repositorio y vault**:

`F:\Tesis\App Tesis`

No crear una segunda raíz llamada `app/`, `backend/` o `src/`. El ejecutable del proyecto,
la configuración y las apps de dominio vivirán junto a `docs/`, `specs/` y los contratos de
agentes, pero cada responsabilidad conservará su carpeta.

Esta opción mantiene una sola fuente Git, una sola raíz de Obsidian y rutas cortas para
Django, pruebas y automatización.

## Estructura propuesta

```text
F:\Tesis\App Tesis\
├── manage.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── config/
│   ├── __init__.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│   └── settings/
│       ├── __init__.py
│       ├── base.py
│       ├── development.py
│       ├── test.py
│       └── production.py
├── apps/
│   ├── __init__.py
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

Las carpetas Django se crearán únicamente cuando SPEC-001, su plan y sus tareas superen las
puertas de aprobación. Este documento describe la ubicación futura; no autoriza crear código.

## Responsabilidad de cada área

| Carpeta o archivo | Responsabilidad | Regla de separación |
|---|---|---|
| `manage.py` y `config/` | Arranque, rutas y configuración por entorno | No contienen reglas de negocio |
| `apps/` | Capacidades del monolito modular | Cada app posee sus modelos, formularios, vistas, permisos, plantillas y pruebas locales |
| `templates/` | Layout global y componentes compartidos | Las pantallas propias permanecen en `apps/<app>/templates/<app>/` |
| `static/` | Tokens visuales, estilos base e imágenes versionables | Los archivos generados de despliegue van a `staticfiles/` y no se versionan |
| `tests/` | Recorridos críticos entre módulos | Las pruebas específicas permanecen cerca de cada app |
| `specs/` | Spec, plan, contratos y tareas por funcionalidad | Es la puerta antes del código |
| `docs/` | Vault Obsidian, decisiones, evidencia y trazabilidad | No duplica código ni secretos |
| `AGENTS.md` | Contrato común para todos los agentes | Es la entrada normativa única |
| `agents/tesis/` | Contexto, conocimiento y políticas estables del proyecto | No contiene configuraciones particulares de un motor |
| `.agents/skills/` | Skills portables de Spec Kit | Se comparte entre motores; no se copia por agente |
| `.codex/agents/` | Definición de roles especializados de Codex | Solo adapta los roles al motor Codex |
| `tools/agent-lab/` | Laboratorio heredado y aislado | No forma parte de la aplicación Django |

## Organización interna de una app

La estructura inicial de `accounts`, primera app de dominio, deberá mantenerse pequeña:

```text
apps/accounts/
├── __init__.py
├── apps.py
├── models.py
├── forms.py
├── views.py
├── urls.py
├── policies.py
├── migrations/
├── templates/accounts/
├── static/accounts/
└── tests/
```

- `models.py` conserva las entidades e invariantes de acceso.
- `forms.py` valida las entradas de usuaria.
- `views.py` coordina solicitudes y respuestas sin concentrar reglas complejas.
- `policies.py` contiene comprobaciones de autorización reutilizables cuando sean necesarias.
- `services.py` solo se añadirá si una operación real coordina varias entidades o requiere
  una transacción; no se crea de forma preventiva.
- `queries.py` solo se añadirá para consultas complejas justificadas.

El usuario personalizado debe pertenecer a `accounts` y existir antes de la primera migración
estable.

## Estructura de agentes

La organización actual es adecuada si se conserva esta jerarquía:

```text
AGENTS.md                    contrato común y obligatorio
agents/tesis/                conocimiento estable del dominio
├── AGENT.md
├── PROJECT_CONTEXT.md
├── KNOWLEDGE_POLICY.md
└── OBSIDIAN_POLICY.md
.agents/skills/              flujos portables speckit-*
.codex/agents/               requirements, architect, ux, implementer y reviewer
```

No se debe crear un agente por app ni copiar el contexto de tesis dentro de cada rol. Los
roles reciben una tarea delimitada, rutas permitidas y pruebas esperadas; el coordinador es
el único que actualiza dashboard, sprint y matriz global durante una ejecución multiagente.

## Alternativas descartadas por ahora

### Aplicación dentro de `backend/` o `app/`

Añade un nivel de rutas sin separar un frontend independiente ni otro servicio. No aporta
valor al monolito actual.

### Aplicación dentro de `src/`

Mejora el aislamiento de paquetes en bibliotecas distribuibles, pero aumenta la configuración
y la carga pedagógica para una única aplicación Django de tesis.

### Repositorio separado para código y documentación

Rompe la trazabilidad directa entre requisito, tarea, prueba y evidencia, además de crear dos
fuentes de verdad.

## Consecuencias

- La aplicación se ejecutará desde `F:\Tesis\App Tesis`.
- Las rutas principales serán `manage.py`, `config/` y `apps/`.
- Obsidian seguirá abriendo la misma raíz.
- Los agentes y skills permanecerán separados del código de producción.
- No habrá una segunda carpeta que también se llame “aplicación”.
- La propuesta fue confirmada y promovida a ADR-0003. Su aplicación concreta se incorporará
  al plan técnico de SPEC-001.
