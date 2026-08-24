---
title: "Skill — speckit-implement"
canonical_id: speckit-implement
type: skill
kind: workflow
status: guarded
tags:
  - proyecto/tesis
  - tipo/skill
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
source_path: ".agents/skills/speckit-implement/SKILL.md"
---

# Skill — speckit-implement

## Qué hace

Procesa y ejecuta las tareas definidas en `tasks.md`.

## Activación

Solo después de que la especificación esté aprobada y las tareas hayan sido revisadas.

## Entradas y salidas

- Entrada: `spec.md`, `plan.md`, `tasks.md`, código y pruebas.
- Salida: cambios de implementación, pruebas y evidencia.

## Escritura

Sí. Puede modificar código y archivos de trabajo dentro del alcance autorizado.

## Agentes relacionados

- [[agente-implementer]]
- [[agente-reviewer]]

## Restricción del proyecto

No debe ejecutarse sobre una especificación sin aprobación humana.

## Fuente

`.agents/skills/speckit-implement/SKILL.md`
