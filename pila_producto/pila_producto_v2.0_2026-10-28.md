---
titulo: Pila de producto con campos separados
version: "2.0"
actualizacion_diseno: "UI-01 a UI-08; instruccion del tesista; cumplimiento pendiente"
fecha: 2026-10-28
autor: Franklin Acero
estado: alcance-multicanal-aceptado-por-tesista-revision-academica-pendiente
elementos_base: 60
elementos_listados_ordenados: 71
adiciones_acceso_multicanal: 6
historias_usuario: 55
historias_usuario_base: 51
historias_usuario_acceso: 4
historias_tecnicas: 11
historias_tecnicas_base: 9
historias_tecnicas_acceso: 2
historias_tecnicas_planificadas_s1: 5
historias_tecnicas_aceptadas_s1: 5
historias_tecnicas_aun_propuestas: 5
historias_superadmin_candidatas_fuera_de_base: 5
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-transferencia
---

## Precisión transversal de diseño — 2026-10-28

Esta edición conserva íntegro el alcance de la edición anterior y añade la instrucción
expresa del tesista sobre interfaces coherentes: UI-01 carga, UI-02 adaptación, UI-03
jerarquía, UI-04 tokens, UI-05 componentes, UI-06 accesibilidad, UI-07 estados y UI-08
interacción. Los criterios y su comprobación están en [Criterios de diseño v1.1](../diseno/criterios_diseno_v1.1_2026-10-28.md).
Precisan RNF-UX-001 a 003 y RNF-CON-001, HT-GEN-004 y las HU con interfaz. Se aplican
a la porción nueva o modificada; SB-S1-04 conserva su historial y SB-S2-02 su avance.
No cambian los IDs, conteos, prioridades, fechas, estimaciones ni estados de terminación.
La identidad visual sigue provisional. Registrar reglas no acredita implementación,
pruebas de interfaz, validación con usuarias ni aprobación académica.

Edición anterior conservada: [pila_producto_v1.9_2026-10-28.md](pila_producto_v1.9_2026-10-28.md).



# Pila de producto

La línea base conserva 51 historias de usuario y 9 historias técnicas (60 posiciones). La lista principal conserva esas 60 historias junto con las cinco HT-PRE aceptadas para S1 el 2026-10-21. Esta edición añade cinco historias candidatas de Superadministración fuera de la línea base. El orden y las columnas de sprint de la lista principal reflejan el corte anterior; el orden de ejecución propuesto S2–S5 se presenta abajo. Las decisiones no completan tareas ni validan automáticamente requisitos. Cada columna muestra **un solo dato**. Los detalles y dependencias están en las fichas de [HU v2.7](../historias/usuario/historias_usuario_v2.7_2026-10-28.md), [HT v1.8](../historias/tecnicas/historias_tecnicas_v1.8_2026-10-28.md) y el [plan v1.6](../sprints/plan_sprints_v1.6_2026-10-27.md).

## Actualización de acceso del 2026-10-28

Esta edición conserva la [pila_producto_v1.8_2026-10-27.md](pila_producto_v1.8_2026-10-27.md) y registra el plan de acceso por correo, passkeys y WhatsApp aceptado expresamente por el tesista. RF-ACC-006 a 009, HU-ACC-010 a 013 y SB-S2-05 a 09 identifican la ampliación. Su implementación está pendiente; no se atribuyen pruebas, validación con usuarias ni publicación al docente. RF-ACC-005 conserva estado propuesto. La aceptación no fija puntos ni fechas nuevas.


## Listado principal conservado del corte anterior

El listado principal reúne las 60 historias de la línea base y las cinco historias técnicas aceptadas para S1 el 2026-10-21 (65 registros en total). Las cinco HT-PRE se incorporan en el bloque S1; la columna «Origen» distingue las entradas de línea base de las aceptadas por el tesista. Las filas conservan el primer sprint previsto en el corte del 2026-10-21 para trazabilidad. S1 fue extendido hasta el 2026-10-27 por decisión posterior del tesista; su cierre por calendario no completa tareas ni valida requisitos o criterios. Las etiquetas S6 de este listado pertenecen al corte anterior y no crean un S6 en el plan vigente.

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

## Orden de ejecución propuesto hasta el 23 de diciembre

