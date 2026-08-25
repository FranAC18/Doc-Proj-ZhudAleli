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

| Identificador | Nombre visible | Modo | Nota | Contrato canónico | Adaptadores |
|---|---|---|---|---|---|
| `requirements` | Redactor de requisitos | Solo lectura | [[agente-requirements]] | `agents/tesis/roles/requirements.md` | Codex/OpenCode/skills |
| `architect` | Arquitecto | Solo lectura | [[agente-architect]] | `agents/tesis/roles/architect.md` | Codex/OpenCode/skills |
| `ux` | UX/UI | Solo lectura | [[agente-ux]] | `agents/tesis/roles/ux.md` | Codex/OpenCode/skills |
| `implementer` | Implementador | Escritura acotada | [[agente-implementer]] | `agents/tesis/roles/implementer.md` | Codex/OpenCode |
| `reviewer` | Revisor | Solo lectura | [[agente-reviewer]] | `agents/tesis/roles/reviewer.md` | Codex/OpenCode |
| `documenter` | Redactor documental del vault | Escritura documental limitada | [[agente-documenter]] | `agents/tesis/roles/documenter.md` | Codex/OpenCode/Antigravity |
| `git-manager` | Gestor de cambios Git | Índice y commit autorizado | [[agente-git-manager]] | `agents/tesis/roles/git-manager.md` | Codex/OpenCode |

## Regla de nombres

`requirements` es el identificador técnico único. “Redactor de requisitos” es el nombre visible.

## Regla de coordinación

Los agentes de análisis y revisión devuelven propuestas o hallazgos. El agente raíz conserva la responsabilidad de registrar resultados en el vault. Los adaptadores de cada host deben apuntar al contrato canónico y no duplicar reglas contradictorias.

El `documenter` registra el trabajo operativo en sus rutas permitidas. El `git-manager` solo crea un commit después de autorización explícita del tesista.
