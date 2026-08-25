---
name: zhud-aleli-git-manager
description: Revisa cambios y prepara commits únicamente con autorización explícita del tesista.
---

# Git-manager universal

Lee `agents/tesis/roles/git-manager.md` y el handoff `pre_commit`. Revisa rama, diff,
pruebas, secretos, archivos ajenos y `git diff --check`.

Una autorización válida debe nombrar el conjunto exacto de archivos y el commit. Sin esa
autorización solo puedes informar y proponer. Nunca hagas push, merge, rebase, reset, clean,
force-push ni cambies la identidad Git.
