---
title: Autorización permanente de commit y push para programación de la app
type: checkpoint
status: completed
date: 2026-10-29
task_id: DOC-GIT-20261029
requirement_ids: []
sprint: S2
module: transversal
repository: ZhudAleli
phase: pre_commit
writer: codex
branch: docs/requisitos-y-organizacion-del-vault
head: dbd0e2207972715ebaf2b7ef2b67f6af63feb6e9
commit: pending
related:
  - "[[../ESTADO-ACTIVO]]"
  - "[[../../git/REPOSITORIOS-Y-PRE-PUSH]]"
  - "[[../../../AGENTS]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
---

# Autorización permanente de commit y push para programación de la app

El tesista solicita expresamente el 2026-10-29 hacer commit descriptivo y push al
repositorio de app después de cada cambio de programación que salga correcto.
Esta solicitud es la autorización permanente: no se infiere de una petición de implementar.
Satisface la exigencia constitucional de solicitud explícita dentro del alcance nombrado.

## Regla registrada

Tras cada porción coherente de programación de la app con verificaciones aplicables
correctas y diff revisado: staging por rutas de la tarea, commit que describe cambio y
validación con RF/sprint reales, y push a la rama de trabajo de
`FranAC18/App-zhudaleli`, sin pedir confirmación de nuevo. No crear commits vacíos.
Excluir cambios ajenos o previos no verificados; si el diff cambia, revisar y verificar
lo afectado. Fallo de verificación: no publicar. Fallo de push: conservar el commit
e informar el envío pendiente, sin integrar ni reescribir historia para completarlo.

La autorización no cubre Git del vault/documentación, push directo a main, force push,
merge, tags, rebase, reset, clean, identidad Git ni despliegue. Una instrucción puntual
del tesista puede suspenderla para una tarea. El cierre de un commit no completa por
sí solo un requisito o historia.

## Fuentes y continuidad

Se alinean AGENTS, contrato/skill de git-manager, adaptadores Codex/OpenCode, regla de
handoff y guía pre-push. Se actualizan estado y alcance de mantenimiento del vault.
Los roles implementer/frontend conservan sus límites; el coordinador o git-manager
ejecuta el cierre Git con esta autorización, sin exigir otro agente ni una nota previa.

Raíces verificadas: vault en `docs/requisitos-y-organizacion-del-vault`, HEAD
`dbd0e2207972715ebaf2b7ef2b67f6af63feb6e9`; app en
`feature/RF-ACC-001-base-proyecto`, HEAD `d208fba3e347bf2fffae1f91ff178a1d33414249`,
remoto de fetch/push `https://github.com/FranAC18/App-zhudaleli.git`.
La app tiene cambios locales previos en frontend de acceso, pruebas, configuración y
CSS compartido. Esta tarea no los modifica, prueba, prepara, commitea ni publica.
El estado refleja el HEAD observado; la evidencia de e3cc071 mantiene su fecha y alcance.

La tarea solo modifica reglas operativas; conserva RF/HU/HT, criterios, prioridades y
estados funcionales del sprint. No se generan ediciones académicas ni se cambia el
gestor local por esta autorización. No hubo acciones Git de escritura ni despliegue.

## Verificación y siguiente paso

- Contrato universal: OK; conserva la advertencia previa del MOC que omite frontend-design.
- Skill git-manager: `Skill is valid!`; YAML/TOML, enlaces, rutas y formato de diez
  archivos correctos; revisión del diff y `git diff --check` correctos.
- HEAD y estado de la app comprobados de nuevo: mismo d208fba y cambios locales previos.
  No se ejecutan pruebas Django porque no se modifica el producto en esta tarea.

Retomar la tarea de programación elegida por el tesista; aplicar la regla al completar
y verificar su próxima porción.
