---
title: Acta de Levantamiento de requisitos 1.0
type: meeting
status: recorded
id: ACT-REQ-001
version: 1.0
date: 2026-07-25
baseline_validation_date: 2026-07-22
phase: Fase I
sprint: s1
module: acceso
approval_status: confirmed
approval_scope: tesista-confirmation-and-rf-acc-001-clarifications
source_type: human-approval
source_medium: instrucción registrada en la sesión de trabajo del repositorio
signature_status: not-attached
participants:
  - Tesista
previously_declared_participants:
  - Organización
  - Presidenta
related:
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[2026-07-22-validacion-cat-req-001-v1]]"
  - "[[../../bitacora/checkpoints/2026-07-25-versionado-fase-i-y-factibilidad-acceso]]"
  - "[[../../00-inicio/01-decisiones-pendientes]]"
  - "[[../../traceability/MATRIZ-TRAZABILIDAD]]"
  - "[[../../sprints/ROADMAP-ANTEPROYECTO]]"
tags:
  - proyecto/tesis
  - tipo/evidencia
  - sprint/s1
  - modulo/acceso
---

# ACT-REQ-001 — Acta de Levantamiento de requisitos 1.0

## Identificación

- Proyecto: aplicación web para la gestión organizacional del Comité de Mujeres Indígenas
  “Tránsito Amaguaña” de Zhud.
- Línea base relacionada: [[../../requirements/CAT-REQ-001|CAT-REQ-001 v1.0]].
- Fecha de validación de la línea base: 2026-07-22.
- Fecha de formalización de esta acta y aclaraciones de acceso: 2026-07-25.
- Participante de la aprobación actual: tesista.
- Participantes declarados en la validación previa: organización y presidenta.
- Medio actual: instrucción humana registrada en la sesión de trabajo del repositorio.
- Firma manuscrita o electrónica adjunta: no.

Esta acta consolida decisiones registradas en el repositorio y la aprobación actual del
tesista. No atribuye una firma nueva a la organización ni sustituye un acta externa firmada
si esta existe.

## Objetivo

Formalizar el resultado de **Levantamiento de requisitos 1.0**, registrar la aprobación del
plan de factibilidad del checkpoint del 2026-07-25 y delimitar la primera spec de Sprint 1.

## Antecedentes validados

CAT-REQ-001 v1.0 conserva:

| Estado | Cantidad |
|---|---:|
| `confirmed` | 57 |
| `proposed` | 2 |
| `superseded` | 12 |

`RF-COS-001` y `RNF-OPS-001` permanecen `proposed`. P-01 a P-12 conservan el efecto
delimitado en la línea base y no se consideran resueltas por esta acta.

## Decisiones confirmadas en esta sesión

1. Se aprueba el plan documentado en
   [[../../bitacora/checkpoints/2026-07-25-versionado-fase-i-y-factibilidad-acceso|el
   checkpoint de factibilidad]].
2. Se acepta la **opción A**: preparar primero una spec limitada a `RF-ACC-001` y los
   requisitos no funcionales aplicables.
3. La usuaria utilizará un **nombre de usuario (`username`)** para iniciar sesión.
4. La primera cuenta se almacenará en la base de datos y se entregará cuando el sistema esté
   funcional.
5. El cambio de contraseña forma parte de la primera porción.
6. Después de iniciar sesión se mostrará un dashboard de bienvenida con las opciones
   disponibles del sistema.
7. Esta porción no declara completado el Sprint 1.

## Alcance aprobado para la primera spec

### Incluido

- Inicio de sesión con `username` y contraseña.
- Cierre de sesión.
- Rechazo no revelador de credenciales inválidas.
- Rechazo de cuentas inactivas.
- Protección de una vista privada frente a acceso anónimo.
- Cambio de contraseña para una usuaria autenticada.
- Dashboard privado de bienvenida.
- `RNF-UX-001`, `RNF-UX-002`, `RNF-UX-003`, `RNF-CON-001`, `RNF-SEC-001` y
  `RNF-PRV-001` en lo que corresponda al recorrido.
- Pruebas positivas y negativas de autenticación y sesión.

### Excluido

- Administración de membresías de `RF-ACC-002`.
- Matriz de cargos y operaciones de `RF-ACC-003`.
- Actividades, pendientes y encargos de `RF-ACC-004`.
- Recuperación de contraseña mediante correo, teléfono u otro canal externo.
- Contenido público final y operaciones de negocio.
- Resolución de P-01.

## Recomendación técnica propuesta

Estas recomendaciones orientan la futura spec y su plan; no sustituyen su aprobación:

1. Crear la primera cuenta mediante un comando de administración de Django o un procedimiento
   equivalente que use el gestor de contraseñas del framework. No insertar una contraseña en
   texto plano mediante SQL.
2. Guardar únicamente el hash de contraseña y entregar la credencial temporal por un canal
   separado y seguro.
3. Solicitar cambio de contraseña en el primer acceso o antes de entregar la cuenta para uso
   real.
4. Mostrar en el dashboard solo opciones ya disponibles. En la primera porción: bienvenida,
   “Cambiar contraseña” y “Cerrar sesión”. No simular actividades o encargos todavía.
5. No incluir “recordarme” en la primera versión. El tiempo exacto de cierre por inactividad
   debe validarse considerando equipos compartidos y conectividad.
6. Invalidar las sesiones apropiadas después del cambio de contraseña y asegurar que cerrar
   sesión impida reutilizar una URL privada.

## Pendientes para la spec y el plan

- Identificar qué persona o cargo recibirá la primera cuenta; P-01 sigue abierta.
- Definir el canal seguro de entrega de la credencial temporal.
- Definir si el cambio inicial será obligatorio técnicamente y cómo se informará.
- Validar el tiempo de inactividad de sesión para equipos compartidos.
- Precisar el contenido textual del dashboard de bienvenida.
- Diseñar usuario personalizado antes de la primera migración.
- Aprobar PostgreSQL, configuración por entorno, CI, pruebas y UX en el plan.

## Criterio de avance

La aprobación de esta acta permite crear la spec en borrador para `RF-ACC-001`. No autoriza
todavía código Django. La implementación requiere:

1. spec redactada con estas decisiones;
2. revisión y confirmación humana de la spec;
3. plan aprobado;
4. tareas verificables;
5. análisis de coherencia;
6. rama o worktree propio para la porción vertical.

## Registro de aprobación

| Fecha | Participante | Decisión | Medio | Resultado |
|---|---|---|---|---|
| 2026-07-25 | Tesista | Aprueba el plan del checkpoint, acepta opción A y responde aclaraciones de acceso | Sesión de trabajo del repositorio | Decisiones registradas; primera spec autorizada para preparación |

## Limitación de evidencia

Este archivo es una transcripción estructurada de la aprobación recibida. Si existe un acta
externa firmada de **Levantamiento de requisitos 1.0**, debe conservarse o enlazarse de forma
anonimizada sin reescribir esta evidencia.
