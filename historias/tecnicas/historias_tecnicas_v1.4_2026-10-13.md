---
titulo: Historias técnicas y prioridad por sprint
version: "1.4"
fecha: 2026-10-13
autor: Tesista
estado: final-documental-con-propuestas-identificadas
historias_base: 9
historias_nuevas_propuestas: 10
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
fuentes: "CAT-REQ-001 v1.1; historias técnicas v1.3; Gantt aportado; constitución 0.2.0; ADR-0006"
---

# Historias técnicas y prioridad por sprint

Este documento ordena el trabajo que permite comprobar las historias de usuario. Las **nueve historias técnicas existentes** conservan sus IDs y criterios detallados en la [edición v1.3](historias_tecnicas_v1.3_2026-10-12.md). Se proponen **diez historias adicionales** para hacer visible el levantamiento, diseño, pruebas, integración y capacitación que aparecen en el Gantt. Son propuestas de planificación, no requisitos aprobados ni trabajo realizado.

## Regla de prioridad

| Nivel | Significado para ordenar el trabajo |
|---|---|
| Crítica | Bloquea un recorrido esencial, la protección de datos o una puerta de calidad. Debe resolverse antes de comprometer la historia de usuario dependiente. |
| Alta | Aporta una condición importante del sprint o reduce un riesgo importante; se planifica antes de trabajo de menor impacto. |
| Media | Necesaria para completar una entrega posterior, pero puede prepararse después de las dependencias críticas. |
| Baja | Mejora diferible que no bloquea la entrega mínima. No se asignó este nivel a las historias actuales. |

La prioridad es **propuesta**. Una historia con prioridad crítica puede seguir bloqueada por una decisión pendiente; su prioridad no la convierte en aprobada. La estimación, el responsable y la selección definitiva se fijan al planificar cada sprint.

## Nueve historias técnicas de la línea base

| Orden de trabajo | ID y trabajo | Prioridad | Sprint principal | Relación y salida verificable |
|---:|---|---|---|---|
| 1 | `HT-GEN-008` Explorar despliegue y recuperación | Alta | S1; revisión en S6 | Habilita la futura entrega piloto. Comparar entorno, costos, archivos, HTTPS y recuperación; P-11 sigue abierto. |
| 2 | `HT-GEN-001` Preparar la base modular Django | Crítica | S2 | Habilita `HU-ACC-001` a `HU-ACC-004`; usuario personalizado y migraciones en PostgreSQL comprobados. |
| 3 | `HT-GEN-009` Preparar pruebas y trazabilidad | Crítica | S2–S6 | Cada HU elegida conserva vínculo con RF, prueba y resultado; se ejecuta regresión en cada incremento. |
| 4 | `HT-GEN-002` Aplicar autorización en el servidor | Crítica | S2–S6 | Protege `HU-ACC`, `HU-PLA`, `HU-ASI`, `HU-TRA`, `HU-INV`, `HU-VEN`, `HU-REP` y `HU-PUB`; probar acceso permitido y denegado. |
| 5 | `HT-GEN-004` Preparar componentes móviles y accesibles | Alta | S2–S6 | Habilita recorridos HU en móvil, teclado, contraste y errores recuperables. |
| 6 | `HT-GEN-003` Asegurar integridad y auditoría | Crítica | S4–S5 | Protege correcciones de `HU-ASI`, movimientos `HU-TRA`/`HU-INV`, ventas `HU-VEN` y saldos `HU-CXC`; probar reversión y concurrencia. |
| 7 | `HT-GEN-005` Preparar captura local protegida | Alta | S4–S5 | Habilita `HU-PWA-001` y `HU-PWA-002` para operaciones autorizadas; P-13/P-14 pendientes. |
| 8 | `HT-GEN-006` Sincronizar sin duplicados | Crítica | S4–S5 | Habilita `HU-PWA-003`; probar reintento, permiso revocado y conflicto sin cambios parciales. |
| 9 | `HT-GEN-007` Generar reportes PDF verificables | Alta | S6 | Habilita `HU-REP-001` a `HU-REP-005`; contrastar totales con datos fuente y permisos. |

Las prioridades anteriores sustituyen la lectura implícita de «posición 1/60» como nivel de importancia. El orden de la pila sigue siendo una **secuencia propuesta**, no una clasificación de gravedad.

## Diez historias técnicas nuevas para estudiar y estimar

