---
title: Rutas universales de hosts, proveedores y modelos
type: architecture
status: proposed
date: 2026-08-24
related:
  - "[[CONTRATO-UNIVERSAL-ORQUESTADORES]]"
  - "[[../bitacora/ESTADO-ACTIVO]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
---

# Rutas universales de hosts, proveedores y modelos

La configuración ejecutable está en `tools/agent-routes.toml`. Esta nota explica la política
para el tesista y para los hosts.

## Ruta por rol

| Rol | Primario | Fallback manual | Motivo |
|---|---|---|---|
| `coordinator` | Codex | Antigravity + Gemini Pro | Mantener gobierno y decisiones en el host de referencia |
| `requirements` | Codex | Antigravity + `gemini-3.7-flash` | Contrastar fuentes y mantener trazabilidad |
| `architect` | Antigravity + `gemini-3.1-pro` | Codex | Análisis profundo aprovechando Google AI Pro |
| `ux` | Antigravity + `gemini-3.5-flash` | Codex | Revisar recorridos y accesibilidad |
| `implementer` | OpenChamber + OpenCode Go + `deepseek-v4` | Antigravity + `gemini-3.6-flash` | Código rutinario con el menor costo disponible |
| `reviewer` | Codex | Antigravity + `gemini-3.1-pro` | Revisión independiente y control de riesgos |
| `documenter` | Antigravity + `gemini-3.1-pro` | Codex | Redacción del vault usando la cuota disponible |
| `git-manager` | Codex | OpenCode con autorización | La puerta de commit permanece humana |

## Reglas de uso

1. La ruta indica una preferencia, no una autorización para cambiar alcance.
2. El fallback se activa manualmente después de registrar un handoff `partially-complete`.
3. El host siguiente debe conservar la tarea, branch/worktree, rutas y pruebas originales.
4. `opencode-go/<modelo>` identifica una ruta de OpenCode Go; para este proyecto se propone
   `deepseek-v4`, pero debe confirmarse que aparezca en el catálogo de OpenCode Go antes de
   ejecutarlo. No se sustituye por un proveedor OpenAI sin verificar autenticación y endpoint.
5. Antigravity puede mostrar variantes locales con nivel de esfuerzo; esas variantes no se
   versionan como IDs universales ni se reutilizan como prueba de acceso a la API de Google.
6. Los IDs Gemini universales confirmados para este proyecto son `gemini-3.7-flash`,
   `gemini-3.6-flash`, `gemini-3.5-flash` y `gemini-3.1-pro`. Si la herramienta no muestra uno
   de ellos o requiere un alias local, se detiene y se registra el bloqueo; no se inventa un
   alias.

## Qué ocurre al cambiar de cuota

El cambio es a nivel de tarea:

```text
error de cuota → detener host → handoff → abrir ruta fallback → leer handoff → continuar
```

No se promete failover invisible de una conversación porque Codex, Antigravity y OpenCode Go
gestionan autenticación, sesiones y límites por superficies distintas. La continuidad real
proviene de los archivos versionados del vault.
