---
title: Casos de uso — revisión del documento académico
type: requirement
status: proposed
id: PRO-CU-001
version: 0.2
date: 2026-09-28
task_id: CU-REVIEW-001
phase: Fase II
sprint: transversal
module: transversal
commit: pending
related:
  - "[[../../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack]]"
  - "[[../CAT-REQ-001]]"
  - "[[2026-09-28-diagramas-casos-de-uso]]"
  - "[[../../evidence/casos-de-uso/2026-09-28-analisis-coherencia]]"
  - "[[../../evidence/casos-de-uso/2026-09-28-factibilidad-aportada]]"
  - "[[../../bitacora/checkpoints/2026-09-28-revision-casos-de-uso]]"
  - "[[../../../specs/001-acceso-usuarias-internas/spec]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - estado/proposed
  - modulo/transversal
---

# Casos de uso — revisión del documento académico

## Estado y navegación

Se documentan los **21 casos del PDF de 25/09/2026** y las correcciones propuestas contra la
línea base. Esta nota es una propuesta de documentación, no una nueva aprobación de requisitos.
El PDF original permanece intacto. Las fichas siguientes son síntesis analíticas, no una
transcripción literal: «PDF» describe lo recibido; «Ajuste» identifica la redacción recomendada.

- [[2026-09-28-diagramas-casos-de-uso|Archivo de esquemas y diagramas]].
- [[../../evidence/casos-de-uso/2026-09-28-analisis-coherencia|Hallazgos, fuentes, cobertura y análisis Spec Kit]].
- [[../CAT-REQ-001|Catálogo aprobado]] y sus reglas incorporadas desde
  [[2026-07-22-catalogo-revisado-requisitos-r3|R3 histórico]]. Prevalecen los ajustes del catálogo.
- [[../../../specs/001-acceso-usuarias-internas/spec|SPEC-001]] solo cubre acceso básico;
  el conjunto de casos de negocio no pertenece íntegramente a esa entrega.

## Fuente y límites

Fuente local: [PDF académico](<F:/Software/8vo Semestre/Aplicaciones Informaticas II/Acero_Franklin_7402_CasosDeUso_Aplicaciones II.pdf>),
23 páginas. Su identificación y huella SHA-256 constan en el informe de evidencia.
La página 3 tiene espacios de fecha y firma sin completar: no acredita por sí sola aprobación.
La factibilidad citada fue aportada como texto por el tesista durante esta revisión y se registra
en [[../../evidence/casos-de-uso/2026-09-28-factibilidad-aportada|EVID-FACT-001]]. El tesista
exige guardar y sincronizar sin conexión. **Esta versión del diseño incorpora esa capacidad
como obligatoria**; [[../CAT-REQ-001|CAT-REQ-001 v1.1]] incorpora la actualización
versionada aprobada expresamente por el tesista el 2026-09-28. SPEC-001 conserva acceso básico en línea: no necesita
convertirse en una spec offline ni incluir operaciones de negocio. No se atribuye aprobación de la organización o directora a esta
instrucción ni se da por resuelto el detalle operativo de cada flujo.
El [[../../architecture/PLAN-DESDE-CERO|plan maestro]] ya contempla PWA como planificación
condicionada. Se conserva su puerta de especificación y pruebas por operación.

Para tiempo, presupuesto y stack, la referencia actualizada aportada después por el tesista
es [[../../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack|EVID-PLAN-002]]:
16 semanas, USD 2.869 y tecnologías Django/PostgreSQL/SSR/Bootstrap/PWA. Las pruebas
integradas offline están en S13–S14; la construcción se distribuye con los módulos.

## Actores y reglas comunes

| Actor | Interacción y límite |
|---|---|
| Visitante (ACT-01 del PDF) | Consulta contenido público aprobado; sin acceso a información interna. |
| Directiva (ACT-02) | Actor agrupador de presidenta, secretaria y tesorera; no concede todos los permisos a todos los cargos. P-01 delimita cada operación sensible. |
| Socia operaria (ACT-03) | Consulta lo propio y opera según autorizaciones vigentes. |
| Socia con encargo vigente | Contexto temporal de la socia, de producción o feria/venta, ligado a actividad, periodo y alcance; no es un cuarto rol permanente (D-005, RF-PLA-003). |
| Asamblea | Decide sobre pendientes de asistencia en el proceso organizativo; la Directiva registra el resultado. No se le atribuye una cuenta de aplicación. |
| Soporte técnico | Procedimiento técnico controlado de primera cuenta; no autoridad organizacional ni permiso ilimitado de negocio. |

