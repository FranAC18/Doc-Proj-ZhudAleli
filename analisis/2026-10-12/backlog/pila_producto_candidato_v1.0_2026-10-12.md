---
titulo: Pila de producto de Zhud Alelí
version: "1.0"
fecha: 2026-10-12
autor: Codex, para revisión del tesista
estado: candidato-interno
fuente_requisitos: "CAT-REQ-001 v1.1"
fuente_formato: "Material de Aplicaciones Informáticas II, sección 2.8"
elementos: 60
historias_usuario: 51
historias_tecnicas: 9
prioridad: orden-preliminar-por-validar
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: no-autorizada
---

# Pila de producto — candidato para revisión

## Visión del producto

La aplicación debe ayudar al Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud a organizar actividades, registrar asistencia, seguir la producción y rendir cuentas de existencias y ventas. Debe funcionar en móvil y conservar las operaciones habilitadas durante cortes de conexión. La pila reúne **51 historias de usuario** derivadas de requisitos funcionales confirmados y **9 historias técnicas** que las habilitan.

## Cómo se lee el orden

La posición 1 es la primera prioridad **propuesta**; el orden combina dependencias conocidas, valor de los recorridos y la secuencia de cinco sprints confirmada para el proyecto. No equivale a una prioridad aprobada por la organización ni a un compromiso de meter todos los elementos de una etapa en un sprint. Los elementos pueden reordenarse al refinar la pila. La estimación de todos los elementos figura como **pendiente del equipo**, sin inventar horas ni puntos.

El estado de preparación distingue una capacidad confirmada de sus detalles aún abiertos. Una decisión P pendiente impide cerrar la porción afectada; no elimina la capacidad aprobada. Ningún elemento se declara implementado.

`HU-CAT-001` se adelanta en este orden respecto de su Sprint 4 previsto porque la planificación semanal (`HU-PLA-005`) necesita identificar productos. Ese adelanto es una propuesta de dependencia para el refinamiento, no un cambio aprobado de fechas.

## Elementos ordenados

