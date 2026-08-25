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
   * Codex, OpenCode/OpenChamber, Antigravity, Kimi Code y Spec Kit operan sobre estos archivos
     comunes; cada host conserva su adaptador local sin duplicar la fuente canónica.
2. **Nivel de Runtime y Ejecución de Agentes (Model Abstraction Layer - MAL)**:
   * El arnés Python (`tools/agent-lab/src/agent_harness/`) implementa una arquitectura desacoplada basada en capacidades.
   * Permite alternar dinámicamente entre OpenAI (GPT-5.6 Sol/Luna), DeepSeek (V4), GLM (GLM-4/5.2) y Google Gemini (2.5 y los identificadores 3.7 Flash, 3.6 Flash, 3.5 Flash y 3.1 Pro proporcionados para este entorno) sin modificar la lógica del agente.

La capa Python enruta modelos y capacidades, pero no controla las sesiones de Codex,
Antigravity u OpenChamber ni transfiere cuotas de suscripciones. La continuidad entre hosts se
implementa mediante los contratos canónicos de `agents/tesis/roles/` y handoffs versionados.

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

## Matriz de capacidades del adaptador

El laboratorio separa dos conceptos para no confundir documentación del proveedor con
evidencia reproducible:

- `declared_capabilities`: capacidades declaradas por el adaptador o esperadas del proveedor;
  no habilitan por sí solas una ruta operativa.
- `verified_capabilities`: capacidades respaldadas por la implementación y las pruebas locales;
  son las únicas que usa `ModelRouter` y `CapabilityValidator` para seleccionar un modelo.

| Adaptador | Declaradas | Verificadas localmente | Disponibilidad del modelo/API |
| :--- | :--- | :--- | :--- |
| OpenAI | tool calling, parallel tools, structured output, JSON schema, system messages, reasoning, streaming | tool calling, system messages | Por verificar con credencial y endpoint reales |
| DeepSeek | tool calling, structured output, JSON schema, system messages, reasoning, contexto 100k, streaming | tool calling, system messages, reasoning | `deepseek-v4` debe confirmarse en el catálogo del proveedor |
| GLM | tool calling, parallel tools, structured output, system messages, reasoning, contexto 1M, streaming | tool calling, system messages | Por verificar con credencial y endpoint reales |
| Gemini | tool calling, parallel tools, structured output, JSON schema, system messages, reasoning, visión, contexto 1M, streaming | tool calling, system messages | Los IDs Gemini 3.x deben probarse mediante el canal elegido |

La propiedad histórica `capabilities` permanece como alias de `verified_capabilities` para
compatibilidad, pero no vuelve a declarar las capacidades no verificadas como disponibles.

## Uso del CLI Multi-Modelo

El identificador del modelo debe conservar su proveedor real. OpenCode Go usa rutas del tipo
`opencode-go/<modelo>`; Antigravity puede usar slugs propios con nivel de esfuerzo. No se deben
reutilizar esos nombres como prueba de acceso a una API diferente.

Listar modelos registrados y capacidades:
```bash
python -m agent_harness.cli --list-models
```

Ejecutar una consulta con un modelo específico:
```bash
python -m agent_harness.cli --model deepseek-v4 --once "Calcula la merma de 100kg al 12%"
python -m agent_harness.cli --model gemini-3.1-pro --once "¿Qué verificaciones de seguridad requiere SPEC-001?"

# Resolver el modelo configurado para el agente documenter del laboratorio:
python -m agent_harness.cli --agent-name documenter --once "Prepara el resumen documental de la tarea indicada."
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
