---
titulo: Pila de producto con campos separados
version: "1.8"
fecha: 2026-10-27
autor: Tesista
estado: propuesta-interna-pendiente-de-validacion
elementos_base: 60
elementos_listados_ordenados: 65
historias_usuario: 51
historias_tecnicas: 9
historias_tecnicas_planificadas_s1: 5
historias_tecnicas_aceptadas_s1: 5
historias_tecnicas_aun_propuestas: 5
historias_superadmin_candidatas_fuera_de_base: 5
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Pila de producto

La copia mantiene la línea base de 51 historias de usuario y 9 historias técnicas (60 elementos), y su lista principal de 65 filas, que incluye las cinco HT-PRE aceptadas para S1 el 2026-10-21. Esta v1.8 es una propuesta interna basada en la [pila v1.7](../../../documentacion/pila_producto/pila_producto_v1.7_2026-10-21.md) y agrega cinco historias candidatas fuera de la línea base. El tesista decidió el 2026-10-27 definir el acceso y la superadministración en S1, implementar la base de acceso y permisos en S2 y las funciones de cada módulo en S3–S5. La presidenta validó el rol de superadministradora con autoridad para gestionar todo el sistema, según el tesista; la evidencia queda pendiente de adjuntar. Las historias de usuario se detallan en [[2026-10-27-historias-usuario-v2.6-superadmin|la propuesta v2.6]]; las historias técnicas vigentes están en [v1.7](../../../documentacion/historias/tecnicas/historias_tecnicas_v1.7_2026-10-21.md). La capacidad comunicada es 16–25 horas semanales; prioridades y estimaciones por historia siguen pendientes.

## Listado principal del corte anterior, ordenado por primer sprint previsto

El listado principal reúne las 60 historias de la línea base y las cinco historias técnicas aceptadas para S1 el 2026-10-21 (65 registros en total). Las cinco HT-PRE se incorporan en el bloque S1; la columna «Origen» distingue las entradas de línea base de las aceptadas por el tesista. Las filas y su columna de sprint conservan el corte del 2026-10-21 para trazabilidad; la ejecución S2–S5 se rige por la hoja de ruta del 2026-10-27 y se afina al seleccionar historias. La nota del 2026-10-21 decía que esa aceptación no reabría el timebox; la decisión expresa del tesista del 2026-10-27 amplía el periodo documental de S1 hasta esa fecha para definir acceso y superadministración. La ampliación no completa tareas ni valida por sí sola requisitos o criterios.

