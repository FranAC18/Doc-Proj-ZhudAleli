---
title: Decisiones pendientes del proyecto
type: decision-log
status: in-progress
updated: 2026-07-25
---

# Decisiones pendientes

Las decisiones D-001 a D-010 permitieron construir la primera línea base. Esta nota también
mantiene las decisiones de detalle P-01 a P-12 de
[[../requirements/CAT-REQ-001|CAT-REQ-001 v1.0]]. El catálogo ya está aprobado; cada P
bloquea únicamente la parte de una spec indicada.

## D-001 - Denominación legal

- Pregunta: ¿la organización debe aparecer como Comité o Asociación?
- Fuente del conflicto: anteproyecto.
- Impacto: nombre del sistema, documentos, usuarios, reportes y tesis.
- Decisión: usar `Comité de Mujeres Indígenas “Tránsito Amaguaña”`.
- Confirmó: tesista, 2026-07-21.
- Estado: confirmado para el nombre visible del sistema; la evidencia jurídica formal se verificará si la tesis realiza una afirmación legal.

## D-002 - Alcance comercial

- Pregunta: ¿ventas y cuentas por cobrar forman parte de la primera versión?
- Impacto: módulos, entidades, permisos, reportes y tamaño del proyecto.
- Decisión: ventas y cuentas por cobrar forman parte del alcance inicial.
- Confirmó: tesista, 2026-07-21.
- Estado: confirmado; el modelo funcional económico queda registrado en D-010 y sus detalles
  técnicos se definirán en la especificación.

## D-003 - Variables de secado

- Pregunta: ¿qué variables se deben registrar obligatoriamente?
- Opciones a validar: peso inicial, peso final, tiempo, humedad, temperatura y observaciones.
- Impacto: trazabilidad, métricas y formularios.
- Decisión: peso inicial, peso final y un único valor de temperatura en grados Celsius son
  obligatorios; humedad no es obligatoria.
- Fechas: el inicio y el fin registran automáticamente fecha y hora. El fin ocurre normalmente el
  mismo día, según la planta y el tipo de horno utilizados.
- Confirmó: tesista, 2026-07-21.
- Estado: confirmado.

## D-004 - Correcciones y auditoría

- Pregunta: ¿quién puede corregir asistencia, pesajes, lotes o inventario?
- Impacto: permisos, historial de cambios y rendición de cuentas.
- Decisión: solo la directiva y la encargada pueden corregir estos registros.
- Auditoría: conservar usuario, fecha y hora, valor anterior, valor nuevo y motivo de cada cambio.
- Confirmó: tesista, 2026-07-21.
- Nota: el alcance funcional de la encargada está definido en D-005; los permisos de cada pantalla
  se especificarán por funcionalidad.
- Estado: confirmado, con detalles de pantalla pendientes de las especificaciones.

## D-005 - Perfiles reales

- Pregunta: ¿los perfiles serán directiva y socias operarias, o se dividirán presidenta,
  secretaria y tesorera con permisos distintos?
- Impacto: RBAC y navegación.
- Decisión estructural: los perfiles técnicos serán Directiva, Socia operaria y Visitante.
  Presidenta, tesorera y secretaria se conservarán como cargos organizativos dentro de Directiva;
  visitante consultará únicamente información pública.
- Encargada: asignación temporal a una socia operaria para una actividad y periodo concretos;
  no crea un usuario ni un rol permanente adicional. El encargo puede ser de Producción
  (acopio, secado, transformación o lote) o de Feria/venta (productos recibidos, vendidos,
  devueltos y dinero entregado).
- UX: cada persona tendrá una interfaz personalizada por cargo o encargo, sin mostrar permisos
  técnicos ni exigir que elija un rol.
- Confirmó estructura y simplificación: tesista, 2026-07-21.
- Estado: confirmado; las reglas detalladas de cada pantalla se especificarán por funcionalidad.

