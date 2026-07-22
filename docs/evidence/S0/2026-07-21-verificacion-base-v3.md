---
title: Verificación de la base portable v3
type: evidence
status: completed
date: 2026-07-21
sprint: S0
module: transversal
tags:
  - proyecto/tesis
  - tipo/evidencia
  - sprint/s0
---

# Verificación de la base portable v3

## Resultados ejecutados

| Verificación | Resultado |
|---|---|
| Laboratorio Python en entorno aislado | `10 passed in 0.16s` |
| Spec Kit 0.13.2 | `Integration status: OK` |
| Integraciones instaladas | Solo `codex`; multi-install seguro |
| Plantillas activas | Las cinco resuelven desde `.specify/templates/overrides/` |
| TOML de `.codex/` y laboratorio | Parseado correctamente con `tomllib` |
| Sintaxis de `scripts/agent.sh` | Correcta con `bash -n` |
| Módulo `python -m agent_harness.cli --help` | Ejecuta después de instalar dependencias |
| Artefactos generados en la entrega | No se encontraron cachés, `*.pyc` ni `*.egg-info` |
| Archivos sensibles | No se encontraron `.env`, SQLite, DB o patrones de clave revisados |
| Espacios/fin de archivo | Sin errores en `git diff --no-index --check` |

## No verificado todavía

- `scripts/agent.ps1`, porque el entorno de verificación no dispone de PowerShell.
- Inicio real de Codex con credenciales del tesista queda pendiente como verificación
  obligatoria del entorno final.
- Descubrimiento y ejecución de skills dentro de Kimi/GLM en la máquina final quedan como
  validaciones opcionales y no bloquean el cierre de Sprint 0.
- Apertura del vault y funcionamiento de enlaces en la instalación de Obsidian del tesista.
- CI dentro del repositorio GitHub, porque esta entrega no hace `push`.

La verificación obligatoria debe ejecutarse en el entorno final antes del cierre. Las pruebas
con Kimi/GLM solo se registrarán si el tesista decide realizarlas y cuenta con acceso sin
costo adicional.
