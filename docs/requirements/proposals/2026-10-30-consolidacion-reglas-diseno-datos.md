---
title: Consolidación de reglas para diseño de datos
status: proposed
date: 2026-10-30
author: Codex por instrucción expresa del tesista
organization_validation: pending-direct-evidence
task_id: SB-S1-03
commit: pending
---

# Consolidación de requisitos y decisiones

Fuente: decisiones expresas del tesista del 30/10, incluyendo 1A, 2B, 3B, 4A, 5A, 6A, 7A, 8B, y solicitud de consolidar. [Diseño único v2.0](../../../documentacion/arquitectura/diseno_base_datos_v2.0_2026-10-30.md) contiene reglas C01–C18, entidades y 20 casos de verificación. Reemplaza la enmienda del 29/10 para estos temas; no altera evidencia de aprobación del CAT.

## Discrepancias resueltas para el diseño

- D28 administración sin negocio: sustituido por ejecución/aprobación y sustitución de cargos; sigue prohibida venta personal. D19 designación presidencial se conserva.
- D29 ajustes desconocidos: cancelación sin entrega, defecto, sobrepago y faltante ahora definidos. Daño de otra causa requiere decisión económica específica.
- Deuda por cada venta: saldo acumulado visible, liquidación formal periódica y anticipos aplicables una sola vez.
- Reparto igualitario: sustituido por proporcional a ventas compartidas o manual negociado; cerrar exige asignación exacta.
- Stock compartido solo online: sustituido por contingencia provisional conciliada.
- Receta secreta aplazada: retirada del almacenamiento; kit por variante y resultado real.
- Factura/comprador por venta de feria: resumen por vendedora/producto/origen, nota opcional, evidencia de verificación para retornos.

## Requisitos

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

## Historias

| ID | Reglas | Criterio vigente de esta revisión |
|---|---|---|
| HU-VEN-001 | C01-C03, C14-C15 | Venta pagada antes de entrega; distinguir contexto feria/individual y origen individual/compartido. Dueña, vendedora y registradora diferentes; Superadministradora no vende. |
| HU-VEN-002 | C01, C15 | Sin crédito al comprador. Resumen de feria sin datos de cliente obligatorios y nota opcional; precio, base y política históricos por línea. |
| HU-VEN-007 | C01 | Venta institucional identificada, pago completo antes de entregar y sin excedente individual; la prohibición de venta personal incluye a Superadministración. |
| HU-VEN-006 | C03, C06, C18 | Repartir solo fondo compartido: proporcional a ventas compartidas por vendedora o montos negociados. Excedente individual de dueña excluido; suma exacta al cierre. |
| HU-VEN-008 | C01, C15 | Sin crédito al comprador. Resumen de feria sin datos de cliente obligatorios y nota opcional; precio, base y política históricos por línea. |
| HU-CXC-001 | C01, C04-C05 | Custodia sin deuda. Base acumulada visible y obligación interna al cierre del periodo, con fuente por venta o resolución de faltante. No crédito externo. |
| HU-CXC-002 | C04-C05 | Entregas de dinero durante jornada o al final, aplicadas una sola vez al periodo y liquidación. Abonos internos sin duplicar cobro ni saldo. |
| HU-TRA-002 | C16 | Secado de un solo acopio, consumos efectivos, lote húmedo/seco y linaje conservado. |
| HU-TRA-003 | C16-C17 | Transformación por receta autorizada o kit por variante, referencia 50 L y salida real separada. Fórmula secreta de shampoo no se almacena. |
| HU-TRA-004 | C16-C17 | Lotes y consumos conservan origen; unidades compatibles, etiqueta oficial del kit sin fórmula secreta. |
| HU-TRA-005 | C16 | Salida de venta por lote y presentación permite reconstruir acopio o kit, sin ciclos ni origen inventado. |
| HU-ACC-005 | C13 | Administrar permisos existentes sin concesión por módulo; autoridad organizacional separada de is_superuser. No habilitar venta personal. |
| HU-ACC-006 | C13 | Concesión/revocación con autorización presidencial D19 y evidencia; varias administradoras posibles, sin autoconcesión. |
| HU-ACC-007 | C13 | Conservar historial de concesión/revocación y actor real; la autonomía operativa no cambia la designación del rol. |
| HU-ACC-008 | C13 | Superadministradora ejecuta, aprueba y sustituye cargos sin permiso previo; no vende personalmente. Actor y autoridad auditados. Concesión/revocación conserva D19. |
| HU-ACC-009 | C13 | Superadministradora ejecuta, aprueba y sustituye cargos sin permiso previo; no vende personalmente. Actor y autoridad auditados. Concesión/revocación conserva D19. |
| HU-ASI-003 | C13 | Cargo competente o sustitución por Superadministradora decide con actor real, motivo y evidencia; no suplantar autoridad ajena. |
| HU-ASI-006 | C13 | Justificaciones e impugnaciones conservan su revisión y evidencia; Superadministradora puede sustituir la decisión y deja auditoría. |
| HU-ASI-007 | C13 | Secretaria o Superadministradora opera fases QR; vigencia y correcciones auditadas, tokens protegidos. |

## Trabajo técnico y sprint

| ID | Reglas | Criterio vigente de esta revisión |
|---|---|---|
| HT-PRE-003 | C01-C18 / DB-01 a DB-20 | Preparar esquema por módulo con identidades, flujos de stock y dinero, cierre periódico, devoluciones, reparto, políticas e idempotencia; pruebas PostgreSQL y migraciones pendientes. |
| Tarea | Contenido consolidado |
|---|---|
| SB-S1-03 | Diseño consolidado v2.0 y 20 casos definidos. Trabajo documental listo para diseño físico; no certifica implementación ni cierre de tarea. |
| SB-S5-01 | Catálogo, valores versionados, recetas conocidas y kits 50 L sin fórmula secreta; parámetros incompletos inactivos. |
| SB-S5-02 | Acopio, secado único y lotes; cantidades efectivas y conversiones compatibles. |
| SB-S5-03 | Transformación, kits y movimientos; linaje hasta salida, stock por titular/feria/condición. |
| SB-S5-04 | Custodia sin deuda; rendición periódica y anticipos; conciliación de capturas provisionales y stock. |
| SB-S5-05 | Ventas pagadas, resúmenes de feria, delegación y propiedad del excedente; permisos y prohibición de venta Superadministradora. |
| SB-S5-06 | Dinero, gastos, reembolsos, faltantes y reparto compartido exacto; ejecución separada de autorización y acuerdo. |

## Verificación y estados

Las reglas sustituyen los criterios de diseño anteriores, no el estado de validación organizacional. Las discrepancias del CAT confirmado quedan expresamente identificadas arriba para reconciliación puntual antes de implementar. No se reabren decisiones ya contestadas ni se inventan IDs o aprobaciones. Pruebas de producto pendientes. Configuraciones concretas y responsabilidad por daños no fabriles se delimitan en §12 del diseño, sin impedir modelar los flujos definidos.

Ediciones sincronizadas: requisitos 2.5, HU 3.0, HT 2.1, pila 2.2, backlog 1.8; índice/control 5.8. Evidencia de persistencia del gestor y controles documentales en [verificación](../../evidence/architecture/2026-10-30-consolidacion/verificacion.json).
