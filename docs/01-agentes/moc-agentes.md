---
title: "MOC — Agentes"
type: moc
status: active
tags:
  - proyecto/tesis
  - tipo/moc
  - estado/activo
verified_at: "2026-08-24"
---

# Agentes del arnés

| Identificador | Nombre visible | Modo | Nota | Fuente |
|---|---|---|---|---|
| `requirements` | Redactor de requisitos | Solo lectura | [[agente-requirements]] | `.codex/agents/requirements.toml` |
| `architect` | Arquitecto | Solo lectura | [[agente-architect]] | `.codex/agents/architect.toml` |
| `ux` | UX/UI | Solo lectura | [[agente-ux]] | `.codex/agents/ux.toml` |
| `implementer` | Implementador | Escritura acotada | [[agente-implementer]] | `.codex/agents/implementer.toml` |
| `reviewer` | Revisor | Solo lectura | [[agente-reviewer]] | `.codex/agents/reviewer.toml` |

## Regla de nombres

`requirements` es el identificador técnico único. “Redactor de requisitos” es el nombre visible.

## Regla de coordinación

Los agentes de análisis y revisión devuelven propuestas o hallazgos. El agente raíz conserva la responsabilidad de registrar resultados en el vault.
