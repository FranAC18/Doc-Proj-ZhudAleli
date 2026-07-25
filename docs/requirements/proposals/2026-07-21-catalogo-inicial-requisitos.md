---
title: Catálogo inicial de requisitos propuestos
type: requirement
status: superseded
id: CAT-REQ-001-R1
superseded_by: CAT-REQ-001-R2
created: 2026-07-21
phase: Fase I
sprint: transversal
priority: high
module: transversal
validated_by: []
related:
  - "[[../../../agents/tesis/PROJECT_CONTEXT]]"
  - "[[../../00-inicio/01-decisiones-pendientes]]"
  - "[[../../sprints/ROADMAP-ANTEPROYECTO]]"
  - "[[../../ui/SISTEMA-DISENO]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - estado/superseded
---

# CAT-REQ-001-R1 - Catálogo inicial de requisitos propuestos

## Propósito y estado

Este documento transforma el anteproyecto y las decisiones D-001 a D-010 en propuestas
revisables. No aprueba requisitos, no reemplaza entrevistas con la organización y no autoriza
crear Django, PostgreSQL ni código funcional.

- **Estado durante esta revisión**: `proposed`; actualmente `superseded` por
  `CAT-REQ-001-R2`.
- **Debe validar**: tesista y representantes autorizadas del Comité.
- **Fecha de validación**: pendiente.
- **Resultado esperado**: aceptar, ajustar o descartar cada requisito antes de crear su spec.

## Cómo revisar en Obsidian

Revisa un bloque por vez. Para comunicar una decisión puedes responder, por ejemplo:

```text
Acepto: RF-ACC-001, RF-ACC-002.
Ajustar RF-PLA-001: ...
Descartar RF-ASI-002 porque ...
```

Aceptar un requisito significa confirmar su necesidad y reglas funcionales, no aprobar aún
el diseño de pantallas, base de datos o implementación.

## Fuentes utilizadas

- **F1**: [[../../../agents/tesis/PROJECT_CONTEXT|Contexto del anteproyecto]].
- **F2**: [[../../00-inicio/01-decisiones-pendientes|Decisiones D-001 a D-010]].
- **F3**: [[../../00-inicio/02-evaluacion-documentos|Evaluación de documentos previos]].
- **F4**: [[../../sprints/ROADMAP-ANTEPROYECTO|Roadmap del anteproyecto]].
- **F5**: [[../../ui/SISTEMA-DISENO|Criterios UX propuestos]].
- **F6**: [[../../architecture/ARQUITECTURA-OBJETIVO|Arquitectura objetivo propuesta]].
- **F7**: confirmaciones del tesista registradas el 2026-07-21 en D-001 a D-010.

## Alcance excluido por ahora

- Registro o afirmaciones de cumplimiento sanitario.
- Facturación electrónica, contabilidad tributaria o integración con sistemas fiscales.
- Sanciones económicas a las socias sin una regla validada por la organización.
- Sincronización offline; solo se propone tolerancia a conexión inestable.
- Cálculo de distribución de utilidades distinto del valor base y excedente confirmados.
- Notificaciones por correo, SMS o mensajería sin canal y consentimiento validados.

---

## 1. Administración, acceso y perfiles — Sprint 1

### RF-ACC-001 - Acceso de usuarias internas

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Socia operaria.
- **Descripción**: el sistema debe permitir a una usuaria interna activa iniciar y cerrar
  sesión para acceder únicamente a la información y acciones autorizadas.
- **Reglas**:
  - Visitante no necesita una cuenta para consultar información pública.
  - Una cuenta inactiva no puede iniciar sesión.
- **Criterios de aceptación**:
  1. Dada una cuenta activa con credenciales válidas, cuando la usuaria inicia sesión,
     entonces accede a su inicio personalizado.
  2. Dada una cuenta inactiva o credenciales inválidas, cuando intenta acceder, entonces el
     sistema rechaza la operación sin revelar información sensible.
- **Fuente**: F1, F4.
- **Debe validar**: Directiva y tesista.

### RF-ACC-002 - Administración de cuentas y membresía

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva autorizada.
- **Descripción**: el sistema debe permitir registrar, actualizar, activar o desactivar
  cuentas de las socias sin eliminar su historial organizativo o productivo.
- **Reglas**:
  - Desactivar una cuenta impide nuevos accesos, pero conserva registros históricos.
  - No se almacenarán datos personales que no sean necesarios para operar el sistema.
- **Criterios de aceptación**:
  1. Dada una socia registrada, cuando la Directiva la desactiva, entonces pierde acceso y
     sus registros previos permanecen consultables por quienes tengan permiso.
  2. Dada una Socia operaria, cuando intenta administrar cuentas, entonces la operación se
     deniega.
- **Fuente**: F1, F5, F6.
- **Debe validar**: Directiva y tesista.

