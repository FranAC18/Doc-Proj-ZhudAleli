---
title: Índice operativo de contexto
type: context-index
status: active
updated: 2026-10-29
source_of_truth: AGENTS.md
---

# Índice operativo de contexto

## Entrada mínima

1. `AGENTS.md`: contrato común; reutilizar si ya está disponible y vigente en el chat.
2. [Estado activo](../bitacora/ESTADO-ACTIVO.md): resultado actual, pendientes y siguiente
   acción. Antes de escribir, consultar las rutas del archivo indicado por `scope_file`
   y comprobar raíz, rama, HEAD y cambios locales en cada repositorio afectado.
3. Clasificar con el bloque `task_types.<tipo>` de `tools/agent-routes.toml`.
   Los perfiles describen capacidades; no seleccionan automáticamente modelo o razonamiento.

Leer solo lo necesario para resolver la tarea. Buscar con `rg -n` y extraer secciones;
si se trunca la salida, acotar la lectura. No recorrer todos los enlaces de un índice.
Reutilizar lecturas vigentes; al cambiar de tarea/host o tras compactación, revalidar
Git y recuperar lo faltante. El historial no es contexto inicial.
Para producto, buscar los IDs y abrir solo las secciones relacionadas. La
[guía de lectura](recorrido-tarea.md) se consulta si hay dudas; no exige fichas ni auditoría global.

## Según la tarea

| Tipo | Contexto adicional |
|---|---|
| `architecture` | Constitución; arquitectura y ADR relevantes; funcionalidad afectada. |
| `planning` | Requisito, sprint, constitución, arquitectura y funcionalidad pertinentes. |
| `implementation` | RF y sprint vigentes; tarea/spec si existen; código y pruebas afectados. |
| `frontend` | [Ocho reglas obligatorias](../ui/REGLAS-DISENO-INTERFACES.md); sistema de diseño, componentes y assets pertinentes. |
| `debugging` | Síntoma, archivos afectados, pruebas y contratos relacionados. |
| `research` | Pregunta y fuentes necesarias; para cuota/herramientas, no abrir specs de producto. |
| `review` | Diff, criterios, archivos modificados, pruebas y reglas aplicables. |
| `documentation` | Fuente concreta, plantilla y rutas del rol; [política del vault](../../agents/tesis/OBSIDIAN_POLICY.md) cuando se registre memoria. |

La constitución sigue siendo obligatoria para arquitectura, permisos, seguridad,
planificación y puertas de implementación. Código/plantillas/recursos de la app:
aplicar `zhud-aleli-codigo-legible`. La revisión independiente se reserva según riesgo
según AGENTS.md; clasificar una tarea no convoca agentes por sí solo.

## Fuentes bajo demanda

- Funcionalidad: [feature-index.md](feature-index.md); abrir solo el bloque de la spec
  afectada. SPEC-003 contiene el incremento multicanal; SPEC-001 conserva la base de
  acceso; SPEC-002/RF-ACC-005 siguen propuestos. Confirmar el estado en su fuente.
- Planificación: [hoja de ruta](../sprints/PLAN-HASTA-2026-12-23.md), bloque del sprint.
- Arquitectura: [guía canónica](../architecture/ARQUITECTURA-OBJETIVO.md), constitución
  2.0.0 y ADR pertinentes (0006 modularidad, 0007 sprints, 0008 repositorios).
- Edición académica: [índice documental](../../documentacion/README.md). Consultar ahí
  versiones y revisión; no repetir el catálogo en este índice. Publicación con
  autorización específica y vista previa; no sustituye RF, specs ni evidencia interna.
- Memoria: checkpoint enlazado para la tarea y su evidencia. `documentacion/`, MOCs,
  auditorías, propuestas antiguas, snapshots y `.obsidian/workspace*` no se cargan por defecto.
- `tools/agent-lab/` es un laboratorio separado; su memoria no demuestra una integración
  con este chat. Obsidian visualiza los Markdown; no constituye otra fuente de verdad.

Prevalece la jerarquía de AGENTS.md: RF validados/evidencia → specs/ADR aprobados →
código/pruebas → fuentes oficiales → propuestas/historial → conversación/memoria.
Las discrepancias se muestran; el ahorro no elimina contexto obligatorio ni evidencia.
El índice anterior íntegro se conserva como
[referencia histórica](../bitacora/checkpoints/2026-10-29-contexto-previo/context-index.md),
con enlaces relativos a su ubicación original; no usarlo como entrada vigente.
