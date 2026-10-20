---
title: Publicación documental verificada
type: checkpoint
status: completed
date: 2026-10-13
task_id: DOC-ORG-001
phase: post_commit
branch: opencode/spec-001-fase-1-diseno
commit: 09f4318106fd85d10c3095d592c177c33972c1ff
documentary_branch: main
documentary_commit: 20f42279a769b3aefc6d52a0efde79e4c707e498
documentary_remote: https://github.com/FranAC18/Doc-Proj-ZhudAleli.git
module: transversal
sprint: transversal
related:
  - "[[2026-10-13-preparacion-publicacion-documental]]"
  - "[[../ESTADO-ACTIVO]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/transversal
---

# Publicación documental verificada

## Resultado

El tesista autorizó expresamente los dos conjuntos exactos del manifiesto
pre_commit y el push del repositorio del docente. Se crearon estos commits:

| Repositorio | Rama | Hash | Archivos | Publicación |
|---|---|---|---:|---|
| General | `opencode/spec-001-fase-1-diseno` | `09f4318106fd85d10c3095d592c177c33972c1ff` | 38 archivos internos | Commit local; sin push. |
| [Documental del docente](https://github.com/FranAC18/Doc-Proj-ZhudAleli) | `main` | `20f42279a769b3aefc6d52a0efde79e4c707e498` | 24 archivos Markdown | Push a `origin/main` verificado. |

## Comprobaciones realizadas

| Comprobación | Resultado |
|---|---|
| Lista preparada del repositorio general | Coincidió con los 38 archivos autorizados; no incluyó `documentacion/`, `design/`, `specs/` ni archivos de host. |
| Lista preparada del repositorio docente | Coincidió con los 24 Markdown autorizados; cero archivos adicionales. |
| Contenido copiado | Antes del commit, rutas y SHA-256 de los 24 archivos coincidieron con `documentacion/`. |
| Formato | `git diff --cached --check` pasó en ambos repositorios. |
| Enlaces y trazabilidad documental | 0 enlaces locales rotos; 51 RF, 9 RNF, 51 HU, 9 HT y 60 entradas de pila sin duplicados. |
| Exclusión del repositorio general | `git check-ignore` confirmó que `.gitignore` excluye `documentacion/README.md`. |
| Publicación remota | `git ls-remote` devolvió `20f42279a769b3aefc6d52a0efde79e4c707e498` para `refs/heads/main`, igual que el commit local. |

La comprobación global `git diff --check` antes de los commits señaló dos
espacios finales preexistentes en `design/style-guide/tokens.html`, fuera del
conjunto autorizado. La comprobación limitada a los archivos de esta tarea
pasó. No se hicieron pruebas de aplicación: todavía no existe una aplicación
Django funcional. Otros cambios locales anteriores permanecen fuera de estos
commits.

## Pendientes del contenido

La publicación documenta el estado conocido, no aprueba nuevas capacidades.
Siguen pendientes el acta de la entrevista, P-03 y otras reglas de negocio, la
unidad de USD 15 por inconsistencia, costos operativos, estimación de la pila,
revisión académica y evaluación del sistema cuando exista.

Este checkpoint post_commit se creó después de los commits y conserva sus
hashes reales. No forma parte del conjunto de 38 archivos ya confirmado.
