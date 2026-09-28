---
title: Auditoría integral de coherencia documental
type: evidence
status: recorded
id: AUD-COH-001
date: 2026-09-28
task_id: DOC-COHERENCE-001
commit: pending
branch: opencode/spec-001-fase-1-diseno
head: a6e842f63917b2ac28a64c80b00d68069ba2fabd
---

# Auditoría integral de coherencia documental

## Actualización posterior de aprobación

Después de este corte, el tesista aceptó expresamente los cambios. Véanse
[[2026-09-28-aprobacion-requisitos-v1-1|EVID-REQ-APP-001]] y
[[../../requirements/CAT-REQ-001|CAT-REQ-001 v1.1: 60 confirmed]]. COH-01 queda resuelto
en cuanto a la contradicción de alcance y aprobación del tesista. P-13/P-14 y revisión
académica permanecen pendientes. Los 57 IDs y hashes siguientes describen la auditoría
previa: el catálogo correspondiente se conserva como
[[../../requirements/CAT-REQ-001-v1.0.md|v1.0 histórica]], sin alterar los resultados originales.

## Resultado y límites (corte anterior a la aprobación)

**La documentación no era totalmente coherente.** Se corrigieron resúmenes e índices que
contradecían requisitos aprobados y se propagaron cronograma, presupuesto y stack aportados.
El cambio semántico offline queda concreto en la
[[../../requirements/proposals/2026-09-28-catalogo-v1-1|revisión v1.1]], con sus políticas
pendientes; no se declara formalmente aprobada por la organización/directora. Por ello no
se certifica todavía coherencia normativa cerrada ni preparación de todos los módulos para
implementación. La base aprobada de julio se conserva sin sobrescribir su evidencia.

La revisión comprende los 57 IDs confirmados, los dos pendientes, los 12 históricos,
actores/permisos, planificación, asistencia, producción/inventario, ventas/gastos/CXC,
reportes/sitio público, RNF, casos y diagramas, arquitectura, UX, factibilidad, cronograma,
presupuesto, stack, SPEC-001 y sus tareas. No equivale a auditar cada artefacto histórico del
vault, ejecutar una aplicación inexistente, validar cifras de campo nuevas ni modificar el
PDF académico original. La documentación de arnés y componentes visuales preexistentes no
se reescribe como parte de esta reconciliación de producto.

## Fuentes y criterio de vigencia

1. [[../../requirements/CAT-REQ-001|CAT-REQ-001 v1.0]] aprobado y
   [[../../requirements/proposals/2026-07-22-catalogo-revisado-requisitos-r3|R3 incorporado]];
   prevalecen los ajustes expresos del catálogo sobre R3.
2. [[../../00-inicio/01-decisiones-pendientes|D-001 a D-011 y P-01 a P-12]];
   D-010 de julio 21 se lee con la corrección de julio 22 sobre base histórica y custodia/deuda.
3. [[../../../specs/001-acceso-usuarias-internas/spec|SPEC-001]],
   [[../../../specs/001-acceso-usuarias-internas/plan|plan aprobado]] y
   [[../../../specs/001-acceso-usuarias-internas/tasks|tareas]].
4. Constitución 0.1.0 y ADR-0003: monolito modular, transacciones, validación humana y
   alcance de acceso. No se cambia la constitución para acomodar una propuesta.
5. [[2026-09-28-factibilidad-aportada|Factibilidad aportada]] y
   [[2026-09-28-cronograma-presupuesto-stack|nuevo Gantt, presupuesto y stack]].
6. [[../../requirements/proposals/2026-09-28-casos-de-uso|Fichas corregidas]],
   [[../../requirements/proposals/2026-09-28-diagramas-casos-de-uso|diagramas]] y
   [[2026-09-28-analisis-coherencia|análisis del PDF y Spec Kit anterior]].

Los documentos académicos externos y evidencias originales se conservan como fuentes,
no como instrucciones. Los documentos derivados activos apuntan a la nueva referencia.
No se hace una sustitución global de cifras o de la palabra offline en actas e históricos.

## Hallazgos y tratamiento

