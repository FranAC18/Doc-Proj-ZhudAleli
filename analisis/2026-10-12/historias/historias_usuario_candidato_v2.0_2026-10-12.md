---
titulo: Historias de usuario de Zhud Alelí adaptadas al formato de cátedra
version: "2.0"
fecha: 2026-10-12
autor: Codex, para revisión del tesista
estado: candidato-interno
fuente_requisitos: "CAT-REQ-001 v1.1"
fuente_formato: "Material de Aplicaciones Informáticas II, secciones 2.7 a 2.9"
historias: 51
prioridad: orden-preliminar-por-validar
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: no-autorizada
---

# Historias de usuario — candidato adaptado al material de cátedra

Cada historia se centra en una capacidad confirmada y expresa **rol, función y beneficio**. Sus pruebas de aceptación contienen contexto, evento y resultado esperado; hay un máximo de cuatro por historia. El texto evita describir pantallas, pasos de navegación o flujo interno de trabajo. El ID `HU-...` corresponde al requisito `RF-...` del mismo sufijo; no crea un requisito nuevo.

La **prioridad** es una posición preliminar en la pila del producto, sujeta a validación y refinamiento. La **estimación** queda pendiente de quien realizará el trabajo; no se asignan puntos u horas sin esa estimación. Las decisiones P-02 a P-14 conservan sus límites, por lo que una historia puede estar priorizada y todavía no estar lista para un sprint. La revisión de la directora y la validación de la organización de los ajustes v1.1 no constan realizadas.

## Sprint 1 — acceso y administración

### HU-ACC-001 — Entrar y salir de la parte privada

**Historia:** Como usuaria interna con cuenta activa, quiero iniciar y cerrar sesión, para proteger mi información organizacional.

**Ficha:** requisito `RF-ACC-001`; prioridad preliminar: posición 6 de 60; estimación: pendiente del equipo; dependencias: HT-GEN-001, HT-GEN-002.

**Pruebas de aceptación:**

1. Dada una cuenta activa, cuando ingresa con credenciales correctas, entonces accede solo a información autorizada.
2. Dada una cuenta inactiva o credenciales incorrectas, cuando intenta entrar, entonces no obtiene acceso ni información privada.
3. Dada una sesión activa, cuando la usuaria la cierra, entonces deja de poder acceder a información privada con esa sesión.

### HU-ACC-002 — Administrar membresías

**Historia:** Como integrante autorizada de la Directiva, quiero activar o desactivar cuentas de socias, para mantener vigentes los accesos sin perder la historia.

**Ficha:** requisito `RF-ACC-002`; prioridad preliminar: posición 7 de 60; estimación: pendiente del equipo; dependencias: HU-ACC-001, HT-GEN-002.

**Pruebas de aceptación:**

1. Dada una cuenta de socia, cuando la Directiva la desactiva, entonces cesan los nuevos accesos y se conservan sus registros.
2. Dada una socia sin permiso, cuando intenta cambiar una membresía, entonces el sistema rechaza el cambio.

### HU-ACC-003 — Usar funciones según responsabilidades

**Historia:** Como usuaria interna, quiero realizar solo operaciones permitidas por mi perfil, cargo o encargo, para respetar las responsabilidades de la organización.

**Ficha:** requisito `RF-ACC-003`; prioridad preliminar: posición 8 de 60; estimación: pendiente del equipo; dependencias: HU-ACC-001, HT-GEN-002.

**Pruebas de aceptación:**

1. Dado un encargo vencido o un cargo sin autorización, cuando la usuaria intenta una operación restringida, entonces esta se rechaza sin cambiar datos.

### HU-ACC-004 — Ver mis opciones disponibles

**Historia:** Como usuaria interna, quiero consultar mis actividades, pendientes y encargos disponibles, para saber qué puedo hacer ahora.

**Ficha:** requisito `RF-ACC-004`; prioridad preliminar: posición 15 de 60; estimación: pendiente del equipo; dependencias: HU-ACC-001, HU-ACC-003.

**Pruebas de aceptación:**

1. Dada una sesión válida, cuando la usuaria consulta su inicio privado, entonces encuentra únicamente actividades y acciones que le corresponden.

## Sprint 2 — planificación

### HU-PLA-001 — Programar una actividad

**Historia:** Como integrante de la Directiva, quiero registrar jornadas y eventos, para coordinar el trabajo de la organización.

