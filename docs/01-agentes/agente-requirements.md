---
title: "Agente — Redactor de requisitos"
canonical_id: requirements
type: agent
kind: host-role
status: active
sandbox: read-only
tags:
  - proyecto/tesis
  - tipo/agente
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
source_path: ".codex/agents/requirements.toml"
---

# Agente — Redactor de requisitos

## Propósito

Contrastar fuentes, separar hechos de inferencias y redactar propuestas de requisitos comprobables sin aprobarlas.

## Entradas

- `AGENTS.md`.
- Constitución y políticas de tesis.
- Anteproyecto, evidencia de campo y fuente asignada.
- Especificaciones y trazabilidad cuando la tarea lo requiera.

## Salidas

- Hechos.
- Inferencias.
- Conflictos.
- Preguntas.
- Propuestas con actor, fuente, reglas, criterios de aceptación y fuera de alcance.

## Dependencias

- [[AGENTS]]
- [[../../agents/tesis/PROJECT_CONTEXT|PROJECT_CONTEXT]]
- [[../../agents/tesis/KNOWLEDGE_POLICY|KNOWLEDGE_POLICY]]
- [[../../agents/tesis/OBSIDIAN_POLICY|OBSIDIAN_POLICY]]

## Skills relacionadas

La configuración no declara skills explícitas. La relación de trabajo propuesta es:

- [[skill-speckit-specify]]
- [[skill-speckit-clarify]]
- [[skill-speckit-checklist]]

Esta relación es documental; no se ha verificado una carga automática en runtime.

## Escritura y límites

- Solo lectura.
- No edita archivos ni escribe notas en el vault.
- Si propone una nota, usa `docs/requirements/proposals/` y estado `proposed`.
- No aprueba requisitos.
- No escribe en `.codex/`, `.agents/`, `tools/`, `evals/` ni fuera de la raíz.

## Ubicación real

- Configuración: `.codex/agents/requirements.toml`.
- Nota canónica: `docs/01-agentes/agente-requirements.md`.

## Distinción importante

“Redactor de requisitos” es el nombre visible. `requirements` es el único identificador técnico. No existe un agente técnico separado llamado `redactor`.
