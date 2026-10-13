---
titulo: Pila de producto de Zhud Alelí
version: "1.3"
fecha: 2026-10-13
autor: Tesista
estado: final-documental
fuente_entrevista: EVID-ENT-2026-10-12-001
fuente_requisitos: "CAT-REQ-001 v1.1"
fuente_formato: "Material de Aplicaciones Informáticas II, sección 2.8"
elementos: 60
historias_usuario: 51
historias_tecnicas: 9
prioridad: orden-preliminar-por-validar
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Pila de producto

## Visión del producto

La aplicación debe ayudar al Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud a organizar actividades, registrar asistencia, seguir la producción y rendir cuentas de existencias y ventas. Debe funcionar en móvil y conservar las operaciones habilitadas durante cortes de conexión. La **línea base de esta pila** reúne **51 historias de usuario** derivadas de requisitos funcionales confirmados y **9 historias técnicas** que las habilitan. Diez trabajos técnicos nuevos aparecen más abajo como **candidatos fuera de las 60 posiciones**.

## Cómo se lee el orden

La posición 1 es el primer lugar en la secuencia **propuesta** de la línea base; combina dependencias, valor y los cinco bloques funcionales. **No es el nivel de prioridad**: para las HT se añade una clasificación Crítica, Alta, Media o Baja, definida en la [edición técnica v1.4](../historias/tecnicas/historias_tecnicas_v1.4_2026-10-13.md). Ni el orden ni el nivel equivalen a compromiso de incluir todo en un sprint. La estimación de todos los elementos sigue **pendiente del equipo**, sin horas ni puntos inventados.

El estado de preparación distingue una capacidad confirmada de sus detalles aún abiertos. Una decisión P pendiente impide cerrar la porción afectada; no elimina la capacidad aprobada. Ningún elemento se declara implementado.

**Calendario:** S1 cubre requisitos y diseño del 15 de septiembre al 12 de octubre de 2026. Los bloques funcionales que en la edición anterior se llamaban S1–S5 pasan a ser S2–S6 desde el 13 de octubre hasta el 21 de diciembre. Solo cambia la numeración editorial; ninguna especificación aprobada se altera automáticamente.

## Nivel de prioridad de las nueve HT existentes

| Nivel | Historias técnicas | Razón principal |
|---|---|---|
| Crítica | `HT-GEN-001`, `HT-GEN-002`, `HT-GEN-003`, `HT-GEN-006`, `HT-GEN-009` | Base de la aplicación, permisos, integridad, sincronización y evidencia de calidad. |
| Alta | `HT-GEN-004`, `HT-GEN-005`, `HT-GEN-007`, `HT-GEN-008` | Uso móvil, captura local, reportes y preparación de entrega. |
| Media o baja | Ninguna por ahora. | El nivel se revisa al estimar y seleccionar trabajo. |

`HU-CAT-001` se adelanta en este orden respecto de su Sprint 5 previsto porque la planificación semanal (`HU-PLA-005`) necesita identificar productos. Ese adelanto es una propuesta de dependencia para el refinamiento, no un cambio aprobado de fechas.

## Elementos ordenados por prioridad propuesta

### Posiciones 1 a 15

