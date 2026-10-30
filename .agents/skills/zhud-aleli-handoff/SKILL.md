---
name: zhud-aleli-handoff
description: Persiste el estado de una tarea para continuarla desde Codex, Antigravity, OpenCode u OpenChamber sin depender del historial privado.
---

# Handoff universal

Usa la plantilla `docs/templates/PLANTILLA-HANDOFF-UNIVERSAL.md` y registra el handoff en
`docs/bitacora/checkpoints/` con un nombre único.
Un checkpoint puede cubrir también el resumen de sesión. Enlaza evidencia extensa y
conserva aquí resultado, pendientes y siguiente acción, sin copiar el historial.

El handoff debe incluir como mínimo:

- `task_id`, `requirement_ids`, `sprint`, `module`, `repository` y `phase`;
- `status` (`planned`, `in-progress`, `partially-complete`, `blocked` o `completed`);
- `writer`, `allowed_paths` y `forbidden_paths`;
- `changed_files` y `unchanged_files` relevantes;
- comandos ejecutados y resultados reales;
- criterios cubiertos y pendientes;
- decisiones, bloqueos y `next_action`;
- `branch`, `commit` (`pending` si aún no existe), `remote` y `handoff_to`.

Un cambio de proveedor no autoriza a cambiar de tarea ni de alcance. La herramienta siguiente
debe leer el handoff enlazado para esa tarea, comprobar el estado de Git y confirmar la raíz del
repositorio correspondiente antes de escribir.
Consulta `scope_file` desde el estado activo para las rutas vigentes. No cargues todos
los checkpoints ni las fuentes ya vigentes en el chat.
Si hay cambios sin commit, no se abre otro escritor sobre el mismo worktree.
