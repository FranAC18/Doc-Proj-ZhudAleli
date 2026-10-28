---
title: ADR-0008 — Separación de repositorios y flujo Git
type: decision
status: accepted
date: 2026-10-20
decision_owner: tesista
---

# ADR-0008 — Separación de repositorios y flujo Git

## Contexto

El repositorio general contiene requisitos, sprints, agentes y memoria académica. La
aplicación Django todavía no existe. Mantener en el mismo repositorio código y proceso
podría inducir commits al remoto equivocado y exigir documentos de proceso dentro del
proyecto ejecutable. El tesista confirmó el 2026-10-20 el plan para separar los repositorios
y simplificar la base documental del desarrollo.

ADR-0003 había aprobado una sola raíz Git y descartado repositorios separados. La
necesidad actual de aislar el código y reducir bloqueos documentales cambia esa premisa.
Esta decisión posterior sustituye expresamente esa parte de ADR-0003 sin alterar la
arquitectura interna del monolito Django aprobada allí y en ADR-0006.

## Decisión

`FranAC18/ZhudAleli` conserva el vault, la constitución, requisitos, specs, sprints,
agentes, trazabilidad y documentación académica revisada. `/app/` queda ignorada.
`FranAC18/App-zhudaleli` aloja solo el código de producto y los archivos técnicos
necesarios para ejecutarlo, probarlo y construirlo. El checkout local puede estar en
`app/`, pero su raíz Git y su remoto se verifican antes de cualquier push.

La estructura `manage.py`, `config/`, `apps/`, `templates/`, `static/` y `tests/`
descrita por ADR-0003 se traslada intacta a la raíz Git de `App-zhudaleli`.
`specs/`, `docs/` y agentes permanecen en la raíz del repositorio general. La
antigua objeción de ADR-0003 a repositorios separados queda sustituida por la
trazabilidad de RF, sprint, PR y tag de esta decisión.

La base documental mínima para desarrollar es un requisito vigente con criterios
verificables y su sprint. Se respetan specs, planes y tareas aprobados cuando existen;
la falta de esos archivos o su ausencia en la app no bloquea por sí sola un commit.
La revisión, seguridad y evidencia requeridas para declarar trabajo terminado continúan.

El código se integra a `main` protegida mediante PR desde ramas
`feature/RF-XXX-descripcion`, con Conventional Commits y referencias a RF y sprint.
La matriz general enlaza requisito, sprint y PR/tag de cada entrega de aplicación.
Un sprint sin código integrado se registra sin inventar un tag de aplicación.

## Consecuencias y controles

- Hay dos raíces Git y dos remotos; el git-manager comprueba ambos antes de staging/push.
- La app no duplica agentes, specs ni documentación de proceso.
- La matriz puede actualizarse después del PR/tag, sin exigir un commit documental previo
  a cada commit de código.
- `git filter-repo` se usa solo si la auditoría encuentra historial de código de la app
  en una ruta del repositorio general; opera sobre clon desechable con respaldo verificado.
- La constitución pasa de 1.0.0 a 2.0.0 por el cambio incompatible en la puerta documental
  previa al desarrollo. No modifica el alcance funcional aprobado ni declara el Sprint 1
  completamente implementado.
- La frase de ADR-0003 que exige plan/tareas antes del código se sustituye por la base
  mínima de RF y sprint; las decisiones materiales pendientes siguen requiriendo
  validación antes de implementarse.

## Referencias

- [[../../.specify/memory/constitution|Constitución 2.0.0]]
- [[ADR-0003-estructura-raiz-aplicacion-django|ADR-0003, parcialmente sustituido]]
- [[../git/REPOSITORIOS-Y-PRE-PUSH|Guía de repositorios y pre-push]]
- [[../traceability/MATRIZ-TRAZABILIDAD|Matriz de trazabilidad]]