| Orden | ID y tipo | Elemento | Etapa prevista | Dependencias | Preparación y estimación |
|---:|---|---|---|---|---|
| 1 | `HT-GEN-008`<br>Técnica | Explorar despliegue y recuperación | S1; revisión en S6 | ADR-0006; P-11 para política de respaldo | Exploración; P-11 abierto<br>Estimación: Pendiente |
| 2 | `HT-GEN-001`<br>Técnica | Preparar la base modular Django | S2 | SPEC-001; ADR-0006 | Por especificar<br>Estimación: Pendiente |
| 3 | `HT-GEN-009`<br>Técnica | Preparar pruebas y trazabilidad | Transversal desde S2 | HT-GEN-001 | Por especificar<br>Estimación: Pendiente |
| 4 | `HT-GEN-002`<br>Técnica | Aplicar autorización en el servidor | Transversal desde S2 | HT-GEN-001 | Por especificar<br>Estimación: Pendiente |
| 5 | `HT-GEN-004`<br>Técnica | Preparar componentes móviles y accesibles | Transversal desde S2 | HT-GEN-001 | Por especificar<br>Estimación: Pendiente |
| 6 | `HU-ACC-001`<br>Usuario | Entrar y salir de la parte privada | S2 | HT-GEN-001, HT-GEN-002 | SPEC-001 confirmada; sin implementación verificada<br>Estimación: Pendiente |
| 7 | `HU-ACC-002`<br>Usuario | Administrar membresías | S2 | HU-ACC-001, HT-GEN-002 | Por especificar<br>Estimación: Pendiente |
| 8 | `HU-ACC-003`<br>Usuario | Usar funciones según responsabilidades | S2 | HU-ACC-001, HT-GEN-002 | Por especificar<br>Estimación: Pendiente |
| 9 | `HU-PLA-001`<br>Usuario | Programar una actividad | S3 | HU-ACC-003 | Por especificar<br>Estimación: Pendiente |
| 10 | `HU-PLA-002`<br>Usuario | Asignar participantes y responsables | S3 | HU-PLA-001, HU-ACC-003 | Por especificar<br>Estimación: Pendiente |
| 11 | `HU-PLA-003`<br>Usuario | Crear un encargo temporal | S3 | HU-PLA-001, HU-PLA-002 | Por especificar<br>Estimación: Pendiente |
| 12 | `HU-PLA-004`<br>Usuario | Consultar mis actividades | S3 | HU-PLA-001, HU-PLA-002 | Por especificar<br>Estimación: Pendiente |
| 13 | `HU-CAT-001`<br>Usuario | Mantener catálogo productivo | S5 | HU-ACC-003 | Detalle P-04<br>Estimación: Pendiente |
| 14 | `HU-PLA-005`<br>Usuario | Planificar producción semanal | S3 | HU-PLA-001, HU-CAT-001 | Por especificar<br>Estimación: Pendiente |
| 15 | `HU-ACC-004`<br>Usuario | Ver mis opciones disponibles | S2 | HU-ACC-001, HU-ACC-003 | Por especificar<br>Estimación: Pendiente |

### Posiciones 16 a 30

| Orden | ID y tipo | Elemento | Etapa prevista | Dependencias | Preparación y estimación |
|---:|---|---|---|---|---|
| 16 | `HT-GEN-003`<br>Técnica | Asegurar integridad y auditoría | Transversal desde S4 | HT-GEN-001 | Por especificar<br>Estimación: Pendiente |
| 17 | `HT-GEN-005`<br>Técnica | Preparar captura local protegida | Transversal S4/S5 | HT-GEN-002; P-13/P-14 | P-13/P-14 abiertos<br>Estimación: Pendiente |
| 18 | `HT-GEN-006`<br>Técnica | Sincronizar sin duplicados | Transversal S4/S5 | HT-GEN-003; HT-GEN-005; P-13/P-14 | P-13/P-14 abiertos<br>Estimación: Pendiente |
| 19 | `HU-PWA-001`<br>Usuario | Abrir tareas habilitadas sin conexión | Transversal S4/S5 | HT-GEN-005 | P-13/P-14 abiertos<br>Estimación: Pendiente |
| 20 | `HU-PWA-002`<br>Usuario | Conservar registros pendientes sin conexión | Transversal S4/S5 | HU-PWA-001, HT-GEN-005 | P-13/P-14 abiertos<br>Estimación: Pendiente |
| 21 | `HU-PWA-003`<br>Usuario | Sincronizar registros pendientes | Transversal S4/S5 | HU-PWA-002, HT-GEN-006 | P-13/P-14 abiertos<br>Estimación: Pendiente |
| 22 | `HU-ASI-001`<br>Usuario | Registrar entrada y salida | S4 | HU-PLA-001, HU-ACC-003; HU-PWA-002 solo para captura sin red | Captura sin red: P-13<br>Estimación: Pendiente |
| 23 | `HU-ASI-002`<br>Usuario | Evitar asistencia duplicada | S4 | HU-ASI-001 | Por especificar<br>Estimación: Pendiente |
| 24 | `HU-ASI-003`<br>Usuario | Corregir asistencia con historial | S4 | HU-ASI-001, HT-GEN-003 | Por especificar<br>Estimación: Pendiente |
| 25 | `HU-ASI-004`<br>Usuario | Consultar historial de asistencia | S4 | HU-ASI-001, HT-GEN-002 | Por especificar<br>Estimación: Pendiente |
| 26 | `HU-ASI-005`<br>Usuario | Registrar participación adicional | S4 | HU-PLA-001, HU-ASI-001 | Por especificar<br>Estimación: Pendiente |
| 27 | `HU-ASI-006`<br>Usuario | Resolver una inconsistencia de asistencia | S4 | HU-ASI-001, HU-ASI-003 | Por especificar<br>Estimación: Pendiente |
| 28 | `HU-ASI-007`<br>Usuario | Registrar asistencia con QR o alternativa | S4 | HU-ASI-001, HU-ACC-003 | P-02/P-13 abiertos<br>Estimación: Pendiente |
| 29 | `HU-INV-001`<br>Usuario | Conservar valores comerciales históricos | S5 | HU-CAT-001, HU-ACC-003 | Por especificar<br>Estimación: Pendiente |
| 30 | `HU-TRA-001`<br>Usuario | Registrar acopio de materia | S5 | HU-CAT-001, HU-PLA-003 | Captura sin red: P-13<br>Estimación: Pendiente |

