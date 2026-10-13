---
titulo: Candidato de requisitos funcionales para edición académica
version: "1.1"
fecha: 2026-10-12
autor: Codex, para revisión del tesista
estado: candidato-interno
fuente_entrevista: EVID-ENT-2026-10-12-001
fuente_principal: CAT-REQ-001 v1.1
requisitos_confirmados_por_tesista: 51
revision_directora: pendiente
validacion_organizacional_de_ajustes_v1_1: no-registrada
publicacion: no-autorizada
---

# Requisitos funcionales — candidato para revisión

## Control de esta edición

Este texto reúne los **51 requisitos funcionales confirmados por el tesista** en
[CAT-REQ-001 v1.1](../../../docs/requirements/CAT-REQ-001.md). Para los 48 IDs
heredados se conserva la definición de
[R3 incorporado](../../../docs/requirements/proposals/2026-07-22-catalogo-revisado-requisitos-r3.md),
con los ajustes expresos de v1.1 por encima de R3. Los tres IDs `RF-PWA` proceden
de v1.1. El estado `confirmed` de la fuente **no significa implementado o probado**.

La versión 1.0 anterior del catálogo tuvo validación del tesista, la organización
y la presidenta. Los ajustes v1.1 tienen aprobación del tesista del 28 de
septiembre de 2026; no se registra una nueva aprobación de la organización ni
la revisión académica de la directora. Esas validaciones se muestran como
pendientes y no se atribuyen a otras personas.

Cada fila resume necesidad, regla y comprobación mínima. La especificación de
cada funcionalidad debe completar pantallas, datos, permisos y pruebas antes de
implementarla. Las decisiones P-02 a P-14 permanecen abiertas en la parte indicada.

## Acceso y administración — Sprint 1

| ID | Necesidad y regla aprobada | Comprobación mínima |
|---|---|---|
| RF-ACC-001 | Una usuaria interna con cuenta activa inicia y cierra sesión y accede solo a contenido autorizado. | Credenciales válidas permiten entrar; intento inválido o cuenta inactiva se rechaza sin revelar datos. |
| RF-ACC-002 | La Directiva administra membresías, activación y desactivación sin borrar la historia. | Una socia sin permiso no modifica cuentas; desactivar impide nuevos accesos y conserva registros. |
| RF-ACC-003 | Las funciones dependen del perfil, cargo, encargo y operación; el soporte técnico queda separado de la autoridad organizacional. | Cargo incorrecto, encargo vencido y acceso directo a una dirección protegida se deniegan sin cambiar datos. P-01 se cerró para acceso básico; otras operaciones precisan sus permisos en cada spec. |
| RF-ACC-004 | Cada usuaria ve un inicio comprensible con actividades, pendientes y encargos que le correspondan. | Solo aparecen y funcionan acciones disponibles para su situación actual. |

## Planificación — Sprint 2

| ID | Necesidad y regla aprobada | Comprobación mínima |
|---|---|---|
| RF-PLA-001 | La Directiva registra jornadas y eventos con instancia, fecha, hora, lugar, responsable, participantes y estado. | Datos válidos crean la actividad; un error permite corregir sin perder lo escrito. |
| RF-PLA-002 | La organización asigna responsables y participantes con un alcance claro. | Una cuenta inactiva no recibe asignaciones; cada participante ve solo lo que le corresponde. |
| RF-PLA-003 | Un encargo temporal de producción o feria tiene actividad, periodo, alcance y cierre. | Solo permite operaciones mientras esté vigente y dentro de su alcance. |
| RF-PLA-004 | Directiva y socias consultan sus actividades y pendientes con filtros comprensibles. | Cada socia ve sus propios datos; una búsqueda sin resultados se explica. |
| RF-PLA-005 | Se planifica la producción semanal con producto, cantidad objetivo, responsables e insumos previstos. | El plan es visible para las asignadas, registra cambios y no crea existencias ni lotes por anticipado. |

## Asistencia y participación — Sprint 3

