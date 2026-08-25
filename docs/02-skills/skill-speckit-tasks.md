---
title: "Skill — speckit-tasks"
canonical_id: speckit-tasks
type: skill
kind: workflow
status: active
tags:
  - proyecto/tesis
  - tipo/skill
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
source_path: ".agents/skills/speckit-tasks/SKILL.md"
---

# Skill — speckit-tasks

## Qué hace

Genera un `tasks.md` accionable y ordenado por dependencias a partir de los artefactos de diseño.

## Activación

Después de `plan.md` y los documentos de diseño requeridos.

## Entradas y salidas

- Entrada: `spec.md`, `plan.md`, contratos y modelo de datos.
- Salida: `tasks.md` con rutas, dependencias y verificaciones.

## Escritura

Sí, en el directorio de la funcionalidad.

## Agentes relacionados

- [[agente-architect]]
- [[agente-implementer]]

## Fuente

`.agents/skills/speckit-tasks/SKILL.md`
