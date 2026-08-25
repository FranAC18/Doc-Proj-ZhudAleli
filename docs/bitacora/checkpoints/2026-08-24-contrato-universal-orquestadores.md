---
title: Checkpoint - contrato universal de orquestadores
type: checkpoint
status: completed
date: 2026-08-24
task_id: HARNESS-UNIVERSAL-001
requirement_ids: []
sprint: Sprint 0 - Arnés y documentación
module: transversal
phase: post_commit
writer: coordinator
handoff_to: reviewer
branch: codex/001-acceso-usuarias-internas
commit: 62dadf5
commit_hash: 62dadf58c56a33874d5b6e37949bd0a4b5845977
allowed_paths:
  - AGENTS.md
  - agents/tesis/roles/**
  - .agents/rules/**
  - .agents/skills/zhud-aleli-*/**
  - .codex/agents/**
  - .opencode/**
  - docs/architecture/**
  - docs/bitacora/**
  - docs/templates/**
  - scripts/agent.*
  - tools/agent-routes.toml
  - tools/validate-universal.py
  - tools/agent-lab/tests/test_universal_contract.py
forbidden_paths:
  - .env
  - .venv/**
  - db.sqlite3
  - secrets/**
related:
  - "[[../../architecture/CONTRATO-UNIVERSAL-ORQUESTADORES]]"
  - "[[../../architecture/RUTAS-MODELOS-IA]]"
  - "[[../../templates/PLANTILLA-HANDOFF-UNIVERSAL]]"
  - "[[../ESTADO-ACTIVO]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/arnes
  - estado/partially-complete
---

# Checkpoint - contrato universal de orquestadores

## Contexto

Se implementó la primera versión operativa del contrato universal para que Codex, Antigravity,
OpenCode y OpenChamber trabajen sobre la raíz del repositorio, que también es el vault de
Obsidian. El objetivo es conservar el contexto en archivos versionados y permitir un cambio de
herramienta por tarea cuando cambien la cuota o el modelo disponible.

## Implementado

- Contratos canónicos de roles en `agents/tesis/roles/`.
- Skills compartidas en `.agents/skills/` y reglas de continuidad en `.agents/rules/`.
- Adaptadores de Codex en `.codex/agents/` y de OpenCode/OpenChamber en `.opencode/agents/`.
- Contrato, rutas de modelos, plantilla de handoff y estado activo en `docs/`.
- Validador de raíz y adaptadores en `tools/validate-universal.py`.
- Rutas declarativas sin credenciales en `tools/agent-routes.toml`.
- Launchers `scripts/agent.ps1` y `scripts/agent.sh` con validación previa.
- Prueba permanente `tools/agent-lab/tests/test_universal_contract.py`.

## Verificación realizada

Hechos verificados en esta sesión:

- `pytest tools/agent-lab/tests`: 30 pruebas aprobadas.
- `tools/validate-universal.py`: contrato universal OK.
- `python -m py_compile tools/validate-universal.py`: correcto.
- `bash -n scripts/agent.sh`: correcto.
- `opencode --help`: CLI disponible.
- `opencode agent list`: detecta `architect`, `documenter`, `git-manager`, `implementer`,
  `requirements`, `reviewer` y `ux`.
- La raíz detectada es `F:\Tesis\App Tesis`, el vault coincide y la rama actual es
  `codex/001-acceso-usuarias-internas`.
- El commit real del contrato es `62dadf58c56a33874d5b6e37949bd0a4b5845977`.
- La referencia local `origin/codex/001-acceso-usuarias-internas` coincide con ese hash.

## Smoke test terminado (2026-08-24)

Se ejecutó una sesión real de humo read-only con Codex, Antigravity y OpenCode/OpenChamber sobre
la raíz `F:\Tesis\App Tesis`. Los tres resolvieron la raíz como vault, leyeron este checkpoint y
respetaron el escritor único. Evidencia:
`docs/evidence/S0/2026-08-24-smoke-test-contrato-universal.md`.

- `tools/validate-universal.py --json`: OK (0 faltantes, sin errores de rutas).
- `tools/agent-lab/tests/test_universal_contract.py`: 1 passed.
- `opencode agent list`: roles universales detectados.
- `git status --short --branch`: `## main...origin/main` (limpio). `git diff --check`: sin errores.

Guardarraíl verificado: un intento de Codex se abrió en `F:\Prácticas\Tarjetas digitales\scriptQr`
(raíz ajena); en lugar de escribir, reportó el bloqueo y no generó artefactos, cumpliendo el
contrato de inicio. Se reabrió con `scripts/agent.ps1 codex` desde la raíz y pasó.

## Pendiente

- Confirmar con el tesista la selección concreta de modelos y cuotas por host (`opencode:big-pickle`
  en uso vs `deepseek-v4` propuesto en `RUTAS-MODELOS-IA.md`; las variantes Gemini locales de
  Antigravity no se versionan como IDs universales).

## Próxima acción

Estando el smoke test satisfecho, el coordinador conserva: (1) la confirmación de modelos/cuotas
con el tesista y (2) la continuación con las tareas aprobadas de `SPEC-001` (Fase 1: diseño sin
Django). No se crea otro commit solo para repetir esta evidencia; se revisa el diff pendiente con
el `git-manager` antes de cualquier commit.

## Nota sobre cambios preexistentes

El worktree contenía modificaciones del laboratorio Python y documentación que fueron incluidas
en el commit `62dadf5`. El cambio local posterior de `.obsidian/graph.json` no forma parte de este
checkpoint ni debe mezclarse automáticamente con la siguiente tarea.
