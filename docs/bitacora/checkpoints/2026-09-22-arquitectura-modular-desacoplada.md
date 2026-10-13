---
title: Checkpoint - propuesta de arquitectura modular desacoplada
type: checkpoint
status: partially-complete
date: 2026-09-22
task_id: HARNESS-ARCH-001
phase: pre_commit
commit: pending
branch: opencode/spec-001-fase-1-diseno
head: a6e842f63917b2ac28a64c80b00d68069ba2fabd
writer: documenter
handoff_to: reviewer
allowed_paths:
  - docs/decisions/proposals/2026-09-22-arquitectura-modular-desacoplada.md
  - docs/bitacora/checkpoints/2026-09-22-arquitectura-modular-desacoplada.md
forbidden_paths:
  - .env
  - .venv/**
  - db.sqlite3
  - secrets/**
  - apps/**
  - config/**
related:
  - "[[../../decisions/proposals/2026-09-22-arquitectura-modular-desacoplada]]"
  - "[[../../architecture/ARQUITECTURA-OBJETIVO]]"
  - "[[../../decisions/ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[../ESTADO-ACTIVO]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - estado/proposed
  - modulo/transversal
---

# Checkpoint - propuesta de arquitectura modular desacoplada

## Contexto

Se recibió una solicitud para abandonar un monolito tradicional acoplado y documentar una
arquitectura que permita iterar por módulos, desplegar de forma simple y probar cada contexto.
La fuente de alcance entregada describe la gestión organizacional y trazabilidad productiva del
Comité, cinco módulos, Django/PostgreSQL/Bootstrap/PWA y 16 semanas.

## Resultado registrado

Se redactó la propuesta `PRO-ADR-004` con bounded contexts, contratos de comunicación, estructura
de directorios, reglas de persistencia, roadmap de ocho fases y ruta de migración strangler.
La propuesta recomienda un monolito modular desacoplado; no cambia la constitución aprobada ni
convierte la decisión en un ADR aceptado. Posteriormente, con autorización explícita del tesista,
se actualizó `docs/architecture/PLAN-DESDE-CERO.md` para incorporar el Plan Maestro de 16 semanas,
PWA offline-first con outbox por puerta, contratos HTTP de sincronización y la normalización de
apps a `accounts`, `traceability` y `reports`.

## Hechos verificados

- La raíz y la rama fueron comprobadas antes de escribir. El `HEAD` real es
  `a6e842f63917b2ac28a64c80b00d68069ba2fabd`; `ESTADO-ACTIVO.md` conserva el valor anterior
  `73e3c0f68cbb7539aaec5478a83c9e288b80e617`, por lo que existe drift operativo pendiente.
- La constitución 0.1.0 y ADR-0003 ya establecen Django modular, PostgreSQL y la raíz del
  repositorio.
- `SPEC-001` está confirmada y limitada al acceso interno; no se creó código ni se alteraron
  sus artefactos.
- `.specify/scripts/bash/setup-plan.sh --json` se ejecutó; detectó el plan existente de
  `specs/001-acceso-usuarias-internas` y no lo sobrescribió.
- No existe `.specify/extensions.yml`; no hubo hooks de constitución o planificación.
- La auditoría universal devuelve `ok: true` después de sincronizar el `HEAD` documentado; mantiene
  tres advertencias de enlaces heredados no resueltos. No se atribuyen esos hallazgos a esta
  propuesta.
- Se dejó explícita la discrepancia entre la sincronización offline automática del texto pegado y
  la línea base validada; el nuevo plan la incorpora con una puerta de spec, conflicto e
  idempotencia por módulo.
- El tesista autorizó planificar e implementar la nueva arquitectura; la revisión de la directora
  y la aceptación formal del ADR permanecen pendientes.

## Archivos escritos

- `docs/decisions/proposals/2026-09-22-arquitectura-modular-desacoplada.md`
- `docs/architecture/PLAN-DESDE-CERO.md`
- `docs/bitacora/checkpoints/2026-09-22-arquitectura-modular-desacoplada.md`

## Verificaciones pendientes

- Revisión independiente de límites, contratos y estrategia de persistencia.
- Revisar el diff completo antes de cualquier commit. La comprobación global de `git diff --check`
  también encontró espacios finales
  preexistentes en `design/style-guide/tokens.html`; los dos archivos nuevos no tienen espacios
  finales.
- Validación humana de las decisiones abiertas enumeradas en la propuesta.
- Promoción posterior a ADR aceptado después de la revisión de la directora y la aprobación
  formal correspondiente.

## Próximo paso

Entregar el plan para revisión arquitectónica; mantener `commit: pending`, continuar solo con
`SPEC-001` y preparar specs/tareas de los módulos futuros antes de escribir código PWA, outbox,
asistencia, trazabilidad o reportes.
