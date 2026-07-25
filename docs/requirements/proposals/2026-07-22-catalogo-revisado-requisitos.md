---
title: Catálogo revisado de requisitos para validación
type: requirement
status: superseded
id: CAT-REQ-001-R2
supersedes: CAT-REQ-001-R1
superseded_by: CAT-REQ-001-R3
created: 2026-07-22
phase: Fase I
sprint: transversal
priority: high
module: transversal
validated_by: []
related:
  - "[[2026-07-21-catalogo-inicial-requisitos]]"
  - "[[../../00-inicio/01-decisiones-pendientes]]"
  - "[[../../sprints/ROADMAP-ANTEPROYECTO]]"
  - "[[../../traceability/MATRIZ-TRAZABILIDAD]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - estado/superseded
  - sprint/fase-i
---

# CAT-REQ-001-R2 - Catálogo revisado de requisitos para validación

## Propósito y límite de esta revisión

Esta revisión incorpora el informe de validación entregado por el tesista y los análisis de
requisitos, UX y arquitectura realizados en lectura. Reemplaza como base de discusión al
catálogo inicial, pero no lo convierte en requisito aprobado.

Durante esta revisión, el estado de todo el documento fue `proposed`; actualmente está
`superseded` por `CAT-REQ-001-R3`. La validación debía realizarse con el tesista, la Directiva
y las representantes de las socias que ejecutan producción, asistencia y ferias. Ninguna
sección de esta revisión histórica autoriza crear modelos, migraciones, una aplicación Django
o una integración externa.

### Fuentes y autoridad

- **F1**: `agents/tesis/PROJECT_CONTEXT.md` y anteproyecto.
- **F2**: decisiones D-001 a D-010 del proyecto.
- **F3**: evaluación de documentos previos.
- **F4**: roadmap oficial de sprints.
- **F5**: sistema de diseño y restricciones UX propuestas.
- **F6**: arquitectura objetivo propuesta.
- **F7**: confirmaciones del tesista registradas en D-001 a D-010.
- **F8**: informe de validación entregado en la conversación del 2026-07-22; requiere
  registro de participantes, fecha, evidencia y confirmación de la organización.

Si F8 contradice una evidencia de campo o una decisión confirmada por la organización, se
debe conservar la discrepancia y resolverla con las representantes, no escogerla
automáticamente.

## Decisiones propuestas para validar

Estas decisiones permiten continuar el levantamiento con una base coherente. Son propuestas,
no aprobaciones.

