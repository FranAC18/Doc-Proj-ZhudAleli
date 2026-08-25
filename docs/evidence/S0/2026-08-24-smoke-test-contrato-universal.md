---
title: Smoke test del contrato universal de orquestadores
type: evidence
status: completed
date: 2026-08-24
sprint: S0
module: transversal
task_id: HARNESS-UNIVERSAL-001
workflow: universal-contract-smoke
tester: tesista y reviewer (multi-host)
related:
  - "[[../../architecture/CONTRATO-UNIVERSAL-ORQUESTADORES]]"
  - "[[../../architecture/RUTAS-MODELOS-IA]]"
  - "[[../../bitacora/checkpoints/2026-08-24-contrato-universal-orquestadores]]"
  - "[[../fase-i/2026-08-24-aprobacion-plan-spec-001]]"
  - "[[../../../ONBOARDING-IA]]"
  - "[[../../../AGENTS]]"
tags:
  - proyecto/tesis
  - tipo/evidencia
  - sprint/s0
  - modulo/transversal
  - estado/completed
---

# Smoke test del contrato universal de orquestadores

## Objetivo

Verificar que Codex, Antigravity y OpenCode/OpenChamber resuelven la raíz, leen el contrato
universal y respetan el escritor único sobre el mismo worktree, de forma que un cambio de
herramienta conserve el estado versionado sin depender de memoria privada de conversación.

## Método

Cada host abrió una sesión real en `F:\Tesis\App Tesis` con la instrucción de humo de solo
lectura: resolver la raíz con `AGENTS.md` y `.specify/memory/constitution.md`, leer
`docs/bitacora/ESTADO-ACTIVO.md` y el checkpoint `2026-08-24-contrato-universal-orquestadores`,
ejecutar `git status --short --branch`, y declarar hechos verificados, lectura del contrato,
escritor único y próximo paso. Ningún host debía modificar archivos.

## Resultado por host

| Host | Raíz resuelta | Contrato leído | `validate-universal.py` | Escritor único | Resultado |
|------|---------------|----------------|-------------------------|----------------|-----------|
| Codex | `F:\Tesis\App Tesis` | Sí (AGENTS, constitución, contexto, dashboard, estado activo, checkpoint, roles, SPEC-001) | OK | Respetado (read-only) | Aprobado |
| Antigravity | `F:\Tesis\App Tesis` | Sí (AGENTS, constitución, ESTADO-ACTIVO, checkpoint) | OK | Respetado (read-only) | Aprobado |
| OpenCode / OpenChamber | `F:\Tesis\App Tesis` | Sí | OK | Respetado | Aprobado |

## Verificación local (host OpenCode / reviewer)

- `tools/validate-universal.py --json`: `ok: true`, raíz = vault = `F:\Tesis\App Tesis`,
  0 faltantes, `route_error: null`, hosts `codex`/`opencode`/`openchamber`/`antigravity` = `true`.
- `tools/agent-lab/tests/test_universal_contract.py`: **1 passed**.
- `opencode agent list`: detecta los roles universales `architect`, `documenter`,
  `git-manager`, `implementer`, `requirements`, `reviewer` y `ux`.
- `git status --short --branch`: `## main...origin/main` (árbol limpio).
- `git diff --check`: sin errores.
- OpenChamber reconoce el proyecto `App Tesis` en `F:\Tesis\App Tesis` (sesión `Smoke test
  contrato universal` despachada sobre OpenCode Go).

## Comportamiento de guardarraíl verificado

El primer intento de Codex se abrió por error desde `F:\Prácticas\Tarjetas digitales\scriptQr`
(proyecto ajeno), donde no existían `AGENTS.md` ni la constitución. En lugar de escribir, Codex
**reportó el bloqueo y no produjo artefactos**, cumpliendo el paso 1 del contrato de inicio
("si no puede resolver la raíz o falta una fuente obligatoria, no escribe"). La corrección fue
abrir Codex desde la raíz mediante el guardarraíl `scripts/agent.ps1 codex`.

## Discrepancia documental detectada

- El checkpoint registra `branch: codex/001-acceso-usuarias-internas` y `commit: 62dadf5`.
- El worktree actual está en `main` (`...origin/main`), commit `1210065`, árbol limpio.
- Aclaración: la rama `codex/001-acceso-usuarias-internas` ya se fusionó en `main`
  (`Merge ... codex/001-acceso-usuarias-internas`); `62dadf5` permanece en la historia. Los
  metadatos del checkpoint quedaron desactualizados, no incorrectos. Se registra aquí y se
  actualiza el checkout/puntero al estado real (`main`).

## Verificación de OpenAI/OpenChamber: pytest

`pytest` no está disponible dentro del entorno de Codex, por lo que no se ejecutó allí. La prueba
permanente del arnés se ejecutó desde el host OpenCode/reviewer (resultado: **1 passed**).

## Conclusión

El contrato universal es portable y legible en Codex, Antigravity y OpenCode/OpenChamber sobre
la misma raíz. Los tres hosts resolvieron la raíz como vault, leyeron el checkpoint y respetaron
el escritor único. La puerta de humo del contrato queda satisfecha con esta evidencia.

## Siguiente

- Confirmar con el tesista la selección concreta de modelos y cuotas por host
  (pendiente: `opencode:big-pickle` en uso vs `deepseek-v4` propuesto en `RUTAS-MODELOS-IA.md`;
  variantes Gemini locales de Antigravity no se versionan como IDs universales).
- Después, continuar con las tareas aprobadas de `SPEC-001` (Fase 1: diseño sin Django).
