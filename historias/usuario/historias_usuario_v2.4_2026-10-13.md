---
titulo: Historias de usuario de Zhud Alelí
version: "2.4"
fecha: 2026-10-13
autor: Tesista
estado: final-documental-con-prioridad-propuesta
fuente_requisitos: CAT-REQ-001 v1.1
fuente_prioridad: priorizacion_requisitos_v1.2_2026-10-13.md
historias: 51
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Historias de usuario

Esta edición presenta primero una **tabla breve por bloque** y después los criterios de cada historia. La importancia propuesta deriva del requisito funcional de origen: **Esencial**, **Alta** o **Complementaria**. El número de la pila es una **posición de trabajo**, no una medida de importancia. Dentro de cada tabla se muestran primero las historias esenciales y luego las altas y complementarias; la ejecución respeta también dependencias y capacidad real.

| Importancia | Sentido para esta edición |
|---|---|
| Esencial | Sin la capacidad, un recorrido central falla o hay un riesgo grave de acceso o integridad. |
| Alta | Necesaria para completar los procesos acordados de la primera versión. |
| Complementaria | Mejora consulta, comunicación o presentación dentro del alcance aprobado. |

La clasificación sigue siendo una **propuesta analítica**: no cambia los 51 RF, no acredita validación académica y no declara trabajo implementado. Estimaciones y responsables siguen pendientes. S1 cubre requisitos y diseño; estas historias se agrupan en S2–S6 y continuidad transversal.

## Sprint 2 — acceso y administración

| Importancia | Historia | Necesidad resumida | Orden en pila |
|---|---|---|---:|
| **Esencial** | `HU-ACC-001` · Entrar y salir de la parte privada | Iniciar y cerrar sesión | 6/60 |
| **Esencial** | `HU-ACC-003` · Usar funciones según responsabilidades | Realizar solo operaciones permitidas por mi perfil, cargo o encargo | 8/60 |
| **Alta** | `HU-ACC-002` · Administrar membresías | Activar o desactivar cuentas de socias | 7/60 |
| **Complementaria** | `HU-ACC-004` · Ver mis opciones disponibles | Consultar mis actividades, pendientes y encargos disponibles | 15/60 |

### Criterios y dependencias

#### HU-ACC-001 — Entrar y salir de la parte privada

**Origen:** `RF-ACC-001` · **Importancia:** Esencial · **Pila:** 6/60 · **Estimación:** pendiente del equipo.

Como usuaria interna con cuenta activa, quiero iniciar y cerrar sesión, para proteger mi información organizacional.

**Aceptación:**

1. Dada una cuenta activa, cuando ingresa con credenciales correctas, entonces accede solo a información autorizada.
2. Dada una cuenta inactiva o credenciales incorrectas, cuando intenta entrar, entonces no obtiene acceso ni información privada.
3. Dada una sesión activa, cuando la usuaria la cierra, entonces deja de poder acceder a información privada con esa sesión.

**Dependencias:** HT-GEN-001, HT-GEN-002.

#### HU-ACC-003 — Usar funciones según responsabilidades

**Origen:** `RF-ACC-003` · **Importancia:** Esencial · **Pila:** 8/60 · **Estimación:** pendiente del equipo.

Como usuaria interna, quiero realizar solo operaciones permitidas por mi perfil, cargo o encargo, para respetar las responsabilidades de la organización.

**Aceptación:**

1. Dado un encargo vencido o un cargo sin autorización, cuando la usuaria intenta una operación restringida, entonces esta se rechaza sin cambiar datos.

**Dependencias:** HU-ACC-001, HT-GEN-002.

#### HU-ACC-002 — Administrar membresías

**Origen:** `RF-ACC-002` · **Importancia:** Alta · **Pila:** 7/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero activar o desactivar cuentas de socias, para mantener vigentes los accesos sin perder la historia.

**Aceptación:**

1. Dada una cuenta de socia, cuando la Directiva la desactiva, entonces cesan los nuevos accesos y se conservan sus registros.
2. Dada una socia sin permiso, cuando intenta cambiar una membresía, entonces el sistema rechaza el cambio.

**Dependencias:** HU-ACC-001, HT-GEN-002.

#### HU-ACC-004 — Ver mis opciones disponibles

**Origen:** `RF-ACC-004` · **Importancia:** Complementaria · **Pila:** 15/60 · **Estimación:** pendiente del equipo.

Como usuaria interna, quiero consultar mis actividades, pendientes y encargos disponibles, para saber qué puedo hacer ahora.

**Aceptación:**

1. Dada una sesión válida, cuando la usuaria consulta su inicio privado, entonces encuentra únicamente actividades y acciones que le corresponden.

**Dependencias:** HU-ACC-001, HU-ACC-003.

## Sprint 3 — planificación

| Importancia | Historia | Necesidad resumida | Orden en pila |
|---|---|---|---:|
| **Alta** | `HU-PLA-001` · Programar una actividad | Registrar jornadas y eventos | 9/60 |
| **Alta** | `HU-PLA-002` · Asignar participantes y responsables | Asignar personas a una actividad | 10/60 |
| **Alta** | `HU-PLA-003` · Crear un encargo temporal | Asignar una responsabilidad de producción o feria por un periodo | 11/60 |
| **Alta** | `HU-PLA-005` · Planificar producción semanal | Definir productos, objetivos, insumos y responsables de la semana | 14/60 |
| **Complementaria** | `HU-PLA-004` · Consultar mis actividades | Consultar actividades y pendientes que me corresponden | 12/60 |