### RF-ACC-003 - Perfiles técnicos y cargos organizativos

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva, Socia operaria y Visitante.
- **Descripción**: el sistema debe reconocer tres perfiles técnicos: Directiva, Socia
  operaria y Visitante; presidenta, tesorera y secretaria se registran como cargos dentro de
  Directiva.
- **Reglas**:
  - Una usuaria no elige ni cambia su perfil al entrar.
  - Los cargos pueden personalizar funciones sin crear perfiles técnicos innecesarios.
- **Criterios de aceptación**:
  1. Dada una integrante de la Directiva, cuando inicia sesión, entonces conserva su cargo y ve las opciones correspondientes.
  2. Dado un Visitante, cuando navega por el sitio, entonces solo puede consultar contenido público aprobado.
- **Fuente**: F1, F2-D-005, F7.
- **Debe validar**: Directiva y tesista.

### RF-ACC-004 - Inicio personalizado y encargos vigentes

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Socia operaria.
- **Descripción**: el sistema debe mostrar un inicio sencillo con las actividades y encargos
  vigentes de la usuaria, sin exponer nombres técnicos de permisos.
- **Reglas**:
  - Una Socia operaria solo recibe acciones adicionales mientras su encargo esté vigente.
  - El inicio prioriza “Mis actividades” y “Mis encargos”.
- **Criterios de aceptación**:
  1. Dada una socia con encargo vigente, cuando abre su inicio, entonces ve el encargo, su
     periodo y las acciones permitidas.
  2. Dada una socia sin encargo vigente, cuando abre su inicio, entonces no ve acciones de encargada.
- **Fuente**: F2-D-005, F5, F7.
- **Debe validar**: Socias operarias, Directiva y tesista.

---

## 2. Planificación de actividades y encargos — Sprint 2

### RF-PLA-001 - Gestión de actividades

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva.
- **Descripción**: el sistema debe permitir crear y actualizar actividades o jornadas con
  nombre, descripción breve, fecha, hora, lugar, responsable y estado.
- **Reglas**:
  - Los estados mínimos propuestos son pendiente, en curso, completada y cancelada.
  - Una cancelación conserva la actividad y su motivo.
- **Criterios de aceptación**:
  1. Dada una actividad con datos válidos, cuando la Directiva la registra, entonces queda
     disponible para las participantes asignadas.
  2. Dada una fecha u hora inválida, cuando intenta guardar, entonces el sistema explica qué
     debe corregirse y conserva los demás datos válidos.
- **Fuente**: F1, F4, F5.
- **Debe validar**: Directiva, socias y tesista.

### RF-PLA-002 - Asignación de participantes y responsable

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva.
- **Descripción**: el sistema debe permitir asignar una responsable y las socias
  participantes de cada actividad.
- **Reglas**:
  - Una persona puede participar sin ser responsable.
  - La asignación debe permanecer visible para cada socia implicada.
- **Criterios de aceptación**:
  1. Dada una actividad vigente, cuando la Directiva asigna participantes, entonces cada una
     puede consultarla en su inicio.
  2. Dada una cuenta inactiva, cuando se intenta asignarla, entonces el sistema advierte y no
     completa la asignación.
- **Fuente**: F1, F4.
- **Debe validar**: Directiva y tesista.

### RF-PLA-003 - Encargo temporal de producción o feria

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Socia operaria encargada.
- **Descripción**: el sistema debe permitir asignar a una socia un encargo temporal de
  producción o de feria/venta, con actividad, periodo, responsabilidad y estado.
- **Reglas**:
  - Encargada es una asignación temporal, no un perfil permanente.
  - El permiso adicional termina al cerrar o vencer el encargo.
- **Criterios de aceptación**:
  1. Dado un encargo vigente, cuando la socia accede, entonces puede realizar únicamente las operaciones asociadas a ese encargo.
  2. Dado un encargo finalizado, cuando la socia intenta usar una operación adicional, entonces el sistema la deniega.
- **Fuente**: F2-D-005, F2-D-010, F7.
- **Debe validar**: Directiva, socias encargadas y tesista.

### RF-PLA-004 - Consulta de actividades y encargos pendientes

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Socia operaria.
- **Descripción**: el sistema debe permitir consultar actividades y encargos por periodo,
  estado, responsable y participación de la usuaria.
- **Criterios de aceptación**:
  1. Dada una usuaria autenticada, cuando consulta sus pendientes, entonces ve solo los elementos que le corresponden y su estado actual.
  2. Dada una consulta sin resultados, entonces el sistema muestra un mensaje claro y no una  tabla vacía sin explicación.
- **Fuente**: F1, F2-D-006, F5.
- **Debe validar**: Directiva, socias y tesista.

---

## 3. Asistencia y participación — Sprint 3

### RF-ASI-001 - Registro de asistencia por actividad

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: perfil registrador por confirmar; Socia operaria como participante.
- **Descripción**: el sistema debe registrar la asistencia de cada socia a una actividad,
  vinculando actividad, socia, fecha y responsable del registro.
