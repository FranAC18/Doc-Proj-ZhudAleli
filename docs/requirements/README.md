# Requisitos del sistema

Esta carpeta recibe hallazgos y propuestas provenientes de entrevistas, observación,
anteproyecto o decisiones. Una propuesta vive en `docs/requirements/proposals/` con estado
`proposed`.

Cuando se valida una funcionalidad, su definición canónica se conserva en
`specs/<id-funcionalidad>/spec.md`. Esta carpeta puede mantener el índice y la nota de origen,
pero no una segunda copia divergente del requisito.

## Mínimos

- Identificador estable: `RF-<MOD>-XXX`, `RNF-<MOD>-XXX` o `RN-<MOD>-XXX`.
- Actor y problema.
- Descripción y reglas de negocio.
- Criterios de aceptación.
- Fuente identificable y fecha.
- Sprint/módulo.
- Persona o grupo que debe validar.
- Estado: `proposed`, `confirmed`, `implemented`, `validated`, `superseded` o `discarded`.
- Enlaces a spec, pruebas y evidencia cuando existan.

Un agente puede redactar una propuesta, pero no cambiarla a `confirmed`.

Consulta [[../architecture/FUENTES-DE-VERDAD|Fuentes de verdad]] y
[[../traceability/MATRIZ-TRAZABILIDAD|Matriz de trazabilidad]].

## Línea base actual

[[CAT-REQ-001|CAT-REQ-001 v1.0]] es el catálogo canónico aprobado el 2026-07-22. Registra
57 requisitos `confirmed`, 2 `proposed` y 12 `superseded`, además de las decisiones de detalle
que deben cerrarse en las specs correspondientes.

[[proposals/2026-07-22-catalogo-revisado-requisitos-r3|CAT-REQ-001-R3]] queda como antecedente
histórico `superseded`; no debe editarse para cambiar la línea base vigente.
