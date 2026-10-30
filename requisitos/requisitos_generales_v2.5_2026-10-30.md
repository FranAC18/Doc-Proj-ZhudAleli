---
titulo: Requisitos afectados: consolidación de datos
version: "2.5"
fecha: 2026-10-30
autor: Codex por instrucción del tesista
estado: consolidado-para-revision
validacion_organizacional: evidencia-directa-pendiente
publicacion: pendiente
---

# Requisitos afectados: consolidación de datos

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.0](../arquitectura/diseno_base_datos_v2.0_2026-10-30.md). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

| ID | Reglas | Criterio vigente de esta revisión |
|---|---|---|
| RF-VEN-001 | C01-C03, C14-C15 | Venta pagada antes de entrega; distinguir contexto feria/individual y origen individual/compartido. Dueña, vendedora y registradora diferentes; Superadministradora no vende. |
| RF-VEN-002 | C01, C15 | Sin crédito al comprador. Resumen de feria sin datos de cliente obligatorios y nota opcional; precio, base y política históricos por línea. |
| RF-VEN-007 | C01 | Venta institucional identificada, pago completo antes de entregar y sin excedente individual; la prohibición de venta personal incluye a Superadministración. |
| RF-CXC-001 | C01, C04-C05 | Custodia sin deuda. Base acumulada visible y obligación interna al cierre del periodo, con fuente por venta o resolución de faltante. No crédito externo. |
| RF-CXC-002 | C04-C05 | Entregas de dinero durante jornada o al final, aplicadas una sola vez al periodo y liquidación. Abonos internos sin duplicar cobro ni saldo. |
| RF-CXC-003 | C07-C12 | Conciliación de cancelaciones, devoluciones, sobrepagos y faltantes; autorización separada de ejecución. Defecto de fabricación a cargo de asociación sin recuperar excedente de socia. |
| RF-ACC-005 | C13 | Superadministradora ejecuta, aprueba y sustituye cargos sin permiso previo; no vende personalmente. Actor y autoridad auditados. Concesión/revocación conserva D19. |
| RF-TRA-002 | C16 | Secado de un solo acopio, consumos efectivos, lote húmedo/seco y linaje conservado. |
| RF-TRA-003 | C16-C17 | Transformación por receta autorizada o kit por variante, referencia 50 L y salida real separada. Fórmula secreta de shampoo no se almacena. |
| RF-TRA-004 | C16-C17 | Lotes y consumos conservan origen; unidades compatibles, etiqueta oficial del kit sin fórmula secreta. |
| RF-TRA-005 | C16 | Salida de venta por lote y presentación permite reconstruir acopio o kit, sin ciclos ni origen inventado. |
| RF-INV-003 | C01-C03 | Entrega en custodia conserva lote, presentación, titular, feria y condición. No crea deuda ni venta. |
| RF-INV-004 | C05, C14 | Conciliar stock físico, capturas y dinero al cierre; provisional compartido offline conserva diferencias hasta resolución, sin stock confirmado negativo. |
| RF-INV-005 | C08, C12, C14 | Retorno segregado; faltante solo causa cargo tras responsabilidad decidida; transferencias y correcciones auditadas, sin borrar hechos. |
| RF-ASI-003 | C13 | Cargo competente o sustitución por Superadministradora decide con actor real, motivo y evidencia; no suplantar autoridad ajena. |
| RF-ASI-006 | C13 | Justificaciones e impugnaciones conservan su revisión y evidencia; Superadministradora puede sustituir la decisión y deja auditoría. |
| RF-ASI-007 | C13 | Secretaria o Superadministradora opera fases QR; vigencia y correcciones auditadas, tokens protegidos. |
| RF-VEN-006 | C03, C06, C18 | Repartir solo fondo compartido: proporcional a ventas compartidas por vendedora o montos negociados. Excedente individual de dueña excluido; suma exacta al cierre. |
| RF-VEN-009 | C06, C18 | Cuotas por socia y versión, acuerdo y pago separados; cambios exigen nuevas aceptaciones. Redondeo por restos y desempate por ID de asignación. Sin pago duplicado. |

Catálogo completo no afectado: [base v2.3](requisitos_generales_v2.3_2026-10-28.md). RF-ACC-005 conserva estado propuesto. No se cancela CXC: mantiene rendición interna.


## Control de edición

2.5, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.
