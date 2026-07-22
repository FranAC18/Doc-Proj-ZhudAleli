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
