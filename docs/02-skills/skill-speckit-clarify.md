---
title: "Skill — speckit-clarify"
canonical_id: speckit-clarify
type: skill
kind: workflow
status: active
tags:
  - proyecto/tesis
  - tipo/skill
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
source_path: ".agents/skills/speckit-clarify/SKILL.md"
---

# Skill — speckit-clarify

## Qué hace

Identifica ambigüedades de una especificación mediante hasta cinco preguntas dirigidas y registra las respuestas.

## Activación

Cuando una ambigüedad puede cambiar alcance, seguridad, datos o experiencia de uso.

## Entradas y salidas

- Entrada: especificación actual.
- Salida: preguntas y actualización de `spec.md` después de recibir respuestas.

## Escritura

Sí, sobre la especificación y sus artefactos asociados.

## Agentes relacionados

- [[agente-requirements]]
- [[agente-ux]]

## Fuente

`.agents/skills/speckit-clarify/SKILL.md`
