---
title: Separación de repositorios y reglas Git — pre_commit
type: checkpoint
status: partially-complete
date: 2026-10-20
task_id: GOV-GIT-001
phase: pre_commit
repository: ZhudAleli
branch: docs/requisitos-y-organizacion-del-vault
base_head: d053980819ff3b0ff783a1d8f7c124eb8f8d217f
commit: pending
requirement_ids: []
sprint: governance
related:
  - "[[../../decisions/ADR-0008-separacion-repositorios-y-flujo-git]]"
  - "[[../../git/REPOSITORIOS-Y-PRE-PUSH]]"
---

# Separación de repositorios y reglas Git — pre_commit

## Autorización y alcance

El tesista confirmó el plan el 2026-10-20 y solicitó actualizar las skills y agentes
necesarios para ordenar el desarrollo y reducir riesgos. Esta autorización cubre los
cambios locales descritos aquí. No se ha solicitado un conjunto exacto para commit o
push de estos cambios.

## Resultado local

- La constitución pasa a 2.0.0 y ADR-0008 registra dos repositorios y la base
  documental mínima de RF y sprint. ADR-0008 sustituye expresamente la decisión
  de raíz Git única de ADR-0003 y conserva su estructura Django interna.
- `AGENTS.md`, README, roles canónicos, adaptadores, skills y templates relevantes
  distinguen código de producto y documentación de proceso. El roadmap propuesto
  y la política Obsidian fueron alineados con esa separación.
- El repositorio general ignora `/app/`; `documentacion/` sigue ignorada por defecto
  porque contiene ediciones con estados de revisión distintos. Su incorporación se
  hará por archivo revisado y staging explícito.
- Se creó `app/` como repositorio Git local independiente, sin commits, con remoto
  `https://github.com/FranAC18/App-zhudaleli.git` y su propio `.gitignore`.
- La consulta a GitHub identificó `App-zhudaleli` como repositorio privado vacío.
  El repositorio general no contiene `app/` versionada ni historial de esa ruta.
  Por ello no se ejecutó `git filter-repo` ni se reescribió historia; la guía deja
  los pasos condicionales con respaldo verificado.
- La matriz declara que S0 y S1 calendario no tuvieron entrega de código de app.
  SPEC-001 usaba un S1 histórico que corresponde al S2 del calendario vigente.

## Verificaciones reales

- Rama general: `docs/requisitos-y-organizacion-del-vault`; HEAD base:
  `d053980819ff3b0ff783a1d8f7c124eb8f8d217f`.
- Remoto general: `https://github.com/FranAC18/ZhudAleli.git`.
- `git check-ignore -v app/.gitignore` confirma que `/app/` se ignora en el general.
- `git -C app rev-parse --show-toplevel` confirma la raíz independiente `app/`;
  `git -C app remote -v` apunta solo a `App-zhudaleli`.
- `git diff --check` del repositorio general terminó sin errores de espacios.
- No se ejecutaron pruebas de aplicación: no existe código Django en este cambio.

## Pendientes

- Revisar y autorizar el conjunto exacto de archivos antes de hacer commit/push.
- El `.gitignore` de la app sigue local y sin commit; el remoto continúa vacío.
- Tras un bootstrap inicial autorizado se debe activar protección de `main` y PR
  obligatorio antes de integrar funcionalidades.
- Antes del primer commit de código, registrar el sprint de ejecución real de los
  RF pendientes del S1 cerrado. No se crea tag `sprint-0` o `sprint-1` sin código.
- La modificación local preexistente de `.codex/config.toml` y el archivo temporal
  de Office no forman parte de este cambio.