**Ficha:** requisito `RF-PLA-001`; prioridad preliminar: posición 9 de 60; estimación: pendiente del equipo; dependencias: HU-ACC-003.

**Pruebas de aceptación:**

1. Dados fecha, hora, lugar y responsable válidos, cuando la Directiva registra una actividad, entonces esta queda asociada a sus participantes y estado.

### HU-PLA-002 — Asignar participantes y responsables

**Historia:** Como integrante de la Directiva, quiero asignar personas a una actividad, para clarificar quién participa y quién responde por ella.

**Ficha:** requisito `RF-PLA-002`; prioridad preliminar: posición 10 de 60; estimación: pendiente del equipo; dependencias: HU-PLA-001, HU-ACC-003.

**Pruebas de aceptación:**

1. Dada una actividad existente, cuando se asigna una cuenta activa dentro del alcance autorizado, entonces la persona queda vinculada a esa actividad.
2. Dada una cuenta inactiva, cuando se intenta asignarla, entonces la asignación se rechaza.

### HU-PLA-003 — Crear un encargo temporal

**Historia:** Como integrante de la Directiva, quiero asignar una responsabilidad de producción o feria por un periodo, para delegar tareas con límites claros.

**Ficha:** requisito `RF-PLA-003`; prioridad preliminar: posición 11 de 60; estimación: pendiente del equipo; dependencias: HU-PLA-001, HU-PLA-002.

**Pruebas de aceptación:**

1. Dados tipo, actividad, periodo y alcance válidos, cuando se asigna un encargo, entonces solo habilita las operaciones correspondientes mientras esté vigente.

### HU-PLA-004 — Consultar mis actividades

**Historia:** Como socia, quiero consultar actividades y pendientes que me corresponden, para organizar mi participación.

**Ficha:** requisito `RF-PLA-004`; prioridad preliminar: posición 12 de 60; estimación: pendiente del equipo; dependencias: HU-PLA-001, HU-PLA-002.

**Pruebas de aceptación:**

1. Dadas actividades asignadas, cuando la socia consulta sus pendientes, entonces ve sus propios registros y no información privada ajena.

### HU-PLA-005 — Planificar producción semanal

**Historia:** Como integrante autorizada de la Directiva, quiero definir productos, objetivos, insumos y responsables de la semana, para coordinar la producción prevista.

**Ficha:** requisito `RF-PLA-005`; prioridad preliminar: posición 14 de 60; estimación: pendiente del equipo; dependencias: HU-PLA-001, HU-CAT-001.

**Pruebas de aceptación:**

1. Dados producto, cantidad objetivo y responsables válidos, cuando se registra el plan semanal, entonces queda disponible para las asignadas sin crear existencias anticipadas.

## Sprint 3 — asistencia y participación

### HU-ASI-001 — Registrar entrada y salida

**Historia:** Como socia, quiero registrar por separado mi entrada y salida, para contar con asistencia verificable.

**Ficha:** requisito `RF-ASI-001`; prioridad preliminar: posición 22 de 60; estimación: pendiente del equipo; dependencias: HU-PLA-001, HU-ACC-003; HU-PWA-002 solo para captura sin red.

**Pruebas de aceptación:**

1. Dada una actividad habilitada, cuando se registra una entrada o salida en línea, entonces queda el tipo de evento, la hora del servidor y su origen.
2. Dada una captura sin red habilitada, cuando se conserva localmente, entonces queda provisional y diferencia hora declarada de recepción.

### HU-ASI-002 — Evitar asistencia duplicada

**Historia:** Como socia, quiero conservar un solo evento de cada tipo por actividad, para evitar registros contradictorios.

**Ficha:** requisito `RF-ASI-002`; prioridad preliminar: posición 23 de 60; estimación: pendiente del equipo; dependencias: HU-ASI-001.

**Pruebas de aceptación:**

1. Dado un evento de asistencia ya registrado, cuando se intenta repetirlo para la misma socia y actividad, entonces no se crea otro y se informa el registro existente.

### HU-ASI-003 — Corregir asistencia con historial

**Historia:** Como integrante de la Directiva o encargada autorizada, quiero corregir un registro sensible con motivo, para resolver errores sin borrar la historia.

**Ficha:** requisito `RF-ASI-003`; prioridad preliminar: posición 24 de 60; estimación: pendiente del equipo; dependencias: HU-ASI-001, HT-GEN-003.

