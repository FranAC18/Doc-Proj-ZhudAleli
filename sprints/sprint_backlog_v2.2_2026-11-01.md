---
titulo: Sprint backlog: alcance de datos consolidado
version: "2.2"
fecha: 2026-11-01
autor: Codex por instrucción del tesista
estado: preparado-para-revision-academica
aprobacion_regla_ferias: aprobada-por-tesista
validacion_organizacional: pendiente
publicacion: publicada-para-revision-documental
---

# Sprint backlog: alcance de datos consolidado

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación integral.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.2](../arquitectura/diseno_base_datos_v2.2_2026-10-30.md). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

| Tarea | Contenido consolidado |
|---|---|
| SB-S1-03 | Diseño consolidado v2.2; físico parcial en `accounts` y `planning`. No certifica implementación integral ni cierre de tarea. |
| SB-S5-01 | Catálogo, valores versionados, recetas conocidas y kits 50 L sin fórmula secreta; parámetros incompletos inactivos. |
| SB-S5-02 | Acopio, secado único y lotes; cantidades efectivas y conversiones compatibles. |
| SB-S5-03 | Transformación, kits y movimientos; linaje hasta salida, stock por titular/feria/condición. |
| SB-S5-04 | Custodia sin deuda; rendición periódica y anticipos; conciliación de capturas provisionales y stock. |
| SB-S5-05 | Ventas pagadas, resúmenes de feria, delegación y propiedad del excedente; permisos y prohibición de venta Superadministradora. |
| SB-S5-06 | Dinero, gastos, reembolsos, faltantes y reparto compartido exacto; ejecución separada de autorización y acuerdo. |

[Base de compromisos v1.6](sprint_backlog_v1.6_2026-10-28.md). SB-S2-02 conserva sus pendientes; SB-S2-05 registra el refuerzo parcial indicado abajo. Gestor: SB-S1-03 figura done en dashboard y en_curso en seguimiento; discrepancia histórica conservada, no cierre inferido.


## Seguimiento verificable del desarrollo — 2026-10-30

| Tarea | Estado comprobado | Evidencia y pendiente |
|---|---|---|
| SB-S1-03 / HT-PRE-003 | Parcial; no se cierra | El esquema de identidad y membresías de accounts fue implementado y probado; el modelo físico de los demás módulos y los casos restantes continúan pendientes. |
| SB-S2-02 | Abierta | El cambio de esquema no completa login, sesión, cierre, cambio de contraseña ni validación de experiencia. |
| SB-S2-03 | En curso, avance parcial | `accounts.0006`; alta/cierre de membresías para cuentas existentes y permisos backend para Presidenta, Tesorera y Secretaria cuando tengan designación vigente. 68 pruebas en la suite. Faltan crear cuentas, activar/desactivar acceso y asignar cargos; sin datos reales cargados. |
| SB-S2-04 | Candidata, sin verificación | Se conservan los criterios de inicio propio, móvil y regresión. |
| SB-S2-05 | Parcial | Se conserva el avance de contactos y desafíos; seguridad común no está completa. |
| SB-S2-06 a SB-S2-09 | Pendientes | Correo, passkeys, WhatsApp y recuperación esperan sus dependencias y verificaciones reales. |
| SB-S3-01 | En curso parcial; inicio anticipado en S2 por instrucción del tesista | `planning.0001`; crear/editar actividad básica con responsable y participantes, consulta con alcance por cuenta y permisos backend para los tres cargos autorizados. 68 pruebas totales y revisión UI sin overflow en 360/375/768/1280/1440 px. Mantiene Sprint 3 y sus fechas; faltan instancias, detalle de cancelación y designaciones reales. |

S2 permanece abierto; este seguimiento no cierra tareas por la existencia de un modelo ni por el cambio de sprint. Las demás tareas conservan el estado de su fuente.

## Ajuste de alcance aprobado por el tesista para S5 — validación pendiente

- SB-S5-02: reflejar que el acopio individual se habilita junto con la venta individual; en modo ordinario se utiliza inventario de lotes de fábrica.
- SB-S5-05: conservar las reglas de cobro y trazabilidad; la Superadministradora controla la opción, pero no vende personalmente.
- SB-S5-06: calcular la ganancia conjunta restando del total recaudado el valor base correspondiente a las cantidades vendidas y los gastos; dividir únicamente esa ganancia en partes iguales entre las encargadas.

La aceptación del tesista no cambia fechas, prioridad, estimaciones, responsables ni estado. S5 es futuro y no recibe un compromiso nuevo. La validación organizacional y los detalles abiertos deben resolverse antes de planificar la implementación.

2.1 → 2.2, 2026-11-01: se anotan criterios de feria aprobados por el tesista para SB-S5-02/05/06; validación organizacional pendiente, sin compromisos ni cambios de estado, fecha o prioridad.

## Control de edición

2.0 → 2.1, 2026-10-31: se actualiza el avance parcial de SB-S2-03 y se registra el inicio anticipado de SB-S3-01 durante S2 sin cambiar sprint asignado, criterios, estimaciones o responsabilidades.

1.8, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.

## Avance técnico del corte anterior 1.9 — referencia histórica

Refuerzo de normalización 2026-10-30: ER/base lógica v2.2 con relaciones y claves corregidas por módulo. accounts.0004 aplicada en desarrollo; FK de propietario, unicidad canónica y HMAC contextual verificados con 44 pruebas PostgreSQL y revisión independiente. Commit c5899d37c7886cd2786e66ce75cb76a32eaa05db. Solo esta porción de acceso está implementada; negocio futuro y acceso multicanal completo siguen pendientes. No cambia criterios, estimaciones, prioridad ni aprobaciones.

Trazabilidad: RF-ACC-006 / HU-ACC-010 / HT-ACC-001 / SB-S2-05 (S2), y HT-PRE-003 / SB-S1-03 para el diseño revisado durante S2. HT-ACC-002 corresponde a WebAuthn y no recibe implementación en esta porción. SB-S2-05 queda parcialmente implementada; no se marca completa ninguna de estas tareas.

El ER corrige N05–N18 como estructura futura, conserva reglas C01–C18 y no genera todavía tablas de asistencia, inventario, ventas o rendición. Datos de configuración y decisiones económicas pendientes conservan sus límites. Ediciones anteriores intactas; publicación académica y Git del vault pendientes.
