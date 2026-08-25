---
title: Contratos canónicos de roles del arnés
type: architecture-contract
status: proposed
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
---

# Contratos canónicos de roles

Estos archivos son la fuente común de responsabilidades, límites de escritura y handoffs
para Codex, OpenCode/OpenChamber y Antigravity. Cada host tiene un adaptador propio, pero
no debe redefinir el alcance ni relajar estas restricciones.

| Rol | Contrato | Escritura | Handoff principal |
|---|---|---|---|
| `requirements` | [[requirements]] | No | `coordinator` |
| `architect` | [[architect]] | Solo propuestas arquitectónicas autorizadas | `coordinator` |
| `ux` | [[ux]] | No | `coordinator` |
| `frontend` | [[frontend]] | UI asignada | `reviewer` |
| `implementer` | [[implementer]] | Código asignado | `reviewer` |
| `reviewer` | [[reviewer]] | No | `coordinator` |
| `researcher` | [[researcher]] | Solo propuestas documentales autorizadas | `coordinator` |
| `documenter` | [[documenter]] | Documentación operativa permitida | `git-manager` / `coordinator` |
| `git-manager` | [[git-manager]] | Índice y commit autorizado | `documenter` |

## Regla de precedencia

`AGENTS.md`, la constitución, las políticas de conocimiento/Obsidian y las fuentes de verdad
del proyecto prevalecen sobre cualquier instrucción de un host o modelo. Estos contratos
detallan el rol; no aprueban requisitos ni decisiones.

## Regla de continuidad

Un cambio de Codex a Antigravity, OpenChamber u otra herramienta se hace mediante un handoff
en `docs/bitacora/checkpoints/`. La nueva herramienta continúa desde el último estado
persistido, no desde la memoria privada de la conversación anterior.
