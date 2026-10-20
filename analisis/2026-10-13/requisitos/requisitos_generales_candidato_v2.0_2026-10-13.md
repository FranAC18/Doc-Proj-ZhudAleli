---
titulo: Requisitos generales — candidato v2.0
version: "2.0-candidato"
fecha: 2026-10-13
autor: Codex, para revisión del tesista
estado: candidato-interno
fuente_principal: CAT-REQ-001 v1.1
requisitos_funcionales_confirmados: 51
requisitos_funcionales_propuestos: 13
requisitos_no_funcionales_confirmados: 9
requisitos_no_funcionales_propuestos: 3
revision_directora: pendiente
validacion_organizacional_de_ajustes_v1_1: no-registrada
publicacion: no-autorizada
---

# Requisitos generales del sistema Zhud Alelí — candidato v2.0

## Propósito y autoridad

Este documento es una propuesta interna de segunda edición general. Parte de la línea base CAT-REQ-001 v1.1 y conserva intactos sus 51 RF y 9 RNF confirmados. Añade por separado requisitos candidatos derivados de la entrevista, sin modificar el catálogo aprobado. Fuente de entrevista: [registro del 12/10/2026](../../../documentacion/levantamiento/registro_entrevista_v1.0_2026-10-12.md) y evidencia EVID-ENT-2026-10-12-001.

Esta primera edición general 1.0 refleja la línea base del catálogo v1.1; las dos numeraciones identifican documentos distintos. Las ediciones especializadas de requisitos funcionales y no funcionales siguen disponibles como documentos de detalle.

`confirmed` expresa aprobación del requisito, no implementación ni pruebas ejecutadas. La revisión de la directora y la validación de la organización para los ajustes v1.1 no constan realizadas. Los detalles P-02 a P-14 continúan pendientes donde corresponda. Todos los elementos nuevos derivados de entrevista aparecen únicamente en las tablas `proposed`; no se incluyen en la línea base confirmada.

## Requisitos funcionales

La lista incluye los 51 requisitos confirmados y el único requisito funcional propuesto. El propuesto se muestra aparte por estado y no forma parte de la línea base aprobada.

