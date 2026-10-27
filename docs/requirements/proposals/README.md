# Propuestas de requisitos

Guarda aquí hallazgos todavía no validados, con estado `proposed`, fuente, fecha, actor y
persona/grupo que debe confirmarlos. Cuando una propuesta se confirma, enlaza la spec
canónica en `specs/`; no dupliques su contenido completo.

## Catálogo vigente

- **Canónico:** [[../CAT-REQ-001|CAT-REQ-001 v1.2]], con 67 requisitos `confirmed`, dos
  `proposed` y 12 IDs históricos `superseded`.
- **Revisión candidata:** [CAT-REQ-001 v1.3 — superadministración](2026-10-27-CAT-REQ-001-v1.3-superadmin.md),
  estado `proposed`; no reemplaza la línea base hasta ser validada y aprobada.
- `RF-COS-001` y `RNF-OPS-001` permanecen `proposed` en la base canónica. `RF-ACC-005` es un
  código candidato en la revisión v1.3 y requiere confirmación del tesista; su fuente se reporta
  como solicitud de la presidenta, sin validación directa registrada.

## Paquete candidato de superadministración — 2026-10-27

El paquete permanece en el vault interno. El requisito, las historias, SPEC-002 y la pila son
propuestas; el plan v1.1 fue aprobado por el tesista solo como plan técnico. No se aprueba el
requisito, la validación de la presidenta, una prioridad, un sprint ni código.

| Artefacto | Estado | Uso |
|---|---|---|
| [Historias de usuario v2.6 candidata](2026-10-27-historias-usuario-v2.6-superadmin.md) | `proposed` | Refinamientos candidatos de HU-ACC-002/003 y cinco historias sin sprint ni prioridad |
| [SPEC-002](../../../specs/002-superadministracion/spec.md) | `proposed` | Matriz actor → acción → recurso → resultado; no está lista para `speckit-implement` |
| [Checklist de SPEC-002](../../../specs/002-superadministracion/checklists/requirements.md) | `incomplete` | Puertas y preguntas que deben resolverse para validar requisitos |
| [Pila v1.8 candidata](2026-10-27-pila-producto-v1.8-superadmin.md) | `proposed` | Conserva la lista base y mantiene aparte los candidatos sin sprint |
| [Plan de implementación v1.1](../../decisions/proposals/2026-10-27-plan-implementacion-superadmin-v1.1.md) | `approved` por el tesista | Enfoque y fases aprobados como plan; no autoriza implementación ni asigna sprint |

La atribución de la solicitud a la presidenta procede del relato del tesista. La confirmación
directa de la presidenta, la delimitación de datos y la prioridad del incremento siguen
pendientes. Se conserva `.specify/feature.json` apuntando a SPEC-001 durante el trabajo activo
de acceso; SPEC-002 no desplaza la funcionalidad activa.

## Historial de propuestas

- [[2026-07-22-catalogo-revisado-requisitos-r3|CAT-REQ-001-R3 (validado con ajustes y superseded)]].
- [[2026-07-22-catalogo-revisado-requisitos|CAT-REQ-001-R2 (superseded)]].
- [[2026-07-21-catalogo-inicial-requisitos|CAT-REQ-001-R1 (superseded)]].

## Historial de actualización

| Fecha | Cambio |
|---|---|
| 2026-10-27 | Se corrige el puntero canónico a CAT-REQ-001 v1.2 y se indexa el paquete de propuestas de superadministración sin aprobar requisitos ni asignar sprint. |
| 2026-10-27 | Se indexa el plan v1.1 aprobado por el tesista, manteniendo `RF-ACC-005`, SPEC-002, prioridad y sprint pendientes. |