**Pruebas de aceptación:**

1. Dado un registro de asistencia y autorización vigente, cuando se corrige con motivo, entonces se conservan actor, fecha, valor anterior y nuevo valor.
2. Dada una persona sin permiso, cuando intenta corregir, entonces no cambia el registro.

### HU-ASI-004 — Consultar historial de asistencia

**Historia:** Como socia, quiero consultar mi asistencia por periodo, para conocer mis registros y sus estados.

**Ficha:** requisito `RF-ASI-004`; prioridad preliminar: posición 25 de 60; estimación: pendiente del equipo; dependencias: HU-ASI-001, HT-GEN-002.

**Pruebas de aceptación:**

1. Dado un periodo consultado, cuando la socia solicita su historial, entonces ve sus eventos y estados sin acceso a los de otra socia.

### HU-ASI-005 — Registrar participación adicional

**Historia:** Como responsable autorizada de una actividad, quiero registrar una participación distinta de la asistencia cuando se necesite, para reflejar el aporte real de las socias.

**Ficha:** requisito `RF-ASI-005`; prioridad preliminar: posición 26 de 60; estimación: pendiente del equipo; dependencias: HU-PLA-001, HU-ASI-001.

**Pruebas de aceptación:**

1. Dada una actividad que exige participación adicional, cuando se registra ese dato, entonces queda vinculado a la socia y actividad.
2. Dada una actividad simple, cuando se confirma la asistencia, entonces no se exige participación adicional.

### HU-ASI-006 — Resolver una inconsistencia de asistencia

**Historia:** Como integrante autorizada de la Directiva, quiero registrar el acuerdo de la asamblea sobre una inconsistencia, para conservar una decisión justa y rastreable.

**Ficha:** requisito `RF-ASI-006`; prioridad preliminar: posición 27 de 60; estimación: pendiente del equipo; dependencias: HU-ASI-001, HU-ASI-003.

**Pruebas de aceptación:**

1. Dada una inconsistencia pendiente, cuando se registra una decisión de la asamblea, entonces quedan acuerdo, actor, fecha y motivo sin sanción automática.

### HU-ASI-007 — Registrar asistencia con QR o alternativa

**Historia:** Como socia, quiero usar un QR temporal o código alternativo para mi asistencia, para registrarla por un medio disponible y auditable.

**Ficha:** requisito `RF-ASI-007`; prioridad preliminar: posición 28 de 60; estimación: pendiente del equipo; dependencias: HU-ASI-001, HU-ACC-003.

**Pruebas de aceptación:**

1. Dado un QR válido para la fase habilitada, cuando la socia registra su evento, entonces queda identificado como autorregistro.
2. Dado un token vencido, repetido o para otra acción, cuando se intenta registrar asistencia, entonces no se modifica el evento.
3. Dado un registro delegado autorizado, cuando se confirma, entonces quedan identificadas la socia, la persona delegada y el motivo.

## Sprint 4 — producción, inventario y rendición

### HU-CAT-001 — Mantener catálogo productivo

**Historia:** Como integrante autorizada de la Directiva, quiero distinguir materias primas, insumos, productos y unidades, para usar datos coherentes en producción y venta.

**Ficha:** requisito `RF-CAT-001`; prioridad preliminar: posición 13 de 60; estimación: pendiente del equipo; dependencias: HU-ACC-003.

**Pruebas de aceptación:**

1. Dado un elemento de catálogo activo, cuando se usa en una operación permitida, entonces conserva su tipo y unidad.
2. Dado un elemento desactivado, cuando se intenta usarlo en una operación nueva, entonces se rechaza sin borrar su historia.

### HU-INV-001 — Conservar valores comerciales históricos

**Historia:** Como Tesorera autorizada, quiero mantener precios y valor base con vigencia, para explicar cada venta según los valores de su momento.

**Ficha:** requisito `RF-INV-001`; prioridad preliminar: posición 29 de 60; estimación: pendiente del equipo; dependencias: HU-CAT-001, HU-ACC-003.

**Pruebas de aceptación:**

1. Dado un cambio de valor comercial, cuando se aplica a operaciones nuevas, entonces una venta anterior conserva el valor histórico utilizado.

### HU-TRA-001 — Registrar acopio de materia

