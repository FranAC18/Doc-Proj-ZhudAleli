---
title: Identidad organizacional y roles para el ER
date: 2026-10-30
status: documented
task_id: SB-S1-03
technical_story: HT-PRE-003
phase: pre_commit
commit: pending
---

# Aclaración incorporada

El tesista confirmó que hay seis personas en la asociación y todas tienen cuenta. Los cuatro roles de negocio son General, Presidenta, Tesorera y Secretaria, y pueden combinarse en una cuenta. La Superadmin es una cuenta externa al padrón. Esto implica al menos siete cuentas actuales: seis de socias y una externa de Superadmin. El número actual no es CHECK ni máximo del esquema. La concesión de Superadministración conserva su posibilidad de más de una persona autorizada, conforme la decisión anterior; una única titular describe la situación reportada hoy.

El ER incorpora `PersonaOrganizacional` 1:1 con cuenta para socias; cada usuario externo (incluida Superadmin) puede no tener persona asociada. Perfil General y cargos se guardan como asignaciones combinables con vigencia. La persona es la referencia para membresía, encargos, stock individual, ventas y cuotas; la cuenta sigue siendo actor de acceso/auditoría.

# Contraste con PostgreSQL de desarrollo

La base `zhud_aleli_dev` tiene 13 tablas y todas las migraciones registradas aplicadas; `makemigrations --check --dry-run` no detecta divergencia modelo/migración. Se contó una fila en `accounts_user` y cero flags técnicos `is_superuser`/`is_staff`. La base no contiene el padrón de al menos siete cuentas reportado; las tablas de cargos/membresía aún no existen. No se consultaron nombres ni valores personales. No se puede identificar qué representa la cuenta actual porque el esquema de roles aún no está implementado.

Archivos vigentes: [ER v2.1](../../../documentacion/arquitectura/modelo_er_integral_v2.1_2026-10-30.md) y [base de diseño v2.1](../../../documentacion/arquitectura/diseno_base_datos_v2.1_2026-10-30.md). La v2.0 queda como antecedente. Evidencia: [introspección](../../evidence/architecture/2026-10-30-er-integral/postgres-introspeccion.json) y [verificación final](../../evidence/architecture/2026-10-30-er-integral/verificacion.json).

Se mantiene separada la Superadmin del booleano Django `is_superuser`. Ese flag tiene efecto técnico amplio y no se debe utilizar como cargo organizacional. No se modificó la aplicación.
