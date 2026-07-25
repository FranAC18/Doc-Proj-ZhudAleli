---
title: Catálogo de requisitos R3 para validación humana
type: requirement
status: superseded
id: CAT-REQ-001-R3
supersedes: CAT-REQ-001-R2
superseded_by: "[[../CAT-REQ-001]]"
created: 2026-07-22
updated: 2026-07-22
phase: Fase I
sprint: transversal
priority: high
module: transversal
validated_by:
  - Tesista
  - Organización
  - Presidenta
recommended_promotion: accepted-with-adjustments
related:
  - "[[../CAT-REQ-001]]"
  - "[[2026-07-22-catalogo-revisado-requisitos]]"
  - "[[2026-07-21-catalogo-inicial-requisitos]]"
  - "[[../../00-inicio/01-decisiones-pendientes]]"
  - "[[../../sprints/ROADMAP-ANTEPROYECTO]]"
  - "[[../../architecture/ARQUITECTURA-OBJETIVO]]"
  - "[[../../ui/SISTEMA-DISENO]]"
  - "[[../../traceability/MATRIZ-TRAZABILIDAD]]"
  - "[[../../evidence/fase-i/2026-07-22-respuestas-tesista-cat-req-001-r3]]"
  - "[[../../evidence/fase-i/2026-07-22-validacion-cat-req-001-v1]]"
  - "[[../../bitacora/checkpoints/2026-07-22-catalogo-r3-para-validacion]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - estado/superseded
  - sprint/fase-i
---

# CAT-REQ-001-R3 - Catálogo para validación humana

## Propósito y control humano

Esta revisión integra CAT-REQ-001, R2, las respuestas entregadas por el tesista el
2026-07-22 y tres revisiones independientes en lectura: requisitos, arquitectura y UX.
Presenta una recomendación única para una organización comunitaria con conectividad
inestable, presupuesto limitado y sin personal técnico permanente.

Al prepararse, todo el documento mantenía estado `proposed`. La columna **Recomendación**
indicaba qué se consideraba suficientemente definido para someterlo a confirmación humana,
pero no cambiaba por sí sola el estado del requisito.

El 2026-07-22 esta revisión fue validada con ajustes por el tesista, la organización y la
presidenta. R3 queda `superseded` como antecedente congelado; la decisión vigente y el estado
por ID están en [[../CAT-REQ-001|CAT-REQ-001 v1.0]].

La validación de este catálogo no autoriza todavía modelos, migraciones, código Django,
integraciones externas ni implementación. Habilita la creación posterior de specs únicamente
para los IDs confirmados.

## Clases de fuente

| Clase | Autoridad |
|---|---|
| A | Anteproyecto, contexto y decisiones D-001 a D-010 confirmadas |
| B | Respuestas del tesista recibidas el 2026-07-22; falta evidencia de validación organizativa |
| C | Recomendación integrada de requisitos, arquitectura o UX |
| D | Decisión exclusiva de la organización todavía pendiente |

Fuentes concretas:

- **F1**: `agents/tesis/PROJECT_CONTEXT.md` y anteproyecto.
- **F2**: decisiones D-001 a D-010.
- **F3**: evaluación de documentos previos.
- **F4**: roadmap oficial de sprints.
- **F5**: sistema de diseño y restricciones UX.
- **F6**: arquitectura objetivo y Constitución.
- **F7**: catálogo inicial CAT-REQ-001.
- **F8**: catálogo revisado CAT-REQ-001-R2.
- **F9**: [[../../evidence/fase-i/2026-07-22-respuestas-tesista-cat-req-001-r3|respuestas del tesista del 2026-07-22]].

Si una fuente B o C contradice evidencia de campo confirmada, prevalece la evidencia de campo
y la discrepancia se documenta. Una propuesta de bajo costo no se convierte automáticamente
en práctica aprobada.

## Recomendación única para la organización

1. Construir una aplicación principalmente en línea, renderizada por Django y ligera en
   móviles; no implementar sincronización offline automática en la primera versión.
2. Registrar entrada y salida mediante dos fases QR temporales supervisadas por la secretaria,
   con hora del servidor, confirmación de la socia y alternativa delegada auditable.
3. Marcar faltantes o inconsistencias como pendientes y resolverlos colectivamente en
   asamblea, sin ventana automática de tres días ni sanciones automáticas.
4. Conservar los perfiles organizativos Directiva, Socia operaria y Visitante. Los cargos y encargos otorgan permisos limitados; la administración organizacional no es un bypass técnico.
5. Separar al Administrador técnico del gobierno de la organización. No decide reglas de negocio ni corrige datos ordinarios mediante Django Admin o SQL.
6. Registrar inventario, lotes, entregas, ventas, devoluciones, pagos y ajustes mediante
   movimientos; nunca reemplazar la historia con totales editables.