**Historia:** Como socia encargada de producción, quiero registrar materia recibida, cantidad y origen, para conocer quién entregó cada insumo.

**Ficha:** requisito `RF-TRA-001`; prioridad preliminar: posición 30 de 60; estimación: pendiente del equipo; dependencias: HU-CAT-001, HU-PLA-003.

**Pruebas de aceptación:**

1. Dados origen, unidad, responsable y peso positivo, cuando se registra acopio, entonces queda trazable la entrega.
2. Dado un peso no positivo, cuando se intenta registrar, entonces la operación se rechaza.

### HU-TRA-002 — Registrar secado

**Historia:** Como socia encargada de producción, quiero registrar pesos, temperatura e inicio y fin del secado, para seguir cada proceso productivo.

**Ficha:** requisito `RF-TRA-002`; prioridad preliminar: posición 31 de 60; estimación: pendiente del equipo; dependencias: HU-TRA-001, HU-PLA-003.

**Pruebas de aceptación:**

1. Dados peso inicial y temperatura válidos, cuando se inicia el secado, entonces se conservan sus datos y el momento correspondiente.
2. Dados peso final y cierre válidos, cuando termina el secado, entonces queda el cierre sin exigir humedad opcional.

### HU-TRA-003 — Conocer duración y merma

**Historia:** Como responsable de producción, quiero conocer la duración y pérdida de peso de un secado, para evaluar el resultado del proceso.

**Ficha:** requisito `RF-TRA-003`; prioridad preliminar: posición 32 de 60; estimación: pendiente del equipo; dependencias: HU-TRA-002.

**Pruebas de aceptación:**

1. Dado un secado con inicio, fin y pesos válidos, cuando se consulta su resultado, entonces se muestran duración y merma absoluta con unidad y fórmula.
2. Dado un peso final mayor que el inicial, cuando se calcula el resultado, entonces queda pendiente de revisión o excepción autorizada.

### HU-TRA-004 — Seguir la procedencia de lotes

**Historia:** Como responsable de producción, quiero relacionar un lote con sus orígenes y derivados, para reconstruir la procedencia de un producto.

**Ficha:** requisito `RF-TRA-004`; prioridad preliminar: posición 33 de 60; estimación: pendiente del equipo; dependencias: HU-TRA-001, HU-TRA-002.

**Pruebas de aceptación:**

1. Dada una mezcla física permitida, cuando se crea un lote derivado, entonces sus lotes de origen permanecen identificables.
2. Dado un lote cerrado, cuando aún tiene existencias, entonces no se confunde cierre productivo con stock agotado.

### HU-TRA-005 — Registrar transformación

**Historia:** Como socia encargada de producción, quiero registrar insumos consumidos y producto resultante, para conservar la composición y cantidad de cada lote.

**Ficha:** requisito `RF-TRA-005`; prioridad preliminar: posición 34 de 60; estimación: pendiente del equipo; dependencias: HU-TRA-004, HU-CAT-001.

**Pruebas de aceptación:**

1. Dados insumos y composición válidos, cuando se confirma la transformación, entonces el producto resultante queda vinculado a consumos, versión y lote.

### HU-INV-002 — Reconstruir existencias

**Historia:** Como responsable de inventario, quiero consultar existencias derivadas de movimientos, para evitar saldos sin respaldo.

**Ficha:** requisito `RF-INV-002`; prioridad preliminar: posición 35 de 60; estimación: pendiente del equipo; dependencias: HU-CAT-001, HT-GEN-003.

**Pruebas de aceptación:**

1. Dadas entradas, consumos, ventas y devoluciones confirmadas, cuando se calcula la existencia, entonces coincide con sus movimientos.
2. Dado un ajuste autorizado, cuando se confirma con motivo, entonces el cambio queda registrado íntegramente.

### HU-INV-003 — Entregar productos para feria

**Historia:** Como socia encargada de feria, quiero recibir productos identificados por lote y modalidad, para rendir cuentas de lo que quedó bajo mi custodia.

**Ficha:** requisito `RF-INV-003`; prioridad preliminar: posición 36 de 60; estimación: pendiente del equipo; dependencias: HU-INV-002, HU-PLA-003.

**Pruebas de aceptación:**

1. Dado stock suficiente y un encargo vigente, cuando se confirma una entrega, entonces quedan producto, lote, cantidad, socia y origen individual o compartido.
2. Dada cantidad superior al stock, cuando se intenta entregar, entonces se rechaza.

