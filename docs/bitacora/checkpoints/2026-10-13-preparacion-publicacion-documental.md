---
title: Preparación de commits documentales separados
type: checkpoint
status: partially-complete
date: 2026-10-13
task_id: DOC-ORG-001
phase: pre_commit
commit: pending
branch: opencode/spec-001-fase-1-diseno
head: c2654519b041d8f96a2028482608c93ac9d8ea0b
module: transversal
sprint: transversal
related:
  - "[[../ESTADO-ACTIVO]]"
  - "[[../../evidence/requirements/2026-10-12-resumen-entrevista-temas-organizacionales]]"
  - "[[../../../documentacion/README]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/transversal
---

# Preparación de commits documentales separados

## Resultado real

Se actualizaron localmente las ediciones de documentacion/ y se copiaron al clon
independiente de Doc-Proj-ZhudAleli, rama main. El remoto documental se consultó vacío.
La carpeta pública contiene solo Markdown. .gitignore excluye documentacion/ del
repositorio general. Las nuevas ideas de entrevista conservan estado pendiente; el
catálogo canónico no se cambió. No hay commit ni push.

## Comprobaciones

| Comprobación | Resultado |
|---|---|
| Archivos documentales | 24 archivos Markdown; solo carpeta documental en el clon. |
| Copia local | 24 rutas y hashes SHA-256 coincidentes; cero faltantes y cero extras. |
| Trazabilidad | 51 RF, 9 RNF, 51 HU, 9 HT y 60 entradas de pila; IDs sin duplicados. |
| Enlaces locales | 0 enlaces rotos entre los documentos de documentacion/. |
| Formato | YAML básico, historial y espacios finales verificados en 24 archivos. |
| Economía | Escenarios condicionados; USD 15 por caso sigue supuesto y ahorro realizado no demostrado. |
| Git general | No se incluyen archivos de código, configuración de host ni documentacion/. |
| Git docente | No se incluyen analisis/, _archivo/, docs/, código, skills o agentes. |
| Revisión académica | Pendiente; no se atribuye aprobación de nuevas capacidades. |
| Commit y push | Pendientes de autorización específica. |

## Conjunto exacto propuesto para el repositorio general (38 archivos)

```text
_archivo/README.md
_archivo/registro.md
.gitignore
agents/tesis/OBSIDIAN_POLICY.md
analisis/2026-10-12/alcance/alcance_candidato_v1.0_2026-10-12.md
analisis/2026-10-12/alcance/alcance_candidato_v1.1_2026-10-12.md
analisis/2026-10-12/backlog/pila_producto_candidato_v1.0_2026-10-12.md
analisis/2026-10-12/backlog/pila_producto_candidato_v1.1_2026-10-12.md
analisis/2026-10-12/backlog/pila_producto_candidato_v1.2_2026-10-12.md
analisis/2026-10-12/entrevista/impacto-documental-candidato_v1.0_2026-10-12.md
analisis/2026-10-12/factibilidad/factibilidad_candidato_v1.0_2026-10-12.md
analisis/2026-10-12/factibilidad/factibilidad_candidato_v1.1_2026-10-12.md
analisis/2026-10-12/factibilidad/factibilidad_candidato_v1.2_2026-10-12.md
analisis/2026-10-12/factibilidad/factibilidad_candidato_v1.3_2026-10-12.md
analisis/2026-10-12/historias/datos_historias_usuario_v2.0_2026-10-12.psv
analisis/2026-10-12/historias/historias_tecnicas_candidato_v1.0_2026-10-12.md
analisis/2026-10-12/historias/historias_tecnicas_candidato_v1.1_2026-10-12.md
analisis/2026-10-12/historias/historias_tecnicas_candidato_v1.2_2026-10-12.md
analisis/2026-10-12/historias/historias_tecnicas_candidato_v1.3_2026-10-12.md
analisis/2026-10-12/historias/historias_usuario_candidato_v1.0_2026-10-12.md
analisis/2026-10-12/historias/historias_usuario_candidato_v2.0_2026-10-12.md
analisis/2026-10-12/historias/historias_usuario_candidato_v2.1_2026-10-12.md
analisis/2026-10-12/historias/historias_usuario_candidato_v2.2_2026-10-12.md
analisis/2026-10-12/requisitos/priorizacion_requisitos_candidato_v1.0_2026-10-12.md
analisis/2026-10-12/requisitos/priorizacion_requisitos_candidato_v1.1_2026-10-12.md
analisis/2026-10-12/requisitos/requisitos_funcionales_candidato_v1.0_2026-10-12.md
analisis/2026-10-12/requisitos/requisitos_funcionales_candidato_v1.1_2026-10-12.md
analisis/2026-10-12/requisitos/requisitos_no_funcionales_candidato_v1.0_2026-10-12.md
analisis/2026-10-12/requisitos/requisitos_no_funcionales_candidato_v1.1_2026-10-12.md
analisis/README.md
docs/00-inicio/moc-documentacion.md
docs/bitacora/checkpoints/2026-10-12-impacto-entrevista-documental.md
docs/bitacora/checkpoints/2026-10-12-inicio-organizacion-documental.md
docs/bitacora/checkpoints/2026-10-13-preparacion-publicacion-documental.md
docs/bitacora/ESTADO-ACTIVO.md
docs/context/context-index.md
docs/evidence/requirements/2026-10-12-resumen-entrevista-temas-organizacionales.md
docs/requirements/proposals/2026-10-12-temas-entrevista-para-validacion.md
```

