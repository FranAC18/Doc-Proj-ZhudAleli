---
title: Resolución de ocho decisiones del flujo organizacional
version: "1.2"
date: 2026-10-30
author: Codex, por instrucción del tesista
status: prepared-for-academic-review
decision_source: respuestas-expresas-tesista-1A-2B-3B-4A-5A-6A-7A-8B
organizational_validation: pending-direct-evidence
publication: pending
implementation_status: logical-design-only
phase: pre_commit
commit: pending
---

# Resolución de ocho decisiones del flujo organizacional

El tesista respondió expresamente `1A, 2B, 3B, 4A, 5A, 6A, 7A, 8B` al análisis de coherencia del 30/10/2026. Esta edición sustituye las reglas incompatibles de la [adenda v1.1](adenda_diseno_base_datos_v1.1_2026-10-30.md) y del [diseño v1.0](diseno_base_datos_v1.0_2026-10-30.md). Las respuestas cierran estas ocho decisiones para la revisión del diseño; no acreditan implementación ni validación organizacional directa.

## Decisiones y efecto sobre el modelo

| Respuesta | Regla elegida | Consecuencia |
|---|---|---|
| 1A | El excedente del stock individual pertenece siempre a su dueña, aunque otra socia venda durante una ausencia o relevo. | Conservar dueña del stock, vendedora efectiva y persona que registra como identidades distintas. El relevo no transfiere el excedente individual. |
| 2B | El cierre del reparto queda pendiente hasta asignar todo el fondo disponible. | Durante preparación la suma no excede el fondo; al cerrar debe igualar el fondo positivo, al centavo. El remanente no pasa automáticamente a la asociación. Con fondo cero o negativo no se crean pagos de comisión; la diferencia negativa conserva su conciliación. |
| 3B | La asociación devuelve el total y absorbe el defecto de fabricación; la socia conserva su excedente. | Registrar el reembolso como salida real de dinero de la asociación, vinculada al caso y a la venta o resumen verificado. Conservar base y reparto históricos: no recuperar el excedente de la socia por ese defecto ni contabilizar dos veces el mismo reembolso. Esta decisión no atribuye a la asociación daños causados por terceros por inferencia. |
| 4A | Sin comprobante obligatorio, la Tesorera verifica con la vendedora producto, cantidad, fecha y pago; deja constancia de la comprobación y del artículo recibido. | Caso de devolución con evidencia de revisión y vínculo al resumen de ventas, sin imponer ficha de comprador. Registrar devoluciones anteriores y cantidades para evitar duplicaciones; el control agregado no demuestra por sí solo una compra individual. |
| 5A | La habilitación de devoluciones es global y versionada; cada venta conserva la política aplicable al realizarse. Desactivar después no cambia los casos ya admitidos. | Solo Superadministración cambia la política. La venta conserva versión; la solicitud conserva entrega y plazo calculado. Se adopta el cómputo propuesto en la pregunta: dos días hábiles desde el día hábil siguiente a la entrega, usando el calendario registrado. No aplicar retrospectivamente el interruptor a operaciones anteriores. |
| 6A | Superadministración puede sustituir decisiones asignadas a otros cargos, incluidos devoluciones y justificativos, registrando que actuó como Superadministración. | El actor, autoridad usada, decisión, fecha y motivo quedan auditados. No exigir aprobación previa de Presidenta/comité para esas operaciones. Se conserva la prohibición de vender personalmente. La revisión de una devolución puede hacerla Tesorera o Superadministración, con las mismas comprobaciones. |
| 7A | La fórmula secreta de champú no se almacena en la aplicación. | Gestionar kit por variante, lote, cantidad utilizada, rendimiento de referencia de 50 litros y resultado real. Mostrar solamente ingredientes de etiqueta oficial. No exigir fórmula secreta ni calcular consumos de ingredientes no registrados. |
| 8B | Durante una caída de conexión continúan las ventas de stock compartido con control provisional por socia y producto; después se registra el resumen y se concilia. | Identificar origen provisional y estado pendiente de verificación. La captura no acredita validación central de stock. Reconciliar cantidades y dinero antes del cierre; vincular capturas y resúmenes para no duplicar ventas cuando vuelve la conexión. |

