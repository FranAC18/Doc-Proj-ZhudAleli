---
titulo: Pila de producto con campos separados
version: "1.6"
fecha: 2026-10-14
autor: Tesista
estado: final-documental-con-prioridades-propuestas
elementos_base: 60
historias_usuario: 51
historias_tecnicas: 9
historias_tecnicas_planificadas_s1: 5
historias_tecnicas_aun_propuestas: 5
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Pila de producto

La línea base ordenada conserva 51 historias de usuario y 9 historias técnicas (60 posiciones). Cinco HT-PRE están planificadas para S1 y se muestran aparte, sin sumarlas a esas posiciones; otras cinco historias técnicas continúan propuestas para sprints posteriores. Cada columna muestra **un solo dato**. Los detalles y dependencias están en las fichas de [HU](../historias/usuario/historias_usuario_v2.5_2026-10-13.md) y [HT](../historias/tecnicas/historias_tecnicas_v1.6_2026-10-14.md). La planificación no acredita que las tareas estén terminadas.

## Línea base ordenada

| N.º | Código | Tipo | Nombre | Prioridad propuesta | Sprint previsto |
|---:|---|---|---|---|---|
| 1 | `HT-GEN-008` | Técnica | Explorar despliegue y recuperación | Alta | S1; revisión en S6 |
| 2 | `HT-GEN-001` | Técnica | Preparar la base modular Django | Crítica | S2 |
| 3 | `HT-GEN-009` | Técnica | Preparar pruebas y trazabilidad | Crítica | Transversal desde S2 |
| 4 | `HT-GEN-002` | Técnica | Aplicar autorización en el servidor | Crítica | Transversal desde S2 |
| 5 | `HT-GEN-004` | Técnica | Preparar componentes móviles y accesibles | Alta | Transversal desde S2 |
| 6 | `HU-ACC-001` | Usuario | Entrar y salir de la parte privada | Esencial | S2 |
| 7 | `HU-ACC-002` | Usuario | Administrar membresías | Alta | S2 |
| 8 | `HU-ACC-003` | Usuario | Usar funciones según responsabilidades | Esencial | S2 |
| 9 | `HU-PLA-001` | Usuario | Programar una actividad | Alta | S3 |
| 10 | `HU-PLA-002` | Usuario | Asignar participantes y responsables | Alta | S3 |
| 11 | `HU-PLA-003` | Usuario | Crear un encargo temporal | Alta | S3 |
| 12 | `HU-PLA-004` | Usuario | Consultar mis actividades | Complementaria | S3 |
| 13 | `HU-CAT-001` | Usuario | Mantener catálogo productivo | Esencial | S5 |
| 14 | `HU-PLA-005` | Usuario | Planificar producción semanal | Alta | S3 |
| 15 | `HU-ACC-004` | Usuario | Ver mis opciones disponibles | Complementaria | S2 |
| 16 | `HT-GEN-003` | Técnica | Asegurar integridad y auditoría | Crítica | Transversal desde S4 |
| 17 | `HT-GEN-005` | Técnica | Preparar captura local protegida | Alta | Transversal S4/S5 |
| 18 | `HT-GEN-006` | Técnica | Sincronizar sin duplicados | Crítica | Transversal S4/S5 |
| 19 | `HU-PWA-001` | Usuario | Abrir tareas habilitadas sin conexión | Esencial | Transversal S4/S5 |
| 20 | `HU-PWA-002` | Usuario | Conservar registros pendientes sin conexión | Esencial | Transversal S4/S5 |
| 21 | `HU-PWA-003` | Usuario | Sincronizar registros pendientes | Esencial | Transversal S4/S5 |
| 22 | `HU-ASI-001` | Usuario | Registrar entrada y salida | Esencial | S4 |
| 23 | `HU-ASI-002` | Usuario | Evitar asistencia duplicada | Esencial | S4 |
| 24 | `HU-ASI-003` | Usuario | Corregir asistencia con historial | Esencial | S4 |
| 25 | `HU-ASI-004` | Usuario | Consultar historial de asistencia | Complementaria | S4 |
| 26 | `HU-ASI-005` | Usuario | Registrar participación adicional | Complementaria | S4 |
| 27 | `HU-ASI-006` | Usuario | Resolver una inconsistencia de asistencia | Alta | S4 |
| 28 | `HU-ASI-007` | Usuario | Registrar asistencia con QR o alternativa | Alta | S4 |
| 29 | `HU-INV-001` | Usuario | Conservar valores comerciales históricos | Esencial | S5 |
| 30 | `HU-TRA-001` | Usuario | Registrar acopio de materia | Esencial | S5 |
| 31 | `HU-TRA-002` | Usuario | Registrar secado | Esencial | S5 |
| 32 | `HU-TRA-003` | Usuario | Conocer duración y merma | Alta | S5 |
| 33 | `HU-TRA-004` | Usuario | Seguir la procedencia de lotes | Esencial | S5 |
| 34 | `HU-TRA-005` | Usuario | Registrar transformación | Esencial | S5 |
| 35 | `HU-INV-002` | Usuario | Reconstruir existencias | Esencial | S5 |
| 36 | `HU-INV-003` | Usuario | Entregar productos para feria | Alta | S5 |
| 37 | `HU-INV-004` | Usuario | Conciliar productos de feria | Alta | S5 |
| 38 | `HU-VEN-001` | Usuario | Registrar una venta | Esencial | S5 |
| 39 | `HU-VEN-002` | Usuario | Identificar comprador según la venta | Alta | S5 |
| 40 | `HU-VEN-003` | Usuario | Conocer valor base y excedente | Esencial | S5 |
| 41 | `HU-VEN-004` | Usuario | Autorizar venta bajo valor base | Esencial | S5 |
| 42 | `HU-VEN-005` | Usuario | Configurar descuento por volumen | Complementaria | S5 |
| 43 | `HU-VEN-006` | Usuario | Distinguir stock individual y compartido | Alta | S5 |
| 44 | `HU-VEN-007` | Usuario | Registrar venta institucional | Alta | S5 |
| 45 | `HU-VEN-008` | Usuario | Conciliar comprobante manual de feria | Alta | S5 |
| 46 | `HU-GAS-001` | Usuario | Registrar gasto operativo | Alta | S5 |
| 47 | `HU-CXC-001` | Usuario | Distinguir deudas y custodia | Esencial | S5 |
| 48 | `HU-CXC-002` | Usuario | Registrar un abono | Esencial | S5 |
| 49 | `HU-CXC-003` | Usuario | Rendir cuentas de la feria | Alta | S5 |
| 50 | `HU-GAS-002` | Usuario | Consultar resumen económico | Complementaria | S5 |
| 51 | `HT-GEN-007` | Técnica | Generar reportes PDF verificables | Alta | S6 |
| 52 | `HU-REP-001` | Usuario | Consultar reporte de asistencia | Alta | S6 |
| 53 | `HU-REP-002` | Usuario | Consultar reporte de actividades | Alta | S6 |
| 54 | `HU-REP-003` | Usuario | Consultar reporte productivo | Alta | S6 |
| 55 | `HU-REP-004` | Usuario | Consultar reporte de inventario | Alta | S6 |
| 56 | `HU-REP-005` | Usuario | Consultar reporte de ventas y saldos | Alta | S6 |
| 57 | `HU-REP-006` | Usuario | Consultar mi resumen privado | Complementaria | S6 |
| 58 | `HU-NOT-001` | Usuario | Recibir recordatorios internos | Complementaria | S6 |
| 59 | `HU-PUB-002` | Usuario | Gestionar contenido público | Complementaria | S6 |
| 60 | `HU-PUB-001` | Usuario | Conocer información pública aprobada | Complementaria | S6 |