Mensaje propuesto: docs: registrar análisis de entrevista y separar publicación documental.

## Conjunto exacto propuesto para el repositorio del docente (24 archivos)

```text
alcance/alcance_v1.0_2026-10-12.md
alcance/alcance_v1.1_2026-10-12.md
arquitectura/arquitectura_v1.0_2026-10-12.md
control_de_cambios/registro_v1.0_2026-10-12.md
control_de_cambios/registro_v1.1_2026-10-12.md
control_de_cambios/registro_v1.2_2026-10-12.md
control_de_cambios/registro_v1.3_2026-10-12.md
control_de_cambios/registro_v1.4_2026-10-12.md
control_de_cambios/registro_v2.0_2026-10-12.md
diseno/criterios_diseno_v1.0_2026-10-12.md
factibilidad/factibilidad_v1.3_2026-10-12.md
historias/tecnicas/historias_tecnicas_v1.3_2026-10-12.md
historias/usuario/historias_usuario_v1.0_2026-10-12.md
historias/usuario/historias_usuario_v2.2_2026-10-12.md
levantamiento/registro_entrevista_v1.0_2026-10-12.md
pila_producto/pila_producto_v1.2_2026-10-12.md
pruebas/plan_pruebas_v1.0_2026-10-12.md
README.md
requisitos/funcionales/requisitos_funcionales_v1.0_2026-10-12.md
requisitos/funcionales/requisitos_funcionales_v1.1_2026-10-12.md
requisitos/no_funcionales/requisitos_no_funcionales_v1.0_2026-10-12.md
requisitos/no_funcionales/requisitos_no_funcionales_v1.1_2026-10-12.md
requisitos/priorizacion/priorizacion_requisitos_v1.1_2026-10-12.md
sprints/plan_sprints_v1.0_2026-10-12.md
```

Mensaje propuesto: docs: publicar línea base y planificación de Zhud Alelí.

## Próximo paso

El tesista revisa ambos conjuntos y autoriza por separado el commit del repositorio
general, el commit documental y el push del repositorio documental. Después de cada
commit se registra el hash real y se verifica el estado remoto antes de declarar
publicación. Las decisiones P-03, alcance ampliado, estimación y revisión de la
directora continúan pendientes.