- **Reglas**:
  - El mecanismo exacto de entrada, salida y ausencia depende de la pregunta crítica Q1.
  - El registro debe ser más rápido y claro que completar una lista manual extensa.
- **Criterios de aceptación**:
  1. Dada una actividad vigente y una socia participante, cuando un perfil autorizado registra
     su asistencia, entonces queda vinculada una sola vez a esa actividad.
  2. Dado un perfil no autorizado, cuando intenta registrar asistencia, entonces la operación
     se deniega.
- **Fuente**: F1, F3, F4.
- **Debe validar**: Directiva, socias y tesista.

### RF-ASI-002 - Prevención de duplicados e inconsistencias

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: perfil registrador de asistencia.
- **Descripción**: el sistema debe impedir registros duplicados para una misma socia y
  actividad y debe detectar horas incompatibles con el flujo confirmado.
- **Criterios de aceptación**:
  1. Dada una asistencia existente, cuando se intenta registrar otra para la misma socia y
     actividad, entonces el sistema evita el duplicado y muestra el registro existente.
  2. Dada una salida anterior a la entrada, si ambas se confirman como necesarias, entonces
     el sistema rechaza el dato e indica cómo corregirlo.
- **Fuente**: F1, F5.
- **Debe validar**: Directiva y tesista.

### RF-ASI-003 - Corrección autorizada de asistencia

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Encargada vigente.
- **Descripción**: el sistema debe permitir corregir una asistencia únicamente a la Directiva
  o a la Encargada autorizada, exigiendo un motivo y conservando historial.
- **Criterios de aceptación**:
  1. Dado un registro existente, cuando una persona autorizada lo corrige con motivo, entonces
     se conserva quién, cuándo, valor anterior, valor nuevo y motivo.
  2. Dada una Socia operaria sin encargo, cuando intenta corregirlo, entonces la operación se
     deniega sin alterar el historial.
- **Fuente**: F2-D-004, F2-D-005, F7.
- **Debe validar**: Directiva y tesista.

### RF-ASI-004 - Historial individual y por periodo

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Socia operaria.
- **Descripción**: el sistema debe permitir consultar asistencia por socia, actividad y
  periodo; una socia consulta su propio historial y la Directiva el conjunto autorizado.
- **Criterios de aceptación**:
  1. Dada una socia autenticada, cuando consulta su historial, entonces ve sus registros y
     correcciones visibles permitidas.
  2. Dado un periodo sin registros, entonces el sistema informa que no existen datos para ese
     filtro.
- **Fuente**: F1, F2-D-006.
- **Debe validar**: Directiva, socias y tesista.

### RF-ASI-005 - Registro de participación en actividades

- **Estado**: `proposed`.
- **Prioridad**: media.
- **Actor**: Directiva, Encargada y Socia participante.
- **Descripción**: el sistema debe permitir registrar la participación de una socia en una
  actividad cuando asistir no sea suficiente para describir su intervención.
- **Reglas**:
  - Los tipos de participación se definirán con la organización y deben ser pocos y claros.
  - La participación permanece vinculada a la actividad y a la socia.
- **Criterios de aceptación**:
  1. Dada una actividad que requiere detalle de participación, cuando un perfil autorizado lo
     registra, entonces queda asociado a la socia y actividad correctas.
  2. Dada una actividad que solo necesita asistencia, entonces el detalle de participación no
     se exige como campo obligatorio.
- **Fuente**: F1, F4.
- **Debe validar**: Directiva, socias y tesista.

---

## 4. Trazabilidad productiva — Sprint 4

### RF-TRA-001 - Registro de acopio de materia prima

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Encargada de producción y Directiva.
- **Descripción**: el sistema debe registrar cada recepción de materia prima con socia que
  entrega, tipo de materia prima, cantidad o peso, fecha y responsable del registro.
- **Reglas**:
  - La unidad y el catálogo de plantas se validan en Q2.
  - Una corrección conserva historial.
- **Criterios de aceptación**:
  1. Dada una entrega válida, cuando la Encargada la registra, entonces queda disponible como
     origen de un proceso o lote posterior.
  2. Dado un valor de peso nulo o no positivo cuando sea obligatorio, entonces el sistema no
     guarda y explica la corrección requerida.
- **Fuente**: F1, F3, F4.
- **Debe validar**: Encargadas de producción, Directiva y tesista.

### RF-TRA-002 - Registro del proceso de secado

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Encargada de producción y Directiva.
- **Descripción**: el sistema debe registrar peso inicial, peso final, una temperatura en
  grados Celsius, humedad opcional, inicio automático y final registrado al concluir.
- **Reglas**:
  - Inicio y fin guardan fecha y hora automáticamente.
  - Una edición posterior se trata como corrección autorizada y auditada.
  - El proceso ocurre normalmente el mismo día, pero no se fuerza una duración fija.
