---
title: "Handoff universal - {{task_id}}"
type: checkpoint
status: partially-complete
date: {{date:YYYY-MM-DD}}
task_id: "TXXX"
requirement_ids: []
sprint: "S1"
module: transversal
repository: "ZhudAleli | App-zhudaleli"
remote: ""
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

Indicar solo fuentes y secciones realmente consultadas o ya disponibles en el chat.
Aplicar `docs/context/context-index.md`; esta plantilla no exige abrir constitución,
contexto de dominio, dashboard ni todos los artefactos de una spec para cada handoff.

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

La herramienta siguiente debe leer este handoff, confirmar la raíz, remoto y estado de Git antes
de escribir. No puede cambiar `allowed_paths`, alcance, requisito o criterio sin devolver una
pregunta al coordinador.
Leer solo el checkpoint enlazado para la tarea y sus fuentes necesarias; no recorrer
cronológicamente la bitácora. Este checkpoint también puede ser el resumen de sesión.

## Commit

Antes del commit:

```yaml
commit: pending
commit_hash: null
```

Después del commit, el `git-manager` debe completar el hash real, rama, archivos incluidos y
resultado posterior. El `documenter` registra entonces la fase `post_commit`.