| ID | Decisión propuesta | Motivo y validación necesaria |
|---|---|---|
| DP-01 | Mantener tres perfiles organizativos: Directiva, Socia operaria y Visitante. Añadir `Administrador técnico del sistema` únicamente como perfil de operación y soporte, sin pertenencia a la organización ni acceso rutinario a información de negocio. | Resuelve la mención de “administrador general” sin crear una autoridad organizativa oculta. Debe confirmarse quién desempeñaría esa función. |
| DP-02 | La Encargada es una asignación temporal con tipo, actividad, periodo y alcance. Una Encargada de producción no obtiene automáticamente permisos de feria ni de asistencia, y viceversa. | Evita que un encargo amplio permita corregir datos ajenos. Validar la matriz cargo/encargo/operación. |
| DP-03 | La asistencia registra entrada y salida con fecha/hora automática del servidor. Cada socia puede registrar su propia asistencia durante la ventana de la actividad; una Encargada o Directiva puede registrar en nombre de otra socia solo si la actividad lo permite. | Recoge el informe y conserva el alcance de entrada/salida del anteproyecto. Debe validarse la necesidad de estados de ausencia y justificación. |
| DP-04 | Las actividades ordinarias de los miércoles se planifican como jornadas recurrentes o instancias fechadas. Los eventos adicionales los crea la Directiva; una Encargada solo puede crearlos si recibe delegación explícita. | Evita que la encargada pueda alterar el calendario organizativo sin autorización. |
| DP-05 | La ventana ordinaria para completar o solicitar corrección de asistencia es de tres días calendario. Después se crea una solicitud; la Directiva aprueba o rechaza y el Administrador técnico ejecuta únicamente la corrección aprobada. | Separa decisión organizativa de ejecución técnica y conserva auditoría. Validar si son días calendario o laborables. |
| DP-06 | QR es un canal opcional para abrir la actividad o identificarla; no se considera prueba suficiente de presencia. La foto de un QR o de un producto y la visión artificial quedan fuera del primer incremento. | Reduce suplantación, privacidad, costos y riesgo de falsos positivos. Podrán estudiarse como experimento separado. |
| DP-07 | El catálogo distingue materia prima, planta, insumo, empaque, producto, presentación y unidad. Producto y presentación pueden tener imagen, precio sugerido, precio de venta vigente y valor base histórico. | Integra productos, kits, envases, fundas, etiquetas y otros insumos sin mezclarlos. Validar nombres y unidades reales. |
| DP-08 | El costo de una presentación se calcula desde consumos registrados y costos unitarios de entradas, insumos, empaque y gastos asignables. Cada entrada debe tener valoración o marcarse explícitamente como aporte propio sin valoración monetaria. | Hace calculable el costo sin pedir fórmulas a las socias, pero requiere confirmar tratamiento de mano de obra, transporte y gastos compartidos. |
| DP-09 | Una feria puede tener varias socias. La opción recomendada para la primera versión es stock individual por socia; un fondo común y la distribución por partes iguales o porcentajes quedan como políticas configurables, no como supuesto. | Permite trazabilidad individual y prepara la división de excedentes sin inventar una regla económica. Validar la política real. |
| DP-10 | El precio sugerido se muestra desde el catálogo y puede modificarse en la venta solo si la política lo permite. Una venta bajo el valor base siempre requiere autorización, motivo y auditoría. Los descuentos por volumen se configuran por producto/presentación y vigencia. | Distingue precio sugerido, precio aplicado, valor base y costo. Validar umbrales y autoridad para descuentos. |
| DP-11 | La venta en feria debe funcionar offline desde el primer incremento comercial. El alcance offline se limita inicialmente a registrar ventas, pagos asociados y estado de sincronización desde stock previamente asignado. | Cumple la prioridad del informe sin prometer que todos los módulos funcionan sin conexión. Requiere una prueba técnica y una decisión de despliegue. |
| DP-12 | Los recordatorios internos se muestran en el inicio y en “Mis actividades”. SMS o WhatsApp se consideran canales opcionales posteriores, sujetos a proveedor, consentimiento, costos, privacidad y cobertura. | Permite recordar asistencia sin bloquear el núcleo por una integración externa. Validar si la organización exige un canal externo desde la primera versión. |
| DP-13 | El respaldo es una responsabilidad operativa explícita: copia automática de la base, copia de archivos, responsable nombrado, frecuencia, retención y prueba de restauración. | Q3 no queda resuelta mientras solo se hable de sincronización. Validar proveedor, ubicación y procedimiento. |

## Actores y permisos propuestos

| Actor | Alcance propuesto |
|---|---|
| Directiva | Administra actividades, membresía, catálogos autorizados, aprobaciones, correcciones y reportes según el cargo real. Presidenta, tesorera y secretaria no deben compartir automáticamente todos los permisos. |
| Socia operaria | Consulta sus actividades, asistencia, encargos, productos asignados y su información individual. No administra cuentas ni corrige registros generales. |
| Encargada de producción | Opera únicamente acopios, secados, transformaciones o lotes vinculados a su encargo vigente. |
| Encargada de feria | Opera únicamente productos asignados, ventas, devoluciones y rendición de su feria vigente. |
| Tesorera | Administra valores base, costos, gastos, pagos y reportes financieros solo dentro de la matriz validada. |
| Administrador técnico | Mantiene cuentas técnicas, sincronización, respaldos y correcciones aprobadas. No decide reglas de negocio ni aprueba sus propias correcciones. |
| Visitante | Consulta únicamente contenido público aprobado. |

Toda autorización se comprueba en backend. La interfaz personalizada oculta opciones, pero no
reemplaza la autorización del servidor. Las operaciones sensibles deben tener una prueba
permitida y una denegada.

## Requisitos revisados

Todos los requisitos siguientes tienen estado `proposed`. Los IDs existentes se conservan
para facilitar la trazabilidad; las ampliaciones y requisitos nuevos deben validarse antes de
crear specs.

### A. Acceso, membresía y planificación

#### RF-ACC-001 a RF-ACC-004 — Acceso e inicio personalizado

Se mantienen con estas precisiones:

- una cuenta inactiva no inicia sesión y conserva su historia;
- la persona no elige su perfil técnico al ingresar;
- el inicio muestra tareas, actividades y encargos vigentes, no permisos técnicos;
- una cuenta puede tener más de un encargo vigente solo si la Directiva lo autoriza y los
  alcances no generan conflicto;
- el cierre de sesión, el tiempo de inactividad y la privacidad en equipos compartidos deben
  definirse antes de las pruebas con usuarias.

#### RF-PLA-001 — Gestión de actividades y jornadas

La Directiva registra una actividad con nombre, tipo, fecha, hora, lugar, participantes,
responsable, estado y si admite asistencia. Se conservan cancelaciones y motivos.

#### RF-PLA-002 — Participantes y responsable

La Directiva asigna participantes y responsable. Una cuenta inactiva no puede recibir una
nueva asignación. La asignación debe indicar si la persona solo participa, registra asistencia
o tiene un encargo operativo.

#### RF-PLA-003 — Encargo temporal

Un encargo tiene tipo (`producción` o `feria/venta`), actividad, periodo, responsable, alcance,
estado y cierre. Al vencer o cerrarse, las operaciones adicionales se deniegan sin borrar la
historia.

#### RF-PLA-005 — Planificación productiva semanal

La Directiva puede planificar una producción por semana o fecha, producto, presentación,
cantidad objetivo, actividad del miércoles, responsables, insumos previstos y estado. La
planificación no crea automáticamente stock ni lotes; estos nacen de registros operativos.

**Aceptación propuesta:** una planificación vigente aparece para las personas asignadas; un
cambio de cantidad, responsable o fecha conserva quién lo hizo y cuándo; una socia no puede
alterar la planificación general.

### B. Asistencia y participación

#### RF-ASI-001 — Registro de entrada y salida

Para cada instancia de actividad y socia participante, el sistema registra:

- actividad e instancia concreta;
- socia;
- entrada y salida con fecha/hora automática;
- origen del registro: propio, QR o registro autorizado en nombre de otra persona;
- estado derivado: abierta, completa, pendiente de revisión o justificada;
- responsable de una corrección, si existe.

La unicidad se aplica por socia e instancia o turno, no únicamente por actividad general.

#### RF-ASI-002 — Ventana, duplicados e inconsistencias

El sistema impide doble entrada, salida sin entrada, salida anterior a entrada y registros
fuera de la ventana sin una razón autorizada. Una salida olvidada queda pendiente de revisión,
no se inventa automáticamente.

#### RF-ASI-003 — Correcciones y solicitudes tardías

Durante la ventana definida, la Directiva corrige registros; una Encargada solo puede corregir
la asistencia de la actividad que tiene asignada y si su encargo lo incluye. Después de tres
días calendario, la socia solicita corrección, la Directiva decide y el Administrador técnico
ejecuta la decisión aprobada. Cada paso conserva solicitante, aprobador, ejecutor, fecha,
valores anterior y nuevo y motivo.

#### RF-ASI-004 — Consulta individual y organizativa

Una socia solo ve su historial. La Directiva ve el conjunto permitido por su cargo. La vista
debe mostrar periodo, actividad, entrada, salida, estado y correcciones visibles para ese
actor.

#### RF-ASI-005 — Participación

La participación se registra solo cuando una actividad necesita describir una intervención
distinta de asistir. Sus tipos deben ser pocos, comprensibles y validados con las socias.

### C. Catálogos, producción e inventario

#### RF-CAT-001 — Catálogo de materias, insumos y productos

El sistema mantiene catálogos activos e históricos de:

- plantas y materias primas;
- insumos y empaques: envases, fundas, etiquetas y otros;
- productos elaborados, incluidos kits;
- presentaciones, unidades, conversiones y precisión;
- imagen, descripción y publicación pública, si corresponde.

Cada elemento tiene responsable de alta, vigencia y regla de desactivación. Desactivar no
elimina historia.

#### RF-INV-001 — Catálogo comercial

Cada producto/presentación puede tener nombre, imagen, unidad, costo calculado, precio de
venta sugerido, precio vigente, valor base organizacional y vigencias históricas. El valor
base y los precios usados en una venta quedan congelados en esa venta; cambiarlos no modifica
operaciones anteriores.

#### RF-TRA-001 — Acopio