## Flujo consolidado de trabajo

1. Entregar stock en custodia conserva lote, producto, cantidad y responsable; no genera por sí solo un saldo exigible.
2. Registrar por separado venta individual fuera de feria y venta perteneciente a una feria. Dentro de esta, distinguir stock individual y compartido.
3. El comprador paga antes de recibir. El registro resumido conserva socia vendedora, dueña cuando corresponda, producto, cantidad, origen, precio y valor base históricos. Separar líneas cuando cambie precio, base o política aplicable; no exigir datos de cliente ni nota por comprador.
4. Mostrar base acumulada y entregas de dinero durante el periodo. El cierre concilia lo vendido y lo rendido, evitando volver a exigir importes ya entregados. La organización define el periodo fuera de feria.
5. Todo valor base de productos vendidos corresponde a la asociación. El excedente individual pertenece a la dueña. Fondo compartido = ventas compartidas menos valor base y gastos comunes aprobados.
6. Repartir el fondo compartido proporcionalmente al importe compartido vendido por cada socia o mediante importes acordados manualmente. Conservar versión y aceptación de las beneficiarias. No cerrar con remanente positivo sin asignar.
7. Distinguir importe acordado, pendiente de entrega y efectivamente entregado. La propuesta registra cada desembolso con importe, fecha y responsables; no deduce un pago de la sola aceptación de la cuota.
8. Mantener devoluciones físicas separadas del inventario vendible. Una anulación solicitada antes de entrega autoriza el reembolso completo sin aprobación adicional; la mera espera de entrega no causa una anulación. Separar autorización automática del hecho de devolver efectivo o completar una transferencia.
9. Una devolución admitida por defecto de fabricación produce reembolso completo financiado por la asociación, sin quitar el excedente a la socia. Un cierre histórico se conserva; la devolución posterior genera un ajuste vinculado y visible.

## Sustituciones y límites

- La prohibición general de Superadministración de ejecutar/aprobar negocio y la exclusividad de revisiones de cargos descritas en versiones anteriores quedan sustituidas por 6A. La prohibición de venta personal permanece.
- La regla anterior que impedía vender stock compartido sin red queda sustituida por 8B. La verificación central y conciliación posterior siguen siendo necesarias; no se declara que la captura local garantiza saldo global.
- La expectativa de almacenar posteriormente fórmulas secretas de champú queda retirada por 7A. Las recetas de otros productos conservan su alcance previo. Cincuenta litros es rendimiento de referencia, no prueba de producción efectiva ni de cien envases realmente obtenidos.
- El remanente del reparto y el alcance del interruptor de devoluciones ya están resueltos. Los importes manuales no utilizan automáticamente un reparto igualitario. D-30 conserva redondeo y desempate por ID de asignación para el cálculo proporcional cuando corresponda.
- El procedimiento previo D-19 para otorgar/revocar la autoridad Superadministradora se conserva; 6A responde sobre decisiones operativas y no autoriza autootorgamiento por inferencia.
- La responsabilidad por daño ajeno a defecto de fabricación, los valores de descuentos y el calendario concreto de periodos mantienen su definición específica pendiente. No se extiende 3B a causas diferentes.

## Alcance documental y continuidad

Fuente principal: respuestas expresas del tesista en este chat del 30/10/2026. Referencias: [CAT-REQ-001](../../docs/requirements/CAT-REQ-001.md), [registro previo de decisiones](../../docs/architecture/proposals/2026-10-29-decisiones-pendientes-diseno-datos.md) y [adenda anterior](adenda_diseno_base_datos_v1.1_2026-10-30.md).

Los textos antiguos se conservan como antecedentes. Sigue pendiente consolidar el diccionario completo, RF/HU/HT, pila, backlog y gestor local con estas reglas; esta edición no afirma que esa sincronización esté realizada. No cambia estados de cumplimiento, no aplica migraciones y no acredita una jornada de validación con socias.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.2 | 2026-10-30 | Registra las ocho elecciones explícitas, sus efectos y sustituciones; conserva los límites de verificación e implementación. |
