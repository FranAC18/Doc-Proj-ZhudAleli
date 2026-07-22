---
title: Dashboard del proyecto de tesis
type: dashboard
status: in-progress
project: tesis-zhud-aleli
updated: 2026-07-21
---

# Dashboard del proyecto

## Proyecto

[[../../agents/tesis/PROJECT_CONTEXT|Contexto del anteproyecto]]

Aplicación web para apoyar la gestión organizacional y la trazabilidad productiva del
Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud y su unidad productiva Zhud Alelí.

## Estado actual

- Fase: levantamiento y validación de requisitos.
- Último sprint cerrado: [[../sprints/SPRINT-00-preparacion|Sprint 0 - Preparación]].
- Arnés portable: Codex validado como motor principal; Kimi/GLM son alternativas opcionales.
- Constitución: aprobada por el tesista; la comparación con otros motores es opcional.
- Aplicación Django: no creada ni instalada como aplicación del proyecto.
- Base de datos PostgreSQL: no creada ni configurada.
- Requisitos: deben levantarse y validarse con la organización.
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

Iniciar el levantamiento de requisitos y convertir únicamente los requisitos validados en
especificaciones propuestas. Kimi y GLM son opcionales. Django y PostgreSQL solo comenzarán
cuando existan especificaciones aprobadas y diseño técnico suficiente.

## Regla de avance

Sprint 0 está cerrado con evidencia y confirmación humana. Cada fase siguiente conserva sus
propias puertas de aprobación antes de implementar.
