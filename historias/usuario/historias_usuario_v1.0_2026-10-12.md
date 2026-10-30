---
titulo: Historias de usuario de Zhud Alelí
version: "1.0"
fecha: 2026-10-12
autor: Tesista
estado: final-aprobado-por-tesista
fuente_principal: "CAT-REQ-001 v1.1"
historias_editoriales: 19
aprobacion_editorial: 2026-10-12
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Historias de usuario

## Cómo leer este documento

Estas historias expresan en lenguaje cotidiano los **51 requisitos funcionales
confirmados** en CAT-REQ-001 v1.1. Los identificadores `HU-GEN` organizan esta
redacción académica: no son requisitos nuevos ni cambian la aprobación del catálogo.
Los criterios de aceptación son una síntesis mínima; las especificaciones de cada
funcionalidad completarán pantallas, permisos, datos y pruebas. Las historias locales
`HU-01` y siguientes de SPEC-001 mantienen su propia numeración y detalle.

Los nueve requisitos no funcionales confirmados también se aplican a las historias
pertinentes, especialmente accesibilidad, seguridad, auditoría, continuidad,
privacidad y claridad de PDF. Una historia describe trabajo previsto, no una función
ya implementada. La revisión académica de la directora y la validación de la
organización de los ajustes v1.1 no constan realizadas.

## Sprint 1 — Acceso y administración

### HU-GEN-001 — Entrar a la parte privada

**Como** usuaria interna con cuenta activa, **quiero** iniciar y cerrar sesión,
**para** usar mi espacio privado de forma segura.

- **Requisito:** `RF-ACC-001`.
- **Aceptación mínima:** una cuenta activa con datos correctos entra; los intentos
  inválidos o una cuenta inactiva no muestran información privada. Al salir, la
  sesión deja de dar acceso.
- **Detalle existente:** SPEC-001 cubre solo esta primera porción de acceso.

### HU-GEN-002 — Administrar cuentas y ver opciones propias

**Como** integrante autorizada de la Directiva, **quiero** gestionar membresías y
permisos; **como** usuaria interna, **quiero** ver solo las opciones que me corresponden.

- **Requisitos:** `RF-ACC-002`, `RF-ACC-003`, `RF-ACC-004`.
- **Aceptación mínima:** desactivar una cuenta impide nuevos accesos sin borrar
  su historia; una operación fuera del cargo o encargo se rechaza; el inicio
  privado muestra únicamente acciones disponibles.
- **Decisión:** P-01 se cerró para acceso básico; cada funcionalidad futura precisa
  sus permisos particulares.

## Sprint 2 — Planificación

### HU-GEN-003 — Organizar actividades y encargos

**Como** integrante de la Directiva, **quiero** programar actividades y asignar
responsables; **como** socia, **quiero** consultar mis pendientes y encargos.

- **Requisitos:** `RF-PLA-001`, `RF-PLA-002`, `RF-PLA-003`, `RF-PLA-004`.
- **Aceptación mínima:** una actividad válida conserva fecha, responsable y estado;
  un encargo tiene periodo y alcance; cada socia ve solo sus asignaciones y no
  puede operar con un encargo vencido.

### HU-GEN-004 — Planificar la producción semanal

**Como** responsable de planificación, **quiero** definir productos, cantidades
objetivo, insumos y responsables de la semana, **para** coordinar el trabajo.

- **Requisito:** `RF-PLA-005`.
- **Aceptación mínima:** el plan puede consultarse por las asignadas y conserva
  cambios; planificar no crea todavía existencias ni lotes.

## Sprint 3 — Asistencia y participación

### HU-GEN-005 — Registrar entrada y salida

**Como** socia, **quiero** registrar mi entrada y salida, incluso por un mecanismo
alternativo cuando corresponda, **para** que mi asistencia quede identificada.

- **Requisitos:** `RF-ASI-001`, `RF-ASI-002`, `RF-ASI-007`.
- **Aceptación mínima:** entrada y salida se distinguen; un evento duplicado o un
  QR vencido no modifica datos; se diferencia autorregistro de registro delegado.
- **Decisiones:** P-02 define parámetros de QR y delegación; P-13 define cómo
  aceptar capturas provisionales realizadas sin conexión.

### HU-GEN-006 — Consultar y resolver asistencia

**Como** socia, **quiero** consultar mi historial; **como** Directiva o encargada
autorizada, **quiero** corregir errores y registrar las decisiones organizacionales.

