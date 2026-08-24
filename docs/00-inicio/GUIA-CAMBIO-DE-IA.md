---
title: Guía de cambio de IA y onboarding de modelos
type: guide
status: confirmed
date: 2026-08-15
related:
  - "[[../../AGENTS]]"
  - "[[../../ONBOARDING-IA]]"
  - "[[../architecture/PORTABILIDAD-IA]]"
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
Lee obligatoriamente `ONBOARDING-IA.md` y `AGENTS.md` para situarte en el contexto actual, estado del sprint y reglas de operación antes de responder.
Indica en qué fase nos encontramos y cuál es el próximo paso permitido.
```

## 3. Comandos de Lanzamiento por Motor

### OpenCode
```bash
opencode --model gpt-5.6-luna
opencode --model deepseek/deepseek-v4
```

### Codex CLI
```powershell
.\scripts\agent.ps1 codex
```

### Kimi Code CLI
```powershell
.\scripts\agent.ps1 kimi
```

### Arnés Autónomo Python (Laboratorio)
```powershell
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m agent_harness.cli --model gpt-5.6-luna
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m agent_harness.cli --model deepseek-v4
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m agent_harness.cli --model gemini-2.5-pro
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m agent_harness.cli --model glm-5.2
```
