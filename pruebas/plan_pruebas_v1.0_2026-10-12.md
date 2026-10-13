---
titulo: Plan de pruebas y evaluación
version: "1.0"
fecha: 2026-10-12
autor: Tesista
estado: plan-vigente-sin-resultados
fuentes: CAT-REQ-001-v1.1; constitucion-0.2.0; pila-producto-v1.2
publicacion: pendiente-de-confirmacion
---

# Plan de pruebas y evaluación

Este documento define **qué se comprobará** cuando exista la aplicación.
Al 12 de octubre de 2026 no hay una aplicación Django funcional ni resultados
de pruebas del producto; ninguna fila afirma que se haya aprobado un ensayo.

| Área | Prueba prevista | Evidencia que se guardará |
|---|---|---|
| Acceso | Entrar con cuenta válida; rechazar cuenta sin permiso; comprobar cargo y encargo. | Caso, resultado esperado, resultado obtenido y captura o registro. |
| Actividades | Crear, asignar, consultar y corregir una actividad autorizada. | Datos de prueba y trazabilidad de cambios. |
| Asistencia | Registrar entrada y salida; detectar duplicado e inconsistencia; revisar corrección. | Horas, actor, motivo y decisión; no automatizar multa mientras P-03 siga abierta. |
| Producción e inventario | Seguir materia prima, secado, lote y movimientos hasta la existencia. | Conciliación con unidades, origen y responsable. |
| Ventas y cuentas | Registrar venta, devolución, gasto y pago parcial; distinguir deudas. | Cálculos reproducibles y saldos antes/después. |
| Reportes | Comparar PDF y pantalla con registros de origen y filtros. | Totales, periodo, unidades y permiso aplicado. |
| Sin conexión | Guardar operación habilitada, recuperar red, reintentar y resolver rechazo. | Estados local/remoto, ausencia de duplicados y aislamiento de cuentas. |
| Uso y accesibilidad | Recorrido en móvil, teclado, zoom, contraste, errores y comprensión con usuarias. | Fecha, participantes anonimizados, observación y mejora. |

## Criterio de cierre

Cada historia implementada enlazará requisito, criterio de aceptación, prueba,
resultado y corrección si corresponde. Un recorrido se declara completo solo
después de comprobar su funcionamiento y permisos; una maqueta no basta.
La adecuación funcional se evaluará conforme al plan académico basado en
ISO/IEC 25010:2023, sin afirmar certificación ni resultados anticipados.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.0 | 2026-10-12 | Se establece el plan de comprobación por módulo y la evidencia de cierre. | Plan; resultados pendientes |
