---
title: Recuperación selectiva de contexto y memoria del vault
type: checkpoint
status: completed
date: 2026-10-29
task_id: DOC-CTX-20261029
requirement_ids: []
sprint: S2
module: transversal
repository: ZhudAleli
phase: pre_commit
writer: codex
branch: docs/requisitos-y-organizacion-del-vault
head: dbd0e2207972715ebaf2b7ef2b67f6af63feb6e9
commit: pending
related:
  - "[[../ESTADO-ACTIVO]]"
  - "[[../../context/context-index]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/transversal
---

# Recuperación selectiva de contexto y memoria del vault

Solicitud del tesista: «modifica lo necesario para ahorrarnos tokens», y explicar
la memoria/documentación de Obsidian. Trabajo de documentación y configuración de
contexto; conserva la tarea de producto SB-S2-02 y los cambios locales previos.

## Resultado

- Estado activo reducido de 595 a 69 líneas; alcance de escritura separado en
  [alcance-activo.yaml](../alcance-activo.yaml), obligatorio antes de escribir.
- Primera medición del estado e índice: 43.534 → 7.772 bytes UTF-8 (82,1 % menos). Es una medida del texto
  de esos dos archivos, no una medición de tokens, caché, cuota o coste por tarea.
  En tareas de escritura se suma la lectura necesaria del archivo de alcance.
- AGENTS, skill de contexto, regla de Antigravity y routing de OpenCode piden fuentes
  por tarea y reutilización de lecturas vigentes, sin cargar todo el historial.
- Política Obsidian, skill/plantilla de handoff y adaptador Codex de documenter evitan
  resúmenes duplicados y cargas generales de documentos ajenos al registro.
- No cambia el modelo del host ni se configura una memoria semántica. Obsidian muestra
  y enlaza los archivos del vault; los agentes recuperan el contexto necesario.

## Conservación y límites

El estado y el índice previos se conservaron completos, antes de editarlos, en
[contexto-previo](2026-10-29-contexto-previo/ESTADO-ACTIVO.md) y su
[índice](2026-10-29-contexto-previo/context-index.md). Motivo: retirar del arranque el
relato histórico y las versiones repetidas. Origen: `docs/bitacora/ESTADO-ACTIVO.md` y
`docs/context/context-index.md`; reemplazo: las versiones breves en esas mismas rutas.
Sus enlaces relativos describen la ubicación de origen; los snapshots no son entradas
vigentes. [Métricas y hashes](2026-10-29-contexto-previo/metricas.json) identifican las
copias exactas. Las rutas previas se conservan sin retirarlas; solo se añaden las rutas
concretas de este mantenimiento autorizado.

RF/HU/HT, alcance, criterios, prioridades y estados del sprint se conservan. No procede
generar ediciones académicas ni modificar el gestor por este ajuste de recuperación;
su sincronización sigue siendo obligatoria cuando cambien los datos de producto.
No se modifica la app, `.obsidian/` ni la configuración privada de Codex. Sin Git ni
publicación. El vault ya tenía cambios locales, incluidos AGENTS, estado e índice.

## Verificación y siguiente acción

- `python tools/validate-universal.py`: contrato OK; mantiene la advertencia previa
  de que el MOC omite `frontend-design`, ajena a este ajuste.
- `quick_validate.py` para las skills de contexto y handoff: `Skill is valid!` en ambas.
- Comparación de SHA-256: dos snapshots idénticos a los originales de esta sesión.
  Comparación estructural: rutas previas, prohibiciones y metadatos de producto conservados;
  rutas concretas de mantenimiento añadidas, sin permisos generales nuevos.
- Lectura YAML de estado/alcance y TOML del adaptador correcta; quince archivos comprobados,
  sin enlaces nuevos rotos ni caracteres de sustitución. La cabecera histórica conserva
  su `next_action` sin comillas; para comparar YAML se normalizó solo en memoria.
- Revisión del diff y `git diff --check`: correctos. No se repiten pruebas Django porque
  este ajuste no modifica código ni comportamiento del producto.

Retomar la tarea seleccionada por el tesista con el estado breve y las fuentes pertinentes;
para código, comprobar ambas raíces Git y el requisito/sprint antes de escribir.

## Precisión del recorrido por relaciones — 2026-10-29

El tesista pidió mantener presente arquitectura, avance previo y RF/HU/HT mediante las
relaciones del vault. Se incorpora [[../../context/recorrido-tarea|una ruta de lectura]]
desde AGENTS, índice y skill de contexto: tarea → requisitos/historias/criterios →
arquitectura y dependencias → código/pruebas → evidencia y continuidad. Incluye el caso
real SB-S2-06/RF-ACC-006/HU-ACC-010/HT-ACC-001, sin iniciar su implementación.
No exige crear otra ficha por tarea ni abrir todo el grafo.

Se observó que la matriz conserva rutas de plantillas y un corte de 17 pruebas anteriores
al checkpoint de 31 pruebas; se trata como índice, sin sustituir el código o evidencia
vigentes. Esa reconciliación queda pendiente; esta tarea no modifica resultados ni
declara completas historias. Los IDs en texto no son enlaces ni nodos individuales del
grafo de notas. Las referencias nuevas se validan contra sus archivos y secciones reales.

Verificación de la ampliación: enlaces resueltos y siete encabezados Wikilink comprobados
en sus fuentes; contrato universal, skill de contexto y `git diff --check` correctos.
Estado e índice ahora suman 7.935 bytes (81,8 % menos que los 43.534 iniciales); la guía
de recorrido se abre bajo demanda al preparar producto, sin sumarla a todas las consultas.

## Simplificación solicitada — 2026-10-29

El tesista precisa que busca lectura eficiente, sin burocracia. AGENTS, índice y skill
dejan la guía como referencia opcional y eliminan la obligación de recorrerla en cada
tarea. La guía se reduce a buscar IDs, leer secciones pertinentes y detenerse al tener
contexto suficiente; reconciliar solo lo que afecte el cambio. No se exige ficha,
tabla adicional, auditoría global ni presentación formal por tarea. Las verificaciones
y sincronizaciones de producto ya exigidas se conservan.
