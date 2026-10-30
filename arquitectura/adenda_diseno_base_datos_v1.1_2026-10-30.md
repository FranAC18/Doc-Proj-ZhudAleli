---
title: Adenda de decisiones del diseño lógico de base de datos
type: database-design-addendum
version: "1.1"
date: 2026-10-30
author: "Codex, bajo instrucción del tesista"
status: prepared-for-academic-review
academic_review: pending
organizational_validation: pending-direct-evidence
publication: pending
implementation_status: logical-design-only
base_document: diseno_base_datos_v1.0_2026-10-30.md
phase: pre_commit
commit: pending
---

# Adenda de decisiones del diseño lógico de base de datos

Esta adenda incorpora las precisiones del tesista del 30/10/2026 a la [edición 1.0](diseno_base_datos_v1.0_2026-10-30.md). En los temas tratados aquí, prevalece sobre el texto anterior. Registra instrucciones directas del tesista para orientar la propuesta; no afirma que los requisitos en CAT-REQ-001 o SPEC-002 hayan sido formalmente aprobados o actualizados. No acredita modelos, migraciones ni pruebas de producto.

**Referencias previas que se sustituyen:** el criterio de reparto de centavos aceptado en D-30 usa el ID menor de la asignación de encargada, aunque D-09 conserve la frase histórica “encargo menor”. La hipótesis de D-23 sobre una Superadministradora que vende queda sin caso porque se mantiene la prohibición de venta personal. El alcance general restrictivo de D-28 queda reemplazado por la regla de Superadministración de esta adenda.

## Reglas incorporadas

| Tema | Regla para el modelo lógico |
|---|---|
| Superadministración | La Superadministradora puede ejecutar y aprobar operaciones de negocio sin autorización previa de la Presidenta o del comité. Conserva la prohibición expresa de vender personalmente. En operaciones con un control específico ya indicado —por ejemplo, revisión de devoluciones por la Tesorera— se conserva ese paso específico. Esta instrucción reemplaza el límite general anterior de D-28; el estado propuesto de RF-ACC-005 y la asignación/revocación de la autoridad requieren reconciliación documental. |
| Venta individual y feria | Son contextos separados. Una venta individual no se registra como venta de feria. En una feria, el stock individual de cada socia se mantiene separado del stock compartido y cada salida identifica su origen y vendedora. |
| Valor base | El valor base de cada producto vendido vuelve a la asociación, sin importar si se vendió desde stock individual o compartido. En stock individual, el excedente sobre el valor base corresponde a la dueña del stock. El excedente de stock compartido se distribuye conforme a un modo acordado, luego de descontar gastos comunes aprobados. |
| Rendición | La socia liquida el valor base al cierre de ventas del periodo que defina la organización. En feria puede entregarlo durante la jornada o al final de esta, manteniendo cada entrega asociada a las ventas que liquida. El periodo configurable aún no tiene una duración fija. |
| Reparto de stock compartido | Se permiten dos modos: proporcional al importe de ventas compartidas registrado por cada socia; o asignación manual de importes acordados verbalmente. El total asignado no puede superar el fondo disponible. |
| Registro resumido de feria | La aplicación registra totales por socia, producto y origen de stock durante la jornada, sin exigir identificación del comprador ni nota de venta por persona. La nota de venta puede emitirse cuando se necesite. |
| Anulación pagada sin entrega | Si el comprador ya pagó y todavía no recibió el producto, se devuelve automáticamente el total cobrado, sin autorización adicional. El evento de anulación y la devolución quedan vinculados y auditados. |
| Devolución de producto entregado | Puede solicitarse dentro de dos días hábiles, solo por defecto de fábrica o daño. La Tesorera revisa el caso. Si procede, se reembolsa el total por el mismo medio cuando sea posible; el producto recibido queda separado y no vuelve al stock vendible. |
| Habilitación de devoluciones | La Superadministradora dispone de un control exclusivo para habilitar o deshabilitar devoluciones. Al habilitarlas, se aplican las condiciones de plazo, defecto/daño y revisión de la Tesorera indicadas arriba. El alcance global o por tipo de venta/producto está pendiente. |
| Faltantes de custodia | Si la revisión confirma responsabilidad de la socia, el faltante genera una obligación por rendir calculada al valor base de las unidades afectadas. La transferencia inicial a custodia no genera obligación. |
| Sobrepago | El excedente se devuelve al mismo pagador y, cuando sea posible, por el mismo medio, con aprobación y comprobante de la Tesorera. No se deja un saldo a favor del comprador. |
| Operación offline | Se puede completar una venta offline solo contra stock individual asignado a la socia, con pago completo y comprobante local. El stock compartido de feria requiere conexión. El stock individual llevado a feria se identifica separado del compartido. |
| Producción y secreto de receta | La materia prima se registra en kilogramos y no se convierte masa a volumen. Cada variante de champú tiene un kit cuyo rendimiento de referencia es 50 litros. La composición y las cantidades internas se documentarán después y se tratarán como confidenciales; la lista pública se limita a los ingredientes de la etiqueta oficial. |

