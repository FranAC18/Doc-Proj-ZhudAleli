---
title: Recuperación del repositorio documental al corte README v5.0
type: checkpoint
status: restored-verified
date: 2026-10-28
author: Codex
task_id: DOC-ORG-001
phase: post_commit
repository: Doc-Proj-ZhudAleli
branch: main
commit: bdd91aed16caf837e36406b0914c530d3a6afc5e
target_commit: 277b41cc527cd439ea93c0890b21b134f963b271
target_tree: 908b2d8a44aa203d93e48d602aba25bb12edecf0
previous_head: 7212e74e7bd36e0eb237c3223b3d04e9c9750791
remote: https://github.com/FranAC18/Doc-Proj-ZhudAleli.git
default_branch: main
publication: verified
documentation_commit: pending
---

# Recuperación documental al corte README v5.0

El tesista informó de un force push accidental y pidió corregir el repositorio documental
para volver a «docs: actualizar índice README v5.0». La inspección confirmó que el commit
objetivo `277b41c` seguía disponible y que `main` y `recuperada` apuntaban al nuevo commit raíz
`7212e74`. La rama predeterminada era `recuperada`.

## Respaldo previo

- Se creó un clon técnico separado, sin checkout, en
  `tmp/recuperacion-documental-2026-10-28/`, ignorado en el repositorio general.
- Se recuperó el objeto completo del commit objetivo y se comprobó su historial.
- Se creó y verificó un bundle completo en
  `tmp/Doc-Proj-ZhudAleli-antes-restaurar-20261028.bundle`.
- Se conservaron dos ramas remotas: `codex/respaldo-antes-restaurar-20261028` en `7212e74`
  y `codex/historial-original-readme-v5` en `277b41c`.

## Restauración publicada

Se creó el [commit de recuperación bdd91ae](https://github.com/FranAC18/Doc-Proj-ZhudAleli/commit/bdd91aed16caf837e36406b0914c530d3a6afc5e),
con padre `7212e74` y exactamente el árbol documental del objetivo `277b41c`.
La rama `main` avanzó normalmente mediante una actualización condicionada a su HEAD esperado;
no se realizó force push, reset, borrado de ramas ni reescritura del historial.

La comparación previa identificó nueve archivos afectados, incluidas diferencias en dos
Word. La restauración del árbol conserva exactamente las versiones anteriores de esos
archivos y retira de `main` arquitectura v1.2 y control de cambios v5.1, conforme al corte
solicitado. El estado posterior al force push sigue disponible en su rama de respaldo.

La restauración del contenido no vuelve a colocar el puntero de `main` en el commit antiguo:
`main` contiene un commit nuevo de recuperación. La cadena original de commits se conserva
íntegra en `codex/historial-original-readme-v5`, sin fusionarla ni reescribirla.
Se restableció `main` como rama predeterminada; `recuperada` permanece sin modificaciones.

## Verificación posterior

- El remoto `main` apunta a `bdd91aed16caf837e36406b0914c530d3a6afc5e`.
- Los árboles de `main` y `277b41c` son idénticos:
  `908b2d8a44aa203d93e48d602aba25bb12edecf0`.
- `git diff --exit-code 277b41c origin/main` no devuelve diferencias.
- El árbol restaurado contiene 113 archivos; el README declara versión 5.0.
- Ambas ramas de respaldo apuntan a sus hashes esperados.
- El conector GitHub confirmó que la rama predeterminada es `main`.

La recuperación se limitó a `FranAC18/Doc-Proj-ZhudAleli`. No se cambió el código de la app
ni se sustituyeron las ediciones locales de `documentacion/` en el repositorio general.
Esta nota operativa permanece local, sin commit ni push adicional.