| ID | Estado | Requisito | Criterio de comprobación |
|---|---|---|---|
| RF-ACC-001 | confirmed | Una usuaria interna con cuenta activa inicia y cierra sesión y accede solo a contenido autorizado. | Credenciales válidas permiten entrar; intento inválido o cuenta inactiva se rechaza sin revelar datos. |
| RF-ACC-002 | confirmed | La Directiva administra membresías, activación y desactivación sin borrar la historia. | Una socia sin permiso no modifica cuentas; desactivar impide nuevos accesos y conserva registros. |
| RF-ACC-003 | confirmed | Las funciones dependen del perfil, cargo, encargo y operación; el soporte técnico queda separado de la autoridad organizacional. | Cargo incorrecto, encargo vencido y acceso directo a una dirección protegida se deniegan sin cambiar datos. P-01 se cerró para acceso básico; otras operaciones precisan sus permisos en cada spec. |
| RF-ACC-004 | confirmed | Cada usuaria ve un inicio comprensible con actividades, pendientes y encargos que le correspondan. | Solo aparecen y funcionan acciones disponibles para su situación actual. |
| RF-PLA-001 | confirmed | La Directiva registra jornadas y eventos con instancia, fecha, hora, lugar, responsable, participantes y estado. | Datos válidos crean la actividad; un error permite corregir sin perder lo escrito. |
| RF-PLA-002 | confirmed | La organización asigna responsables y participantes con un alcance claro. | Una cuenta inactiva no recibe asignaciones; cada participante ve solo lo que le corresponde. |
| RF-PLA-003 | confirmed | Un encargo temporal de producción o feria tiene actividad, periodo, alcance y cierre. | Solo permite operaciones mientras esté vigente y dentro de su alcance. |
| RF-PLA-004 | confirmed | Directiva y socias consultan sus actividades y pendientes con filtros comprensibles. | Cada socia ve sus propios datos; una búsqueda sin resultados se explica. |
| RF-PLA-005 | confirmed | Se planifica la producción semanal con producto, cantidad objetivo, responsables e insumos previstos. | El plan es visible para las asignadas, registra cambios y no crea existencias ni lotes por anticipado. |
| RF-ASI-001 | confirmed | Cada instancia conserva entrada y salida separadas, con hora del servidor cuando hay conexión y origen propio o delegado. Una captura offline es provisional. | No se aceptan eventos duplicados o secuencias imposibles; se distingue hora declarada de recepción en capturas sin red. La aceptación tardía depende de P-13. |
| RF-ASI-002 | confirmed | La asistencia conserva unicidad por socia, instancia y tipo de evento; inconsistencias quedan pendientes. | Un duplicado muestra el registro existente; una salida olvidada no recibe una hora inventada. |
| RF-ASI-003 | confirmed | Directiva o encargada autorizada corrige registros sensibles con motivo e historial. | Quien carece de permiso no modifica; se reconstruyen valor anterior, nuevo valor, actor y fecha. |
| RF-ASI-004 | confirmed | La socia consulta su historial y la Directiva consulta según cargo y periodo. | Los filtros y estados se entienden y no exponen datos de otras socias. |
| RF-ASI-005 | confirmed | Se registra participación adicional solo cuando la actividad necesita un dato distinto de asistencia. | Una actividad simple no obliga a completar participación; cada registro se vincula con socia y actividad. |
| RF-ASI-006 | confirmed | Las inconsistencias se mantienen pendientes hasta decisión de la asamblea, registrada por la Directiva. | No se genera una falta o sanción automática; quedan actor, fecha, motivo, acuerdo y cambios. P-03 define consecuencias aún abiertas. |
| RF-ASI-007 | confirmed | La organización puede habilitar fases QR distintas para entrada y salida; hay código alternativo y registro delegado auditable. El token temporal no contiene datos personales. | Token vencido, repetido o de otra acción no modifica asistencia. Se distingue autorregistro de registro delegado y se conserva su motivo. P-02 define duración, responsables y casos de delegación; P-13 rige el uso offline. |
| RF-CAT-001 | confirmed | Se distinguen plantas, materias primas, insumos, empaques, productos, presentaciones y unidades con historia. | Desactivar impide uso nuevo sin borrar registros anteriores. Presentaciones y conversiones siguen en P-04. |
| RF-INV-001 | confirmed | Los valores comerciales tienen vigencia e historia: costo conocido, precio sugerido, precio vigente y valor base. | Un cambio no altera ventas anteriores; un producto inactivo no entra en ventas nuevas. |
| RF-TRA-001 | confirmed | El acopio registra origen, socia, materia, peso o cantidad, unidad, fecha, valoración, responsable y observación. Pesajes habilitados pueden capturarse sin red de forma provisional. | Peso no positivo se rechaza; corrección queda auditada; una captura local no se presenta como aceptación remota. |
| RF-TRA-002 | confirmed | El secado registra peso inicial y final, temperatura en °C, inicio y fin; humedad es opcional. Pesajes habilitados pueden capturarse provisionalmente sin red. | En línea se usa hora del servidor; el cierre exige valores válidos. P-13 debe definir el tratamiento temporal de capturas sin red antes de calcular duraciones. |
| RF-TRA-003 | confirmed | Se calculan duración y merma absoluta con fórmula y unidad visibles; el porcentaje espera reglas de redondeo. | Peso final mayor que inicial exige revisión o excepción autorizada. |
| RF-TRA-004 | confirmed | Cada lote conserva su procedencia; cierre productivo y agotamiento de stock son conceptos distintos. Solo una mezcla física crea un lote derivado. | Se recorren orígenes; una mezcla incompatible se rechaza; atender un pedido desde varios lotes no los fusiona. P-05 rige excepciones. |
| RF-TRA-005 | confirmed | La transformación registra insumos consumidos, composición y versión, resultado, cantidad, residuos, responsable, fecha y lote. | El producto resultante enlaza sus consumos; cantidades incompatibles se rechazan. |
| RF-INV-002 | confirmed | Entradas, consumos, producción, asignaciones, ventas, devoluciones y ajustes generan movimientos. | La existencia deriva de movimientos; un ajuste exige permiso y motivo y la operación se confirma completa. |
| RF-INV-003 | confirmed | Cada entrega de feria identifica encargo, socia, producto, lote, cantidad y modalidad individual o compartida. | No excede el stock; quien recibe confirma o informa diferencia; el origen permanece visible. |
| RF-INV-004 | confirmed | Se concilian productos recibidos, transferidos, vendidos, devueltos y retornados sin mezclarlos con deudas monetarias. | Una diferencia queda visible para conciliar y no produce stock negativo silencioso. |
| RF-VEN-001 | confirmed | La socia encargada registra ventas de varios productos desde stock autorizado, con cantidad, precio, total y forma de pago. | El total se calcula; no se vende más de lo disponible; la venta completa se confirma o se revierte. |
| RF-VEN-002 | confirmed | Se pide identificación del comprador solo según el riesgo: contado puede usar «Público general»; crédito o venta institucional exige datos mínimos aprobados. | Crédito sin comprador se rechaza; contado no solicita datos innecesarios. |
| RF-VEN-003 | confirmed | Cada venta conserva valor base y precio aplicado históricos y calcula excedente bruto sin llamarlo utilidad neta. | Ambos importes se muestran y no cambian retroactivamente. |
| RF-VEN-004 | confirmed | Vender bajo el valor base requiere excepción autorizada, motivo e historial. | La venta ordinaria bajo base se rechaza; la excepción identifica autoridad y diferencia. |
| RF-VEN-005 | confirmed | La Tesorera puede configurar descuentos por volumen con producto, presentación, umbral, valor y vigencia. | Una política incompleta no se aplica. P-08 debe fijar sus valores; vender bajo base también requiere excepción. |
| RF-VEN-006 | confirmed | En feria, cada línea identifica si procede de stock individual o compartido. | Los resultados individuales no se mezclan; el excedente compartido no se reparte automáticamente mientras P-07 esté abierto. |
| RF-VEN-007 | confirmed | La organización registra ventas institucionales desde stock general mediante la Tesorera. | Quedan claros tipo y responsable; no se atribuye excedente a una socia. |
| RF-VEN-008 | confirmed | El comprobante manual único permite una contingencia de feria y registro tardío auditable. No reemplaza la capacidad PWA obligatoria ni autoriza por sí solo venta offline digital. | Un folio repetido no descuenta dos veces; conflictos de stock quedan para revisión. P-10 define custodia, plazos y conciliación. |
| RF-GAS-001 | confirmed | La Tesorera registra gastos con categoría, monto, fecha, concepto, periodo o lote y responsable. | Monto inválido se rechaza; cambios sensibles quedan auditados. |
| RF-GAS-002 | confirmed | La Directiva consulta un resumen de ingresos organizacionales, gastos y pendientes con fórmula visible. | Los totales remiten a su fuente y periodo; no se presenta como balance certificado. |
| RF-CXC-001 | confirmed | Se separan custodia física, deuda de socia y cuenta por cobrar externa; retiro individual impago usa valor base congelado. | Custodia compartida no crea deuda individual; pagos afectan solo el saldo elegido. P-09 rige devoluciones y ajustes monetarios. |
| RF-CXC-002 | confirmed | Se registran abonos con monto, fecha, forma, responsable y saldo aplicado. | Un abono válido reduce el saldo elegido; el tratamiento de sobrepagos depende de P-09. |
| RF-CXC-003 | confirmed | La rendición de feria muestra recibido, vendido, devuelto, sobrante, dinero, base, excedente y diferencias. | Una discrepancia deja el encargo por conciliar y explica qué falta. |
| RF-REP-001 | confirmed | La Directiva consulta asistencia por periodo, actividad y socia con estados y correcciones. | Los totales coinciden con registros; la ausencia de datos se explica. |
| RF-REP-002 | confirmed | La Directiva consulta actividades y encargos por estado, tipo, responsable y periodo. | Los pendientes son visibles con el detalle permitido para su cargo. |
| RF-REP-003 | confirmed | La Directiva consulta acopio, secado, transformación, lotes y merma con unidad y origen. | Los totales enlazan movimientos y no ocultan insumos sin valoración. |
| RF-REP-004 | confirmed | La Directiva consulta existencias derivadas y movimientos por producto, lote y periodo. | La existencia concilia con movimientos; ajustes se distinguen. |
| RF-REP-005 | confirmed | La Tesorera consulta ventas, deuda de socias, deuda externa, pagos y pendientes por separado. | No se mezclan saldos; filtros y fórmulas son visibles. |
| RF-REP-006 | confirmed | Cada socia consulta un resumen privado de asistencia, actividades, productos, valores por entregar, créditos de clientes y excedente bruto. | No ve datos de otras socias ni se presenta excedente como ganancia neta. |
| RF-NOT-001 | confirmed | Las usuarias reciben recordatorios dentro del sistema sobre actividades, asistencia, encargos, rendiciones y registros tardíos. | Cada recordatorio abre el elemento correcto sin depender de correo o mensajería. |
| RF-PUB-001 | confirmed | Visitantes ven solo historia, misión, visión, productos, ubicación, redes y contacto aprobados. | Una sección sin aprobar permanece oculta y no muestra información interna ni sanitaria. P-12 define el contenido. |
| RF-PUB-002 | confirmed | La organización prepara, aprueba, publica y retira contenido según permisos. | Una persona no autorizada no publica; retirar conserva historia. La matriz de permisos se precisa por funcionalidad. |
| RF-PWA-001 | confirmed | La interfaz esencial de los flujos habilitados puede abrirse sin red después de preparar el dispositivo compatible. | Al cortar la red se muestra el estado y las acciones disponibles; el primer uso sin recursos precargados explica la limitación; caché público no expone páginas privadas. |
| RF-PWA-002 | confirmed | Asistencia y pesajes habilitados se guardan localmente como operaciones pendientes con datos mínimos y origen identificable. | La operación persiste al recargar; un fallo local no muestra éxito; otra cuenta no ve la cola; se distingue hora capturada de recepción. P-14 define retención y dispositivo compartido. |
| RF-PWA-003 | confirmed | Al recuperar conexión, se reintenta cada operación con la misma identidad y el servidor revalida sesión, permisos y reglas antes de confirmarla. | Una respuesta perdida y su reintento crean un solo registro; conflicto y revocación se muestran sin mutaciones indebidas; un fallo atómico no deja registros parciales. P-13/P-14 concretan políticas. |
| `RF-COS-001` | proposed | Registrar consumos y costos directos conocidos, sin presentar entradas no valoradas como cero. | Resolver P-06: valoración de plantas propias, trabajo comunitario, mano de obra, energía, transporte y gastos compartidos antes de confirmar. |

