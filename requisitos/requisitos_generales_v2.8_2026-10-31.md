---
titulo: Requisitos afectados: consolidación de datos
version: "2.8"
fecha: 2026-10-31
autor: Codex por instrucción del tesista
estado: consolidado-para-revision
validacion_organizacional: evidencia-directa-pendiente
publicacion: pendiente
---

# Requisitos afectados: consolidación de datos

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación integral.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.2](../arquitectura/diseno_base_datos_v2.2_2026-10-30.md). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

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

2.7 → 2.8, 2026-10-31: se registra el inicio parcial de membresías y planificación, la autorización operativa expresada por el tesista y la verificación técnica; no cambian criterios, prioridades, sprint asignado ni aprobaciones de requisitos.

2.5, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Avance técnico de esta edición 2.7

En App-zhudaleli, el commit [c9f2d6a3e0f0fa474485546075eda55e8d729592](https://github.com/FranAC18/App-zhudaleli/commit/c9f2d6a3e0f0fa474485546075eda55e8d729592), rama `feature/RF-PLA-001-actividades`, incorpora la migración `accounts.0006` con el catálogo de cargos y el historial de designaciones, operaciones transaccionales para iniciar/cerrar membresías y la primera porción del módulo `planning` con actividades, responsables y participantes. Ambas migraciones (`accounts.0006` y `planning.0001`) se aplicaron en `zhud_aleli_dev`.

Verificación: 68 pruebas PostgreSQL, Ruff, `manage.py check`, `makemigrations --check --dry-run` y `git diff --cached --check` correctos. El esquema de desarrollo tiene 19 tablas base y 22 migraciones aplicadas; el catálogo contiene tres cargos y aún no hay designaciones activas. La evidencia UI comprobó los anchos 360, 375, 768, 1280 y 1440 px, navegación por teclado y contraste AA. No se cargaron identidades reales.

El tesista indicó que Presidenta, Tesorera y Secretaria pueden administrar periodos de membresía y crear/editar actividades. Esta instrucción delimita la autorización para la porción de código; no se presenta como validación organizacional directa ni modifica la línea base de requisitos. En el código, las tres operaciones requieren una designación vigente registrada para la cuenta.

RF-ACC-002 queda parcial: se pueden iniciar/cerrar periodos de socias con cuentas ya existentes; crear cuentas, activar/desactivar accesos y administrar designaciones siguen pendientes. RF-PLA-001 queda parcial: se pueden crear/editar actividades básicas con fecha, lugar, responsable, participantes y estado; las instancias recurrentes y el motivo de cancelación indicado en los casos de uso requieren completar su definición. RF-ACC-003 y RF-ACC-005 no reciben alcance nuevo. `SB-S2-03` y `SB-S3-01` siguen parciales; `SB-S2-02` permanece abierto, Sprint 2 sigue activo y `SB-S2-05` conserva su estado parcial. No se cambia sprint asignado, prioridad ni aprobación.

La base local tiene cero designaciones activas; la pantalla de asignación de cargos y los datos de las incumbentes reales no forman parte de esta entrega. Por ello, las cuentas reales de la Directiva aún no pueden ejercer estas operaciones hasta registrar sus designaciones. Véanse el [[../../docs/evidence/requirements/2026-10-30-permisos-directiva-membresias-planificacion|registro de autorización]], el [[../../docs/evidence/architecture/2026-10-30-planificacion-backend/implementacion|resultado técnico]] y el [[../../docs/bitacora/checkpoints/2026-10-31-planificacion-y-membresias|checkpoint]].