Registra socia que entrega, materia prima, lote de origen si existe, cantidad/peso, unidad,
fecha, valoración o aporte propio, responsable y observaciones. Un peso no positivo se
rechaza. Toda corrección es auditada.

#### RF-TRA-002 y RF-TRA-003 — Secado, duración y merma

Se conservan peso inicial, peso final, temperatura en Celsius, humedad opcional, inicio y fin
automáticos, duración y merma. El porcentaje, redondeo y tratamiento de un peso final mayor
al inicial deben validarse con la organización antes de la spec.

#### RF-TRA-004 — Lotes y compatibilidad

Un lote vincula acopios, secados, transformaciones, productos resultantes, cantidades y
responsables. No se mezclan insumos automáticamente. La mezcla, división o combinación debe
estar permitida por una regla de compatibilidad del producto y conservar todos los orígenes.

Un lote puede consumirse parcialmente y dividirse con trazabilidad; no se elimina ni se
reescribe su historia.

#### RF-TRA-005 — Transformación y rendimiento

Registra entradas consumidas, fórmula o composición aplicada, producto resultante, cantidad,
residuos/merma, responsable, fecha y lote. Esta separación evita que la transformación quede
implícita dentro de “formar lote”.

#### RF-INV-002 — Movimientos y existencias

Entradas, consumos, producción, asignaciones, ventas, devoluciones y ajustes son movimientos
identificables. Las existencias se derivan de ellos. Un ajuste exige permiso, motivo y
auditoría.

#### RF-INV-003 — Entrega y confirmación

Una feria puede tener una o varias socias. La entrega identifica feria, socia, productos,
cantidades, lote, fecha y responsable. La socia confirma lo recibido o reporta diferencia.
La configuración recomendada inicial es stock individual por socia; el stock compartido exige
una política explícita.

#### RF-INV-004 — Devolución y conciliación

El saldo operativo de productos se calcula como:

`recibido + transferido a la socia - vendido - devuelto - transferido de vuelta`.

Si el resultado supera lo recibido, la conciliación queda pendiente y exige revisión. La
fórmula económica de la deuda de la socia se mantiene separada de este saldo físico hasta que
la organización confirme cuándo nace y cuándo se reduce.

#### RF-COS-001 — Costo calculado

El sistema calcula el costo de una presentación desde consumos de materias primas, insumos,
empaque y gastos asignables registrados. El costo unitario se deriva de la valoración de las
entradas y de la cantidad producida. La fórmula debe indicar si incluye mano de obra,
transporte, energía y gastos compartidos; no se presenta como contabilidad tributaria.

### D. Ventas, precios y rendición

#### RF-VEN-001 y RF-VEN-002 — Venta simple y comprador

Una socia con encargo vigente registra una venta con uno o varios productos de su stock o del
fondo autorizado, cantidad, precio aplicado, comprador, forma de pago y total. Para contado se
usa `Público general`; para crédito se exige la identificación mínima acordada.

La operación debe conservar precio sugerido, precio aplicado, valor base, cantidad, total,
usuario, dispositivo/cola si fue offline y fecha/hora.

#### RF-VEN-003 — Valor base y excedente

El sistema calcula por unidad y total el valor base de la organización y el excedente bruto
sobre el precio base. No lo denomina utilidad neta ni descuenta gastos individuales sin una
regla aprobada.

#### RF-VEN-004 — Venta bajo valor base

Una venta bajo el valor base requiere autorización, motivo, usuario autorizador y fecha. La
operación muestra claramente el valor recibido por la organización y cualquier diferencia; no
se permite como venta normal.

#### RF-VEN-005 — Precios por volumen

La Directiva autorizada puede configurar por producto/presentación un umbral, precio o
porcentaje de descuento, periodo de vigencia y autoridad. El sistema diferencia descuento
configurado de venta excepcional bajo valor base. Los ejemplos de 50, 500 o 1000 unidades son
datos pendientes de validar, no valores predeterminados.

#### RF-VEN-006 — Feria con varias socias y distribución

La feria registra quién vende cada operación. La política de distribución puede ser
individual, partes iguales o porcentajes, pero debe seleccionarse y quedar auditada antes del
cierre. Mientras no se valide, el sistema muestra ventas y excedente bruto por socia sin
calcular una ganancia distribuida.

#### RF-GAS-001 y RF-GAS-002 — Gastos y resumen