## Requisitos funcionales candidatos derivados de la entrevista

Las siguientes propuestas amplían la lista general únicamente para análisis. Las claves `PROP-ENT-Fxx` son referencias temporales, no IDs oficiales. Su prioridad y ubicación también son propuestas. Las menciones parciales en requisitos confirmados no se amplían silenciosamente.

| Ref. temporal | Ubicación propuesta y relación | Requisito candidato | Importancia propuesta | Criterio preliminar y decisión pendiente |
|---|---|---|---|---|
| PROP-ENT-F01 | Capacidad transversal de gestión documental; relacionar con RF-REP-001…006 y RNF-PRV-001. Módulo dueño por decidir. | La Directiva registra y consulta documentos organizacionales y productivos por tipo, entidad relacionada, fecha, vigencia y versión, con acceso según autorización. | Alta; privacidad esencial antes de habilitar documentos sensibles. | Una persona no autorizada no abre ni descarga el archivo; una nueva versión conserva la anterior. Definir si se almacenan documentos personales, firmas, permisos y retención antes de diseñar el alcance. |
| PROP-ENT-F02 | Avisos internos, relacionado con RF-NOT-001 y con el candidato F01. | El sistema identifica vencimientos de documentos habilitados y avisa a las personas autorizadas según anticipación acordada. | Alta para evitar vencimientos; urgencia de definir fechas alta. | Una fecha de vencimiento produce un aviso verificable a destinatarios autorizados. Confirmar tipos de documento y anticipaciones comunicadas de tres meses y seis meses para registros sanitarios; la cobertura y calendario requieren validación. |
| PROP-ENT-F03 | Extensión del dominio de asistencia, relacionada con RF-ASI-001/006/007 y P-03. | El sistema apoya el registro y cálculo transparente de atrasos y faltas conforme a reglas aprobadas y permite revisar el resultado antes de cualquier efecto monetario. | Esencial para evitar cobros erróneos; aclaración inmediata. | Se reconstruyen minutos, evento, regla y revisión humana. Los USD 0,01/min, USD 10 desde la primera falta y aviso a la tercera son valores comunicados, pero no se automatizan hasta definir justificativos, autoridad, redondeo, vigencia y cobro. Resolver la tensión con RF-ASI-006, que prohíbe sanción automática ante inconsistencias. |
| PROP-ENT-F04 | Planificación/avisos internos, relacionada con RF-PLA-001/004 y RF-NOT-001. | Las personas asignadas reciben recordatorios de reuniones o talleres en los plazos acordados. | Alta. | Una actividad notifica a destinatarias correctas uno o dos días antes según configuración aprobada. Confirmar si ambos plazos aplican y qué excepciones existen. |
| PROP-ENT-F05 | Flujo de encargos, relacionada con RF-PLA-003 y RF-TRA-002. | La encargada asigna una tarea de secado con fecha, responsable, estado, confirmación y evidencia de cierre; puede reasignarla si no se confirma. | Alta para responsabilidad y trazabilidad. | Solo responsable o autoridad autorizada actualiza el estado; el cierre conserva evidencia y actor. Definir quién acepta el resultado, formatos de evidencia y cuándo se reasigna. |
| PROP-ENT-F06 | Catálogo/inventario; posible requisito separado de suministros y productos, relacionado con RF-CAT-001 y RF-INV-002. | La Directiva registra activos de la organización separados del inventario consumible y consulta su historial. | Complementaria; candidato para delimitar alcance o incremento posterior. | Dar de alta y retirar un activo conserva su historial y no altera el stock de insumos. Definir datos y responsables. La depreciación queda fuera hasta acordar método, vida útil y tratamiento contable. |
| PROP-ENT-F07 | Inventario, relacionada con RF-INV-002/003/004 y RF-TRA-004. | El sistema distingue stock organizacional y stock bajo custodia individual y permite conciliarlos sin convertir automáticamente custodia en deuda. | Alta por impacto en existencias y rendiciones. | Cada movimiento conserva origen, destino, responsable y saldo; una diferencia queda pendiente de conciliación. Definir propiedad, custodia, transferencias, devoluciones y reglas para deuda. |
| PROP-ENT-F08 | Producción/trazabilidad, relacionada con RF-PLA-005, RF-TRA-005 y RF-INV-002. | La organización registra recetas aprobadas con insumos, unidades y rendimiento y consulta alertas cuando una materia habilitada se acerca a un mínimo acordado. | Alta por riesgo de producir o abastecer con cálculos erróneos. | Una receta conserva versión y unidades; un aviso muestra umbral y existencia fuente. Validar fórmulas, conversiones, mermas y mínimos por planta. El ejemplo «50 litros = 100 champús» no se incorpora como regla. |
| PROP-ENT-F09 | Sitio público/consulta comercial, relacionada con RF-PUB-001/002 y RF-VEN-001. | La organización puede publicar precios aprobados y ofrecer un contacto personalizado por WhatsApp, identificándolo como consulta o como pedido según la decisión de alcance. | Complementaria; decidir antes de publicar el contenido. | Solo se muestra precio vigente aprobado; el enlace identifica producto y no crea una venta/pedido sin confirmación. Resolver P-12, responsables de precios y si se requiere registro de pedidos. |
| PROP-ENT-F10 | Feria y rendición, relacionada con RF-INV-003/004, RF-VEN-006/008, RF-GAS-001 y RF-CXC-003. | La encargada registra por separado gastos previstos y reales y prepara una rendición de comisiones usando una fórmula autorizada. | Esencial para conciliación económica; aclaración inmediata de fórmula. | La rendición distingue estimado, comprobado, ventas, devoluciones y comisión; no calcula reparto mientras falte fórmula aprobada. Definir base, porcentaje, destinatarios, excepciones y autorización. |
| PROP-ENT-F11 | Venta individual mensual, relacionada con RF-INV-003/004, RF-VEN-001/003/006 y RF-CXC-001/002. | La organización registra entregas y ventas mensuales por socia y concilia productos, pagos a la asociación, saldos y comisión individual conforme a reglas aprobadas. | Alta por impacto en dinero y stock individual/general. | El periodo concilia unidades entregadas, vendidas, devueltas y saldo monetario; diferencias quedan visibles. Definir periodo, devolución, valor base, comisión, saldo y fuente de inventario antes de calcular. |
| PROP-ENT-F12 | Canal externo opcional de avisos, relacionado con RF-NOT-001 y RNF-SEC-001/RNF-PRV-001. | Si se aprueba automatización, el sistema envía avisos externos solo a destinatarios habilitados y con consentimiento registrado. | Complementaria; depende de decisión de canal, privacidad y costo. | Se registra autorización, destinatario y resultado; fallos no se presentan como enviados y reintentos no duplican avisos. Decidir enlace manual frente a envío automático, consentimiento, costos y responsable del canal. |

