---
title: Enmienda propuesta de ventas sin crédito y administración separada
type: requirement-proposal
status: proposed
date: 2026-10-29
version: 0.1
author: Codex
requested_by: Tesista
task_id: SB-S1-03
technical_story: HT-PRE-003
sprint_execution: S2
module: transversal
organization_validation: pending-direct-evidence
related:
  - "[[../CAT-REQ-001]]"
  - "[[../../architecture/proposals/2026-10-29-decisiones-pendientes-diseno-datos]]"
  - "[[../../architecture/proposals/2026-10-29-diseno-integral-base-datos]]"
  - "[[../../../specs/002-superadministracion/spec]]"
---

# Enmienda de los recorridos afectados por el diseño de datos

> Referencia de trabajo actual — 2026-10-30: [consolidación de datos v2.0](../../../documentacion/arquitectura/diseno_base_datos_v2.0_2026-10-30.md). Este archivo conserva el antecedente; las reglas incompatibles sobre Superadministración, devoluciones, reparto, rendición periódica, contingencia offline y kits están sustituidas. Las decisiones no modificadas conservan su evidencia.

## Fuente y alcance

El tesista pidió resolver los puntos de la revisión del diseño y respondió directamente en este chat el 29/10/2026:

- «No trabajamos con crédito, únicamente pago y después entrega, jamás crédito» (D-24).
- «El super admin no vende nada absolutamente nada, solo administra» (D-25).
- Cada secado corresponde a un solo acopio (D-26).
- La socia recibe en custodia y rinde después (D-27).
- Superadministradora administra cuentas/permisos/parámetros y corrige con auditoría; no ejecuta ni aprueba negocio (D-28).
- Devoluciones con reembolso y anulaciones después de cobrar no están definidas; dejarlas pendientes (D-29).
- Redondeo por línea al centavo con medio hacia arriba y desempate de reparto por ID de asignación menor aceptados expresamente (D-30).

Son instrucciones directas para corregir el diseño propuesto. No se atribuyen firmas ni validación directa a organización, Presidenta o asamblea. El CAT confirmado conserva la línea base y su evidencia; esta enmienda expone la discrepancia antes de implementar los comportamientos afectados. Las ediciones nuevas son adendas locales pendientes de revisión, sin publicación al docente, cambio de sprint, puntos ni estados de terminado.

## Requisitos afectados y criterio de sustitución

| ID existente | Regla anterior / discrepancia | Redacción candidata corregida | Criterio verificable |
|---|---|---|---|
| RF-VEN-001 | Venta por encargada; D-02 precisó venta desde custodia propia. | Socia activa vende stock propio en custodia; stock compartido requiere encargo. Toda entrega a comprador exige cobro completo previo. Superadministradora no vende. | Titularidad/encargo y saldo; cobro incompleto no entrega; venta repetida no duplica salida. |
| RF-VEN-002 | Permite modalidad crédito y exige identificar al comprador a crédito. | Todas las ventas son sin crédito. Venta ordinaria admite Público general; institucional conserva identificación mínima aprobada. Forma de pago no concede plazo. | No existe opción de crédito ni entrega con saldo de comprador; se minimizan datos personales. |
| RF-VEN-007 | Venta institucional por Tesorera; fuentes heredadas contemplan crédito. | Tesorera vende desde stock general a comprador institucional identificado, con cobro completo antes de entregar y sin excedente individual. | Misma barrera de pago que venta ordinaria; no generar cuenta por cobrar externa. |
| RF-CXC-001 | Incluye deuda externa y deuda por retiro individual impago. | Distinguir custodia y obligación interna por rendir. La custodia no causa deuda; vender desde custodia individual causa la base histórica por rendir según D-04/D-27. No hay crédito al comprador. | Transferir no cobra; vender causa una sola obligación; reparto compartido no duplica deuda individual. |
| RF-CXC-002 | Abonos sobre saldo elegido, incluida deuda externa. | Aplicaciones de rendición únicamente a obligaciones internas identificadas. Mantener abonos internos previstos sin confundirlos con crédito a clientes. | Importe aplicado <= pago y saldo; pago/rendición no cuenta como venta adicional. |
| RF-CXC-003 | Conciliación y efectos monetarios de ajustes. | Conciliar venta/cobro/rendición y conservar incidencias; efectos de reembolsos, pérdidas, anulaciones y sobrepagos quedan pendientes. | Ningún efecto monetario automático sin regla aprobada; incidente no desaparece. |
| RF-INV-003/004/005 | Entregas, conciliación y custodia. | Mantener custodia por lote, presentación, titular y feria; rendición posterior de socia; cierre conjunto encargada/Tesorera. | Transferencias equivalentes, origen recuperable, ambas intervenciones en cierre. |
| RF-TRA-002/003/004/005 | Origen de secado/transformación sin relación física totalmente precisada. | Secado de un solo acopio; lote húmedo y seco con consumos/linaje explícitos. Transformación conserva lotes de insumo; venta conserva salida por lote. | Desde una venta se reconstruye acopio de origen; no secado con múltiples acopios. |
| RF-ACC-005 (proposed) | Ejecutar todas las acciones ordinarias y administrar transversalmente. | Superadministradora administra cuentas, permisos y parámetros aprobados y revisa/corrige con auditoría mediante operaciones del módulo. No ejecuta ni aprueba operaciones de negocio. | Positivo: cuenta/configuración/corrección autorizada. Negativo: venta, cobro, entrega, QR, multa, excepción y cierre. No firmas por terceros. |
| RF-ASI-003/006/007 | Algunas propuestas daban ejecución transversal a Superadministradora. | Corrección administrativa auditada sin reemplazar cargo: Secretaria opera QR, Presidenta decide justificativos y Tesorera decide impugnación/valida y cobra multa. | Concesión administrativa no habilita esos actos de negocio. |
| RF-VEN-006/009 | Hipótesis de Superadministradora vendedora y su autoaprobación. | Beneficiarias son encargadas de feria conforme reglas; Superadministradora no vende ni acepta comisiones por su rol. Cada beneficiaria acepta la cuota de su versión. | Cambio de versión exige nuevas aceptaciones; sin sustitución administrativa. |

