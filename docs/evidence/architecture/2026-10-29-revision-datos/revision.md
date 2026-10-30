---
title: Evidencia de corrección documental del diseño de datos
type: evidence
status: partially-complete
date: 2026-10-29
author: Codex
task_id: SB-S1-03
technical_story: HT-PRE-003
sprint_execution: S2
module: transversal
related:
  - "[[../../../architecture/proposals/2026-10-29-diseno-integral-base-datos]]"
  - "[[../../../requirements/proposals/2026-10-29-enmienda-datos-sin-credito-y-administracion]]"
  - "[[../../../bitacora/checkpoints/2026-10-29-correccion-integridad-diseno-datos]]"
---

# Resultado verificado

La revisión 0.2 del diseño incorpora las respuestas directas D-24 a D-30: ningún crédito al comprador; cobro antes de entrega; custodia y rendición posterior de socia; Superadministradora dedicada a administración/correcciones auditadas; secado de un único acopio; reembolsos/anulaciones pendientes; redondeo `ROUND_HALF_UP` por línea y desempate por ID de asignación menor.

Se corrigieron relaciones entre lotes, cuentas, movimientos, cobros, entregas y rendiciones; unicidad con nulos y comprobantes; límites administrativos; versiones de conciliación y fuentes de reparto. La especificación candidata SPEC-002 muestra el aviso de incompatibilidad antes de sus criterios históricos. Se conservaron CAT y ediciones aprobadas; seis adendas nuevas registran la sincronización editorial propuesta.

## Controles realizados

- 15 documentos revisados por presencia de metadatos, codificación UTF-8, bloques de código cerrados, destinos de enlaces relativos y estructura de tablas. Resultado final: cero errores.
- 14 controles sobre el contrato documental: 15 casos DAT definidos; ausencia de deuda externa activa/en ER; cobro/entrega/salida explícitos; acopio obligatorio en secado; unicidad de receta estándar; denegación administrativa de venta/cobro; identidad de cuenta; rendición interna; padre existente para bloqueo; reembolso no automático; siete respuestas registradas; redondeo explícito.
- Ejemplo decimal calculado con Python `Decimal`: `1.005 → 1.01`. Ejemplo de fondo de USD 10,00 entre asignaciones 3, 5 y 8: USD 3,34; 3,33; 3,33. Son comprobaciones aritméticas de la regla, no pruebas del código de producto.
- `git diff --check` correcto en general y app; las advertencias sobre finales de línea no son fallos de whitespace. Se revisaron los diffs de archivos rastreados y diferencias de las cinco propuestas contra copias locales tomadas antes de editarlas, porque eran archivos sin seguimiento Git.
- Resultados y SHA-256 de los documentos: [verificacion.json](verificacion.json).

Durante el control se corrigieron separadores de aliases de Wikilinks dentro de tablas y la continuidad de cabeceras/historial. El informe JSON corresponde al resultado final, no a las pasadas de reparación.

## Sincronización local comprobada

El gestor `http://127.0.0.1:55478/` no estaba disponible al inicio. Se inició `servidor.py --no-browser` en segundo plano con ventana oculta. Se usaron sus API locales con cabecera Origin y se releyó el estado guardado.

- 39 requisitos/HU/HT actualizados mediante overlays con fuente en las nuevas adendas; criterios previos conservados como antecedente en el overlay.
- SB-S1-03 y las seis tareas existentes de S5 recibieron evidencia/notas de impacto; no se cambiaron estimaciones, fechas, cierres de sprint ni estados de tarea.
- Se preservaron las marcas de criterios existentes y los estados de sprint mediante comparación antes/después.
- Discrepancia previa conservada: `/api/seguimiento` registra SB-S1-03 `en_curso`; el dashboard v5 conserva `done` con evidencia/revisor anteriores. Las notas nuevas indican que esta revisión no verifica la terminación total. No se rebajó ni se certificó el estado histórico por inferencia.
- No se inventaron IDs nuevos. La evidencia es accesible por `/evidencias/architecture/2026-10-29-revision-datos/revision.md`.

## Límites

No se ejecutaron migraciones ni se inspeccionó la BD física. DAT-01 a DAT-15 son casos de aceptación para la implementación futura; no son pruebas ejecutadas de modelos ni de concurrencia. No se modificó código de la app ni se hicieron commit, push o publicación al docente. Las pruebas y modificaciones previas de la app quedan fuera de esta revisión.

Pendientes: reconciliar enmienda con CAT/SPEC-002 conservando evidencia; completar parámetros productivos, descuentos y política offline cuando se active cada recorrido; decidir efectos de devoluciones/pérdidas/sobrepagos. No se declara terminado el modelo físico ni SB-S1-03.