| Prioridad propuesta | ID | Tipo | Elemento | Etapa prevista | Dependencias principales | Estimación | Preparación |
|---:|---|---|---|---|---|---|---|
| 1 | `HT-GEN-008` | Técnica | Explorar despliegue y recuperación | Exploración previa | ADR-0006; P-11 para política de respaldo | Pendiente | Exploración; P-11 abierto |
| 2 | `HT-GEN-001` | Técnica | Preparar la base modular Django | S1 | SPEC-001; ADR-0006 | Pendiente | Por especificar |
| 3 | `HT-GEN-009` | Técnica | Preparar pruebas y trazabilidad | Transversal desde S1 | HT-GEN-001 | Pendiente | Por especificar |
| 4 | `HT-GEN-002` | Técnica | Aplicar autorización en el servidor | Transversal desde S1 | HT-GEN-001 | Pendiente | Por especificar |
| 5 | `HT-GEN-004` | Técnica | Preparar componentes móviles y accesibles | Transversal desde S1 | HT-GEN-001 | Pendiente | Por especificar |
| 6 | `HU-ACC-001` | Usuario | Entrar y salir de la parte privada | S1 | HT-GEN-001, HT-GEN-002 | Pendiente | SPEC-001 confirmada; sin implementación verificada |
| 7 | `HU-ACC-002` | Usuario | Administrar membresías | S1 | HU-ACC-001, HT-GEN-002 | Pendiente | Por especificar |
| 8 | `HU-ACC-003` | Usuario | Usar funciones según responsabilidades | S1 | HU-ACC-001, HT-GEN-002 | Pendiente | Por especificar |
| 9 | `HU-PLA-001` | Usuario | Programar una actividad | S2 | HU-ACC-003 | Pendiente | Por especificar |
| 10 | `HU-PLA-002` | Usuario | Asignar participantes y responsables | S2 | HU-PLA-001, HU-ACC-003 | Pendiente | Por especificar |
| 11 | `HU-PLA-003` | Usuario | Crear un encargo temporal | S2 | HU-PLA-001, HU-PLA-002 | Pendiente | Por especificar |
| 12 | `HU-PLA-004` | Usuario | Consultar mis actividades | S2 | HU-PLA-001, HU-PLA-002 | Pendiente | Por especificar |
| 13 | `HU-CAT-001` | Usuario | Mantener catálogo productivo | S4 | HU-ACC-003 | Pendiente | Detalle P-04 |
| 14 | `HU-PLA-005` | Usuario | Planificar producción semanal | S2 | HU-PLA-001, HU-CAT-001 | Pendiente | Por especificar |
| 15 | `HU-ACC-004` | Usuario | Ver mis opciones disponibles | S1 | HU-ACC-001, HU-ACC-003 | Pendiente | Por especificar |
| 16 | `HT-GEN-003` | Técnica | Asegurar integridad y auditoría | Transversal desde S3 | HT-GEN-001 | Pendiente | Por especificar |
| 17 | `HT-GEN-005` | Técnica | Preparar captura local protegida | Transversal S3/S4 | HT-GEN-002; P-13/P-14 | Pendiente | P-13/P-14 abiertos |
| 18 | `HT-GEN-006` | Técnica | Sincronizar sin duplicados | Transversal S3/S4 | HT-GEN-003; HT-GEN-005; P-13/P-14 | Pendiente | P-13/P-14 abiertos |
| 19 | `HU-PWA-001` | Usuario | Abrir tareas habilitadas sin conexión | Transversal S3/S4 | HT-GEN-005 | Pendiente | P-13/P-14 abiertos |
| 20 | `HU-PWA-002` | Usuario | Conservar registros pendientes sin conexión | Transversal S3/S4 | HU-PWA-001, HT-GEN-005 | Pendiente | P-13/P-14 abiertos |
| 21 | `HU-PWA-003` | Usuario | Sincronizar registros pendientes | Transversal S3/S4 | HU-PWA-002, HT-GEN-006 | Pendiente | P-13/P-14 abiertos |
| 22 | `HU-ASI-001` | Usuario | Registrar entrada y salida | S3 | HU-PLA-001, HU-ACC-003; HU-PWA-002 solo para captura sin red | Pendiente | Captura sin red: P-13 |
| 23 | `HU-ASI-002` | Usuario | Evitar asistencia duplicada | S3 | HU-ASI-001 | Pendiente | Por especificar |
| 24 | `HU-ASI-003` | Usuario | Corregir asistencia con historial | S3 | HU-ASI-001, HT-GEN-003 | Pendiente | Por especificar |
| 25 | `HU-ASI-004` | Usuario | Consultar historial de asistencia | S3 | HU-ASI-001, HT-GEN-002 | Pendiente | Por especificar |
| 26 | `HU-ASI-005` | Usuario | Registrar participación adicional | S3 | HU-PLA-001, HU-ASI-001 | Pendiente | Por especificar |
| 27 | `HU-ASI-006` | Usuario | Resolver una inconsistencia de asistencia | S3 | HU-ASI-001, HU-ASI-003 | Pendiente | Por especificar |
| 28 | `HU-ASI-007` | Usuario | Registrar asistencia con QR o alternativa | S3 | HU-ASI-001, HU-ACC-003 | Pendiente | P-02/P-13 abiertos |
| 29 | `HU-INV-001` | Usuario | Conservar valores comerciales históricos | S4 | HU-CAT-001, HU-ACC-003 | Pendiente | Por especificar |
| 30 | `HU-TRA-001` | Usuario | Registrar acopio de materia | S4 | HU-CAT-001, HU-PLA-003 | Pendiente | Captura sin red: P-13 |
| 31 | `HU-TRA-002` | Usuario | Registrar secado | S4 | HU-TRA-001, HU-PLA-003 | Pendiente | Captura sin red: P-13 |
| 32 | `HU-TRA-003` | Usuario | Conocer duración y merma | S4 | HU-TRA-002 | Pendiente | Por especificar |
| 33 | `HU-TRA-004` | Usuario | Seguir la procedencia de lotes | S4 | HU-TRA-001, HU-TRA-002 | Pendiente | Excepciones P-05 |
| 34 | `HU-TRA-005` | Usuario | Registrar transformación | S4 | HU-TRA-004, HU-CAT-001 | Pendiente | Por especificar |
| 35 | `HU-INV-002` | Usuario | Reconstruir existencias | S4 | HU-CAT-001, HT-GEN-003 | Pendiente | Por especificar |
| 36 | `HU-INV-003` | Usuario | Entregar productos para feria | S4 | HU-INV-002, HU-PLA-003 | Pendiente | Por especificar |
| 37 | `HU-INV-004` | Usuario | Conciliar productos de feria | S4 | HU-INV-003, HU-INV-002 | Pendiente | Por especificar |
| 38 | `HU-VEN-001` | Usuario | Registrar una venta | S4 | HU-INV-002, HU-INV-003, HT-GEN-003 | Pendiente | Por especificar |
| 39 | `HU-VEN-002` | Usuario | Identificar comprador según la venta | S4 | HU-VEN-001 | Pendiente | Por especificar |
| 40 | `HU-VEN-003` | Usuario | Conocer valor base y excedente | S4 | HU-VEN-001, HU-INV-001 | Pendiente | Por especificar |
| 41 | `HU-VEN-004` | Usuario | Autorizar venta bajo valor base | S4 | HU-VEN-001, HU-VEN-003 | Pendiente | Por especificar |
| 42 | `HU-VEN-005` | Usuario | Configurar descuento por volumen | S4 | HU-CAT-001, HU-INV-001, HU-VEN-001 | Pendiente | Parámetros P-08 |
| 43 | `HU-VEN-006` | Usuario | Distinguir stock individual y compartido | S4 | HU-INV-003, HU-VEN-001 | Pendiente | Reparto P-07 excluido |
| 44 | `HU-VEN-007` | Usuario | Registrar venta institucional | S4 | HU-VEN-001, HU-VEN-002 | Pendiente | Por especificar |
| 45 | `HU-VEN-008` | Usuario | Conciliar comprobante manual de feria | S4 | HU-VEN-001, HU-INV-004 | Pendiente | Procedimiento P-10 |
| 46 | `HU-GAS-001` | Usuario | Registrar gasto operativo | S4 | HU-ACC-003 | Pendiente | Por especificar |
| 47 | `HU-CXC-001` | Usuario | Distinguir deudas y custodia | S4 | HU-INV-003, HU-VEN-001, HU-INV-001 | Pendiente | Ajustes P-09 |
| 48 | `HU-CXC-002` | Usuario | Registrar un abono | S4 | HU-CXC-001 | Pendiente | Sobrepagos P-09 |
| 49 | `HU-CXC-003` | Usuario | Rendir cuentas de la feria | S4 | HU-INV-004, HU-VEN-001, HU-CXC-001 | Pendiente | Por especificar |
| 50 | `HU-GAS-002` | Usuario | Consultar resumen económico | S4 | HU-GAS-001, HU-VEN-001, HU-CXC-001 | Pendiente | Por especificar |
| 51 | `HT-GEN-007` | Técnica | Generar reportes PDF verificables | S5 | HT-GEN-002; datos de cada reporte | Pendiente | Por especificar |
| 52 | `HU-REP-001` | Usuario | Consultar reporte de asistencia | S5 | HU-ASI-001, HU-ASI-003 | Pendiente | Por especificar |
| 53 | `HU-REP-002` | Usuario | Consultar reporte de actividades | S5 | HU-PLA-001, HU-PLA-003 | Pendiente | Por especificar |
| 54 | `HU-REP-003` | Usuario | Consultar reporte productivo | S5 | HU-TRA-001, HU-TRA-002, HU-TRA-004, HU-TRA-005 | Pendiente | Por especificar |
| 55 | `HU-REP-004` | Usuario | Consultar reporte de inventario | S5 | HU-INV-002, HU-INV-004 | Pendiente | Por especificar |
| 56 | `HU-REP-005` | Usuario | Consultar reporte de ventas y saldos | S5 | HU-VEN-001, HU-CXC-001, HU-CXC-002 | Pendiente | Por especificar |
| 57 | `HU-REP-006` | Usuario | Consultar mi resumen privado | S5 | HU-ASI-004, HU-PLA-004, HU-CXC-001 | Pendiente | Por especificar |
| 58 | `HU-NOT-001` | Usuario | Recibir recordatorios internos | S5 | HU-PLA-004, HU-ACC-003 | Pendiente | Por especificar |
| 59 | `HU-PUB-002` | Usuario | Gestionar contenido público | S5 | HU-ACC-003, HT-GEN-002 | Pendiente | Publicadores P-12 |
| 60 | `HU-PUB-001` | Usuario | Conocer información pública aprobada | S5 | HU-PUB-002, HT-GEN-002 | Pendiente | Contenido P-12 |

