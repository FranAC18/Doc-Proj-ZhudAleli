---
description: Registra sesiones, checkpoints y evidencias operativas en el vault.
mode: all
permission:
  edit:
    "*": deny
    "docs/bitacora/sesiones/**": allow
    "docs/bitacora/checkpoints/**": allow
    "docs/evidence/**": allow
    "docs/requirements/proposals/**": allow
    "docs/decisions/proposals/**": allow
    "docs/ui/proposals/**": allow
  bash: ask
  external_directory: deny
  task: deny
---

Lee y cumple `agents/tesis/roles/documenter.md` y la skill `zhud-aleli-documenter`. Solo
escribe después de pruebas y revisión. Exige `commit_hash` real para `post_commit`.
