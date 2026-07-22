---
title: Repositorios de referencia para el arnés
type: research
status: completed
date: 2026-07-21
tags:
  - proyecto/tesis
  - tipo/investigacion
  - modulo/transversal
---

# Repositorios de referencia para el arnés

Evaluación realizada el 21 de julio de 2026. Las versiones y compatibilidades deben volver a
comprobarse antes de una actualización.

| Proyecto | Aporte útil | Encaje | Decisión |
|---|---|---|---|
| [GitHub Spec Kit](https://github.com/github/spec-kit) | Desarrollo guiado por especificaciones, 30+ agentes, plantillas y overrides | Muy alto: artefactos Markdown y flujo portable | Adoptado, versión 0.13.2 |
| [OpenSpec](https://github.com/Fission-AI/openspec) | Propuestas/cambios ligeros para proyectos existentes | Alto, pero solapa el flujo elegido | Alternativa si Spec Kit se vuelve demasiado pesado |
| [BMAD Method](https://github.com/bmad-code-org/bmad-method) | Muchos agentes y workflows de ciclo completo | Medio: duplica Scrum y añade carga de coordinación | No adoptar completo; solo tomar ideas puntuales |
| [Kimi Code](https://github.com/MoonshotAI/kimi-code) | Agente terminal, subagentes, skills, MCP y proveedores compatibles | Alto como motor alternativo Kimi/GLM | Adoptar como alternativa, sujeto a smoke test |
| [OpenCode](https://github.com/anomalyco/opencode) | Agente proveedor-agnóstico con modos plan/build | Medio-alto, pero hay incidencias recientes con GLM/Kimi | Mantener como tercera opción, no base actual |
| [Aider](https://github.com/Aider-AI/aider) | Edición en terminal, mapa del repo y Git con muchos modelos | Medio: fuerte para pair programming, menos alineado al proceso de tesis | Respaldo para tareas acotadas |
| [LiteLLM](https://github.com/BerriAI/litellm) | Gateway común para múltiples proveedores y formato OpenAI | Útil si se exige un solo endpoint | Opcional; no añadir hasta probar Responses/tool calling |

## Razón de la combinación elegida

Spec Kit resuelve la parte que sí debe sobrevivir a un cambio de IA: constitución, specs,
planes, tareas y controles. Codex y Kimi Code aportan el runtime de programación. Obsidian
consume los mismos Markdown. Esta separación evita que un gateway, una memoria privada o el
formato de un proveedor se vuelvan indispensables para continuar la tesis.

## Riesgo observado en soluciones “agnósticas”

Que una herramienta permita escribir una URL OpenAI compatible no garantiza que el modelo
maneje igual tool calling, razonamiento, streaming, subagentes o límites de contexto. Los
repositorios de OpenCode, Kimi Code y LiteLLM tienen incidencias activas en esas zonas. Por
eso cada combinación debe aprobar `evals/providers/SMOKE-TEST.md` y fijar su versión durante
un sprint.

## Qué no se copiará

- Un equipo de 12 agentes permanentes para un proyecto individual.
- Memoria automática que convierta errores en reglas sin aprobación.
- Fusión o publicación autónoma.
- Microservicios para coordinar agentes.
- Duplicación de specs por cada proveedor.
- Dependencia obligatoria de un gateway antes de demostrar su necesidad.
