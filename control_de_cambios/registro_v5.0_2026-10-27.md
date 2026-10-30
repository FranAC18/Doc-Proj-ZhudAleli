---
titulo: Registro de cambios documentales
version: "5.0"
fecha: 2026-10-27
autor: Franklin Acero
estado: preparado-para-revision
publicacion: pendiente-de-transferencia
---

# Registro de cambios documentales v5.0

## Sincronización de requisitos, historias y pila

| Documento | Versión | Cambio | Estado |
|---|---:|---|---|
| [Requisitos generales](../requisitos/requisitos_generales_v2.1_2026-10-27.md) | 2.1 | Conserva íntegra la v2.0 aprobada y añade `RF-ACC-005` propuesto. Explicita autoridad transversal de la Superadministradora, acciones ordinarias, accesos, registros, asistencia, valores y opciones del panel, con reglas e historia por módulo. | Preparado para revisión; no aprobado ni publicado. |
| [Historias de usuario](../historias/usuario/historias_usuario_v2.6_2026-10-27.md) | 2.6 | Conserva las 51 historias de base, refina HU-ACC-002/003 y añade HU-ACC-005–009 como candidatas con criterios de acceso, configuración y operación por módulo. | Preparado para revisión; cinco historias adicionales propuestas. |
| [Pila de producto](../pila_producto/pila_producto_v1.8_2026-10-27.md) | 1.8 | Conserva 65 registros principales del corte anterior, agrega cinco historias candidatas fuera de la base y presenta el orden de ejecución propuesto S2–S5. | Preparado para revisión; no convierte filas en compromisos del sprint. |
| [Índice documental](../README.md) | 5.0 | Señala por separado la línea base aprobada y las tres ediciones candidatas; conserva versiones anteriores. | Actualizado localmente; transferencia pendiente. |

La decisión del tesista del 2026-10-27 define que una Superadministradora activa puede
realizar las acciones ordinarias de todos los módulos sin asignación individual y,
desde el panel, editar registros, valores de campos existentes y opciones publicadas.
Los módulos conservan validaciones, aprobaciones aplicables y trazabilidad. El panel
no crea campos físicos ni altera directamente el esquema de la base de datos.

El rol fue reportado por el tesista como validado por la presidenta; falta adjuntar
la evidencia directa. `RF-ACC-005` y las historias nuevas permanecen propuestos.
La edición académica aprobada y publicada de requisitos v2.0 no se reescribe ni se
presenta como si incluyera esta ampliación. Las tareas y pruebas no se marcan
completas por la edición documental.

No se realizó commit, transferencia ni publicación al repositorio del docente.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| [4.9](registro_v4.9_2026-10-27.md) | 2026-10-27 | Se registraron el plan y los criterios de Superadministración. |
| 5.0 | 2026-10-27 | Se sincronizan ediciones completas de requisitos, historias y pila, preservando la línea base aprobada. |