La Tesorera registra gastos por lote o periodo con categoría, monto, fecha, concepto y
responsable. El resumen muestra ingresos organizacionales, gastos clasificados, pendientes y
fórmula aplicada. No se presenta como balance contable ni utilidad certificada.

#### RF-CXC-001 y RF-CXC-002 — Saldos separados y pagos

Se mantienen separados:

1. el saldo de la socia con la organización;
2. la cuenta por cobrar de clientes externos.

Cada abono conserva monto, fecha/hora, forma de pago, responsable y saldo al que se aplica.
No se mezclan saldos ni se aceptan sobrepagos sin una regla explícita.

#### RF-CXC-003 — Rendición

La rendición presenta productos recibidos, vendidos, devueltos, sobrantes, dinero entregado,
valor base, excedente y diferencias. Una discrepancia no se oculta: el encargo queda pendiente
con una explicación de lo que falta conciliar.

### E. Operación offline y continuidad

#### RF-OFF-001 — Registro offline de ventas

Si una socia tiene un encargo vigente, stock previamente asignado y catálogo descargado, puede
registrar una venta sin Internet desde un dispositivo compatible. El registro local contiene
un identificador único, usuario, feria/encargo, líneas, cantidades, precios y forma de pago.
La aplicación muestra que la venta está pendiente y no la presenta como sincronizada.

El formato interno puede ser JSON, pero el requisito es la cola local segura y verificable, no
un formato visible para la usuaria.

#### RF-OFF-002 — Sincronización idempotente

Al volver Internet, la cola se sincroniza sin duplicar ventas. Cada registro queda como
`pendiente`, `enviado`, `confirmado`, `en conflicto` o `rechazado`. El registro local no se
elimina antes de recibir confirmación del servidor y conservar el comprobante de sincronización.

#### RF-OFF-003 — Conflictos y límites

Una venta que exceda el stock asignado, use una política vencida o tenga datos incompatibles
queda en conflicto para revisión de la Directiva/Tesorera. El sistema nunca sobrescribe datos
silenciosamente. La primera versión no permitirá offline modificar catálogos, permisos,
valores base ni políticas de descuento.

#### RNF-CON-001-R2 — Conectividad y gama baja

Los recorridos críticos deben funcionar con HTML ligero, JavaScript progresivo, carga de
recursos mínimos, sin fuentes remotas obligatorias y sin desplazamiento horizontal desde
360 px. El modo offline se limita inicialmente al recorrido de ventas definido arriba. Debe
probarse en los dispositivos reales de las socias.

#### RNF-OPS-001 — Respaldos y recuperación

La operación debe definir responsable, frecuencia, destino, retención, protección, procedimiento
de restauración y prueba periódica. La prueba de recuperación debe producir evidencia sin
exponer datos personales innecesarios.

### F. Reportes, privacidad y publicación

#### RF-REP-001 a RF-REP-005 — Reportes organizativos

Se mantienen reportes de asistencia, actividades/encargos, producción, inventario, ventas y
cuentas por cobrar. Cada reporte indica periodo, filtros, fuente, unidad, fórmula, fecha de
generación y permisos.

#### RF-REP-006 — Reporte individual de la socia

Cada socia consulta en una vista sencilla únicamente sus datos: asistencia, actividades,
encargos, productos asignados, ventas, devoluciones, saldos y excedente bruto cuando aplique.
La Directiva y Tesorera ven información agregada o detallada solo según la matriz autorizada.
No se muestran datos de otras socias a una socia operaria.

#### RF-PUB-001 y RF-PUB-002 — Sitio público

La página pública muestra únicamente contenido, imágenes, productos y contacto aprobados. El
flujo editorial conserva preparación, aprobación, publicación y retiro sin exponer información
de socias, saldos, lotes detallados ni afirmaciones sanitarias.

#### RNF-UX-001 a RNF-UX-003 — Uso y accesibilidad

Se mantienen 360 px, controles táctiles amplios, teclado, foco visible, contraste AA, zoom al
200 %, etiquetas persistentes, estados con texto e icono, formularios recuperables y lenguaje
cotidiano. Los recorridos deben probarse con Directiva, Socia operaria, Encargada y Visitante.

#### RNF-SEC-001, RNF-AUD-001, RNF-DAT-001 y RNF-PRV-001

Se mantienen y se amplían para cubrir:

