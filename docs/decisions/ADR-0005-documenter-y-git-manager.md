---
title: "ADR-0005 — Documenter y Git Manager"
type: decision
status: accepted
date: 2026-08-24
decision: "accepted"
tags:
  - proyecto/tesis
  - tipo/decision
  - modulo/transversal
related:
  - "[[FLUJO-MULTIAGENTE]]"
  - "[[../01-agentes/agente-documenter|documenter]]"
  - "[[../01-agentes/agente-git-manager|git-manager]]"
  - "[[../01-agentes/agente-requirements|requirements]]"
---

# ADR-0005 — Documenter y Git Manager

## Contexto

El agente `requirements` es de solo lectura y no existe un agente dedicado a registrar de forma sistemática las sesiones, pruebas, evidencias y resultados de cada tarea. Tampoco existe un agente de commits; las reglas actuales exigen confirmación humana antes de modificar la historia de Git.

## Decisión

Se crean dos roles separados:

- `documenter`: Redactor documental del vault, con escritura limitada a sesiones, checkpoints, evidencias y propuestas.
- `git-manager`: Gestor de cambios Git, con capacidad de preparar y crear commits únicamente después de autorización explícita del tesista.

Estos dos roles se coordinan desde los hosts de trabajo Codex y Kimi. Gemini puede utilizarse
como modelo de redacción del documenter mediante el puente del laboratorio, pero no obtiene
permisos propios de Git ni sustituye al host o al `git-manager`.

El proceso será de dos fases documentales:

```text
implementación → pruebas → revisión
→ documenter/pre_commit
→ git-manager valida y crea commit autorizado
→ documenter/post_commit con hash real
```

## Límites

- `requirements` conserva su identidad y solo lectura.
- `documenter` no modifica specs aprobadas, requisitos confirmados, ADR aceptados, dashboard, roadmap ni matriz global.
- `git-manager` no hace push, merge, rebase, reset, clean ni cambia identidad Git.
- Ningún agente convierte una propuesta en una decisión aprobada.

## Consecuencias

- Cada cambio revisado tendrá un registro previo y evidencia posterior con hash real.
- La documentación no dependerá de que el modelo recuerde registrar manualmente el trabajo.
- El commit seguirá bajo control del tesista.
- La automatización inicial depende de que el coordinador entregue el handoff al documenter en los puntos definidos.

## Estado

Decisión confirmada por el tesista para implementación en el arnés. La creación de los roles no autoriza por sí sola ningún commit o push.