### HU-INV-004 — Conciliar productos de feria

**Historia:** Como socia encargada de feria, quiero comparar productos recibidos, vendidos y devueltos, para explicar diferencias físicas.

**Ficha:** requisito `RF-INV-004`; prioridad preliminar: posición 37 de 60; estimación: pendiente del equipo; dependencias: HU-INV-003, HU-INV-002.

**Pruebas de aceptación:**

1. Dado un encargo con movimientos, cuando se realiza la conciliación, entonces se distinguen recibidos, transferidos, vendidos, devueltos y sobrantes.
2. Dada una diferencia, cuando se cierra el recuento, entonces permanece visible sin generar stock negativo silencioso.

### HU-VEN-001 — Registrar una venta

**Historia:** Como socia encargada de feria, quiero registrar varios productos y su forma de pago, para conocer el total sin vender más de lo disponible.

**Ficha:** requisito `RF-VEN-001`; prioridad preliminar: posición 38 de 60; estimación: pendiente del equipo; dependencias: HU-INV-002, HU-INV-003, HT-GEN-003.

**Pruebas de aceptación:**

1. Dado stock autorizado suficiente, cuando se confirma una venta de varios productos, entonces se registra completa con total calculado.
2. Dado stock insuficiente, cuando se intenta confirmar, entonces no se registra ninguna parte de la venta.

### HU-VEN-002 — Identificar comprador según la venta

**Historia:** Como socia encargada de venta, quiero registrar los datos de comprador necesarios, para conservar un cobro rastreable sin pedir datos de más.

**Ficha:** requisito `RF-VEN-002`; prioridad preliminar: posición 39 de 60; estimación: pendiente del equipo; dependencias: HU-VEN-001.

**Pruebas de aceptación:**

1. Dada una venta a crédito o institucional, cuando se intenta confirmar sin comprador identificado, entonces se rechaza.
2. Dada una venta al contado ordinaria, cuando se registra, entonces puede usar Público general sin pedir datos personales innecesarios.

### HU-VEN-003 — Conocer valor base y excedente

**Historia:** Como socia encargada de venta, quiero conocer valor base, precio aplicado y excedente bruto de la venta, para rendir cuentas sin confundir excedente con utilidad neta.

**Ficha:** requisito `RF-VEN-003`; prioridad preliminar: posición 40 de 60; estimación: pendiente del equipo; dependencias: HU-VEN-001, HU-INV-001.

**Pruebas de aceptación:**

1. Dada una venta confirmada, cuando se consulta su resultado, entonces conserva valor base y precio aplicado históricos y calcula excedente bruto.

### HU-VEN-004 — Autorizar venta bajo valor base

**Historia:** Como integrante autorizada de la Directiva, quiero decidir una excepción de precio bajo el valor base, para proteger y explicar el resultado comercial.

**Ficha:** requisito `RF-VEN-004`; prioridad preliminar: posición 41 de 60; estimación: pendiente del equipo; dependencias: HU-VEN-001, HU-VEN-003.

**Pruebas de aceptación:**

1. Dada una venta bajo valor base sin autorización, cuando se intenta confirmar, entonces se rechaza.
2. Dada una excepción autorizada con motivo, cuando se confirma, entonces quedan responsable, diferencia y razón registrados.

### HU-VEN-005 — Configurar descuento por volumen

**Historia:** Como Tesorera, quiero definir descuentos con umbral, valor y vigencia, para aplicar reglas comerciales aprobadas de forma consistente.

**Ficha:** requisito `RF-VEN-005`; prioridad preliminar: posición 42 de 60; estimación: pendiente del equipo; dependencias: HU-CAT-001, HU-INV-001, HU-VEN-001.

**Pruebas de aceptación:**

1. Dada una política con datos incompletos, cuando una venta cumple la cantidad indicada, entonces no se aplica descuento.
2. Dada una política completa y vigente, cuando se cumplen sus condiciones, entonces se aplica el valor configurado respetando excepciones bajo base.

### HU-VEN-006 — Distinguir stock individual y compartido

**Historia:** Como socia encargada de feria, quiero identificar el origen de cada línea vendida, para separar resultados individuales y compartidos.

**Ficha:** requisito `RF-VEN-006`; prioridad preliminar: posición 43 de 60; estimación: pendiente del equipo; dependencias: HU-INV-003, HU-VEN-001.