## Requisitos no funcionales

La lista incluye los nueve requisitos confirmados y el único requisito no funcional propuesto. El propuesto se muestra aparte por estado y no forma parte de la línea base aprobada.

| ID | Estado | Requisito | Criterio de comprobación |
|---|---|---|---|
| RNF-UX-001 | confirmed | La interfaz debe permitir completar las tareas esenciales en móviles desde 360 px, con acciones claras y formularios breves. | Recorrer tareas críticas en pantallas pequeñas y dispositivos reales sin desplazamiento horizontal accidental ni controles ocultos. |
| RNF-UX-002 | confirmed | La interfaz debe ser accesible: contraste AA, teclado, foco visible, etiquetas comprensibles y errores recuperables. | Revisar zoom de 200 %, navegación por teclado, foco, resumen de errores y objetivos táctiles de al menos 44 px. |
| RNF-UX-003 | confirmed | Se usa lenguaje cotidiano y el sistema calcula lo que no corresponde calcular manualmente a las socias. | Usuarias completan recorridos sin seleccionar roles técnicos ni hacer fórmulas manuales. |
| RNF-CON-001 | confirmed | El sistema debe ser ligero y resistir cortes. Los recursos esenciales y los flujos habilitados funcionan con PWA; distingue guardado local, pendiente, aceptado y rechazado. | Cortar y recuperar conexión durante tareas habilitadas; no mostrar éxito remoto antes de confirmación ni duplicar operaciones al reintentar. Los detalles de P-13/P-14 siguen pendientes. |
| RNF-SEC-001 | confirmed | Toda operación sensible verifica autorización en el servidor, aunque la interfaz o una petición directa intente eludirla. | Probar casos permitidos y denegados; una denegación no cambia datos. |
| RNF-AUD-001 | confirmed | Correcciones, aprobaciones y excepciones deben poder reconstruirse con dato original, cambio o reversión, actor, fecha, autorización y motivo. | Un cambio sensible conserva la historia verificable dentro de la operación que lo confirma. |
| RNF-DAT-001 | confirmed | Los cambios que afectan varias entidades se confirman juntos y las existencias se derivan de movimientos, sin totales editables sin respaldo. | Un error revierte todo; no se produce sobreventa, saldo negativo silencioso ni movimiento parcial. |
| RNF-PRV-001 | confirmed | Se recoge solo la información necesaria y se separan claramente datos internos de contenido público. | Una persona sin permiso y el sitio público no muestran datos personales u operativos innecesarios. |
| RNF-PDF-001 | confirmed | Los reportes descargables en PDF deben ser claros, trazables y comprensibles sin depender solo del color. | Cada PDF incluye título, periodo, filtros, fecha, unidades, totales conciliados y logo autorizado cuando esté disponible. |
| `RNF-OPS-001` | proposed | Copias protegidas y restauración demostrable. | Resolver P-11: responsables, proveedor, retención, RPO/RTO, frecuencia y autorización de restauración. |