- permisos por cargo, encargo, periodo y alcance;
- movimientos de inventario, precios, costos, saldos y pagos;
- correcciones, autorizaciones, aprobaciones, sincronización y publicación;
- privacidad de datos personales en equipos compartidos y reportes;
- operaciones atómicas y reintentos idempotentes.

## Notificaciones, QR y visión artificial

### RF-NOT-001 — Recordatorios

El sistema debe mostrar recordatorios internos para asistencia pendiente, actividades próximas,
encargos por cerrar y ventas offline pendientes. SMS o WhatsApp pueden implementarse como
canales adicionales cuando exista proveedor, consentimiento y presupuesto validados.

No se aprueba todavía un agente conversacional de WhatsApp. Tampoco se exige visión artificial
para validar presencia. Ambas ideas quedan como investigación posterior con criterios de
privacidad, exactitud, costo, soporte y consentimiento.

## Alcance de la primera versión

### Incluido como requisito a diseñar

- autenticación, membresía y perfiles;
- actividades, miércoles y encargos temporales;
- asistencia con entrada, salida, ventana de tres días y correcciones auditadas;
- catálogos de materias, insumos, productos y presentaciones;
- planificación productiva;
- acopio, secado, transformación, lotes e inventario con movimientos;
- entregas, devoluciones, ventas, pagos y rendición;
- venta offline y sincronización idempotente;
- reportes organizativos y reporte individual;
- página pública aprobada;
- accesibilidad, privacidad, auditoría y respaldos.

### Diferido o excluido de la primera versión

- agente autónomo de WhatsApp;
- visión artificial como prueba de presencia;
- sanciones económicas automáticas sin regla validada;
- facturación electrónica, contabilidad tributaria y cumplimiento sanitario;
- distribución de utilidades netas sin fórmula aprobada;
- sincronización offline de producción, catálogos o administración;
- descuentos por volumen hasta validar umbrales y autoridad.

Lo diferido debe conservarse en el backlog, no desaparecer como necesidad futura.

## Preguntas que bloquean la confirmación humana

1. ¿Cada socia registra su entrada y salida, o la registra una Encargada en nombre del grupo?
2. ¿La ventana de tres días es calendario o laborable? ¿Qué ocurre con una salida olvidada?
3. ¿Qué cargos de la Directiva pueden corregir, aprobar, pagar, publicar y consultar cada dato?
4. ¿Se acepta el Administrador técnico como perfil separado de la organización?
5. ¿Cuál es el catálogo real y qué unidades/conversiones se utilizan?
6. ¿Qué reglas permiten mezclar, dividir y cerrar lotes?
7. ¿Cómo se valoran plantas recolectadas, materias compradas, envases y otros insumos?
8. ¿El costo incluye mano de obra, energía, transporte y gastos compartidos?
9. ¿Una feria usa stock individual, fondo común o ambos?
10. ¿Cómo se divide el excedente entre varias socias: individual, partes iguales o porcentajes?
11. ¿Cuándo nace y cuándo se reduce el saldo monetario de una socia?
12. ¿Qué productos tienen umbrales de compra grande y quién configura los descuentos?
13. ¿Qué datos deben estar disponibles offline y cuál dispositivo se usará en la feria?
14. ¿Quién administra respaldos y qué frecuencia de restauración se puede cumplir?
15. ¿Qué información, imágenes y contacto están aprobados para el sitio público?

## Criterio de salida de Fase I

Esta revisión podrá pasar a specs únicamente cuando:

- las preguntas 1 a 4 (actores, permisos y asistencia) estén decididas;
- exista catálogo inicial con unidades y reglas de lote;
- exista decisión explícita sobre offline, conflictos y respaldos;
- estén definidas precio sugerido, precio aplicado, valor base, costo y descuentos;
- esté definida la política de feria multi-socia y saldos;
- el reporte individual tenga contenido y límites de privacidad;
- las representantes revisen los recorridos con ejemplos;
- el registro de validación incluya fecha, participantes, decisiones y evidencia;
- se creen specs solo para requisitos confirmados, dejando los diferidos trazados.

## Registro de validación

| Fecha | Participantes/rol | IDs revisados | Decisión | Evidencia |
|---|---|---|---|---|
| Pendiente | Pendiente | CAT-REQ-001-R2 | `proposed` | Pendiente |
