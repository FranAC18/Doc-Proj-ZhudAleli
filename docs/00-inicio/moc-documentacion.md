---
title: "MOC — Documentación del proyecto"
type: moc
status: active
tags:
  - proyecto/tesis
  - tipo/moc
  - estado/activo
verified_at: "2026-10-13"
---

# Mapa de documentación

## Recorrido recomendado

- [[00-dashboard]]
- [[ESTADO-ACTIVO|Estado operativo y tarea actual]]
- [[context-index|Índice de contexto para agentes]]
- [[feature-index|Índice de funcionalidad activa]]
- [Índice de ediciones finales](../../documentacion/README.md)

## Mapa del vault

| Área | Punto de entrada | Contenido |
|---|---|---|
| Inicio y decisiones pendientes | [[00-dashboard]], [[01-decisiones-pendientes]], [[02-evaluacion-documentos]] | Estado general, dudas abiertas y evaluación documental. |
| Requisitos | [[../requirements/README|Índice de requisitos]], [[../requirements/CAT-REQ-001|Catálogo vigente]] | Catálogo, propuestas y trazabilidad de validación. |
| Arquitectura y decisiones | [[../architecture/ARQUITECTURA-OBJETIVO|Arquitectura objetivo]], [[../architecture/PLAN-DESDE-CERO|Plan técnico]], [[../decisions/ADR-0006-monolito-modular-y-entrega-incremental|ADR-0006]] | Arquitectura vigente, antecedentes y decisiones. |
| Especificación técnica | [[../../specs/001-acceso-usuarias-internas/spec|SPEC-001]], [[../../specs/001-acceso-usuarias-internas/plan|Plan]], [[../../specs/001-acceso-usuarias-internas/tasks|Tareas]] | Especificación, plan y tareas de acceso. |
| Trazabilidad | [[../traceability/MATRIZ-TRAZABILIDAD|Matriz de trazabilidad]] | Relación entre requisitos, diseño, tareas y evidencia. |
| Sprints y continuidad | [[../sprints/ROADMAP-ANTEPROYECTO|Roadmap]], [[../sprints/SPRINT-00-preparacion|Sprint 0]], [[../bitacora/README|Índice de bitácora]] | Planificación, sesiones y checkpoints. |
| Evidencia | [[../evidence/README|Índice de evidencia]] | Aprobaciones, verificaciones y registros de trabajo. |
| Agentes y herramientas | [[moc-agentes-y-skills]], [[../01-agentes/moc-agentes|Agentes]], [[../02-skills/moc-skills|Skills]], [[../../agents/tesis/roles/README|Roles canónicos]] | Guías de uso; los roles canónicos están en `agents/tesis/roles/`. |
| Diseño de interfaz | [[../ui/SISTEMA-DISENO|Sistema de diseño]] | Reglas visuales y de interacción. |
| Ediciones académicas finales | [Índice de `documentacion/`](../../documentacion/README.md) | Versiones preparadas para entrega y su control de cambios. |
| Análisis interno | [Índice de `analisis/`](../../analisis/README.md) | Borradores, comparaciones y material por fecha. |
| Archivo interno | [Índice de `_archivo/`](../../_archivo/README.md) | Material sustituido con motivo y reemplazo registrados. |
| Plantillas | [[../templates/PLANTILLA-CHECKPOINT|Plantilla de checkpoint]], [[../templates/PLANTILLA-DECISION|Plantilla de decisión]], [[../templates/PLANTILLA-REQUISITO|Plantilla de requisito]] | Formatos para crear notas consistentes. |

## Agentes y arquitectura

- [[moc-agentes-y-skills]]
- [[auditoria-agentes-skills-2026-08-24]]
- [[ONBOARDING-IA]]
- [[AGENTS]]
- [[FLUJO-MULTIAGENTE]]
- [[FUENTES-DE-VERDAD]]
- [[PORTABILIDAD-IA]]
- [[PLAN-DESDE-CERO]]
- [[ARQUITECTURA-OBJETIVO]]
- [[ADR-0002-arnes-portable-de-ia]]
- [[ADR-0004-capa-abstraccion-modelos-ia]]
- [[MATRIZ-TRAZABILIDAD]]
- [[ROADMAP-ANTEPROYECTO]]
- [[SPRINT-00-preparacion]]

## Lectura y ubicación

Los documentos conservan sus rutas canónicas para mantener sus enlaces y referencias.
La tabla anterior organiza la navegación sin duplicar el contenido ni cambiar su estado.
Las carpetas ocultas de herramientas (`.agents/`, `.opencode/` y `.specify/`) contienen
adaptadores, plantillas y configuración; no son una segunda fuente de requisitos o roles.
