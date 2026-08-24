---
title: "Skill — speckit-taskstoissues"
canonical_id: speckit-taskstoissues
type: skill
kind: external-integration
status: conditional
tags:
  - proyecto/tesis
  - tipo/skill
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
source_path: ".agents/skills/speckit-taskstoissues/SKILL.md"
---

# Skill — speckit-taskstoissues

## Qué hace

Convierte las tareas existentes en issues de GitHub accionables y ordenados por dependencia.

## Activación

Cuando se decide llevar el trabajo de `tasks.md` a GitHub.

## Entradas y salidas

- Entrada: `spec.md`, `plan.md`, `tasks.md` y contexto del repositorio.
- Salida: issues de GitHub.

## Escritura

Sí, en un sistema externo mediante la integración disponible.

## Agentes relacionados

- [[agente-implementer]]
- [[agente-reviewer]]

## Dependencia

Requiere acceso a la integración de GitHub. Esa conexión no fue verificada en esta auditoría.

## Fuente

`.agents/skills/speckit-taskstoissues/SKILL.md`
