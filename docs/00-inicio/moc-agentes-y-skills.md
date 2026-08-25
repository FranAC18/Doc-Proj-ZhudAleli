---
title: "MOC — Agentes y skills"
type: moc
status: active
tags:
  - proyecto/tesis
  - tipo/moc
  - estado/activo
verified_at: "2026-08-25"
verified_against_commit: "73e3c0f"
---

# Mapa de agentes y skills

Este MOC conecta la configuración real del arnés con sus notas de Obsidian.

## Capas

| Capa | Ubicación | Función |
|---|---|---|
| Roles host | `.codex/agents/` | Define responsabilidades, permisos y límites de agentes. |
| Roles canónicos | `agents/tesis/roles/` | Fuente común de responsabilidades, rutas y handoffs. |
| Adaptación OpenCode | `.opencode/agents/` | Perfiles que apuntan a los contratos canónicos. |
| Comandos OpenCode | `.opencode/commands/` | Prompts `/route`, `/architect`, `/implement`, `/frontend`, `/review` y `/research`. |
| Adaptación Antigravity | `.agents/rules/` | Reglas de contexto y continuidad del workspace. |
| Skills Spec Kit | `.agents/skills/` | Define flujos de especificación, planificación, tareas y revisión. |
| Laboratorio Python | `tools/agent-lab/` | Experimenta con modelos, memoria, herramientas y persistencia. |
| Vault | `docs/`, `specs/` y `agents/tesis/` | Conserva conocimiento, decisiones, evidencias y artefactos. |
| Contexto operativo | `docs/context/` | Índice único y recuperación selectiva por funcionalidad. |

El laboratorio Python no carga automáticamente los TOML de `.codex/agents/` ni las skills de `.agents/skills/`. La relación entre ambas capas es documental hasta que exista una integración explícita.

El laboratorio de modelos tampoco cambia de host por sí solo. La continuidad entre Codex,
Antigravity y OpenChamber se hace mediante `docs/bitacora/checkpoints/` y la plantilla de
handoff universal.

## Agentes

- [[agente-requirements]] — Redactor de requisitos.
- [[agente-architect]] — Revisión de arquitectura.
- [[agente-ux]] — Revisión UX/UI.
- `.opencode/agents/frontend.md` — Implementación de UI asignada.
- [[agente-implementer]] — Implementación acotada.
- [[agente-reviewer]] — Revisión independiente.
- `.opencode/agents/researcher.md` — Investigación focalizada.
- [[agente-documenter]] — Redacción documental del vault.
- [[agente-git-manager]] — Gestión de commits autorizados.

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

Skills operativas de Zhud Alelí:

- `.agents/skills/zhud-aleli-context/SKILL.md`
- `.agents/skills/zhud-aleli-documenter/SKILL.md`
- `.agents/skills/zhud-aleli-git-manager/SKILL.md`
- `.agents/skills/zhud-aleli-handoff/SKILL.md`

## Registros relacionados

- [[auditoria-agentes-skills-2026-08-24]]
- [[FLUJO-MULTIAGENTE]]
- [[FUENTES-DE-VERDAD]]
- [[CONTRATO-UNIVERSAL-ORQUESTADORES]]
- [[../bitacora/ESTADO-ACTIVO]]
- [[../../agents/tesis/roles/README]]
- [[ADR-0002-arnes-portable-de-ia]]
- [[ADR-0004-capa-abstraccion-modelos-ia]]
