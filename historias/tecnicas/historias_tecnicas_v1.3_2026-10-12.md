---
titulo: Historias técnicas de Zhud Alelí
version: "1.3"
fecha: 2026-10-12
autor: Tesista
estado: final-documental
fuente_entrevista: EVID-ENT-2026-10-12-001
fuentes: "CAT-REQ-001 v1.1; constitución 0.2.0; ADR-0006; material de cátedra 2.9"
historias_tecnicas: 9
prioridad: orden-preliminar-por-validar
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Historias técnicas

Las historias técnicas son trabajos que habilitan o protegen las historias de usuario. Se expresan como tareas técnicas, sin el patrón «Como… quiero…». Las tablas separan su propósito de los criterios y pruebas para facilitar la revisión. La prioridad es una propuesta y la estimación queda pendiente del equipo; ningún trabajo se presenta como ejecutado.

## Resumen de trabajo

| Historia técnica | Tipo y descripción | Prioridad y estimación | Dependencias |
|---|---|---|---|
| **`HT-GEN-008` — Explorar despliegue y recuperación** | **Tipo:** exploración técnica.<br>determinar un entorno viable para ejecutar Django con PostgreSQL, archivos y acceso seguro, y documentar cómo se comprobarían una publicación y su recuperación. Es necesario antes de comprometer una entrega piloto. | Prioridad propuesta: 1/60<br>Estimación: pendiente del equipo | constitución 0.2.0 y ADR-0006; P-11 para la política definitiva. |
| **`HT-GEN-001` — Preparar la base modular Django** | **Tipo:** arquitectura e infraestructura de producto.<br>organizar los módulos Django por responsabilidad y crear el usuario personalizado antes de la primera migración estable. Cada dato y escritura debe tener propietario para facilitar los incrementos posteriores. | Prioridad propuesta: 2/60<br>Estimación: pendiente del equipo | SPEC-001 y ADR-0006. Esta historia habilita `HU-ACC-001`. |
| **`HT-GEN-009` — Preparar pruebas y trazabilidad** | **Tipo:** infraestructura del equipo.<br>establecer cómo se enlazan requisitos, historias, especificaciones, pruebas y evidencia, y automatizar las comprobaciones disponibles para cada incremento. Permite revisar lo entregado y detectar regresiones. | Prioridad propuesta: 3/60<br>Estimación: pendiente del equipo | `HT-GEN-001` para comprobaciones de aplicación; constitución 0.2.0. |
| **`HT-GEN-002` — Aplicar autorización en el servidor** | **Tipo:** arquitectura y seguridad.<br>centralizar las comprobaciones de identidad y permisos vigentes en las operaciones sensibles, incluidas entradas de sincronización, y separar datos privados de contenido público. | Prioridad propuesta: 4/60<br>Estimación: pendiente del equipo | `HT-GEN-001`, `RNF-SEC-001`, `RNF-PRV-001`; permisos particulares pendientes por funcionalidad. |
| **`HT-GEN-004` — Preparar componentes móviles y accesibles** | **Tipo:** infraestructura de producto.<br>establecer patrones de formularios, mensajes y controles con Bootstrap 5 y plantillas Django que permitan uso móvil, teclado y lenguaje comprensible, sin convertir el Django Admin en interfaz principal. | Prioridad propuesta: 5/60<br>Estimación: pendiente del equipo | `HT-GEN-001`, `RNF-UX-001`, `RNF-UX-002`, `RNF-UX-003`. |
| **`HT-GEN-003` — Asegurar integridad y auditoría** | **Tipo:** arquitectura de datos.<br>hacer que correcciones, movimientos y operaciones que afectan varias entidades se confirmen de forma íntegra y con historia suficiente para reconstruirlas. | Prioridad propuesta: 16/60<br>Estimación: pendiente del equipo | `HT-GEN-001`, `RNF-DAT-001`, `RNF-AUD-001`; P-04, P-05 y P-09 para excepciones dependientes. |
| **`HT-GEN-005` — Preparar captura local protegida** | **Tipo:** infraestructura de producto.<br>preparar recursos esenciales y persistir operaciones habilitadas en el dispositivo como pendientes, aisladas por cuenta y diferenciadas de una confirmación remota. | Prioridad propuesta: 17/60<br>Estimación: pendiente del equipo | `HT-GEN-002`, `RF-PWA-001`, `RF-PWA-002`, `RNF-CON-001`; decisiones P-13 y P-14 antes de cerrar el diseño. |
| **`HT-GEN-006` — Sincronizar sin duplicados** | **Tipo:** arquitectura e infraestructura de producto.<br>enviar operaciones pendientes al volver la conexión, reconocer reintentos y volver a comprobar reglas y permisos en el servidor. El resultado debe distinguir aceptación, rechazo y conflicto. | Prioridad propuesta: 18/60<br>Estimación: pendiente del equipo | `HT-GEN-003`, `HT-GEN-005`, `RF-PWA-003`; P-13 y P-14 para tiempos, orden y conflictos. |
| **`HT-GEN-007` — Generar reportes PDF verificables** | **Tipo:** infraestructura de producto.<br>obtener reportes desde datos autorizados y generar PDF con periodo, filtros, unidades y totales que puedan conciliarse con su origen. | Prioridad propuesta: 51/60<br>Estimación: pendiente del equipo | `RNF-PDF-001`, `HT-GEN-002` y datos confirmados de las funciones que cada reporte consulta. Habilita `HU-REP-001` a `HU-REP-005`. |

