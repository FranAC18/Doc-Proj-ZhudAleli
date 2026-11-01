---
titulo: Sprint backlog: alcance de datos consolidado
version: "1.9"
fecha: 2026-10-30
autor: Codex por instrucción del tesista
estado: consolidado-para-revision
validacion_organizacional: evidencia-directa-pendiente
publicacion: pendiente
---

# Sprint backlog: alcance de datos consolidado

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación integral.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.2](../arquitectura/diseno_base_datos_v2.2_2026-10-30.md). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

| Tarea | Contenido consolidado |
|---|---|
| SB-S1-03 | Diseño consolidado v2.0 y 20 casos definidos. Trabajo documental listo para diseño físico; no certifica implementación ni cierre de tarea. |
| SB-S5-01 | Catálogo, valores versionados, recetas conocidas y kits 50 L sin fórmula secreta; parámetros incompletos inactivos. |
| SB-S5-02 | Acopio, secado único y lotes; cantidades efectivas y conversiones compatibles. |
| SB-S5-03 | Transformación, kits y movimientos; linaje hasta salida, stock por titular/feria/condición. |
| SB-S5-04 | Custodia sin deuda; rendición periódica y anticipos; conciliación de capturas provisionales y stock. |
| SB-S5-05 | Ventas pagadas, resúmenes de feria, delegación y propiedad del excedente; permisos y prohibición de venta Superadministradora. |
| SB-S5-06 | Dinero, gastos, reembolsos, faltantes y reparto compartido exacto; ejecución separada de autorización y acuerdo. |

[Base de compromisos v1.6](sprint_backlog_v1.6_2026-10-28.md). SB-S2-02 conserva sus pendientes; SB-S2-05 registra el refuerzo parcial indicado abajo. Gestor: SB-S1-03 figura done en dashboard y en_curso en seguimiento; discrepancia histórica conservada, no cierre inferido.


## Control de edición

1.8, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Avance técnico de esta edición 1.9

Refuerzo de normalización 2026-10-30: ER/base lógica v2.2 con relaciones y claves corregidas por módulo. accounts.0004 aplicada en desarrollo; FK de propietario, unicidad canónica y HMAC contextual verificados con 44 pruebas PostgreSQL y revisión independiente. Commit c5899d37c7886cd2786e66ce75cb76a32eaa05db. Solo esta porción de acceso está implementada; negocio futuro y acceso multicanal completo siguen pendientes. No cambia criterios, estimaciones, prioridad ni aprobaciones.

Trazabilidad: RF-ACC-006 / HU-ACC-010 / HT-ACC-001 / SB-S2-05 (S2), y HT-PRE-003 / SB-S1-03 para el diseño revisado durante S2. HT-ACC-002 corresponde a WebAuthn y no recibe implementación en esta porción. SB-S2-05 queda parcialmente implementada; no se marca completa ninguna de estas tareas.

El ER corrige N05–N18 como estructura futura, conserva reglas C01–C18 y no genera todavía tablas de asistencia, inventario, ventas o rendición. Datos de configuración y decisiones económicas pendientes conservan sus límites. Ediciones anteriores intactas; publicación académica y Git del vault pendientes.
