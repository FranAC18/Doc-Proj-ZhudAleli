---
title: Índice de análisis y artefactos del 13 de octubre de 2026
type: index
status: active
date: 2026-10-13
tags:
  - proyecto/tesis
  - tipo/analisis
  - estado/activo
---

# Análisis y artefactos del 13 de octubre de 2026

Esta carpeta agrupa el trabajo interno de esa fecha por tema. Los scripts y archivos
de origen están junto a sus resultados; las carpetas `render/` guardan vistas de
control y no son documentos finales para el docente.

| Carpeta | Contenido | Archivo de entrada o referencia |
|---|---|---|
| `fichas-separadas/` | Generadores, verificaciones y renders de fichas de historias, sprints y tareas. | `generar_markdown.py`, `generar_word.py`, `verificar_fichas.py` |
| `formato-historias-docx/` | Comparación visual del formato de historias Word y sus versiones. | [Contrato de formato](formato-historias-docx/contrato-formato-historias.md), `build_historias.py` |
| `gantt-interactivo/` | Cronograma interactivo, generador, verificador, capturas y copia del proyecto local. | [README del cronograma](gantt-interactivo/README.md) |
| `alcances-modulos/` | Carpeta única de alcances modulares, plantilla, versiones históricas y estado vigente por sprint. | [Índice de alcances modulares](alcances-modulos/README.md) |
| `casos-uso/` | Casos de uso detallados, trazabilidad y diagramas de flujo por proceso. | Documentos ZA-CU por módulo; consultar el índice de alcances. |
| `diagramas-procesos/` | Catálogo visual general de procesos. | [ZA-DG-001](diagramas-procesos/ZA-DG-001-diagramas-generales-por-proceso-v1.1-2026-10-13.md) |
| `orden-tablas/` | Scripts, verificaciones y renders de tablas reordenadas. | `reordenar_historias_y_sprints.py`, `build_plan_backlog_v1_3.py`, `verificar_edicion.py` |
| `plan-incremental-docx/` | Iteraciones del plan incremental en Word, PDFs y renders de revisión. | [Contrato de formato](plan-incremental-docx/contrato-formato-plan-incremental.md), `build_plan.py`, `build_plan_v1_1.py` |
| `sprint-backlog/` | Generación y revisión visual del documento de sprint backlog. | `build_plan_backlog_docx.py`, `renumerar_fuentes.py` |

## Cómo orientarse

- Para el cronograma interactivo, empezar por su README; `index.html` es la vista local.
- Para conocer la edición final vigente, consultar el [índice de documentación final](../../documentacion/README.md).
- Los PDF y PNG de estas carpetas son material interno de revisión. Su presencia por sí sola
  no indica que sean versiones finales ni que puedan eliminarse.
- Las carpetas vacías llamadas `render` son destinos de salida de los scripts. Se conservan
  mientras no se confirme que ningún flujo las necesita.

## Revisión de vacíos

El 2026-10-13 se revisaron los archivos Markdown de `documentacion/`, `analisis/` y
`_archivo/`: no se encontraron documentos vacíos. No se eliminó ningún archivo. Los
archivos de dependencias y entornos locales quedan fuera de esta revisión documental.