La pila expresa valor y dependencias. Esta vista orienta el refinamiento de cada
sprint; no compromete todas las historias de un grupo ni altera su estado de
cumplimiento. La capacidad comunicada por el tesista es de 16–25 horas semanales.

| Secuencia | Bloque y referencias | Primer recorrido priorizado | Condición |
|---:|---|---|---|
| 1 | S2: `HU-ACC-001/002/003/004`, `HU-ACC-005/006/007` candidatas | Login, cuentas, autoridad transversal, permisos y estructura del panel. | RF-ACC-005 y configuración nueva requieren criterios validados; recuperación y delegación posterior siguen condicionadas. |
| 2 | S3: `HU-PLA-001` a `HU-PLA-005` | Programar, asignar y consultar trabajo organizacional. | Cada operación del módulo incluye acceso de Superadministradora y prueba de denegación. |
| 3 | S4: `HU-ASI-001` a `HU-ASI-007`, `HU-PWA-001/002/003` | Registrar y corregir asistencia sin duplicados. | Reglas de QR y continuidad sin red sujetas a decisiones pendientes; el panel ofrece operaciones del módulo que se implementen. |
| 4 | S5: `HU-CAT-001`, `HU-TRA-001` a `HU-TRA-005`, `HU-INV-001` a `HU-INV-004` y comercio relacionado | Seguir un lote desde materia recibida hasta existencias comprobables. | Comercio y rendición entran según capacidad y reglas aprobadas; no se comprometen las 23 historias antes agrupadas en S5. |
| Transversal | `HU-ACC-008/009` candidatas; reportes de cada módulo | Opciones, valores, registros y reportes administrables desde el panel. | Se entregan con el módulo propietario, no como funciones vacías en S2. |

## Inserción priorizada de acceso multicanal en S2

Después de la base de acceso HU-ACC-001 y antes de las ampliaciones funcionales aún no implementadas, se insertan seis registros aceptados. Las 65 filas anteriores se conservan como corte histórico; el listado vigente contiene 71 registros principales más las cinco HU candidatas y cinco HT aún propuestas separadas. No se trasladan tareas terminadas ni se inventan estimaciones.

| Orden del incremento | Código | Tipo | Nombre | Sprint | Dependencia | Estado |
|---:|---|---|---|---|---|---|
| 1 | `HT-ACC-001` | Técnica | Separar envíos y proteger desafíos de autenticación | S2 | Base de acceso; ver tareas SB-S2-05 a 09 | Aceptada en el plan; pendiente de implementación |
| 2 | `HU-ACC-010` | Usuario | Ingresar mediante código por correo | S2 | Base de acceso; ver tareas SB-S2-05 a 09 | Aceptada en el plan; pendiente de implementación |
| 3 | `HT-ACC-002` | Técnica | Verificar WebAuthn y gestionar el ciclo de passkeys | S2 | Base de acceso; ver tareas SB-S2-05 a 09 | Aceptada en el plan; pendiente de implementación |
| 4 | `HU-ACC-011` | Usuario | Registrar y utilizar passkeys | S2 | Base de acceso; ver tareas SB-S2-05 a 09 | Aceptada en el plan; pendiente de implementación |
| 5 | `HU-ACC-012` | Usuario | Ingresar mediante código por WhatsApp | S2 | Base de acceso; ver tareas SB-S2-05 a 09 | Aceptada en el plan; pendiente de implementación |
| 6 | `HU-ACC-013` | Usuario | Recuperar el acceso y proteger la cuenta | S2 | Base de acceso; ver tareas SB-S2-05 a 09 | Aceptada en el plan; pendiente de implementación |

Correo habilita recuperación antes de registrar passkeys. WhatsApp puede desarrollarse en paralelo después de la seguridad común, con entrega real condicionada al proveedor y costo. Se mantienen pendientes de validación los detalles de RF-ACC-005 y las operaciones de otros módulos.

## Historias candidatas de Superadministración

Las siguientes cinco historias quedan **fuera de las 60 posiciones de la línea base**
y de las 65 filas conservadas en el listado principal. El tesista decidió que una
Superadministradora pueda realizar todas las acciones ordinarias de cada módulo y
administrar desde el panel accesos, asistencia, registros, valores de campos
existentes y opciones publicadas, sin asignación individual por módulo. El requisito
`RF-ACC-005` y el detalle de estas fichas mantienen estado propuesto.