## Requisitos no funcionales candidatos derivados de la entrevista

# Requisitos no funcionales candidatos derivados de la entrevista

Estas propuestas no amplían RNF confirmados hasta su validación. Las claves son temporales y no son IDs oficiales.

| Ref. temporal | Ubicación propuesta y relación | Exigencia candidata | Importancia propuesta | Criterio preliminar y decisión pendiente |
|---|---|---|---|---|
| PROP-ENT-NF01 | Extiende privacidad y autorización, relacionado con RNF-PRV-001, RNF-SEC-001 y RNF-AUD-001. | Los documentos sensibles, justificativos y datos personales se protegen por acceso mínimo, historial de consulta/cambio y una regla de conservación y retiro aprobada. | Esencial antes de habilitar repositorio documental o expedientes personales. | Acceso directo no autorizado se deniega y queda registro; la retención y eliminación siguen una política aprobada. Definir categorías, responsables, periodos y base de autorización. |
| PROP-ENT-NF02 | Extiende comunicación externa, relacionado con RNF-SEC-001, RNF-PRV-001 y RNF-AUD-001. | Los avisos externos conservan destinatario autorizado, consentimiento, contenido permitido y resultado de envío sin exponer información innecesaria. | Alta si se aprueba mensajería automática; no aplica a un enlace que la usuaria abre manualmente. | Destinatario sin consentimiento no recibe mensaje; fallo y reintento quedan distinguibles y no generan duplicados. Confirmar canal, costo, proveedor y contenido. |