7. Distinguir lote productivo cerrado de lote comercialmente agotado. Solo una mezcla física  crea un lote derivado; atender un pedido desde varios lotes conserva orígenes sin fusionarlos.
8. Admitir stock individual y compartido en feria, identificando el origen en cada línea de
   venta. No repartir automáticamente el excedente compartido sin fórmula aprobada.
9. Separar custodia física, deuda de una socia, cuenta por cobrar de clientes y excedente
   bruto. Ninguno debe mostrarse como un único “saldo”.
10. Ante falta de Internet, usar comprobante manual identificable y registro tardío auditado.
    No prometer operación offline ni sincronización que la organización no necesita mantener.
11. Registrar consumos y costos directos conocidos, pero etiquetar el costo como parcial mientras mano de obra, energía, transporte y gastos compartidos sigan sin regla.
12. Publicar solo historia, misión, visión, productos, ubicación, redes y contacto expresamente aprobados, sin datos internos ni afirmaciones sanitarias.
13. Proponer respaldo automático diario de base y archivos, retención mínima de 30 días y restauración trimestral; la política definitiva y sus responsables deben validarse.

## Correcciones materiales respecto de R2

| Tema | R2 | Recomendación R3 |
|---|---|---|
| Asistencia | QR opcional y flujo aún ambiguo | QR temporal para entrada y salida como propuesta principal, sin considerarlo prueba infalible |
| Pendientes | Ventana de tres días y escalamiento individual | Sin plazo automático; revisión y resolución en asamblea |
| Corrección | El técnico podía ejecutar correcciones aprobadas | Directiva o Encargada dentro de D-004; técnico fuera del flujo ordinario |
| Administración | Administrador técnico añadido como actor | Autoridad organizacional dentro de Directiva y soporte técnico separado |
| Feria | Preferencia por stock individual | Stock individual y compartido desde la primera versión |
| Sin Internet | Cola local y sincronización idempotente | Comprobante manual y registro tardío auditable |
| Lote | Cierre asociado a venta total | Cierre productivo separado de agotamiento comercial |
| Costo | Costo calculado sin fórmula completa | Costo directo registrado y marcado como parcial |
| Saldo | Custodia física y deuda todavía mezclables | Eventos físicos y monetarios separados |
| Admin/SQL | Se sugirió usar Django Admin con auditoría | Interfaces de negocio; Admin y SQL solo para mantenimiento o recuperación excepcional |

## Actores y límites propuestos

| Actor o contexto | Alcance |
|---|---|
| Directiva | Perfil organizativo. Sus cargos obtienen únicamente permisos definidos en la matriz pendiente |
| Presidenta | Cargo de Directiva; posible responsable de administración organizacional, sujeto a validación |
| Tesorera | Cargo de Directiva para valores base, gastos, pagos, descuentos y reportes financieros autorizados |
| Secretaria | Cargo de Directiva propuesto para actividades, fases QR y registro delegado de asistencia |
| Socia operaria | Consulta información propia y registra operaciones permitidas por su participación o encargo |
| Encargada de producción | Asignación temporal limitada a acopio, secado, transformación o lote de su encargo |
| Encargada de feria | Asignación temporal limitada a productos, ventas, devoluciones y rendición de su feria |
| Responsable de administración organizacional | Atribución dentro de Directiva; no es `is_superuser` ni permite edición libre |
| Administrador técnico | Cuenta de soporte separada; mantiene servicio y respaldos sin decidir negocio |
| Asamblea | Actor colectivo que decide pendientes y futuras sanciones; una persona autorizada registra el acuerdo |
| Visitante | Consulta únicamente contenido público aprobado |

Reglas transversales:

- Toda autorización se verifica en backend por perfil, cargo, encargo, objeto, periodo y
  operación; ocultar un botón no concede ni revoca permiso.
- Ningún actor operativo recibe el bypass `is_superuser` de Django.
- Un registro operativo publicado se corrige, revierte o ajusta conservando el original,
  autorización, valores, actor, fecha y motivo.
- SQL directo queda limitado a recuperación excepcional con aprobación, copia previa,
  procedimiento documentado y conciliación posterior.

## Requisitos candidatos a confirmación humana

Todos los IDs de esta sección siguen en `proposed`. La recomendación `confirmar` significa “presentar para decisión humana en esta ronda”.

### Administración y acceso — Sprint 1

