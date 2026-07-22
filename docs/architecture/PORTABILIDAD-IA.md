---
title: Portabilidad entre motores y modelos de IA
type: architecture
status: proposed
date: 2026-07-21
related:
  - "[[../decisions/ADR-0002-arnes-portable-de-ia]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
---

# Portabilidad entre motores y modelos de IA

## Dos cambios diferentes

- **Cambiar de interfaz**: Codex app a Codex CLI. Ambos pueden leer `AGENTS.md`, specs,
  pruebas y agentes del proyecto.
- **Cambiar de proveedor/modelo**: OpenAI/Codex a Kimi o una versión disponible de GLM. Puede
  requerir otro agente CLI porque los protocolos y herramientas no son idénticos.

La portabilidad garantizada está en los artefactos, no en que toda API acepte exactamente el
mismo cuerpo HTTP. Kimi y GLM se conservan como opciones futuras y su validación no es una
puerta obligatoria del proyecto.

## Matriz práctica

| Opción | Integración versionada | Configuración secreta | Invocación Spec Kit | Uso recomendado |
|---|---|---|---|---|
| Codex app | `AGENTS.md`, `.agents/skills`, `.codex/agents` | inicio de sesión del usuario | `$speckit-*` cuando la superficie exponga skills | principal con interfaz gráfica |
| Codex CLI | las mismas rutas | `~/.codex/`, fuera de Git | `$speckit-*` | principal en terminal y worktrees |
| Kimi Code + Kimi | `.agents/skills` | `/login` o config local | `/skill:speckit-*` | alternativa Kimi nativa |
| Kimi Code + GLM | `.agents/skills` | variables temporales o config local | `/skill:speckit-*` | alternativa GLM por Chat Completions |

## Comandos del repositorio

Linux/macOS o Git Bash:

```bash
./scripts/agent.sh codex
./scripts/agent.sh kimi
ZAI_API_KEY="..." GLM_MODEL="modelo-disponible" ./scripts/agent.sh glm
```

PowerShell:

```powershell
.\scripts\agent.ps1 codex
.\scripts\agent.ps1 kimi
$env:ZAI_API_KEY = "..."
$env:GLM_MODEL = "modelo-disponible"
.\scripts\agent.ps1 glm
```

El perfil `glm` usa Kimi Code como arnés y define temporalmente:

- proveedor `openai`;
- modelo indicado explícitamente mediante `GLM_MODEL`, sin versión obligatoria;
- endpoint de Coding Plan `https://api.z.ai/api/coding/paas/v4`;
- contexto máximo declarado de 1 000 000 tokens;
- capacidades de razonamiento y herramientas.

La clave nunca se imprime ni se escribe en el repositorio.

## Por qué no se configura GLM/Kimi dentro de `.codex/config.toml`

Codex exige que proveedores personalizados se configuren a nivel del usuario y actualmente
usa `responses` como protocolo soportado. Z.AI y Moonshot documentan principalmente
Chat Completions para estos endpoints. Un gateway puede traducir, pero introduce otra capa y
debe probarse antes de adoptarlo. Además, Codex ignora proveedores y credenciales definidos
en la configuración local del proyecto por seguridad.

Si en el futuro se necesita un único CLI para todos los modelos:

1. montar un gateway compatible con `/v1/responses` en entorno local;
2. probar tool calling, streaming, razonamiento y recuperación de errores;
3. ejecutar el smoke test completo;
4. registrar versión, configuración y resultados en un ADR;
5. solo entonces añadir un perfil de usuario de Codex, nunca claves al repo.

## Contrato que todos los motores deben respetar

- Leer `AGENTS.md`, constitución, sprint y feature activa.
- No aprobar requisitos ni decisiones.
- No implementar sin spec aprobada y tarea asignada.
- No hacer operaciones Git externas automáticamente.
- Ejecutar y reportar pruebas reales.
- Actualizar documentos solo en rutas autorizadas.
- Producir un diff revisable y evidencia enlazada.

## Prueba antes de cambiar

Si el tesista decide activar un motor alternativo, ejecuta `evals/providers/SMOKE-TEST.md`
con el motor y versión elegidos. El cambio se acepta solo si los casos críticos pasan y no
aparecen modificaciones fuera de alcance. Registra
fecha, modelo, CLI, latencia orientativa, fallos y diferencias; no compares únicamente la
calidad del texto generado.