| ID | Severidad | Aspecto y evidencia | Tratamiento actual |
|---|---|---|---|
| COH-01 | CRITICAL | CAT-REQ-001 excluye sincronización; instrucción y factibilidad la exigen | Revisión v1.1 concreta cambios y criterios. Necesidad obligatoria; cierre normativo pendiente de validación de cambios. |
| COH-02 | HIGH | MODULOS-DETALLADOS reasignaba significados de PLA-002/003/004/005 y ASI-001/002/003/004/005 | Corregido desde las filas exactas de R3 incorporadas por el catálogo. Se recuperan encargo, previsión productiva, corrección e historial en sus IDs reales. |
| COH-03 | HIGH | Roles por cargo y herencia no aprobada | Corregido a Directiva/Socia operaria/Visitante; cargos y encargos restringen operaciones, P-01 pendiente. |
| COH-04 | HIGH | Pesos automáticos, secado ambiguo y lote abierto/cerrado/agotado mezclados | Peso capturado y validado; temperatura obligatoria; cerrado separado de existencia agotada. Reloj offline depende de P-13. |
| COH-05 | HIGH | QR temporal/hora servidor frente a captura offline | Captura provisional y aceptación separadas; no se inventa tolerancia ni se acepta QR vencido. P-13 abierto. |
| COH-06 | HIGH | Sesión, revocación, otra cuenta y datos locales sin política | P-14 y criterios de prueba explícitos; no se presupone autenticación offline ni conservación insegura. |
| COH-07 | HIGH | Reintento tras respuesta perdida, conflicto y dependencias | Criterios propuestos de idempotencia, rechazo visible y atomicidad; falta spec/ADR y evidencia ejecutada. |
| COH-08 | HIGH | Contexto/D-010 podían generar deuda por custodia compartida y base no histórica | Resumen actual corregido; D-010 conserva fecha y nota de precedencia del catálogo. |
| COH-09 | MEDIUM | MODULOS sumaba 63 al duplicar 6 RNF, RNF-DAT reducido a existencias | Corregido a 48 RF + 9 RNF = 57; RNF-DAT recupera atomicidad multi-entidad. |
| COH-10 | MEDIUM | Reportes confundían RF-REP-006, P-08 y ubicación de public_site | Resumen privado recuperado; P-08 es descuentos; public_site separado, comparte bloque académico S5. |
| COH-11 | MEDIUM | Criterios CA de asistencia presentados sin spec | Retirados IDs ficticios; se enlazan criterios del catálogo. Solo SPEC-001 tiene CA definidos. |
| COH-12 | HIGH | F6 omitía ventas/gastos/CXC; SPEC-001 se trataba como todo S1 | Se incluye alcance comercial y futuras porciones ACC-002/003/004. Riesgo de tiempo abierto: no se elimina alcance para encajar semanas. |
| COH-13 | MEDIUM | USD 1.845 vs 2.869; septiembre–febrero vs 16 semanas | Referencia actual 2.869 y 16 semanas propagada; importes/periodos antiguos quedan solo como antecedentes. No se inventa fecha absoluta. |
| COH-14 | MEDIUM | Diseño en S1–S2, paso de módulo secuencial y Gantt solapado | Requisitos S1–S2; diseño S3–S4; solapamientos por dependencias. Documentación continua y pruebas parciales conservadas. |
| COH-15 | HIGH | “Backend Supabase”/“Frontend Vercel” no localiza ejecución Django | Se aclara persistencia frente a runtime; verificación de despliegue pendiente. Costo cero presupuestado no es garantía técnica/comercial. |
| COH-16 | HIGH | Páginas visitadas en caché podían incluir respuestas privadas de SPEC-001 | Plan limita caché genérico a público; shell offline específico con P-14; seguridad de acceso vigente. |
| COH-17 | HIGH | Modularidad estricta/eventos podían confundirse con transacciones parciales | Atomicidad multi-entidad prevalece; outbox de comandos local distinto del de eventos remotos. Detalle arquitectónico sigue propuesto hasta ADR. |
| COH-18 | MEDIUM | Metodología volvía a dejar abiertos perfiles, ventas y variables ya confirmados | Pendientes reemplazados por parámetros reales; ISO funcional sigue como objetivo y UX/offline complementan pruebas. |
| COH-19 | HIGH | Tasks T013 comprobaba Django sin settings; T033 no esperaba T032 | Corregido: check en T014 y revisión después de UI/CI. No se ejecutaron tareas de aplicación. |
| COH-20 | MEDIUM | D-012 inexistente y CI/lint sin tarea de finalización | T008 cita D-001…D-011; T037 asigna CI/Ruff del plan; 37 tareas pendientes. |

