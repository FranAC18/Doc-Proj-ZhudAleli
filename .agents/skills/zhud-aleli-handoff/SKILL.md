---
name: zhud-aleli-handoff
description: Persiste el estado de una tarea para continuarla desde Codex, Antigravity, OpenCode u OpenChamber sin depender del historial privado.
---

# Handoff universal

Usa la plantilla `docs/templates/PLANTILLA-HANDOFF-UNIVERSAL.md` y registra el handoff en
`docs/bitacora/checkpoints/` con un nombre único.

El handoff debe incluir como mínimo:

- `task_id`, `requirement_ids`, `sprint`, `module` y `phase`;
- `status` (`planned`, `in-progress`, `partially-complete`, `blocked` o `completed`);
- `writer`, `allowed_paths` y `forbidden_paths`;
- `changed_files` y `unchanged_files` relevantes;
- comandos ejecutados y resultados reales;
- criterios cubiertos y pendientes;
- decisiones, bloqueos y `next_action`;
- `branch`, `commit` (`pending` si aún no existe) y `handoff_to`.

Un cambio de proveedor no autoriza a cambiar de tarea ni de alcance. La herramienta siguiente
debe leer el último handoff, comprobar el estado de Git y confirmar la raíz antes de escribir.
Si hay cambios sin commit, no se abre otro escritor sobre el mismo worktree.