### Criterios y dependencias

#### HU-PLA-001 — Programar una actividad

**Origen:** `RF-PLA-001` · **Importancia:** Alta · **Pila:** 9/60 · **Estimación:** pendiente del equipo.

Como integrante de la Directiva, quiero registrar jornadas y eventos, para coordinar el trabajo de la organización.

**Aceptación:**

1. Dados fecha, hora, lugar y responsable válidos, cuando la Directiva registra una actividad, entonces esta queda asociada a sus participantes y estado.

**Dependencias:** HU-ACC-003.

#### HU-PLA-002 — Asignar participantes y responsables

**Origen:** `RF-PLA-002` · **Importancia:** Alta · **Pila:** 10/60 · **Estimación:** pendiente del equipo.

Como integrante de la Directiva, quiero asignar personas a una actividad, para clarificar quién participa y quién responde por ella.

**Aceptación:**

1. Dada una actividad existente, cuando se asigna una cuenta activa dentro del alcance autorizado, entonces la persona queda vinculada a esa actividad.
2. Dada una cuenta inactiva, cuando se intenta asignarla, entonces la asignación se rechaza.

**Dependencias:** HU-PLA-001, HU-ACC-003.

#### HU-PLA-003 — Crear un encargo temporal

**Origen:** `RF-PLA-003` · **Importancia:** Alta · **Pila:** 11/60 · **Estimación:** pendiente del equipo.

Como integrante de la Directiva, quiero asignar una responsabilidad de producción o feria por un periodo, para delegar tareas con límites claros.

**Aceptación:**

1. Dados tipo, actividad, periodo y alcance válidos, cuando se asigna un encargo, entonces solo habilita las operaciones correspondientes mientras esté vigente.

**Dependencias:** HU-PLA-001, HU-PLA-002.

#### HU-PLA-005 — Planificar producción semanal

**Origen:** `RF-PLA-005` · **Importancia:** Alta · **Pila:** 14/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero definir productos, objetivos, insumos y responsables de la semana, para coordinar la producción prevista.

**Aceptación:**

1. Dados producto, cantidad objetivo y responsables válidos, cuando se registra el plan semanal, entonces queda disponible para las asignadas sin crear existencias anticipadas.

**Dependencias:** HU-PLA-001, HU-CAT-001.

#### HU-PLA-004 — Consultar mis actividades

**Origen:** `RF-PLA-004` · **Importancia:** Complementaria · **Pila:** 12/60 · **Estimación:** pendiente del equipo.

Como socia, quiero consultar actividades y pendientes que me corresponden, para organizar mi participación.

**Aceptación:**

1. Dadas actividades asignadas, cuando la socia consulta sus pendientes, entonces ve sus propios registros y no información privada ajena.

**Dependencias:** HU-PLA-001, HU-PLA-002.

## Sprint 4 — asistencia y participación

| Importancia | Historia | Necesidad resumida | Orden en pila |
|---|---|---|---:|
| **Esencial** | `HU-ASI-001` · Registrar entrada y salida | Registrar por separado mi entrada y salida | 22/60 |
| **Esencial** | `HU-ASI-002` · Evitar asistencia duplicada | Conservar un solo evento de cada tipo por actividad | 23/60 |
| **Esencial** | `HU-ASI-003` · Corregir asistencia con historial | Corregir un registro sensible con motivo | 24/60 |
| **Alta** | `HU-ASI-006` · Resolver una inconsistencia de asistencia | Registrar el acuerdo de la asamblea sobre una inconsistencia | 27/60 |
| **Alta** | `HU-ASI-007` · Registrar asistencia con QR o alternativa | Usar un QR temporal o código alternativo para mi asistencia | 28/60 |
| **Complementaria** | `HU-ASI-004` · Consultar historial de asistencia | Consultar mi asistencia por periodo | 25/60 |
| **Complementaria** | `HU-ASI-005` · Registrar participación adicional | Registrar una participación distinta de la asistencia cuando se necesite | 26/60 |

### Criterios y dependencias

#### HU-ASI-001 — Registrar entrada y salida

**Origen:** `RF-ASI-001` · **Importancia:** Esencial · **Pila:** 22/60 · **Estimación:** pendiente del equipo.

Como socia, quiero registrar por separado mi entrada y salida, para contar con asistencia verificable.

**Aceptación:**

1. Dada una actividad habilitada, cuando se registra una entrada o salida en línea, entonces queda el tipo de evento, la hora del servidor y su origen.
2. Dada una captura sin red habilitada, cuando se conserva localmente, entonces queda provisional y diferencia hora declarada de recepción.

**Dependencias:** HU-PLA-001, HU-ACC-003; HU-PWA-002 solo para captura sin red.

#### HU-ASI-002 — Evitar asistencia duplicada

**Origen:** `RF-ASI-002` · **Importancia:** Esencial · **Pila:** 23/60 · **Estimación:** pendiente del equipo.

Como socia, quiero conservar un solo evento de cada tipo por actividad, para evitar registros contradictorios.

**Aceptación:**

1. Dado un evento de asistencia ya registrado, cuando se intenta repetirlo para la misma socia y actividad, entonces no se crea otro y se informa el registro existente.

**Dependencias:** HU-ASI-001.

#### HU-ASI-003 — Corregir asistencia con historial

**Origen:** `RF-ASI-003` · **Importancia:** Esencial · **Pila:** 24/60 · **Estimación:** pendiente del equipo.

Como integrante de la Directiva o encargada autorizada, quiero corregir un registro sensible con motivo, para resolver errores sin borrar la historia.

