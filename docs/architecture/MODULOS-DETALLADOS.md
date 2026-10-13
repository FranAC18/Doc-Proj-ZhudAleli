---
title: Módulos detallados de la aplicación
type: architecture
status: in-progress
updated: 2026-09-28
task_id: DOC-COHERENCE-001
---

# Módulos detallados de la aplicación

Esta revisión corrige asociaciones erróneas entre IDs y funciones. La fuente de las reglas es
[[../requirements/CAT-REQ-001|CAT-REQ-001 v1.1]], que incorpora las filas de
[[../requirements/proposals/2026-07-22-catalogo-revisado-requisitos-r3|R3]] con sus ajustes.
Los resúmenes no sustituyen criterios de aceptación ni aprueban entidades nuevas.
La [[../requirements/CAT-REQ-001|v1.1]] incorpora los cambios de continuidad aprobados
expresamente por el tesista; P-13/P-14 mantienen abiertos sus detalles operativos.

## Mapa y calendario

Cinco módulos académicos se implementan con seis apps de dominio y un core pequeño.
No son siete módulos académicos. El [[../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack|Gantt aportado]]
reserva acceso S5–S6, planificación S6–S7, asistencia S7–S8, trazabilidad S9–S10 y reportes
S11–S12. El sitio público pertenece al bloque S5 académico, no a la semana 5.

## core — utilidades compartidas

IDs, reloj y utilidades de auditoría realmente compartidas. No posee usuarios, catálogos
productivos, estados de negocio ni unidades del dominio. El usuario pertenece a accounts;
catálogos y unidades productivas, a traceability. Los mecanismos PWA se especifican aparte,
con contratos y autorización del módulo propietario. No se crean apps vacías por anticipación.

## accounts — Administración y acceso

Directiva, Socia operaria y Visitante son los perfiles. Presidenta, tesorera y secretaria son cargos; un encargo temporal no crea otro rol. P-01 define permisos sensibles. SPEC-001 implementará solamente RF-ACC-001 y seis RNF aplicables: acceso, cambio de contraseña, sesión de 30 minutos y bienvenida. Gestión de cuentas y dashboard operativo completo requieren otra porción. Desactivar conserva historia; no hay borrado de membresía ni herencia de permisos aprobada por este resumen.

| ID aprobado | Regla de referencia |
|---|---|
| `RF-ACC-001` | Cuenta activa inicia/cierra sesión y accede solo a lo autorizado |
| `RF-ACC-002` | Crear, actualizar, activar o desactivar sin borrar historia |
| `RF-ACC-003` | Mantener Directiva, Socia y Visitante; cargos y encargos limitan operaciones; soporte técnico queda separado |
| `RF-ACC-004` | Mostrar actividades, pendientes y encargos vigentes, no nombres técnicos de permisos |

## planning — Planificación

Incluye encargos temporales y planificación productiva sin crear stock. RF-PLA-002 es asignación; RF-PLA-003 es encargo; RF-PLA-004 es consulta; RF-PLA-005 es previsión productiva. P-01 limita acciones. Los estados finales y los campos del modelo se concretarán en su spec; esta nota no inventa entidades obligatorias.

| ID aprobado | Regla de referencia |
|---|---|
| `RF-PLA-001` | Registrar actividad, instancia, fecha, hora, lugar, responsable, participantes, estado y motivo de cancelación |
| `RF-PLA-002` | Asignar responsable, participantes y alcance de cada persona |
| `RF-PLA-003` | Encargo de producción o feria con actividad, periodo, alcance y cierre |
| `RF-PLA-004` | Filtrar por periodo, estado, responsable y participación |
| `RF-PLA-005` | Planificar fecha, producto, cantidad objetivo, responsables e insumos previstos |

## attendance — Asistencia y participación

RF-ASI-001 incluye entrada y salida; RF-ASI-002 controla unicidad; RF-ASI-003 corrige; RF-ASI-004 consulta historial; RF-ASI-005 registra participación adicional y RF-ASI-006 registra resolución de asamblea. La asamblea es una autoridad del proceso, no una cuenta de aplicación. Para RF-ASI-007 prevalece el ajuste expreso de CAT-REQ-001. P-02/P-03 siguen abiertos. La captura offline solicitada exige diferenciar hora local declarada y recepción del servidor; QR vencido no se acepta automáticamente. Véase revisión v1.1.

| ID aprobado | Regla de referencia |
|---|---|
| `RF-ASI-001` | Conservar entrada y salida con hora del servidor y origen propio o delegado |
| `RF-ASI-002` | Unicidad por socia, instancia y tipo de evento; inconsistencias quedan pendientes |
| `RF-ASI-003` | Directiva o Encargada autorizada corrige con motivo e historial conforme D-004 |
| `RF-ASI-004` | Socia ve solo su historial; Directiva consulta según cargo y periodo |
| `RF-ASI-005` | Registrar tipos pocos y validados solo cuando aporten información distinta de asistencia |
| `RF-ASI-006` | Acumular pendientes; asamblea decide justificada, injustificada, corregida o pendiente; Directiva registra cada resultado |
| `RF-ASI-007` | Fases QR de entrada/salida, autorregistro propio, código alternativo y registro delegado auditable; prevalece el ajuste del catálogo |

