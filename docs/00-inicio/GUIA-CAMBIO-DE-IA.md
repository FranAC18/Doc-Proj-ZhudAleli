---
title: Guía de cambio de IA y onboarding de modelos
type: guide
status: confirmed
date: 2026-08-24
related:
  - "[[../../AGENTS]]"
  - "[[../../ONBOARDING-IA]]"
  - "[[../architecture/PORTABILIDAD-IA]]"
  - "[[../architecture/CONTRATO-UNIVERSAL-ORQUESTADORES]]"
  - "[[../bitacora/ESTADO-ACTIVO]]"
tags:
  - proyecto/tesis
  - tipo/guia
  - modulo/transversal
---

# Guía de cambio de IA y onboarding de modelos

Esta guía explica cómo transferir el contexto del proyecto a cualquier nuevo modelo de lenguaje o herramienta asistida por IA (OpenCode, Codex, Gemini, Claude, Cursor, ChatGPT, etc.).

## 1. Documento Maestro

El documento principal de arranque para cualquier IA vive en la raíz del repositorio:
👉 **[[../../ONBOARDING-IA|ONBOARDING-IA.md]]**

## 2. Prompt Universal de Inicialización

Al abrir el proyecto con una nueva IA o en una nueva ventana de chat, pega este mensaje:

```text
Actúa como ingeniero de software y asistente de tesis para el proyecto Zhud Alelí.
Resuelve la raíz buscando `AGENTS.md` y `.specify/memory/constitution.md` hacia arriba.
Lee `AGENTS.md`, la constitución, `agents/tesis/roles/README.md`,
`docs/00-inicio/00-dashboard.md`, `docs/bitacora/ESTADO-ACTIVO.md` y el último handoff
relacionado antes de responder. Indica la fase, el escritor permitido, la rama, el estado de
Git, lo verificado y el próximo paso permitido. No escribas si no puedes resolver la raíz.
```

## 3. Comandos de Lanzamiento por Motor

### Codex CLI
```powershell
.\scripts\agent.ps1 codex
```

### OpenCode y OpenChamber
```powershell
.\scripts\agent.ps1 opencode
.\scripts\agent.ps1 openchamber
```

### Antigravity con Gemini
```powershell
.\scripts\agent.ps1 antigravity
```

### Kimi Code CLI
```powershell
.\scripts\agent.ps1 kimi
```

### Validar raíz y hosts
```powershell
.\scripts\agent.ps1 status
```

### Arnés Autónomo Python (Laboratorio)
```powershell
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m agent_harness.cli --model gpt-5.6-luna
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m agent_harness.cli --model deepseek-v4
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m agent_harness.cli --model gemini-2.5-pro
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m agent_harness.cli --model glm-5.2
```

El laboratorio Python no inicia ni cambia sesiones de Codex, Antigravity, OpenCode u
OpenChamber. Solo prueba adaptadores y rutas de modelos configuradas para ese laboratorio.

## 4. Cambio seguro entre herramientas

1. Termina o detén el host actual.
2. Ejecuta `status` y registra un handoff desde
   `docs/templates/PLANTILLA-HANDOFF-UNIVERSAL.md` en `docs/bitacora/checkpoints/`.
3. Conserva la misma tarea, branch/worktree, `allowed_paths` y `next_action`.
4. Abre el siguiente host desde la raíz del repositorio.
5. Lee el handoff antes de escribir.
6. Mantén un solo escritor activo por worktree.

El cambio de cuota se maneja a nivel de tarea. No se intenta continuar el historial privado de
una conversación en otro proveedor.
