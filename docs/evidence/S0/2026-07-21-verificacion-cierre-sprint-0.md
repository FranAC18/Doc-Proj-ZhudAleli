---
title: Verificación final para cerrar Sprint 0
type: evidence
status: completed
date: 2026-07-21
sprint: S0
module: transversal
tester: tesista y Codex
related:
  - "[[../../sprints/SPRINT-00-preparacion]]"
  - "[[2026-07-21-smoke-test-codex]]"
  - "[[2026-07-21-verificacion-base-v3]]"
tags:
  - proyecto/tesis
  - tipo/evidencia
  - sprint/s0
  - modulo/transversal
---

# Verificación final para cerrar Sprint 0

## Entorno

| Elemento | Resultado |
|---|---|
| Carpeta definitiva | `F:\Tesis\App Tesis` |
| Sistema | Windows, PowerShell |
| Python | 3.12.2 del sistema; 3.12.13 resuelto por `uv` |
| Git | 2.52.0.windows.1 |
| uv | 0.10.9 |
| Codex CLI | 0.145.0 |
| Aplicación Django | No existe; `manage.py`, settings y apps de negocio ausentes |

## Resultados técnicos

| Verificación | Comando o procedimiento | Resultado |
|---|---|---|
| Laboratorio aislado | `uv run --extra dev pytest -q` en `tools/agent-lab` | `10 passed in 0.27s` |
| PowerShell | parser de `System.Management.Automation` | 0 errores |
| Ayuda del lanzador | `powershell -ExecutionPolicy Bypass -File scripts/agent.ps1 help` | correcta; GLM se muestra opcional |
| Script Bash | Git Bash con `bash -n scripts/agent.sh` | sintaxis correcta |
| TOML | `tomllib` sobre configuraciones del proyecto | correcto |
| JSON versionado | `ConvertFrom-Json` | 0 errores |
| Enlaces del dashboard | resolución de 28 Wikilinks | 28 válidos, 0 rotos |
| Constitución | existencia de `.specify/memory/constitution.md` | presente; se consulta desde VS Code |
| Archivos sensibles | búsqueda de `.env`, bases, certificados y claves | 0 archivos sensibles, 0 patrones de secreto |
| Datos personales | búsqueda de correos reales y números de 10 dígitos | 0 coincidencias después de anonimizar ejemplos |
| Espacios | revisión de archivos de texto versionables | 0 espacios finales |
| Modelo GLM fijo | búsqueda de `GLM-5.2`/`glm-5.2` | 0 referencias obligatorias |

Tres Wikilinks ilustrativos de `ESTADOS-Y-PROGRESO.md` apuntan a nombres ficticios dentro de
un bloque de ejemplo YAML; no son enlaces de navegación ni se consideran rotos. Los 28
enlaces reales del dashboard sí fueron comprobados.

La auditoría detectó una copia heredada del arnés en `src/`, `tests/` y el `pyproject.toml`
de la raíz. Esa copia superó 6 pruebas antes de retirarse, pero contradecía
`MIGRACION-V2-A-V3.md`. La versión conservada y canónica es `tools/agent-lab/`, con 10 pruebas
aprobadas. La raíz queda libre para la futura aplicación Django, que aún no se crea.

## Validaciones humanas ya registradas

- [x] El tesista abrió la raíz como vault de Obsidian y abrió el dashboard.
- [x] Los enlaces principales funcionan.
- [x] La carpeta oculta `.specify` no aparece en Obsidian; la Constitución se abre desde VS
      Code y el dashboard documenta esa ruta.
- [x] El anteproyecto original se conserva fuera del repositorio.
- [x] Constitución y ADR-0002 fueron aceptados.
- [x] D-001 a D-010 fueron revisadas y confirmadas en el nivel funcional indicado.
- [x] Kimi y GLM quedaron como alternativas opcionales sin costo obligatorio.

## Estado de Git y autorización

La auditoría se realizó sobre `main` antes del primer commit. El tesista autorizó crear la
línea base inicial con el mensaje `chore: close sprint 0 preparation`. Esta autorización no
incluye `push`, `merge`, rebase ni publicación remota.

Sprint 0 queda aprobado y cerrado. Django y PostgreSQL continúan ausentes y fuera del alcance
de este cierre; se incorporarán únicamente después de las puertas de requisitos y diseño.
