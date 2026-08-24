---
title: Portabilidad entre motores y modelos de IA
type: architecture
status: confirmed
date: 2026-08-15
related:
  - "[[../decisions/ADR-0002-arnes-portable-de-ia]]"
  - "[[../decisions/ADR-0004-capa-abstraccion-modelos-ia]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
---

# Portabilidad entre motores y modelos de IA

## Dos niveles de portabilidad

1. **Nivel Metodológico y de Desarrollo (Dev-time)**:
   * Los artefactos (`AGENTS.md`, `specs/`, `constitution.md`, `docs/`) son la fuente de verdad independiente de cualquier IA.
   * Codex CLI, Kimi Code CLI y Spec Kit operan sobre estos archivos comunes sin modificar la estructura del proyecto.
2. **Nivel de Runtime y Ejecución de Agentes (Model Abstraction Layer - MAL)**:
   * El arnés Python (`tools/agent-lab/src/agent_harness/`) implementa una arquitectura desacoplada basada en capacidades.
   * Permite alternar dinámicamente entre OpenAI (GPT-5.6 Sol/Luna), DeepSeek (V3/V4/R1), GLM (GLM-4/5.2) y Google Gemini (2.5/3.0) sin modificar la lógica del agente.

## Arquitectura de la Capa de Abstracción de Modelos (MAL)

```text
Agent / Workflow
       │
       ▼
ModelRouter (Resuelve por agente, modelo o fallback)
       │
       ▼
CapabilityValidator (Verifica tool_calling, reasoning, etc.)
       │
       ▼
<< Protocol >> ModelAdapter
 ├── OpenAIAdapter    (GPT-5.6 Sol / Luna)
 ├── DeepSeekAdapter  (DeepSeek V4 / R1 con reasoning_content)
 ├── GLMAdapter       (Z.AI Coding PaaS)
 └── GeminiAdapter    (Google GenAI nativo)
```

## Matriz de Capacidades de Modelos

| Modelo / Clave | Proveedor | Contexto | Tool Calling | Parallel Tools | Reasoning Tokens | Structured Output |
| :--- | :--- | ---: | :---: | :---: | :---: | :---: |
| `gpt-5.6-luna` | `openai` | 200k | Nativo | Sí | Sí | Strict JSON |
| `gpt-5.6-sol` | `openai` | 200k | Nativo | Sí | Sí | Strict JSON |
| `deepseek-v4` | `deepseek` | 128k | Nativo | Seguro (False) | Sí (`reasoning_content`) | JSON Schema |
| `glm-5.2` | `glm` | 1M | Nativo | Sí | Sí | JSON Mode |
| `gemini-2.5-pro` | `google` | 1M - 2M | Nativo | Sí | Sí | Strict Schema |

## Uso del CLI Multi-Modelo

Listar modelos registrados y capacidades:
```bash
python -m agent_harness.cli --list-models
```

Ejecutar una consulta con un modelo específico:
```bash
python -m agent_harness.cli --model deepseek-v4 --once "Calcula la merma de 100kg al 12%"
python -m agent_harness.cli --model gemini-2.5-pro --once "¿Qué verificaciones de seguridad requiere SPEC-001?"
```

Consultar telemetría y costos acumulados en SQLite:
```bash
python -m agent_harness.cli --telemetry
```

## Suite de Evaluación y Benchmarking

Para comparar empíricamente el rendimiento de los modelos en los casos de la tesis:
```bash
python evals/benchmark.py --dry-run
python evals/benchmark.py --models gpt-5.6-luna,deepseek-v4,glm-5.2,gemini-2.5-pro --output docs/evidence/evals/benchmark-report.md
```