- **Criterios de aceptación**:
  1. Dado el inicio de un secado, cuando la Encargada lo registra, entonces el sistema coloca
     fecha y hora de inicio sin pedirlas manualmente.
  2. Dado un proceso abierto, cuando se registra peso final y temperatura válidos, entonces se
     guarda el final con fecha y hora; la humedad puede quedar vacía.
- **Fuente**: F1, F2-D-003, F7.
- **Debe validar**: Encargadas de producción, Directiva y tesista.

### RF-TRA-003 - Cálculo de duración y merma

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Encargada de producción y Directiva.
- **Descripción**: el sistema debe calcular la duración del secado y la merma de peso a partir de los valores registrados, sin pedir fórmulas manuales a la usuaria.
- **Reglas**:
  - La fórmula propuesta de merma absoluta es peso inicial menos peso final.
  - El porcentaje y las reglas de redondeo se validarán antes de aprobar la spec.
- **Criterios de aceptación**:
  1. Dados pesos válidos e inicio/final, cuando se cierra el secado, entonces se muestran duración y merma con sus unidades.
  2. Dado un peso final mayor al inicial, entonces el sistema solicita revisión o motivo antes de aceptar una excepción.
- **Fuente**: F1, F2-D-003, F5.
- **Debe validar**: Encargadas de producción, Directiva y tesista.

### RF-TRA-004 - Formación y consulta de lotes

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Encargada de producción y Directiva.
- **Descripción**: el sistema debe formar lotes de producto vinculando los acopios, procesos
  de secado o transformación, productos resultantes, cantidades y responsables.
- **Reglas**:
  - Un lote conserva su origen y movimientos; no se reemplaza la historia con un total.
  - Las reglas exactas para mezclar materias primas se validan en Q2.
- **Criterios de aceptación**:
  1. Dado un lote registrado, cuando se consulta, entonces se puede recorrer desde el producto
     resultante hasta sus acopios y procesos de origen.
  2. Dada una operación que dejaría cantidades incompatibles con el origen, entonces el
     sistema la rechaza o exige una corrección autorizada.
- **Fuente**: F1, F2-D-004, F6.
- **Debe validar**: Encargadas de producción, Directiva y tesista.

---

## 5. Productos e inventario — Sprint 4

### RF-INV-001 - Catálogo de productos y presentaciones

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Tesorera.
- **Descripción**: el sistema debe mantener un catálogo de productos y presentaciones activos,
  con unidad, nombre visible y valor base vigente para la organización.
- **Reglas**:
  - El valor base es fijo por producto mientras esté vigente.
  - Cambiar un valor base no modifica ventas históricas.
- **Criterios de aceptación**:
  1. Dado un producto activo, cuando se usa en inventario o venta, entonces se aplica la
     presentación y valor base vigentes.
  2. Dado un producto con historia, cuando se desactiva, entonces deja de estar disponible para
     nuevas operaciones sin borrar registros anteriores.
- **Fuente**: F2-D-010, F3, F7.
- **Debe validar**: Tesorera, Directiva y tesista.

### RF-INV-002 - Movimientos y existencias

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva, Encargada de producción y Encargada de feria según operación.
- **Descripción**: el sistema debe registrar entradas, salidas, asignaciones, devoluciones y
  ajustes autorizados como movimientos y calcular las existencias desde ellos.
- **Reglas**:
  - Ningún cambio de stock se realiza sin un movimiento identificable.
  - Un ajuste exige permiso, motivo e historial.
- **Criterios de aceptación**:
  1. Dado un movimiento válido, cuando se registra, entonces la existencia cambia exactamente
     en la cantidad y dirección indicadas.
  2. Dado un perfil no autorizado, cuando intenta ajustar inventario, entonces la operación se
     deniega.
- **Fuente**: F1, F2-D-004, F2-D-010, F6.
- **Debe validar**: Directiva, encargadas y tesista.

### RF-INV-003 - Entrega de productos a una socia o feria

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Encargada de feria, Directiva y Socia receptora.
- **Descripción**: el sistema debe registrar qué productos y cantidades recibe una socia para
  vender, asociados a un encargo o feria.
- **Reglas**:
  - La entrega disminuye el stock disponible y crea el saldo de productos bajo responsabilidad
    de la socia.
  - La socia confirma o consulta lo recibido mediante un flujo corto.
- **Criterios de aceptación**:
  1. Dada una entrega válida, cuando se registra, entonces se identifica socia, productos,
     cantidades, fecha y responsable.
  2. Dada una cantidad superior al stock disponible, entonces el sistema impide la entrega.
- **Fuente**: F2-D-005, F2-D-010, F7.
- **Debe validar**: Socias, Tesorera, Directiva y tesista.