## Priorización propuesta de necesidades de entrevista

La importancia valora impacto si la función se aprueba. La urgencia de aclaración indica qué decisión resolver primero; no ordena sprints ni autoriza implementación.

| Orden para aclarar | Tema/candidatos | Importancia propuesta | Motivo y puerta previa |
|---:|---|---|---|
| 1 | Sanciones y asistencia (F03) | Esencial | Impacto monetario directo y tensión con RF-ASI-006. Resolver P-03, evidencia del acuerdo, justificativos, autoridad, redondeo y cobro antes de automatizar. |
| 2 | Privacidad documental (F01, NF01) | Esencial | La entrevista incluye documentos personales y justificativos. Delimitar datos, acceso, conservación y retiro antes de crear repositorio. |
| 3 | Comisiones, venta mensual e inventario personal (F07, F10, F11) | Esencial/Alta | Errores afectan dinero y existencias. Cerrar bases, fórmulas, devoluciones y conciliación vinculadas con P-06/P-07/P-09. |
| 4 | Vencimientos y encargos (F02, F05) | Alta | Evitar documentos vencidos y tareas sin responsable/cierre; confirmar fechas y autoridad. |
| 5 | Recetas y mínimos (F08) | Alta | Previene cálculos y compras/producción incorrectos; no fijar fórmula ni umbral desde ejemplos. |
| 6 | Agenda y mensajería externa (F04, F12, NF02) | Alta para aclaración; canal externo complementario | Confirmar plazos, canal, consentimiento, costos y contenido antes de conectar proveedor. |
| 7 | Activos (F06) | Complementaria | Alcance contable adicional; registrar inventario básico puede separarse de depreciación, que requiere regla. |
| 8 | Precio público/contacto (F09) | Complementaria | Depende de P-12 y de distinguir consulta de pedido antes de exponer precios. |