| Código | Tipo | Nombre | Prioridad | Ubicación de trabajo | Estado |
|---|---|---|---|---|---|
| `HU-ACC-005` | Usuario | Asignar o retirar acceso a módulos | Pendiente de validar | Base S2; acciones de módulo S3–S5 | Propuesta |
| `HU-ACC-006` | Usuario | Conceder o revocar autoridad administrativa | Pendiente de validar | Primera designación S2; delegación posterior según regla validada | Propuesta |
| `HU-ACC-007` | Usuario | Consultar intentos y configurar acceso | Pendiente de validar | S2, condicionada a límites y SPEC-001 | Propuesta |
| `HU-ACC-008` | Usuario | Editar opciones y valores configurables de módulos | Pendiente de validar | S3–S5 con cada módulo | Propuesta |
| `HU-ACC-009` | Usuario | Crear y corregir registros de cualquier módulo | Pendiente de validar | S3–S5 con cada módulo | Propuesta |

El panel no crea campos físicos ni altera el esquema de la base de datos. Las
operaciones conservan las validaciones, aprobaciones aplicables y el historial del
módulo. La evidencia de validación presidencial reportada por el tesista sigue
pendiente de adjuntar.

## Historias técnicas aún propuestas para S3–S6

Estas cinco historias permanecen separadas del listado principal: no forman parte de las 60 historias de línea base ni de las cinco asignaciones aceptadas para S1. Las referencias S6 de esta tabla son históricas y se refinan para S3–S5 o para integración y entrega, sin cambiar automáticamente su estado.

| N.º | Código | Nombre | Prioridad propuesta | Sprint previsto | Estado |
|---:|---|---|---|---|---|
| 1 | `HT-S3-001` | Preparar pruebas de planificación y regresión de permisos sobre actividades y encargos. | Alta | S3 | Propuesta |
| 2 | `HT-S4-001` | Precisar y probar QR, alternativa de registro y operaciones de asistencia sin red antes de implementarlas. | Alta | S4 | Propuesta |
| 3 | `HT-S5-001` | Probar la cadena productiva y las operaciones comerciales que entren realmente al sprint. | Crítica | S5 | Propuesta |
| 4 | `HT-S6-001` | Ejecutar integración, pruebas funcionales y de uso, continuidad aprobada y regresión. | Crítica | S6 | Propuesta |
| 5 | `HT-S6-002` | Preparar manuales, capacitación y acta de validación final. | Alta | S6 y cierre | Propuesta |

## Pendientes para planificar

Las reglas P-02 a P-14, la revisión académica y la estimación se registran antes de comprometer una historia. La capacidad comunicada de 16–25 horas semanales no sustituye la estimación ni compromete la pila. Las necesidades adicionales de entrevista permanecen en la [edición anterior](pila_producto_v1.4_2026-10-13.md) hasta que se validen. El orden puede cambiar con una decisión humana registrada.

## Historial de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 1.4 | 2026-10-13 | Nivel cualitativo de HU separado de posición en pila. |
| 1.5 | 2026-10-13 | Columnas independientes y tabla aparte para HT adicionales. |
| 1.6 | 2026-10-14 | Se separan cinco HT planificadas para S1 de cinco propuestas posteriores; la base conserva 60 posiciones. |
| 1.7 | 2026-10-21 | Se ordena el listado principal por sprint desde S1 y se integran HT-PRE-001 a HT-PRE-005 como adiciones aceptadas; se mantienen las 60 historias de línea base y sus estados de cumplimiento. |
| 1.8 | 2026-10-27 | Se conserva la lista principal de 65 filas, se añaden cinco historias candidatas de Superadministración fuera de la línea base y se muestra el orden de trabajo S2–S5 sin marcar compromisos ni terminación. Preparada para revisión; no publicada. |

| 1.9 | 2026-10-28 | Inserta cuatro HU y dos HT de acceso multicanal aceptado para S2; conserva el listado histórico, la prioridad de dependencias y todos los estados pendientes. |


## Control editorial de esta edición

1.9 → 2.0, 2026-10-28: precisión de criterios UI-01 a UI-08; fuentes y fichas previas conservadas. Revisión académica y publicación pendientes.
