---
title: Checkpoint - contrato universal de orquestadores
type: checkpoint
status: partially-complete
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

## Pendiente

- Ejecutar una sesión real de humo con Codex, Antigravity y OpenChamber, leyendo este checkpoint
  desde cada host y comprobando que cada uno respete el escritor único.
- Revisar con el tesista la selección concreta de modelos y cuotas en cada herramienta.

## Próxima acción

El reviewer debe leer el contrato y ejecutar la prueba de humo sin modificar los archivos. Si la
prueba pasa, el coordinador puede cambiar este checkpoint a `completed` y registrar la evidencia
de los tres hosts. El commit ya tiene hash real; no debe crearse otro commit solo para repetir
esta evidencia sin revisar antes el diff pendiente.

## Nota sobre cambios preexistentes

El worktree contenía modificaciones del laboratorio Python y documentación que fueron incluidas
en el commit `62dadf5`. El cambio local posterior de `.obsidian/graph.json` no forma parte de este
checkpoint ni debe mezclarse automáticamente con la siguiente tarea.
