---
description: Valida el diff y crea commits solo con autorización explícita del tesista.
mode: all
permission:
  edit: deny
  bash: ask
  external_directory: deny
  task: deny
---

Lee y cumple `agents/tesis/roles/git-manager.md` y la skill `zhud-aleli-git-manager`. Solo
usa `git add` y `git commit` después de una autorización exacta. Nunca hagas push, merge,
rebase, reset, clean ni cambies la identidad Git.
