---
title: Persistencia en archivo del Gantt local
type: checkpoint
status: prepared-pending-review
date: 2026-10-13
task_id: DOC-ORG-001
phase: pre_commit
branch: opencode/spec-001-fase-1-diseno
commit: pending
publication: not-requested
module: planificacion
related:
  - "[[../ESTADO-ACTIVO]]"
  - "[[2026-10-13-gantt-interactivo-pre-commit]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/planificacion
---

# Persistencia en archivo del Gantt local

El tesista pidió que **Guardar seguimiento** actualice un archivo y que al abrir
`index.html` directamente, sin servidor, se recupere el avance. Se preparó la
edición 1.1 del Gantt dentro de `analisis/2026-10-13/gantt-interactivo/`.
El primer guardado solicita elegir un JSON. Los siguientes guardados actualizan
ese archivo y el vínculo se recuerda en el navegador. Al volver a abrir el
índice, se carga el archivo si el permiso sigue vigente. Si el navegador revoca
el permiso, el usuario puede elegir el archivo otra vez. Un indicador visible
distingue el guardado en archivo del guardado local; Exportar e Importar siguen
disponibles como respaldo. No se publicó contenido en `documentacion/`. El JSON
con nombre predeterminado se excluye del repositorio general mediante `.gitignore`.

## Comprobación

- Se abrió `index.html` mediante `file://` en Chrome, sin servidor ni puerto.
- Una prueba de navegador verificó escritura en un archivo de prueba del
  navegador y recuperación tras recargar sin datos en `localStorage`.
- La misma prueba comprobó relaciones y conteos, evidencia exigida, exportación,
  importación y vista móvil.
- La prueba utiliza un archivo simulado del navegador; queda pendiente la
  comprobación manual del selector de archivos del entorno del tesista.
- `git diff --check -- .gitignore` no detectó errores; se verificó que Git
  ignora el JSON con nombre predeterminado.

No se hizo commit ni push. El archivo de seguimiento que cree el tesista es
un dato local de uso y no debe publicarse en el repositorio documental.
