---
titulo: Registro de cobertura y pendientes documentales
codigo: ZA-SEG-002
version: "1.0"
fecha: 2026-10-19
autor: Franklin Acero
elaboracion: Asistencia de Codex a solicitud del tesista
estado: preparado-para-revision
publicacion: pendiente-de-transferencia
---

# Registro de cobertura y pendientes documentales

## Alcance de la revisión

Se comparó la lista de 58 RF confirmados de requisitos generales v2.0 y CAT-REQ-001 v1.2 con las referencias de historias de usuario v2.5 y pila de producto v1.6. La revisión identificó 51 RF cubiertos por referencias y siete sin referencia en esas ediciones. La diferencia no cuenta con una agrupación explícita que permita declarar cobertura completa.

Este registro documenta hallazgos. No actualiza todavía las historias, no aprueba criterios nuevos y no compromete capacidad o fechas de sprint. Las comprobaciones corresponden a trabajo posterior a Sprint 0.

## RF sin referencia en las ediciones revisadas

| Requisito | Capacidad confirmada | Actualización documental pendiente | Decisiones de detalle que deben conservarse abiertas |
|---|---|---|---|
| RF-DOC-001 | Gestión y versiones de documentos | Incorporar historia, criterios y referencia en la pila. | Tipos, metadatos, plazos, retención y documentos personales. |
| RF-AST-001 | Registro de activos e historial | Incorporar historia y distinguir activos de existencias consumibles. | La depreciación queda fuera hasta aprobar método y vida útil. |
| RF-INV-005 | Custodia individual y conciliación de inventario | Incorporar historia y criterios de transferencias sin deuda automática. | Propiedad, faltantes y conciliación monetaria. |
| RF-INV-006 | Alertas de existencias mínimas | Incorporar historia y criterios de umbrales y unidades compatibles. | Catálogo, mínimos, mermas y responsables. |
| RF-PUB-003 | Precios publicados y contacto contextual | Incorporar historia y distinguir consulta de pedido o venta. | Aprobación y vigencia de precios, alcance del contacto. |
| RF-VEN-009 | Distribución de comisiones de feria | Incorporar historia y trazabilidad de fórmula y base. | Porcentajes, destinatarios y excepciones; no calcular una distribución sin fórmula aprobada. |
| RF-NOT-002 | Recordatorios externos autorizados | Incorporar historia condicionada a habilitación y consentimiento. | Canal, proveedor, contenido y costo; reintentos sin duplicados. |

## Historias existentes que requieren cotejo

| Referencia | Hallazgo o trabajo requerido |
|---|---|
| RF-ASI-006 / HU-ASI-006 | La historia conserva resolución por asamblea sin sanción automática. Debe alinearse con la falta automática, plazo máximo de tres días hábiles para justificar y validación de multas por la Tesorera, sin resolver por inferencia P-03. |
| RF-PLA-003 | Cotejar su ampliación en CAT v1.2 con la historia y criterios actuales. |
| RF-NOT-001 | Cotejar su ampliación y mantener consistencia con notificaciones internas y externas. |
| RF-TRA-005 | Cotejar la ampliación vigente con criterios y trazabilidad de la historia. |
| RF-GAS-001 | Cotejar la ampliación vigente con criterios de registro y control de gastos. |
| RF-REP-005 | Cotejar la ampliación vigente con los criterios del reporte correspondiente. |

Las notas de HU v2.5 y pila v1.6 que presentan todas las novedades de entrevista como exploración pendiente deben distinguir los siete RF ya confirmados de sus reglas de detalle todavía abiertas. La aprobación del tesista y la validación académica u organizacional son estados diferentes.

## Criterios para verificar la actualización posterior

1. Preparar nuevas ediciones de HU y pila conservando las anteriores.
2. Relacionar los 58 RF confirmados con historias y entradas de pila; si se agrupan, documentar expresamente la correspondencia.
3. Comprobar los criterios de los seis RF ampliados y conservar decisiones abiertas identificables.
4. Mantener RF-COS-001 y RNF-OPS-001 como propuestos; no convertirlos en compromisos aprobados.
5. Conservar estimación, capacidad, responsable y compromiso de sprint como pendientes donde no exista evidencia.
6. Actualizar compendios derivados, índice y control de cambios cuando las nuevas ediciones estén revisadas.
7. Verificar IDs, enlaces, coherencia de estados y diferencias antes de publicar.

## Fuentes

- [Requisitos generales v2.0](../requisitos/requisitos_generales_v2.0_2026-10-13.md).
- [Historias de usuario v2.5](../historias/usuario/historias_usuario_v2.5_2026-10-13.md).
- [Pila de producto v1.6](../pila_producto/pila_producto_v1.6_2026-10-14.md).
- [Priorización v1.3](../requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13.md).
- Fuente interna: CAT-REQ-001 v1.2 y revisión de trazabilidad del 18 de octubre de 2026.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-19 | Registra siete RF sin referencia y seis ampliaciones por cotejar; no presenta los hallazgos como resueltos. |