| ID | Necesidad y regla aprobada | Comprobación mínima |
|---|---|---|
| RF-ASI-001 | Cada instancia conserva entrada y salida separadas, con hora del servidor cuando hay conexión y origen propio o delegado. Una captura offline es provisional. | No se aceptan eventos duplicados o secuencias imposibles; se distingue hora declarada de recepción en capturas sin red. La aceptación tardía depende de P-13. |
| RF-ASI-002 | La asistencia conserva unicidad por socia, instancia y tipo de evento; inconsistencias quedan pendientes. | Un duplicado muestra el registro existente; una salida olvidada no recibe una hora inventada. |
| RF-ASI-003 | Directiva o encargada autorizada corrige registros sensibles con motivo e historial. | Quien carece de permiso no modifica; se reconstruyen valor anterior, nuevo valor, actor y fecha. |
| RF-ASI-004 | La socia consulta su historial y la Directiva consulta según cargo y periodo. | Los filtros y estados se entienden y no exponen datos de otras socias. |
| RF-ASI-005 | Se registra participación adicional solo cuando la actividad necesita un dato distinto de asistencia. | Una actividad simple no obliga a completar participación; cada registro se vincula con socia y actividad. |
| RF-ASI-006 | Las inconsistencias se mantienen pendientes hasta decisión de la asamblea, registrada por la Directiva. | No se genera una falta o sanción automática; quedan actor, fecha, motivo, acuerdo y cambios. P-03 define consecuencias aún abiertas. |
| RF-ASI-007 | La organización puede habilitar fases QR distintas para entrada y salida; hay código alternativo y registro delegado auditable. El token temporal no contiene datos personales. | Token vencido, repetido o de otra acción no modifica asistencia. Se distingue autorregistro de registro delegado y se conserva su motivo. P-02 define duración, responsables y casos de delegación; P-13 rige el uso offline. |

## Catálogo, producción e inventario — Sprint 4

| ID | Necesidad y regla aprobada | Comprobación mínima |
|---|---|---|
| RF-CAT-001 | Se distinguen plantas, materias primas, insumos, empaques, productos, presentaciones y unidades con historia. | Desactivar impide uso nuevo sin borrar registros anteriores. Presentaciones y conversiones siguen en P-04. |
| RF-INV-001 | Los valores comerciales tienen vigencia e historia: costo conocido, precio sugerido, precio vigente y valor base. | Un cambio no altera ventas anteriores; un producto inactivo no entra en ventas nuevas. |
| RF-TRA-001 | El acopio registra origen, socia, materia, peso o cantidad, unidad, fecha, valoración, responsable y observación. Pesajes habilitados pueden capturarse sin red de forma provisional. | Peso no positivo se rechaza; corrección queda auditada; una captura local no se presenta como aceptación remota. |
| RF-TRA-002 | El secado registra peso inicial y final, temperatura en °C, inicio y fin; humedad es opcional. Pesajes habilitados pueden capturarse provisionalmente sin red. | En línea se usa hora del servidor; el cierre exige valores válidos. P-13 debe definir el tratamiento temporal de capturas sin red antes de calcular duraciones. |
| RF-TRA-003 | Se calculan duración y merma absoluta con fórmula y unidad visibles; el porcentaje espera reglas de redondeo. | Peso final mayor que inicial exige revisión o excepción autorizada. |
| RF-TRA-004 | Cada lote conserva su procedencia; cierre productivo y agotamiento de stock son conceptos distintos. Solo una mezcla física crea un lote derivado. | Se recorren orígenes; una mezcla incompatible se rechaza; atender un pedido desde varios lotes no los fusiona. P-05 rige excepciones. |
| RF-TRA-005 | La transformación registra insumos consumidos, composición y versión, resultado, cantidad, residuos, responsable, fecha y lote. | El producto resultante enlaza sus consumos; cantidades incompatibles se rechazan. |
| RF-INV-002 | Entradas, consumos, producción, asignaciones, ventas, devoluciones y ajustes generan movimientos. | La existencia deriva de movimientos; un ajuste exige permiso y motivo y la operación se confirma completa. |
| RF-INV-003 | Cada entrega de feria identifica encargo, socia, producto, lote, cantidad y modalidad individual o compartida. | No excede el stock; quien recibe confirma o informa diferencia; el origen permanece visible. |
| RF-INV-004 | Se concilian productos recibidos, transferidos, vendidos, devueltos y retornados sin mezclarlos con deudas monetarias. | Una diferencia queda visible para conciliar y no produce stock negativo silencioso. |

## Ventas, gastos y rendición — Sprint 4

