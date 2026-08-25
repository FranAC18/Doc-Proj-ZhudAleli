---
title: Estado activo de continuidad
type: state
status: ready
project: tesis-zhud-aleli
updated: 2026-08-24
active_task: null
last_handoff: "[[checkpoints/2026-08-24-contrato-universal-orquestadores]]"
last_commit: 1210065
next_action: Confirmar con el tesista la selección de modelos/cuotas por host y continuar las tareas aprobadas de SPEC-001 (Fase 1, diseño sin Django).
tags:
  - proyecto/tesis
  - tipo/checkpoint
---

# Estado activo de continuidad

Este archivo es el puntero estable que deben leer Codex, Antigravity, OpenCode y OpenChamber
antes de trabajar. El detalle de cada tarea vive en su checkpoint dentro de
`docs/bitacora/checkpoints/`.

## Estado actual

- No hay una tarea de implementación activa registrada en este puntero.
- La aplicación Django todavía no existe.
- La primera funcionalidad aprobada es `SPEC-001` y su implementación continúa limitada a
  `accounts` y acceso.
- El arnés y el contrato universal están registrados; HEAD actual en `main` (`1210065`).
- El smoke test del contrato universal con Codex, Antigravity y OpenCode/OpenChamber **pasó**;
  evidencia en `docs/evidence/S0/2026-08-24-smoke-test-contrato-universal.md`. El checkpoint
  `2026-08-24-contrato-universal-orquestadores` cambió a `completed`.
- Pendiente: confirmar con el tesista la selección de modelos/cuotas por host (en uso
  `opencode:big-pickle` vs `deepseek-v4` propuesto en `RUTAS-MODELOS-IA.md`).

## Cómo actualizarlo

El coordinador actualiza este puntero únicamente cuando cambia la tarea activa, el último
handoff o el próximo paso permitido. El documenter registra el detalle operativo en el
checkpoint, no sobrescribe este archivo sin indicación del coordinador.

## Regla de continuidad

Si `active_task` no es `null`, lee el checkpoint enlazado antes de modificar cualquier
archivo. Si es `null`, no inventes una tarea: solicita o identifica una spec aprobada.