## D-006 - Reportes prioritarios

- Pregunta: ¿qué reportes necesita primero la organización?
- Impacto: diseño de consultas y validación del valor del sistema.
- Decisión: la primera versión incluirá reportes de asistencia por periodo y socia, actividades y
  encargos pendientes, producción (acopio, secado, lotes y mermas), inventario y movimientos,
  ventas y cuentas por cobrar.
- Formato: descarga en PDF.
- Presentación: estructura clara, gráficos comprensibles y logo autorizado de Zhud Alelí.
- Confirmó: tesista, 2026-07-21.
- Pendiente técnico: definir gráficos, filtros, periodos, generación del PDF y obtener el archivo
  oficial del logo.
- Estado: confirmado.

## D-007 - Registro sanitario

- Pregunta: ¿qué productos tienen registro sanitario y qué documentación puede verificarse?
- Impacto: alcance de trazabilidad, reportes y redacción de cumplimiento.
- Decisión: existe un registro sanitario, pero queda fuera del sistema y no es obligatorio
  mostrarlo.
- Restricción: la aplicación no realizará afirmaciones de cumplimiento sanitario.
- Confirmó: tesista, 2026-07-21.
- Estado: confirmado fuera de alcance.

## D-008 - Equipamiento y conectividad

- Pregunta: ¿cuál es el estado real de las dos computadoras, el router y la conectividad?
- Impacto: despliegue, accesibilidad y pruebas en campo.
- Situación confirmada: dos computadoras funcionales, red Wi-Fi e Internet casi estable.
- Alcance de acceso: la aplicación debe funcionar dentro y fuera de la organización, incluso
  durante ferias y otras actividades externas.
- Restricción técnica: interfaz ligera y tolerante a conectividad inestable.
- Pendiente técnico: definir despliegue, respaldos y si se necesita funcionamiento offline con
  sincronización; esto no se asumirá automáticamente.
- Confirmó: tesista, 2026-07-21.
- Estado: confirmado con diseño técnico pendiente.

## D-009 - Sitio web público

- Pregunta: ¿se debe crear o actualizar una landing page dentro del alcance del sistema?
- Impacto: diseño, navegación pública y esfuerzo del Sprint 5.
- Decisión: se incluirá una página pública para visitantes, con información aprobada por la
  organización.
- Confirmó: tesista, 2026-07-21.
- Pendiente: definir contenido, imágenes, datos de contacto y si existe un sitio previo que deba
  actualizarse.
- Estado: confirmado con contenido pendiente.

## D-010 - Distribución y rendición de cuentas

- Pregunta: ¿cómo se calcula el costo de producción, el margen organizacional, la ganancia
  individual y la deuda de cada socia?
- Impacto: inventario, ventas, cuentas por cobrar y reportes.
- Reglas funcionales confirmadas por el tesista:
  - Un encargo temporal puede corresponder a producción o a una feria/venta; la socia usará
    una pantalla simple de “Mis encargos” con campos según el tipo.
  - La socia registra solo productos recibidos, productos vendidos y productos devueltos o
    sobrantes; el sistema calcula el saldo de productos que conserva.
  - En una feria, la venta se registra desde el stock asignado y permite incluir varios productos
    en una sola operación, con cantidad, comprador y forma de pago; el precio y total se completan
    desde el catálogo.
  - Para una venta al contado se propone usar `Público general` como comprador predeterminado; para
    ventas a crédito o a instituciones se solicitará nombre del comprador y se generará el saldo
    pendiente.
  - Cada producto entregado a una socia tendrá un valor base para la organización, configurado por
    la directiva o tesorera. Por cada unidad vendida, ese valor base corresponde a la organización;
    el excedente sobre el valor base corresponde a la socia. El valor base será fijo por producto.
  - El sistema calculará el aporte organizacional y el excedente de la socia sin pedirle fórmulas
    manuales.
  - Una venta por debajo del valor base requerirá autorización de la directiva, motivo y registro
    de auditoría; no se permitirá como operación normal.
  - La directiva o tesorera registra una sola vez por lote o periodo los gastos operativos,
    como botellas, fundas, etiquetas, transporte, energía u otros.
  - El sistema conserva movimientos y calcula existencias y resultados desde esos movimientos,
    sin pedir a cada socia que registre costos o fórmulas contables.
  - La ganancia individual no se calcula hasta confirmar la regla de distribución.
  - Se manejarán dos saldos separados: saldo de la socia con la organización por el valor base de
    productos entregados y cuenta por cobrar de clientes externos por ventas a crédito.
  - Se permitirán pagos parciales. Cada abono conservará monto, fecha/hora, forma de pago y
    responsable del registro; el sistema calculará el saldo restante.
