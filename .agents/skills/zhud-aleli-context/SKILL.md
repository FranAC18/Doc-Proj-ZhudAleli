---
name: zhud-aleli-context
description: Recupera el contexto mínimo de Zhud Alelí al iniciar o retomar trabajo, según la tarea y sin releer historial.
---

# Contexto universal de Zhud Alelí

Usa esta skill al iniciar o retomar trabajo, o al cambiar de host/modelo. Reutiliza las
fuentes ya disponibles y vigentes en el chat; no vuelvas a leerlas por cada mensaje.

1. Identifica la raíz Git actual con `git rev-parse --show-toplevel` y distingue
   `ZhudAleli` (vault y proceso) de `App-zhudaleli` (código). Si trabajarás en
   ambos, comprueba ambas rutas y remotos por separado.
2. Recupera `AGENTS.md`, `docs/context/context-index.md` y
   `docs/bitacora/ESTADO-ACTIVO.md` del general. Clasifica con el bloque pertinente
   de `tools/agent-routes.toml`. Antes de escribir, consulta las rutas en `scope_file`.
3. Para producto, confirma RF y sprint; abre `docs/context/feature-index.md` solo si
   necesitas una funcionalidad. Lee constitución, spec, plan, tareas, contratos o datos
   según la clasificación de AGENTS.md. Su ausencia en la app no bloquea el desarrollo.
   Busca por ID y abre las secciones relacionadas, sin exigir una ficha o un recorrido
   documental completo. La guía `docs/context/recorrido-tarea.md` es opcional si hay dudas.
4. Ejecuta `git status --short --branch` en cada repositorio que vaya a tocarse.
5. Indica qué es hecho verificado, propuesta o pendiente; no confundas código del
   laboratorio `tools/agent-lab/` con la aplicación Django.

El historial y los checkpoints se abren para resolver una duda o continuar una tarea
concreta, no por defecto. Tras compactación, revalida Git y recupera solo lo faltante.
No cargues todos los destinos de un índice ni todo el TOML. Si no puedes identificar la
raíz y el alcance de escritura, detente antes de escribir.