## traceability — Producción y gestión comercial

Agrupa 23 RF, incluidos ventas, gastos y cuentas por cobrar; una futura separación de app requiere ADR. Los pesos se introducen con unidad y validación; no hay báscula ni medición automática aprobada. Secado exige temperatura Celsius; solo las fechas de inicio/fin se generan automáticamente en el flujo en línea. Lote cerrado y existencia agotada son variables distintas. Retiro individual impago crea deuda al valor base histórico; custodia compartida no genera deuda individual. Los cambios de varias entidades son atómicos, incluida venta multiproducto. P-04 a P-10 delimitan datos y excepciones; RF-COS-001 sigue propuesto. Comprobante manual de ventas sigue como contingencia: no sustituye el guardado offline obligatorio de asistencia/pesajes ni habilita ventas/pagos offline sin definirlos.

| ID aprobado | Regla de referencia |
|---|---|
| `RF-CAT-001` | Separar planta, materia prima, insumo, empaque, producto, presentación y unidad; desactivar no borra historia |
| `RF-INV-001` | Conservar presentación, costo conocido, precio sugerido, precio vigente y valor base con vigencia |
| `RF-TRA-001` | Registrar socia, materia, peso/cantidad, unidad, fecha, valoración, responsable y observación |
| `RF-TRA-002` | Registrar peso inicial/final, temperatura Celsius, humedad opcional e inicio/fin automáticos |
| `RF-TRA-003` | Calcular duración y merma absoluta; porcentaje solo cuando se apruebe redondeo |
| `RF-TRA-004` | Crear lote por producción; cerrar al finalizar y confirmar rendimiento; agotado se deriva del stock; mezcla física crea lote derivado con orígenes |
| `RF-TRA-005` | Registrar entradas consumidas, composición/version, resultado, cantidad, residuos, responsable, fecha y lote |
| `RF-INV-002` | Toda entrada, consumo, producción, asignación, venta, devolución y ajuste produce movimiento |
| `RF-INV-003` | Identificar encargo, socia, producto, lote, cantidad y modo individual o compartido |
| `RF-INV-004` | Calcular recibido + transferido - vendido - devuelto - retorno; separar este saldo de deuda monetaria |
| `RF-VEN-001` | Venta multiproducto desde stock autorizado con cantidad, precio, total y forma de pago |
| `RF-VEN-002` | Contado usa Público general; crédito/institución exige identificación mínima aprobada |
| `RF-VEN-003` | Congelar valor base y calcular excedente bruto; no llamarlo utilidad neta |
| `RF-VEN-004` | Exigir autorización previa o posterior según contingencia, motivo y auditoría |
| `RF-VEN-005` | Configurar umbral, precio o porcentaje, producto/presentación, vigencia y autoridad |
| `RF-VEN-006` | Admitir líneas desde stock individual o compartido; fuente queda fijada por línea |
| `RF-VEN-007` | Venta organizacional usa stock general, la gestiona Tesorera y no atribuye excedente a una socia |
| `RF-VEN-008` | Comprobante manual único y registro tardío con momento real, momento de digitación, actor y motivo |
| `RF-GAS-001` | Registrar categoría, monto, fecha, concepto, lote/periodo y responsable |
| `RF-GAS-002` | Mostrar ingresos organizacionales, gastos, pendientes y fórmula, sin presentarlo como balance certificado |
| `RF-CXC-001` | Retiro individual impago crea deuda al valor base congelado; custodia compartida no crea deuda individual; deuda externa queda separada |
| `RF-CXC-002` | Registrar monto, fecha/hora, forma, responsable y saldo aplicado |
| `RF-CXC-003` | Mostrar recibido, vendido, devuelto, sobrante, dinero, base, excedente y diferencias |

## reports — Reportes y recordatorios

Los seis reportes incluyen el resumen privado de cada socia (RF-REP-006); no son seis reportes globales intercambiables. RF-NOT-001 son recordatorios internos, no correo o push obligatorio. Fórmulas, filtros, unidades y fuentes deben ser visibles. P-08 es descuentos, no una decisión de filtros. El detalle de reportes se deriva de D-006, cada RF y P-01 para permisos.

