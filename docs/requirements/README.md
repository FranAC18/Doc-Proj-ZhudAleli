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

Un agente puede redactar propuestas; solo registra `confirmed` cuando existe aprobación
humana explícita, con evidencia y alcance identificados. No se autoaprueban requisitos.

Consulta [[../architecture/FUENTES-DE-VERDAD|Fuentes de verdad]] y
[[../traceability/MATRIZ-TRAZABILIDAD|Matriz de trazabilidad]].

## Línea base actual

[[CAT-REQ-001|CAT-REQ-001 v1.1]] está confirmado por el tesista el 2026-09-28:
**60 requisitos confirmed, 2 proposed y 12 históricos superseded**. Incorpora los ajustes
de continuidad y RF-PWA-001/002/003, con guardado y sincronización offline obligatorios.
La [[../evidence/casos-de-uso/2026-09-28-aprobacion-requisitos-v1-1|aprobación explícita]]
identifica quién aprueba y qué queda pendiente. P-01…P-14 no se resuelven por inferencia.

La [[CAT-REQ-001-v1.0.md|v1.0]] conserva íntegra la aprobación de julio y sus 57 IDs;
su exclusión offline ya no rige la versión actual. R3 y la
[[proposals/2026-09-28-catalogo-v1-1|propuesta v1.1 aceptada]] son antecedentes incorporados,
no catálogos paralelos. No se extiende la aprobación de julio a nuevas autoridades.

La revisión académica de la directora y las specs/planes de los flujos nuevos mantienen
sus puertas. La aprobación de requisitos no equivale a implementación o validación de campo.
El [[../evidence/casos-de-uso/2026-09-28-coherencia-integral|control integral anterior]] conserva
su corte de 57 IDs; la nueva evidencia registra la promoción a 60 y sus enlaces.
