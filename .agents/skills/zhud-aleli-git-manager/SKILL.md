---
name: zhud-aleli-git-manager
description: Revisa y publica porciones verificadas de código bajo la autorización permanente de AGENTS.md; otros cambios Git requieren autorización específica.
---

# Git-manager universal

Lee `agents/tesis/roles/git-manager.md` y la guía
`docs/git/REPOSITORIOS-Y-PRE-PUSH.md`. Identifica la raíz Git y remoto objetivo antes
de staging. Para código, consulta RF y sprint en el repo general y opera solo en
`App-zhudaleli`; no exige que sus documentos de proceso estén dentro de la app.
Revisa rama, diff, verificaciones reales, secretos, archivos ajenos y
`git diff --check`. Usa el handoff `pre_commit` cuando exista; no inventa uno para
justificar un commit intermedio.

En `ZhudAleli`, la carpeta `/app/` debe permanecer excluida del repositorio general.
Antes de preparar cambios allí, comprueba que `git check-ignore -v app/` la reconoce
como ignorada y que `git ls-files -- app/` no devuelve archivos. Nunca la agregues,
fuerces con `git add -f`, ni la registres como submódulo o gitlink. Si aparece en el
índice o deja de estar ignorada, detén el staging y reporta el problema. El checkout
`app/` es una raíz Git independiente: cualquier operación sobre su código se hace
desde esa raíz y con la autorización aplicable de AGENTS.md; no lo incorpores al repositorio
general.

Para programación de la app, aplica la autorización permanente del 2026-10-29 de
AGENTS.md: tras cada porción coherente con pruebas/verificaciones aplicables y diff
revisado, prepara sus rutas exactas, crea commit descriptivo y haz push a la rama de
trabajo, sin pedir otra confirmación. Excluye cambios ajenos o previos no verificados;
no crees commits vacíos. El mensaje explica el cambio y validación con RF/sprint reales.
Si cambia el diff, repite la revisión y verificación afectadas. Si fallan, no publiques;
si falla el push, conserva el commit e informa el pendiente.

Para el vault/documentación u otras acciones Git, exige autorización específica del
tesista. Antes de cada push ejecuta el checklist de ruta, raíz, `git remote -v`, URL
de push, rama e índice. La autorización permanente no cubre push directo a `main`,
force push, merge, tags, rebase, reset, clean, identidad Git ni despliegue. No uses
`git add .` desde la raíz general.
