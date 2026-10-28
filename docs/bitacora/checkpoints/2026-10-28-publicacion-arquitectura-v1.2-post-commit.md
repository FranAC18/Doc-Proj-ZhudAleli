---
title: Publicación docente de arquitectura v1.2 y documentación v5.1
type: checkpoint
status: published-verified
date: 2026-10-28
author: Codex
task_id: DOC-ORG-001
phase: post_commit
repository: Doc-Proj-ZhudAleli
branch: codex/historial-original-readme-v5
commit: d5943a50adba78c4f020e4f5268e0ba916b660be
parent_commit: 277b41cc527cd439ea93c0890b21b134f963b271
remote: https://github.com/FranAC18/Doc-Proj-ZhudAleli.git
documentation_commit: pending
---

# Publicación docente y comandos para próximas ediciones

El tesista solicitó publicar la documentación preparada en la rama predeterminada elegida
y conocer los comandos para repetir el proceso. Se utilizó el clon separado limpio de
`tmp/Doc-Proj-ZhudAleli-2026-10-27/`; el clon anterior solo seguía `main`, por lo que se añadió
el seguimiento de `codex/historial-original-readme-v5` antes de cambiar de rama.

## Resultado publicado

El [commit d5943a5](https://github.com/FranAC18/Doc-Proj-ZhudAleli/commit/d5943a50adba78c4f020e4f5268e0ba916b660be)
contiene únicamente:

- `README.md`, índice v5.1.
- `arquitectura/arquitectura_v1.2_2026-10-28.md`.
- `control_de_cambios/registro_v5.1_2026-10-28.md`.

Se actualizaron los estados de transferencia de esas tres ediciones; la revisión académica
sigue pendiente. Se comprobaron igualdad de contenido con las fuentes copiadas, metadatos,
enlaces dentro del clon documental, tablas, diff y conjunto preparado. El push fue normal,
sin force; el remoto devuelve el mismo hash y el clon quedó limpio. La rama predeterminada
sigue siendo `codex/historial-original-readme-v5` y conserva los nueve commits originales
más la nueva publicación: diez commits en total.

No se copiaron el `.git` existente en `documentacion/`, modificaciones de ediciones
históricas, archivos Word ni cambios del repositorio general o de la aplicación. Los avisos
«Compare & pull request» de las otras ramas son sugerencias de comparación, no errores ni
una obligación de fusionarlas para continuar publicando en la rama predeterminada.

## Flujo manual en PowerShell

El clon ya tiene el seguimiento remoto configurado. Ajustar la lista de archivos y el
mensaje para cada edición revisada. Ejecutar por pasos y continuar solo si el comando
anterior terminó correctamente. Las publicaciones posteriores a otros destinos o cambios
de historia quedan fuera de este procedimiento.

```powershell
$repoDoc = 'F:/Tesis/App Tesis/tmp/Doc-Proj-ZhudAleli-2026-10-27'
$fuenteDoc = 'F:/Tesis/App Tesis/documentacion'
$archivosDoc = @(
    'README.md',
    'arquitectura/arquitectura_v1.2_2026-10-28.md',
    'control_de_cambios/registro_v5.1_2026-10-28.md'
)

Set-Location $repoDoc
git remote get-url --push origin
git status --short --branch
git switch codex/historial-original-readme-v5
git pull --ff-only origin codex/historial-original-readme-v5

foreach ($archivoDoc in $archivosDoc) {
    $destinoDoc = Join-Path $repoDoc $archivoDoc
    New-Item -ItemType Directory -Force -Path (Split-Path $destinoDoc) | Out-Null
    Copy-Item -LiteralPath (Join-Path $fuenteDoc $archivoDoc) -Destination $destinoDoc
}

git diff --stat
git add -- $archivosDoc
git diff --cached
git diff --cached --check
git commit -m 'docs: actualizar documentación revisada'
git push origin codex/historial-original-readme-v5
git status --short --branch
```

Antes de copiar se espera un clon limpio; el remoto de push debe ser
`https://github.com/FranAC18/Doc-Proj-ZhudAleli.git`. `pull --ff-only` evita fusiones o
reescrituras implícitas. Si se rechaza una actualización, se revisa el estado y la diferencia;
no se añade `--force`. La lista explícita evita copiar el Git de la fuente o publicar material
interno. Cada próxima versión requiere actualizar los nombres de archivo correspondientes.

Esta nota de evidencia y comandos permanece local, sin commit ni push del repositorio general.