| ID         | Actor y problema                                           | Regla propuesta                                                                                              | Criterios mínimos                                                                               | Fuente | Recomendación                       |
| ---------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ------ | ----------------------------------- |
| RF-ACC-001 | Usuaria interna necesita acceso seguro                     | Cuenta activa inicia/cierra sesión y accede solo a lo autorizado                                             | Credenciales válidas permiten acceso; inválidas o cuenta inactiva se rechazan sin filtrar datos | A      | confirmar                           |
| RF-ACC-002 | Directiva necesita administrar membresía                   | Crear, actualizar, activar o desactivar sin borrar historia                                                  | Socia sin permiso recibe denegación; desactivar impide acceso y conserva registros              | A      | confirmar                           |
| RF-ACC-003 | Personas necesitan funciones según perfil, cargo y encargo | Mantener Directiva, Socia y Visitante; cargos y encargos limitan operaciones; soporte técnico queda separado | Cargo incorrecto, encargo vencido y URL directa se deniegan sin mutación                        | A+C    | confirmar con matriz pendiente P-01 |
| RF-ACC-004 | Cada usuaria necesita un inicio comprensible               | Mostrar actividades, pendientes y encargos vigentes, no nombres técnicos de permisos                         | Con encargo vigente aparecen acciones permitidas; sin encargo no aparecen ni funcionan          | A      | confirmar                           |

**Fuera de alcance:** recuperación de contraseña por un canal externo y matriz definitiva de
permisos hasta resolver P-01.

### Planificación — Sprint 2

| ID         | Actor y problema                                                         | Regla propuesta                                                                                                | Criterios mínimos                                                                      | Fuente | Recomendación              |
| ---------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- | ------ | -------------------------- |
| RF-PLA-001 | Directiva necesita organizar jornadas y eventos                          | Registrar actividad, instancia, fecha, hora, lugar, responsable, participantes, estado y motivo de cancelación | Datos válidos crean la actividad; error conserva datos y explica corrección            | A      | confirmar                  |
| RF-PLA-002 | Socias necesitan conocer responsabilidad y participación                 | Asignar responsable, participantes y alcance de cada persona                                                   | Cuenta inactiva no recibe asignación; cada participante ve lo que le corresponde       | A      | confirmar                  |
| RF-PLA-003 | Una socia puede asumir trabajo temporal                                  | Encargo de producción o feria con actividad, periodo, alcance y cierre                                         | Solo permite operaciones del encargo vigente; al cerrar se deniegan nuevas operaciones | A      | confirmar                  |
| RF-PLA-004 | Directiva y socias necesitan consultar pendientes                        | Filtrar por periodo, estado, responsable y participación                                                       | Cada socia ve solo lo propio; conjunto vacío muestra explicación                       | A      | confirmar                  |
| RF-PLA-005 | La producción semanal necesita previsión sin crear existencias ficticias | Planificar fecha, producto, cantidad objetivo, responsables e insumos previstos                                | Plan aparece a asignadas; cambiarlo conserva actor/fecha; no crea stock ni lotes       | B+C    | confirmar con organización |

### Asistencia y participación — Sprint 3

| ID         | Actor y problema                                          | Regla propuesta                                                                                                                                      | Criterios mínimos                                                                                             | Fuente | Recomendación                 |
| ---------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------ | ----------------------------- |
| RF-ASI-001 | Socia necesita registrar presencia por instancia          | Conservar entrada y salida con hora del servidor y origen propio o delegado                                                                          | Rechazar doble entrada, salida sin entrada y salida anterior; delegado identifica a ambas personas            | A+B    | confirmar                     |
| RF-ASI-002 | La organización necesita registros coherentes             | Unicidad por socia, instancia y tipo de evento; inconsistencias quedan pendientes                                                                    | Duplicado muestra registro existente; salida olvidada no inventa hora                                         | A+C    | confirmar                     |
| RF-ASI-003 | Registros sensibles requieren corrección controlada       | Directiva o Encargada autorizada corrige con motivo e historial conforme D-004                                                                       | Perfil no autorizado no modifica; antes/después, actor, fecha y motivo son reconstruibles                     | A      | confirmar                     |
| RF-ASI-004 | Socia y Directiva necesitan historial                     | Socia ve solo su historial; Directiva consulta según cargo y periodo                                                                                 | Filtros y estados son comprensibles; no se exponen datos de otras socias                                      | A      | confirmar                     |
| RF-ASI-005 | Algunas actividades requieren describir participación     | Registrar tipos pocos y validados solo cuando aporten información distinta de asistencia                                                             | Actividad simple no exige participación; registro queda vinculado a socia y actividad                         | A      | confirmar                     |
| RF-ASI-006 | Faltantes deben resolverse sin proceso individual costoso | Acumular pendientes; asamblea decide justificada, injustificada, corregida o pendiente; Directiva registra cada resultado                            | Pendiente no se convierte solo en falta; decisión conserva asamblea, actor, fecha, motivo y cambios           | B+C    | confirmar con organización    |
| RF-ASI-007 | Autorregistro debe ser rápido en celulares básicos        | Secretaria abre fases QR distintas para entrada y salida; token temporal no contiene datos personales; existe código alternativo y registro delegado | Token vencido, repetido o de otra acción no modifica; cada socia confirma su evento; delegado registra motivo | B+C    | confirmar con parámetros P-02 |

