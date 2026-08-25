---
title: Preparación de SPEC-001 — Acceso de usuarias internas
type: checkpoint
status: completed
date: 2026-07-25
sprint: s1
module: acceso
related:
  - "[[../../../specs/001-acceso-usuarias-internas/spec]]"
  - "[[../../../specs/001-acceso-usuarias-internas/checklists/requirements]]"
  - "[[../../evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0]]"
  - "[[../../evidence/fase-i/2026-07-25-confirmacion-spec-001]]"
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[../../decisions/ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[../../traceability/MATRIZ-TRAZABILIDAD]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - sprint/s1
  - modulo/acceso
---

# Preparación de SPEC-001 — Acceso de usuarias internas

## Objetivo

Crear el primer borrador formal de la funcionalidad `RF-ACC-001` y los requisitos no
funcionales aplicables, según la opción A aprobada en ACT-REQ-001.

## Resultado de la sesión

- Se creó
  [[../../../specs/001-acceso-usuarias-internas/spec|SPEC-001 — Acceso de usuarias internas]]
  inicialmente como `draft` y, tras resolver Q1–Q3, pasó a `proposed`.
- Se registró el directorio activo en `.specify/feature.json`.
- Se creó el
  [[../../../specs/001-acceso-usuarias-internas/checklists/requirements|checklist de calidad]]
  requerido por el flujo de especificación.
- Se delimitó el alcance a inicio y cierre de sesión, protección de vistas privadas, cambio
  de contraseña, primera cuenta y dashboard básico de bienvenida.
- Permanecen fuera `RF-ACC-002`, `RF-ACC-003`, `RF-ACC-004`, recuperación externa de
  contraseña, operaciones de negocio y contenido público final.
- La rama predeterminada del repositorio remoto se corrigió de
  `docs/fase-1-requisitos` a `main`.
- Se propuso desarrollar Django directamente en la raíz `F:\Tesis\App Tesis`, con
  `manage.py`, `config/` y `apps/`, conservando `docs/`, `specs/` y los agentes como áreas
  separadas del mismo repositorio.
- El tesista confirmó integralmente SPEC-001 y aceptó la estructura el 2026-07-25.
- La confirmación se registró en
  [[../../evidence/fase-i/2026-07-25-confirmacion-spec-001|EVID-SPEC-001]], sin reescribir el
  acta anterior.
- La estructura aceptada se formalizó como
  [[../../decisions/ADR-0003-estructura-raiz-aplicacion-django|ADR-0003]].

## Aclaraciones resueltas

1. Q1=A: cambio obligatorio de la credencial temporal antes de usar el dashboard.
2. Q2=A: cierre de sesión después de 30 minutos sin actividad.
3. Q3=A: entrega presencial a una representante designada por la Directiva.

## Estado de calidad

La segunda validación cumple las 16 comprobaciones. No quedan marcadores de aclaración y
SPEC-001 está `confirmed`. La planificación está autorizada; la implementación todavía no.

## Próxima puerta

Ejecutar `speckit-plan`, revisar el resultado y solicitar aprobación antes de generar tareas.
Después corresponden `speckit-tasks` y `speckit-analyze`. Solo entonces puede evaluarse el
inicio de la implementación.

## Secuencia posterior a la confirmación

1. **Planificar** con `speckit-plan`: producir `plan.md`, `research.md`, `data-model.md`,
   contrato HTTP de recorridos, `quickstart.md` y estrategia de pruebas.
2. **Revisar y aprobar el plan**: comprobar constitución, ADR-0003, límites de `accounts`,
   PostgreSQL, sesiones, seguridad, UX móvil y primera cuenta.
3. **Generar tareas** con `speckit-tasks`: dividir la porción vertical por archivos,
   dependencias y pruebas, con un solo escritor por tarea.
4. **Analizar coherencia** con `speckit-analyze`: resolver contradicciones entre spec, plan y
   tareas antes del código.
5. **Autorizar implementación**: el tesista confirma la primera porción y el alcance Git.
6. **Crear la base mínima**: únicamente `config/`, `apps/accounts/`, usuario personalizado,
   acceso, cambio obligatorio, dashboard y pruebas; no crear apps futuras vacías.
7. **Verificar y revisar**: comprobaciones Django, migraciones, pruebas positivas y negativas,
   PostgreSQL, seguridad, 360 px, teclado, foco y zoom.
8. **Registrar evidencia e integrar**: actualizar matriz, evidencia y documentación; revisar
   el diff y solicitar autorización antes de commit, push o merge cuando corresponda.

El plan deberá decidir explícitamente el gestor de dependencias y el archivo de bloqueo. No
se asume `uv` solo porque apareció de forma ilustrativa en la propuesta de estructura.

## Control de Git

- Rama local de trabajo: `codex/001-acceso-usuarias-internas`.
- No se realizó commit, push ni merge durante la preparación de este borrador.
- Se preservaron los cambios locales previos en `.obsidian/graph.json`, `README.md` y el
  ajuste de formato de ACT-REQ-001.