- **Requisitos:** `RF-ASI-003`, `RF-ASI-004`, `RF-ASI-005`, `RF-ASI-006`.
- **Aceptación mínima:** una corrección conserva valor anterior, nuevo valor,
  actor y motivo; la participación adicional se pide solo cuando hace falta;
  una inconsistencia espera decisión de la asamblea y no genera sanción automática.
- **Decisión:** P-03 conserva abiertas las consecuencias de faltas.

## Sprint 4 — Producción, inventario y rendición

### HU-GEN-007 — Mantener productos y valores vigentes

**Como** integrante autorizada de la Directiva, **quiero** administrar el catálogo
y los valores comerciales, **para** operar con datos vigentes sin alterar la historia.

- **Requisitos:** `RF-CAT-001`, `RF-INV-001`.
- **Aceptación mínima:** plantas, insumos, productos, presentaciones y unidades se
  distinguen; un cambio de precio o valor base no modifica ventas anteriores.
- **Decisión:** P-04 define presentaciones y conversiones aún faltantes.

### HU-GEN-008 — Registrar acopio y secado

**Como** socia encargada de producción, **quiero** registrar materia recibida,
pesos y secado, **para** conocer procedencia, duración y merma.

- **Requisitos:** `RF-TRA-001`, `RF-TRA-002`, `RF-TRA-003`.
- **Aceptación mínima:** se registra origen, responsable, unidad, peso inicial y
  final y temperatura; humedad es opcional; duración y merma muestran fórmula
  y unidad, y un peso final mayor exige revisión.
- **Decisión:** P-13 define el tratamiento del tiempo en capturas sin conexión.

### HU-GEN-009 — Seguir los lotes y la transformación

**Como** responsable de producción, **quiero** vincular cada lote con sus orígenes
y consumos, **para** reconstruir la transformación de los productos.

- **Requisitos:** `RF-TRA-004`, `RF-TRA-005`.
- **Aceptación mínima:** producto e insumos quedan relacionados; solo una mezcla
  física crea un lote derivado; cerrar un lote no equivale a agotar sus existencias.
- **Decisión:** P-05 define mezclas, bajas y cierres excepcionales.

### HU-GEN-010 — Controlar existencias y entregas de feria

**Como** responsable de inventario o feria, **quiero** registrar movimientos,
entregas y devoluciones, **para** conciliar cantidades sin perder su origen.

- **Requisitos:** `RF-INV-002`, `RF-INV-003`, `RF-INV-004`.
- **Aceptación mínima:** la existencia se calcula desde movimientos; ninguna
  entrega excede el stock disponible; una diferencia permanece visible para
  conciliación sin crear un saldo negativo silencioso.

### HU-GEN-011 — Registrar una venta verificable

**Como** socia encargada de venta, **quiero** registrar varios productos y su
forma de pago, **para** conocer total, valor base y excedente bruto.

- **Requisitos:** `RF-VEN-001`, `RF-VEN-002`, `RF-VEN-003`, `RF-VEN-004`.
- **Aceptación mínima:** el total se calcula y la venta se confirma completa o
  se revierte; un crédito identifica comprador; vender bajo valor base requiere
  autorización y motivo; los valores históricos no cambian después.

### HU-GEN-012 — Aplicar reglas de venta según el origen

**Como** Tesorera, **quiero** configurar descuentos y registrar ventas
institucionales; **como** encargada de feria, **quiero** distinguir stock individual
y compartido, **para** rendir cuentas sin mezclar resultados.

- **Requisitos:** `RF-VEN-005`, `RF-VEN-006`, `RF-VEN-007`.
- **Aceptación mínima:** una política de descuento incompleta no se aplica; cada
  línea conserva el origen del stock; una venta institucional no atribuye
  excedente a una socia.
- **Decisiones:** P-08 fija parámetros de descuentos; P-07 impide distribuir
  automáticamente el excedente compartido.

### HU-GEN-013 — Conciliar una venta con comprobante manual

**Como** encargada de feria, **quiero** registrar una operación respaldada por
comprobante manual cuando la contingencia lo exija, **para** evitar omisiones
y registros duplicados.

- **Requisito:** `RF-VEN-008`.
- **Aceptación mínima:** el comprobante conserva folio, origen, responsables y
  momentos de operación y digitación; un folio repetido no descuenta dos veces.
- **Decisión:** P-10 define custodia, plazo y conciliación. Este mecanismo no
  sustituye la continuidad sin conexión requerida para flujos habilitados.