| ID | Necesidad y regla aprobada | Comprobación mínima |
|---|---|---|
| RF-VEN-001 | La socia encargada registra ventas de varios productos desde stock autorizado, con cantidad, precio, total y forma de pago. | El total se calcula; no se vende más de lo disponible; la venta completa se confirma o se revierte. |
| RF-VEN-002 | Se pide identificación del comprador solo según el riesgo: contado puede usar «Público general»; crédito o venta institucional exige datos mínimos aprobados. | Crédito sin comprador se rechaza; contado no solicita datos innecesarios. |
| RF-VEN-003 | Cada venta conserva valor base y precio aplicado históricos y calcula excedente bruto sin llamarlo utilidad neta. | Ambos importes se muestran y no cambian retroactivamente. |
| RF-VEN-004 | Vender bajo el valor base requiere excepción autorizada, motivo e historial. | La venta ordinaria bajo base se rechaza; la excepción identifica autoridad y diferencia. |
| RF-VEN-005 | La Tesorera puede configurar descuentos por volumen con producto, presentación, umbral, valor y vigencia. | Una política incompleta no se aplica. P-08 debe fijar sus valores; vender bajo base también requiere excepción. |
| RF-VEN-006 | En feria, cada línea identifica si procede de stock individual o compartido. | Los resultados individuales no se mezclan; el excedente compartido no se reparte automáticamente mientras P-07 esté abierto. |
| RF-VEN-007 | La organización registra ventas institucionales desde stock general mediante la Tesorera. | Quedan claros tipo y responsable; no se atribuye excedente a una socia. |
| RF-VEN-008 | El comprobante manual único permite una contingencia de feria y registro tardío auditable. No reemplaza la capacidad PWA obligatoria ni autoriza por sí solo venta offline digital. | Un folio repetido no descuenta dos veces; conflictos de stock quedan para revisión. P-10 define custodia, plazos y conciliación. |
| RF-GAS-001 | La Tesorera registra gastos con categoría, monto, fecha, concepto, periodo o lote y responsable. | Monto inválido se rechaza; cambios sensibles quedan auditados. |
| RF-GAS-002 | La Directiva consulta un resumen de ingresos organizacionales, gastos y pendientes con fórmula visible. | Los totales remiten a su fuente y periodo; no se presenta como balance certificado. |
| RF-CXC-001 | Se separan custodia física, deuda de socia y cuenta por cobrar externa; retiro individual impago usa valor base congelado. | Custodia compartida no crea deuda individual; pagos afectan solo el saldo elegido. P-09 rige devoluciones y ajustes monetarios. |
| RF-CXC-002 | Se registran abonos con monto, fecha, forma, responsable y saldo aplicado. | Un abono válido reduce el saldo elegido; el tratamiento de sobrepagos depende de P-09. |
| RF-CXC-003 | La rendición de feria muestra recibido, vendido, devuelto, sobrante, dinero, base, excedente y diferencias. | Una discrepancia deja el encargo por conciliar y explica qué falta. |

## Reportes, recordatorios y sitio público — Sprint 5

| ID | Necesidad y regla aprobada | Comprobación mínima |
|---|---|---|
| RF-REP-001 | La Directiva consulta asistencia por periodo, actividad y socia con estados y correcciones. | Los totales coinciden con registros; la ausencia de datos se explica. |
| RF-REP-002 | La Directiva consulta actividades y encargos por estado, tipo, responsable y periodo. | Los pendientes son visibles con el detalle permitido para su cargo. |
| RF-REP-003 | La Directiva consulta acopio, secado, transformación, lotes y merma con unidad y origen. | Los totales enlazan movimientos y no ocultan insumos sin valoración. |
| RF-REP-004 | La Directiva consulta existencias derivadas y movimientos por producto, lote y periodo. | La existencia concilia con movimientos; ajustes se distinguen. |
| RF-REP-005 | La Tesorera consulta ventas, deuda de socias, deuda externa, pagos y pendientes por separado. | No se mezclan saldos; filtros y fórmulas son visibles. |
| RF-REP-006 | Cada socia consulta un resumen privado de asistencia, actividades, productos, valores por entregar, créditos de clientes y excedente bruto. | No ve datos de otras socias ni se presenta excedente como ganancia neta. |
| RF-NOT-001 | Las usuarias reciben recordatorios dentro del sistema sobre actividades, asistencia, encargos, rendiciones y registros tardíos. | Cada recordatorio abre el elemento correcto sin depender de correo o mensajería. |
| RF-PUB-001 | Visitantes ven solo historia, misión, visión, productos, ubicación, redes y contacto aprobados. | Una sección sin aprobar permanece oculta y no muestra información interna ni sanitaria. P-12 define el contenido. |
| RF-PUB-002 | La organización prepara, aprueba, publica y retira contenido según permisos. | Una persona no autorizada no publica; retirar conserva historia. La matriz de permisos se precisa por funcionalidad. |

