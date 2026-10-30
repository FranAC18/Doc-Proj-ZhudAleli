---
title: Índice operativo de contexto
type: context-index
status: active
updated: 2026-10-27
source_of_truth: "AGENTS.md"
---

# Índice operativo de contexto

Este índice define la recuperación mínima para una tarea. No es una copia de las fuentes.
Si un documento no aparece aquí o en el índice de la funcionalidad activa, no se carga por
defecto.

## Siempre

| Fuente | Uso |
|---|---|
| `AGENTS.md` | Reglas no negociables, gobierno y límites de escritura. |
| `docs/bitacora/ESTADO-ACTIVO.md` | Rama, `HEAD`, tarea, rutas y próximo paso. |
| `tools/agent-routes.toml` | Clasificación, perfil de modelo y nivel de revisión. |

## Según la tarea

| Tipo | Leer primero | Agente recomendado |
|---|---|---|
| `architecture` | Constitución, arquitectura/ADR relevantes, feature index | `architect` |
| `planning` | Requisitos, constitución, arquitectura, feature index | `architect` |
| `implementation` | Requisito y sprint vigentes; tarea y spec si existen; código y pruebas relevantes | `implementer` |
| `frontend` | `docs/ui/REGLAS-DISENO-INTERFACES.md` (obligatorio), sistema de diseño, componentes y assets relevantes | `frontend` |
| `debugging` | Síntoma, archivos afectados, pruebas y contratos relacionados | `implementer` |
| `research` | Solo las fuentes necesarias para responder | `researcher` |
| `review` | Diff, archivos modificados, pruebas, contratos y reglas | `reviewer` |
| `documentation` | Fuente concreta, plantilla y ruta autorizada | `documenter` |

## Funcionalidad activa

La planificación operativa hasta el 2026-12-23 se mantiene en
[`PLAN-HASTA-2026-12-23.md`](../sprints/PLAN-HASTA-2026-12-23.md). Sus fechas y alcances
propuestos se distinguen de decisiones del tesista y de resultados verificados. Para una
tarea concreta se abre solo el bloque del sprint o módulo afectado.
La edición académica `plan_sprints_v1.6` refleja la reordenación operativa S2–S5 y el
alcance transversal de Superadministración decidido el 2026-10-27. Las ediciones
académicas `requisitos_generales_v2.1`, `historias_usuario_v2.6` y
`pila_producto_v1.8` conservan la línea base y señalan `RF-ACC-005` y cinco HU como
propuestos; están preparadas localmente para revisión. `sprint_backlog_v1.4` conserva
el corte anterior S1–S6: sus tareas no se mueven automáticamente y se actualizarán
solo al seleccionar compromisos concretos. Para desarrollo se consulta la hoja de ruta viva.

Para arquitectura, la guía canónica vigente es
[`ARQUITECTURA-OBJETIVO.md`](../architecture/ARQUITECTURA-OBJETIVO.md), vinculada a
[`ADR-0006`](../decisions/ADR-0006-monolito-modular-y-entrega-incremental.md), aceptado bajo
la constitución 0.2.0. La constitución vigente es 2.0.0; el cierre administrativo de sprints se
rige por [`ADR-0007`](../decisions/ADR-0007-autoridad-del-tesista-para-cierre-de-sprints.md)
y la separación de repositorios por
[`ADR-0008`](../decisions/ADR-0008-separacion-repositorios-y-flujo-git.md).
ADR-0008 sustituye solo la ubicación en un único repositorio y la puerta documental
previa de ADR-0003; conserva la estructura interna Django del monolito.
Las propuestas previas se recuperan como antecedentes, no como reglas alternativas vigentes.

Leer [`feature-index.md`](feature-index.md) antes de abrir cualquier artefacto de una spec.
No leer automáticamente `research.md`, `data-model.md`, `contracts/` o `quickstart.md`:
se abren únicamente si la tarea los necesita.

## Ampliación vigente de acceso — 2026-10-28

Para acceso multicanal consultar SPEC-003 en el feature index: plan de correo, passkeys y WhatsApp aceptado por el tesista; código pendiente. El catálogo vigente es CAT-REQ-001 v1.3 (71 confirmados, 3 propuestos). Las ediciones académicas de consulta son requisitos v2.2, HU v2.7, HT v1.8, pila v1.9 y backlog v1.5, preparadas localmente. Los cortes y estados históricos descritos arriba se conservan; no sustituyen este incremento. Cada cambio relevante debe sincronizar los cinco destinos documentales y el gestor local según AGENTS.md.

## Fuentes de verdad

Para interfaces, [REGLAS-DISENO-INTERFACES.md](../ui/REGLAS-DISENO-INTERFACES.md)
concreta ocho reglas obligatorias solicitadas por el tesista el 2026-10-28. La dirección
visual conserva su estado provisional. Las ediciones de consulta con esta precisión son
diseño v1.1, requisitos v2.3, HU v2.8, HT v1.9, pila v2.0 y backlog v1.6; conservan
los requisitos, conteos y avances de las ediciones anteriores. Revisión académica pendiente.

1. Requisitos validados y evidencia de campo.
2. Especificaciones y ADR aprobados.
3. Código, migraciones y pruebas.
4. Documentación oficial vigente.
5. Propuestas e historial.
6. Conversación y memoria como contexto auxiliar.

## Edición documental para el docente

`documentacion/README.md` indexa las ediciones finales revisadas y versionadas en el
repositorio general, destinadas también al repositorio documental. Sus fuentes de
trabajo siguen en `docs/` y `specs/`; `analisis/` y
`_archivo/` son internos. Antes de sincronizar, revisar el estado y la versión de
cada documento, el control de cambios y la lista exacta de archivos. El `commit`
y la publicación externa tienen autorizaciones humanas separadas.

## Código de producto

La app se desarrolla en la raíz Git independiente `App-zhudaleli`. Para trabajo de
código se leen aquí el RF y sprint vigentes y, si existen, las secciones pertinentes
de spec/plan/tareas. La ausencia de documentos de proceso en la app no bloquea
commits. Antes de cada push se sigue
[`REPOSITORIOS-Y-PRE-PUSH.md`](../git/REPOSITORIOS-Y-PRE-PUSH.md).

## Referencia, no contexto normal

- `README.md`, `ONBOARDING-IA.md` y las notas de `docs/01-agentes/` y `docs/02-skills/`.
- Auditorías fechadas, propuestas superseded y checkpoints completados.
- `.obsidian/workspace*.json`, gráficos y configuración visual de Obsidian.
- `tools/agent-lab/`, que es un laboratorio separado y no la memoria de Codex/OpenCode.

## Reglas de lectura

- Seguir enlaces solo hasta cubrir el criterio de la tarea.
- Preferir secciones relevantes y no documentos completos cuando el artefacto lo permita.
- Si dos fuentes difieren, detener la decisión y reportar la discrepancia según la jerarquía.
- Antes de escribir, comprobar `allowed_paths`, `forbidden_paths`, rama y `HEAD`.
