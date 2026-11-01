---
titulo: Historia técnica del modelo de datos
version: "2.5"
fecha: 2026-11-01
autor: Codex por instrucción del tesista
estado: preparado-para-revision-academica
aprobacion_regla_ferias: aprobada-por-tesista
validacion_organizacional: pendiente
publicacion: publicada-para-revision-documental
---

# Historia técnica del modelo de datos

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación integral.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.2](../../arquitectura/diseno_base_datos_v2.2_2026-10-30.md). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

| ID | Reglas | Criterio vigente de esta revisión |
|---|---|---|
| HT-PRE-003 | C01-C18 / DB-01 a DB-20 | Preparar esquema por módulo con identidades, flujos de stock y dinero, cierre periódico, devoluciones, reparto, políticas e idempotencia; pruebas PostgreSQL y migraciones pendientes. |

HT-PRE-003 conserva sprint S1; revisión durante S2. Criterios: entidades con propietario; claves y cardinalidades; invariantes BD/servicio; casos concurrentes; permisos positivos/negativos; trazabilidad de saldos y pruebas físicas antes de cierre. [Base de historias técnicas](historias_tecnicas_v1.9_2026-10-28.md).


## Regla de feria aprobada por el tesista — diseño técnico pendiente

HT-PRE-003 deberá considerar la dirección de negocio aprobada por el tesista: inventario de lotes de fábrica en modo ordinario; una opción auditable de la Superadministradora que habilite o deshabilite juntas el acopio y la venta individual; y reparto igualitario, entre encargadas, únicamente de la ganancia conjunta calculada como total recaudado menos el valor base correspondiente a las cantidades vendidas y los gastos de feria. Debe conservarse origen, titular, configuración y valores históricos por operación. El diseño no debe alterar ferias ya iniciadas o cerradas.

La aprobación del tesista no acredita validación organizacional. La tabla de historias técnicas mantiene su estado actual; esta ampliación no aprueba diseño físico, migraciones ni implementación. El alcance global o por feria, la cantidad de lotes, el tratamiento de saldos no positivos, la asignación de centavos y el destino del precio base descontado requieren definición antes de diseñar pruebas y migraciones.

2.4 → 2.5, 2026-11-01: se registra el alcance de feria aprobado por el tesista, pendiente de validación organizacional y diseño técnico; sin diseño físico ni implementación aprobados.

## Control de edición

2.3 → 2.4, 2026-10-31: se registra el avance físico de membresías y planificación, sus migraciones PostgreSQL y las verificaciones reales; las demás entidades ER conservan su estado futuro.

2.1, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Avance técnico de esta edición 2.3

HT-PRE-003 continúa parcial. El commit [c9f2d6a3e0f0fa474485546075eda55e8d729592](https://github.com/FranAC18/App-zhudaleli/commit/c9f2d6a3e0f0fa474485546075eda55e8d729592) agrega `CargoOrganizacional`, `DesignacionCargo`, las operaciones de membresía en `accounts` y las tablas `planning_actividad` y `planning_participanteactividad`. Se mantienen índices, claves foráneas, unicidad de membresía abierta y de participante por actividad, auditoría de actor y límites de escritura propiedad de cada módulo. Los casos coordinados usan transacciones.

Verificación real en `zhud_aleli_dev`: 19 tablas base, 22 migraciones aplicadas, tres cargos de catálogo y cero designaciones activas. La suite completa pasó 68 pruebas PostgreSQL; Ruff, `manage.py check`, `makemigrations --check --dry-run` y diff-check pasaron. La revisión UI midió cinco anchos y no encontró desbordamiento horizontal; teclado y contraste se comprobaron en los formularios intervenidos.

El mapa ER integral v2.2 sigue siendo mayor al esquema físico actual: asistencia, trazabilidad, inventario, comercio, cierres y reportes no se han migrado ni implementado. La asignación de cargos carece de flujo UI y de designaciones reales; creación/activación de cuentas y parte de RF-PLA-001 también siguen pendientes. No se cierra SB-S1-03 ni ninguna historia de usuaria. La continuidad mantiene los propietarios `accounts` y `planning` dentro del monolito modular.
