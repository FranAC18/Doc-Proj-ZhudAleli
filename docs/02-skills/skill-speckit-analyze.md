---
title: "Skill — speckit-analyze"
canonical_id: speckit-analyze
type: skill
kind: review
status: active
read_only: true
tags:
  - proyecto/tesis
  - tipo/skill
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
source_path: ".agents/skills/speckit-analyze/SKILL.md"
---

# Skill — speckit-analyze

## Qué hace

Realiza un análisis no destructivo de consistencia y calidad entre `spec.md`, `plan.md` y `tasks.md`.

## Activación

Después de generar las tareas y antes de implementar.

## Entradas y salidas

- Entrada: especificación, plan y tareas.
- Salida: informe de inconsistencias, cobertura, duplicidades, riesgos y recomendaciones.

## Escritura

No. Es estrictamente de solo lectura.

## Agentes relacionados

- [[agente-architect]]
- [[agente-reviewer]]

## Fuente

`.agents/skills/speckit-analyze/SKILL.md`