**Aceptación:**

1. Dado un registro de asistencia y autorización vigente, cuando se corrige con motivo, entonces se conservan actor, fecha, valor anterior y nuevo valor.
2. Dada una persona sin permiso, cuando intenta corregir, entonces no cambia el registro.

**Dependencias:** HU-ASI-001, HT-GEN-003.

#### HU-ASI-006 — Resolver una inconsistencia de asistencia

**Origen:** `RF-ASI-006` · **Importancia:** Alta · **Pila:** 27/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero registrar el acuerdo de la asamblea sobre una inconsistencia, para conservar una decisión justa y rastreable.

**Aceptación:**

1. Dada una inconsistencia pendiente, cuando se registra una decisión de la asamblea, entonces quedan acuerdo, actor, fecha y motivo sin sanción automática.

**Dependencias:** HU-ASI-001, HU-ASI-003.

#### HU-ASI-007 — Registrar asistencia con QR o alternativa

**Origen:** `RF-ASI-007` · **Importancia:** Alta · **Pila:** 28/60 · **Estimación:** pendiente del equipo.

Como socia, quiero usar un QR temporal o código alternativo para mi asistencia, para registrarla por un medio disponible y auditable.

**Aceptación:**

1. Dado un QR válido para la fase habilitada, cuando la socia registra su evento, entonces queda identificado como autorregistro.
2. Dado un token vencido, repetido o para otra acción, cuando se intenta registrar asistencia, entonces no se modifica el evento.
3. Dado un registro delegado autorizado, cuando se confirma, entonces quedan identificadas la socia, la persona delegada y el motivo.

**Dependencias:** HU-ASI-001, HU-ACC-003.

#### HU-ASI-004 — Consultar historial de asistencia

**Origen:** `RF-ASI-004` · **Importancia:** Complementaria · **Pila:** 25/60 · **Estimación:** pendiente del equipo.

Como socia, quiero consultar mi asistencia por periodo, para conocer mis registros y sus estados.

**Aceptación:**

1. Dado un periodo consultado, cuando la socia solicita su historial, entonces ve sus eventos y estados sin acceso a los de otra socia.

**Dependencias:** HU-ASI-001, HT-GEN-002.

#### HU-ASI-005 — Registrar participación adicional

**Origen:** `RF-ASI-005` · **Importancia:** Complementaria · **Pila:** 26/60 · **Estimación:** pendiente del equipo.

Como responsable autorizada de una actividad, quiero registrar una participación distinta de la asistencia cuando se necesite, para reflejar el aporte real de las socias.

**Aceptación:**

1. Dada una actividad que exige participación adicional, cuando se registra ese dato, entonces queda vinculado a la socia y actividad.
2. Dada una actividad simple, cuando se confirma la asistencia, entonces no se exige participación adicional.

**Dependencias:** HU-PLA-001, HU-ASI-001.

## Sprint 5 — producción, inventario y rendición

| Importancia | Historia | Necesidad resumida | Orden en pila |
|---|---|---|---:|
| **Esencial** | `HU-CAT-001` · Mantener catálogo productivo | Distinguir materias primas, insumos, productos y unidades | 13/60 |
| **Esencial** | `HU-INV-001` · Conservar valores comerciales históricos | Mantener precios y valor base con vigencia | 29/60 |
| **Esencial** | `HU-TRA-001` · Registrar acopio de materia | Registrar materia recibida, cantidad y origen | 30/60 |
| **Esencial** | `HU-TRA-002` · Registrar secado | Registrar pesos, temperatura e inicio y fin del secado | 31/60 |
| **Esencial** | `HU-TRA-004` · Seguir la procedencia de lotes | Relacionar un lote con sus orígenes y derivados | 33/60 |
| **Esencial** | `HU-TRA-005` · Registrar transformación | Registrar insumos consumidos y producto resultante | 34/60 |
| **Esencial** | `HU-INV-002` · Reconstruir existencias | Consultar existencias derivadas de movimientos | 35/60 |
| **Esencial** | `HU-VEN-001` · Registrar una venta | Registrar varios productos y su forma de pago | 38/60 |
| **Esencial** | `HU-VEN-003` · Conocer valor base y excedente | Conocer valor base, precio aplicado y excedente bruto de la venta | 40/60 |
| **Esencial** | `HU-VEN-004` · Autorizar venta bajo valor base | Decidir una excepción de precio bajo el valor base | 41/60 |
| **Esencial** | `HU-CXC-001` · Distinguir deudas y custodia | Distinguir deuda de socia, cuenta por cobrar externa y custodia física | 47/60 |
| **Esencial** | `HU-CXC-002` · Registrar un abono | Registrar pagos parciales sobre un saldo identificado | 48/60 |
| **Alta** | `HU-TRA-003` · Conocer duración y merma | Conocer la duración y pérdida de peso de un secado | 32/60 |
| **Alta** | `HU-INV-003` · Entregar productos para feria | Recibir productos identificados por lote y modalidad | 36/60 |
| **Alta** | `HU-INV-004` · Conciliar productos de feria | Comparar productos recibidos, vendidos y devueltos | 37/60 |
| **Alta** | `HU-VEN-002` · Identificar comprador según la venta | Registrar los datos de comprador necesarios | 39/60 |
| **Alta** | `HU-VEN-006` · Distinguir stock individual y compartido | Identificar el origen de cada línea vendida | 43/60 |
| **Alta** | `HU-VEN-007` · Registrar venta institucional | Registrar una venta desde stock general | 44/60 |
| **Alta** | `HU-VEN-008` · Conciliar comprobante manual de feria | Incorporar una venta respaldada por comprobante de contingencia | 45/60 |
| **Alta** | `HU-GAS-001` · Registrar gasto operativo | Registrar un gasto con categoría, monto y periodo | 46/60 |
| **Alta** | `HU-CXC-003` · Rendir cuentas de la feria | Comparar productos, dinero y diferencias | 49/60 |
| **Complementaria** | `HU-VEN-005` · Configurar descuento por volumen | Definir descuentos con umbral, valor y vigencia | 42/60 |
| **Complementaria** | `HU-GAS-002` · Consultar resumen económico | Consultar ingresos, gastos y pendientes | 50/60 |

