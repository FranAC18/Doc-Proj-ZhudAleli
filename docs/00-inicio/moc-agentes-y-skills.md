---
title: "MOC — Agentes y skills"
type: moc
status: active
tags:
  - proyecto/tesis
  - tipo/moc
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
---

# Mapa de agentes y skills

Este MOC conecta la configuración real del arnés con sus notas de Obsidian.

## Capas

| Capa | Ubicación | Función |
|---|---|---|
| Roles host | `.codex/agents/` | Define responsabilidades, permisos y límites de agentes. |
| Skills Spec Kit | `.agents/skills/` | Define flujos de especificación, planificación, tareas y revisión. |
| Laboratorio Python | `tools/agent-lab/` | Experimenta con modelos, memoria, herramientas y persistencia. |
| Vault | `docs/`, `specs/` y `agents/tesis/` | Conserva conocimiento, decisiones, evidencias y artefactos. |

El laboratorio Python no carga automáticamente los TOML de `.codex/agents/` ni las skills de `.agents/skills/`. La relación entre ambas capas es documental hasta que exista una integración explícita.

## Agentes

- [[agente-requirements]] — Redactor de requisitos.
- [[agente-architect]] — Revisión de arquitectura.
- [[agente-ux]] — Revisión UX/UI.
- [[agente-implementer]] — Implementación acotada.
- [[agente-reviewer]] — Revisión independiente.

## Skills

- [[skill-speckit-specify]]
- [[skill-speckit-clarify]]
- [[skill-speckit-plan]]
- [[skill-speckit-tasks]]
- [[skill-speckit-analyze]]
- [[skill-speckit-implement]]
- [[skill-speckit-converge]]
- [[skill-speckit-checklist]]
- [[skill-speckit-constitution]]
- [[skill-speckit-taskstoissues]]

## Registros relacionados

- [[auditoria-agentes-skills-2026-08-24]]
- [[FLUJO-MULTIAGENTE]]
- [[FUENTES-DE-VERDAD]]
- [[ADR-0002-arnes-portable-de-ia]]
- [[ADR-0004-capa-abstraccion-modelos-ia]]