### RF-INV-004 - Conciliación de productos vendidos y devueltos

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Socia encargada de feria, Tesorera y Directiva.
- **Descripción**: el sistema debe conciliar productos recibidos, vendidos, devueltos y aún en poder de la socia, calculando el saldo sin pedirle fórmulas.
- **Criterios de aceptación**:
  1. Dados productos recibidos, ventas y devoluciones, cuando se consulta el encargo, entonces el sistema muestra el saldo de unidades pendiente.
  2. Dada una conciliación que supera las unidades recibidas, entonces el sistema no la acepta y señala la inconsistencia.
- **Fuente**: F2-D-010, F7.
- **Debe validar**: Socias, Tesorera, Directiva y tesista.

---

## 6. Ventas, gastos y cuentas por cobrar — Sprint 4

### RF-VEN-001 - Registro sencillo de ventas

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Socia con encargo de feria/venta, Tesorera y Directiva.
- **Descripción**: el sistema debe registrar una venta desde el stock asignado, permitiendo
  varios productos, cantidad, precio de venta, comprador y forma de pago en una sola operación.
- **Reglas**:
  - Los productos se eligen del catálogo y del stock disponible de la socia.
  - El total se calcula automáticamente.
- **Criterios de aceptación**:
  1. Dados productos disponibles, cuando la socia registra cantidades y precio, entonces el sistema calcula el total y descuenta las unidades correspondientes.
  2. Dada una cantidad no disponible, entonces no permite completar la venta.
- **Fuente**: F2-D-002, F2-D-010, F7.
- **Debe validar**: Socias vendedoras, Tesorera, Directiva y tesista.

### RF-VEN-002 - Comprador y forma de pago

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: persona que registra la venta.
- **Descripción**: el sistema debe usar “Público general” como comprador predeterminado en
  ventas al contado y exigir identificación mínima del comprador en ventas a crédito o
  institucionales.
- **Reglas**:
  - Solo se solicitan datos necesarios para identificar la deuda.
  - Una venta a crédito genera una cuenta por cobrar externa.
- **Criterios de aceptación**:
  1. Dada una venta al contado, cuando no se indica comprador, entonces se registra como “Público general”.
  2. Dada una venta a crédito sin comprador identificable, entonces el sistema no permite completarla.
- **Fuente**: F2-D-010, F7.
- **Debe validar**: Tesorera, Directiva y tesista.

### RF-VEN-003 - Valor base y excedente de la socia

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Socia vendedora, Tesorera y Directiva.
- **Descripción**: el sistema debe calcular por cada venta el valor que corresponde a la
  organización y el excedente que corresponde a la socia.
- **Reglas**:
  - La organización recibe siempre el valor base vigente por unidad vendida.
  - El monto vendido por encima del valor base corresponde a la socia.
  - No se calcula otra distribución de utilidad o gasto individual sin una regla posterior.
- **Criterios de aceptación**:
  1. Dado un producto con valor base 5 y precio de venta 6, cuando se vende una unidad, entonces el sistema asigna 5 a la organización y 1 como excedente de la socia.
  2. Dada una venta de varias unidades, entonces ambos valores se calculan por cantidad y se muestran por separado.
- **Fuente**: F2-D-010, F7.
- **Debe validar**: Socias, Tesorera, Directiva y tesista.

### RF-VEN-004 - Venta excepcional bajo el valor base

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y persona que registra la venta.
- **Descripción**: el sistema debe impedir como operación normal una venta bajo el valor base;  la excepción requiere autorización de Directiva, motivo y auditoría.
- **Criterios de aceptación**:
  1. Dado un precio inferior al valor base, cuando no existe autorización, entonces la venta no se completa.
  2. Dada una autorización válida con motivo, cuando se completa la venta, entonces se registra
     quién autorizó, cuándo y por qué.
- **Fuente**: F2-D-010, F7.
- **Debe validar**: Directiva, Tesorera y tesista.

### RF-GAS-001 - Registro de gastos operativos

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Tesorera y Directiva.
- **Descripción**: el sistema debe registrar gastos operativos por lote o periodo, con categoría,
  monto, fecha, concepto y responsable.
- **Reglas**:
  - Categorías iniciales: botellas, fundas, etiquetas, transporte, energía y otros.
  - Las socias operarias no registran fórmulas ni distribuciones contables.
- **Criterios de aceptación**:
  1. Dado un gasto válido, cuando la Tesorera lo registra, entonces queda asociado una sola vez
     al lote o periodo indicado.
  2. Dado un monto no positivo o sin concepto, entonces el sistema no lo acepta.
- **Fuente**: F2-D-010, F7.
- **Debe validar**: Tesorera, Directiva y tesista.

### RF-GAS-002 - Resumen económico por lote o periodo

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Tesorera y Directiva.
- **Descripción**: el sistema debe resumir ingresos correspondientes a la organización,
  gastos operativos y resultado del lote o periodo, manteniendo separado el excedente de las
  socias.