## Criterios, tareas y pruebas

| Historia técnica | Criterios de aceptación | Tareas | Prueba prevista |
|---|---|---|---|
| `HT-GEN-008` | 1. Existe una evaluación documentada de al menos una opción viable que cubre ejecución de Django, conexión a PostgreSQL, archivos, HTTPS, costos y límites conocidos.<br>2. El plan identifica comprobaciones previas y posteriores a publicar, riesgos de migración y pasos de recuperación pendientes de validar.<br>3. Las preguntas de política de respaldo de P-11 quedan registradas sin declarar aprobado `RNF-OPS-001`. | revisar la factibilidad vigente; probar un entorno mínimo cuando se autorice; registrar decisión y dudas. | comprobación reproducible de arranque y conexión en el entorno elegido, una vez aprobado. |
| `HT-GEN-001` | 1. La configuración inicial define el usuario personalizado antes de aplicar la primera migración estable.<br>2. Los modelos y migraciones se descubren con los mecanismos nativos de Django y cada módulo creado responde a una necesidad de su especificación.<br>3. Las dependencias entre módulos creados tienen dirección y propietario documentados, sin ciclos detectados. | configurar proyecto y base; crear solo el módulo de acceso requerido; verificar migraciones. | comprobación Django y aplicación de migraciones en PostgreSQL de prueba. |
| `HT-GEN-009` | 1. Cada historia implementada puede rastrearse hasta su requisito, criterio de aceptación, prueba y resultado real.<br>2. La verificación automatizada ejecuta las comprobaciones Django, migraciones, pruebas y análisis disponibles cuando exista el proyecto.<br>3. La revisión de un incremento incluye los recorridos anteriores afectados y registra resultados reproducibles. | definir matriz de trazabilidad; incorporar comprobaciones conforme exista código; registrar evidencia por incremento. | ejecutar la secuencia de verificación sobre un incremento real y conservar su resultado. |
| `HT-GEN-002` | 1. Para cada operación sensible implementada, una prueba permitida confirma el resultado y una denegada demuestra ausencia de cambios.<br>2. Un acceso directo sin permiso no muestra datos ajenos; el sitio público solo recibe contenido autorizado.<br>3. Un reintento de sincronización no devuelve a otra cuenta el resultado de una operación privada. | definir permisos por especificación; aplicarlos en operaciones propietarias; probar accesos directos y reintentos. | integración con perfiles, cargos y encargos permitidos y denegados. |
| `HT-GEN-004` | 1. Un recorrido esencial implementado funciona desde 360 px sin desplazamiento horizontal accidental ni controles ocultos.<br>2. Los controles de ese recorrido tienen etiqueta, foco visible, contraste AA y errores recuperables, comprobados con teclado y zoom al 200 %.<br>3. Los estados se expresan con texto además de color y no exigen que la socia seleccione permisos técnicos. | definir patrones compartidos necesarios; aplicarlos a un recorrido real; recoger observaciones de usuarias. | revisión de accesibilidad y prueba de recorrido con usuarias cuando haya una versión utilizable. |
| `HT-GEN-003` | 1. Si falla una parte de una operación que debe confirmarse junta, la prueba demuestra que no permanece un cambio parcial.<br>2. La existencia consultada se deriva de movimientos y una corrección sensible conserva actor, momento, motivo y valores necesarios.<br>3. Las pruebas de concurrencia de los recorridos afectados no permiten sobreventa ni saldo negativo silencioso. | fijar propietario de cada dato; definir restricciones y límites transaccionales por funcionalidad; añadir auditoría donde el requisito la exige. | integración PostgreSQL, reversión de fallos y concurrencia proporcional al riesgo. |
| `HT-GEN-005` | 1. En un dispositivo preparado, un flujo habilitado permanece disponible durante un corte de red.<br>2. Una operación habilitada guardada localmente sigue pendiente tras recargar y no se presenta como aceptada por el servidor.<br>3. Una cuenta distinta no puede consultar la cola local de otra usuaria. | precisar acciones y datos mínimos; diseñar almacenamiento y estados; probar corte y cambio de cuenta. | recorrido sin red y aislamiento en dispositivo compartido. |
| `HT-GEN-006` | 1. Reenviar una operación con la misma identidad después de perder la respuesta produce un único registro.<br>2. Un permiso revocado o dato inválido causa rechazo sin cambios parciales ni lectura de resultados ajenos.<br>3. La persona puede distinguir qué operaciones siguen pendientes, cuáles fueron aceptadas y cuáles requieren revisión. | definir identidad y contrato de operación; aplicar reglas propietarias; probar reintentos, conflictos y revocación. | integración con respuesta perdida, reintento y cambio de permisos. |
| `HT-GEN-007` | 1. Un PDF generado contiene título, fecha, periodo, filtros, unidades y totales que coinciden con los registros fuente.<br>2. La información se entiende sin depender solo del color y no incluye datos fuera del permiso de quien lo solicita.<br>3. El logo aparece únicamente si se dispone del archivo autorizado. | definir consultas por reporte; preparar formato común; verificar totales y permisos. | comparar PDF con registros conocidos y revisar legibilidad visual. |