Fuentes: [[../../00-inicio/01-decisiones-pendientes#D-005 - Perfiles reales|D-005]],
[[../CAT-REQ-001#Ajuste aprobado a RF-ASI-007|RF-ASI-007 ajustado]] y SPEC-001.
Los nombres de actores son papeles de interacción; sus atributos de identidad pertenecen al
modelo de datos. La matriz cargo/operación continúa pendiente fuera del acceso básico.

Para las propuestas de fichas se aplican estas garantías, aunque el PDF no las desarrolla:
autorización en servidor; denegación sin mutaciones; transacción en cambios de varias entidades;
correcciones con motivo e historial; mensajes sin éxito ficticio ante un corte de red; datos
personales mínimos. Son reglas de CAT-REQ-001, no nuevos requisitos introducidos aquí.

## Fichas de los 21 casos originales

### CU-ADM-01

**Consultar información pública** · PDF p. 9 · Actor: Visitante · Módulo `public_site`, S5.
Fuente: RF-PUB-001; RNF-PRV-001. Relación: CU-PUB-01 propuesto para la gestión editorial.

- **Disparador / precondición (PDF):** abrir la dirección pública; sitio disponible.
- **Curso normal (PDF):** entrar → cargar recursos → mostrar información y acceso → consultar o ir al inicio de sesión.
- **Resultado (PDF):** información pública visible, sin sesión autenticada.
- **Alternos (PDF):** recurso no cargado; conservar información disponible. Elegir acceso lleva a CU-ADM-02.
- **Ajuste:** retirar «Opcional» como señal de alcance: la capacidad está confirmada. Ocultar secciones y recursos sin aprobación; no mostrar datos internos ni afirmaciones sanitarias.
- **Aceptación propuesta:** sin sesión se ve solo contenido publicado; un recurso no aprobado no es accesible por su URL; no se crea sesión privada.
- **Pendiente:** P-12, contenido y publicadores; no impide documentar la estructura.

### CU-ADM-02

**Iniciar sesión** · PDF p. 10 · Actores: Directiva, Socia operaria · `accounts`, S1.
Fuente: RF-ACC-001.1, .2 y .5a; CA-ACC-001-01/02/03/08 de SPEC-001.

- **Disparador / precondición (PDF):** solicitar acceso; cuenta activa y sin sesión.
- **Curso normal (PDF):** solicitar credenciales → ingresarlas → validar cuenta → cargar permisos → abrir pantalla del perfil.
- **Resultado (PDF):** sesión autenticada con permisos del rol.
- **Alternos (PDF):** credenciales incorrectas; mensaje específico para cuenta inactiva; conexión requerida.
- **Ajuste:** usar rechazo equivalente para cuenta inexistente, inactiva y clave errónea. Cuenta activa es condición de éxito, no requisito para poder intentar el acceso. En SPEC-001, credencial temporal conduce al cambio obligatorio y cuenta normal al inicio básico; el dashboard de negocio se difiere.
- **Aceptación:** tres causas de rechazo indistinguibles en información; clave temporal no abre inicio ni URL privada de negocio; sin respuesta del servidor no se anuncia acceso confirmado.

### CU-ADM-03

**Cerrar sesión** · PDF pp. 10–11 · Actores: Directiva, Socia operaria · `accounts`, S1.
Fuente: RF-ACC-001.4; CA-ACC-001-05; contrato HTTP de SPEC-001.

- **Disparador / precondición (PDF):** elegir salir; sesión activa.
- **Curso normal (PDF):** solicitar salida → confirmar cuando corresponda → invalidar sesión → volver a zona pública o acceso.
- **Resultado (PDF):** no hay acceso privado hasta una nueva autenticación.
- **Alternos (PDF):** cancelar confirmación conserva sesión; conservar registros locales pendientes.
- **Ajuste:** para SPEC-001 volver al acceso; la salida es POST protegido y el retroceso no expone contenido privado. En el diseño PWA solicitado, conservar pendientes aislados por cuenta sin mostrarlos a otra usuaria; reconectar y autenticarse antes de enviarlos. La confirmación adicional no debe declararse obligatoria sin fuente UX. El cierre local sin red no prueba revocación de la sesión del servidor: ese alterno debe especificarse.
- **Aceptación:** sesión cerrada no se reutiliza; GET no cierra sesión; navegación atrás no revela contenido privado. Caducidad de 30 minutos es regla transversal, no un clic de la usuaria.

### CU-ADM-04

**Gestionar usuarios y permisos** · PDF p. 11 · Actor: Directiva autorizada · `accounts`, S1 posterior a SPEC-001.
Fuente: RF-ACC-002/003; RNF-AUD-001; P-01.

- **Disparador / precondición (PDF):** entrar a administración; sesión y permiso administrativo.
- **Curso normal (PDF):** consultar cuentas → crear o modificar → completar datos/rol → validar unicidad y permiso → confirmar → guardar.
- **Resultado (PDF):** cuenta creada, actualizada o desactivada con permisos efectivos.
- **Alternos (PDF):** denegar sin permiso; errores de integridad; cancelar sin cambios.
- **Ajuste:** separar como operaciones identificables membresía, activación/desactivación y asignación de cargo/permiso; conservar historia. No asumir que toda Directiva administra todo ni tratar encargos como roles permanentes.
- **Aceptación propuesta:** cuenta desactivada no accede, pero sus registros permanecen; cargo incorrecto y encargo vencido no autorizan; cambios sensibles auditados.
- **Pendiente:** P-01 y spec propia; no añadir esta administración a SPEC-001.

### CU-OFF-01

**Registrar operación esencial sin conexión** · PDF p. 12 · Actores: Directiva, Socia operaria.
**Estado: obligatoria en el diseño solicitado por el tesista el 28/09; integración canónica pendiente.**

- **Disparador / precondición (PDF):** corte de red en una función habilitada; PWA y recursos en caché disponibles.
- **Curso normal (PDF):** detectar ausencia de conexión → cargar caché → completar → validar localmente → guardar en IndexedDB → mostrar pendiente.
- **Resultado (PDF):** registro local pendiente, todavía no persistido en servidor.
- **Alternos (PDF):** función no habilitada, datos inválidos o almacenamiento no disponible impiden guardar.
- **Contraste histórico:** RF-OFF-001/002/003 siguen `superseded` en CAT-REQ-001; la nueva factibilidad y la instrucción del tesista exigen revisar esa exclusión. No retirar este caso de los diagramas nuevos.
- **Ajuste propuesto:** conservar operación identificable y propietaria de la cuenta, tipo de registro, datos mínimos y momento capturado; estado «Guardado en este dispositivo, pendiente de enviar». Solo el servidor confirma la operación de negocio. Reabrir la PWA debe permitir recuperar el pendiente.
- **Aceptación propuesta:** corte antes/después de guardar, recarga y fallo de almacenamiento nunca producen éxito falso; otra cuenta no accede a la cola; registro local inválido no se encola. No guardar credenciales en la cola.
- **Pendientes de detalle:** lista cerrada de operaciones (la fuente nombra asistencia y pesajes), duración de habilitación offline, reloj, protección/retención local y datos precargados. No se presume venta, despacho o abono offline.

### CU-OFF-02

**Sincronizar registros pendientes** · PDF pp. 12–13 · Actores declarados: Directiva, Socia operaria.
**Estado: obligatoria en el diseño solicitado**, ligada a CU-OFF-01 y a una spec propia de sincronización.

- **Disparador / precondición (PDF):** el sistema detecta retorno de red; hay registros locales.
- **Curso normal (PDF):** leer pendientes → enviar por tipo/orden → validar respuesta → marcar aceptados o revisión → usuaria consulta el estado.
- **Resultado (PDF):** aceptados persistidos centralmente; rechazados identificados.
- **Alternos (PDF):** nuevo corte conserva pendientes; rechazo conserva revisión; cola vacía no cambia datos.
- **Ajuste de modelado:** conservar CU-OFF-02 como sincronización supervisable por la usuaria; retorno de conexión dispara el proceso y una acción visible permite reintentar/consultar. El mecanismo automático no se modela como actor externo.
- **Curso propuesto:** comprobar conexión efectiva → requerir autenticación si venció → enviar operación con ID estable → servidor revalida permisos, datos y dependencias → aplicar cambio, auditoría y resultado idempotente en transacción → confirmar recepción → actualizar estado local. No enviar identidad libre para suplantar a otra cuenta.
- **Aceptación propuesta:** si se pierde el acuse y se reenvía el mismo ID, existe un solo efecto; rechazo no desaparece ni figura aceptado; permiso revocado no permite aplicar el cambio; error revierte toda la operación. La cola distingue pendiente, enviando, sincronizado y requiere revisión.
- **Pendientes de detalle:** criterio de conflictos, orden entre registros relacionados, reintentos, revocación, hora capturada frente a hora del servidor y eliminación local segura. Debe existir reintento con la app abierta aunque el navegador no admita sincronización en segundo plano.

### CU-PLA-01

**Gestionar actividades programadas** · PDF pp. 13–14 · Actor: Directiva autorizada · `planning`, S2.
Fuente: RF-PLA-001; RNF-AUD-001.

- **Disparador / precondición:** crear, editar o cancelar actividad; sesión y permiso.
- **Curso normal (PDF):** abrir listado → elegir acción → completar programación → validar → guardar.
- **Resultado:** actividad creada/actualizada o conservada como cancelada.
- **Alternos:** errores conservan edición; cancelar requiere confirmación; abandonar no guarda.
- **Ajuste:** explicitar actividad e instancia, fecha/hora, lugar, responsable, participantes, estado y motivo de cancelación. La planificación productiva de cantidades/insumos se desarrolla en CU-PLA-05.
- **Aceptación propuesta:** error conserva campos válidos; cancelación conserva motivo e historia; planificar no genera stock ni lote.

### CU-PLA-02

**Asignar responsabilidades** · PDF p. 14 · Actor: Directiva autorizada · `planning`, S2.
Fuente: RF-PLA-002; relación con RF-PLA-003 y CU-PLA-04.

- **Disparador / precondición:** asignar personas a una actividad existente y disponible; permiso de planificación.
- **Curso normal (PDF):** elegir actividad → mostrar socias → seleccionar responsables → revisar resumen → confirmar → guardar asignación.
- **Resultado:** personas vinculadas a la actividad.
- **Alternos:** actividad no disponible, selección vacía o cancelación.
- **Ajuste:** distinguir responsable y participantes; impedir asignación a cuenta inactiva. Un encargo temporal agrega periodo y alcance y no se agota en esta asociación. Quitar la relación «uses» con CU-PLA-01: la actividad existente es precondición, no obligación de gestionarla de nuevo.
- **Aceptación propuesta:** cada participante consulta solo su alcance; una cuenta inactiva se rechaza sin asignación parcial.

### CU-PLA-03

**Consultar actividades asignadas** · PDF pp. 14–15 · Actores: Directiva, Socia operaria · `planning`, S2.
Fuente: RF-PLA-004; RF-ACC-004 como navegación futura.

- **Disparador / precondición:** abrir planificación; sesión activa.
- **Curso normal (PDF):** identificar alcance → listar actividades → seleccionar una → presentar detalle autorizado.
- **Resultado:** consulta sin modificación.
- **Alternos:** estado vacío; acceso fuera del alcance denegado.
- **Ajuste:** precisar filtros por periodo, estado, responsable y participación, sin convertir el rol en una elección del formulario.
- **Aceptación propuesta:** una socia no obtiene otra asignación por manipular la URL; consulta vacía ofrece explicación; los filtros mantienen el alcance autorizado.

### CU-ASI-01

**Registrar asistencia** · PDF pp. 15–16 · Actores: Directiva, Socia operaria · `attendance`, S3.
Fuente: RF-ASI-001/002/007; prevalece el ajuste de RF-ASI-007 en CAT-REQ-001.

- **Disparador / precondición (PDF):** registrar presencia; sesión y actividad habilitada.
- **Curso normal (PDF):** seleccionar actividad → determinar entrada/salida → confirmar → guardar hora → confirmar resultado.
- **Resultado:** evento de entrada o salida registrado.
- **Alternos (PDF):** sin actividad, evento duplicado o CU-OFF-01 ante corte.
- **Ajuste:** distinguir instancia y acción; QR temporal por fase, código alternativo y registro delegado con ambas personas y motivo. Una salida olvidada queda pendiente; no se inventa su hora. El nuevo alterno offline enlaza CU-OFF-01/02 y debe diferenciar captura provisional de evento aceptado. La regla previa de hora del servidor no permite considerar el reloj local como hora verificada de presencia.
- **Aceptación propuesta:** QR vencido, repetido o de otra acción no cambia datos; doble entrada y salida sin entrada se rechazan; origen propio/delegado identificable.
- **Pendiente:** P-02 (vigencia, apertura de fases y delegación) y política explícita de QR, hora y presencia durante desconexión; no resolverla aceptando automáticamente tokens vencidos al reconectar.

### CU-ASI-02

**Validar participación** · PDF p. 16 · Actor declarado: Directiva · `attendance`, S3.
Fuente relacionada: RF-ASI-003/005/006; el objetivo del PDF necesita precisarse.

- **Disparador / precondición (PDF):** revisar registros de una actividad; sesión, permiso y datos.
- **Curso normal (PDF):** mostrar integrantes/eventos → revisar → seleccionar → confirmar → marcar validación.
- **Resultado:** presencia validada o pendiente.
- **Alternos:** registros incompletos, cancelación o falta de permiso.
- **Ajuste propuesto:** denominar «Registrar resolución de pendientes de asistencia». La asamblea decide; Directiva registra resultado, referencia a asamblea, actor, fecha, motivo y cambios. No asumir facultad unilateral para convertir faltantes en justificados/injustificados. Corrección de datos y participación adicional son CU-ASI-04/05.
- **Aceptación propuesta:** pendiente permanece pendiente sin resolución; no hay sanción automática; resultado reconstruible.
- **Pendiente:** distinguir validación rutinaria de resolución organizativa; P-03 afecta sanciones, no el registro básico.

### CU-ASI-03

**Consultar historial de participación** · PDF pp. 16–17 · Actores: Directiva, Socia operaria · `attendance`, S3.
Fuente: RF-ASI-004; RNF-PRV-001.

- **Disparador / precondición (PDF):** consultar historial; sesión y existencia de datos.
- **Curso normal:** aplicar alcance → elegir periodo/criterio → recuperar eventos y estados → presentar.
- **Resultado:** historial visible sin modificarlo.
- **Alternos:** periodo sin registros; consulta de otra socia denegada.
- **Ajuste:** quitar «existen datos» de la precondición para permitir el estado vacío; mostrar pendientes y correcciones autorizadas de forma comprensible, diferenciando asistencia de participación adicional.
- **Aceptación propuesta:** socia ve solo su historial; Directiva según cargo; filtros no amplían permisos.

### CU-TRA-01

**Registrar acopio de materia prima** · PDF p. 17 · Actor: Socia operaria autorizada · `traceability`, S4.
Fuente: RF-TRA-001; RNF-AUD-001; P-04.

- **Disparador / precondición:** ingresar materia prima; sesión y autorización productiva.
- **Curso normal (PDF):** seleccionar socia y materia → ingresar peso → validar positivo → confirmar → guardar.
- **Resultado:** entrega asociada a socia y peso, disponible para trazabilidad.
- **Alternos:** peso inválido, cancelación o registro offline.
- **Ajuste:** completar unidad, fecha, valoración, responsable y observación según requisito; quien registra no necesariamente es quien entrega. No interpretar valoración desconocida como cero. El pesaje sin red queda provisional en CU-OFF-01 y se confirma con CU-OFF-02; resolver catálogos precargados y referencias todavía no sincronizadas.
- **Aceptación propuesta:** peso no positivo no persiste; unidad y origen se conservan; corrección autorizada conserva antes/después y motivo.

### CU-TRA-02

**Registrar seguimiento de secado** · PDF p. 18 · Actor: Socia autorizada/encargo de producción · `traceability`, S4.
Fuente: RF-TRA-002/003 y D-003.

- **Disparador / precondición:** iniciar o finalizar secado; material disponible y permiso.
- **Curso normal (PDF):** seleccionar acopio → confirmar peso/inicio → guardar activo → abrir al finalizar → registrar peso final → calcular duración/merma → cerrar.
- **Resultado (PDF):** tiempos y pesajes disponibles; merma cuando hay ambos pesos.
- **Alternos:** peso inicial/final inválido o interrupción con CU-OFF-01.
- **Ajuste:** inicio/fin automáticos con hora del servidor; peso inicial/final y un valor de temperatura Celsius obligatorios; humedad opcional. Merma absoluta y duración calculadas con fórmula/unidad; porcentaje espera redondeo aprobado. Peso final mayor exige revisión/excepción, no merma normal silenciosa.
- **Aceptación propuesta:** cierre sin temperatura válida no se confirma; error conserva secado abierto; no recrear acopio durante el secado ni ejecutar «include» por una relación de datos. Inicio/cierre offline requiere política para distinguir hora capturada y recibida; no calcular duración usando tiempos incompatibles.

### CU-TRA-03

**Registrar manufactura y lote** · PDF pp. 18–19 · Actor: Socia autorizada/encargo de producción · `traceability`, S4.
Fuente: RF-TRA-004/005; RF-INV-002; RNF-DAT-001; P-04/P-05.

- **Disparador / precondición:** transformar materiales; sesión, autorización e insumos disponibles.
- **Curso normal (PDF):** elegir línea e insumos → ingresar cantidades/resultados → validar disponibilidad → confirmar → generar lote/linaje → actualizar inventario.
- **Resultado:** lote vinculado a insumos y unidades resultantes.
- **Alternos:** datos incompletos, insuficiencia o cancelación impiden confirmar.
- **Ajuste:** composición/version, consumos, residuos, responsable, fecha y rendimiento; consumos y producto se aplican atómicamente. Cierre productivo no equivale a agotamiento. Mezcla física crea lote derivado; un pedido con varios lotes no los fusiona. Productos editoriales no necesitan secado.
- **Aceptación propuesta:** fallo revierte lote y movimientos; cada resultado permite recorrer orígenes; no consume dos veces por reintento.

### CU-TRA-04

**Gestionar inventario de bodega** · PDF pp. 19–20 · Actor declarado: Socia con permiso · `traceability`, S4.
Fuente: RF-INV-002; RNF-DAT-001; D-004.

- **Disparador / precondición:** consultar inventario; sesión y permiso.
- **Curso normal (PDF):** mostrar existencias → seleccionar elemento → ver saldo/movimientos → registrar movimiento si ocurre manufactura/despacho → verificar actualización.
- **Resultado:** existencias y movimientos trazables.
- **Alternos:** saldo vacío, existencia inválida o falta de permiso.
- **Ajuste:** renombrar objetivo consultivo a «Consultar existencias y movimientos». Sacar el paso 5 del recorrido de lectura: las operaciones origen generan sus movimientos al confirmarse. Ajustes/correcciones son otra acción autorizada (CU-TRA-08), nunca edición libre del total.
- **Aceptación propuesta:** abrir inventario no muta datos; existencia concilia con movimientos; un error de operación origen revierte todo.

### CU-TRA-05

**Registrar despacho** · PDF p. 20 · Actor: Socia con autorización de entrega · `traceability`, S4.
Fuente: RF-INV-003/004; RF-CXC-001; P-01/P-09.

- **Disparador / precondición:** entregar productos; sesión, autorización y disponibilidad.
- **Curso normal (PDF):** seleccionar destino/socia y productos → cantidades → validar stock → generar salida → dejar saldo disponible si corresponde → confirmar.
- **Resultado:** despacho y salida de inventario.
- **Alternos:** stock insuficiente, cancelación o despacho sin cuenta por cobrar.
- **Ajuste:** identificar encargo, receptora, lote y modo individual/compartido; registrar confirmación o diferencia de recepción. Distinguir traslado de custodia y retiro individual impago al valor base congelado; custodia compartida no genera deuda personal. No representar el despacho como una venta.
- **Aceptación propuesta:** no sobreentrega; origen visible; saldo físico separado del monetario; cuenta pagada no genera deuda. Efectos de devoluciones esperan P-09.

### CU-TRA-06

**Gestionar cuentas por cobrar** · PDF pp. 20–21 · Actor: Directiva autorizada · ámbito comercial, S4.
Fuente: RF-CXC-001/002; RF-VEN-002/003; D-010; P-09.

- **Disparador / precondición (PDF):** revisar saldos; permiso y despachos con deuda.
- **Curso normal (PDF):** listar cuentas → seleccionar → actualizar saldo/estado → validar → confirmar → guardar.
- **Resultado:** nuevo estado asociado al despacho.
- **Alternos:** sin pendientes, valor inconsistente o falta de permiso.
- **Ajuste:** separar deuda de socia y deuda externa de clientes; consultar saldos derivados. Para reducirlos, registrar abono como movimiento con monto, fecha/hora, forma, responsable y saldo destino (CU-CXC-01). No introducir un saldo editable directo. Cobrar después no «extiende» la ejecución del despacho.
- **Aceptación propuesta:** abono afecta solo cuenta elegida y conserva historia; sobrepago no se aplica silenciosamente; consulta vacía válida. P-09 debe cerrar ajustes excepcionales.

### CU-TRA-07

**Consultar trazabilidad de lote** · PDF pp. 21–22 · Actores: Directiva, Socia autorizada · `traceability`, S4.
Fuente: RF-TRA-004/005; RF-INV-002/003.

- **Disparador / precondición (PDF):** buscar lote; sesión y registros trazables.
- **Curso normal:** escoger criterio → recuperar etapas relacionadas → ordenar → presentar según permisos.
- **Resultado:** historial consultado sin modificarlo.
- **Alternos:** no encontrado, etapa inexistente o dato restringido.
- **Ajuste:** admitir búsqueda vacía sin exigir datos previos; preservar linaje, mezcla física, consumos y movimientos sin inventar etapas. No todo producto sigue acopio/secado; no exponer saldos ajenos mediante la consulta técnica.
- **Aceptación propuesta:** consulta recorre todos los orígenes disponibles; etapas faltantes explícitas; autorización controla detalle y URL directa.

### CU-REP-01

**Consultar dashboard** · PDF p. 22 · Actor declarado: Directiva · `reports`, S5; inicio operativo relacionado con S1.
Fuente relacionada: RF-ACC-004; RF-GAS-002 y RF-REP-001 a 006 según contenido.

- **Disparador / precondición:** abrir panel; sesión y permiso de información consolidada.
- **Curso normal (PDF):** verificar permiso → consolidar → presentar indicadores → seleccionar → mostrar detalle.
- **Resultado:** resumen actualizado sobre registros existentes.
- **Alternos:** módulo vacío, acceso denegado o conexión requerida.
- **Ajuste:** enumerar cada indicador con fórmula, unidad, periodo y fuente antes de implementarlo. Separar este panel del inicio de bienvenida de SPEC-001 y del resumen privado de cada socia (CU-REP-03). «Indicadores relevantes» no es aceptación verificable.
- **Aceptación propuesta:** totales concilian con sus fuentes; sin datos se distingue ausencia de información de un cero real; cada detalle respeta permisos.

### CU-REP-02

**Generar reportes consolidados** · PDF p. 23 · Actor: Directiva autorizada por cargo · `reports`, S5.
Fuente: RF-REP-001 a 005; RNF-PDF-001; D-006.

- **Disparador / precondición (PDF):** pedir reporte; permiso y datos para algún criterio.
- **Curso normal:** elegir tipo/filtros → validar → consolidar → mostrar → revisar o cambiar criterios.
- **Resultado (PDF):** reporte presentado sin alterar registros fuente.
- **Alternos:** filtro inválido, sin registros o sin conexión.
- **Ajuste:** aceptar periodos vacíos; explicitar asistencia, actividades/encargos, producción, inventario y ventas/cuentas por cobrar. Añadir descarga PDF con título, periodo, filtros, fecha, unidades, logo autorizado y totales conciliados; el diseño concreto de gráficos permanece pendiente. El resumen de socia necesita su propio acceso.
- **Aceptación propuesta:** pantalla y PDF corresponden al mismo filtro y datos; saldos separados; no se filtra información no autorizada ni se presenta una certificación contable/sanitaria.

## Descomposición propuesta de capacidades ausentes

Los siguientes **15 IDs nuevos son propuestas de organización del diseño**. Sus capacidades
fuente ya están documentadas, pero estos IDs y su agrupación no están aprobados. No se usan
para declarar cubierto el PDF original. Cada ficha futura ampliará curso normal, alternos,
permisos y pruebas; las reglas aún pendientes no se rellenan por inferencia.

| ID propuesto | Objetivo, actor y resultado esperado | Fuente / límite |
|---|---|---|
| CU-ADM-05 | Cambiar contraseña propia. Usuaria con sesión presenta clave actual, nueva y confirmación; cambio válido sustituye la credencial, cambio inválido no muta. Credencial temporal obliga a completar este recorrido antes del inicio. | SPEC-001 RF-ACC-001.5/.5a, CA-06/07/08; T029–T032. |
| CU-ADM-06 | Consultar inicio personal. Usuaria ve bienvenida y, según incremento, opciones reales; sin sesión se deniega. | SPEC-001 RF-ACC-001.6: solo cambiar contraseña/salir. RF-ACC-004 es ampliación futura para actividades, pendientes y encargos. |
| CU-PLA-04 | Gestionar encargo temporal. Directiva autorizada define actividad, persona, periodo y alcance; al cerrar o vencer se deniegan nuevas operaciones del encargo. | RF-PLA-003; P-01. |
| CU-PLA-05 | Planificar producción semanal. Persona autorizada define fecha, producto, objetivo e insumos previstos; asignadas consultan; cambios conservan actor/fecha y no generan stock. | RF-PLA-005; unidades sujetas a P-04. |
| CU-ASI-04 | Corregir asistencia. Directiva o Encargada autorizada corrige con motivo e historial; perfil indebido no cambia datos. | RF-ASI-003; RNF-AUD-001; P-01. |
| CU-ASI-05 | Registrar participación adicional. Persona autorizada registra tipo validado, socia y actividad únicamente cuando aporta algo distinto de la asistencia. | RF-ASI-005; tipos pendientes de validación. |
| CU-CAT-01 | Mantener catálogo y valores históricos. Directiva/Tesorera autorizada gestiona unidades, presentaciones y valores con vigencia; desactivar conserva historia y cambiar precio no altera ventas previas. | RF-CAT-001; RF-INV-001; P-01/P-04. |
| CU-TRA-08 | Registrar ajuste o corrección productiva. Directiva/Encargada autorizada registra motivo, cambio y movimiento aplicable; se conserva original y operación atómica. | RF-INV-002; RF-TRA-001; RNF-AUD-001/DAT-001; P-05/P-09. |
| CU-VEN-01 | Registrar venta. Encargada con stock autorizado vende varias líneas con precios/base históricos, comprador proporcional y forma de pago; se aplica completa o se revierte. Tesorera registra venta organizacional. | RF-VEN-001 a 007; P-01/P-07/P-08. Subflujos pendientes para excepciones bajo base, políticas y venta organizacional. |
| CU-CON-01 | Registrar comprobante de contingencia. Persona autorizada digita folio, momento real, momento de digitación, actor y motivo; folio duplicado no descuenta de nuevo y conflicto queda por revisar. | RF-VEN-008; RNF-CON-001; P-10. Comprobante manual fuera del sistema y digitación con conexión. |
| CU-CXC-01 | Registrar abono. Directiva/Tesorera autorizada elige uno de los dos tipos de saldo, ingresa monto/fecha/forma/responsable y confirma; el movimiento reduce solo ese saldo. | RF-CXC-001/002; P-09 para sobrepago y ajustes. |
| CU-CXC-02 | Conciliar encargo y rendición. Encargada y Directiva/Tesorera según permisos comparan recibido, transferido, vendido, devuelto, sobrante, dinero/base/excedente; diferencias quedan por conciliar. | RF-INV-004; RF-CXC-003; P-07/P-09. |
| CU-GAS-01 | Registrar gastos y consultar resumen. Tesorera registra categoría, monto, fecha, concepto y lote/periodo; Directiva autorizada consulta fuentes y pendientes; sin balance certificado. | RF-GAS-001/002; fórmula de costo completo RF-COS-001 sigue proposed. |
| CU-REP-03 | Consultar resumen propio y recordatorios. Socia ve asistencia, actividades, productos, montos, crédito externo y excedente separados; recordatorio abre registro autorizado. | RF-REP-006; RF-NOT-001; no mostrar datos ajenos. Puede descomponerse durante su spec. |
| CU-PUB-01 | Preparar, aprobar, publicar y retirar contenido. Persona autorizada sigue el flujo editorial y conserva historial; publicador indebido se deniega. | RF-PUB-002; P-01/P-12. |

La creación/entrega de primera cuenta y la caducidad de sesión también se documentan como
procedimiento técnico y regla transversal en SPEC-001. No se convierten artificialmente en
funciones de una Directiva con permisos aún no definidos.

## Orden de corrección propuesto

1. Integrar la factibilidad aportada y la exigencia de offline en una actualización trazable del catálogo; precisar operaciones, reloj, autorización y conflictos, conservando CU-OFF-01/02 como obligatorios en el diseño solicitado.
2. Alinear CU-ADM-02/03 y añadir CU-ADM-05/06 con SPEC-001.
3. Precisar asistencia, autoridad de asamblea, encargos y correcciones.
4. Completar secado, movimientos, ventas, dos tipos de deuda y abonos.
5. Completar reportes PDF, resumen individual, contenido público y sus permisos.
6. Revisar las fichas y diagramas por módulo; solo después preparar una versión académica para validación.

Las propuestas ya están concretadas para revisión. La promoción a versión aprobada necesita
evidencia humana según la constitución; esta sesión no ejecuta tareas de Django ni modifica
las specs, el catálogo aprobado, el PDF fuente o la matriz global.

## Enlace a la reconciliación integral

La [[../../evidence/casos-de-uso/2026-09-28-coherencia-integral|auditoría integral]] comprueba
los 57 IDs aprobados y corrige los resúmenes de módulos. La
[[2026-09-28-catalogo-v1-1|revisión v1.1]] relaciona CU-OFF-01/02 con RF-PWA-001/002/003
confirmados en el catálogo; define el cambio de RNF-CON-001 y los pendientes P-13/P-14. No hereda validaciones
de julio. La tabla de cobertura del PDF original permanece como análisis histórico del PDF,
no como afirmación de ausencia en estas fichas ampliadas.

## Aprobación de los requisitos fuente

[[../../evidence/casos-de-uso/2026-09-28-aprobacion-requisitos-v1-1|EVID-REQ-APP-001]] registra
la aprobación del tesista. Los 60 requisitos son fuente vigente; las fichas y los esquemas
siguen siendo artefactos de diseño sujetos a sus propias revisiones, no pruebas ejecutadas.
