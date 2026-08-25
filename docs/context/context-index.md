---
title: Índice operativo de contexto
type: context-index
status: active
updated: 2026-08-25
source_of_truth: "AGENTS.md"
---

# Índice operativo de contexto

Este índice define la recuperación mínima para una tarea. No es una copia de las fuentes.
Si un documento no aparece aquí o en el índice de la funcionalidad activa, no se carga por
defecto.

## Siempre

| Fuente | Uso |
|---|---|
| `AGENTS.md` | Reglas no negociables, gobierno y límites de escritura. |
| `docs/bitacora/ESTADO-ACTIVO.md` | Rama, `HEAD`, tarea, rutas y próximo paso. |
| `tools/agent-routes.toml` | Clasificación, perfil de modelo y nivel de revisión. |

## Según la tarea

| Tipo | Leer primero | Agente recomendado |
|---|---|---|
| `architecture` | Constitución, arquitectura/ADR relevantes, feature index | `architect` |
| `planning` | Requisitos, constitución, arquitectura, feature index | `architect` |
| `implementation` | `tasks.md`, spec relevante, código y pruebas | `implementer` |
| `frontend` | Reglas UI, design system, componentes y assets relevantes | `frontend` |
| `debugging` | Síntoma, archivos afectados, pruebas y contratos relacionados | `implementer` |
| `research` | Solo las fuentes necesarias para responder | `researcher` |
| `review` | Diff, archivos modificados, pruebas, contratos y reglas | `reviewer` |
| `documentation` | Fuente concreta, plantilla y ruta autorizada | `documenter` |

## Funcionalidad activa

Leer [`feature-index.md`](feature-index.md) antes de abrir cualquier artefacto de una spec.
No leer automáticamente `research.md`, `data-model.md`, `contracts/` o `quickstart.md`:
se abren únicamente si la tarea los necesita.

## Fuentes de verdad

1. Requisitos validados y evidencia de campo.
2. Especificaciones y ADR aprobados.
3. Código, migraciones y pruebas.
4. Documentación oficial vigente.
5. Propuestas e historial.
6. Conversación y memoria como contexto auxiliar.

## Referencia, no contexto normal

- `README.md`, `ONBOARDING-IA.md` y las notas de `docs/01-agentes/` y `docs/02-skills/`.
- Auditorías fechadas, propuestas superseded y checkpoints completados.
- `.obsidian/workspace*.json`, gráficos y configuración visual de Obsidian.
- `tools/agent-lab/`, que es un laboratorio separado y no la memoria de Codex/OpenCode.

## Reglas de lectura

- Seguir enlaces solo hasta cubrir el criterio de la tarea.
- Preferir secciones relevantes y no documentos completos cuando el artefacto lo permita.
- Si dos fuentes difieren, detener la decisión y reportar la discrepancia según la jerarquía.
- Antes de escribir, comprobar `allowed_paths`, `forbidden_paths`, rama y `HEAD`.
