---
title: Checkpoint de alternativas de arquitectura para entrega incremental
type: checkpoint
status: partially-complete
date: 2026-10-07
task_id: ARCH-REVIEW-003
phase: pre_commit
commit: pending
commit_hash: null
branch: opencode/spec-001-fase-1-diseno
head: c2654519b041d8f96a2028482608c93ac9d8ea0b
sprint: S1
project_phase: Fase-II-diseno
module: transversal
objective: Conservar la comparación ampliada y la selección arquitectónica todavía pendiente.
decision_status: alternatives-under-evaluation
technical_review: completed-no-open-findings
constitution_current: 0.1.0
constitution_action: deferred-until-architecture-agreement
universal_final_validation: passed-with-inherited-warnings
requirement_ids:
  - RF-ACC-001
  - RF-ACC-004
  - RF-VEN-001
  - RF-PWA-002
  - RF-PWA-003
  - RNF-SEC-001
  - RNF-AUD-001
  - RNF-DAT-001
related:
  - "[[../../decisions/proposals/2026-10-07-alternativas-arquitectura-entrega-incremental]]"
  - "[[../../evidence/architecture/2026-10-07-alternativas-entrega-incremental]]"
  - "[[2026-10-07-revision-arquitectura-monolito-capas]]"
  - "[[../ESTADO-ACTIVO]]"
  - "[[../../sprints/ROADMAP-ANTEPROYECTO]]"
  - "[[../../../specs/001-acceso-usuarias-internas/plan]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/transversal
  - sprint/s1
---

# Checkpoint de alternativas de arquitectura para entrega incremental

## Estado recibido

El tesista quiere terminar un incremento útil, probarlo con las socias, incorporar el
siguiente y facilitar cambios futuros. Pidió comparar también microservicios; todavía no
decide si requiere publicación independiente. No aceptó PRO-ARCH-002 ni su enmienda.

[[../../decisions/proposals/2026-10-07-alternativas-arquitectura-entrega-incremental|PRO-ARCH-003]]
compara monolito con capas, puertos/adaptadores selectivos, servicios amplios y microservicios.
Las opciones internas y las de distribución pueden combinarse. Entregar incrementos y
publicar capacidades por separado son objetivos distintos; todas las opciones conservan
integración, regresión y validación de recorridos.

El arquitecto completó el análisis read-only de alternativas, incrementos, dependencias,
datos, permisos y PWA con recomendación provisional, según el handoff final. El reviewer
encontró un P3 sobre asumir que una función nueva requiere un servicio nuevo.
El coordinador lo corrigió para permitir ampliar el propietario o crear otro con frontera
y autonomía justificadas. El reviewer confirmó y cerró sin hallazgos accionables pendientes,
según el handoff. La selección, ADR aceptado y enmienda siguen pendientes; constitución 0.1.0
intacta. La candidata 0.2.0 de la revisión anterior no se traslada a otra alternativa.

## Handoff estructurado

| Campo | Estado |
|---|---|
| `task_id` | ARCH-REVIEW-003 |
| `requirement_ids` | IDs relacionados en el YAML; sin nuevos requisitos ni aprobación inferida. |
| `sprint` / `module` | Preparación de S1 en Fase II / transversal. |
| `objective` | Comparar incrementos, mantenibilidad, autonomía, datos, permisos y operación. |
| `changed_files` | PRO-ARCH-003 y estado activo a cargo del coordinador; esta evidencia y checkpoint a cargo de documenter. |
| `tests` | Validación universal final exit 0 con cuatro advertencias heredadas; 43 enlaces locales y whitespace de cuatro documentos comprobados sin problemas. Sin pruebas funcionales o de carga. |
| `reviewer_findings` | Único P3 corregido; reviewer confirmó cierre sin hallazgos accionables pendientes. |
| `decisions` | Alternativas bajo evaluación; ninguna seleccionada por el tesista. |
| `blockers` | Acuerdo real pendiente para seleccionar arquitectura y aplicar una enmienda. |
| `next_steps` | Aclarar prioridades de publicación/operación y presentar opciones para selección. |
| `phase` / `commit_hash` | `pre_commit` / `null`; `commit: pending`. |

Archivos principales de esta tarea:

- `docs/decisions/proposals/2026-10-07-alternativas-arquitectura-entrega-incremental.md`.
- `docs/bitacora/ESTADO-ACTIVO.md`.
- `docs/evidence/architecture/2026-10-07-alternativas-entrega-incremental.md`.
- `docs/bitacora/checkpoints/2026-10-07-alternativas-entrega-incremental.md`.

Se preservan la revisión anterior y cambios locales ajenos. Documenter solo creó los dos
últimos archivos; no modificó propuesta, estado activo, constitución, roadmap ni SPEC-001.

## Integridad, dependencias y límites

La venta multiproducto y la auditoría conservan la atomicidad aprobada. Permisos se verifican
en backend, también entre servicios y al sincronizar. Una interfaz SSR/Bootstrap común puede
consumir servicios; algunos cambios requieren publicar esa interfaz. Versiones de contratos
y comandos PWA pendientes requieren compatibilidad, autorización vigente y recuperación
según specs/P-13/P-14. Compensación no sustituye por sí sola una garantía transaccional.

El roadmap permite incrementos con dependencias satisfechas y pruebas parciales. SPEC-001
entrega acceso y bienvenida, no completa S1. El dashboard posterior consume planificación,
pendientes y encargos; reportes requieren sus fuentes. Esta tarea no realizó pruebas con
socias ni ejecutó tareas de implementación.

Rama y HEAD comprobados; `manage.py`, `apps/` y `config/` ausentes. Diff de constitución
contra HEAD: exit 0. SHA-256 comprobado:
`0E45B53EFCC32E154D8B54FF09DA24A4A6C46403C9328E74E54E6D919CA09C63`.
La validación universal final del coordinador dio exit 0, `ok: true`, `missing: []` y
`errors: []`, con cuatro advertencias heredadas. Su comprobación con Python estándar validó
43 enlaces locales y whitespace de PRO-ARCH-003, estas dos notas y estado activo: exit 0,
sin problemas. Documenter comprobó sus 19 Wikilinks y whitespace sin problemas; el diff
dirigido a docs y constitución pasó. El diff global mantiene exit 1 solo por espacios
previos en `design/style-guide/tokens.html:19` y `:75`, fuera de tarea. Las advertencias y
procedencia de cada comprobación están en EVID-ARCH-003. No hay código Django,
migraciones, rendimiento probado, publicación ni commit de esta tarea. Destinos nuevos sin
conflicto al iniciar el handoff.

## Continuación permitida

Presentar criterios de publicación/reversión independiente,
operación posterior a la tesis, contratos, dependencias de datos, disponibilidad y presupuesto.
Después de la selección y aceptación reales, elaborar el ADR y enmienda que correspondan
sin aplicar automáticamente la candidata anterior. Revisión académica, P-11/P-13/P-14,
specs futuras y despliegue conservan sus puertas propias.

La [[../../evidence/architecture/2026-10-07-alternativas-entrega-incremental|EVID-ARCH-003]]
conserva fuentes, comparación y límites. Un commit requiere autorización explícita y
validación de git-manager; `post_commit` exige hash real, rama, archivos incluidos y resultado.