**Pruebas de aceptación:**

1. Dada una venta de feria, cuando se confirma una línea, entonces conserva si el producto procede de stock individual o compartido.
2. Dado excedente de stock compartido, cuando se presenta el resultado, entonces no se reparte automáticamente.

### HU-VEN-007 — Registrar venta institucional

**Historia:** Como Tesorera, quiero registrar una venta desde stock general, para rendir cuentas sin atribuir excedente a una socia.

**Ficha:** requisito `RF-VEN-007`; prioridad preliminar: posición 44 de 60; estimación: pendiente del equipo; dependencias: HU-VEN-001, HU-VEN-002.

**Pruebas de aceptación:**

1. Dado stock general y una compradora institucional identificada, cuando se confirma la venta, entonces quedan su tipo y responsable sin asignar excedente individual.

### HU-VEN-008 — Conciliar comprobante manual de feria

**Historia:** Como socia encargada de feria, quiero incorporar una venta respaldada por comprobante de contingencia, para evitar pérdidas y duplicados durante fallos.

**Ficha:** requisito `RF-VEN-008`; prioridad preliminar: posición 45 de 60; estimación: pendiente del equipo; dependencias: HU-VEN-001, HU-INV-004.

**Pruebas de aceptación:**

1. Dado un comprobante manual con folio único, cuando se incorpora después de la contingencia, entonces se conserva su origen y momento declarado.
2. Dado un folio ya registrado, cuando se intenta incorporarlo de nuevo, entonces no descuenta stock dos veces.

### HU-GAS-001 — Registrar gasto operativo

**Historia:** Como Tesorera, quiero registrar un gasto con categoría, monto y periodo, para conocer los egresos vinculados al trabajo.

**Ficha:** requisito `RF-GAS-001`; prioridad preliminar: posición 46 de 60; estimación: pendiente del equipo; dependencias: HU-ACC-003.

**Pruebas de aceptación:**

1. Dado monto positivo y datos válidos, cuando se confirma un gasto, entonces quedan concepto, periodo o lote, responsable y fecha.
2. Dado monto inválido, cuando se intenta registrar, entonces se rechaza.

### HU-GAS-002 — Consultar resumen económico

**Historia:** Como integrante autorizada de la Directiva, quiero consultar ingresos, gastos y pendientes, para comprender los resultados del periodo.

**Ficha:** requisito `RF-GAS-002`; prioridad preliminar: posición 50 de 60; estimación: pendiente del equipo; dependencias: HU-GAS-001, HU-VEN-001, HU-CXC-001.

**Pruebas de aceptación:**

1. Dado un periodo con operaciones, cuando se consulta el resumen, entonces cada total indica su fuente y fórmula sin presentarse como balance certificado.

### HU-CXC-001 — Distinguir deudas y custodia

**Historia:** Como Tesorera, quiero distinguir deuda de socia, cuenta por cobrar externa y custodia física, para evitar cargos monetarios incorrectos.

**Ficha:** requisito `RF-CXC-001`; prioridad preliminar: posición 47 de 60; estimación: pendiente del equipo; dependencias: HU-INV-003, HU-VEN-001, HU-INV-001.

**Pruebas de aceptación:**

1. Dado un retiro individual impago, cuando se registra, entonces genera deuda con valor base histórico.
2. Dada custodia de stock compartido, cuando se registra la entrega, entonces no crea deuda individual.

### HU-CXC-002 — Registrar un abono

**Historia:** Como Tesorera, quiero registrar pagos parciales sobre un saldo identificado, para conocer cuánto queda pendiente.

**Ficha:** requisito `RF-CXC-002`; prioridad preliminar: posición 48 de 60; estimación: pendiente del equipo; dependencias: HU-CXC-001.

**Pruebas de aceptación:**

1. Dado un saldo y un abono válido, cuando se aplica el pago, entonces quedan monto, fecha, forma y responsable y se reduce solo ese saldo.

### HU-CXC-003 — Rendir cuentas de la feria

**Historia:** Como socia encargada de feria, quiero comparar productos, dinero y diferencias, para cerrar mi encargo con cifras explicables.

**Ficha:** requisito `RF-CXC-003`; prioridad preliminar: posición 49 de 60; estimación: pendiente del equipo; dependencias: HU-INV-004, HU-VEN-001, HU-CXC-001.

