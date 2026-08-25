---
title: Índice de funcionalidades activas
type: feature-context-index
status: active
updated: 2026-08-25
---

# Índice de funcionalidades activas

## SPEC-001 — Acceso de usuarias internas

| Campo | Valor |
|---|---|
| Estado | `confirmed` |
| Plan | `approved` |
| Tareas | `planned` |
| Fase actual | Diseño del sistema; todavía sin Django |
| Alcance inmediato | Hoja de estilos y modelo conceptual de `accounts` |
| Fuente principal | [`spec.md`](../../specs/001-acceso-usuarias-internas/spec.md) |
| Plan | [`plan.md`](../../specs/001-acceso-usuarias-internas/plan.md) |
| Tareas | [`tasks.md`](../../specs/001-acceso-usuarias-internas/tasks.md) |

### Recuperación por tipo de tarea

- Arquitectura: abrir únicamente las secciones de arquitectura y datos relevantes de
  `spec.md`, `plan.md`, `data-model.md` y ADRs relacionados.
- Planificación: abrir requisitos, alcance, dependencias y criterios de `spec.md` y `plan.md`.
- Implementación: abrir `tasks.md`, la tarea asignada y los archivos relacionados; no abrir
  artefactos de fases futuras.
- Frontend: abrir `docs/ui/SISTEMA-DISENO.md`, la tarea asignada y `design/` relevante.
- Revisión: abrir diff, criterios y pruebas de la tarea; añadir contratos solo si están afectados.

### Artefactos bajo demanda

| Artefacto | Cuándo abrirlo |
|---|---|
| `research.md` | Solo si se revisa una decisión de investigación. |
| `data-model.md` | Solo si se revisa modelo, migración o integridad de datos. |
| `contracts/http.md` | Solo si se revisan rutas, formularios o contratos HTTP. |
| `quickstart.md` | Solo para reproducir el entorno o sus verificaciones. |
| `checklists/requirements.md` | Solo al revisar completitud de requisitos. |

La implementación de la aplicación continúa bloqueada hasta que la fase de diseño tenga la
validación humana indicada en `tasks.md`.
