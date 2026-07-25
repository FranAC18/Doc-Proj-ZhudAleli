# Especificaciones de funcionalidades

Cada funcionalidad ocupa un directorio numerado:

```text
specs/001-nombre-corto/
├── spec.md
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
├── checklists/
└── tasks.md
```

## Estados

- `draft`: generado y todavía incompleto.
- `proposed`: listo para discusión, no autorizado para implementar.
- `confirmed`: validado por las personas indicadas; permite planificar. Implementar requiere
  además plan y tareas aprobados, análisis de coherencia y las puertas del proyecto superadas.
- `implemented`: integrado con pruebas, pendiente de validación final si aplica.
- `validated`: evidencia de aceptación registrada.
- `superseded`: reemplazado por una revisión enlazada.
- `discarded`: descartado con motivo.

El estado se cambia por una decisión humana identificable. Un agente puede preparar la
edición, pero no aprobarla.

## Invocación

- Codex: `$speckit-specify`, `$speckit-clarify`, `$speckit-plan`, `$speckit-tasks`,
  `$speckit-analyze`, `$speckit-implement`.
- Kimi Code: `/skill:speckit-specify`, `/skill:speckit-clarify`,
  `/skill:speckit-plan`, `/skill:speckit-tasks`, `/skill:speckit-analyze`,
  `/skill:speckit-implement`.

Las plantillas resueltas deben provenir de `.specify/templates/overrides/`.
