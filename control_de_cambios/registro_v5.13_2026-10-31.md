---
version: "5.13"
fecha: 2026-10-31
autor: Codex por instrucción expresa del tesista
estado: preparado-para-revision
publicacion: pendiente
---

# Control de cambios 5.13

## Solicitud y alcance

Completar pendientes inmediatos de membresías y planificación, registrar el estado real de las tablas PostgreSQL y sincronizar los documentos de requisitos, historias, pila y sprint backlog. El código corresponde a una porción de `SB-S2-03` y `SB-S3-01`; ambas tareas permanecen parciales. El inicio anticipado de planificación durante S2 conserva la asignación y fechas de S3.

La autorización del tesista cubre a Presidenta, Tesorera y Secretaria para administrar periodos de membresía y crear/editar actividades. El backend exige designación vigente. Esta autorización concreta el trabajo de implementación y no se presenta como validación organizacional directa, aprobación de requisito nuevo o cambio de la línea base.

## Ediciones sincronizadas

- [Requisitos v2.8](../requisitos/requisitos_generales_v2.8_2026-10-31.md)
- [Historias de usuaria v3.3](../historias/usuario/historias_usuario_v3.3_2026-10-31.md)
- [Historias técnicas v2.4](../historias/tecnicas/historias_tecnicas_v2.4_2026-10-31.md)
- [Pila de producto v2.5](../pila_producto/pila_producto_v2.5_2026-10-31.md)
- [Sprint backlog v2.1](../sprints/sprint_backlog_v2.1_2026-10-31.md)

Se conservan criterios, prioridades, estimaciones y aprobaciones. `SB-S2-03` refleja las operaciones de membresía para cuentas ya existentes. `SB-S3-01` refleja actividades básicas con responsables y participantes; instancia/recurrencia y cancelación siguen pendientes. No se cierra historia, tarea ni sprint.

## Evidencia técnica

La app publicó el commit [`c9f2d6a3e0f0fa474485546075eda55e8d729592`](https://github.com/FranAC18/App-zhudaleli/commit/c9f2d6a3e0f0fa474485546075eda55e8d729592) en `feature/RF-PLA-001-actividades`. En `zhud_aleli_dev` se verificaron 19 tablas base y 22 migraciones aplicadas, tres cargos de catálogo y cero designaciones activas. Pasaron 68 pruebas PostgreSQL, Ruff, controles de Django y comprobación de migraciones. [Evidencia de implementación](../../docs/evidence/architecture/2026-10-30-planificacion-backend/implementacion.md), [revisión UI](../../docs/evidence/frontend/2026-10-31-planificacion-ui/revision.md) y [checkpoint](../../docs/bitacora/checkpoints/2026-10-31-planificacion-y-membresias.md).

Las 19 tablas describen la porción física de acceso, identidad, membresías y planificación que existe hoy. Asistencia, producción, inventario, ventas, rendiciones y reportes del ER integral continúan sin tablas físicas. No se insertaron personas reales ni titulares de cargos.

## Estado editorial y publicación

El índice académico se actualiza a v5.13 y queda preparado para revisión. No se sincronizó con el repositorio documental del docente ni se publicó. No se hizo Git del vault. La app no tiene PR, merge, tag ni despliegue asociados a este corte.