- **Reglas**:
  - Cada total debe derivarse de ventas, valores base y gastos registrados.
  - La fórmula final y el tratamiento de gastos compartidos deben ser validados por la Tesorera.
  - El resultado no se presenta como utilidad tributaria o contable certificada.
- **Criterios de aceptación**:
  1. Dados valores base obtenidos y gastos asociados, cuando se consulta el resumen, entonces
     se muestran componentes, fórmula aplicada y resultado verificable.
  2. Dado un gasto sin lote o periodo compatible, entonces no se incluye silenciosamente y se
     muestra como pendiente de clasificación.
- **Fuente**: F2-D-010, F3, F7.
- **Debe validar**: Tesorera, Directiva y tesista.

### RF-CXC-001 - Separación de dos tipos de saldo

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Tesorera, Directiva y Socia operaria según consulta.
- **Descripción**: el sistema debe separar el saldo de una socia con la organización por
  productos entregados del saldo de clientes externos por ventas a crédito.
- **Reglas**:
  - Los saldos no se compensan ni mezclan automáticamente.
  - Cada saldo se deriva de operaciones y pagos identificables.
- **Criterios de aceptación**:
  1. Dada una entrega a una socia y una venta externa a crédito, cuando se consultan saldos, entonces aparecen en categorías independientes.
  2. Dado un pago asociado a un tipo de saldo, entonces no altera el otro.
- **Fuente**: F2-D-010, F7.
- **Debe validar**: Tesorera, Directiva, socias y tesista.

### RF-CXC-002 - Registro de pagos parciales

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Tesorera y Directiva; Socia encargada si se autoriza para el encargo.
- **Descripción**: el sistema debe registrar abonos parciales con monto, fecha y hora, forma de
  pago y responsable, calculando el saldo restante.
- **Criterios de aceptación**:
  1. Dado un saldo pendiente, cuando se registra un abono válido, entonces el sistema conserva
     el pago y reduce el saldo por ese monto.
  2. Dado un abono superior al saldo, entonces el sistema impide registrarlo o exige una regla
     explícita de excedente antes de continuar.
- **Fuente**: F2-D-010, F7.
- **Debe validar**: Tesorera, Directiva y tesista.

### RF-CXC-003 - Rendición de un encargo de feria

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Socia encargada de feria, Tesorera y Directiva.
- **Descripción**: el sistema debe resumir por encargo productos recibidos, vendidos,
  devueltos, saldo de productos, valor para la organización, excedente de la socia y pagos
  entregados.
- **Criterios de aceptación**:
  1. Dado un encargo con movimientos, cuando se prepara la rendición, entonces el sistema
     presenta todos los componentes sin pedir cálculos manuales.
  2. Dada una diferencia entre ventas, productos y pagos, entonces el encargo permanece
     pendiente y muestra qué falta conciliar.
- **Fuente**: F2-D-005, F2-D-010, F7.
- **Debe validar**: Socias vendedoras, Tesorera, Directiva y tesista.

---

## 7. Reportes y sitio público — Sprint 5

### RF-REP-001 - Reporte de asistencia

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva.
- **Descripción**: el sistema debe generar un reporte de asistencia filtrable por periodo,
  actividad y socia, descargable en PDF.
- **Criterios de aceptación**:
  1. Dado un periodo con datos, cuando la Directiva genera el reporte, entonces ve totales y
     detalle coherentes con los registros de asistencia.
  2. Dado un periodo sin datos, el PDF indica claramente que no existen registros.
- **Fuente**: F2-D-006, F7.
- **Debe validar**: Directiva y tesista.

### RF-REP-002 - Reporte de actividades y encargos

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva.
- **Descripción**: el sistema debe generar un reporte de actividades y encargos por periodo,
  estado, tipo y responsable, destacando pendientes.
- **Criterios de aceptación**:
  1. Dado un filtro válido, cuando se genera el reporte, entonces incluye las actividades y
     encargos correspondientes con su estado.
  2. Dado un elemento cancelado, entonces se distingue por texto y no solo por color.
- **Fuente**: F2-D-006, F5.
- **Debe validar**: Directiva y tesista.

### RF-REP-003 - Reporte de producción

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Encargada de producción según permiso.
- **Descripción**: el sistema debe generar un reporte de acopio, secado, lotes y mermas por
  periodo, producto y responsable.
- **Criterios de aceptación**:
  1. Dado un periodo con producción, cuando se genera el reporte, entonces sus totales se
     pueden rastrear hasta los registros operativos.
  2. Dada una gráfica, entonces muestra título, unidad, periodo y etiquetas comprensibles.
- **Fuente**: F2-D-006, F7.
- **Debe validar**: Directiva, encargadas y tesista.

### RF-REP-004 - Reporte de inventario y movimientos

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Tesorera.
- **Descripción**: el sistema debe generar un reporte de existencias y movimientos por
  producto, presentación, periodo, tipo de movimiento y responsable.
