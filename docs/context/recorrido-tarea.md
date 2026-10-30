---
title: Recuperación del contexto por relaciones de una tarea
type: context-guide
status: active
updated: 2026-10-29
source_of_truth: AGENTS.md
related:
  - "[[context-index]]"
  - "[[../bitacora/ESTADO-ACTIVO]]"
  - "[[../traceability/MATRIZ-TRAZABILIDAD]]"
tags:
  - proyecto/tesis
  - modulo/transversal
---

# Lectura eficiente para una tarea

Referencia opcional si hay dudas sobre cómo recuperar contexto; no es otro trámite.

1. Partir de la solicitud y el estado activo. Reutilizar lo ya leído y vigente.
2. Buscar por ID de tarea o RF/HU/HT en el archivo o módulo probable. Abrir solo las
   secciones con criterios, arquitectura y dependencias que afecten el cambio.
3. Consultar el checkpoint relacionado si hace falta saber dónde quedó el trabajo;
   comprobar código y pruebas pertinentes antes de editar. Parar al tener contexto
   suficiente para implementar y verificar la porción solicitada.

No crear fichas, matrices o resúmenes adicionales para poder empezar. No recorrer
cronológicamente la bitácora ni todos los enlaces del vault. Los índices orientan;
los criterios y decisiones conservan sus fuentes canónicas.

Si aparece una discrepancia que afecta la tarea, comprobar y corregir esa referencia
según la jerarquía de AGENTS.md. Una auditoría del vault o reconciliación general no
es precondición de una tarea ordinaria. Un resultado antiguo puede conservarse como
histórico; no equivale a la verificación del código actual.

Las reglas de seguridad, arquitectura aplicable, pruebas y sincronización de cambios
de producto de AGENTS.md siguen vigentes. Esta guía solo simplifica la recuperación.
