---
title: Estado activo de continuidad
type: state
status: ready
project: tesis-zhud-aleli
updated: 2026-08-24
active_task: null
last_handoff: null
last_commit: c6df8f5
next_action: Seleccionar una tarea aprobada y crear su handoff universal
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
- Los cambios locales del arnés y del contrato universal permanecen pendientes de revisión y
  commit.

## Cómo actualizarlo

El coordinador actualiza este puntero únicamente cuando cambia la tarea activa, el último
handoff o el próximo paso permitido. El documenter registra el detalle operativo en el
checkpoint, no sobrescribe este archivo sin indicación del coordinador.

## Regla de continuidad

Si `active_task` no es `null`, lee el checkpoint enlazado antes de modificar cualquier
archivo. Si es `null`, no inventes una tarea: solicita o identifica una spec aprobada.