Los IDs se conservan para trazabilidad. No se cancela globalmente RF-CXC-001/002 porque la rendición interna sigue siendo necesaria. D-24 no elimina pagos internos parciales por inferencia. No se añade facturación fiscal, reserva anticipada ni entrega parcial automática.

## Historias afectadas

| ID existente | Ajuste candidato / prueba |
|---|---|
| HU-VEN-001 | Venta desde custodia/encargo y cobro antes de entrega; Superadministradora denegada. |
| HU-VEN-002 | Público general para contado ordinario; identificación institucional; retirar crédito. |
| HU-VEN-006/007/008 | Origen individual/compartido, contado institucional y comprobante único por venta; rendición/cierre conciliables. |
| HU-CXC-001 | Custodia sin deuda al recibir; obligación interna al vender, sin cuenta por cobrar externa. |
| HU-CXC-002 | Abono de rendición interna con saldo identificado; no cuotas de crédito de comprador. |
| HU-TRA-002/003/004/005 | Secado con único acopio, consumos/linaje, receta versionada y salidas por lote. |
| HU-ACC-005 | Administrar permisos existentes; no concesión individual de autoridad Superadministradora por módulo. |
| HU-ACC-006/007/008 | Designación con autorización presidencial; configuración dentro de reglas aprobadas; no ejecución de negocio. |
| HU-ACC-009 | Sustituir «crear y corregir registros de cualquier módulo» por revisión/corrección auditada, sin ejecutar ni aprobar negocio. |
| HU-ASI-003/006/007 | Corrección e impugnación/QR mantienen cargo competente; no bypass administrativo. |

Los criterios completos del diseño están en DAT-01 a DAT-15 de la revisión 0.2. Las HU de requisitos sin ficha existente se conservan como brecha documental; no se inventan IDs nuevos para aparentar cobertura.

## Pila, historia técnica y sprint backlog

- HT-PRE-003 / SB-S1-03: incorporar relaciones corregidas, matriz de permisos, transacciones y casos DAT como evidencia de avance. S1 conserva su cierre por calendario; revisión se ejecuta durante S2. No se marca el entregable completo por escribir esta nota.
- SB-S5-01: configuraciones/precios/recetas sin valores inventados; DAT-08/09.
- SB-S5-02/03: acopio, secado único, linaje y movimientos; DAT-01 a 04.
- SB-S5-04: custodia y rendición, cierre conjunto; DAT-06/11.
- SB-S5-05: cobro/entrega sin crédito, institucional y permisos; DAT-04/05/07/10.
- SB-S5-06: gastos, rendición interna y conciliación; reembolso pendiente; DAT-06/11/12/13.
- HU-ACC-005 a 009: conservar ubicación/estimación propuestas; sustituir criterios incompatibles antes de implementar SPEC-002. No mover trabajo de S5 a S2 por esta enmienda.

## Límites de terminación

Sincronización editorial local por adendas: [[../../../documentacion/requisitos/requisitos_generales_v2.4_2026-10-29|requisitos 2.4]], [[../../../documentacion/historias/usuario/historias_usuario_v2.9_2026-10-29|HU 2.9]], [[../../../documentacion/historias/tecnicas/historias_tecnicas_v2.0_2026-10-29|HT 2.0]], [[../../../documentacion/pila_producto/pila_producto_v2.1_2026-10-29|pila 2.1]], [[../../../documentacion/sprints/sprint_backlog_v1.7_2026-10-29|backlog 1.7]] y [[../../../documentacion/control_de_cambios/registro_v5.4_2026-10-29|control 5.4]]. La revisión de cada adenda y la reconciliación del CAT confirmado conservan su estado pendiente.

Estructura técnica corregida no significa software terminado. Pendientes: revisión de las discrepancias con CAT/SPEC-002, parámetros de P-04/P-08, política offline P-13/P-14 y D-29. Las operaciones independientes pueden avanzar con requisito y sprint vigentes. Las ediciones anteriores, aprobaciones y evidencia no se sobrescriben.

## Historial

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 0.1 | 2026-10-29 | D-24 a D-30 y correcciones de relaciones/integridad; sincronización por adendas. | Propuesta solicitada por tesista; revisión/validación organizacional pendientes. |