### Posiciones 31 a 45

| Orden | ID y tipo | Elemento | Etapa prevista | Dependencias | Preparación y estimación |
|---:|---|---|---|---|---|
| 31 | `HU-TRA-002`<br>Usuario | Registrar secado | S5 | HU-TRA-001, HU-PLA-003 | Captura sin red: P-13<br>Estimación: Pendiente |
| 32 | `HU-TRA-003`<br>Usuario | Conocer duración y merma | S5 | HU-TRA-002 | Por especificar<br>Estimación: Pendiente |
| 33 | `HU-TRA-004`<br>Usuario | Seguir la procedencia de lotes | S5 | HU-TRA-001, HU-TRA-002 | Excepciones P-05<br>Estimación: Pendiente |
| 34 | `HU-TRA-005`<br>Usuario | Registrar transformación | S5 | HU-TRA-004, HU-CAT-001 | Por especificar<br>Estimación: Pendiente |
| 35 | `HU-INV-002`<br>Usuario | Reconstruir existencias | S5 | HU-CAT-001, HT-GEN-003 | Por especificar<br>Estimación: Pendiente |
| 36 | `HU-INV-003`<br>Usuario | Entregar productos para feria | S5 | HU-INV-002, HU-PLA-003 | Por especificar<br>Estimación: Pendiente |
| 37 | `HU-INV-004`<br>Usuario | Conciliar productos de feria | S5 | HU-INV-003, HU-INV-002 | Por especificar<br>Estimación: Pendiente |
| 38 | `HU-VEN-001`<br>Usuario | Registrar una venta | S5 | HU-INV-002, HU-INV-003, HT-GEN-003 | Por especificar<br>Estimación: Pendiente |
| 39 | `HU-VEN-002`<br>Usuario | Identificar comprador según la venta | S5 | HU-VEN-001 | Por especificar<br>Estimación: Pendiente |
| 40 | `HU-VEN-003`<br>Usuario | Conocer valor base y excedente | S5 | HU-VEN-001, HU-INV-001 | Por especificar<br>Estimación: Pendiente |
| 41 | `HU-VEN-004`<br>Usuario | Autorizar venta bajo valor base | S5 | HU-VEN-001, HU-VEN-003 | Por especificar<br>Estimación: Pendiente |
| 42 | `HU-VEN-005`<br>Usuario | Configurar descuento por volumen | S5 | HU-CAT-001, HU-INV-001, HU-VEN-001 | Parámetros P-08<br>Estimación: Pendiente |
| 43 | `HU-VEN-006`<br>Usuario | Distinguir stock individual y compartido | S5 | HU-INV-003, HU-VEN-001 | Reparto P-07 excluido<br>Estimación: Pendiente |
| 44 | `HU-VEN-007`<br>Usuario | Registrar venta institucional | S5 | HU-VEN-001, HU-VEN-002 | Por especificar<br>Estimación: Pendiente |
| 45 | `HU-VEN-008`<br>Usuario | Conciliar comprobante manual de feria | S5 | HU-VEN-001, HU-INV-004 | Procedimiento P-10<br>Estimación: Pendiente |

### Posiciones 46 a 60