**Fuera de alcance:** geolocalización, visión artificial, considerar el QR prueba concluyente y
sanciones automáticas.

### Catálogo, producción e inventario — Sprint 4

| ID         | Actor y problema                                                      | Regla propuesta                                                                                                                                    | Criterios mínimos                                                                                               | Fuente | Recomendación                       |
| ---------- | --------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------- | ------ | ----------------------------------- |
| RF-CAT-001 | Directiva y Tesorera necesitan catálogos históricos                   | Separar planta, materia prima, insumo, empaque, producto, presentación y unidad; desactivar no borra historia                                      | Elemento desactivado no se usa en operaciones nuevas; historia conserva nombre y unidad                         | B+C    | confirmar con datos pendientes P-04 |
| RF-INV-001 | Catálogo comercial requiere valores vigentes e históricos             | Conservar presentación, costo conocido, precio sugerido, precio vigente y valor base con vigencia                                                  | Cambiar un valor no altera ventas anteriores; producto inactivo no entra en nuevas ventas                       | A      | confirmar                           |
| RF-TRA-001 | El acopio necesita origen y peso                                      | Registrar socia, materia, peso/cantidad, unidad, fecha, valoración, responsable y observación                                                      | Peso no positivo se rechaza; corrección queda auditada                                                          | A+B    | confirmar                           |
| RF-TRA-002 | El secado necesita datos mínimos reales                               | Registrar peso inicial/final, temperatura Celsius, humedad opcional e inicio/fin automáticos                                                       | Inicio usa hora del servidor; cierre exige peso final y temperatura válidos                                     | A      | confirmar                           |
| RF-TRA-003 | La organización necesita duración y merma sin cálculo manual          | Calcular duración y merma absoluta; porcentaje solo cuando se apruebe redondeo                                                                     | Muestra fórmula y unidad; peso final mayor exige revisión o excepción autorizada                                | A      | confirmar                           |
| RF-TRA-004 | Lotes necesitan linaje y estados no ambiguos                          | Crear lote por producción; cerrar al finalizar y confirmar rendimiento; agotado se deriva del stock; mezcla física crea lote derivado con orígenes | Orígenes son recorribles; mezcla incompatible se rechaza; pedido de varios lotes no reescribe ni fusiona origen | A+B+C  | confirmar con excepciones P-05      |
| RF-TRA-005 | La transformación no debe quedar implícita                            | Registrar entradas consumidas, composición/version, resultado, cantidad, residuos, responsable, fecha y lote                                       | Cantidades incompatibles se rechazan; producto resultante enlaza todos sus consumos                             | A+C    | confirmar con organización          |
| RF-INV-002 | Las existencias necesitan evidencia                                   | Toda entrada, consumo, producción, asignación, venta, devolución y ajuste produce movimiento                                                       | Movimiento cambia exactamente la existencia; ajuste exige permiso y motivo; operación atómica                   | A      | confirmar                           |
| RF-INV-003 | Entregas de feria necesitan origen y responsabilidad                  | Identificar encargo, socia, producto, lote, cantidad y modo individual o compartido                                                                | No excede stock; receptora confirma o reporta diferencia; origen permanece visible                              | A+B    | confirmar                           |
| RF-INV-004 | Productos físicos necesitan conciliación                              | Calcular recibido + transferido - vendido - devuelto - retorno; separar este saldo de deuda monetaria                                              | Diferencia queda por conciliar; no se oculta ni crea stock negativo                                             | A+C    | confirmar                           |
| RF-COS-001 | La organización necesita conocer costos sin recibir un total engañoso | Registrar consumos y costos directos; marcar cálculo parcial si existen entradas sin valoración o componentes no decididos                         | Insumo no valorado no equivale a cero; reporte enumera incluidos y excluidos                                    | B+C+D  | mantener pendiente P-06             |

#### Catálogo inicial para validar

| Categoría | Producto o variante | Tratamiento propuesto |
|---|---|---|
| Shampoo | Atuk sara, cebolla, romero y quinua | Producto elaborado con variantes |
| Acondicionador | Romero | Producto elaborado |
| Horchata o kit de hierbas “Zhud Alelí” | Mezcla de plantas indicada por la organización | Requiere nombre definitivo, receta/versiones y eliminar “otras” como dato abierto |
| Mashua seca | Sin variante informada | Producto elaborado/seco |
| Tónico capilar | Romero y cebolla | Producto elaborado con variantes |
| Libro de recetas “Zhud Alelí” | Producto editorial | Inventario comercial sin flujo de acopio/secado |
| Kit por contrato | Composición específica del pedido | Versión de composición vinculada al contrato, sin alterar la versión estándar |