| Orden | Código | Tipo | Nombre | Prioridad propuesta | Sprint previsto | Origen |
|---:|---|---|---|---|---|---|
| 1 | `HT-PRE-001` | Técnica | Levantar y consolidar entrevistas, observación y documentos disponibles. | Alta | S1 | Aceptada 2026-10-21 |
| 2 | `HT-PRE-002` | Técnica | Validar alcance, requisitos, reglas y criterios de aceptación con las personas competentes. | Crítica | S1 | Aceptada 2026-10-21 |
| 3 | `HT-PRE-003` | Técnica | Preparar arquitectura, modelo conceptual y límites de datos por módulo. | Alta | S1 | Aceptada 2026-10-21 |
| 4 | `HT-PRE-004` | Técnica | Diseñar recorridos móviles y preparación PWA sin afirmar que la aplicación ya funciona. | Alta | S1 | Aceptada 2026-10-21 |
| 5 | `HT-PRE-005` | Técnica | Refinar historias, pila, dependencias, estimaciones y calendario con capacidad real. | Alta | S1 | Aceptada 2026-10-21 |
| 6 | `HT-GEN-008` | Técnica | Explorar despliegue y recuperación | Alta | S1; revisión en S6 | Línea base |
| 7 | `HT-GEN-001` | Técnica | Preparar la base modular Django | Crítica | S2 | Línea base |
| 8 | `HT-GEN-009` | Técnica | Preparar pruebas y trazabilidad | Crítica | Transversal desde S2 | Línea base |
| 9 | `HT-GEN-002` | Técnica | Aplicar autorización en el servidor | Crítica | Transversal desde S2 | Línea base |
| 10 | `HT-GEN-004` | Técnica | Preparar componentes móviles y accesibles | Alta | Transversal desde S2 | Línea base |
| 11 | `HU-ACC-001` | Usuario | Entrar y salir de la parte privada | Esencial | S2 | Línea base |
| 12 | `HU-ACC-002` | Usuario | Administrar membresías | Alta | S2 | Línea base |
| 13 | `HU-ACC-003` | Usuario | Usar funciones según responsabilidades | Esencial | S2 | Línea base |
| 14 | `HU-ACC-004` | Usuario | Ver mis opciones disponibles | Complementaria | S2 | Línea base |
| 15 | `HU-PLA-001` | Usuario | Programar una actividad | Alta | S3 | Línea base |
| 16 | `HU-PLA-002` | Usuario | Asignar participantes y responsables | Alta | S3 | Línea base |
| 17 | `HU-PLA-003` | Usuario | Crear un encargo temporal | Alta | S3 | Línea base |
| 18 | `HU-PLA-004` | Usuario | Consultar mis actividades | Complementaria | S3 | Línea base |
| 19 | `HU-PLA-005` | Usuario | Planificar producción semanal | Alta | S3 | Línea base |
| 20 | `HT-GEN-003` | Técnica | Asegurar integridad y auditoría | Crítica | Transversal desde S4 | Línea base |
| 21 | `HT-GEN-005` | Técnica | Preparar captura local protegida | Alta | Transversal S4/S5 | Línea base |
| 22 | `HT-GEN-006` | Técnica | Sincronizar sin duplicados | Crítica | Transversal S4/S5 | Línea base |
| 23 | `HU-PWA-001` | Usuario | Abrir tareas habilitadas sin conexión | Esencial | Transversal S4/S5 | Línea base |
| 24 | `HU-PWA-002` | Usuario | Conservar registros pendientes sin conexión | Esencial | Transversal S4/S5 | Línea base |
| 25 | `HU-PWA-003` | Usuario | Sincronizar registros pendientes | Esencial | Transversal S4/S5 | Línea base |
| 26 | `HU-ASI-001` | Usuario | Registrar entrada y salida | Esencial | S4 | Línea base |
| 27 | `HU-ASI-002` | Usuario | Evitar asistencia duplicada | Esencial | S4 | Línea base |
| 28 | `HU-ASI-003` | Usuario | Corregir asistencia con historial | Esencial | S4 | Línea base |
| 29 | `HU-ASI-004` | Usuario | Consultar historial de asistencia | Complementaria | S4 | Línea base |
| 30 | `HU-ASI-005` | Usuario | Registrar participación adicional | Complementaria | S4 | Línea base |
| 31 | `HU-ASI-006` | Usuario | Resolver una inconsistencia de asistencia | Alta | S4 | Línea base |
| 32 | `HU-ASI-007` | Usuario | Registrar asistencia con QR o alternativa | Alta | S4 | Línea base |
| 33 | `HU-CAT-001` | Usuario | Mantener catálogo productivo | Esencial | S5 | Línea base |
| 34 | `HU-INV-001` | Usuario | Conservar valores comerciales históricos | Esencial | S5 | Línea base |
| 35 | `HU-TRA-001` | Usuario | Registrar acopio de materia | Esencial | S5 | Línea base |
| 36 | `HU-TRA-002` | Usuario | Registrar secado | Esencial | S5 | Línea base |
| 37 | `HU-TRA-003` | Usuario | Conocer duración y merma | Alta | S5 | Línea base |
| 38 | `HU-TRA-004` | Usuario | Seguir la procedencia de lotes | Esencial | S5 | Línea base |
| 39 | `HU-TRA-005` | Usuario | Registrar transformación | Esencial | S5 | Línea base |
| 40 | `HU-INV-002` | Usuario | Reconstruir existencias | Esencial | S5 | Línea base |
| 41 | `HU-INV-003` | Usuario | Entregar productos para feria | Alta | S5 | Línea base |
| 42 | `HU-INV-004` | Usuario | Conciliar productos de feria | Alta | S5 | Línea base |
| 43 | `HU-VEN-001` | Usuario | Registrar una venta | Esencial | S5 | Línea base |
| 44 | `HU-VEN-002` | Usuario | Identificar comprador según la venta | Alta | S5 | Línea base |
| 45 | `HU-VEN-003` | Usuario | Conocer valor base y excedente | Esencial | S5 | Línea base |
| 46 | `HU-VEN-004` | Usuario | Autorizar venta bajo valor base | Esencial | S5 | Línea base |
| 47 | `HU-VEN-005` | Usuario | Configurar descuento por volumen | Complementaria | S5 | Línea base |
| 48 | `HU-VEN-006` | Usuario | Distinguir stock individual y compartido | Alta | S5 | Línea base |
| 49 | `HU-VEN-007` | Usuario | Registrar venta institucional | Alta | S5 | Línea base |
| 50 | `HU-VEN-008` | Usuario | Conciliar comprobante manual de feria | Alta | S5 | Línea base |
| 51 | `HU-GAS-001` | Usuario | Registrar gasto operativo | Alta | S5 | Línea base |
| 52 | `HU-CXC-001` | Usuario | Distinguir deudas y custodia | Esencial | S5 | Línea base |
| 53 | `HU-CXC-002` | Usuario | Registrar un abono | Esencial | S5 | Línea base |
| 54 | `HU-CXC-003` | Usuario | Rendir cuentas de la feria | Alta | S5 | Línea base |
| 55 | `HU-GAS-002` | Usuario | Consultar resumen económico | Complementaria | S5 | Línea base |
| 56 | `HT-GEN-007` | Técnica | Generar reportes PDF verificables | Alta | S6 | Línea base |
| 57 | `HU-REP-001` | Usuario | Consultar reporte de asistencia | Alta | S6 | Línea base |
| 58 | `HU-REP-002` | Usuario | Consultar reporte de actividades | Alta | S6 | Línea base |
| 59 | `HU-REP-003` | Usuario | Consultar reporte productivo | Alta | S6 | Línea base |
| 60 | `HU-REP-004` | Usuario | Consultar reporte de inventario | Alta | S6 | Línea base |
| 61 | `HU-REP-005` | Usuario | Consultar reporte de ventas y saldos | Alta | S6 | Línea base |
| 62 | `HU-REP-006` | Usuario | Consultar mi resumen privado | Complementaria | S6 | Línea base |
| 63 | `HU-NOT-001` | Usuario | Recibir recordatorios internos | Complementaria | S6 | Línea base |
| 64 | `HU-PUB-002` | Usuario | Gestionar contenido público | Complementaria | S6 | Línea base |
| 65 | `HU-PUB-001` | Usuario | Conocer información pública aprobada | Complementaria | S6 | Línea base |

