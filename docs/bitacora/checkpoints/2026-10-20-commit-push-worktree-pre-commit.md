---
title: Commit y push del conjunto acumulado del proyecto — pre-commit
type: checkpoint
status: ready-for-commit
date: 2026-10-20
task_id: DOC-ORG-001
phase: pre_commit
commit: pending
branch: docs/requisitos-y-organizacion-del-vault
upstream: origin/docs/requisitos-y-organizacion-del-vault
base_head: 5ccbe09dda2ebf435e979888e64c6b9dbdc4b1db
files_count: 182
excluded_local_items:
  - .codex/config.toml (ruta absoluta del equipo; no portable)
  - tmp/** (artefactos temporales)
  - _codex_tmp_lib_image_20261020_2/** (payloads/auxiliares temporales)
  - _archivo/2026-10-13/office-locks/** (bloqueo temporal de Office)
  - Abrir cronograma de sprints.lnk (acceso directo local)
---

# Handoff pre-commit

## Autorización y alcance

El tesista solicitó expresamente hacer commit y push de todos los cambios del workspace.
Se prepararon 182 archivos: los 181 cambios de proyecto revisados y este handoff. Se excluyeron únicamente los elementos locales enumerados arriba. La publicación se hará a la rama actual y su upstream, sin force-push.

## Base y revisión

| Comprobación | Resultado |
|---|---|
| Rama / upstream | `docs/requisitos-y-organizacion-del-vault` / `origin/docs/requisitos-y-organizacion-del-vault`. |
| HEAD antes del commit | `5ccbe09dda2ebf435e979888e64c6b9dbdc4b1db`; alineado con upstream al iniciar la revisión. |
| Archivos staged | 182; el listado exacto está abajo. |
| Secretos y bases locales | La búsqueda heurística no detectó credenciales ni bases locales en el conjunto. Se excluyeron configuración local y payloads temporales. |
| Datos personales | No se detectaron teléfonos, cédulas ni correos en los documentos revisados; los nombres y roles del reporte S1 se conservaron como atribución entregada por el tesista. |
| `git diff --cached --check` | Detecta seis líneas con espacio final: `cronograma-interactivo/cronograma_interactivo_v2.0_2026-10-20.html` (líneas 67 y 233), `design/style-guide/components/layout.html` (líneas 38 y 67) y `design/style-guide/tokens.html` (líneas 19 y 75). También detecta líneas vacías finales adicionales en `analisis/2026-10-13/alcances-modulos/README.md`, los candidatos de requisitos v2.0, v2.1 y v2.2, y `analisis/2026-10-19/arquitectura/arquitectura_candidato_v1.1_2026-10-19.md`. Se conservan los artefactos recibidos y se registra el hallazgo para su corrección posterior. |
| Pruebas de aplicación | No ejecutadas: esta revisión prepara la publicación de cambios acumulados, sin petición de ejecutar pruebas. |
| Commit y push | Pendientes; no se afirma publicación hasta verificar los resultados reales. |

## Archivos incluidos

```text
.gitignore
.obsidian/graph.json
.specify/memory/constitution.md
.specify/templates/overrides/README.md
.specify/templates/overrides/constitution-template.md
.specify/templates/overrides/plan-template.md
.specify/templates/overrides/spec-template.md
.specify/templates/overrides/tasks-template.md
.specify/templates/plan-template.md
.specify/templates/spec-template.md
.specify/templates/tasks-template.md
AGENTS.md
README.md
_archivo/2026-10-13/diagramas-procesos/README.md
_archivo/2026-10-13/diagramas-procesos/ZA-CU-003-diagramas-generales-por-proceso-v1.0-2026-10-13.docx
_archivo/2026-10-13/diagramas-procesos/ZA-CU-003-diagramas-generales-por-proceso-v1.0-2026-10-13.md
_archivo/registro.md
agents/tesis/OBSIDIAN_POLICY.md
agents/tesis/PROJECT_CONTEXT.md
analisis/2026-10-12/entrevista/impacto-documental-candidato_v1.1_2026-10-13.md
analisis/2026-10-13/README.md
analisis/2026-10-13/alcances-modulos/Formato Corregido.docx
analisis/2026-10-13/alcances-modulos/README.md
analisis/2026-10-13/alcances-modulos/ZA-ALC-001-acceso-usuarias-y-roles-v1.0-2026-10-13.docx
analisis/2026-10-13/alcances-modulos/ZA-ALC-001-acceso-usuarias-y-roles-v1.0-2026-10-13.md
analisis/2026-10-13/alcances-modulos/ZA-ALC-001-acceso-usuarias-y-roles-v1.1-2026-10-13.docx
analisis/2026-10-13/alcances-modulos/ZA-ALC-001-acceso-usuarias-y-roles-v1.1-2026-10-13.md
analisis/2026-10-13/alcances-modulos/ZA-ALC-002-asistencia-y-participacion-v1.0-2026-10-13.docx
analisis/2026-10-13/alcances-modulos/ZA-ALC-002-asistencia-y-participacion-v1.0-2026-10-13.md
analisis/2026-10-13/alcances-modulos/ZA-ALC-002-asistencia-y-participacion-v1.1-2026-10-13.docx
analisis/2026-10-13/alcances-modulos/ZA-ALC-002-asistencia-y-participacion-v1.1-2026-10-13.md
analisis/2026-10-13/alcances-modulos/ZA-ALC-003-planificacion-de-actividades-v1.0-2026-10-13.docx
analisis/2026-10-13/alcances-modulos/ZA-ALC-003-planificacion-de-actividades-v1.0-2026-10-13.md
analisis/2026-10-13/alcances-modulos/ZA-ALC-003-planificacion-de-actividades-v1.1-2026-10-13.docx
analisis/2026-10-13/alcances-modulos/ZA-ALC-003-planificacion-de-actividades-v1.1-2026-10-13.md
analisis/2026-10-13/alcances-modulos/artifact.md
analisis/2026-10-13/alcances-modulos/build_scope_docx.py
analisis/2026-10-13/casos-uso/ZA-CU-001-acceso-usuarias-y-roles-v1.0-2026-10-13.docx
analisis/2026-10-13/casos-uso/ZA-CU-001-acceso-usuarias-y-roles-v1.0-2026-10-13.md
analisis/2026-10-13/casos-uso/ZA-CU-002-asistencia-y-participacion-v1.0-2026-10-13.docx
analisis/2026-10-13/casos-uso/ZA-CU-002-asistencia-y-participacion-v1.0-2026-10-13.md
analisis/2026-10-13/casos-uso/ZA-CU-002-asistencia-y-participacion-v1.1-2026-10-13.docx
analisis/2026-10-13/casos-uso/ZA-CU-002-asistencia-y-participacion-v1.1-2026-10-13.md
analisis/2026-10-13/casos-uso/ZA-CU-002-asistencia-y-participacion-v1.2-2026-10-13.docx
analisis/2026-10-13/casos-uso/ZA-CU-002-asistencia-y-participacion-v1.2-2026-10-13.md
analisis/2026-10-13/casos-uso/ZA-CU-002-asistencia-y-participacion-v1.3-2026-10-13.docx
analisis/2026-10-13/casos-uso/ZA-CU-002-asistencia-y-participacion-v1.3-2026-10-13.md
analisis/2026-10-13/casos-uso/ZA-CU-004-planificacion-de-actividades-v1.0-2026-10-13.docx
analisis/2026-10-13/casos-uso/ZA-CU-004-planificacion-de-actividades-v1.0-2026-10-13.md
analisis/2026-10-13/casos-uso/ZA-CU-004-planificacion-de-actividades-v1.1-2026-10-13.docx
analisis/2026-10-13/casos-uso/ZA-CU-004-planificacion-de-actividades-v1.1-2026-10-13.md
analisis/2026-10-13/casos-uso/figuras/ZA-CU-ASI-diagrama-faltas-multas.png
analisis/2026-10-13/casos-uso/figuras/ZA-CU-ASI-diagrama-faltas-multas.svg
analisis/2026-10-13/casos-uso/figuras/ZA-CU-ASI-diagrama-registro-consulta.png
analisis/2026-10-13/casos-uso/figuras/ZA-CU-ASI-diagrama-registro-consulta.svg
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-001-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-002-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-003-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-004-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-005-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-006-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-007-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-008-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-asi-009-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-pla-001-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-pla-002-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-pla-003-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-pla-004-flujo.png
analisis/2026-10-13/casos-uso/figuras/za-cu-pla-005-flujo.png
analisis/2026-10-13/diagramas-procesos/ZA-DG-001-diagramas-generales-por-proceso-v1.1-2026-10-13.docx
analisis/2026-10-13/diagramas-procesos/ZA-DG-001-diagramas-generales-por-proceso-v1.1-2026-10-13.md
analisis/2026-10-13/diagramas-procesos/figuras/za-dg-01-acceso-membresias-y-permisos.png
analisis/2026-10-13/diagramas-procesos/figuras/za-dg-02-planificacion-de-actividades-y-encargos.png
analisis/2026-10-13/diagramas-procesos/figuras/za-dg-03-produccion-y-trazabilidad.png
analisis/2026-10-13/diagramas-procesos/figuras/za-dg-04-inventario-entregas-y-conciliacion-fisica.png
analisis/2026-10-13/diagramas-procesos/figuras/za-dg-05-ventas-tesoreria-y-rendicion.png
analisis/2026-10-13/diagramas-procesos/figuras/za-dg-06-reportes-recordatorios-y-sitio-público.png
analisis/2026-10-13/diagramas-procesos/figuras/za-dg-07-gestion-documental-y-activos.png
analisis/2026-10-13/diagramas-procesos/figuras/za-dg-08-continuidad-y-sincronizacion-sin-conexion.png
analisis/2026-10-13/fichas-separadas/generar_markdown.py
analisis/2026-10-13/fichas-separadas/generar_word.py
analisis/2026-10-13/fichas-separadas/verificar_fichas.py
analisis/2026-10-13/formato-historias-docx/build_historias.py
analisis/2026-10-13/gantt-interactivo/README-movido.txt
analisis/2026-10-13/historias-modulo-acceso/ZA-HU-001-a-004-acceso-usuarias-roles-v1.0-2026-10-13.md
analisis/2026-10-13/orden-tablas/build_plan_backlog_v1_3.py
analisis/2026-10-13/orden-tablas/reordenar_historias_y_sprints.py
analisis/2026-10-13/orden-tablas/verificar_edicion.py
analisis/2026-10-13/plan-incremental-docx/build_plan.py
analisis/2026-10-13/plan-incremental-docx/build_plan_v1_1.py
analisis/2026-10-13/requisitos/requisitos_generales_candidato_v2.0_2026-10-13.md
analisis/2026-10-13/requisitos/requisitos_generales_candidato_v2.1_2026-10-13.md
analisis/2026-10-13/requisitos/requisitos_generales_candidato_v2.2_2026-10-13.md
analisis/2026-10-13/sprint-backlog/build_plan_backlog_docx.py
analisis/2026-10-13/sprint-backlog/renumerar_fuentes.py
analisis/2026-10-19/arquitectura/arquitectura_candidato_v1.1_2026-10-19.md
cronograma-interactivo/README.md
cronograma-interactivo/cronograma_interactivo_v1.0_2026-10-13.html
cronograma-interactivo/cronograma_interactivo_v1.1_2026-10-13.html
cronograma-interactivo/cronograma_interactivo_v2.0_2026-10-20.html
cronograma-interactivo/cronograma_interactivo_v3.0_2026-10-20.html
cronograma-interactivo/cronograma_interactivo_v4.0_2026-10-20.html
cronograma-interactivo/cronograma_interactivo_v5.0_2026-10-20.html
cronograma-interactivo/dashboard_template.html
cronograma-interactivo/generar_dashboard.py
cronograma-interactivo/generar_gantt.py
cronograma-interactivo/index.html
cronograma-interactivo/plantilla.html
cronograma-interactivo/proyecto-local/Abrir cronograma.cmd
cronograma-interactivo/proyecto-local/README.md
cronograma-interactivo/proyecto-local/servidor.py
cronograma-interactivo/proyecto-local/verificar_proyecto.mjs
cronograma-interactivo/proyecto-local/web/assets/app.js
cronograma-interactivo/proyecto-local/web/assets/interaction.css
cronograma-interactivo/proyecto-local/web/assets/styles.css
cronograma-interactivo/proyecto-local/web/datos-proyecto.json
cronograma-interactivo/proyecto-local/web/index.html
cronograma-interactivo/proyecto-local/web/recursos-sprints.json
cronograma-interactivo/verificar_dashboard.mjs
cronograma-interactivo/verificar_gantt.mjs
cronograma-interactivo/vista-escritorio.png
cronograma-interactivo/vista-movil.png
design/style-guide/DESIGN-SYSTEM-SPEC.md
design/style-guide/components/badges.html
design/style-guide/components/buttons.html
design/style-guide/components/cards.html
design/style-guide/components/feedback.html
design/style-guide/components/forms.html
design/style-guide/components/layout.html
design/style-guide/components/modals.html
design/style-guide/components/navigation.html
design/style-guide/components/table.html
design/style-guide/index.html
design/style-guide/style.css
design/style-guide/tokens.html
docs/00-inicio/00-dashboard.md
docs/00-inicio/moc-documentacion.md
docs/architecture/ARQUITECTURA-OBJETIVO.md
docs/architecture/PLAN-DESDE-CERO.md
docs/bitacora/ESTADO-ACTIVO.md
docs/bitacora/checkpoints/2026-10-07-alternativas-entrega-incremental.md
docs/bitacora/checkpoints/2026-10-07-revision-arquitectura-monolito-capas.md
docs/bitacora/checkpoints/2026-10-08-aceptacion-monolito-modular.md
docs/bitacora/checkpoints/2026-10-08-evolucion-modular-y-versiones-piloto.md
docs/bitacora/checkpoints/2026-10-13-correccion-autoria-word-pre-commit.md
docs/bitacora/checkpoints/2026-10-13-fichas-historias-sprints-pre-commit.md
docs/bitacora/checkpoints/2026-10-13-gantt-archivo-local-pre-commit.md
docs/bitacora/checkpoints/2026-10-13-gantt-interactivo-pre-commit.md
docs/bitacora/checkpoints/2026-10-13-proyecto-gantt-local-pre-commit.md
docs/bitacora/checkpoints/2026-10-13-publicacion-documental-verificada.md
docs/bitacora/checkpoints/2026-10-13-resumen-tablas-sprint-backlog-pre-commit.md
docs/bitacora/checkpoints/2026-10-13-sprint-backlog-documental-pre-commit.md
docs/bitacora/checkpoints/2026-10-13-tablas-prioridades-documentales-pre-commit.md
docs/bitacora/checkpoints/2026-10-14-publicacion-compendios-post-commit.md
docs/bitacora/checkpoints/2026-10-14-publicacion-compendios-pre-commit.md
docs/bitacora/checkpoints/2026-10-14-publicacion-requisitos-v2.0-post-commit.md
docs/bitacora/checkpoints/2026-10-14-publicacion-requisitos-v2.0-pre-commit.md
docs/bitacora/checkpoints/2026-10-18-cierre-sesion-pendientes.md
docs/bitacora/checkpoints/2026-10-18-verificacion-cierre-sprint-0.md
docs/bitacora/checkpoints/2026-10-19-edicion-docente-seguimiento.md
docs/bitacora/checkpoints/2026-10-20-cierre-sprint-1-parcial.md
docs/bitacora/checkpoints/2026-10-20-reconciliacion-gantt-sprint-1.md
docs/context/context-index.md
docs/context/feature-index.md
docs/decisions/ADR-0006-monolito-modular-y-entrega-incremental.md
docs/decisions/ADR-0007-autoridad-del-tesista-para-cierre-de-sprints.md
docs/decisions/proposals/2026-09-22-arquitectura-modular-desacoplada.md
docs/decisions/proposals/2026-10-07-alternativas-arquitectura-entrega-incremental.md
docs/decisions/proposals/2026-10-07-monolito-modular-con-capas.md
docs/decisions/proposals/2026-10-08-evolucion-modular-y-versiones-piloto.md
docs/evidence/architecture/2026-10-07-alternativas-entrega-incremental.md
docs/evidence/architecture/2026-10-07-revision-monolito-capas.md
docs/evidence/architecture/2026-10-08-aceptacion-monolito-modular.md
docs/evidence/architecture/2026-10-08-evolucion-modular-y-versiones-piloto.md
docs/evidence/requirements/2026-10-13-aprobacion-propuesta-requisitos-generales-v2-2.md
docs/evidence/requirements/2026-10-13-reporte-revision-docente-en-clase.md
docs/evidence/requirements/2026-10-20-reporte-aprobaciones-verbales-s1.md
docs/requirements/CAT-REQ-001-v1.1.md
docs/requirements/CAT-REQ-001.md
docs/requirements/proposals/2026-10-13-pro-ent-001-v0.2.md
docs/traceability/MATRIZ-TRAZABILIDAD.md
docs/bitacora/checkpoints/2026-10-20-commit-push-worktree-pre-commit.md
```

## Commit propuesto

Mensaje: `chore: consolidate thesis project artifacts`

Comando de publicación: `git push origin docs/requisitos-y-organizacion-del-vault`.
