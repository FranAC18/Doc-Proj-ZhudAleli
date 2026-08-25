---
id: ADR-0004
title: Capa de abstracción de modelos de IA y arquitectura multi-proveedor
type: decision
status: accepted
date: 2026-08-15
module: transversal
accepted_by: tesista
accepted_date: 2026-08-15
related:
  - "[[ADR-0002-arnes-portable-de-ia]]"
tags:
  - proyecto/tesis
  - tipo/decision
  - modulo/transversal
---

# ADR-0004: Capa de abstracción de modelos de IA y arquitectura multi-proveedor

## Contexto

El arnés de IA y el laboratorio de agentes (`tools/agent-lab/`) dependían estrechamente del formato de la API `/chat/completions` de OpenAI. Para garantizar la sostenibilidad académica de la tesis y permitir evaluar experimentalmente múltiples familias de modelos (OpenAI GPT-5.6 Sol/Luna, DeepSeek V4/R1, GLM 5.2, Google Gemini 2.5/3.0) sin reescribir los agentes ni acoplarse a un solo proveedor, se requería una capa de abstracción formal.

## Decisión

1. **Diseñar una Capa de Abstracción de Modelos (MAL - Model Abstraction Layer)** basada en contratos canónicos (`Message`, `ToolCall`, `ModelResponse`, `ModelCapability`) y el protocolo `ModelAdapter`.
2. **Implementar adaptadores dedicados** para cada familia de proveedores:
   * `OpenAIAdapter`: OpenAI oficial y endpoints compatibles.
   * `DeepSeekAdapter`: Soporte nativo para extracción de `reasoning_content`.
   * `GLMAdapter`: Integración con Z.AI Coding PaaS.
   * `GeminiAdapter`: Mapeo al formato nativo de Google Gemini (`functionDeclarations`, `functionResponse`).
3. **Implementar un Sistema de Capacidades (`CapabilityValidator`)** para validar que un modelo soporte las características requeridas por un agente (ej. `TOOL_CALLING`, `REASONING_TOKENS`, `VISION`) antes de ejecutar la llamada a la red.
4. **Implementar un Enrutador Dinámico (`ModelRouter`)** que permita resolver modelos por variable de entorno, flag CLI o política de agente, incluyendo cadenas de *fallback* protegidas.
5. **Añadir telemetría y estimación de costos normalizada** persistida en SQLite para respaldar empíricamente los capítulos de evaluación de la tesis.

## Motivos

* Evita la dispersión de condicionales de tipo `if provider == "openai":` por todo el código.
* Permite comparar empíricamente la calidad de código, costo y latencia entre proveedores bajo condiciones idénticas de prueba.
* No añade dependencias externas pesadas ni pasarelas intermedias obligatorias.
* Mantiene la compatibilidad hacia atrás con el código existente del laboratorio y los contratos de Obsidian.

## Consecuencias

### Positivas
* El agente no conoce la implementación ni la API del proveedor subyacente.
* Incorporar un nuevo modelo o proveedor requiere únicamente crear una clase derivada de `ModelAdapter`.
* Registro detallado de tokens y costos en SQLite para análisis científico en la tesis.

### Costes y riesgos
* Cada nuevo proveedor exige mantener su adaptador actualizado ante cambios de versión de API.
* Modelos sin capacidades de razonamiento profundo o tool calling estructurado pueden requerir ajustes en sus prompts o ser descartados por el validador.

## Validación técnica

- [x] 21 pruebas unitarias y de contrato pasando en `pytest tools/agent-lab/tests`.
- [x] Selección dinámica de modelos y listado de capacidades verificado en CLI.
- [x] Ejecución de benchmark multi-modelo reproducible en `evals/benchmark.py`.
- [x] Cero credenciales ni secretos versionados en Git.