## Historias técnicas aún propuestas para S3–S6

Estas cinco historias permanecen separadas del listado principal: no forman parte de las 60 historias de línea base ni de las cinco asignaciones aceptadas para S1.

| N.º | Código | Nombre | Prioridad propuesta | Sprint previsto | Estado |
|---:|---|---|---|---|---|
| 1 | `HT-S3-001` | Preparar pruebas de planificación y regresión de permisos sobre actividades y encargos. | Alta | S3 | Propuesta |
| 2 | `HT-S4-001` | Precisar y probar QR, alternativa de registro y operaciones de asistencia sin red antes de implementarlas. | Alta | S4 | Propuesta |
| 3 | `HT-S5-001` | Probar la cadena productiva y las operaciones comerciales que entren realmente al sprint. | Crítica | S5 | Propuesta |
| 4 | `HT-S6-001` | Ejecutar integración, pruebas funcionales y de uso, continuidad aprobada y regresión. | Crítica | S6 | Propuesta |
| 5 | `HT-S6-002` | Preparar manuales, capacitación y acta de validación final. | Alta | S6 y cierre | Propuesta |

## Elementos candidatos de administración organizacional

Estas historias permanecen fuera de las 60 posiciones de la línea base y conservan estado
propuesto. Su definición general corresponde a S1; la base de cuentas y permisos se
ubica en S2 y las operaciones de negocio en S3–S5 con el módulo propietario.
El tesista decidió que la Superadministradora podrá realizar todas las acciones de una
usuaria normal en cada módulo y además administrar registros, valores de campos
existentes y opciones publicadas desde su panel. Esta autoridad transversal no exige
asignación individual de módulo y no crea campos físicos desde la interfaz.