- Confirmó: tesista, 2026-07-21.
- Estado: confirmado funcionalmente; el diseño técnico de formularios y reportes queda para la
  especificación.

## D-011 - Acceso inicial y primera cuenta

- Pregunta: ¿cómo inicia sesión una usuaria y qué incluye la primera porción de acceso?
- Decisión: la usuaria inicia sesión con un nombre de usuario (`username`).
- Primera cuenta: se almacenará en la base de datos y se entregará cuando el sistema esté
  funcional.
- Cambio de contraseña: incluido en la primera porción.
- Destino posterior: dashboard privado de bienvenida con las opciones disponibles.
- Alcance: opción A, limitada a `RF-ACC-001` y RNF aplicables; no completa Sprint 1.
- Confirmó: tesista, 2026-07-25.
- Evidencia:
  [[../evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0|ACT-REQ-001]].
- Recomendación técnica: crear la cuenta con mecanismos Django, guardar solo el hash,
  entregar una credencial temporal por un canal seguro y solicitar cambio inicial.
- Pendiente: identificar la persona o cargo receptor, el canal de entrega y el tiempo de
  inactividad. P-01 continúa abierta.
- Estado: confirmado para preparar la spec; los detalles técnicos se aprueban en el plan.

## Decisiones de detalle abiertas de CAT-REQ-001 v1.0

| ID | Tema | Estado | Puerta afectada |
|---|---|---|---|
| P-01 | Matriz cargo por operación y acceso de soporte | `open` | Spec de permisos y operaciones sensibles |
| P-02 | Duración del QR, habilitación de fases y delegación | `open` | Spec de asistencia antes del QR |
| P-03 | Consecuencias y autoridad sobre faltas | `open` | Sanciones; no bloquea asistencia básica |
| P-04 | Presentaciones, unidades, conversiones y plantas | `open` | Fórmulas y movimientos que conviertan unidades |
| P-05 | Mezclas, divisiones, bajas y cierres excepcionales | `open` | Excepciones de lotes |
| P-06 | Fórmula de costo completo | `open` | Mantiene `RF-COS-001` en `proposed` |
| P-07 | Distribución del excedente compartido | `open` | Distribución; no bloquea registrar ventas |
| P-08 | Umbrales y valores de descuentos | `open` | Activación de políticas de `RF-VEN-005` |
| P-09 | Devoluciones, pérdidas, anulaciones y sobrepagos | `open` | Ajustes monetarios automáticos |
| P-10 | Procedimiento operativo de contingencia | `open` | Flujo final de feria sin Internet |
| P-11 | Política y responsables de respaldos | `open` | Mantiene `RNF-OPS-001` en `proposed` |
| P-12 | Contenido y publicadores autorizados | `open` | Publicación de contenido final |

El detalle de cada pregunta, su tratamiento y los requisitos relacionados está en
[[../requirements/CAT-REQ-001#Decisiones de detalle abiertas|CAT-REQ-001]]. Cuando una P se
resuelva, registrar fecha, participantes, fuente y efecto sobre las specs; no editar solo la
tabla sin evidencia.
