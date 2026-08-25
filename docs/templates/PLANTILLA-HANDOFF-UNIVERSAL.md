---
title: "Handoff universal - {{task_id}}"
type: checkpoint
status: partially-complete
date: {{date:YYYY-MM-DD}}
task_id: "TXXX"
requirement_ids: []
sprint: "S1"
module: transversal
phase: in-progress
writer: ""
handoff_to: ""
branch: ""
commit: pending
commit_hash: null
allowed_paths: []
forbidden_paths: []
related:
  - "[[../00-inicio/00-dashboard]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
---

# Handoff universal - {{task_id}}

## Objetivo

Describe el resultado observable de la tarea, no una instrucción abierta.

## Contexto leído

- `AGENTS.md`
- `.specify/memory/constitution.md`
- `agents/tesis/PROJECT_CONTEXT.md`
- `docs/00-inicio/00-dashboard.md`
- `specs/<id>/spec.md`
- `specs/<id>/plan.md`
- `specs/<id>/tasks.md`

## Estado

`partially-complete`

## Archivos modificados

-

## Archivos relevantes sin modificar

-

## Pruebas y verificaciones

| Comando | Resultado real | Observación |
|---|---|---|
| | | |

## Criterios cubiertos

-

## Pendientes

-

## Hallazgos de revisión

-

## Decisiones y supuestos

-

## Bloqueos

- Ninguno.

## Próxima acción

-

## Reglas para el siguiente host

La herramienta siguiente debe leer este handoff, confirmar la raíz y el estado de Git antes
de escribir. No puede cambiar `allowed_paths`, alcance, requisito o criterio sin devolver una
pregunta al coordinador.

## Commit

Antes del commit:

```yaml
commit: pending
commit_hash: null
```

Después del commit, el `git-manager` debe completar el hash real, rama, archivos incluidos y
resultado posterior. El `documenter` registra entonces la fase `post_commit`.
