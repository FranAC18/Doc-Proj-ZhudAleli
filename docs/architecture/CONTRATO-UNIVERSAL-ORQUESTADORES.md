---
title: Contrato universal de orquestadores y continuidad
type: architecture
status: proposed
date: 2026-08-24
related:
  - "[[../decisions/ADR-0002-arnes-portable-de-ia]]"
  - "[[../decisions/ADR-0004-capa-abstraccion-modelos-ia]]"
  - "[[../../agents/tesis/roles/README]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
---

# Contrato universal de orquestadores y continuidad

## Propósito

Permitir que Codex, Antigravity, OpenCode y OpenChamber trabajen sobre el mismo proyecto sin
perder contexto, duplicar reglas ni escribir simultáneamente sobre el mismo worktree.
Obsidian no es una copia del proyecto: la raíz de Git es también el vault y contiene la
memoria persistente que cualquier host puede leer.

## Separación de responsabilidades

| Capa | Responsabilidad | Fuente versionada |
|---|---|---|
| Proyecto | misión, fuentes de verdad, puertas, seguridad y Git | `AGENTS.md`, `.specify/memory/constitution.md` |
| Contexto | dominio, conocimiento y política documental | `agents/tesis/` |
| Funcionalidad | requisito aprobado, diseño, tareas y pruebas | `specs/<id-funcionalidad>/` |
| Memoria | sesiones, handoffs, checkpoints y evidencia | `docs/bitacora/`, `docs/evidence/` |
| Roles | responsabilidades y límites comunes | `agents/tesis/roles/` |
| Adaptador de host | formato específico de cada herramienta | `.codex/`, `.opencode/`, `.agents/rules/` |
| Modelo/proveedor | capacidad, cuota y autenticación | host elegido o laboratorio Python |

Las preferencias por rol están en `tools/agent-routes.toml` y se explican en
`docs/architecture/RUTAS-MODELOS-IA.md`. La ruta es una política de selección, no una
credencial ni un mecanismo de failover invisible.

Un modelo no es un orquestador. Un orquestador no es una fuente de verdad. La conversación
privada de un proveedor nunca sustituye un handoff versionado.

## Hosts soportados

| Host | Función | Adaptación actual | Escritura recomendada |
|---|---|---|---|
| Codex | coordinación, arquitectura, revisión, documenter y git-manager | `.codex/agents/` | según rol y permisos del host |
| OpenCode | ejecución de agentes y herramientas | `.opencode/agents/`, `AGENTS.md`, `.agents/skills/` | una tarea asignada por worktree |
| OpenChamber | interfaz visual que ejecuta OpenCode | usa la configuración de OpenCode | igual que OpenCode |
| Antigravity | carril Gemini y análisis/documentación | `.agents/rules/`, `.agents/skills/`, `AGENTS.md` | solo una fase asignada |

Las adaptaciones deben apuntar a `agents/tesis/roles/` y no redefinir sus límites. Los agentes
de Codex no se consideran automáticamente disponibles en OpenCode o Antigravity.

## Contrato de inicio

Cada host debe, antes de actuar:

1. resolver la raíz buscando `AGENTS.md` y `.specify/memory/constitution.md` hacia arriba;
2. confirmar que la raíz coincide con el vault;
3. leer el contrato común, constitución, contexto, políticas y dashboard;
4. leer `docs/bitacora/ESTADO-ACTIVO.md` y el último handoff relacionado;
5. leer `spec.md`, `plan.md` y `tasks.md` de la funcionalidad activa;
6. ejecutar `git status --short --branch`;
7. declarar hechos verificados, propuestas, bloqueos y próximo paso.

Si no puede resolver la raíz o falta una fuente obligatoria, no escribe.

## Contrato de escritor único

Un worktree puede tener un solo escritor activo. Se permite que varias herramientas estén
abiertas, pero solo una puede modificar el worktree actual. Para trabajo paralelo se usan
branches/worktrees diferentes y cada resultado vuelve al coordinador mediante un handoff.

Los documentos aprobados, dashboard, sprint, matriz, specs confirmadas y ADR aceptados no se
modifican automáticamente por un cambio de proveedor.

## Ciclo universal de una tarea

```text
planned
  ↓
in-progress (implementer en un worktree)
  ↓ pruebas y revisión
partially-complete / blocked / completed
  ↓
documenter: pre_commit con commit: pending
  ↓ autorización humana
git-manager: commit exacto
  ↓ hash real
documenter: post_commit
  ↓
cierre humano y actualización de trazabilidad
```

El estado se persiste en `docs/bitacora/checkpoints/` usando
`docs/templates/PLANTILLA-HANDOFF-UNIVERSAL.md`. Un handoff debe permitir que otra herramienta
continúe sin acceder al historial privado de la conversación.

## Cambio por cuota o proveedor

El cambio de proveedor ocurre a nivel de tarea, no de conversación:

1. detener el host que alcanzó el límite;
2. conservar los archivos modificados y ejecutar las verificaciones posibles;
3. registrar un handoff con `status: partially-complete` y `commit: pending`;
4. cerrar el host anterior;
5. abrir el siguiente host en el mismo worktree, o transferir el commit/worktree si se trabaja
   en paralelo;
6. leer el handoff y confirmar `git status` antes de escribir;
7. continuar solo con los `allowed_paths` originales.

No existe un fallback automático confiable entre la sesión gratuita de Codex, la cuota de
Google AI Pro y OpenCode Go porque son superficies de autenticación y estado diferentes. La
continuidad universal sí es automática a nivel documental: el siguiente host lee el mismo
estado versionado.

## Rutas de modelos

La identidad de un modelo debe registrarse separando:

```text
host: OpenChamber
orquestador: OpenCode
proveedor: opencode-go
modelo: <modelo de OpenCode Go>
```

o:

```text
host: Antigravity
orquestador: Antigravity
proveedor: Google AI Pro
modelo: gemini-3.1-pro
```

No se debe tratar un identificador de OpenCode Go como si fuera un modelo directo de OpenAI,
ni un identificador de Antigravity como si comprobara acceso a la API de Google.

## Criterio de terminado del contrato

El contrato se considera implementado cuando:

- los tres hosts leen la fuente común y skills compartidas;
- cada rol tiene contrato canónico y adaptador;
- un handoff puede ser leído por otro host sin contexto privado;
- la raíz se valida antes de escribir;
- el escritor único y las rutas permitidas están explícitos;
- el documenter y git-manager conservan las puertas de commit;
- una prueba o validador detecta adaptadores faltantes;
- el flujo está enlazado desde el dashboard y es visible en Obsidian.

Este documento permanece `proposed` hasta que el tesista revise el flujo en una sesión real
con los tres hosts.
