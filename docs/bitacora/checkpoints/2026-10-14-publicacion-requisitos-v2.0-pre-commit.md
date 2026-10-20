---
title: Publicación de requisitos generales v2.0 y priorización v1.3 — pre-commit
type: checkpoint
status: ready-for-commit
date: 2026-10-14
task_id: DOC-ORG-001
phase: pre_commit
commit: pending
documentary_branch: main
documentary_remote: https://github.com/FranAC18/Doc-Proj-ZhudAleli.git
files:
  - README.md
  - control_de_cambios/registro_v2.8_2026-10-14.md
  - requisitos/requisitos_generales_v2.0_2026-10-13.md
  - requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13.md
---

# Handoff pre-commit

## Autorización

El tesista aprobó la publicación de requisitos generales v2.0 y priorización v1.3 y solicitó
explícitamente hacer commit y push al repositorio documental. El conjunto oficial exacto incluye
esos dos documentos y los dos archivos de índice/control necesarios para mantener la entrega
consultable y versionada.

## Base y revisión

| Comprobación | Resultado |
|---|---|
| Repositorio y rama | `Doc-Proj-ZhudAleli`, `main`. |
| HEAD antes del cambio | `ced45f66f84b783b47eb730f277fd2bf01e69475`, alineado inicialmente con `origin/main`. |
| Manifiesto staged | Coincide exactamente con los cuatro archivos listados en este checkpoint. |
| Requisitos en la lista general | 58 filas RF confirmadas y 9 filas RNF confirmadas. |
| Copias de los documentos aprobados | SHA-256 de cada copia coincide con su fuente en `documentacion/`. |
| Enlaces Markdown de los cuatro archivos | 0 enlaces locales rotos. |
| `git diff --cached --check` | Pasó. |
| Secretos o código | No se incluyeron. |
| Pruebas de aplicación | No aplican: el cambio publica documentos. |

## Pendientes conservados

La revisión académica formal y la validación organizacional directa de las novedades siguen
pendientes. P-03 conserva decisiones abiertas; la publicación no las resuelve ni declara
terminado Sprint 1.

## Commit autorizado

Mensaje: `docs: publicar requisitos generales v2.0 y priorización v1.3`

Este checkpoint deja `commit: pending` hasta obtener el hash real del commit y verificar el push.
