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

[[CAT-REQ-001|CAT-REQ-001 v1.3]] contiene **71 requisitos confirmed, 3 proposed y 12 históricos superseded**: 62 RF y 9 RNF confirmados; RF-COS-001, RF-ACC-005 y RNF-OPS-001 propuestos. La v1.2 aprobada se conserva en [[CAT-REQ-001-v1.2]].

El 2026-10-28 el tesista aceptó RF-ACC-006 a 009 y el plan de correo, passkeys y WhatsApp configurable. Fuente: [[../evidence/requirements/2026-10-28-aceptacion-acceso-multicanal]]. La definición canónica del incremento está en [[../../specs/003-acceso-multicanal/spec|SPEC-003]]. La aceptación no declara implementación ni validación de campo. La propuesta anterior de superadministración mantiene su estado y no se aprueba mediante este cambio.

La revisión académica de la directora y las specs/planes de los flujos nuevos mantienen
sus puertas. La aprobación de requisitos no equivale a implementación o validación de campo.
El [[../evidence/casos-de-uso/2026-09-28-coherencia-integral|control integral anterior]] conserva
su corte de 57 IDs; la nueva evidencia registra la promoción a 60 y sus enlaces.