Unidades informadas: gramos y mililitros. Continúan pendientes unidad, envase, kit, libro,
kilogramo y conversiones necesarias para compra, producción y venta.

### Ventas, gastos, saldos y rendición — Sprint 4

| ID         | Actor y problema                                   | Regla propuesta                                                                                                                         | Criterios mínimos                                                                                    | Fuente | Recomendación                          |
| ---------- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------ | -------------------------------------- |
| RF-VEN-001 | Socia encargada necesita registrar ventas simples  | Venta multiproducto desde stock autorizado con cantidad, precio, total y forma de pago                                                  | Total se calcula; no permite cantidad superior al stock; operación se aplica completa o no se aplica | A      | confirmar                              |
| RF-VEN-002 | La venta necesita comprador proporcional al riesgo | Contado usa Público general; crédito/institución exige identificación mínima aprobada                                                   | Crédito sin comprador se rechaza; contado no solicita datos innecesarios                             | A      | confirmar                              |
| RF-VEN-003 | Organización y socia necesitan separar valores     | Congelar valor base y calcular excedente bruto; no llamarlo utilidad neta                                                               | Venta conserva precio aplicado y base históricos; muestra ambos importes                             | A      | confirmar                              |
| RF-VEN-004 | Precio bajo base requiere control excepcional      | Exigir autorización previa o posterior según contingencia, motivo y auditoría                                                           | Venta normal bajo base se rechaza; excepción identifica autorizador y diferencia                     | A      | confirmar                              |
| RF-VEN-005 | Tesorera necesita políticas por volumen            | Configurar umbral, precio o porcentaje, producto/presentación, vigencia y autoridad                                                     | Sin política completa no aplica descuento; precio bajo base usa excepción                            | B+D    | mantener pendiente P-08                |
| RF-VEN-006 | Feria multisocia necesita trazabilidad             | Admitir líneas desde stock individual o compartido; fuente queda fijada por línea                                                       | Resultado individual no se mezcla; compartido acumula excedente sin repartir automáticamente         | B+C    | confirmar con reparto pendiente P-07   |
| RF-VEN-007 | La organización realiza ventas grandes propias     | Venta organizacional usa stock general, la gestiona Tesorera y no atribuye excedente a una socia                                        | Tipo y responsable quedan claros; no usa fórmula de reparto individual                               | B+C    | confirmar con organización             |
| RF-VEN-008 | Pérdida de Internet no debe perder ventas          | Comprobante manual único y registro tardío con momento real, momento de digitación, actor y motivo                                      | Folio duplicado no descuenta dos veces; conflicto de stock queda por revisar                         | B+C    | confirmar con operación pendiente P-10 |
| RF-GAS-001 | Tesorera necesita registrar gastos                 | Registrar categoría, monto, fecha, concepto, lote/periodo y responsable                                                                 | Monto inválido se rechaza; edición sensible queda auditada                                           | A      | confirmar                              |
| RF-GAS-002 | Directiva necesita resumen entendible              | Mostrar ingresos organizacionales, gastos, pendientes y fórmula, sin presentarlo como balance certificado                               | Totales enlazan fuente y periodo; gasto sin clasificación queda visible                              | A      | confirmar                              |
| RF-CXC-001 | Deben separarse custodia y dos tipos de deuda      | Retiro individual impago crea deuda al valor base congelado; custodia compartida no crea deuda individual; deuda externa queda separada | Retiro pagado no crea deuda; abono afecta solo saldo elegido; eventos físicos no se mezclan          | A+B+C  | confirmar con devoluciones P-09        |
| RF-CXC-002 | Se necesitan pagos parciales                       | Registrar monto, fecha/hora, forma, responsable y saldo aplicado                                                                        | Abono válido reduce saldo; sobrepago se rechaza o queda pendiente según regla futura                 | A      | confirmar                              |
| RF-CXC-003 | Feria necesita rendición verificable               | Mostrar recibido, vendido, devuelto, sobrante, dinero, base, excedente y diferencias                                                    | Discrepancia deja encargo por conciliar y explica qué falta                                          | A      | confirmar                              |

### Reportes, recordatorios y sitio público — Sprint 5

