# Regla de continuidad entre herramientas

Codex, Antigravity, OpenCode y OpenChamber son hosts alternativos sobre el mismo proyecto.
No se consideran escritores concurrentes. Antes de cambiar de host, lee el último archivo de
`docs/bitacora/checkpoints/` relacionado con la tarea, confirma `git status` y respeta
`allowed_paths`/`forbidden_paths`.

Si hay cambios sin commit en el mismo worktree, solo una herramienta puede continuar como
escritor. Un cambio de modelo o cuota no cambia la tarea ni el alcance: se registra un handoff
y la siguiente herramienta continúa desde el estado persistido.

El `documenter` solo escribe documentación operativa permitida. El `git-manager` solo crea un
commit después de autorización explícita del tesista.