## Refinamiento y paso a sprint

1. El tesista revisa con las representantes el valor y el orden propuesto, y registra cambios con fecha, motivo y versión. No se altera silenciosamente la línea base de requisitos.
2. Antes de pasar un elemento al sprint, se completan sus reglas pendientes, dependencias, criterios verificables y estimación del equipo. El trabajo grande se divide en tareas manejables dentro de la planificación del sprint.
3. Al cerrar cada sprint se actualizan estado, evidencia, estimación restante y orden de los elementos todavía pendientes. Mejoras o correcciones nuevas se incorporan con fuente y aprobación proporcional.
4. La revisión de la directora y la validación organizacional de los ajustes v1.1 se registran cuando ocurran; no se presumen en esta edición.

## Límites

- `RF-COS-001` y `RNF-OPS-001` continúan propuestos y no son elementos de implementación confirmada en esta pila. Una exploración sobre despliegue no aprueba la política de respaldos.
- La planificación de cinco sprints organiza el avance del 13 de octubre al 21 de diciembre de 2026, con cierre del 22 al 23 de diciembre. El orden exacto y la capacidad de cada sprint necesitan refinamiento.
- Las historias de usuario detallan rol, función, beneficio y pruebas de aceptación; las técnicas detallan los trabajos habilitadores. Esta pila mantiene una referencia por ID para evitar duplicar sus fichas.

## Historial de esta edición candidata

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Codex | Pila ordenada de 51 historias de usuario y 9 técnicas, con dependencias y estimación pendiente. | Candidato interno |