Los importes sobre tiempo perdido, USD 15 por inconsistencia, abogado y pérdida eventual de USD 20.000 pertenecen al análisis de factibilidad y no se convierten en requisitos funcionales. Confirmar sus bases antes de usarlos como ahorro o retorno.

## Puertas antes de promover esta propuesta

1. Revisar y resolver las preguntas de política, alcance y autoridad de EVID-ENT-2026-10-12-001.
2. Confirmar con tesista y organización qué propuestas entran en la línea base y en qué versión; la comunicación del tesista sobre aprobación de montos no sustituye acta ni resuelve los detalles abiertos.
3. Validar con la directora los cambios que afecten anteproyecto y alcance académico.
4. Asignar IDs canónicos solo después de aprobar cada propuesta; actualizar CAT-REQ-001, matriz de trazabilidad, prioridad, historias y plan de entrega después de esa aprobación.
5. Mantener las propuestas fuera de especificaciones listas para implementar hasta cerrar datos, permisos y criterios aplicables.

## Requisitos históricos sustituidos

Los 12 IDs históricos se conservan para trazabilidad; no forman parte de la línea base vigente y no deben reactivarse sin una nueva decisión.

| ID anterior | Estado | Sustitución o tratamiento actual |
|---|---|---|
| `RF-OFF-001`, `RF-OFF-002`, `RF-OFF-003` | `superseded` | Sustituidos en v1.0 por contingencia manual; desde v1.1 las capacidades vigentes son `RF-PWA-001/002/003` y `RNF-CON-001` revisado. Se conservan los IDs históricos sin reactivarlos |
| `RN-ACC-001` | `superseded` | Alcance absorbido por `RF-ACC-003`; detalle abierto P-01 |
| `RN-ASI-001` | `superseded` | Alcance absorbido por `RF-ASI-006`; detalle abierto P-03 |
| `RN-ASI-002` | `superseded` | Alcance absorbido por `RF-ASI-007`; detalle abierto P-02 |
| `RN-CAT-001` | `superseded` | Alcance absorbido por `RF-CAT-001`; datos abiertos P-04 |
| `RN-TRA-001` | `superseded` | Alcance absorbido por `RF-TRA-004`; excepciones abiertas P-05 |
| `RN-VEN-001` | `superseded` | Alcance absorbido por `RF-VEN-006`; fórmula abierta P-07 |
| `RN-CXC-001` | `superseded` | Alcance absorbido por `RF-CXC-001`; efectos abiertos P-09 |
| `RN-CON-001` | `superseded` | Alcance absorbido por `RF-VEN-008`; procedimiento abierto P-10 |
| `RN-PUB-001` | `superseded` | Alcance absorbido por `RF-PUB-001` y `RF-PUB-002`; contenido abierto P-12 |