| ID | Actor y problema | Regla propuesta | Criterios mínimos | Fuente | Recomendación |
|---|---|---|---|---|---|
| RF-REP-001 | Directiva necesita reporte de asistencia | Filtrar por periodo, actividad y socia; mostrar estados y correcciones autorizadas | Totales coinciden con registros; periodo sin datos se explica | A | confirmar |
| RF-REP-002 | Directiva necesita actividades y encargos | Filtrar por estado, tipo, responsable y periodo | Pendientes son visibles; permisos limitan detalle | A | confirmar |
| RF-REP-003 | Directiva necesita producción trazable | Resumir acopio, secado, transformación, lotes y merma con unidades y origen | Totales enlazan movimientos; no oculta entradas sin valoración | A | confirmar |
| RF-REP-004 | Directiva necesita inventario y movimientos | Mostrar existencia derivada y movimientos por producto, lote y periodo | Existencia concilia con movimientos; ajustes se identifican | A | confirmar |
| RF-REP-005 | Tesorera necesita ventas y cuentas por cobrar | Separar ventas, deuda de socias, deuda externa, pagos y pendientes | Ningún saldo se mezcla; filtros y fórmulas son visibles | A | confirmar |
| RF-REP-006 | Cada socia necesita su resumen privado | Separar asistencia, actividades, productos, monto a entregar, créditos de clientes y excedente bruto | No muestra datos de otras socias ni llama ganancia neta al excedente | A+C | confirmar con prueba de comprensión |
| RF-NOT-001 | Usuarias necesitan recordar tareas dentro del sistema | Mostrar recordatorios internos de actividades, asistencia, encargos, rendiciones y registros tardíos | Recordatorio abre el elemento correcto; no depende de correo o mensajería | C | confirmar con organización |
| RF-PUB-001 | Visitante necesita información pública | Publicar solo historia, misión, visión, productos, ubicación, redes y contacto aprobados | Sección no aprobada permanece oculta; no expone información interna o sanitaria | A+B | confirmar con contenido pendiente P-12 |
| RF-PUB-002 | Organización necesita controlar publicaciones | Flujo preparar, aprobar, publicar y retirar según permiso | Publicador no autorizado se deniega; retirada no borra historial | A+C | confirmar con matriz P-01 |

### Requisitos no funcionales transversales

| ID          | Regla propuesta                                               | Verificación mínima                                                                      | Fuente | Recomendación           |
| ----------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ------ | ----------------------- |
| RNF-UX-001  | Móvil desde 360 px, acciones claras y formularios cortos      | Sin desplazamiento horizontal accidental; tareas críticas en dispositivos reales         | A+C    | confirmar               |
| RNF-UX-002  | Contraste AA, teclado, foco, etiquetas y errores recuperables | Zoom 200 %, foco visible, resumen de errores y controles táctiles de al menos 44 px      | A+C    | confirmar               |
| RNF-UX-003  | Lenguaje cotidiano y cálculos automáticos                     | Socias completan recorridos sin elegir roles ni calcular fórmulas manuales               | A+C    | confirmar               |
| RNF-CON-001 | Operación ligera y principalmente en línea                    | Sin fuentes remotas obligatorias; caída informa recuperación; no duplica envíos          | A+C    | confirmar               |
| RNF-SEC-001 | Autorización backend en operaciones sensibles                 | Cada operación tiene prueba permitida y denegada; denegación no muta datos               | A      | confirmar               |
| RNF-AUD-001 | Correcciones, aprobaciones y excepciones reconstruibles       | Conserva original, cambio/reversión, actor, fechas, autorización y motivo                | A+C    | confirmar               |
| RNF-DAT-001 | Operaciones multi-entidad atómicas y basadas en movimientos   | Error revierte todo; no hay sobreventa ni saldo negativo silencioso                      | A+C    | confirmar               |
| RNF-PRV-001 | Minimización de datos y separación pública                    | Sitio público y reportes no exponen datos internos innecesarios                          | A      | confirmar               |
| RNF-PDF-001 | PDF claro, trazable y no dependiente solo del color           | Incluye título, periodo, filtros, fecha, unidades, logo autorizado y totales conciliados | A      | confirmar               |
| RNF-OPS-001 | Copias protegidas y restauración demostrable                  | Copia de BD/archivos, retención y prueba de restauración con acceso autorizado           | B+C+D  | mantener pendiente P-11 |

## Decisiones y requisitos que permanecen pendientes

Estos elementos no deben promoverse a `confirmed` ni bloquear la confirmación de módulos no
relacionados.

