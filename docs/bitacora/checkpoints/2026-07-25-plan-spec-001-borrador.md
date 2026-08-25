---
title: Plan técnico borrador de SPEC-001
type: checkpoint
status: partially-complete
date: 2026-07-25
sprint: s1
module: acceso
related:
  - "[[../../../specs/001-acceso-usuarias-internas/spec]]"
  - "[[../../../specs/001-acceso-usuarias-internas/plan]]"
  - "[[../../../specs/001-acceso-usuarias-internas/research]]"
  - "[[../../../specs/001-acceso-usuarias-internas/data-model]]"
  - "[[../../../specs/001-acceso-usuarias-internas/contracts/http]]"
  - "[[../../../specs/001-acceso-usuarias-internas/quickstart]]"
  - "[[../../decisions/ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[../../traceability/MATRIZ-TRAZABILIDAD]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - sprint/s1
  - modulo/acceso
---

# Plan técnico borrador de SPEC-001

## Objetivo

Preparar la puerta técnica de [[../../../specs/001-acceso-usuarias-internas/spec|SPEC-001]]
antes de dividir la funcionalidad en tareas o crear la aplicación Django.

## Trabajo realizado

- Se ejecutó el flujo `speckit-plan` para la funcionalidad activa.
- Se creó el [[../../../specs/001-acceso-usuarias-internas/plan|plan técnico]] con contexto,
  comprobación constitucional, datos, autorización, interfaz, estructura, pruebas, evidencia,
  riesgos y reversión.
- Se documentaron las decisiones y alternativas en
  [[../../../specs/001-acceso-usuarias-internas/research|research.md]].
- Se definieron el
  [[../../../specs/001-acceso-usuarias-internas/data-model|modelo de datos]], el
  [[../../../specs/001-acceso-usuarias-internas/contracts/http|contrato HTTP]] y la
  [[../../../specs/001-acceso-usuarias-internas/quickstart|guía de verificación prevista]].
- Tres agentes especializados hicieron revisiones independientes de arquitectura y
  seguridad, datos y migraciones, y experiencia y pruebas. Trabajaron en solo lectura; el
  agente raíz resolvió las diferencias y conservó la propiedad de los archivos.
- La estructura respeta
  [[../../decisions/ADR-0003-estructura-raiz-aplicacion-django|ADR-0003]]: aplicación en la
  raíz y únicamente `config` y `accounts` en la primera porción.

## Recomendación técnica consolidada

- Python 3.12, Django 5.2 LTS, PostgreSQL 14 o posterior y Psycopg 3.
- `uv`, `pyproject.toml` y `uv.lock` para dependencias reproducibles.
- `accounts.User(AbstractUser)` desde `0001_initial`, con una sola bandera de cambio
  obligatorio.
- Nombre de usuario canónico y restricción funcional de unicidad en PostgreSQL.
- Sesiones nativas de base de datos con vencimiento deslizante de 30 minutos.
- Vistas y formularios nativos de Django, salida solo por `POST`, CSRF y respuestas privadas
  sin caché.
- Guarda backend explícita en toda vista privada para impedir que una credencial temporal
  llegue al dashboard.
- Primera cuenta regular creada por comando interactivo y entregada presencialmente; nunca
  se registra la credencial.
- Interfaz de una columna, Bootstrap local, sin opciones ficticias ni identidad visual no
  validada.

## Diferencias resueltas

1. Se eligió una guarda reutilizable sobre las vistas privadas en vez de middleware global:
   hoy existe un solo dashboard y la alternativa es más simple y verificable.
2. Cerrar el navegador no se trata como cierre de sesión: el requisito confirmado es
   inactividad de 30 minutos y la salida explícita sigue siendo necesaria en equipos
   compartidos.
3. El cambio de contraseña redirige al dashboard con confirmación; no se crea una página de
   confirmación adicional.
4. La limitación de intentos no se inventa dentro de SPEC-001. Se conserva como riesgo que
   debe resolverse antes de una exposición pública si el despliegue lo exige.
5. La revisión independiente detectó dos carreras. El plan ahora serializa la primera cuenta
   con un bloqueo asesor transaccional PostgreSQL y cada cambio de contraseña con bloqueo de
   fila antes de validar.
6. La matriz global ahora contiene una fila individual para cada RNF aplicable. La spec
   confirmada no se reescribe durante el borrador; su referencia “Pendiente de plan” se
   entiende como “plan aprobado pendiente” y se actualizará al registrar la aprobación.

## Estado del entorno

- Python 3.12.2: disponible.
- `uv` 0.10.9: disponible.
- `psql` y `pg_isready`: no detectados en `PATH`.
- Aplicación Django y base de datos: todavía no creadas, de acuerdo con la puerta vigente.

PostgreSQL puede estar instalado fuera de `PATH`; debe localizarse o instalarse antes de
validar migraciones y pruebas. SQLite no sustituirá esa verificación.

## Estado de la puerta

La especificación continúa `confirmed`, pero el plan está `draft`. La comprobación de la
constitución pasa en diseño y no quedan aclaraciones materiales. Después de corregir los
hallazgos de concurrencia, trazabilidad y verificación de producción, la reauditoría
independiente terminó `PASS` sin hallazgos P0–P2. La puerta está `partially-complete` porque
falta la aprobación humana del plan.

## Próximo paso permitido

1. El tesista revisa y aprueba o solicita ajustes al plan.
2. Tras la aprobación, ejecutar `speckit-tasks`.
3. Ejecutar `speckit-analyze` y corregir contradicciones.
4. Resolver la disponibilidad de PostgreSQL.
5. Solicitar autorización de la primera porción de implementación.

No se realizó implementación, commit, push ni merge en esta etapa.