| Orden de revisión | ID, sprint y prioridad | Trabajo propuesto | Relación con HU o entregable | Criterio de salida |
|---:|---|---|---|---|
| 1 | `HT-PRE-001` · S1 · Alta | Levantar y consolidar entrevistas, observación y documentos disponibles. | Fuentes de los RF y de todas las HU; actas de campo. | Cada necesidad registra fuente, fecha, actor, duda y evidencia; no se atribuye aprobación a una nota informal. |
| 2 | `HT-PRE-002` · S1 · Crítica | Validar alcance, requisitos, reglas y criterios de aceptación con las personas competentes. | `CAT-REQ-001`, `HU-ACC` a `HU-PUB`; decisiones P abiertas. | Separar confirmado, propuesto y pendiente; conservar acta o decisión de cada validación. |
| 3 | `HT-PRE-003` · S1 · Alta | Preparar arquitectura, modelo conceptual y límites de datos por módulo. | Diseño para `HU-ACC`, `HU-PLA`, `HU-ASI`, `HU-TRA`, `HU-INV`, `HU-VEN` y `HU-REP`. | Entidades, dueños de escritura, relaciones, permisos y operaciones conjuntas trazados a requisitos. |
| 4 | `HT-PRE-004` · S1 · Alta | Diseñar recorridos móviles y preparación PWA sin afirmar que la aplicación ya funciona. | `RNF-UX-001` a `003`; `HU-PWA-001` a `003`. | Pantallas y estados de error revisables; límites de datos locales, corte y sincronización pendientes identificados. |
| 5 | `HT-PRE-005` · S1 · Alta | Refinar historias, pila, dependencias, estimaciones y calendario con capacidad real. | 51 HU, 9 HT base y candidatas; sprint backlog. | Cada elemento que pase a un sprint tiene criterio, dependencia, tamaño y decisión de inclusión registrados. |
| 6 | `HT-S3-001` · S3 · Alta | Preparar pruebas de planificación y regresión de permisos sobre actividades y encargos. | `HU-PLA-001` a `005`; `HU-ACC-001` a `004`. | Una asignación válida funciona y una inválida no cambia datos; el acceso anterior sigue funcionando. |
| 7 | `HT-S4-001` · S4 · Alta | Precisar y probar QR, alternativa de registro y operaciones de asistencia sin red antes de implementarlas. | `HU-ASI-001` a `007`; `HU-PWA-001` a `003`; P-02/P-13/P-14. | Casos de entrada, salida, duplicado, dispositivo compartido y corte/reintento documentados; reglas abiertas visibles. |
| 8 | `HT-S5-001` · S5 · Crítica | Probar la cadena productiva y las operaciones comerciales que entren realmente al sprint. | `HU-TRA`, `HU-INV`, `HU-VEN`, `HU-CXC`, `HU-GAS`; `HT-GEN-003`. | Movimientos y totales concilian; fallo o concurrencia no deja stock ni saldos incoherentes. |
| 9 | `HT-S6-001` · S6 · Crítica | Ejecutar integración, pruebas funcionales y de uso, continuidad aprobada y regresión. | Todas las HU efectivamente entregadas; `HT-GEN-009`. | Resultados reales, defectos, correcciones y nueva prueba registrados; sesión con usuarias cuando ocurra. |
| 10 | `HT-S6-002` · S6 y cierre · Alta | Preparar manuales, capacitación y acta de validación final. | Recorridos entregados de `HU-ACC` a `HU-PUB`; hito final del Gantt. | Manual refleja la versión comprobada; capacitación y validación tienen fecha, participantes y observaciones, o constan pendientes. |

## Condiciones para pasar a la pila comprometida

Las nuevas historias son **candidatas**. Antes de incorporarlas a un sprint comprometido se confirma que no duplican tareas aprobadas, se estiman con la disponibilidad real y se revisan las puertas de requisito y diseño. `HT-PRE-001` y `HT-PRE-002` describen trabajo previo: la documentación ya existe en parte, pero faltan validaciones; no se marca la historia como terminada por la fecha del cronograma. El desarrollo comienza en S2 el 13 de octubre; las nuevas HT no amplían por sí solas el alcance funcional.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.3 | 2026-10-12 | Nueve historias técnicas con criterios detallados. | Edición anterior conservada. |
| 1.4 | 2026-10-13 | Prioridad cualitativa, mapeo S1–S6 y diez candidatas técnicas ligadas al Gantt. | Preparado; estimación y revisión pendientes. |
