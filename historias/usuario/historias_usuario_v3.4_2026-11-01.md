---
titulo: Historias de usuaria: criterios consolidados de datos
version: "3.4"
fecha: 2026-11-01
autor: Codex por instrucción del tesista
estado: preparado-para-revision-academica
aprobacion_regla_ferias: aprobada-por-tesista
validacion_organizacional: pendiente
publicacion: publicada-para-revision-documental
---

# Historias de usuaria: criterios consolidados de datos

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación integral.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.2](../../arquitectura/diseno_base_datos_v2.2_2026-10-30.md). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

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

Fichas, puntos y dependencias no afectados: [base v2.8](historias_usuario_v2.8_2026-10-28.md). Reembolsos/conciliación conservan RF-CXC-003; no se inventa HU inexistente para aparentar cobertura.


## Criterios de feria aprobados por el tesista — validación organizacional pendiente

Para HU-INV-003/004, HU-VEN-006 y HU-CXC-003, el tesista aprobó el siguiente alcance: por defecto, la feria usa productos de lotes de fábrica. La Superadministradora dispone de una sola opción para habilitar o deshabilitar juntas la recepción individual y la venta individual de productos aportados por socias. Al cierre se calcula la ganancia conjunta como “total recaudado - valor base correspondiente a las cantidades vendidas - gastos de feria”. Únicamente esa ganancia se divide en partes iguales entre las encargadas; el total recaudado no se distribuye ni se asigna la ganancia por titular individual. Se conserva la trazabilidad por lote, origen y titular.

La aprobación del tesista no reemplaza los criterios confirmados de la tabla ni acredita validación organizacional. CAT-REQ-001 y P-07 conservan su estado; las historias mantienen prioridad, puntos, fechas y estado. No se declara implementación.

3.3 → 3.4, 2026-11-01: se incorporan criterios de feria aprobados por el tesista, pendientes de validación organizacional; no se modifican estados ni prioridades.

## Control de edición

3.2 → 3.3, 2026-10-31: se registra avance parcial en HU-ACC-002 y HU-PLA-001/002 y la autorización operativa de tres cargos; se preservan los criterios, estimaciones, prioridades y estados completos/parciales.

3.0, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Avance técnico de esta edición 3.2

En el commit [c9f2d6a3e0f0fa474485546075eda55e8d729592](https://github.com/FranAC18/App-zhudaleli/commit/c9f2d6a3e0f0fa474485546075eda55e8d729592), `accounts` inicia y cierra membresías para cuentas existentes, y `planning` permite registrar/editar actividades y sus responsables y participantes. Pasaron 68 pruebas PostgreSQL, Ruff, `manage.py check` y la revisión de migraciones; las migraciones `accounts.0006` y `planning.0001` están aplicadas en desarrollo.

HU-ACC-002 sigue parcial: falta alta de cuentas, activación/desactivación y gestión de designaciones; no se cierra HU-ACC-003 ni HU-ACC-001. HU-PLA-001 y HU-PLA-002 avanzan parcialmente con campos básicos y selección de participantes/responsable; falta completar instancias, decisiones de cancelación y el recorrido de designación de cargos. La autorización expresada por el tesista para Presidenta, Tesorera y Secretaria se limita a administrar membresías y crear/editar actividades; su validación organizacional directa queda pendiente. La base `zhud_aleli_dev` tiene tres cargos de catálogo y cero designaciones activas, por lo que no se cargaron personas reales ni se habilitó a cuentas reales. No cambian criterios, puntos, dependencias ni aprobaciones.

No cambian criterios, puntos, dependencias ni aprobaciones. Planificación, asistencia y trazabilidad conservan el orden futuro de la hoja de ruta; no se declaran implementadas por este esquema.
