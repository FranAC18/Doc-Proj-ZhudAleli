---
title: Dashboard del proyecto de tesis
type: dashboard
status: in-progress
project: tesis-zhud-aleli
updated: 2026-10-20
---

# Dashboard del proyecto

## Proyecto

[[../../agents/tesis/PROJECT_CONTEXT|Contexto del anteproyecto]]

Aplicación web para apoyar la gestión organizacional y la trazabilidad productiva del
Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud y su unidad productiva Zhud Alelí.

## Referencia actual y revisiones de requisitos

- [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.2]] fue aprobado por el tesista el 2026-10-13.
- La [lista general v2.0](../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13.md)
  contiene 58 RF y 9 RNF confirmados, 2 propuestos y 12 históricos.
- La [priorización v1.3](../../documentacion/requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13.md)
  registra importancia; no modifica la secuencia del plan de sprints.
- El tesista informa que el docente de Aplicaciones II revisó requisitos en
  clase. El [reporte registrado](../evidence/requirements/2026-10-13-reporte-revision-docente-en-clase.md)
  identifica como SIN EVIDENCIA la fecha, versión revisada, resultado y constancia.
  La revisión académica formal y la revisión de la directora siguen pendientes.
- El 2026-10-20 el tesista identificó a Maria Camas, encargada de la organización, como
  quien autorizó verbalmente, y a Julio Santillan, profesor de Aplicaciones Informáticas 2,
  como quien dio el visto bueno en una presentación. No hay actas ni constancias; fecha,
  versión y alcance exacto por precisar. El [informe para el docente](../../documentacion/seguimiento/cierre_sprint_1_y_vistos_buenos_v1.1_2026-10-20.md)
  registra el resultado y la conciliación del seguimiento local.
- La validación organizacional directa de las novedades de entrevista y el acta formal
  continúan pendientes. La aprobación del tesista está en
  [[../evidence/requirements/2026-10-13-aprobacion-propuesta-requisitos-generales-v2-2|EVID-REQ-APP-2026-10-13]].
- El [alcance general v1.3](../../documentacion/alcance/alcance_v1.3_2026-10-13.md)
  está preparado para revisión del tesista; no está aprobado en esta edición.
- Se conserva la [[../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack|evidencia de cronograma, presupuesto y stack]]
  y la [[../evidence/casos-de-uso/2026-09-28-coherencia-integral|auditoría de coherencia]] como antecedentes.

## Estado actual

- Sprint 1 (15 sep-12 oct): requisitos y diseño; timebox cerrado administrativamente el
  2026-10-20 con resultado **partially-complete**. El seguimiento local se concilió con el
  backlog: tres tareas `en_curso`, dos `bloqueada` y ninguna `verificada`. La fecha original
  de SB-S1-05 y las validaciones académica y de interfaz siguen pendientes de evidencia.
  El [[../bitacora/checkpoints/2026-10-20-reconciliacion-gantt-sprint-1|checkpoint de conciliación]] detalla el cotejo; el [[../bitacora/checkpoints/2026-10-20-cierre-sprint-1-parcial|checkpoint de cierre]] conserva el reporte de vistos buenos verbales y las brechas de trazabilidad.
- Sprint 2 (13–26 oct): incremento planificado de acceso privado, cuentas y permisos.
  El inicio del calendario no acredita implementación ni abre la puerta T012.
- Último sprint completado: [[../sprints/SPRINT-00-preparacion|Sprint 0 - Preparación]].
- Arnés portable: contrato universal implementado; Codex, OpenCode/OpenChamber y Antigravity
  comparten la fuente versionada y sus adaptadores propios. Smoke test multi-host **pasado**:
  [[../evidence/S0/2026-08-24-smoke-test-contrato-universal|Smoke test del contrato universal]].
- Codex conserva la coordinación, revisión, documenter y git-manager; OpenChamber ejecuta
  OpenCode Go y Antigravity usa Gemini mediante Google AI Pro.
- Aplicación Django: no creada ni instalada como aplicación del proyecto.
- Base de datos PostgreSQL: servicio local instalado y activo; falta crear la base de desarrollo
  del proyecto Django cuando exista `manage.py`.
- Requisitos: [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.2]] y [requisitos generales v2.0](../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13.md):
  67 confirmados (58 RF + 9 RNF), 2 propuestos y 12 históricos.
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
- [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.2 aprobado por el tesista]].
- [Lista general completa de requisitos v2.0](../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13.md).
- [Importancia de requisitos v1.3](../../documentacion/requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13.md).
- [Alcance general v1.3, pendiente de revisión](../../documentacion/alcance/alcance_v1.3_2026-10-13.md).
- [[../evidence/requirements/2026-10-13-reporte-revision-docente-en-clase|Reporte del tesista sobre revisión docente en clase]].
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

Continuar el trabajo pendiente de S1: completar la trazabilidad de requisitos, cotejar
los criterios ampliados y registrar las revisiones académica y organizacional cuando
ocurran. La arquitectura vigente sigue siendo el monolito modular de ADR-0006. El
timebox de S1 está cerrado, pero su resultado es parcial; no declarar completado el
trabajo ni abrir T012 sin sus evidencias y validaciones.

## Regla de avance

El timebox de Sprint 1 está cerrado y su resultado permanece parcialmente completo.
El tesista aprobó CAT-REQ-001 v1.2 y requisitos generales v2.0; el reporte de revisión
docente en clase no reemplaza la revisión académica formal. Cada spec, plan y porción
de implementación conserva sus propias puertas de aprobación.