**Pruebas de aceptación:**

1. Dado un encargo de feria con ventas y devoluciones, cuando se presenta la rendición, entonces se distinguen recibido, vendido, devuelto, sobrante, dinero, base y excedente.
2. Dada una discrepancia, cuando se revisa, entonces el encargo permanece por conciliar y explica lo faltante.

## Sprint 5 — reportes y sitio público

### HU-REP-001 — Consultar reporte de asistencia

**Historia:** Como integrante autorizada de la Directiva, quiero consultar asistencia por periodo, actividad y socia, para conocer participación e inconsistencias.

**Ficha:** requisito `RF-REP-001`; prioridad preliminar: posición 52 de 60; estimación: pendiente del equipo; dependencias: HU-ASI-001, HU-ASI-003.

**Pruebas de aceptación:**

1. Dado un periodo consultado, cuando se obtiene el reporte de asistencia, entonces sus totales coinciden con registros y correcciones autorizadas.

### HU-REP-002 — Consultar reporte de actividades

**Historia:** Como integrante autorizada de la Directiva, quiero consultar actividades y encargos por estado y responsable, para dar seguimiento al trabajo planificado.

**Ficha:** requisito `RF-REP-002`; prioridad preliminar: posición 53 de 60; estimación: pendiente del equipo; dependencias: HU-PLA-001, HU-PLA-003.

**Pruebas de aceptación:**

1. Dado un periodo y filtro válidos, cuando se obtiene el reporte, entonces aparecen las actividades y encargos permitidos con sus estados.

### HU-REP-003 — Consultar reporte productivo

**Historia:** Como integrante autorizada de la Directiva, quiero consultar acopio, secado, lotes y merma, para seguir la producción y sus orígenes.

**Ficha:** requisito `RF-REP-003`; prioridad preliminar: posición 54 de 60; estimación: pendiente del equipo; dependencias: HU-TRA-001, HU-TRA-002, HU-TRA-004, HU-TRA-005.

**Pruebas de aceptación:**

1. Dados movimientos productivos de un periodo, cuando se obtiene el reporte, entonces conserva unidades, orígenes y totales vinculados a sus registros.

### HU-REP-004 — Consultar reporte de inventario

**Historia:** Como integrante autorizada de la Directiva, quiero consultar existencias y movimientos por producto y lote, para explicar la cantidad disponible.

**Ficha:** requisito `RF-REP-004`; prioridad preliminar: posición 55 de 60; estimación: pendiente del equipo; dependencias: HU-INV-002, HU-INV-004.

**Pruebas de aceptación:**

1. Dado un producto y periodo, cuando se obtiene el reporte, entonces la existencia concilia con movimientos y distingue ajustes.

### HU-REP-005 — Consultar reporte de ventas y saldos

**Historia:** Como Tesorera, quiero consultar ventas, pagos y deudas separadas, para identificar pendientes sin mezclar saldos.

**Ficha:** requisito `RF-REP-005`; prioridad preliminar: posición 56 de 60; estimación: pendiente del equipo; dependencias: HU-VEN-001, HU-CXC-001, HU-CXC-002.

**Pruebas de aceptación:**

1. Dado un periodo consultado, cuando se obtiene el reporte comercial, entonces deuda de socias, deuda externa, pagos y ventas aparecen por separado con fórmulas visibles.

### HU-REP-006 — Consultar mi resumen privado

**Historia:** Como socia, quiero consultar mi actividad, productos y valores pendientes, para comprender mi situación organizacional.

**Ficha:** requisito `RF-REP-006`; prioridad preliminar: posición 57 de 60; estimación: pendiente del equipo; dependencias: HU-ASI-004, HU-PLA-004, HU-CXC-001.

**Pruebas de aceptación:**

1. Dada una sesión de socia, cuando consulta su resumen, entonces ve solo sus datos y el excedente bruto no aparece como ganancia neta.

### HU-NOT-001 — Recibir recordatorios internos

**Historia:** Como usuaria interna, quiero recibir avisos sobre actividades y registros pendientes, para atender tareas a tiempo.

**Ficha:** requisito `RF-NOT-001`; prioridad preliminar: posición 58 de 60; estimación: pendiente del equipo; dependencias: HU-PLA-004, HU-ACC-003.

**Pruebas de aceptación:**

