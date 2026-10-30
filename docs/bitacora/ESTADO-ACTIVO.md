---
title: Estado activo de continuidad
type: state
status: in-progress
updated: 2026-10-30
task_id: SB-S2-02
active_task: SB-S2-02
phase: implementation
branch: docs/requisitos-y-organizacion-del-vault
head: dbd0e2207972715ebaf2b7ef2b67f6af63feb6e9
last_commit: dbd0e2207972715ebaf2b7ef2b67f6af63feb6e9
commit: dbd0e2207972715ebaf2b7ef2b67f6af63feb6e9
current_agent: codex
current_role: coordinator
repository: ZhudAleli
constitution_current: 2.0.0
app_root: app/
app_remote: https://github.com/FranAC18/App-zhudaleli.git
app_branch: feature/RF-ACC-001-base-proyecto
app_head: d208fba3e347bf2fffae1f91ff178a1d33414249
app_head_observed: 2026-10-29
git_authorization_checkpoint: checkpoints/2026-10-29-autorizacion-git-app.md
scope_file: alcance-activo.yaml
continuity_checkpoint: checkpoints/2026-10-28-app-contactos-notificaciones-post-commit.md
history_checkpoint: checkpoints/2026-10-29-contexto-previo/ESTADO-ACTIVO.md
context_checkpoint: checkpoints/2026-10-29-ahorro-contexto.md
next_action: 'Continuar SPEC-003 por incrementos: SB-S2-05 seguridad común, SB-S2-06 correo, SB-S2-07 passkeys, SB-S2-08 WhatsApp con mock/adaptador y SB-S2-09 recuperación/regresión. Conservar avances y pendientes de SB-S2-02. Verificar el requisito y sprint vigentes antes de implementar.'
blockers: []
---

# Estado activo de continuidad

## Lectura y escritura

Este archivo resume el trabajo vigente. Antes de escribir, comprobar Git y las rutas
permitidas/prohibidas en [alcance-activo.yaml](alcance-activo.yaml). Esa lista conserva
el alcance anterior; la tarea elegida y la autorización del tesista delimitan cada uso.
Abrir checkpoints o fuentes solo para la tarea o duda concreta. No añadir aquí el
relato de cada ajuste: enlazar su evidencia y actualizar el resultado vigente.

## Producto y sprint

- S2 sigue activo; SB-S2-02 permanece abierto. S1 concluyó por calendario el 2026-10-27,
  con trabajo parcialmente completo; S0 está completado según el registro anterior.
- S2: fechas comunicadas 2026-10-14 a 2026-10-29; extensión al 2026-11-08 propuesta.
  Capacidad comunicada: 16–25 horas semanales; objetivo 2026-12-23. Consultar la
  [hoja de ruta](../sprints/PLAN-HASTA-2026-12-23.md) antes de planificar.
- Último registro de la app (2026-10-28): commit e3cc071 en la rama indicada; 44 archivos
  publicados y 31 pruebas PostgreSQL correctas. Detalle, comandos y límites en el
  [checkpoint post_commit](checkpoints/2026-10-28-app-contactos-notificaciones-post-commit.md).
  No acredita integración en main, PR, tag ni terminación de SB-S2-02.
- SPEC-003: alcance y plan aceptados por el tesista; existe base de contactos, pero correo,
  passkeys, WhatsApp y recuperación completos siguen pendientes. Entrega SMTP/WhatsApp,
  dominio y dispositivos de passkeys por comprobar; no se autoriza gasto o publicación.
- RF-ACC-005/SPEC-002 conservan estado propuesto; la validación presidencial del rol
  está reportada por el tesista, con evidencia pendiente. No aprobar detalles por inferencia.
- Para RF/HU/HT, orden de tareas y spec pertinentes, usar el
  [índice de funcionalidades](../context/feature-index.md). Para frontend, aplicar las
  [ocho reglas de interfaz](../ui/REGLAS-DISENO-INTERFACES.md); identidad visual y
  validación con usuarias pendientes. Convención de código en la skill obligatoria.

## Continuidad del vault

Consolidación del 2026-10-30: [base lógica v2.1](../../documentacion/arquitectura/diseno_base_datos_v2.1_2026-10-30.md) y [ER integral v2.1](../../documentacion/arquitectura/modelo_er_integral_v2.1_2026-10-30.md). Mantiene reglas C01–C18 y añade seis socias con cuenta, cuatro roles combinables y una cuenta Superadmin externa. PostgreSQL de desarrollo tiene 13 tablas, una cuenta y aún no contiene el padrón/modelos de negocio; no es límite del esquema. Se conserva v2.0 como historial.

ER integral 2026-10-30: revisión vigente [v2.1](../../documentacion/arquitectura/modelo_er_integral_v2.1_2026-10-30.md) y [base lógica v2.1](../../documentacion/arquitectura/diseno_base_datos_v2.1_2026-10-30.md). Incorpora seis socias con cuenta, cuatro roles combinables y cuenta Superadmin externa; el seis no limita el esquema. PostgreSQL de desarrollo tiene 13 tablas/18 migraciones y un solo usuario, sin padrón de negocio. [Checkpoint de roles](checkpoints/2026-10-30-identidad-y-roles-er.md), [evidencia](../../docs/evidence/architecture/2026-10-30-er-integral/verificacion.json).

RF/HU/HT, pila, backlog y gestor local sincronizados conservando estados. [Checkpoint de consolidación](checkpoints/2026-10-30-consolidacion-datos.md). Próximo paso de datos: ER físico, restricciones y transacciones por módulo. Configuración concreta, responsabilidad por daños no fabriles y evidencia organizacional conservan límites explícitos; no se aplicaron migraciones ni se cerró SB-S1-03. Discrepancia histórica de su estado entre vistas del gestor documentada. La continuidad de SPEC-003/SB-S2-02 se conserva.

El vault conserva cambios locales previos sin commit; comprobar `git status` al retomar.
Desde el 2026-10-29, AGENTS.md autoriza commit y push tras cada porción de programación
de la app verificada y revisada, sin nueva confirmación. [Alcance y evidencia](checkpoints/2026-10-29-autorizacion-git-app.md).
HEAD de app actualizado por observación; su checkout tiene cambios locales previos no
verificados por esta tarea. El checkpoint del 2026-10-28 conserva su corte histórico.
El 2026-10-29 se ajusta únicamente la recuperación de contexto y el registro de memoria
por solicitud del tesista. No cambia alcance, criterios, prioridad ni terminación de
RF/HU/HT o tareas del sprint. Resultado y verificaciones en el
[checkpoint de contexto](checkpoints/2026-10-29-ahorro-contexto.md).
El estado anterior íntegro se conserva en
[historial previo](checkpoints/2026-10-29-contexto-previo/ESTADO-ACTIVO.md); sus enlaces
relativos corresponden a su ubicación original. No se carga de forma habitual.
