---
title: "Agente — Redactor documental del vault"
canonical_id: documenter
type: agent
kind: host-role
status: active
sandbox: workspace-write-limited
tags:
  - proyecto/tesis
  - tipo/agente
  - estado/activo
verified_at: "2026-08-24"
verification_scope: "working-tree"
source_path: ".codex/agents/documenter.toml"
---

# Agente — Redactor documental del vault

## Propósito

Registrar de forma estructurada el trabajo realizado después de una implementación y revisión, manteniendo la trazabilidad entre tarea, pruebas, commit y evidencia.

## Hosts permitidos

- Codex.
- Kimi.

Gemini puede ser el modelo de redacción del documenter mediante el laboratorio/puente
configurado. No es el host ni posee los permisos del agente: Codex o Kimi coordinan el flujo,
y `git-manager` controla Git.

## Disparador

```text
implementación → pruebas → revisión → documenter → git-manager → documenter post_commit
```

## Entradas

- Handoff estructurado del coordinador.
- Tarea, requisito, spec y sprint relacionados.
- Archivos modificados y diff revisado.
- Comandos y resultados reales.
- Hallazgos del reviewer.
- Hash del commit, únicamente en fase `post_commit`.

## Salidas

### Fase `pre_commit`

- Resumen de sesión.
- Checkpoint de trabajo.
- Registro con `commit: pending`.

### Fase `post_commit`

- Evidencia de implementación.
- Hash real, rama, archivos y pruebas.
- Enlaces hacia tarea, spec, requisitos y checkpoint.

## Rutas permitidas

- `docs/bitacora/sesiones/`
- `docs/bitacora/checkpoints/`
- `docs/evidence/`
- `docs/requirements/proposals/`
- `docs/decisions/proposals/`

## Rutas protegidas

No modifica dashboard, matriz, roadmap, specs aprobadas, requisitos confirmados, ADR aceptados, código, configuración ni políticas.

## Dependencias

- [[AGENTS]]
- [[../../agents/tesis/OBSIDIAN_POLICY|OBSIDIAN_POLICY]]
- [[FLUJO-MULTIAGENTE]]
- [[agente-git-manager]]

## Ubicación real

- Configuración: `.codex/agents/documenter.toml`.
- Nota: `docs/01-agentes/agente-documenter.md`.
