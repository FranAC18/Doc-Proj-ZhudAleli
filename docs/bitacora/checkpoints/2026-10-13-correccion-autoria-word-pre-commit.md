---
title: Corrección de autoría en documentos Word
type: checkpoint
status: prepared-pending-publication
date: 2026-10-13
task_id: DOC-ORG-001
phase: pre_commit
branch: opencode/spec-001-fase-1-diseno
commit: pending
publication: pending
module: documentacion
related:
  - "[[../ESTADO-ACTIVO]]"
  - "[[2026-10-13-fichas-historias-sprints-pre-commit]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/documentacion
---

# Corrección de autoría en documentos Word

El tesista indicó que Jordy Caranqui no es autor de estos documentos.
La portada, la línea de autor y las propiedades internas de las ediciones
vigentes identifican ahora únicamente a Franklin Acero. Se corrigió también
la propiedad de autor en las siete ediciones Word anteriores. Las rutinas
que generan estos archivos ya escriben la autoría correcta.

Se prepararon el compendio Word v1.2 y el plan Word v1.5. El índice público
quedó en v2.6 y el control de cambios registra la corrección. Un archivo
temporal de bloqueo de Word se movió de `documentacion/` a `_archivo/`
con origen, motivo y reemplazo registrados; no se borró.

## Verificación

- Se revisaron los nueve DOCX de `documentacion/`: todos indican a Franklin
  Acero en sus propiedades y ninguno contiene el nombre erróneo en sus XML.
- El verificador conservó 51 HU, 19 HT, 27 tareas, 60 posiciones base y 10 HT
  propuestas; comprobó enlaces locales y criterios de las historias.
- Microsoft Word generó PDFs de las dos ediciones vigentes: 33 y 11 páginas.
  Se revisaron portadas, primeras páginas de contenido y mosaicos del total.
- `git diff --check` para las rutas afectadas no informó errores.

No se hizo commit ni publicación. La revisión académica sigue pendiente.
