---
title: Matriz de trazabilidad del proyecto
type: traceability
status: in-progress
date: 2026-07-21
tags:
  - proyecto/tesis
  - tipo/trazabilidad
---

# Matriz de trazabilidad

Esta matriz es un índice de enlaces, no una copia de los requisitos. Se completa cuando una
especificación es confirmada y se actualiza al implementar, probar y validar.

## Objetivos a incrementos

| Objetivo del anteproyecto | Capacidad prevista | Sprint | Spec aprobada | Estado |
|---|---|---|---|---|
| OE-01 Analizar procesos y requerimientos | Product Backlog validado | Fase I | Pendiente | `in-progress` |
| OE-02 Desarrollar módulos y control de acceso | Administración y RBAC | S1 | Pendiente | `planned` |
| OE-02 Desarrollar módulos y control de acceso | Planificación | S2 | Pendiente | `planned` |
| OE-02 Desarrollar módulos y control de acceso | Asistencia y participación | S3 | Pendiente | `planned` |
| OE-02 Desarrollar módulos y control de acceso | Trazabilidad productiva | S4 | Pendiente | `planned` |
| OE-02 Desarrollar módulos y control de acceso | Reportes e información | S5 | Pendiente | `planned` |
| OE-03 Evaluar adecuación funcional | Evaluación ISO/IEC 25010:2023 | Fase IV | Pendiente | `planned` |

## Requisitos

| ID | Fuente validada | Spec | Sprint | Diseño/ADR | Código | Prueba | Evidencia | ISO 25010 | Estado |
|---|---|---|---|---|---|---|---|---|---|
| Pendiente | — | — | — | — | — | — | — | — | `planned` |

## Reglas

1. No añadir un RF/RNF como confirmado sin fuente y evidencia de validación.
2. Enlazar rutas relativas o Wikilinks al artefacto exacto.
3. Un requisito puede tener varias pruebas, pero cada criterio de aceptación debe quedar
   cubierto por al menos una evidencia o una limitación documentada.
4. “Implementado” significa código integrado y pruebas ejecutadas; “validado” requiere la
   evidencia humana o técnica definida.
5. Para adecuación funcional registrar la subcaracterística evaluada: completitud,
   corrección o pertinencia/apropiación funcional, según el instrumento aprobado.

## Cierre de sprint

Antes de cerrar un sprint, filtrar sus filas y confirmar que no existen enlaces rotos,
criterios sin prueba, resultados sin evidencia ni defectos críticos abiertos.
