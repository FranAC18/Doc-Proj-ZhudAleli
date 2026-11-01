---
titulo: Historias de usuaria: criterios consolidados de datos
version: "3.1"
fecha: 2026-10-30
autor: Codex por instrucción del tesista
estado: consolidado-para-revision
validacion_organizacional: evidencia-directa-pendiente
publicacion: pendiente
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


## Control de edición

3.0, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Avance técnico de esta edición 3.1

Refuerzo de normalización 2026-10-30: ER/base lógica v2.2 con relaciones y claves corregidas por módulo. accounts.0004 aplicada en desarrollo; FK de propietario, unicidad canónica y HMAC contextual verificados con 44 pruebas PostgreSQL y revisión independiente. Commit c5899d37c7886cd2786e66ce75cb76a32eaa05db. Solo esta porción de acceso está implementada; negocio futuro y acceso multicanal completo siguen pendientes. No cambia criterios, estimaciones, prioridad ni aprobaciones.

Trazabilidad: RF-ACC-006 / HU-ACC-010 / HT-ACC-001 / SB-S2-05 (S2), y HT-PRE-003 / SB-S1-03 para el diseño revisado durante S2. HT-ACC-002 corresponde a WebAuthn y no recibe implementación en esta porción. SB-S2-05 queda parcialmente implementada; no se marca completa ninguna de estas tareas.

El ER corrige N05–N18 como estructura futura, conserva reglas C01–C18 y no genera todavía tablas de asistencia, inventario, ventas o rendición. Datos de configuración y decisiones económicas pendientes conservan sus límites. Ediciones anteriores intactas; publicación académica y Git del vault pendientes.
