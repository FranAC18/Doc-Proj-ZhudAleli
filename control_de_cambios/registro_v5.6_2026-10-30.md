---
titulo: Adenda de decisiones del diseño de base de datos
version: "5.6"
fecha: 2026-10-30
autor: Codex, por instrucción del tesista
estado: preparado-para-revision-academica
publicacion: pendiente
base: registro_v5.5_2026-10-30.md
phase: pre_commit
commit: pending
---

# Adenda de decisiones del diseño de base de datos

Se registra una adenda a la edición lógica v1.0 a partir de las respuestas directas del tesista del 30/10/2026. El material actualiza el diseño propuesto y no representa aprobación organizacional, revisión académica, publicación ni implementación física.

| Documento | Cambio | Fuente y límite |
|---|---|---|
| [Adenda de diseño v1.1](../arquitectura/adenda_diseno_base_datos_v1.1_2026-10-30.md) | Define separación de venta individual y feria, devolución, rendición de valor base, distribución de stock compartido, autonomía de Superadministración sin venta personal, registro resumido de feria, stock offline individual y confidencialidad futura de recetas. | Respuestas directas del tesista del 30/10/2026. Requisitos fuente y SPEC-002 conservan estado previo hasta reconciliación documental; pendientes listados en la adenda. |
| [Índice documental](../README.md) | Versión 5.6 con acceso y precedencia de la adenda v1.1 sobre v1.0 en los temas tratados. | Conserva v1.0 y cortes anteriores. No publica ni reemplaza archivos aprobados. |

Se mantienen sin efecto automático: el excedente manual no asignado, el alcance de la opción de devoluciones, el periodo periódico fuera de feria, la gestión de pagos de comisiones y la visibilidad de las recetas confidenciales. Se marcan como pendientes en la adenda, sin inventar una regla. La edición de requisitos aprobados no se altera por esta incorporación.

## Verificación editorial

Se revisan metadatos, estructura, destinos de enlaces internos y consistencia de los estados editoriales. No se ejecutan pruebas de Django, migraciones, concurrencia ni pruebas de producto. No se sincroniza el gestor local ni se alteran estados, fechas o estimaciones del sprint mientras la enmienda siga pendiente de reconciliación.

Conserva el [control anterior v5.5](registro_v5.5_2026-10-30.md) y el [diseño base de datos v1.0](../arquitectura/diseno_base_datos_v1.0_2026-10-30.md).

## Historial

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 5.6 | 2026-10-30 | Codex | Se incorpora adenda v1.1 con respuestas de negocio del tesista y pendientes acotados; revisión y publicación pendientes. | Preparado localmente. |
