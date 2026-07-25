---
title: Dashboard del proyecto de tesis
type: dashboard
status: in-progress
project: tesis-zhud-aleli
updated: 2026-07-25
---

# Dashboard del proyecto

## Proyecto

[[../../agents/tesis/PROJECT_CONTEXT|Contexto del anteproyecto]]

Aplicación web para apoyar la gestión organizacional y la trazabilidad productiva del
Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud y su unidad productiva Zhud Alelí.

## Estado actual

- Fase: levantamiento y validación de requisitos; primera línea base aprobada.
- Último sprint cerrado: [[../sprints/SPRINT-00-preparacion|Sprint 0 - Preparación]].
- Arnés portable: Codex validado como motor principal; Kimi/GLM son alternativas opcionales.
- Constitución: aprobada por el tesista; la comparación con otros motores es opcional.
- Aplicación Django: no creada ni instalada como aplicación del proyecto.
- Base de datos PostgreSQL: no creada ni configurada.
- Requisitos: [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.0]] aprobado con 57 IDs
  `confirmed`, 2 `proposed` y 12 `superseded`.
- Diseño visual: criterios propuestos; identidad y prototipo pendientes de validación.
- Código de producción: todavía no iniciado.

## Arquitectura y proceso

- [[../architecture/PLAN-DESDE-CERO|Plan de implementación desde cero]].
- [[../architecture/ARQUITECTURA-OBJETIVO|Arquitectura objetivo]].
- [[../architecture/PORTABILIDAD-IA|Portabilidad de motores y modelos]].
- [[../architecture/FLUJO-MULTIAGENTE|Flujo multiagente]].
- [[../architecture/FUENTES-DE-VERDAD|Fuentes de verdad]].
- [[../architecture/REFERENTES-GITHUB|Repositorios de referencia]].
- [[../decisions/ADR-0002-arnes-portable-de-ia|ADR del arnés portable]].
- [[../ui/SISTEMA-DISENO|Sistema de diseño y UX]].
- [[../traceability/MATRIZ-TRAZABILIDAD|Matriz de trazabilidad]].
- [[../evidence/S0/2026-07-21-verificacion-base-v3|Verificación técnica de la base v3]].
- [[../evidence/S0/2026-07-21-smoke-test-codex|Smoke test de Codex para Sprint 0]].
- [[../evidence/S0/2026-07-21-verificacion-cierre-sprint-0|Verificación final de Sprint 0]].

## Documentos de inicio

- [[../sprints/SPRINT-00-preparacion|Sprint 0 - Preparación]].
- [[../decisions/ADR-0001-base-del-proyecto|Decisión técnica inicial]].
- [[../requirements/README|Cómo documentar requisitos]].
- [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.0 aprobado]].
- [[../requirements/proposals/2026-07-22-catalogo-revisado-requisitos-r3|CAT-REQ-001-R3 histórico]].
- [[../evidence/fase-i/2026-07-22-respuestas-tesista-cat-req-001-r3|Fuente del tesista registrada]].
- [[../evidence/fase-i/2026-07-22-validacion-cat-req-001-v1|Validación humana del catálogo]].
- [[../evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0|Acta de Levantamiento de requisitos 1.0]].
- [[../bitacora/checkpoints/2026-07-22-catalogo-r3-para-validacion|Checkpoint de preparación de R3]].
- [[../bitacora/checkpoints/2026-07-22-validacion-cat-req-001-v1|Checkpoint de validación de CAT-REQ-001]].
- [[../bitacora/checkpoints/2026-07-25-versionado-fase-i-y-factibilidad-acceso|Versionado de Fase I y factibilidad de la primera spec]].
- [[02-evaluacion-documentos|Evaluación de documentos previos]].
- [[../metodologia/METODOLOGIA-BASE|Metodología base]].
- [[../sprints/ROADMAP-ANTEPROYECTO|Roadmap oficial de sprints]].
- [[ESTADOS-Y-PROGRESO|Estados y progreso]].
- [[VISTAS-OBSIDIAN|Vistas recomendadas de Obsidian]].
- [[GIT-Y-GITHUB|Flujo de versionamiento con GitHub]].
- [[../bitacora/README|Bitácora de desarrollo]].

## Reglas y contexto del agente

- [[../../AGENTS|Contrato común del repositorio]].
- Constitución de ingeniería: fuente del agente en `.specify/memory/constitution.md`; revisarla desde VS Code.
- [[../../agents/tesis/AGENT|Reglas del agente de desarrollo]].
- [[../../agents/tesis/KNOWLEDGE_POLICY|Política de conocimiento]].
- [[../../agents/tesis/OBSIDIAN_POLICY|Política de Obsidian]].

## Próximo paso permitido

Crear la spec en borrador `001-acceso-usuarias-internas` para `RF-ACC-001` y los RNF
aplicables, según
[[../evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0|ACT-REQ-001]]. La spec debe
incorporar las aclaraciones de acceso, excluir `RF-ACC-002` a `RF-ACC-004` y recibir
confirmación humana antes del plan. Django y PostgreSQL siguen sin crearse hasta aprobar la
spec, su plan y sus tareas.

## Regla de avance

Sprint 0 está cerrado y CAT-REQ-001 v1.0 ya tiene confirmación humana. Cada spec, plan y
porción de implementación conserva sus propias puertas de aprobación.