## Continuidad sin conexión — transversal

| ID | Necesidad y regla aprobada | Comprobación mínima |
|---|---|---|
| RF-PWA-001 | La interfaz esencial de los flujos habilitados puede abrirse sin red después de preparar el dispositivo compatible. | Al cortar la red se muestra el estado y las acciones disponibles; el primer uso sin recursos precargados explica la limitación; caché público no expone páginas privadas. |
| RF-PWA-002 | Asistencia y pesajes habilitados se guardan localmente como operaciones pendientes con datos mínimos y origen identificable. | La operación persiste al recargar; un fallo local no muestra éxito; otra cuenta no ve la cola; se distingue hora capturada de recepción. P-14 define retención y dispositivo compartido. |
| RF-PWA-003 | Al recuperar conexión, se reintenta cada operación con la misma identidad y el servidor revalida sesión, permisos y reglas antes de confirmarla. | Una respuesta perdida y su reintento crean un solo registro; conflicto y revocación se muestran sin mutaciones indebidas; un fallo atómico no deja registros parciales. P-13/P-14 concretan políticas. |

## Límites pendientes y fuera de alcance de esta edición

- `RF-COS-001` y `RNF-OPS-001` permanecen **propuestos**, fuera de los 51
  requisitos funcionales confirmados. P-06 y P-11 impiden confirmarlos.
- P-02 a P-14 conservan los detalles abiertos descritos en CAT-REQ-001 v1.1.
  Esta edición no inventa duraciones QR, fórmulas, umbrales, políticas de respaldo,
  retención local ni contenido público.
- La versión vigente exige guardado y sincronización offline para los flujos
  aprobados. La exclusión offline contenida en R3 es histórica y no se reproduce
  como regla actual.
- No se afirma aplicación implementada, pruebas funcionales ejecutadas,
  validación académica ni aprobación organizacional de los ajustes v1.1.

## Necesidades de entrevista aún no confirmadas como requisitos

La fuente EVID-ENT-2026-10-12-001 se incorpora como material de validación. Ninguna fila siguiente altera los 51 RF confirmados.

| Tema de entrevista | Requisitos relacionados | Pregunta o regla por definir |
|---|---|---|
| Expediente y firmas | RF-REP-001 a 006 generan reportes PDF, pero no administran archivos generales. | Tipos de documento, versiones, búsqueda, permisos, retención y validez de firma. |
| Vencimientos y WhatsApp | RF-NOT-001 solo confirma avisos internos. | Fechas, tres/seis meses de anticipación, destinatarios, consentimiento y canal. |
| Atrasos, faltas y justificativos | RF-ASI-001/006/007; P-02/P-03. | El tesista comunica USD 0,01/min de atraso, USD 10 desde la primera falta y aviso a la tercera falta. Definir justificativos, autoridad, redondeo y cobro antes de proponer automatización. |
| Agenda y delegación | RF-PLA-001/002/003/004. | Recordatorios uno/dos días antes, reencargo de secado, confirmación y evidencia adjunta. |
| Inventarios y producción | RF-CAT-001, RF-TRA-001/005, RF-INV-002/003/004. | Activos fijos/depreciación, stock personal, umbrales, recetas, unidades y mermas. |
| Feria y venta mensual | RF-VEN-001/003/006, RF-GAS-001, RF-CXC-001/003. | Gastos previstos, periodicidad, comisiones, base/costo y conciliación individual/general. |
| Sitio público | RF-PUB-001/002; P-12. | Precios autorizados y si el botón WhatsApp es contacto o genera un pedido. |

El ejemplo «50 litros = 100 champús» no se registra como fórmula validada. La presencia de un PDF sanitario no demuestra cumplimiento normativo. Las multas no se convierten en automatización a partir del resumen.

## Historial de esta edición candidata

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Codex | Consolidación para revisión desde CAT-REQ-001 v1.1 y R3 incorporado. | Candidato interno |
| 1.1 | 2026-10-12 | Codex | Se incorporó el impacto del resumen de entrevista sin cambiar el alcance confirmado. | Candidato interno |