| Orden | ID y tipo | Elemento | Etapa prevista | Dependencias | Preparación y estimación |
|---:|---|---|---|---|---|
| 46 | `HU-GAS-001`<br>Usuario | Registrar gasto operativo | S5 | HU-ACC-003 | Por especificar<br>Estimación: Pendiente |
| 47 | `HU-CXC-001`<br>Usuario | Distinguir deudas y custodia | S5 | HU-INV-003, HU-VEN-001, HU-INV-001 | Ajustes P-09<br>Estimación: Pendiente |
| 48 | `HU-CXC-002`<br>Usuario | Registrar un abono | S5 | HU-CXC-001 | Sobrepagos P-09<br>Estimación: Pendiente |
| 49 | `HU-CXC-003`<br>Usuario | Rendir cuentas de la feria | S5 | HU-INV-004, HU-VEN-001, HU-CXC-001 | Por especificar<br>Estimación: Pendiente |
| 50 | `HU-GAS-002`<br>Usuario | Consultar resumen económico | S5 | HU-GAS-001, HU-VEN-001, HU-CXC-001 | Por especificar<br>Estimación: Pendiente |
| 51 | `HT-GEN-007`<br>Técnica | Generar reportes PDF verificables | S6 | HT-GEN-002; datos de cada reporte | Por especificar<br>Estimación: Pendiente |
| 52 | `HU-REP-001`<br>Usuario | Consultar reporte de asistencia | S6 | HU-ASI-001, HU-ASI-003 | Por especificar<br>Estimación: Pendiente |
| 53 | `HU-REP-002`<br>Usuario | Consultar reporte de actividades | S6 | HU-PLA-001, HU-PLA-003 | Por especificar<br>Estimación: Pendiente |
| 54 | `HU-REP-003`<br>Usuario | Consultar reporte productivo | S6 | HU-TRA-001, HU-TRA-002, HU-TRA-004, HU-TRA-005 | Por especificar<br>Estimación: Pendiente |
| 55 | `HU-REP-004`<br>Usuario | Consultar reporte de inventario | S6 | HU-INV-002, HU-INV-004 | Por especificar<br>Estimación: Pendiente |
| 56 | `HU-REP-005`<br>Usuario | Consultar reporte de ventas y saldos | S6 | HU-VEN-001, HU-CXC-001, HU-CXC-002 | Por especificar<br>Estimación: Pendiente |
| 57 | `HU-REP-006`<br>Usuario | Consultar mi resumen privado | S6 | HU-ASI-004, HU-PLA-004, HU-CXC-001 | Por especificar<br>Estimación: Pendiente |
| 58 | `HU-NOT-001`<br>Usuario | Recibir recordatorios internos | S6 | HU-PLA-004, HU-ACC-003 | Por especificar<br>Estimación: Pendiente |
| 59 | `HU-PUB-002`<br>Usuario | Gestionar contenido público | S6 | HU-ACC-003, HT-GEN-002 | Publicadores P-12<br>Estimación: Pendiente |
| 60 | `HU-PUB-001`<br>Usuario | Conocer información pública aprobada | S6 | HU-PUB-002, HT-GEN-002 | Contenido P-12<br>Estimación: Pendiente |

## Candidatas técnicas fuera de la línea base de 60

Se ordenan por **momento de decisión**, no después de la posición 60 en importancia. El detalle y criterios están en [historias técnicas v1.4](../historias/tecnicas/historias_tecnicas_v1.4_2026-10-13.md). Se muestran en el sprint backlog como trabajo candidato, sujeto a estimación y aprobación; no se cuentan como requisitos funcionales confirmados.

| Orden de revisión | ID | Prioridad propuesta | Sprint | Entregable relacionado | Estado |
|---:|---|---|---|---|---|
| 1 | `HT-PRE-001` | Alta | S1 | Fuentes de 51 HU y catálogo de requisitos. | Propuesta; evidencia previa parcial. |
| 2 | `HT-PRE-002` | Crítica | S1 | Línea base, alcance y criterios validados. | Propuesta; revisiones pendientes. |
| 3 | `HT-PRE-003` | Alta | S1 | Arquitectura y datos para los módulos. | Propuesta; diseño por verificar. |
| 4 | `HT-PRE-004` | Alta | S1 | Recorridos móviles y preparación PWA. | Propuesta; validación de interfaz pendiente. |
| 5 | `HT-PRE-005` | Alta | S1 | Pila, estimación y sprint backlog. | Propuesta; estimación pendiente. |
| 6 | `HT-S3-001` | Alta | S3 | Pruebas de `HU-PLA-001` a `005` y regresión de acceso. | Propuesta. |
| 7 | `HT-S4-001` | Alta | S4 | Pruebas QR/offline de `HU-ASI` y `HU-PWA`. | Propuesta; P-02/P-13/P-14 abiertos. |
| 8 | `HT-S5-001` | Crítica | S5 | Integridad de `HU-TRA`, `HU-INV`, `HU-VEN` y `HU-CXC` incluidos. | Propuesta; alcance a estimar. |
| 9 | `HT-S6-001` | Crítica | S6 | Integración, pruebas y regresión de HU entregadas. | Propuesta. |
| 10 | `HT-S6-002` | Alta | S6 y cierre | Manuales, capacitación y validación final. | Propuesta; agenda de usuarias pendiente. |