## Regla para futuras versiones

Cuando se apruebe una modificación de la línea base, se generará una nueva versión de este documento general con sus tablas funcional y no funcional actualizadas. La nueva edición indicará la versión fuente de CAT-REQ-001, conservará estados y trazabilidad de los IDs, y se registrará en el [índice de documentación](../README.md) y en el control de cambios. Las ediciones anteriores se conservarán como historial; no se sobrescribirán. La preparación o actualización documental no constituye por sí sola una aprobación del requisito.

## Fuentes

- [Catálogo canónico CAT-REQ-001 v1.1](../../../docs/requirements/CAT-REQ-001.md).
- [Edición de requisitos funcionales v1.1](../../../documentacion/requisitos/funcionales/requisitos_funcionales_v1.1_2026-10-12.md).
- [Edición de requisitos no funcionales v1.1](../../../documentacion/requisitos/no_funcionales/requisitos_no_funcionales_v1.1_2026-10-12.md).
- [Evidencia de aprobación de CAT-REQ-001 v1.1](../../../docs/evidence/casos-de-uso/2026-09-28-aprobacion-requisitos-v1-1.md).

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 2.0-candidato | 2026-10-13 | Se conserva la línea base y se agregan 12 candidatos funcionales y 2 no funcionales derivados de entrevista, priorizados para revisión. | Candidato interno; no aprobado |