- **Criterios de aceptación**:
  1. Dado un producto, cuando se genera el reporte, entonces la existencia coincide con la suma
     de sus movimientos válidos.
  2. Dado un ajuste, entonces el reporte permite identificar motivo y responsable autorizado.
- **Fuente**: F2-D-006, F2-D-010.
- **Debe validar**: Tesorera, Directiva y tesista.

### RF-REP-005 - Reporte de ventas y cuentas por cobrar

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Actor**: Directiva y Tesorera.
- **Descripción**: el sistema debe generar reportes de ventas, valores base, excedentes,
  gastos, saldos y pagos, manteniendo separados los saldos de socias y clientes externos.
- **Criterios de aceptación**:
  1. Dado un periodo, cuando se genera el reporte, entonces cada total puede verificarse desde
     ventas, entregas, gastos o pagos registrados.
  2. Dado un saldo parcial, entonces el reporte muestra monto original, abonos y saldo restante.
- **Fuente**: F2-D-002, F2-D-006, F2-D-010.
- **Debe validar**: Tesorera, Directiva y tesista.

### RF-PUB-001 - Información pública para visitantes

- **Estado**: `proposed`.
- **Prioridad**: media.
- **Actor**: Visitante y Directiva editora.
- **Descripción**: el sistema debe ofrecer una página pública con información, imágenes y
  contacto expresamente aprobados por la organización.
- **Reglas**:
  - No muestra datos internos, saldos, producción detallada ni datos personales de socias.
  - No presenta afirmaciones de cumplimiento sanitario.
- **Criterios de aceptación**:
  1. Dado un visitante sin sesión, cuando abre el sitio, entonces consulta solo contenido
     público aprobado.
  2. Dado contenido interno, cuando se intenta acceder sin permiso, entonces no se muestra ni
     se incluye en la respuesta pública.
- **Fuente**: F1, F2-D-007, F2-D-009, F7.
- **Debe validar**: Directiva, organización y tesista.

### RF-PUB-002 - Administración de contenido público

- **Estado**: `proposed`.
- **Prioridad**: media.
- **Actor**: Directiva autorizada.
- **Descripción**: el sistema debe permitir preparar, actualizar, publicar o retirar el
  contenido público aprobado sin afectar los registros internos.
- **Reglas**:
  - Imágenes, identidad, contacto y textos requieren autorización de la organización.
  - Retirar contenido no elimina evidencia interna de quién realizó el cambio.
- **Criterios de aceptación**:
  1. Dado contenido aprobado, cuando una Directiva autorizada lo publica, entonces queda visible
     para visitantes.
  2. Dada una Socia operaria sin permiso editorial, cuando intenta publicar, entonces la
     operación se deniega.
- **Fuente**: F2-D-009, F5, F7.
- **Debe validar**: Directiva, organización y tesista.

---

## 8. Requisitos no funcionales transversales

### RNF-UX-001 - Uso sencillo y responsivo

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: los recorridos principales deben funcionar en móvil desde 360 px y en las
  dos computadoras de la organización, con una acción principal visible y controles táctiles
  amplios.
- **Verificación**: pruebas de los recorridos críticos en móvil y escritorio sin desplazamiento
  horizontal accidental; controles principales de aproximadamente 44 × 44 px.
- **Fuente**: F1, F2-D-008, F5.
- **Debe validar**: Socias, Directiva y tesista.

### RNF-UX-002 - Accesibilidad y mensajes comprensibles

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: la interfaz debe cumplir contraste AA, navegación por teclado, foco visible,
  zoom al 200 %, etiquetas persistentes y estados comunicados con texto además de color.
- **Verificación**: revisión de contraste, teclado, foco, zoom, errores y estados en cada flujo
  aprobado.
- **Fuente**: F5, Constitución.
- **Debe validar**: Tesista y usuarias en pruebas representativas.

### RNF-UX-003 - Lenguaje y carga cognitiva

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: la interfaz debe usar palabras del trabajo cotidiano, evitar mostrar permisos
  técnicos y solicitar únicamente los datos necesarios para la tarea actual.
- **Verificación**: las socias completan tareas representativas siguiendo etiquetas visibles,
  sin seleccionar roles ni realizar cálculos manuales.
- **Fuente**: F1, F2-D-005, F2-D-010, F5.
- **Debe validar**: Socias y tesista.

### RNF-CON-001 - Conectividad limitada y acceso externo

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: la aplicación debe poder utilizarse dentro y fuera de la organización y
  tolerar Internet inestable mediante páginas ligeras, errores recuperables y prevención de
  envíos duplicados.
- **Reglas**:
  - No se promete trabajo offline ni sincronización automática sin resolver Q3.
  - Una interrupción debe informar qué ocurrió y permitir reintentar de forma segura.
- **Verificación**: recorridos de consulta, venta y registro productivo bajo conexión limitada y
  recuperación después de una interrupción simulada.
