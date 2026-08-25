---
title: Rutas universales de tareas, agentes y perfiles de modelo
type: architecture
status: proposed
date: 2026-08-25
related:
  - "[[CONTRATO-UNIVERSAL-ORQUESTADORES]]"
  - "[[../context/context-index]]"
  - "[[../bitacora/ESTADO-ACTIVO]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
---

# Rutas universales de tareas, agentes y perfiles de modelo

La configuración ejecutable está en `tools/agent-routes.toml`. La relación estable es:

```text
tipo de tarea → agente → perfil de capacidad → modelo seleccionado por el host
```

El repositorio no fija IDs de modelos ni proveedores concretos. Eso evita duplicar nombres,
forzar cuotas o convertir un alias de OpenCode Go, Codex o Antigravity en una afirmación de
disponibilidad. El perfil es una exigencia de capacidad; el runtime debe resolver el modelo real.

## Tipos mínimos

| Tipo | Agente | Riesgo | Perfil | Revisión |
|---|---|---:|---|---|
| `architecture` | `architect` | Alto | `reasoning_max` | Obligatoria |
| `planning` | `architect` | Alto | `reasoning_max` | Obligatoria |
| `implementation` | `implementer` | Medio | `coding_efficient` | Obligatoria |
| `frontend` | `frontend` | Medio | `frontend_strong` | Obligatoria |
| `debugging` | `implementer` | Alto | `coding_efficient` | Obligatoria |
| `research` | `researcher` | Bajo | `research_efficient` | Opcional |
| `review` | `reviewer` | Alto | `reasoning_max` | Independiente |
| `documentation` | `documenter` | Bajo | `documentation_economy` | Obligatoria |

## Perfiles

- `reasoning_max`: razonamiento profundo, contexto largo y salida estructurada.
- `coding_efficient`: edición acotada, uso de herramientas y salida estructurada.
- `frontend_strong`: implementación UI, revisión visual y accesibilidad.
- `research_efficient`: investigación focalizada y citas o fuentes trazables.
- `documentation_economy`: redacción estructurada con el menor coste razonable.

Los nombres anteriores son perfiles internos, no IDs de modelos. El modelo concreto se elige
en el host y se verifica con el catálogo y las credenciales disponibles en ese entorno.

## Hosts

OpenCode es el mecanismo nativo para los agentes y comandos de proyecto. Codex conserva sus
adaptadores en `.codex/agents/`. OpenChamber es una interfaz sobre OpenCode y no aparece como
fuente de configuración ni como requisito de ejecución.

## Cambio de cuota o modelo

```text
fallo de disponibilidad → detener la ejecución → registrar handoff → elegir otro modelo
compatible con el mismo perfil → leer el estado → continuar
```

El cambio de modelo no cambia la tarea, el alcance, las fuentes de verdad ni los criterios de
terminado. Si no existe un modelo disponible que cumpla el perfil, la tarea queda bloqueada y
se documenta el motivo; no se inventa un identificador.
