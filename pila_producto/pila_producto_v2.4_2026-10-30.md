---
titulo: Pila de producto: alcance de datos consolidado
version: "2.4"
fecha: 2026-10-30
autor: Codex por instrucción del tesista
estado: consolidado-para-revision
validacion_organizacional: evidencia-directa-pendiente
publicacion: pendiente
---

# Pila de producto: alcance de datos consolidado

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación integral.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.2](../arquitectura/diseno_base_datos_v2.2_2026-10-30.md). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

| ID | Reglas | Criterio vigente de esta revisión |
|---|---|---|
| HT-PRE-003 | C01-C18 / DB-01 a DB-20 | Preparar esquema por módulo con identidades, flujos de stock y dinero, cierre periódico, devoluciones, reparto, políticas e idempotencia; pruebas PostgreSQL y migraciones pendientes. |
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

Se conserva orden, puntos y prioridad de la [base v2.0](pila_producto_v2.0_2026-10-28.md). Dependencias técnicas: catálogo/unidades → producción/stock → venta pagada → rendición → cierre/reparto y ajustes. No mueve S5 a S2.


## Ruta de programación de módulos

1. Completar los pendientes de acceso y delimitar operaciones de cuentas/membresías con permisos verificables en Sprint 2.
2. Iniciar planificación por actividades con SB-S3-01; continuar con asignaciones y encargos según criterios confirmados.
3. Implementar asistencia/participación en S4 cuando planificación proporcione su contexto.
4. Implementar en S5 la cadena de catálogo, acopio, secado, lotes y existencias; ampliar comercio y rendición según reglas disponibles.

Las fechas y el orden de dependencias de la hoja de ruta se conservan. No se habilitan operaciones de escritura con una matriz de permisos incompleta.

## Control de edición

2.3 → 2.4, 2026-10-30: se documenta la secuencia de implementación desde Sprint 2 hacia planificación, asistencia y trazabilidad; sin mover prioridad, fecha ni compromiso.

2.2, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Secuencia de programación por módulos — 2026-10-30

La programación ya inició con la base física de identidad y membresías en accounts; su avance está limitado a las tablas y garantías descritas en el checkpoint de implementación. SB-S2-03 permanece en curso parcial, SB-S2-02 abierto y SB-S2-05 parcial.

Se conserva el orden de la hoja de ruta: terminar los recorridos de acceso y las operaciones de cuentas que estén respaldadas por permisos definidos; después comenzar planificación con SB-S3-01, seguir con asistencia en S4 y la cadena de trazabilidad en S5. No se trasladan tareas entre sprints, ni se inventan estimaciones, fechas, responsables o criterios. La matriz de permisos por cargo y operación pendiente condiciona los cambios que alteren datos organizacionales.