| ID aprobado | Regla de referencia |
|---|---|
| `RF-REP-001` | Filtrar por periodo, actividad y socia; mostrar estados y correcciones autorizadas |
| `RF-REP-002` | Filtrar por estado, tipo, responsable y periodo |
| `RF-REP-003` | Resumir acopio, secado, transformación, lotes y merma con unidades y origen |
| `RF-REP-004` | Mostrar existencia derivada y movimientos por producto, lote y periodo |
| `RF-REP-005` | Separar ventas, deuda de socias, deuda externa, pagos y pendientes |
| `RF-REP-006` | Separar asistencia, actividades, productos, monto a entregar, créditos de clientes y excedente bruto |
| `RF-NOT-001` | Mostrar recordatorios internos de actividades, asistencia, encargos, rendiciones y registros tardíos |

## public_site — Contenido público

App separada según ADR-0003, compartiendo el bloque académico S5 con reports. No es una subapp de reports ni un módulo académico adicional. RF-PUB-002 exige preparar, aprobar, publicar y retirar conservando historia. P-12 controla contenido; P-01, publicadores. Visitantes nunca reciben datos internos ni afirmaciones sanitarias.

| ID aprobado | Regla de referencia |
|---|---|
| `RF-PUB-001` | Publicar solo historia, misión, visión, productos, ubicación, redes y contacto aprobados |
| `RF-PUB-002` | Flujo preparar, aprobar, publicar y retirar según permiso |

## Requisitos transversales

| ID | Regla de referencia |
|---|---|
| `RNF-UX-001` | Móvil desde 360 px, acciones claras y formularios cortos |
| `RNF-UX-002` | Contraste AA, teclado, foco, etiquetas y errores recuperables |
| `RNF-UX-003` | Lenguaje cotidiano y cálculos automáticos |
| `RNF-CON-001` | Operación ligera, recursos esenciales locales y continuidad PWA; estados local/pendiente/aceptado/rechazado, sin duplicados ni éxito remoto ficticio |
| `RNF-SEC-001` | Autorización backend en operaciones sensibles |
| `RNF-AUD-001` | Correcciones, aprobaciones y excepciones reconstruibles |
| `RNF-DAT-001` | Operaciones multi-entidad atómicas y basadas en movimientos |
| `RNF-PRV-001` | Minimización de datos y separación pública |
| `RNF-PDF-001` | PDF claro, trazable y no dependiente solo del color |

RNF-CON-001 tiene alcance revisado y aprobado en v1.1. Los criterios de seguridad, auditoría,
atomicidad y privacidad también se aplican a la sincronización; guardar localmente no
significa aceptación del servidor. El detalle de respaldos RNF-OPS-001 sigue propuesto.

## Continuidad PWA — requisitos confirmados

| ID | Regla aprobada |
|---|---|
| `RF-PWA-001` | Abrir la interfaz esencial preparada sin red en dispositivos compatibles |
| `RF-PWA-002` | Guardar asistencias y pesajes habilitados en IndexedDB, con identidad, contexto y estado provisional |
| `RF-PWA-003` | Sincronizar con identidad de operación, revalidación backend, atomicidad, rechazo visible y reintentos sin duplicar |

Criterios completos y políticas P-13/P-14 en [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.1]].
Estas tres capacidades están confirmadas por el tesista; no implementadas todavía.

## Conteo sin duplicados

| Ámbito | RF únicos | RNF únicos |
|---|---:|---:|
| Administración y acceso | 4 | 0 |
| Planificación | 5 | 0 |
| Asistencia | 7 | 0 |
| Trazabilidad y comercial | 23 | 0 |
| Reportes y recordatorios | 7 | 0 |
| Sitio público | 2 | 0 |
| Transversal | 0 | 9 |
| Continuidad PWA | 3 | 0 |
| Total de la línea base v1.1 | 51 | 9 |

Total vigente: **60 IDs confirmados** (51 RF + 9 RNF). V1.0 tenía 57, no 63: los seis
RNF aplicables a SPEC-001 son parte de los nueve transversales y no se duplican.
RF-COS-001 y RNF-OPS-001 siguen como dos requisitos propuestos separados.

## Enlaces de diseño y verificación

- [[../requirements/proposals/2026-09-28-casos-de-uso|Fichas de casos de uso]].
- [[../requirements/proposals/2026-09-28-diagramas-casos-de-uso|Esquemas UML y archivo fuente]].
- [[../evidence/casos-de-uso/2026-09-28-coherencia-integral|Auditoría de los 57 requisitos y documentos activos]].
- [[../00-inicio/01-decisiones-pendientes|Parámetros organizativos pendientes]].
- [[../../specs/001-acceso-usuarias-internas/spec|SPEC-001 y sus criterios CA-ACC-001-01 a CA-ACC-001-11]].
- [[PLAN-DESDE-CERO|Plan maestro]] y [[../ui/SISTEMA-DISENO|Criterios UX]].

No existe todavía una spec aprobada de asistencia, producción o reportes; no se asignan
códigos CA ficticios a esos módulos. Código, pruebas funcionales y validación con usuarias
quedan pendientes; este documento acredita consistencia del diseño documental.