1. Dada una actividad o rendición pendiente que me corresponde, cuando se genera un recordatorio interno, entonces identifica el elemento permitido sin requerir correo o mensajería.

### HU-PUB-001 — Conocer información pública aprobada

**Historia:** Como visitante, quiero consultar información pública de Zhud Alelí, para conocer sus actividades y productos.

**Ficha:** requisito `RF-PUB-001`; prioridad preliminar: posición 60 de 60; estimación: pendiente del equipo; dependencias: HU-PUB-002, HT-GEN-002.

**Pruebas de aceptación:**

1. Dado contenido aprobado, cuando una visitante consulta el sitio público, entonces ve solo información autorizada.
2. Dado contenido sin aprobación, cuando se consulta el sitio, entonces esa información permanece oculta.

### HU-PUB-002 — Gestionar contenido público

**Historia:** Como integrante autorizada de la organización, quiero preparar, aprobar, publicar o retirar contenido, para mantener vigente la información visible.

**Ficha:** requisito `RF-PUB-002`; prioridad preliminar: posición 59 de 60; estimación: pendiente del equipo; dependencias: HU-ACC-003, HT-GEN-002.

**Pruebas de aceptación:**

1. Dado contenido preparado, cuando una persona autorizada lo aprueba y publica, entonces se vuelve visible con su estado registrado.
2. Dada una persona sin permiso, cuando intenta publicar, entonces el contenido no cambia de estado.

## Continuidad transversal

### HU-PWA-001 — Abrir tareas habilitadas sin conexión

**Historia:** Como socia con dispositivo preparado, quiero acceder a los flujos esenciales habilitados durante un corte, para continuar una tarea posible sin Internet.

**Ficha:** requisito `RF-PWA-001`; prioridad preliminar: posición 19 de 60; estimación: pendiente del equipo; dependencias: HT-GEN-005.

**Pruebas de aceptación:**

1. Dado un dispositivo previamente preparado, cuando se pierde la red, entonces se mantienen disponibles los recursos y acciones habilitados.
2. Dado un dispositivo sin preparación inicial, cuando no hay red, entonces se informa la limitación sin mostrar datos privados guardados indebidamente.

### HU-PWA-002 — Conservar registros pendientes sin conexión

**Historia:** Como socia autorizada, quiero guardar localmente asistencia y pesajes habilitados, para no perder datos mientras vuelve Internet.

**Ficha:** requisito `RF-PWA-002`; prioridad preliminar: posición 20 de 60; estimación: pendiente del equipo; dependencias: HU-PWA-001, HT-GEN-005.

**Pruebas de aceptación:**

1. Dada una operación sin conexión habilitada, cuando se guarda localmente, entonces persiste como pendiente al recargar y conserva su origen.
2. Dada otra cuenta en el mismo dispositivo, cuando intenta acceder a la cola ajena, entonces no ve sus datos.

### HU-PWA-003 — Sincronizar registros pendientes

**Historia:** Como socia autorizada, quiero enviar mis operaciones pendientes al volver la red, para conocer cuáles fueron aceptadas sin duplicados.

**Ficha:** requisito `RF-PWA-003`; prioridad preliminar: posición 21 de 60; estimación: pendiente del equipo; dependencias: HU-PWA-002, HT-GEN-006.

**Pruebas de aceptación:**

1. Dada una operación pendiente, cuando vuelve la red, entonces el servidor revalida sesión, permiso y reglas antes de aceptarla.
2. Dada una respuesta perdida, cuando se reintenta la misma operación, entonces se obtiene un solo registro y el conflicto se informa sin cambios parciales.

## Límites de esta edición

- `RF-COS-001` y `RNF-OPS-001` permanecen propuestos, fuera de estas 51 historias confirmadas.
- Las reglas no resueltas de P-02 a P-14 se precisan en las especificaciones correspondientes antes de implementar las partes afectadas.
- El orden preliminar de la pila y la estimación pendiente no sustituyen la planificación y aprobación de cada sprint.
- Las historias locales de SPEC-001 conservan su numeración propia; esta edición resume la línea base completa sin reemplazar esa especificación.

## Historial de esta edición candidata

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 2.0 | 2026-10-12 | Codex | Redacción individual de los 51 requisitos en formato de cátedra, con pruebas, dependencias, prioridad preliminar y estimación pendiente. | Candidato interno |
