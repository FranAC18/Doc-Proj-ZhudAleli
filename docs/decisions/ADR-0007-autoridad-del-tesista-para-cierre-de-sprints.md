---
id: ADR-0007
title: Autoridad del tesista para cerrar sprints
type: decision
status: accepted
date: 2026-10-20
accepted_by: tesista
accepted_date: 2026-10-20
constitution: 1.0.0
related:
  - "[[../bitacora/ESTADO-ACTIVO]]"
  - "[[../bitacora/checkpoints/2026-10-20-cierre-sprint-1-parcial]]"
  - "[[../traceability/MATRIZ-TRAZABILIDAD]]"
tags: [proyecto/tesis, tipo/decision, modulo/transversal]
---

# ADR-0007: Autoridad del tesista para cerrar sprints

## Confirmación y alcance

El 2026-10-20 el tesista solicitó explícitamente modificar la constitución para tener
autoridad total sobre el cierre de sprints, sin trámites que frenen el desarrollo. Esta
solicitud aprueba esta regla de gobierno. No se atribuye una aprobación externa.

## Contexto

La regla previa hacía depender el cierre de una revisión completa de evidencias y de puertas
que podían mantener abierto un periodo aunque el tesista quisiera continuar. El estado del
proyecto distingue un sprint cerrado de forma parcial de tareas o requisitos terminados; esa
distinción permite avanzar sin alterar los hechos pendientes.

## Decisión

1. El tesista tiene autoridad exclusiva para cerrar o reabrir cualquier sprint, elegir la fecha
   y decidir el avance al siguiente, sin autorización de agentes, revisores, directora u
   organización, y sin acta ni aprobación adicional.
2. El cierre puede tener resultado `completed`, `partially-complete` o `blocked`, según lo
   realmente realizado. Para continuidad, anotar sprint, fecha, resultado y pendientes en el
   estado, backlog o checkpoint que ya se utilice; el apunte no es precondición ni aprobación,
   y no se exige crear un expediente separado.
3. Revisar pruebas, enlaces, defectos y criterios informa el resultado, pero no es una
   condición previa para cerrar el periodo. Los pendientes se conservan y pueden trasladarse.
4. El cierre del periodo no marca tareas como terminadas, no aprueba requisitos ni decisiones,
   no sustituye la validación específica de un entregable y no altera el alcance por sí solo.
   Esas afirmaciones continúan sujetas a sus criterios y evidencia reales.
5. Esta autoridad no autoriza `commit`, `push`, publicación ni otras acciones externas que
   requieren autorización específica según las reglas vigentes.

## Consecuencias y aplicación

La constitución cambia de 0.2.0 a 1.0.0 porque se redefine una puerta de gobierno previamente
bloqueante. Se sincronizan plantillas, guía de Obsidian, matriz de trazabilidad y estado activo.
Esta regla modifica la decisión administrativa del periodo; no declara aprobada una
metodología académica nueva, no cambia el cronograma y no altera aprobaciones requeridas para
entregables concretos.

Sprint 0 permanece `completed`. Sprint 1 permanece cerrado con resultado `partially-complete`
según el registro ya existente [[../bitacora/checkpoints/2026-10-20-cierre-sprint-1-parcial]].
La enmienda no cambia los pendientes documentados ni requiere otra aprobación para continuar.