## Comprobación individual de requisitos aprobados

Cada fila contrasta el significado incorporado por CAT-REQ-001 y su tratamiento en el diseño.
Los códigos de la última columna llevan prefijo CU-. Son asociaciones de diseño, no pruebas
pasadas ni aceptación completa de las fichas. Los RNF son transversales; no necesitan una
elipse propia. P-01…P-12 conservan su efecto según el catálogo, incluso si la fila es coherente.

| ID confirmado en v1.0 | Regla contrastada | Correspondencia en casos propuestos | Resultado documental |
|---|---|---|---|
| `RF-ACC-001` | Cuenta activa inicia/cierra sesión y accede solo a lo autorizado | ADM-02/03/05/06 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ACC-002` | Crear, actualizar, activar o desactivar sin borrar historia | ADM-04 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ACC-003` | Mantener Directiva, Socia y Visitante; cargos y encargos limitan operaciones; soporte técnico queda separado | ADM-04, PLA-04 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ACC-004` | Mostrar actividades, pendientes y encargos vigentes, no nombres técnicos de permisos | ADM-06, REP-03 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-PLA-001` | Registrar actividad, instancia, fecha, hora, lugar, responsable, participantes, estado y motivo de cancelación | PLA-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-PLA-002` | Asignar responsable, participantes y alcance de cada persona | PLA-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-PLA-003` | Encargo de producción o feria con actividad, periodo, alcance y cierre | PLA-04 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-PLA-004` | Filtrar por periodo, estado, responsable y participación | PLA-03 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-PLA-005` | Planificar fecha, producto, cantidad objetivo, responsables e insumos previstos | PLA-05 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ASI-001` | Conservar entrada y salida con hora del servidor y origen propio o delegado | ASI-01 | Regla en línea conservada; extensión offline en revisión v1.1 |
| `RF-ASI-002` | Unicidad por socia, instancia y tipo de evento; inconsistencias quedan pendientes | ASI-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ASI-003` | Directiva o Encargada autorizada corrige con motivo e historial conforme D-004 | ASI-04 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ASI-004` | Socia ve solo su historial; Directiva consulta según cargo y periodo | ASI-03 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ASI-005` | Registrar tipos pocos y validados solo cuando aporten información distinta de asistencia | ASI-05 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ASI-006` | Acumular pendientes; asamblea decide justificada, injustificada, corregida o pendiente; Directiva registra cada resultado | ASI-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-ASI-007` | Fases QR, autorregistro, código alternativo y delegación según ajuste expreso de CAT-REQ-001 | ASI-01 | Regla en línea conservada; extensión offline en revisión v1.1 |
| `RF-CAT-001` | Separar planta, materia prima, insumo, empaque, producto, presentación y unidad; desactivar no borra historia | CAT-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-INV-001` | Conservar presentación, costo conocido, precio sugerido, precio vigente y valor base con vigencia | CAT-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-TRA-001` | Registrar socia, materia, peso/cantidad, unidad, fecha, valoración, responsable y observación | TRA-01 | Regla en línea conservada; extensión offline en revisión v1.1 |
| `RF-TRA-002` | Registrar peso inicial/final, temperatura Celsius, humedad opcional e inicio/fin automáticos | TRA-02 | Regla en línea conservada; extensión offline en revisión v1.1 |
| `RF-TRA-003` | Calcular duración y merma absoluta; porcentaje solo cuando se apruebe redondeo | TRA-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-TRA-004` | Crear lote por producción; cerrar al finalizar y confirmar rendimiento; agotado se deriva del stock; mezcla física crea lote derivado con orígenes | TRA-03/07 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-TRA-005` | Registrar entradas consumidas, composición/version, resultado, cantidad, residuos, responsable, fecha y lote | TRA-03 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-INV-002` | Toda entrada, consumo, producción, asignación, venta, devolución y ajuste produce movimiento | TRA-04/08 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-INV-003` | Identificar encargo, socia, producto, lote, cantidad y modo individual o compartido | TRA-05 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-INV-004` | Calcular recibido + transferido - vendido - devuelto - retorno; separar este saldo de deuda monetaria | CXC-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-VEN-001` | Venta multiproducto desde stock autorizado con cantidad, precio, total y forma de pago | VEN-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-VEN-002` | Contado usa Público general; crédito/institución exige identificación mínima aprobada | VEN-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-VEN-003` | Congelar valor base y calcular excedente bruto; no llamarlo utilidad neta | VEN-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-VEN-004` | Exigir autorización previa o posterior según contingencia, motivo y auditoría | VEN-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-VEN-005` | Configurar umbral, precio o porcentaje, producto/presentación, vigencia y autoridad | VEN-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-VEN-006` | Admitir líneas desde stock individual o compartido; fuente queda fijada por línea | VEN-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-VEN-007` | Venta organizacional usa stock general, la gestiona Tesorera y no atribuye excedente a una socia | VEN-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-VEN-008` | Comprobante manual único y registro tardío con momento real, momento de digitación, actor y motivo | CON-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-GAS-001` | Registrar categoría, monto, fecha, concepto, lote/periodo y responsable | GAS-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-GAS-002` | Mostrar ingresos organizacionales, gastos, pendientes y fórmula, sin presentarlo como balance certificado | REP-01/02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-CXC-001` | Retiro individual impago crea deuda al valor base congelado; custodia compartida no crea deuda individual; deuda externa queda separada | TRA-06 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-CXC-002` | Registrar monto, fecha/hora, forma, responsable y saldo aplicado | CXC-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-CXC-003` | Mostrar recibido, vendido, devuelto, sobrante, dinero, base, excedente y diferencias | CXC-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-REP-001` | Filtrar por periodo, actividad y socia; mostrar estados y correcciones autorizadas | REP-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-REP-002` | Filtrar por estado, tipo, responsable y periodo | REP-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-REP-003` | Resumir acopio, secado, transformación, lotes y merma con unidades y origen | REP-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-REP-004` | Mostrar existencia derivada y movimientos por producto, lote y periodo | REP-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-REP-005` | Separar ventas, deuda de socias, deuda externa, pagos y pendientes | REP-02 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-REP-006` | Separar asistencia, actividades, productos, monto a entregar, créditos de clientes y excedente bruto | REP-03 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-NOT-001` | Mostrar recordatorios internos de actividades, asistencia, encargos, rendiciones y registros tardíos | REP-03 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-PUB-001` | Publicar solo historia, misión, visión, productos, ubicación, redes y contacto aprobados | ADM-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RF-PUB-002` | Flujo preparar, aprobar, publicar y retirar según permiso | PUB-01 | Coherente con fuente; detalle/pruebas aún pendientes |
| `RNF-UX-001` | Móvil desde 360 px, acciones claras y formularios cortos | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Coherente con fuente; detalle/pruebas aún pendientes |
| `RNF-UX-002` | Contraste AA, teclado, foco, etiquetas y errores recuperables | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Coherente con fuente; detalle/pruebas aún pendientes |
| `RNF-UX-003` | Lenguaje cotidiano y cálculos automáticos | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Coherente con fuente; detalle/pruebas aún pendientes |
| `RNF-CON-001` | Operación ligera y principalmente en línea | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Regla en línea conservada; extensión offline en revisión v1.1 |
| `RNF-SEC-001` | Autorización backend en operaciones sensibles | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Coherente con fuente; detalle/pruebas aún pendientes |
| `RNF-AUD-001` | Correcciones, aprobaciones y excepciones reconstruibles | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Coherente con fuente; detalle/pruebas aún pendientes |
| `RNF-DAT-001` | Operaciones multi-entidad atómicas y basadas en movimientos | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Coherente con fuente; detalle/pruebas aún pendientes |
| `RNF-PRV-001` | Minimización de datos y separación pública | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Coherente con fuente; detalle/pruebas aún pendientes |
| `RNF-PDF-001` | PDF claro, trazable y no dependiente solo del color | Transversal; ADM, ASI, TRA, VEN, REP y OFF según operación | Coherente con fuente; detalle/pruebas aún pendientes |

### Pendientes e históricos

RF-COS-001 y RNF-OPS-001 siguen `proposed`; no se presume costo cero para insumos sin
valoración ni se confirma respaldo por elegir proveedor. Los 12 IDs sustituidos permanecen
históricos. RF-PWA-001/002/003 son nuevas capacidades propuestas con necesidad expresamente
solicitada; no se suman a los 57 aprobados ni duplican RF-OFF históricos como activos.

## Cruce de artefactos de SPEC-001

Se revisaron spec, plan y tasks usando el análisis Spec Kit anterior: 21 claves de cobertura
(10 RF contando padre, 6 RNF y 5 SC). La corrección no cambia historias ni CA de acceso.
T037 materializa comprobaciones ya exigidas por plan/constitución. El grafo termina
T024/T028/T032 → T037 → T033 → T034 → T035 → T036. No hay tareas marcadas terminadas.

La autenticación y el cambio de contraseña siguen en línea y con no-caché privado. La nueva
necesidad offline corresponde a otras specs; no vuelve incoherente por sí sola a SPEC-001.
La recuperación y el mensaje de corte del acceso no equivalen a una cola de registros de negocio.

## Verificación de recursos y alcance

- Presupuesto: 14 partidas, total USD 2.869, subtotales 1.527 + 20 + 1.200 + 19 + 103.
- Cronograma: 18 actividades del Gantt dentro de S1–S16; hitos 2/4/12/16, solapamientos 6/7.
- Stack: 14 tecnologías transcritas; la fila de Vercel pertenece al presupuesto, no desaparece
  porque la tabla de tecnologías no la repite. No se sustituye Django por Supabase.
- Cinco módulos académicos; seis apps de dominio más core; 36 IDs CU propuestos en siete vistas.
- Identidad visual provisional, Poppins y color principal compatibles entre sistema UX y
  especificación de la hoja de estilos. No se repitió evaluación visual/comportamental de
  componentes ajenos a esta tarea ni se declaró validada con usuarias.

## Aspectos todavía abiertos para cerrar coherencia normativa

1. Validación versionada de los cambios de requisitos y revisión académica del alcance;
   las aprobaciones de julio no se extienden solas a septiembre.
2. P-13/P-14: aceptación de asistencia tardía/QR, operaciones offline, reloj, sesión,
   protección local, retención y resolución de conflictos. La capacidad obligatoria no se
   vuelve a someter a elección; se define su funcionamiento.
3. P-01…P-12 que aún afecten cada spec; nueva selección tecnológica no los resuelve.
4. Despliegue real de Django, conexiones/archivos y política de restauración.
5. Estimar el trabajo de acceso completo y los 23 RF de trazabilidad/comercial; el cronograma
   aportado no demuestra por sí solo que una persona pueda cumplir ese esfuerzo.

## Artefactos actualizados

- [[../../architecture/MODULOS-DETALLADOS|Módulos]] y [[../../architecture/ARQUITECTURA-OBJETIVO|arquitectura objetivo]].
- [[../../architecture/PLAN-DESDE-CERO|Plan maestro]] y [[../../decisions/proposals/2026-09-22-arquitectura-modular-desacoplada|propuesta arquitectónica]].
- [[../../requirements/README|Índice de requisitos]] y [[../../requirements/proposals/2026-09-28-catalogo-v1-1|revisión v1.1]].
- [[../../00-inicio/00-dashboard|Dashboard]], [[../../00-inicio/01-decisiones-pendientes|decisiones]] y [[../../traceability/MATRIZ-TRAZABILIDAD|matriz global]].
- [[../../../agents/tesis/PROJECT_CONTEXT|Contexto]], [[../../context/feature-index|índice de funcionalidad]], [[../../sprints/ROADMAP-ANTEPROYECTO|roadmap]], [[../../metodologia/METODOLOGIA-BASE|metodología]] y [[../../ui/SISTEMA-DISENO|UX]].
- [[../../../specs/001-acceso-usuarias-internas/tasks|Tareas de acceso]] y [[../../requirements/proposals/2026-09-28-casos-de-uso|casos de uso]].

## Verificaciones reproducibles

Los resultados y límites de las verificaciones se registran en el
[[../../bitacora/checkpoints/2026-09-28-coherencia-integral|checkpoint de cierre documental]].
El manifiesto [coherencia-verificacion.json](coherencia-verificacion.json) conserva los
hashes de fuentes aprobadas, recuentos y cambios de esta tarea, sin datos personales.
