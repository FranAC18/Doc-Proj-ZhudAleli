---
title: Evidencia de evolución modular y versiones piloto
type: evidence
id: EVID-ARCH-004
status: partially-complete
date: 2026-10-08
task_id: ARCH-REVIEW-004
phase: pre_commit
commit: pending
commit_hash: null
branch: opencode/spec-001-fase-1-diseno
head: c2654519b041d8f96a2028482608c93ac9d8ea0b
sprint: S1
module: transversal
decision_status: pending-human-agreement
technical_review: completed-no-open-findings
constitution_current: 0.1.0
universal_final_validation: passed-with-inherited-warnings
requirement_ids: [RF-VEN-002, RNF-DAT-001, RNF-SEC-001]
related:
  - "[[../../decisions/proposals/2026-10-08-evolucion-modular-y-versiones-piloto]]"
  - "[[../../bitacora/checkpoints/2026-10-08-evolucion-modular-y-versiones-piloto]]"
  - "[[../../../specs/001-acceso-usuarias-internas/plan]]"
tags: [proyecto/tesis, tipo/arquitectura, modulo/transversal, sprint/s1]
---

# Evidencia de evolución modular y versiones piloto

## Objetivo y resultado revisado

El tesista aclaró que busca incorporar capacidades futuras, versionar avances en el
repositorio y publicar incrementos utilizables para probarlos con las socias. Facturación,
clientes y funciones relacionadas con ARCSA son ejemplos: no aprueban requisitos ni arquitectura.
[[../../decisions/proposals/2026-10-08-evolucion-modular-y-versiones-piloto|PRO-ARCH-004]]
conserva el análisis, las fuentes y la recomendación de monolito modular con capas internas.

El arquitecto entregó un informe read-only: identidad comercial mínima distinta de
`accounts.User`, dueño único, migración posterior y contenido histórico del receptor;
RF-VEN-002 no se reinterpreta como regla fiscal. El reviewer revisó propuesta, referencias,
enlaces y diff, y cerró sin hallazgos accionables ni impedimentos, según el handoff del coordinador.

Versionar el repositorio, publicar una aplicación piloto y desplegar servicios de forma
independiente son acciones distintas. La propuesta no garantiza capacidad de carga ni cambios
limitados siempre a una carpeta. Los permisos, integridad, migraciones y compatibilidad PWA
conservan sus puertas. La aceptación, ADR y enmienda constitucional siguen pendientes.

## Evidencia real

| Comprobación | Resultado y procedencia |
|---|---|
| Rama, HEAD y destinos nuevos | Documenter comprobó los valores del YAML y ambos destinos libres. |
| Raíz y vault | Coordinador: `AGENTS.md`, constitución y `.obsidian` presentes. |
| Aplicación Django | Coordinador: `manage.py`, `apps` y `config` ausentes. |
| `git diff --check` dirigido a docs y constitución | Exit 0, comunicado por el coordinador. |
| Constitución y plan de SPEC-001 frente a HEAD | Sin diff, exit 0, comunicado por el coordinador. |
| SHA-256 de constitución | Coincide con el original, comprobado por el coordinador. |
| `python tools/validate-universal.py --json`, coordinador | Exit 0, `ok: true`, `missing/errors: []`; estado, rama/HEAD y ARCH-REVIEW-004 coherentes. |
| Chequeo Python estándar del coordinador | 4 documentos, 32 enlaces locales, destinos/whitespace sin problemas; exit 0. |
| Chequeo directo de documenter | 10 Wikilinks y whitespace de sus dos notas sin problemas; diff dirigido exit 0. |

SHA-256 conservado: `0E45B53EFCC32E154D8B54FF09DA24A4A6C46403C9328E74E54E6D919CA09C63`.
La validación final conserva cuatro advertencias heredadas: MOC frente a `73e3c0f` y enlaces
de ejemplo de `ESTADOS-Y-PROGRESO` a `RF-001-autenticacion`, `Tarea-configurar-rbac` y
`SPRINT-01-acceso`; sin errores nuevos. El coordinador repitió el diff dirigido con exit 0.
Fuentes usadas: PRO-ARCH-004, estado activo y handoff del coordinador con informes de
arquitecto/reviewer y resultados de verificación. No se atribuye ejecución propia a los checks recibidos.

## Límites y continuación

No hubo implementación, piloto con socias, pruebas de carga, servicio externo, commit, push
ni despliegue en esta tarea. La constitución sigue en 0.1.0 y el plan aprobado no cambió.
La documentación es `pre_commit`; HEAD no identifica un commit de ARCH-REVIEW-004.

Pendiente: obtener acuerdo arquitectónico explícito
antes de ADR/enmienda. Cualquier capacidad fiscal/sanitaria requiere su investigación y
validación propias; un piloto posterior exige entorno, alcance y autorización concretos.
El [[../../bitacora/checkpoints/2026-10-08-evolucion-modular-y-versiones-piloto|checkpoint]]
conserva el handoff. Una evidencia `post_commit` requiere hash real, archivos y validación.