### Criterios y dependencias

#### HU-CAT-001 — Mantener catálogo productivo

**Origen:** `RF-CAT-001` · **Importancia:** Esencial · **Pila:** 13/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero distinguir materias primas, insumos, productos y unidades, para usar datos coherentes en producción y venta.

**Aceptación:**

1. Dado un elemento de catálogo activo, cuando se usa en una operación permitida, entonces conserva su tipo y unidad.
2. Dado un elemento desactivado, cuando se intenta usarlo en una operación nueva, entonces se rechaza sin borrar su historia.

**Dependencias:** HU-ACC-003.

#### HU-INV-001 — Conservar valores comerciales históricos

**Origen:** `RF-INV-001` · **Importancia:** Esencial · **Pila:** 29/60 · **Estimación:** pendiente del equipo.

Como Tesorera autorizada, quiero mantener precios y valor base con vigencia, para explicar cada venta según los valores de su momento.

**Aceptación:**

1. Dado un cambio de valor comercial, cuando se aplica a operaciones nuevas, entonces una venta anterior conserva el valor histórico utilizado.

**Dependencias:** HU-CAT-001, HU-ACC-003.

#### HU-TRA-001 — Registrar acopio de materia

**Origen:** `RF-TRA-001` · **Importancia:** Esencial · **Pila:** 30/60 · **Estimación:** pendiente del equipo.

Como socia encargada de producción, quiero registrar materia recibida, cantidad y origen, para conocer quién entregó cada insumo.

**Aceptación:**

1. Dados origen, unidad, responsable y peso positivo, cuando se registra acopio, entonces queda trazable la entrega.
2. Dado un peso no positivo, cuando se intenta registrar, entonces la operación se rechaza.

**Dependencias:** HU-CAT-001, HU-PLA-003.

#### HU-TRA-002 — Registrar secado

**Origen:** `RF-TRA-002` · **Importancia:** Esencial · **Pila:** 31/60 · **Estimación:** pendiente del equipo.

Como socia encargada de producción, quiero registrar pesos, temperatura e inicio y fin del secado, para seguir cada proceso productivo.

**Aceptación:**

1. Dados peso inicial y temperatura válidos, cuando se inicia el secado, entonces se conservan sus datos y el momento correspondiente.
2. Dados peso final y cierre válidos, cuando termina el secado, entonces queda el cierre sin exigir humedad opcional.

**Dependencias:** HU-TRA-001, HU-PLA-003.

#### HU-TRA-004 — Seguir la procedencia de lotes

**Origen:** `RF-TRA-004` · **Importancia:** Esencial · **Pila:** 33/60 · **Estimación:** pendiente del equipo.

Como responsable de producción, quiero relacionar un lote con sus orígenes y derivados, para reconstruir la procedencia de un producto.

**Aceptación:**

1. Dada una mezcla física permitida, cuando se crea un lote derivado, entonces sus lotes de origen permanecen identificables.
2. Dado un lote cerrado, cuando aún tiene existencias, entonces no se confunde cierre productivo con stock agotado.

**Dependencias:** HU-TRA-001, HU-TRA-002.

#### HU-TRA-005 — Registrar transformación

**Origen:** `RF-TRA-005` · **Importancia:** Esencial · **Pila:** 34/60 · **Estimación:** pendiente del equipo.

Como socia encargada de producción, quiero registrar insumos consumidos y producto resultante, para conservar la composición y cantidad de cada lote.

**Aceptación:**

1. Dados insumos y composición válidos, cuando se confirma la transformación, entonces el producto resultante queda vinculado a consumos, versión y lote.

**Dependencias:** HU-TRA-004, HU-CAT-001.

#### HU-INV-002 — Reconstruir existencias

**Origen:** `RF-INV-002` · **Importancia:** Esencial · **Pila:** 35/60 · **Estimación:** pendiente del equipo.

Como responsable de inventario, quiero consultar existencias derivadas de movimientos, para evitar saldos sin respaldo.

**Aceptación:**

1. Dadas entradas, consumos, ventas y devoluciones confirmadas, cuando se calcula la existencia, entonces coincide con sus movimientos.
2. Dado un ajuste autorizado, cuando se confirma con motivo, entonces el cambio queda registrado íntegramente.

**Dependencias:** HU-CAT-001, HT-GEN-003.

#### HU-VEN-001 — Registrar una venta

**Origen:** `RF-VEN-001` · **Importancia:** Esencial · **Pila:** 38/60 · **Estimación:** pendiente del equipo.

Como socia encargada de feria, quiero registrar varios productos y su forma de pago, para conocer el total sin vender más de lo disponible.

**Aceptación:**

1. Dado stock autorizado suficiente, cuando se confirma una venta de varios productos, entonces se registra completa con total calculado.
2. Dado stock insuficiente, cuando se intenta confirmar, entonces no se registra ninguna parte de la venta.

