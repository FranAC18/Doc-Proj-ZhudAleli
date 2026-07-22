---
title: Smoke test de Codex para el cierre de Sprint 0
type: evidence
status: completed
date: 2026-07-21
sprint: S0
module: transversal
engine: Codex
engine_version: codex-cli 0.145.0
model: GPT-5
tester: tesista y Codex
related:
  - "[[../../sprints/SPRINT-00-preparacion]]"
  - "../../../evals/providers/SMOKE-TEST.md"
tags:
  - proyecto/tesis
  - tipo/evidencia
  - sprint/s0
  - modulo/transversal
---

# Smoke test de Codex para el cierre de Sprint 0

## Alcance de esta etapa

Sprint 0 exige EVAL-01 y EVAL-02 porque la aplicación Django todavía no existe. EVAL-03,
EVAL-04 y EVAL-05 se conservan para la preparación de implementación, revisión y cierre de
funcionalidades. Kimi y GLM son comparaciones opcionales y no forman parte de esta puerta.

## EVAL-01 — Comprensión de contexto, solo lectura

El tesista ejecutó Codex CLI con la instrucción de leer únicamente `AGENTS.md`, la
Constitución, el dashboard, Sprint 0 y `PROJECT_CONTEXT.md`. El resultado:

- [x] respetó el modo de solo lectura y no modificó el repositorio;
- [x] identificó la misión y que la aplicación Django todavía no existe;
- [x] separó decisiones confirmadas, detalles técnicos pendientes y requisitos aún no
      validados con la organización;
- [x] detectó una discrepancia documental entre las decisiones y el contexto, corregida
      posteriormente en los documentos fuente.

## EVAL-02 — Especificación sin implementación

Se comprobó la plantilla activa mediante una propuesta controlada de registro de asistencia.
No se creó una funcionalidad activa ni código. El resultado mínimo producido fue:

```yaml
id: EVAL-ATT-001
title: Registro de asistencia
type: feature-spec
status: proposed
source:
  - "pendiente: entrevista u observación con la organización"
sprint: S3
module: asistencia
actors:
  - Socia operaria
  - Directiva
  - Encargada temporal
validated_by: []
```

- **Problema propuesto**: los registros actuales pueden contener omisiones; la evidencia de
  campo y el flujo exacto todavía deben validarse.
- **Permiso pendiente**: se debe confirmar quién registra inicialmente la asistencia. La
  corrección queda limitada a Directiva y Encargada según D-004.
- **Criterio positivo propuesto**: dado un perfil autorizado y una actividad vigente, cuando
  registra la asistencia válida, entonces el sistema conserva actividad, socia, fecha y
  responsable del registro.
- **Criterio negativo propuesto**: dado un perfil no autorizado, cuando intenta registrar o
  corregir asistencia, entonces la operación se rechaza sin alterar datos.
- **Dudas materiales**: reglas de entrada/salida, tratamiento de ausencias, duplicados y
  alcance temporal del permiso de la Encargada.

Resultado:

- [x] usa la estructura y controles de la plantilla activa;
- [x] incluye actor, fuente pendiente, permisos, criterios y preguntas materiales;
- [x] mantiene estado `proposed` y no aprueba requisitos;
- [x] no crea código Django ni realiza implementación.

## Resultado de la puerta

| Caso | Resultado | Cambios fuera de alcance | Evidencia |
|---|---|---|---|
| EVAL-01 | Aprobado | Ninguno | salida entregada por el tesista en la sesión de Sprint 0 |
| EVAL-02 | Aprobado | Ninguno | propuesta controlada incluida arriba |
| EVAL-03 | Diferido | N/A | antes de la primera tarea de implementación |
| EVAL-04 | Diferido | N/A | antes de aceptar una revisión funcional |
| EVAL-05 | Diferido | N/A | antes del primer cierre de funcionalidad |

Codex supera la puerta de lectura y especificación requerida para cerrar Sprint 0.
