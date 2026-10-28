---
titulo: Plan de fases y sprints hasta el 23 de diciembre de 2026
version: "1.1"
fecha: 2026-10-13
autor: Tesista
estado: plan-de-referencia-sujeto-a-estimacion
fuentes: "Gantt aportado por el tesista; calendario confirmado; CAT-REQ-001 v1.1; pila de producto v1.3"
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Plan de fases y sprints hasta el 23 de diciembre de 2026

El tesista fijó **S1 del 15 de septiembre al 12 de octubre** para requisitos y diseño. El desarrollo comienza con **S2 el 13 de octubre**. Se conservan los cinco bloques funcionales del plan anterior, ahora numerados S2–S6, y dos días de cierre hasta el **23 de diciembre de 2026**. El calendario organiza trabajo candidato; todavía no hay estimaciones ni capacidad comprobada para prometer las 60 historias de la pila.

## Correspondencia con el Gantt y la edición anterior

| Bloque del Gantt | Edición anterior | Plan vigente | Fechas de 2026 |
|---|---|---|---|
| Requisitos y diseño (semanas relativas 1–4) | Etapa previa | S1 | 15 sep–12 oct |
| Administración y acceso | S1 | S2 | 13–26 oct |
| Planificación de actividades | S2 | S3 | 27 oct–9 nov |
| Asistencia y participación | S3 | S4 | 10–23 nov |
| Trazabilidad productiva y rendición | S4 | S5 | 24 nov–7 dic |
| Reportes e información | S5 | S6 | 8–21 dic |
| Validación y cierre | Cierre | Cierre | 22–23 dic |

S1 dura 28 días calendario; S2–S6 duran 14 días cada uno; el cierre dura 2 días. El plan completo del **15 de septiembre al 23 de diciembre** suma **100 días calendario**, 12 menos que las 16 semanas (112 días) del Gantt. La disponibilidad real puede ser menor por otras obligaciones y por la agenda de las usuarias. En el repositorio técnico, SPEC-001 y su plan aprobado conservan la etiqueta histórica `S1`; en este calendario público se leen como trabajo del **S2 de desarrollo**. Cambiar esos artefactos aprobados requiere revisión y registro de impacto.

## Hitos y documentación

| Sprint | Objetivo y trabajo principal | Entregables documentales y prueba |
|---|---|---|
| S1 · 15 sep–12 oct | Levantar y validar requisitos; arquitectura, datos, recorridos móviles, PWA y pila. | Actas, catálogo y decisiones con estado real; diseño revisable, historias, factibilidad, pila y estimación pendiente explícita. No se presume cierre académico. |
| S2 · 13–26 oct | Acceso privado, cuentas y permisos según historias elegidas. | `HU-ACC`, `HT-GEN-001/002/004/009`; pruebas permitidas y denegadas, revisión y retrospectiva. |
| S3 · 27 oct–9 nov | Actividades, responsables, encargos y planificación. | `HU-PLA`, `HT-S3-001` candidata; pruebas del flujo, permisos y regresión de S2. |
| S4 · 10–23 nov | Asistencia, participación y continuidad aprobada. | `HU-ASI`, `HU-PWA`, `HT-GEN-003/005/006` y `HT-S4-001` candidata; prueba de corte/reintento cuando las decisiones estén cerradas. |
| S5 · 24 nov–7 dic | Materia prima, secado, lotes e inventario; comercio según capacidad y reglas aprobadas. | `HU-CAT/TRA/INV/VEN/GAS/CXC`, `HT-GEN-003` y `HT-S5-001` candidata; integridad de movimientos, cifras y regresión. |
| S6 · 8–21 dic | Reportes, contenido público autorizado e integración final. | `HU-REP/NOT/PUB`, `HT-GEN-007`, `HT-S6-001/002` candidatas; pruebas funcionales, de uso y continuidad, manuales y preparación de capacitación. |
| Cierre · 22–23 dic | Corregir hallazgos críticos, validar con usuarias y entregar según agenda y resultado real. | Acta de validación, capacitación si ocurre, manuales, matriz, retrospectiva y estado de pendientes. |

Las pruebas parciales, autorización, accesibilidad, trazabilidad y actualización documental acompañan cada incremento. La integración empieza antes de S6 cuando los recorridos se conectan; S6 concentra la comprobación final. Las decisiones P abiertas impiden cerrar la parte afectada de una historia. La revisión de la directora y la validación de nuevas reglas de entrevista siguen pendientes.

## Regla de planificación del sprint

El [sprint backlog v1.0](sprint_backlog_v1.0_2026-10-13.md) relaciona historias de usuario, técnicas y tareas candidatas. Antes de comprometerlas se confirma capacidad, estimación, criterios, dependencias y disponibilidad para revisión. En cada cierre se registra qué quedó **completo, parcial o bloqueado**, con resultados de pruebas. Todo cambio documental relevante genera una nueva versión y una entrada en el control de cambios; su publicación requiere confirmación del tesista.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.0 | 2026-10-12 | Cinco sprints de desarrollo numerados S1–S5. | Edición anterior conservada. |
| 1.1 | 2026-10-13 | S1 de requisitos y diseño del 15 sep al 12 oct; desarrollo renumerado S2–S6 y vínculos con historias y pila. | Plan preparado; estimación pendiente. |