**Dependencias:** HU-INV-002, HU-INV-003, HT-GEN-003.

#### HU-VEN-003 — Conocer valor base y excedente

**Origen:** `RF-VEN-003` · **Importancia:** Esencial · **Pila:** 40/60 · **Estimación:** pendiente del equipo.

Como socia encargada de venta, quiero conocer valor base, precio aplicado y excedente bruto de la venta, para rendir cuentas sin confundir excedente con utilidad neta.

**Aceptación:**

1. Dada una venta confirmada, cuando se consulta su resultado, entonces conserva valor base y precio aplicado históricos y calcula excedente bruto.

**Dependencias:** HU-VEN-001, HU-INV-001.

#### HU-VEN-004 — Autorizar venta bajo valor base

**Origen:** `RF-VEN-004` · **Importancia:** Esencial · **Pila:** 41/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero decidir una excepción de precio bajo el valor base, para proteger y explicar el resultado comercial.

**Aceptación:**

1. Dada una venta bajo valor base sin autorización, cuando se intenta confirmar, entonces se rechaza.
2. Dada una excepción autorizada con motivo, cuando se confirma, entonces quedan responsable, diferencia y razón registrados.

**Dependencias:** HU-VEN-001, HU-VEN-003.

#### HU-CXC-001 — Distinguir deudas y custodia

**Origen:** `RF-CXC-001` · **Importancia:** Esencial · **Pila:** 47/60 · **Estimación:** pendiente del equipo.

Como Tesorera, quiero distinguir deuda de socia, cuenta por cobrar externa y custodia física, para evitar cargos monetarios incorrectos.

**Aceptación:**

1. Dado un retiro individual impago, cuando se registra, entonces genera deuda con valor base histórico.
2. Dada custodia de stock compartido, cuando se registra la entrega, entonces no crea deuda individual.

**Dependencias:** HU-INV-003, HU-VEN-001, HU-INV-001.

#### HU-CXC-002 — Registrar un abono

**Origen:** `RF-CXC-002` · **Importancia:** Esencial · **Pila:** 48/60 · **Estimación:** pendiente del equipo.

Como Tesorera, quiero registrar pagos parciales sobre un saldo identificado, para conocer cuánto queda pendiente.

**Aceptación:**

1. Dado un saldo y un abono válido, cuando se aplica el pago, entonces quedan monto, fecha, forma y responsable y se reduce solo ese saldo.

**Dependencias:** HU-CXC-001.

#### HU-TRA-003 — Conocer duración y merma

**Origen:** `RF-TRA-003` · **Importancia:** Alta · **Pila:** 32/60 · **Estimación:** pendiente del equipo.

Como responsable de producción, quiero conocer la duración y pérdida de peso de un secado, para evaluar el resultado del proceso.

**Aceptación:**

1. Dado un secado con inicio, fin y pesos válidos, cuando se consulta su resultado, entonces se muestran duración y merma absoluta con unidad y fórmula.
2. Dado un peso final mayor que el inicial, cuando se calcula el resultado, entonces queda pendiente de revisión o excepción autorizada.

**Dependencias:** HU-TRA-002.

#### HU-INV-003 — Entregar productos para feria

**Origen:** `RF-INV-003` · **Importancia:** Alta · **Pila:** 36/60 · **Estimación:** pendiente del equipo.

Como socia encargada de feria, quiero recibir productos identificados por lote y modalidad, para rendir cuentas de lo que quedó bajo mi custodia.

**Aceptación:**

1. Dado stock suficiente y un encargo vigente, cuando se confirma una entrega, entonces quedan producto, lote, cantidad, socia y origen individual o compartido.
2. Dada cantidad superior al stock, cuando se intenta entregar, entonces se rechaza.

**Dependencias:** HU-INV-002, HU-PLA-003.

#### HU-INV-004 — Conciliar productos de feria

**Origen:** `RF-INV-004` · **Importancia:** Alta · **Pila:** 37/60 · **Estimación:** pendiente del equipo.

Como socia encargada de feria, quiero comparar productos recibidos, vendidos y devueltos, para explicar diferencias físicas.

**Aceptación:**

1. Dado un encargo con movimientos, cuando se realiza la conciliación, entonces se distinguen recibidos, transferidos, vendidos, devueltos y sobrantes.
2. Dada una diferencia, cuando se cierra el recuento, entonces permanece visible sin generar stock negativo silencioso.

**Dependencias:** HU-INV-003, HU-INV-002.

#### HU-VEN-002 — Identificar comprador según la venta

**Origen:** `RF-VEN-002` · **Importancia:** Alta · **Pila:** 39/60 · **Estimación:** pendiente del equipo.

Como socia encargada de venta, quiero registrar los datos de comprador necesarios, para conservar un cobro rastreable sin pedir datos de más.

**Aceptación:**

1. Dada una venta a crédito o institucional, cuando se intenta confirmar sin comprador identificado, entonces se rechaza.
2. Dada una venta al contado ordinaria, cuando se registra, entonces puede usar Público general sin pedir datos personales innecesarios.

**Dependencias:** HU-VEN-001.

#### HU-VEN-006 — Distinguir stock individual y compartido

**Origen:** `RF-VEN-006` · **Importancia:** Alta · **Pila:** 43/60 · **Estimación:** pendiente del equipo.

Como socia encargada de feria, quiero identificar el origen de cada línea vendida, para separar resultados individuales y compartidos.

**Aceptación:**

