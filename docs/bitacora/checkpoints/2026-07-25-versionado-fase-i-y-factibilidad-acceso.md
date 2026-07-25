---
title: Versionado de Fase I y factibilidad de la primera spec de acceso
type: checkpoint
status: completed
date: 2026-07-25
sprint: fase-i
module: acceso
recommendation_status: proposed
git_scope: local-commit-only
related:
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[2026-07-22-validacion-cat-req-001-v1]]"
  - "[[../../evidence/fase-i/2026-07-22-validacion-cat-req-001-v1]]"
  - "[[../../00-inicio/01-decisiones-pendientes]]"
  - "[[../../traceability/MATRIZ-TRAZABILIDAD]]"
  - "[[../../architecture/PLAN-DESDE-CERO]]"
  - "[[../../00-inicio/00-dashboard]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/acceso
  - estado/completado
---

# Versionado de Fase I y factibilidad de la primera spec de acceso

## Objetivo

Revisar la línea base documental de Fase I antes de registrarla en Git y comparar el inicio
por una porción mínima de acceso frente a intentar todo el Sprint 1 en una sola spec.

## Autorización y alcance

- El tesista autorizó el uso de Git y agentes especializados en esta sesión.
- El alcance de Git se limita a revisión, staging y commit local.
- No se autorizó `push`, `merge`, `rebase` ni reescritura de historia.
- El agente raíz fue el único escritor; requisitos, arquitectura y revisión trabajaron en
  lectura.
- El cambio local de zoom en `.obsidian/graph.json` se conservó, pero quedó fuera del commit
  por ser una preferencia visual ajena a Fase I.

## Estado verificado

- Sprint 0 está cerrado.
- CAT-REQ-001 v1.0 conserva 57 requisitos `confirmed`, 2 `proposed` y 12 `superseded`.
- No existe todavía una funcionalidad en `specs/` ni código Django de producción.
- La arquitectura y el sistema visual siguen como propuestas que cada plan debe concretar.
- P-01 a P-12 permanecen abiertas con el efecto delimitado en CAT-REQ-001.
- El acta externa de **Levantamiento de requisitos 1.0** no fue adjuntada; la evidencia
  registrada declara esta limitación.

## Opciones comparadas

| Opción | Alcance | Factibilidad actual | Riesgo |
|---|---|---|---|
| A | `RF-ACC-001` y RNF aplicables | Alta después de spec, aclaración, confirmación, plan y tareas | Medio-bajo |
| B | `RF-ACC-001` a `RF-ACC-004` en una sola spec | Baja hoy; media tras resolver dependencias | Alto |

## Recomendación propuesta

Preparar primero una spec limitada a `RF-ACC-001`, sin declarar completado el Sprint 1.
Esta recomendación no aprueba la spec ni autoriza implementación.

El corte mínimo debería cubrir:

- inicio y cierre de sesión para una cuenta interna activa;
- rechazo no revelador de credenciales inválidas y cuentas inactivas;
- denegación de una vista privada a personas anónimas;
- invalidación de la sesión después de cerrar;
- `RNF-UX-001`, `RNF-UX-002`, `RNF-UX-003`, `RNF-CON-001`, `RNF-SEC-001` y
  `RNF-PRV-001` cuando correspondan al recorrido;
- pruebas backend positivas y negativas, revisión móvil desde 360 px, teclado, foco y
  mensajes recuperables.

Quedan expresamente fuera de este corte:

- administración de membresías de `RF-ACC-002`;
- matriz de cargos y operaciones de `RF-ACC-003`;
- inicio personalizado con actividades y encargos de `RF-ACC-004`;
- recuperación mediante un canal externo;
- operaciones de negocio y contenido público final.

## Motivo de la recomendación

P-01 todavía no define qué cargo puede administrar cuentas u operaciones sensibles, por lo
que incluir `RF-ACC-002` o `RF-ACC-003` obligaría a inventar permisos. `RF-ACC-004` necesita
actividades y encargos cuya propiedad corresponde a planificación en Sprint 2. Intentar los
cuatro requisitos juntos mezclaría dominios y ampliaría las pruebas antes de estabilizar la
base Django y PostgreSQL.

La opción A sigue teniendo esfuerzo medio: su plan deberá incluir el proyecto Django, el
usuario personalizado antes de la primera migración, PostgreSQL, configuración por entorno,
CI, una plantilla Bootstrap accesible y pruebas de sesión y autorización.

## Preguntas para la futura aclaración

1. ¿Qué identificador utilizará la usuaria para iniciar sesión?
2. ¿Cómo se creará y entregará la primera cuenta activa?
3. ¿El cambio de contraseña forma parte de esta primera porción?
4. ¿Cuál es el destino privado mínimo después del inicio de sesión?
5. ¿Qué comportamiento de sesión debe validarse por el uso de equipos compartidos?

## Correcciones integradas antes del versionado

- Se ordenó la historia del catálogo como R1 → R2 → R3 → CAT-REQ-001 v1.0.
- R1 y R2 quedaron `superseded`, sin aparecer como propuestas activas.
- La matriz dejó de presentar catálogos como si fueran specs existentes.
- El flujo volvió a exigir confirmación humana de la spec después de la aclaración.
- Se aclaró que una spec `confirmed` todavía necesita plan, tareas y puertas superadas.
- El checkpoint inicial de Fase I enlaza ahora su resultado posterior.
- El plan propuesto distingue el shell público mínimo de S1 y el contenido público final de
  S5.

## Verificaciones

- Conteo canónico: 57 `confirmed`, 2 `proposed` y 12 `superseded`.
- Suite del laboratorio aislado: 10 pruebas aprobadas.
- Wikilinks de los Markdown revisados: resolubles.
- Revisión de secretos y datos personales: sin hallazgos.
- `git diff --check`: sin errores de espacios; solo avisos informativos LF/CRLF.
- No se ejecutaron verificaciones Django porque la aplicación todavía no existe.

## Próximo paso permitido

Crear `specs/001-acceso-usuarias-internas/spec.md` mediante el flujo de especificación. La
spec debe permanecer en borrador o propuesta hasta resolver sus preguntas, registrar la
confirmación humana y excluir explícitamente `RF-ACC-002` a `RF-ACC-004`.

Después corresponden plan, tareas y análisis de coherencia. Django y PostgreSQL comienzan
únicamente cuando esas puertas estén aprobadas.
