---
title: Índice de funcionalidades activas
type: feature-context-index
status: active
updated: 2026-10-27
---

# Índice de funcionalidades activas

## SPEC-001 — Acceso de usuarias internas

| Campo | Valor |
|---|---|
| Estado | `confirmed` |
| Plan | `approved` |
| Tareas | `planned` |
| Fase actual | Implementación; `SB-S2-02` activo en la app independiente |
| Alcance inmediato | Completar y verificar `HU-ACC-001`, incluidos mensajes claros, seguridad de sesión y bloqueo tras intentos fallidos |
| Fuente principal | [`spec.md`](../../specs/001-acceso-usuarias-internas/spec.md) |
| Plan | [`plan.md`](../../specs/001-acceso-usuarias-internas/plan.md) |
| Tareas | [`tasks.md`](../../specs/001-acceso-usuarias-internas/tasks.md) |

### Recuperación por tipo de tarea

- Arquitectura: abrir únicamente las secciones de arquitectura y datos relevantes de
  `spec.md`, `plan.md`, `data-model.md` y ADRs relacionados.
- Planificación: abrir requisitos, alcance, dependencias y criterios de `spec.md` y `plan.md`.
- Implementación: abrir `tasks.md`, la tarea asignada y los archivos relacionados; no abrir
  artefactos de fases futuras.
- Frontend: abrir `docs/ui/SISTEMA-DISENO.md`, la tarea asignada y `design/` relevante.
- Revisión: abrir diff, criterios y pruebas de la tarea; añadir contratos solo si están afectados.

### Artefactos bajo demanda

| Artefacto | Cuándo abrirlo |
|---|---|
| `research.md` | Solo si se revisa una decisión de investigación. |
| `data-model.md` | Solo si se revisa modelo, migración o integridad de datos. |
| `contracts/http.md` | Solo si se revisan rutas, formularios o contratos HTTP. |
| `quickstart.md` | Solo para reproducir el entorno o sus verificaciones. |
| `checklists/requirements.md` | Solo al revisar completitud de requisitos. |

Las decisiones de diseño que requieren validación humana siguen pendientes para los
comportamientos afectados. Pueden desarrollarse porciones independientes respaldadas
por `RF-ACC-001` y el sprint de ejecución registrado; la falta de un documento adicional no veta un
commit intermedio. `HU-ACC-001` no se declara terminada mientras falten sus verificaciones.

**Estado de la app — 2026-10-23:** `App-zhudaleli` existe en la raíz Git independiente
`app/`. Su commit inicial es `903f1f9a55777992468ad88575d1f58463318516`, publicado en
`feature/RF-ACC-001-base-proyecto`; todavía no hay PR ni tag. El checkpoint
[[../bitacora/checkpoints/2026-10-21-app-commit-903f1f9-post-commit|post_commit]] conserva
el alcance y las verificaciones reales. La frase de
[[../architecture/ARQUITECTURA-OBJETIVO|ARQUITECTURA-OBJETIVO]] que dice que aún no existe
código Django describe el contexto de su actualización del 2026-10-08; no debe usarse como
estado actual del repositorio.

Compatibilidad arquitectónica 2026-10-08: ADR-0006 adoptó la raíz, ORM, modelos/migraciones
nativos y capas proporcionales; la constitución vigente 2.0.0 conserva esa arquitectura. ADR-0007
regula solo el cierre administrativo de los periodos. ADR-0008 separa código y proceso.
El plan de SPEC-001 conserva su estructura sin servicios, `core`, API o apps vacías.
Las decisiones concretas que el plan remite a validación humana siguen pendientes
antes de implementar esos comportamientos; cerrar un sprint no marca la spec o
sus tareas como completadas.

## Cambios de producto posteriores a la línea base

El [[../requirements/CAT-REQ-001|catálogo v1.2 aprobado por el tesista]] contiene 67
requisitos confirmados y 2 propuestos, e incorpora las capacidades obligatorias offline
con sus criterios. No amplía SPEC-001 con datos de negocio ni cuentas offline; el
contenido privado continúa excluido de cachés compartidas. Las specs de
asistencia/pesajes/sincronización siguen pendientes.
La [[../evidence/casos-de-uso/2026-09-28-coherencia-integral|auditoría integral]] documenta la
compatibilidad y las correcciones de dependencias de tasks.md, sin marcar tareas terminadas.

## Panel administrativo — candidato de integración

**Estado funcional: `proposed`; estructura y permisos previstos para S2 por decisión
del tesista del 2026-10-27.** El tesista precisó después que la Superadministradora
podrá hacer todas las acciones ordinarias de cada módulo y editar desde su panel
registros, valores de campos existentes y opciones configurables publicadas por esos
módulos, sin asignación individual de módulo. Esta decisión sustituye la restricción
anterior de autoridad transversal, pero no declara implementadas las funciones de
S3–S5 ni aprueba `RF-ACC-005` completo. La capacidad puede apoyarse en `RF-ACC-002`
(cuentas/membresías) y `RF-ACC-003` (perfiles, cargos, encargos y permisos), pero no amplía
`SB-S2-02`. `HU-ACC-002` y `HU-ACC-003` sí existen en la pila v1.7 y las fichas v2.5; sus
prioridades y fechas detalladas siguen propuestas, y la revisión académica sigue pendiente. Su presencia
no resuelve P-01 ni autoriza implementar operaciones administrativas. Primero se debe definir
la matriz por operación y recurso, mantener cada configuración de negocio bajo su módulo dueño
y resolver los comportamientos de acceso que requieran cambio de requisitos. `PRO-SEC-001`
sigue en revisión y no sustituye los criterios vigentes de SPEC-001. No se autoriza aquí
recuperación de cuenta ni edición de configuración técnica o secretos. El alcance operativo
actual y las fechas candidatas están en
[[../sprints/PLAN-HASTA-2026-12-23|la hoja de ruta viva]].