1. Dada una venta de feria, cuando se confirma una línea, entonces conserva si el producto procede de stock individual o compartido.
2. Dado excedente de stock compartido, cuando se presenta el resultado, entonces no se reparte automáticamente.

**Dependencias:** HU-INV-003, HU-VEN-001.

#### HU-VEN-007 — Registrar venta institucional

**Origen:** `RF-VEN-007` · **Importancia:** Alta · **Pila:** 44/60 · **Estimación:** pendiente del equipo.

Como Tesorera, quiero registrar una venta desde stock general, para rendir cuentas sin atribuir excedente a una socia.

**Aceptación:**

1. Dado stock general y una compradora institucional identificada, cuando se confirma la venta, entonces quedan su tipo y responsable sin asignar excedente individual.

**Dependencias:** HU-VEN-001, HU-VEN-002.

#### HU-VEN-008 — Conciliar comprobante manual de feria

**Origen:** `RF-VEN-008` · **Importancia:** Alta · **Pila:** 45/60 · **Estimación:** pendiente del equipo.

Como socia encargada de feria, quiero incorporar una venta respaldada por comprobante de contingencia, para evitar pérdidas y duplicados durante fallos.

**Aceptación:**

1. Dado un comprobante manual con folio único, cuando se incorpora después de la contingencia, entonces se conserva su origen y momento declarado.
2. Dado un folio ya registrado, cuando se intenta incorporarlo de nuevo, entonces no descuenta stock dos veces.

**Dependencias:** HU-VEN-001, HU-INV-004.

#### HU-GAS-001 — Registrar gasto operativo

**Origen:** `RF-GAS-001` · **Importancia:** Alta · **Pila:** 46/60 · **Estimación:** pendiente del equipo.

Como Tesorera, quiero registrar un gasto con categoría, monto y periodo, para conocer los egresos vinculados al trabajo.

**Aceptación:**

1. Dado monto positivo y datos válidos, cuando se confirma un gasto, entonces quedan concepto, periodo o lote, responsable y fecha.
2. Dado monto inválido, cuando se intenta registrar, entonces se rechaza.

**Dependencias:** HU-ACC-003.

#### HU-CXC-003 — Rendir cuentas de la feria

**Origen:** `RF-CXC-003` · **Importancia:** Alta · **Pila:** 49/60 · **Estimación:** pendiente del equipo.

Como socia encargada de feria, quiero comparar productos, dinero y diferencias, para cerrar mi encargo con cifras explicables.

**Aceptación:**

1. Dado un encargo de feria con ventas y devoluciones, cuando se presenta la rendición, entonces se distinguen recibido, vendido, devuelto, sobrante, dinero, base y excedente.
2. Dada una discrepancia, cuando se revisa, entonces el encargo permanece por conciliar y explica lo faltante.

**Dependencias:** HU-INV-004, HU-VEN-001, HU-CXC-001.

#### HU-VEN-005 — Configurar descuento por volumen

**Origen:** `RF-VEN-005` · **Importancia:** Complementaria · **Pila:** 42/60 · **Estimación:** pendiente del equipo.

Como Tesorera, quiero definir descuentos con umbral, valor y vigencia, para aplicar reglas comerciales aprobadas de forma consistente.

**Aceptación:**

1. Dada una política con datos incompletos, cuando una venta cumple la cantidad indicada, entonces no se aplica descuento.
2. Dada una política completa y vigente, cuando se cumplen sus condiciones, entonces se aplica el valor configurado respetando excepciones bajo base.

**Dependencias:** HU-CAT-001, HU-INV-001, HU-VEN-001.

#### HU-GAS-002 — Consultar resumen económico

**Origen:** `RF-GAS-002` · **Importancia:** Complementaria · **Pila:** 50/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero consultar ingresos, gastos y pendientes, para comprender los resultados del periodo.

**Aceptación:**

1. Dado un periodo con operaciones, cuando se consulta el resumen, entonces cada total indica su fuente y fórmula sin presentarse como balance certificado.

**Dependencias:** HU-GAS-001, HU-VEN-001, HU-CXC-001.

## Sprint 6 — reportes y sitio público

| Importancia | Historia | Necesidad resumida | Orden en pila |
|---|---|---|---:|
| **Alta** | `HU-REP-001` · Consultar reporte de asistencia | Consultar asistencia por periodo, actividad y socia | 52/60 |
| **Alta** | `HU-REP-002` · Consultar reporte de actividades | Consultar actividades y encargos por estado y responsable | 53/60 |
| **Alta** | `HU-REP-003` · Consultar reporte productivo | Consultar acopio, secado, lotes y merma | 54/60 |
| **Alta** | `HU-REP-004` · Consultar reporte de inventario | Consultar existencias y movimientos por producto y lote | 55/60 |
| **Alta** | `HU-REP-005` · Consultar reporte de ventas y saldos | Consultar ventas, pagos y deudas separadas | 56/60 |
| **Complementaria** | `HU-REP-006` · Consultar mi resumen privado | Consultar mi actividad, productos y valores pendientes | 57/60 |
| **Complementaria** | `HU-NOT-001` · Recibir recordatorios internos | Recibir avisos sobre actividades y registros pendientes | 58/60 |
| **Complementaria** | `HU-PUB-002` · Gestionar contenido público | Preparar, aprobar, publicar o retirar contenido | 59/60 |
| **Complementaria** | `HU-PUB-001` · Conocer información pública aprobada | Consultar información pública de Zhud Alelí | 60/60 |

### Criterios y dependencias

#### HU-REP-001 — Consultar reporte de asistencia

