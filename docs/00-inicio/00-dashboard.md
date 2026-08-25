---
title: Dashboard del proyecto de tesis
type: dashboard
status: in-progress
project: tesis-zhud-aleli
updated: 2026-08-24
---

# Dashboard del proyecto

## Proyecto

[[../../agents/tesis/PROJECT_CONTEXT|Contexto del anteproyecto]]

Aplicación web para apoyar la gestión organizacional y la trazabilidad productiva del
Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud y su unidad productiva Zhud Alelí.

## Estado actual

- Fase: preparación técnica del Sprint 1 sobre la línea base aprobada.
- Último sprint cerrado: [[../sprints/SPRINT-00-preparacion|Sprint 0 - Preparación]].
- Arnés portable: contrato universal implementado; Codex, OpenCode/OpenChamber y Antigravity
  comparten la fuente versionada y sus adaptadores propios. Smoke test multi-host **pasado**:
  [[../evidence/S0/2026-08-24-smoke-test-contrato-universal|Smoke test del contrato universal]].
- Codex conserva la coordinación, revisión, documenter y git-manager; OpenChamber ejecuta
  OpenCode Go y Antigravity usa Gemini mediante Google AI Pro.
- Aplicación Django: no creada ni instalada como aplicación del proyecto.
- Base de datos PostgreSQL: servicio local instalado y activo; falta crear la base de desarrollo
  del proyecto Django cuando exista `manage.py`.
- Requisitos: [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.0]] aprobado con 57 IDs
  `confirmed`, 2 `proposed` y 12 `superseded`.
- Primera especificación: [[../../specs/001-acceso-usuarias-internas/spec|SPEC-001 — Acceso
  de usuarias internas]] en `confirmed`.
- Plan técnico: [[../../specs/001-acceso-usuarias-internas/plan|Plan de SPEC-001]] `approved`
  por el tesista el 2026-08-24; `tasks.md` generado y análisis de coherencia realizado.
- Estructura raíz: [[../decisions/ADR-0003-estructura-raiz-aplicacion-django|ADR-0003]]
  aceptada; Django se desarrollará directamente en la raíz del repositorio.
- Diseño visual: criterios propuestos; identidad y prototipo pendientes de validación.
- Código de producción: todavía no iniciado.
- Entorno: Python 3.12, `uv` y PostgreSQL disponibles; la ruta de los clientes PostgreSQL debe
  quedar documentada o incorporarse al entorno reproducible del proyecto.

## Arquitectura y proceso

- [[../architecture/PLAN-DESDE-CERO|Plan de implementación desde cero]].
- [[../architecture/ARQUITECTURA-OBJETIVO|Arquitectura objetivo]].
- [[../architecture/PORTABILIDAD-IA|Portabilidad de motores y modelos]].
- [[../architecture/FLUJO-MULTIAGENTE|Flujo multiagente]].
- [[../architecture/CONTRATO-UNIVERSAL-ORQUESTADORES|Contrato universal de orquestadores]].
- [[../architecture/RUTAS-MODELOS-IA|Rutas universales de hosts y modelos]].
- [[../bitacora/ESTADO-ACTIVO|Estado activo de continuidad]].
- [[../../agents/tesis/roles/README|Contratos canónicos de roles]].
- [[../architecture/FUENTES-DE-VERDAD|Fuentes de verdad]].
- [[../architecture/REFERENTES-GITHUB|Repositorios de referencia]].
- [[../decisions/ADR-0002-arnes-portable-de-ia|ADR del arnés portable]].
- [[../ui/SISTEMA-DISENO|Sistema de diseño y UX]].
- [[../traceability/MATRIZ-TRAZABILIDAD|Matriz de trazabilidad]].
- [[../evidence/S0/2026-07-21-verificacion-base-v3|Verificación técnica de la base v3]].
- [[../evidence/S0/2026-07-21-smoke-test-codex|Smoke test de Codex para Sprint 0]].
- [[../evidence/S0/2026-08-24-smoke-test-contrato-universal|Smoke test del contrato universal de orquestadores]].
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
- [[../bitacora/checkpoints/2026-07-25-preparacion-spec-001-acceso|Preparación de SPEC-001]].
- [[../../specs/001-acceso-usuarias-internas/spec|SPEC-001 — Acceso de usuarias internas]].
- [[../../specs/001-acceso-usuarias-internas/plan|Plan técnico de SPEC-001]].
- [[../../specs/001-acceso-usuarias-internas/research|Investigación técnica de SPEC-001]].
- [[../../specs/001-acceso-usuarias-internas/data-model|Modelo de datos de SPEC-001]].
- [[../../specs/001-acceso-usuarias-internas/contracts/http|Contrato HTTP de SPEC-001]].
- [[../../specs/001-acceso-usuarias-internas/quickstart|Guía de verificación de SPEC-001]].
- [[../bitacora/checkpoints/2026-07-25-plan-spec-001-borrador|Checkpoint del plan de
  SPEC-001]].
- [[../decisions/ADR-0003-estructura-raiz-aplicacion-django|ADR-0003 — Estructura raíz para
  Django y agentes]].
- [[02-evaluacion-documentos|Evaluación de documentos previos]].
- [[../metodologia/METODOLOGIA-BASE|Metodología base]].
- [[../sprints/ROADMAP-ANTEPROYECTO|Roadmap oficial de sprints]].
- [[ESTADOS-Y-PROGRESO|Estados y progreso]].
- [[VISTAS-OBSIDIAN|Vistas recomendadas de Obsidian]].
- [[GIT-Y-GITHUB|Flujo de versionamiento con GitHub]].
- [[../bitacora/README|Bitácora de desarrollo]].

## Reglas y contexto del agente

- [[../../ONBOARDING-IA|Guía rápida de Onboarding para cualquier IA]].
- [[GUIA-CAMBIO-DE-IA|Guía de cambio de motor o IA]].
- [[../../AGENTS|Contrato común del repositorio]].
- Constitución de ingeniería: fuente del agente en `.specify/memory/constitution.md`; revisarla desde VS Code.
- [[../../agents/tesis/AGENT|Reglas del agente de desarrollo]].
- [[../../agents/tesis/KNOWLEDGE_POLICY|Política de conocimiento]].
- [[../../agents/tesis/OBSIDIAN_POLICY|Política de Obsidian]].

## Próximo paso permitido

Confirmar con el tesista la selección concreta de modelos y cuotas por host (en uso
`opencode:big-pickle` vs `deepseek-v4` propuesto en `RUTAS-MODELOS-IA.md`); después continuar las
tareas aprobadas de `SPEC-001` (Fase 1: diseño sin Django). La implementación de S1 se limita a
`accounts` y acceso; no se crean apps ni reglas operativas de sprints futuros.

## Regla de avance

Sprint 0 está cerrado y CAT-REQ-001 v1.0 ya tiene confirmación humana. Cada spec, plan y
porción de implementación conserva sus propias puertas de aprobación.
