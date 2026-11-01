---
titulo: Historia técnica del modelo de datos
version: "2.2"
fecha: 2026-10-30
autor: Codex por instrucción del tesista
estado: consolidado-para-revision
validacion_organizacional: evidencia-directa-pendiente
publicacion: pendiente
---

# Historia técnica del modelo de datos

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación integral.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.2](../../arquitectura/diseno_base_datos_v2.2_2026-10-30.md). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

| ID | Reglas | Criterio vigente de esta revisión |
|---|---|---|
| HT-PRE-003 | C01-C18 / DB-01 a DB-20 | Preparar esquema por módulo con identidades, flujos de stock y dinero, cierre periódico, devoluciones, reparto, políticas e idempotencia; pruebas PostgreSQL y migraciones pendientes. |

HT-PRE-003 conserva sprint S1; revisión durante S2. Criterios: entidades con propietario; claves y cardinalidades; invariantes BD/servicio; casos concurrentes; permisos positivos/negativos; trazabilidad de saldos y pruebas físicas antes de cierre. [Base de historias técnicas](historias_tecnicas_v1.9_2026-10-28.md).


## Control de edición

2.1, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Avance técnico de esta edición 2.2

Refuerzo de normalización 2026-10-30: ER/base lógica v2.2 con relaciones y claves corregidas por módulo. accounts.0004 aplicada en desarrollo; FK de propietario, unicidad canónica y HMAC contextual verificados con 44 pruebas PostgreSQL y revisión independiente. Commit c5899d37c7886cd2786e66ce75cb76a32eaa05db. Solo esta porción de acceso está implementada; negocio futuro y acceso multicanal completo siguen pendientes. No cambia criterios, estimaciones, prioridad ni aprobaciones.

Trazabilidad: RF-ACC-006 / HU-ACC-010 / HT-ACC-001 / SB-S2-05 (S2), y HT-PRE-003 / SB-S1-03 para el diseño revisado durante S2. HT-ACC-002 corresponde a WebAuthn y no recibe implementación en esta porción. SB-S2-05 queda parcialmente implementada; no se marca completa ninguna de estas tareas.

El ER corrige N05–N18 como estructura futura, conserva reglas C01–C18 y no genera todavía tablas de asistencia, inventario, ventas o rendición. Datos de configuración y decisiones económicas pendientes conservan sus límites. Ediciones anteriores intactas; publicación académica y Git del vault pendientes.
