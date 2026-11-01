---
titulo: Historia técnica del modelo de datos
version: "2.3"
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

2.2 → 2.3, 2026-10-30: se registra la migración de identidad en accounts, sus pruebas reales y los pendientes por módulo.

2.1, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Avance técnico de esta edición 2.3

HT-PRE-003 avanza parcialmente en Sprint 2: accounts.0005 materializa la identidad organizacional y el historial básico de membresías con restricciones en PostgreSQL. El cambio está publicado en feature/RF-ACC-002-persona-membresia como 65839bd3067700bcd311ed5785a5d0f894bceaec.

Verificación real: cinco pruebas nuevas y 49 de la suite completa en PostgreSQL; Django check, estado de migraciones, Ruff y diff-check correctos. La migración se aplicó en zhud_aleli_dev. La evidencia conserva comandos, alcance y pendientes en el checkpoint post_commit de identidad de cuentas.

La historia sigue parcial: falta administración, control de permisos validado por operación y el diseño físico/implementación de planificación, asistencia, producción, inventario y comercio. No se cierra SB-S1-03 ni ninguna historia de usuaria. La continuidad de módulos seguirá por recorridos verificables y dentro de las apps propietarias.
