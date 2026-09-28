---
title: Roadmap de sprints del anteproyecto
type: roadmap
status: in-progress
updated: 2026-09-28
---

# Roadmap de sprints del anteproyecto

Este roadmap conserva el orden expresado en el anteproyecto. Los nombres pueden
refinarse durante el levantamiento, pero no se cambia el alcance sin registrar una
decisión.

## Fases previas

### Fase I - Levantamiento de requerimientos

Revisión documental, visitas de campo, observación, entrevistas, análisis, validación y
Product Backlog inicial.

### Fase II - Diseño del sistema

Casos de uso, diagramas UML, arquitectura MTV/Django, modelo relacional PostgreSQL y
diseño de interfaces.

## Desarrollo

| Sprint | Módulo | Resultado esperado |
|---|---|---|
| Sprint 1 | Administración y acceso | Autenticación, roles y permisos RBAC |
| Sprint 2 | Planificación de actividades | Actividades, responsables, fechas y estados |
| Sprint 3 | Asistencia y participación | Entradas, salidas, historial y participación |
| Sprint 4 | Trazabilidad productiva | Materia prima, secado, lotes, inventario, ventas, gastos y cuentas por cobrar según catálogo |
| Sprint 5 | Reportes e información | Reportes organizativos, productivos, comerciales, resumen propio y sitio público |

## Fases posteriores

- Evaluación funcional e ISO/IEC 25010:2023.
- Documentación técnica y de usuario.
- Diccionario de datos.
- Redacción final y defensa.

## Regla

El orden anterior organiza los cinco bloques académicos. El Gantt actualizado permite
solapamientos: cada trabajo comienza cuando sus propios requisitos, criterios y dependencias
están validados; no exige terminar todo el módulo previo. Esto no declara sprints Scrum
simultáneos para una sola persona ni elimina las puertas de implementación.

## Distribución vigente del trabajo

[[../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack|Fuente: Gantt aportado el 2026-09-28]].

| Bloque | Semanas relativas |
|---|---|
| Requisitos | 1–2 |
| Arquitectura, base de datos, UX y configuración PWA | 3–4 |
| Administración y acceso | 5–6 |
| Planificación | 6–7 |
| Asistencia | 7–8 |
| Trazabilidad, incluido alcance comercial aprobado | 9–10 |
| Dashboard, reportes y sitio público | 11–12 |
| Pruebas parciales | 5–12 |
| Integración | 13 |
| Funcionales/usabilidad y offline/sincronización | 13–14 |
| Correcciones | 14 |
| Validación final con usuarias | 15 |
| Capacitación, manuales y cierre documental | 15–16 |

Hitos: semanas 2, 4, 12 y 16. La documentación y las pruebas acompañan el desarrollo;
S13–S14 verifican integración offline, no inician toda su construcción. Fechas absolutas
pendientes de aportación. El estado de esta nota indica planificación, no módulos terminados.