### HU-GEN-014 — Registrar gastos, deudas y rendición

**Como** Tesorera o integrante autorizada de la Directiva, **quiero** registrar
gastos y abonos y distinguir cada deuda; **como** encargada de feria, **quiero**
rendir productos y dinero por separado.

- **Requisitos:** `RF-GAS-001`, `RF-GAS-002`, `RF-CXC-001`, `RF-CXC-002`,
  `RF-CXC-003`.
- **Aceptación mínima:** cada gasto y abono conserva monto, fecha y responsable;
  custodia física, deuda de socia y cuenta por cobrar externa no se mezclan;
  la rendición explica diferencias sin ocultarlas.
- **Decisión:** P-09 define el efecto monetario de devoluciones, anulaciones y
  sobrepagos.

## Sprint 5 — Información y sitio público

### HU-GEN-015 — Consultar reportes de la organización

**Como** integrante autorizada de la Directiva, **quiero** revisar asistencia,
actividades, producción, inventario y saldos, **para** tomar decisiones con datos
que pueda rastrear.

- **Requisitos:** `RF-REP-001`, `RF-REP-002`, `RF-REP-003`, `RF-REP-004`,
  `RF-REP-005`.
- **Aceptación mínima:** los reportes explican periodo, filtros y unidades;
  totales de producción y existencias se vinculan con sus movimientos; las
  deudas y pagos se muestran por separado.

### HU-GEN-016 — Consultar mi resumen

**Como** socia, **quiero** ver mi propia asistencia, actividades, productos
y valores pendientes, **para** comprender mi situación sin ver datos ajenos.

- **Requisito:** `RF-REP-006`.
- **Aceptación mínima:** solo se muestran datos autorizados de la socia y el
  excedente bruto no se presenta como ganancia neta.

### HU-GEN-017 — Recibir recordatorios internos

**Como** usuaria interna, **quiero** ver recordatorios sobre mis actividades y
pendientes, **para** actuar a tiempo.

- **Requisito:** `RF-NOT-001`.
- **Aceptación mínima:** cada recordatorio conduce al elemento permitido que
  lo originó, dentro del sistema, sin depender de correo o mensajería.

### HU-GEN-018 — Mostrar información pública aprobada

**Como** visitante, **quiero** consultar información autorizada de Zhud Alelí;
**como** publicadora autorizada, **quiero** preparar, aprobar o retirar contenido.

- **Requisitos:** `RF-PUB-001`, `RF-PUB-002`.
- **Aceptación mínima:** solo aparece contenido aprobado; retirar contenido
  conserva la historia; no se exponen datos internos ni afirmaciones sanitarias.
- **Decisión:** P-12 define textos, imágenes, contacto y personas publicadoras.

## Continuidad transversal

### HU-GEN-019 — Continuar tareas habilitadas sin conexión

**Como** socia que trabaja con conectividad limitada, **quiero** abrir los flujos
preparados, guardar operaciones habilitadas y enviarlas cuando vuelva la red,
**para** no perder un registro ni confundir un pendiente con uno aceptado.

- **Requisitos:** `RF-PWA-001`, `RF-PWA-002`, `RF-PWA-003`.
- **Aceptación mínima:** el dispositivo preparado muestra qué puede hacerse sin
  red; el guardado local persiste; al sincronizar, el servidor revalida y un
  reintento no duplica el registro. Los estados pendiente, aceptado y rechazado
  se distinguen.
- **Decisiones:** P-13 y P-14 definen operaciones concretas, tiempos, sesiones,
  conflictos y retención. Asistencia y pesajes son el mínimo identificado.

## Condiciones que esta redacción conserva

- `RF-COS-001` y `RNF-OPS-001` siguen propuestos; no se convierten en historias
  de implementación confirmadas.
- Las decisiones P-02 a P-14 se cierran en las especificaciones afectadas antes
  de implementar los detalles que dependen de ellas.
- Esta agrupación no fija prioridad dentro de cada sprint ni estima esfuerzo.
  La pila de producto y la planificación deben registrar esas decisiones aparte.
- Los 19 identificadores de historia son editoriales. Un ajuste posterior requiere
  una nueva versión sin modificar los IDs canónicos de requisitos.

## Historial de esta edición

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Tesista | Agrupación editorialmente aprobada de los 51 requisitos funcionales en historias con aceptación mínima y decisiones abiertas. | Final del tesista; revisión de directora pendiente |
