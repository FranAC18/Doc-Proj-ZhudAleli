---
title: "Agente — Implementador"
canonical_id: implementer
type: agent
kind: host-role
status: active
sandbox: workspace-write
tags:
  - proyecto/tesis
  - tipo/agente
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
source_path: ".codex/agents/implementer.toml"
---

# Agente — Implementador

## Propósito

Implementar únicamente una tarea asignada, con rutas permitidas, pruebas y resultado verificable.

## Entradas y salidas

- Entradas: `spec.md`, `plan.md`, `tasks.md`, ID de tarea, rutas permitidas y pruebas esperadas.
- Salidas: cambios de código, pruebas ejecutadas, archivos modificados, riesgos y criterios no cubiertos.

## Skills relacionadas

- [[skill-speckit-implement]]
- [[skill-speckit-converge]]

## Límites

- Escritura de trabajo limitada al alcance asignado.
- No hace commit, push, merge, rebase ni borra historia.
- No cambia dashboard, sprint, matriz global, dependencias o arquitectura salvo autorización explícita de la tarea.

## Ubicación real

- Configuración: `.codex/agents/implementer.toml`.
- Nota: `docs/01-agentes/agente-implementer.md`.