| Código | Tipo | Nombre | Prioridad | Sprint | Estado |
|---|---|---|---|---|---|
| `HU-ACC-005` | Usuario | Asignar o retirar acceso a módulos | Pendiente | Definición S1; implementación S2 | Propuesta |
| `HU-ACC-006` | Usuario | Conceder o revocar autoridad administrativa | Pendiente | Alta inicial autorizada en S2; delegación posterior sujeta a regla | Propuesta |
| `HU-ACC-007` | Usuario | Consultar intentos recientes y configurar bloqueo de acceso | Pendiente | Definición S1; implementación S2 | Propuesta |
| `HU-ACC-008` | Usuario | Editar opciones, valores de campos existentes, catálogos y fórmulas expuestos por los módulos | Pendiente | Permisos base S2; detalle e implementación por módulo S3–S5 | Propuesta |
| `HU-ACC-009` | Usuario | Crear, consultar y corregir asistencia y otros registros mediante el módulo propietario | Pendiente | Permisos base S2; detalle e implementación por módulo S3–S5 | Propuesta |

Los refinamientos de HU-ACC-002 y HU-ACC-003 continúan vinculados a sus posiciones de la línea
base. Su definición se incorpora al trabajo documental de S1; la prioridad y la estimación
siguen pendientes. `SB-S2-02` permanece como implementación activa de S2 y no se declara
terminado por este cambio.

## Decisión operativa del tesista: S1 documental y S2 de implementación — 2026-10-27

| Campo | Registro |
|---|---|
| Autor y fecha | Tesista, 2026-10-27 |
| S1 | Definición documental integral de login, sesión y superadministración, con término indicado para el 2026-10-27. La fuente v1.4 inicia S1 el 2026-09-15. |
| Entregables de definición y validación | Requisitos, historias, especificación, matriz de permisos y diseño de pantallas, con registro de la validación correspondiente. |
| S2 | Acceso, cuentas y estructura de permisos; comenzó el 2026-10-14 y tiene cierre propuesto para el 2026-11-08 tras la replanificación. |
| S3–S5 | Funciones de gestión organizacional y trazabilidad por módulos, según capacidad y reglas validadas. |
| Capacidad y estimaciones | El tesista comunicó 16–25 horas semanales; estimaciones por historia pendientes. |
| Estado de cumplimiento | La fecha de término de S1 queda fijada por la decisión; el cotejo de entregables y su finalización real siguen pendientes. |
| Solapamiento | Las fechas comunicadas hacen que S1 y S2 se solapen del 2026-10-14 al 2026-10-27. Se registra el intervalo reportado sin inferir un corte distinto. |
| Validación presidencial del rol | «validado por la presidenta (según el tesista)»; evidencia: pendiente de adjuntar. |

Esta decisión reemplaza para acceso y superadministración la nota previa de no alterar S1–S6 y
de dejar la administración para después del trabajo activo de acceso. También sustituye, para
este alcance, la nota del 2026-10-21 de que las HT-PRE aceptadas no reabrían el timebox de S1.
Los registros anteriores se conservan como historia. La decisión de asignación a sprint no
aprueba `RF-ACC-005`, SPEC-002 ni cada criterio candidato.

En S1 se define el proceso completo de login, sesiones, cuentas, política de acceso,
superadministración y configuración base de acceso. También se identifica qué configuraciones
y operaciones ofrece cada módulo. La profundidad de altas, cambios, bajas y correcciones de
datos, así como las fórmulas y catálogos concretos, se define módulo por módulo; esos detalles
no quedan cerrados en S1 por esta decisión.

## Pendientes para planificar

Las reglas P-02 a P-14, la revisión académica y la estimación se registran antes de cerrar cada detalle afectado. Las necesidades adicionales de entrevista permanecen en la [edición anterior](../../../documentacion/pila_producto/pila_producto_v1.4_2026-10-13.md) hasta que se validen. La capacidad histórica de S1 y la estimación del trabajo de S2 siguen pendientes.

## Historial de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 1.4 | 2026-10-13 | Nivel cualitativo de HU separado de posición en pila. |
| 1.5 | 2026-10-13 | Columnas independientes y tabla aparte para HT adicionales. |
| 1.6 | 2026-10-14 | Se separan cinco HT planificadas para S1 de cinco propuestas posteriores; la base conserva 60 posiciones. |
| 1.7 | 2026-10-21 | Se ordena el listado principal por sprint desde S1 y se integran HT-PRE-001 a HT-PRE-005 como adiciones aceptadas; se mantienen las 60 historias de línea base y sus estados de cumplimiento. |
| 1.8 | 2026-10-27 | Candidata interna: conserva la lista base de 65 filas y añade cinco historias del superpanel; registra por decisión del tesista la definición en S1 y la implementación en S2, con fechas comunicadas, capacidad pendiente y validación presidencial del rol atribuida al tesista. |