| ID | Decisión pendiente | Pregunta exacta para la organización | Bloquea |
|---|---|---|---|
| P-01 / RN-ACC-001 | Matriz cargo por operación | ¿Qué pueden crear, corregir, aprobar, pagar, publicar y consultar presidenta, tesorera, secretaria y cada Encargada? ¿Qué acceso puntual puede tener soporte técnico? | Specs de permisos y operaciones sensibles |
| P-02 / RN-ASI-002 | Parámetros del QR y delegación | ¿Confirman dos eventos, entrada y salida, qué duración tendrá cada QR, quién abre cada fase y en qué casos la secretaria registra por otra socia? | Detalle de RF-ASI-007 |
| P-03 / RN-ASI-001 | Sanciones por faltas | ¿Cuántas faltas activan qué consecuencia y la decide la asamblea caso por caso o una regla automática? | Solo sanciones; no bloquea asistencia básica |
| P-04 / RN-CAT-001 | Presentaciones y unidades completas | ¿Cuáles son tamaños, unidades de compra/venta y conversiones? ¿Horchata y kit son el mismo producto? ¿Cuál es la lista cerrada de plantas? | Catálogo y fórmulas de producción |
| P-05 / RN-TRA-001 | Excepciones de lotes | ¿Qué compatibilidades permiten mezclar o dividir y cómo se registran bajas, mermas o cierres excepcionales? | RF-TRA-004 completo |
| P-06 / RF-COS-001 | Fórmula de costo | ¿Cómo se valoran plantas propias y trabajo comunitario? ¿Se incluyen mano de obra, energía, transporte y gastos compartidos y cómo se asignan? | Costo completo y reportes económicos |
| P-07 / RN-VEN-001 | Reparto de excedente compartido | ¿Se reparte por partes iguales, porcentajes, ventas realizadas u otra regla y quién la aprueba? | Distribución; no bloquea registrar ventas |
| P-08 / RF-VEN-005 | Descuentos por volumen | Para cada presentación, ¿cuál es umbral, precio o porcentaje, vigencia y límite respecto del valor base? | Aplicación automática de descuentos |
| P-09 / RN-CXC-001 | Devoluciones, pérdidas y deuda | ¿Una devolución reduce la deuda al valor base? ¿Qué ocurre con daño, pérdida, baja, anulación y sobrepago? | Ajustes del saldo de socia |
| P-10 / RN-CON-001 | Operación de contingencia | ¿Aceptan comprobante manual sin sincronización automática? ¿Quién numera, custodia, digita y verifica y cuál es la demora máxima? | RF-VEN-008 y procedimiento de feria |
| P-11 / RNF-OPS-001 | Política de respaldo | ¿Quién responde y quién opera? ¿Aceptan copia diaria, 30 días y restauración trimestral? ¿Proveedor, RPO/RTO y quién autoriza restaurar? | Despliegue productivo |
| P-12 / RN-PUB-001 | Contenido público final | ¿Quién aprueba/publica y cuáles textos, imágenes, dirección, redes y teléfono están autorizados? | Publicación final; no bloquea estructura |

## Capacidades diferidas o excluidas de la primera versión

- `RF-OFF-001`, `RF-OFF-002` y `RF-OFF-003` de R2: PWA, cola local y sincronización
  automática. Permanecen en backlog y solo se reabren si la contingencia manual falla en una
  validación real.
- Sanciones automáticas y efectos económicos mientras P-03 siga pendiente.
- Agente autónomo de WhatsApp, SMS o mensajería sin proveedor, consentimiento y presupuesto.
- Geolocalización y visión artificial como prueba de presencia.
- Facturación electrónica, contabilidad tributaria y afirmaciones de cumplimiento sanitario.
- Distribución de utilidad neta individual sin fórmula aprobada.
- Edición ordinaria de negocio mediante Django Admin o SQL.

## Invariantes para diseño posterior

1. Cada operación sensible tiene un caso permitido y uno denegado.
2. La auditoría se guarda dentro de la misma transacción que el cambio.
3. Las existencias se derivan de movimientos; no existe un total editable sin respaldo.
4. Una venta multiproducto se aplica completa o se revierte completa.
5. Costo, valor base, precio sugerido y precio aplicado son conceptos distintos e históricos.
6. Un insumo sin valoración produce costo parcial, nunca costo cero silencioso.
7. Lote cerrado y lote agotado son estados distintos.
8. El QR no contiene datos personales y tokens vencidos o de otra acción no modifican datos.
9. Registro delegado identifica quién actuó por quién y el motivo.
10. Registro tardío conserva folio, momento real, momento de digitación, actor y origen.
11. La interfaz separa productos en custodia, deuda propia, deuda de clientes y excedente.
12. El sitio público no publica una sección ni un recurso sin aprobación.

## Criterios UX que deben validarse con usuarias

