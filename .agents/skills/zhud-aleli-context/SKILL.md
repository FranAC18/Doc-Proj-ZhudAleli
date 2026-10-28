---
name: zhud-aleli-context
description: Carga el contrato común, la raíz del vault, el estado activo y la especificación vigente de Zhud Alelí antes de trabajar.
---

# Contexto universal de Zhud Alelí

Usa esta skill al iniciar una sesión o cuando cambies de host/modelo.

1. Identifica la raíz Git actual con `git rev-parse --show-toplevel` y distingue
   `ZhudAleli` (vault y proceso) de `App-zhudaleli` (código). Si trabajarás en
   ambos, comprueba ambas rutas y remotos por separado.
2. En el repositorio general lee `AGENTS.md`,
   `docs/context/context-index.md`, `docs/bitacora/ESTADO-ACTIVO.md` y las
   secciones pertinentes de la constitución; confirma el RF y sprint vigentes.
3. Lee `docs/context/feature-index.md` y solo los apartados de spec, plan o tareas
   pertinentes si existen. Su ausencia en la app no bloquea el desarrollo.
4. Ejecuta `git status --short --branch` en cada repositorio que vaya a tocarse.
5. Indica qué es hecho verificado, propuesta o pendiente; no confundas código del
   laboratorio `tools/agent-lab/` con la aplicación Django.

No cargues todo el repositorio. Sigue los Wikilinks e índices desde estos puntos de entrada.
Si el directorio actual no está dentro de la raíz, detente antes de escribir.