**Origen:** `RF-REP-001` · **Importancia:** Alta · **Pila:** 52/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero consultar asistencia por periodo, actividad y socia, para conocer participación e inconsistencias.

**Aceptación:**

1. Dado un periodo consultado, cuando se obtiene el reporte de asistencia, entonces sus totales coinciden con registros y correcciones autorizadas.

**Dependencias:** HU-ASI-001, HU-ASI-003.

#### HU-REP-002 — Consultar reporte de actividades

**Origen:** `RF-REP-002` · **Importancia:** Alta · **Pila:** 53/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero consultar actividades y encargos por estado y responsable, para dar seguimiento al trabajo planificado.

**Aceptación:**

1. Dado un periodo y filtro válidos, cuando se obtiene el reporte, entonces aparecen las actividades y encargos permitidos con sus estados.

**Dependencias:** HU-PLA-001, HU-PLA-003.

#### HU-REP-003 — Consultar reporte productivo

**Origen:** `RF-REP-003` · **Importancia:** Alta · **Pila:** 54/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero consultar acopio, secado, lotes y merma, para seguir la producción y sus orígenes.

**Aceptación:**

1. Dados movimientos productivos de un periodo, cuando se obtiene el reporte, entonces conserva unidades, orígenes y totales vinculados a sus registros.

**Dependencias:** HU-TRA-001, HU-TRA-002, HU-TRA-004, HU-TRA-005.

#### HU-REP-004 — Consultar reporte de inventario

**Origen:** `RF-REP-004` · **Importancia:** Alta · **Pila:** 55/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la Directiva, quiero consultar existencias y movimientos por producto y lote, para explicar la cantidad disponible.

**Aceptación:**

1. Dado un producto y periodo, cuando se obtiene el reporte, entonces la existencia concilia con movimientos y distingue ajustes.

**Dependencias:** HU-INV-002, HU-INV-004.

#### HU-REP-005 — Consultar reporte de ventas y saldos

**Origen:** `RF-REP-005` · **Importancia:** Alta · **Pila:** 56/60 · **Estimación:** pendiente del equipo.

Como Tesorera, quiero consultar ventas, pagos y deudas separadas, para identificar pendientes sin mezclar saldos.

**Aceptación:**

1. Dado un periodo consultado, cuando se obtiene el reporte comercial, entonces deuda de socias, deuda externa, pagos y ventas aparecen por separado con fórmulas visibles.

**Dependencias:** HU-VEN-001, HU-CXC-001, HU-CXC-002.

#### HU-REP-006 — Consultar mi resumen privado

**Origen:** `RF-REP-006` · **Importancia:** Complementaria · **Pila:** 57/60 · **Estimación:** pendiente del equipo.

Como socia, quiero consultar mi actividad, productos y valores pendientes, para comprender mi situación organizacional.

**Aceptación:**

1. Dada una sesión de socia, cuando consulta su resumen, entonces ve solo sus datos y el excedente bruto no aparece como ganancia neta.

**Dependencias:** HU-ASI-004, HU-PLA-004, HU-CXC-001.

#### HU-NOT-001 — Recibir recordatorios internos

**Origen:** `RF-NOT-001` · **Importancia:** Complementaria · **Pila:** 58/60 · **Estimación:** pendiente del equipo.

Como usuaria interna, quiero recibir avisos sobre actividades y registros pendientes, para atender tareas a tiempo.

**Aceptación:**

1. Dada una actividad o rendición pendiente que me corresponde, cuando se genera un recordatorio interno, entonces identifica el elemento permitido sin requerir correo o mensajería.

**Dependencias:** HU-PLA-004, HU-ACC-003.

#### HU-PUB-002 — Gestionar contenido público

**Origen:** `RF-PUB-002` · **Importancia:** Complementaria · **Pila:** 59/60 · **Estimación:** pendiente del equipo.

Como integrante autorizada de la organización, quiero preparar, aprobar, publicar o retirar contenido, para mantener vigente la información visible.

**Aceptación:**

1. Dado contenido preparado, cuando una persona autorizada lo aprueba y publica, entonces se vuelve visible con su estado registrado.
2. Dada una persona sin permiso, cuando intenta publicar, entonces el contenido no cambia de estado.

**Dependencias:** HU-ACC-003, HT-GEN-002.

#### HU-PUB-001 — Conocer información pública aprobada

**Origen:** `RF-PUB-001` · **Importancia:** Complementaria · **Pila:** 60/60 · **Estimación:** pendiente del equipo.

Como visitante, quiero consultar información pública de Zhud Alelí, para conocer sus actividades y productos.

**Aceptación:**

1. Dado contenido aprobado, cuando una visitante consulta el sitio público, entonces ve solo información autorizada.
2. Dado contenido sin aprobación, cuando se consulta el sitio, entonces esa información permanece oculta.

**Dependencias:** HU-PUB-002, HT-GEN-002.

## Continuidad transversal

| Importancia | Historia | Necesidad resumida | Orden en pila |
|---|---|---|---:|
| **Esencial** | `HU-PWA-001` · Abrir tareas habilitadas sin conexión | Acceder a los flujos esenciales habilitados durante un corte | 19/60 |
| **Esencial** | `HU-PWA-002` · Conservar registros pendientes sin conexión | Guardar localmente asistencia y pesajes habilitados | 20/60 |
| **Esencial** | `HU-PWA-003` · Sincronizar registros pendientes | Enviar mis operaciones pendientes al volver la red | 21/60 |

### Criterios y dependencias

#### HU-PWA-001 — Abrir tareas habilitadas sin conexión