- **Fuente**: F2-D-008, F5, F7.
- **Debe validar**: Socias, Directiva y tesista.

### RNF-SEC-001 - Autorización en operaciones sensibles

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: toda operación interna debe validar autorización en el sistema, aunque un
  botón o enlace no aparezca en la interfaz.
- **Verificación**: cada operación sensible tiene al menos una prueba permitida y una denegada;
  ninguna denegación modifica datos.
- **Fuente**: F2-D-004, F2-D-005, F6, Constitución.
- **Debe validar**: Directiva y tesista.

### RNF-AUD-001 - Historial de correcciones

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: las correcciones de asistencia, pesajes, lotes, inventario y excepciones de
  venta deben conservar usuario, fecha y hora, valor anterior, valor nuevo y motivo.
- **Verificación**: después de una corrección autorizada, el historial permite reconstruir ambos
  valores y no puede ser alterado por una Socia sin permiso.
- **Fuente**: F2-D-004, F2-D-010, F7.
- **Debe validar**: Directiva y tesista.

### RNF-DAT-001 - Integridad y trazabilidad de movimientos

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: operaciones que afectan varias cantidades o saldos deben completarse de
  forma íntegra; inventario, lotes, pesajes, ventas y pagos conservan movimientos verificables.
- **Verificación**: ante un error, ninguna parte de la operación queda aplicada; los saldos se
  pueden reconciliar desde sus movimientos y nunca son negativos sin una excepción aprobada.
- **Fuente**: F2-D-010, F6, Constitución.
- **Debe validar**: Tesorera, Directiva y tesista.

### RNF-PRV-001 - Privacidad y separación pública

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: el sistema debe recopilar solo datos personales necesarios y separar la
  información pública de la organizativa, productiva y financiera.
- **Verificación**: las páginas públicas no exponen información interna; reportes y evidencias
  omiten datos personales innecesarios y respetan permisos.
- **Fuente**: F2-D-007, F2-D-009, F6, Constitución.
- **Debe validar**: Directiva y tesista.

### RNF-PDF-001 - Claridad de reportes PDF

- **Estado**: `proposed`.
- **Prioridad**: alta.
- **Descripción**: los PDF deben incluir título, periodo, filtros, fecha de generación, datos
  legibles, gráficos comprensibles y el logo autorizado de Zhud Alelí.
- **Reglas**:
  - El logo debe provenir de un archivo autorizado.
  - Las gráficas muestran unidad, etiquetas y no dependen solo del color.
- **Verificación**: revisión visual en pantalla e impresión; comparación de totales con la
  fuente operativa y validación de comprensión con representantes de la organización.
- **Fuente**: F2-D-006, F5, F7.
- **Debe validar**: Directiva, organización y tesista.

---

## Preguntas críticas de validación

### Q1 - Flujo real de asistencia

[NEEDS CLARIFICATION: ¿quién registra inicialmente la asistencia y se necesitan entrada y
salida con hora, o basta un estado por actividad como presente/ausente/justificada?]

### Q2 - Catálogos y formación de lotes

[NEEDS CLARIFICATION: ¿cuál es la lista actual de plantas, materias primas, productos,
presentaciones y unidades, y qué reglas permiten combinar acopios o secados en un lote?]

### Q3 - Operación sin Internet y respaldos

[NEEDS CLARIFICATION: en una feria sin conexión, ¿es suficiente conservar el formulario y
reintentar cuando vuelva Internet, o es obligatorio registrar ventas totalmente offline y
sincronizarlas después; además, quién será responsable de los respaldos?]

## Supuestos controlados

- Las confirmaciones D-001 a D-010 respaldan las propuestas, pero la organización aún debe
  validar los recorridos reales.
- “Encargada” siempre se vincula a una actividad y periodo; no crea un cuarto perfil técnico.
- La fecha y hora del secado se generan automáticamente; un cambio posterior es una corrección.
- El excedente de venta pertenece a la socia, pero no se calcula una utilidad neta individual
  después de gastos mientras no exista otra regla confirmada.
- Los precios históricos conservan los valores aplicados al momento de la operación.
- La eliminación física de registros con historia no se asume; las reglas de retención se
  definirán por dominio durante el diseño.

## Criterios para concluir la Fase I

- Cada requisito aceptado tiene actor, fuente, regla y criterios verificables.
- Las tres preguntas críticas están resueltas o explícitamente diferidas con impacto conocido.
- Las representantes revisan los recorridos con ejemplos comprensibles.
- Los requisitos descartados conservan motivo y no pasan a `specs/`.
- Los requisitos aceptados se priorizan en el Product Backlog y luego se convierten, uno por
  funcionalidad, en especificaciones canónicas.

## Registro de validación

| Fecha | Participantes o rol | IDs revisados | Decisión | Cambios | Evidencia |
|---|---|---|---|---|---|
| Pendiente | — | — | — | — | — |