## Límites de esta propuesta

| Tema | Límite vigente |
|---|---|
| Requisitos propuestos | `RNF-OPS-001` y `RF-COS-001` siguen propuestos. La exploración de despliegue no aprueba una política de respaldo ni una fórmula de costo. |
| Continuidad | P-13 y P-14 deben resolver las políticas de captura y sincronización antes de cerrar esas historias. |
| Fuentes | El material de cátedra aporta formato y clasificación; el catálogo y la arquitectura aceptada aportan el contenido específico del proyecto. |

## Exploraciones técnicas derivadas de la entrevista

Las nueve HT de la línea base no cambian. Las siguientes exploraciones solo se convierten en historias técnicas planificables si se aprueba el requisito al que sirven.

| Exploración | Qué debe comprobar | Dependencia de decisión |
|---|---|---|
| Protección de documentos | Almacenamiento privado, versiones, permisos, auditoría, carga y recuperación de PDF; evitar datos sensibles innecesarios. | Alcance documental, privacidad, retención y respaldo. |
| Avisos externos y calendario | Fechas de vencimiento, recordatorios uno/dos días o tres/seis meses antes, errores de envío y costo de WhatsApp. | Canal autorizado, consentimiento y responsable. |
| Reglas monetarias revisables | Si se aprueba automatizar, comprobar cálculo de USD 0,01/min de atraso y USD 10 desde la primera falta, con aviso a la tercera falta, versión de regla, excepción e historial. Separar comisiones y valor base. | Reglamento, justificativos, autoridad y P-03; P-06/P-07/P-09 para comercio; revisión humana. |
| Inventario ampliado | Relación de stock personal/general, receta, unidades, niveles críticos y posible depreciación de activos. | Propiedad de stock, P-04/P-05 y alcance de activos. |
| Contacto comercial público | Separar enlace de consulta de pedido/venta, contenido público aprobado y no exposición de datos internos. | P-12 y decisión comercial. |

La fuente EVID-ENT-2026-10-12-001 no demuestra necesidad de cambiar la constitución 0.2.0 ni autoriza escoger un proveedor, implantar firmas legales o enviar mensajes.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.3 | 2026-10-12 | Se presentan nueve historias técnicas en tablas y se señalan impactos por estudiar. | Edición documental; revisión académica pendiente |