## Refinamiento y paso a sprint

1. El tesista revisa con las representantes el valor y el orden propuesto, y registra cambios con fecha, motivo y versión. No se altera silenciosamente la línea base de requisitos.
2. Antes de pasar un elemento al sprint, se completan sus reglas pendientes, dependencias, criterios verificables y estimación del equipo. El trabajo grande se divide en tareas manejables dentro de la planificación del sprint.
3. Al cerrar cada sprint se actualizan estado, evidencia, estimación restante y orden de los elementos todavía pendientes. Mejoras o correcciones nuevas se incorporan con fuente y aprobación proporcional.
4. La revisión de la directora y la validación organizacional de los ajustes v1.1 se registran cuando ocurran; no se presumen en esta edición.

## Límites

- `RF-COS-001` y `RNF-OPS-001` continúan propuestos y no son elementos de implementación confirmada en esta pila. Una exploración sobre despliegue no aprueba la política de respaldos.
- S1 reúne requisitos y diseño del 15 de septiembre al 12 de octubre. Los cinco sprints de desarrollo S2–S6 van del 13 de octubre al 21 de diciembre de 2026, con cierre del 22 al 23 de diciembre. El orden exacto y la capacidad necesitan refinamiento.
- Las historias de usuario detallan rol, función, beneficio y pruebas de aceptación; las técnicas detallan los trabajos habilitadores. Esta pila mantiene una referencia por ID para evitar duplicar sus fichas.

## Bandeja de descubrimiento por entrevista

Esta bandeja **no forma parte de las 60 entradas** ordenadas arriba. Su objetivo es conseguir una decisión sobre cada novedad antes de estimarla o asignarle sprint. Fuente: EVID-ENT-2026-10-12-001.

| Tema | Resultado de refinamiento necesario | Urgencia de decisión |
|---|---|---|
| Propósito y pérdidas | Medidas iniciales de papel, viajes, tiempo e incidentes; base de cálculo de los montos que el tesista comunica como aprobados. El abogado se indicó como USD 500 por mes durante dos meses; falta comprobante y efecto real del sistema. | Alta para factibilidad |
| Expediente y firmas | Tipos, privacidad, validez, responsables, volumen y alcance temporal. | Inmediata para diseño |
| Vencimientos y WhatsApp | Reglas por documento, canal, consentimiento y costos. | Alta |
| Faltas, atrasos y justificativos | Regla comunicada: USD 0,01/min de atraso, USD 10 desde la primera falta y aviso a la tercera falta. Definir justificativos, autoridad, cobro y cierre formal de P-03. | Inmediata |
| Agenda | Confirmar avisos uno/dos días antes, lugares y delegación. | Alta |
| Encargo de secado | Estados, confirmación, evidencia y reencargo. | Alta |
| Activos y stock personal | Separar inventario patrimonial, comercial y de cada socia. | Alta |
| Recetas y mínimos | Validar unidades, fórmula del ejemplo y umbrales por planta. | Alta |
| Sitio comercial | Aprobar precios y sentido del enlace de WhatsApp. | Alta antes de publicar |
| Feria | Gastos previstos/reales, comisión y conciliación. | Alta |
| Venta mensual | Obligación, periodo, liquidación, comisión y vínculo con stock general. | Alta |

La Directiva y el tesista deberán decidir inclusión, tamaño y orden; cualquier cambio de sprint o de entrega se registra aparte. No se asignan puntos u horas ficticios.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.2 | 2026-10-12 | Se ordenan 60 historias preliminarmente y se añade una bandeja de descubrimiento por entrevista. | Edición documental; revisión académica pendiente |
| 1.3 | 2026-10-13 | Se adapta la numeración S1–S6, se explicitan prioridades de las nueve HT y se añaden diez candidatas técnicas separadas de la línea base. | Preparado; estimación y revisión pendientes |
