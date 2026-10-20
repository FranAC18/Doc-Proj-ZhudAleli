---
title: Índice de funcionalidades activas
type: feature-context-index
status: active
updated: 2026-10-20
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

Compatibilidad arquitectónica 2026-10-08: ADR-0006 adoptó la raíz, ORM, modelos/migraciones
nativos y capas proporcionales; la constitución vigente 1.0.0 conserva esa arquitectura. ADR-0007
regula solo el cierre administrativo de los periodos. El plan de SPEC-001 conserva su estructura
sin servicios, `core`, API o apps vacías. Su validación de diseño continúa siendo necesaria para
esa implementación; cerrar un sprint no marca la spec o sus tareas como completadas.

## Cambios de producto posteriores a la línea base

El [[../requirements/CAT-REQ-001|catálogo v1.1 aprobado por el tesista]] incorpora
las capacidades obligatorias offline con sus criterios. No amplía SPEC-001 con datos de negocio, cuentas offline o
caché privado. Las specs de asistencia/pesajes/sincronización siguen pendientes.
La [[../evidence/casos-de-uso/2026-09-28-coherencia-integral|auditoría integral]] documenta la
compatibilidad y las correcciones de dependencias de tasks.md, sin marcar tareas terminadas.