**Origen:** `RF-PWA-001` · **Importancia:** Esencial · **Pila:** 19/60 · **Estimación:** pendiente del equipo.

Como socia con dispositivo preparado, quiero acceder a los flujos esenciales habilitados durante un corte, para continuar una tarea posible sin Internet.

**Aceptación:**

1. Dado un dispositivo previamente preparado, cuando se pierde la red, entonces se mantienen disponibles los recursos y acciones habilitados.
2. Dado un dispositivo sin preparación inicial, cuando no hay red, entonces se informa la limitación sin mostrar datos privados guardados indebidamente.

**Dependencias:** HT-GEN-005.

#### HU-PWA-002 — Conservar registros pendientes sin conexión

**Origen:** `RF-PWA-002` · **Importancia:** Esencial · **Pila:** 20/60 · **Estimación:** pendiente del equipo.

Como socia autorizada, quiero guardar localmente asistencia y pesajes habilitados, para no perder datos mientras vuelve Internet.

**Aceptación:**

1. Dada una operación sin conexión habilitada, cuando se guarda localmente, entonces persiste como pendiente al recargar y conserva su origen.
2. Dada otra cuenta en el mismo dispositivo, cuando intenta acceder a la cola ajena, entonces no ve sus datos.

**Dependencias:** HU-PWA-001, HT-GEN-005.

#### HU-PWA-003 — Sincronizar registros pendientes

**Origen:** `RF-PWA-003` · **Importancia:** Esencial · **Pila:** 21/60 · **Estimación:** pendiente del equipo.

Como socia autorizada, quiero enviar mis operaciones pendientes al volver la red, para conocer cuáles fueron aceptadas sin duplicados.

**Aceptación:**

1. Dada una operación pendiente, cuando vuelve la red, entonces el servidor revalida sesión, permiso y reglas antes de aceptarla.
2. Dada una respuesta perdida, cuando se reintenta la misma operación, entonces se obtiene un solo registro y el conflicto se informa sin cambios parciales.

**Dependencias:** HU-PWA-002, HT-GEN-006.

## Condiciones de la edición

| Situación | Tratamiento |
|---|---|
| Requisitos propuestos | `RF-COS-001` y `RNF-OPS-001` permanecen fuera de las 51 historias confirmadas. |
| Decisiones abiertas | P-02 a P-14 se resuelven en la especificación afectada antes de implementar el detalle correspondiente. |
| Planificación | El orden es preliminar y las estimaciones se acuerdan con el equipo antes de comprometer trabajo en un sprint. |
| SPEC-001 | Sus historias locales conservan su numeración; este documento resume la línea base completa sin sustituir su especificación. |

## Historias exploratorias de la entrevista

Estas necesidades provienen de EVID-ENT-2026-10-12-001. Son **fichas para descubrir y validar**, fuera de las 51 HU ligadas a RF confirmados. No tienen posición en la pila de 60 ni sprint comprometido.

| Tema | Historia tentativa | Validación necesaria antes de redactar criterios de aceptación definitivos |
|---|---|---|
| Documentos | Como responsable autorizada, quiero organizar documentos de la asociación y producción, para encontrarlos y relacionarlos sin recurrir al papel. | Tipos, permisos, versiones, datos sensibles y firmas. |
| Vencimientos | Como responsable, quiero conocer los documentos próximos a vencer, para tramitar renovaciones a tiempo. | Fecha válida, anticipación por tipo y destinatarios. |
| Agenda | Como socia convocada, quiero recibir el lugar y la fecha de una reunión o taller, para organizar mi asistencia. | Aviso interno existente frente a nuevos avisos por WhatsApp. |
| Secado delegado | Como socia encargada, quiero confirmar que terminé el secado y adjuntar evidencia cuando corresponda, para que la Directiva conozca el resultado. | Quién delega, valida, reencarga y conserva evidencia. |
| Inventario | Como responsable de stock, quiero distinguir existencias personales y generales por lote, para conciliar lo que cada socia tiene. | Propiedad, transferencias, devoluciones y fecha de corte. |
| Materia prima | Como encargada de producción, quiero ver insumos próximos al mínimo, para planificar el abastecimiento. | Umbral por planta/producto y fuente de existencias. |
| Venta mensual | Como socia, quiero registrar mis ventas del mes, para rendir el valor que corresponde a la asociación y conocer mi comisión. | Fórmula, período, permisos y tratamiento de devoluciones. |
| Sitio público | Como visitante, quiero consultar precios aprobados y contactar por WhatsApp, para preguntar por un producto. | Aprobación de precios y si el contacto equivale a pedido. |
| Asistencia | Como encargada, quiero revisar faltas, atrasos y justificativos, para presentar la situación a quien deba decidir. | La entrevista comunica USD 0,01/min de atraso, USD 10 desde la primera falta y aviso a la tercera falta; faltan autoridad, justificativos, procedimiento y cierre de P-03. No se presupone multa automática. |

No se fijan estimaciones ni se cambian los criterios de las 51 historias confirmadas.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 2.2 | 2026-10-12 | Se presentan 51 historias en tablas y nueve temas exploratorios de la entrevista. | Edición documental; revisión académica pendiente |
| 2.3 | 2026-10-13 | Se renumeran los bloques funcionales de S1–S5 a S2–S6 sin cambiar las 51 historias. | Preparado; revisión académica pendiente |
| 2.4 | 2026-10-13 | Se separa importancia de posición en pila; se ordenan tablas por importancia y se conservan criterios, RF y dependencias. | Preparado; revisión académica pendiente |