## Reglas del cierre de feria

La pantalla de cierre debe mantener separados estos bloques para facilitar el cotejo:

1. Stock individual y compartido recibido, vendido, devuelto y restante, desglosado por producto y socia.
2. Valor base de todas las ventas que vuelve a la asociación.
3. Excedentes de ventas desde stock individual, asignados a sus dueñas.
4. Fondo de stock compartido: ventas compartidas menos valores base y gastos comunes aprobados.
5. Reparto del fondo compartido mediante el modo proporcional o los importes manuales negociados.
6. Rendiciones realizadas durante la jornada y saldo pendiente de entregar al cierre del periodo.

La aplicación no exige factura ni comprobante individual para cada comprador. Conserva la opción de emitir nota de venta y registra agregados suficientes para cuadrar cantidades, valor base y beneficiarias. El cálculo proporcional usa los importes compartidos registrados a nombre de cada socia; el modo manual conserva los importes acordados y su versión.

## Ajustes de vocabulario y trazabilidad

- En reportes, presentar la obligación interna como **saldo por rendir** para distinguirla de una deuda o venta a crédito del comprador. El nombre físico `trazabilidad_deuda_socia` de la edición 1.0 queda como propuesta por revisar.
- La venta de una socia fuera de feria y la participación de esa socia en una feria son hechos distintos; los reportes no agregan sus fondos como si fueran un solo cierre.
- Los importes manuales de reparto requieren control de suma contra el fondo disponible y trazabilidad de quién los registró y aceptó. La distribución no modifica el valor base que corresponde a la asociación.
- La receta confidencial, si se almacena, debe tener control de acceso separado de la etiqueta pública. Los roles exactos que pueden consultarla se precisarán antes de habilitar el módulo de producción.

## Pendientes concretos

1. **Remanente del reparto manual:** el importe acordado puede ser menor que el fondo, pero no puede excederlo. Falta decidir si el remanente se conserva para la asociación o queda pendiente de una nueva negociación antes del cierre.
2. **Autoridad Superadministradora:** queda por reconciliar con RF-ACC-005 y SPEC-002. También falta precisar si la facultad general para ejecutar/aprobar negocio incluye otorgar o revocar la propia autoridad Superadministradora; esa operación se conserva bajo control pendiente.
3. **Devoluciones:** el control Superadministrador puede ser global o segmentado por producto/tipo de venta. También falta precisar si los dos días hábiles empiezan el día hábil siguiente a la compra o a partir de la entrega.
4. **Rendición:** se pueden registrar pagos parciales durante la jornada y al final, pero el intervalo máximo fuera de ferias aún lo define la organización.
5. **Reparto y pagos:** las beneficiarias y los importes deben quedar registrados; está pendiente decidir si la aplicación registra también cada desembolso efectivo de comisión y quién captura los importes acordados.
6. **Recetas:** se conoce el rendimiento de 50 litros para cada variante de champú; no se ingresan ingredientes ni cantidades internas hasta recibir los datos autorizados. El catálogo de la etiqueta se conserva separado.
7. **Descuentos:** permanecen inactivos hasta validar umbrales y valores; no se inventan porcentajes ni precios.

## Fuentes y estado de revisión

Fuentes: respuestas directas del tesista del 30/10/2026; [diseño base de datos v1.0](diseno_base_datos_v1.0_2026-10-30.md); [CAT-REQ-001 v1.3](../../docs/requirements/CAT-REQ-001.md); [enmienda propuesta de datos](../../docs/requirements/proposals/2026-10-29-enmienda-datos-sin-credito-y-administracion.md).

La propuesta sigue pendiente de revisión académica, validación organizacional cuando corresponda, sincronización de requisitos/historias y actualización del gestor local. No se modifican las aprobaciones ni los estados del sprint. Esta adenda no se ha publicado al docente y no cambia el código de la aplicación.

## Historial

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.1 | 2026-10-30 | Codex, bajo instrucción del tesista | Incorpora separación feria/venta individual, rendición de valor base, reparto, control de devoluciones, autonomía de Superadministración con prohibición de venta, registro resumido de feria y confidencialidad de recetas. | Preparada localmente; revisión y validación pendientes. |