## Historias técnicas planificadas para S1

Estas cinco historias se incluyen en S1 por indicación del tesista y no forman parte de las 60 posiciones de la línea base. El estado real de sus tareas y evidencias se registra en el sprint backlog; la asignación no declara el sprint completo.

| N.º | Código       | Nombre                                                                                      | Prioridad | Sprint |
| --: | ------------ | ------------------------------------------------------------------------------------------- | --------- | ------ |
|   1 | `HT-PRE-001` | Levantar y consolidar entrevistas, observación y documentos disponibles.                    | Alta      | S1     |
|   2 | `HT-PRE-002` | Validar alcance, requisitos, reglas y criterios de aceptación con las personas competentes. | Crítica   | S1     |
|   3 | `HT-PRE-003` | Preparar arquitectura, modelo conceptual y límites de datos por módulo.                     | Alta      | S1     |
|   4 | `HT-PRE-004` | Diseñar recorridos móviles y preparación PWA sin afirmar que la aplicación ya funciona.     | Alta      | S1     |
|   5 | `HT-PRE-005` | Refinar historias, pila, dependencias, estimaciones y calendario con capacidad real.        | Alta      | S1     |

## Historias técnicas aún propuestas para S3–S6

Estas cinco historias se mantienen como propuestas y no se consideran incorporadas a la línea base.

| N.º | Código | Nombre | Prioridad propuesta | Sprint previsto | Estado |
|---:|---|---|---|---|---|
| 1 | `HT-S3-001` | Preparar pruebas de planificación y regresión de permisos sobre actividades y encargos. | Alta | S3 | Propuesta |
| 2 | `HT-S4-001` | Precisar y probar QR, alternativa de registro y operaciones de asistencia sin red antes de implementarlas. | Alta | S4 | Propuesta |
| 3 | `HT-S5-001` | Probar la cadena productiva y las operaciones comerciales que entren realmente al sprint. | Crítica | S5 | Propuesta |
| 4 | `HT-S6-001` | Ejecutar integración, pruebas funcionales y de uso, continuidad aprobada y regresión. | Crítica | S6 | Propuesta |
| 5 | `HT-S6-002` | Preparar manuales, capacitación y acta de validación final. | Alta | S6 y cierre | Propuesta |

## Pendientes para planificar

Las reglas P-02 a P-14, la revisión académica, la estimación y la capacidad se registran antes de comprometer una historia. Las necesidades adicionales de entrevista permanecen en la [edición anterior](pila_producto_v1.4_2026-10-13.md) hasta que se validen. El orden puede cambiar con una decisión humana registrada.

## Historial de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 1.4 | 2026-10-13 | Nivel cualitativo de HU separado de posición en pila. |
| 1.5 | 2026-10-13 | Columnas independientes y tabla aparte para HT adicionales. |
| 1.6 | 2026-10-14 | Se separan cinco HT planificadas para S1 de cinco propuestas posteriores; la base conserva 60 posiciones. |
