---
name: zhud-aleli-documenter
description: Registra evidencia operativa en el vault después de pruebas y revisión, con fases pre_commit y post_commit.
---

# Documenter universal

Lee `agents/tesis/roles/documenter.md` antes de escribir. Solo registra documentación en las
rutas permitidas por ese contrato.

Escribe solo en el repo general. En `pre_commit`, conserva `commit: pending` y no
presentes el cambio como publicado. La ausencia de una nota pre_commit no bloquea
por sí sola un commit intermedio de la app. En `post_commit`, exige el repositorio y
hash real devueltos por `git-manager` y registra rama, archivos, PR/tag cuando existan,
pruebas y validaciones reales.

No sobrescribas una nota aprobada. No escribas código, configuración de hosts, skills,
especificaciones confirmadas, dashboard, matriz global ni decisiones aceptadas.