- Desde 360 px no existe desplazamiento horizontal accidental.
- Entrada y salida pueden completarse con cámara, código alternativo o respaldo delegado.
- Código vencido, salida olvidada y registro duplicado explican qué ocurrió y cómo continuar.
- Una feria muestra “Mi stock” y “Stock compartido” con texto, no solo color.
- Un resultado de red incierto invita a buscar por folio antes de repetir una venta.
- Los formularios conservan datos válidos después de un error.
- El reporte individual explica quién debe qué a quién y en qué unidad.
- Cada flujo tiene estado vacío, error, éxito y recuperación.
- Los recorridos se prueban con Directiva, Socia, Encargada y Visitante en dispositivos reales.

## Propuesta presentada para decisión humana (histórica)

Esta sección conserva la recomendación que se presentó antes de la validación. El resultado
humano fue distinto: 57 requisitos `confirmed`, 2 `proposed` y 12 `superseded`, con un ajuste
a `RF-ASI-007`. La fuente vigente es [[../CAT-REQ-001|CAT-REQ-001 v1.0]].

### Promoción recomendada

Después de una validación con participantes y evidencia identificados, promover únicamente
los IDs aceptados de la sección “Requisitos candidatos a confirmación humana” a un catálogo
canónico `CAT-REQ-001`. Los requisitos que remiten a P-01 a P-12 pueden confirmarse solo en
su parte explícitamente delimitada; la regla pendiente no se hereda como aprobada.

CAT-REQ-001 canónico deberá contener por cada ID una decisión: `confirmed`, `discarded`,
`superseded` o `proposed`. El contenedor no debe ocultar elementos pendientes bajo un estado
global ambiguo.

Si la validación humana acepta R3 sin ajustes, el lote recomendado queda delimitado así:

- Promover a `confirmed` los 56 IDs de las tablas de requisitos candidatos, excepto
  `RF-COS-001`, `RF-VEN-005` y `RNF-OPS-001`.
- Mantener en `proposed` esos tres IDs y las nueve reglas aún no resueltas:
  `RN-ACC-001`, `RN-ASI-001`, `RN-ASI-002`, `RN-CAT-001`, `RN-TRA-001`, `RN-VEN-001`,
  `RN-CXC-001`, `RN-CON-001` y `RN-PUB-001`.
- Marcar `RF-OFF-001`, `RF-OFF-002` y `RF-OFF-003` como `superseded` para la primera
  versión por `RNF-CON-001`, `RF-VEN-008` y la contingencia manual. Una futura capacidad
  offline requerirá evidencia de necesidad y una nueva validación.
- Conservar la relación P-01 a P-12 para que cada pendiente tenga pregunta, impacto y
  alcance identificados. Los requisitos confirmados que mencionan una P se aprueban solo
  con el límite ya escrito en su regla y criterio; no aprueban la decisión pendiente.

El resultado recomendado sería, por tanto, un CAT-REQ-001 canónico con 56 requisitos
`confirmed`, 12 requisitos o reglas `proposed` y 3 requisitos `superseded`, no una
aprobación global que oculte excepciones o decisiones históricas.

### Respuesta mínima de validación

Registrar una respuesta equivalente a:

```text
Fecha:
Participantes y roles:
Fuente o acta:

Confirmados:
Ajustados:
Descartados:
Permanecen pendientes: P-01 ... P-12

Si se acepta R3 sin ajustes:
Confirmados: los 56 candidatos, excepto RF-COS-001, RF-VEN-005 y RNF-OPS-001.
Permanecen proposed: RF-COS-001, RF-VEN-005, RNF-OPS-001, RN-ACC-001,
RN-ASI-001, RN-ASI-002, RN-CAT-001, RN-TRA-001, RN-VEN-001, RN-CXC-001,
RN-CON-001 y RN-PUB-001.
Superseded para v1: RF-OFF-001, RF-OFF-002 y RF-OFF-003.

Autorizo preparar CAT-REQ-001 canónico con estos resultados: sí/no.
```

Si la revisión la realiza únicamente el tesista, debe indicarse. Las reglas que requieren a
la organización continúan `proposed` hasta registrar su validación correspondiente.

## Registro de validación

| Fecha | Participantes/rol | IDs revisados | Decisión | Evidencia |
|---|---|---|---|---|
| 2026-07-22 | Tesista; organización; presidenta | CAT-REQ-001-R3 | Aceptado con ajustes y sustituido por CAT-REQ-001 v1.0 | [[../../evidence/fase-i/2026-07-22-validacion-cat-req-001-v1]] |

## Criterio de salida de Fase I

- Cada ID promovido tiene actor, fuente, regla, aceptación, límites, objetivo y sprint.
- Las decisiones que cambien D-004, D-005 o el anteproyecto se registran humanamente.
- La matriz enlaza la evidencia exacta de validación.
- Los pendientes conservan ID, pregunta, impacto y responsable de resolverlos.
- Solo los confirmados pasan a specs por funcionalidad.
- La aprobación del catálogo no se presenta como aprobación de diseño o implementación.
