---
titulo: Historias técnicas en fichas
version: "1.5"
fecha: 2026-10-13
autor: Tesista
estado: final-documental-con-propuestas-identificadas
historias_base: 9
historias_nuevas_propuestas: 10
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Historias técnicas

Cada historia técnica se presenta en una ficha separada. Las nueve historias de línea base conservan sus criterios de la [edición detallada v1.3](historias_tecnicas_v1.3_2026-10-12.md). Las diez nuevas siguen siendo **propuestas**; su presencia aquí no cambia los requisitos aprobados. Prioridades, riesgos, puntos y responsables se revisan al preparar cada sprint.

## Historias técnicas de la línea base

### Historia técnica 1 — Explorar despliegue y recuperación

| Campo | Dato |
|---|---|
| **Número** | 1 |
| **Código de referencia** | `HT-GEN-008` |
| **Nombre** | Explorar despliegue y recuperación |
| **Tipo** | exploración técnica |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S1; revisión en S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | determinar un entorno viable para ejecutar Django con PostgreSQL, archivos y acceso seguro, y documentar cómo se comprobarían una publicación y su recuperación. Es necesario antes de comprometer una entrega piloto. |
| **Relación con HU o fuentes** | Habilita la futura entrega piloto. Comparar entorno, costos, archivos, HTTPS y recuperación; P-11 sigue abierto. |
| **Criterios de salida** | 1. Existe una evaluación documentada de al menos una opción viable que cubre ejecución de Django, conexión a PostgreSQL, archivos, HTTPS, costos y límites conocidos.<br>2. El plan identifica comprobaciones previas y posteriores a publicar, riesgos de migración y pasos de recuperación pendientes de validar.<br>3. Las preguntas de política de respaldo de P-11 quedan registradas sin declarar aprobado RNF-OPS-001. |
| **Tareas** | revisar la factibilidad vigente; probar un entorno mínimo cuando se autorice; registrar decisión y dudas. |
| **Prueba prevista** | comprobación reproducible de arranque y conexión en el entorno elegido, una vez aprobado. |
| **Dependencias** | constitución 0.2.0 y ADR-0006; P-11 para la política definitiva. |
| **Estado** | Línea base |

### Historia técnica 2 — Preparar la base modular Django

| Campo | Dato |
|---|---|
| **Número** | 2 |
| **Código de referencia** | `HT-GEN-001` |
| **Nombre** | Preparar la base modular Django |
| **Tipo** | arquitectura e infraestructura de producto |
| **Prioridad técnica** | Crítica (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | organizar los módulos Django por responsabilidad y crear el usuario personalizado antes de la primera migración estable. Cada dato y escritura debe tener propietario para facilitar los incrementos posteriores. |
| **Relación con HU o fuentes** | Habilita `HU-ACC-001` a `HU-ACC-004`; usuario personalizado y migraciones en PostgreSQL comprobados. |
| **Criterios de salida** | 1. La configuración inicial define el usuario personalizado antes de aplicar la primera migración estable.<br>2. Los modelos y migraciones se descubren con los mecanismos nativos de Django y cada módulo creado responde a una necesidad de su especificación.<br>3. Las dependencias entre módulos creados tienen dirección y propietario documentados, sin ciclos detectados. |
| **Tareas** | configurar proyecto y base; crear solo el módulo de acceso requerido; verificar migraciones. |
| **Prueba prevista** | comprobación Django y aplicación de migraciones en PostgreSQL de prueba. |
| **Dependencias** | SPEC-001 y ADR-0006. Esta historia habilita HU-ACC-001. |
| **Estado** | Línea base |

### Historia técnica 3 — Preparar pruebas y trazabilidad

| Campo | Dato |
|---|---|
| **Número** | 3 |
| **Código de referencia** | `HT-GEN-009` |
| **Nombre** | Preparar pruebas y trazabilidad |
| **Tipo** | infraestructura del equipo |
| **Prioridad técnica** | Crítica (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2–S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | establecer cómo se enlazan requisitos, historias, especificaciones, pruebas y evidencia, y automatizar las comprobaciones disponibles para cada incremento. Permite revisar lo entregado y detectar regresiones. |
| **Relación con HU o fuentes** | Cada HU elegida conserva vínculo con RF, prueba y resultado; se ejecuta regresión en cada incremento. |
| **Criterios de salida** | 1. Cada historia implementada puede rastrearse hasta su requisito, criterio de aceptación, prueba y resultado real.<br>2. La verificación automatizada ejecuta las comprobaciones Django, migraciones, pruebas y análisis disponibles cuando exista el proyecto.<br>3. La revisión de un incremento incluye los recorridos anteriores afectados y registra resultados reproducibles. |
| **Tareas** | definir matriz de trazabilidad; incorporar comprobaciones conforme exista código; registrar evidencia por incremento. |
| **Prueba prevista** | ejecutar la secuencia de verificación sobre un incremento real y conservar su resultado. |
| **Dependencias** | HT-GEN-001 para comprobaciones de aplicación; constitución 0.2.0. |
| **Estado** | Línea base |

### Historia técnica 4 — Aplicar autorización en el servidor

| Campo | Dato |
|---|---|
| **Número** | 4 |
| **Código de referencia** | `HT-GEN-002` |
| **Nombre** | Aplicar autorización en el servidor |
| **Tipo** | arquitectura y seguridad |
| **Prioridad técnica** | Crítica (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2–S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | centralizar las comprobaciones de identidad y permisos vigentes en las operaciones sensibles, incluidas entradas de sincronización, y separar datos privados de contenido público. |
| **Relación con HU o fuentes** | Protege `HU-ACC`, `HU-PLA`, `HU-ASI`, `HU-TRA`, `HU-INV`, `HU-VEN`, `HU-REP` y `HU-PUB`; probar acceso permitido y denegado. |
| **Criterios de salida** | 1. Para cada operación sensible implementada, una prueba permitida confirma el resultado y una denegada demuestra ausencia de cambios.<br>2. Un acceso directo sin permiso no muestra datos ajenos; el sitio público solo recibe contenido autorizado.<br>3. Un reintento de sincronización no devuelve a otra cuenta el resultado de una operación privada. |
| **Tareas** | definir permisos por especificación; aplicarlos en operaciones propietarias; probar accesos directos y reintentos. |
| **Prueba prevista** | integración con perfiles, cargos y encargos permitidos y denegados. |
| **Dependencias** | HT-GEN-001, RNF-SEC-001, RNF-PRV-001; permisos particulares pendientes por funcionalidad. |
| **Estado** | Línea base |

### Historia técnica 5 — Preparar componentes móviles y accesibles

| Campo | Dato |
|---|---|
| **Número** | 5 |
| **Código de referencia** | `HT-GEN-004` |
| **Nombre** | Preparar componentes móviles y accesibles |
| **Tipo** | infraestructura de producto |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S2–S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | establecer patrones de formularios, mensajes y controles con Bootstrap 5 y plantillas Django que permitan uso móvil, teclado y lenguaje comprensible, sin convertir el Django Admin en interfaz principal. |
| **Relación con HU o fuentes** | Habilita recorridos HU en móvil, teclado, contraste y errores recuperables. |
| **Criterios de salida** | 1. Un recorrido esencial implementado funciona desde 360 px sin desplazamiento horizontal accidental ni controles ocultos.<br>2. Los controles de ese recorrido tienen etiqueta, foco visible, contraste AA y errores recuperables, comprobados con teclado y zoom al 200 %.<br>3. Los estados se expresan con texto además de color y no exigen que la socia seleccione permisos técnicos. |
| **Tareas** | definir patrones compartidos necesarios; aplicarlos a un recorrido real; recoger observaciones de usuarias. |
| **Prueba prevista** | revisión de accesibilidad y prueba de recorrido con usuarias cuando haya una versión utilizable. |
| **Dependencias** | HT-GEN-001, RNF-UX-001, RNF-UX-002, RNF-UX-003. |
| **Estado** | Línea base |

### Historia técnica 6 — Asegurar integridad y auditoría

| Campo | Dato |
|---|---|
| **Número** | 6 |
| **Código de referencia** | `HT-GEN-003` |
| **Nombre** | Asegurar integridad y auditoría |
| **Tipo** | arquitectura de datos |
| **Prioridad técnica** | Crítica (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4–S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | hacer que correcciones, movimientos y operaciones que afectan varias entidades se confirmen de forma íntegra y con historia suficiente para reconstruirlas. |
| **Relación con HU o fuentes** | Protege correcciones de `HU-ASI`, movimientos `HU-TRA`/`HU-INV`, ventas `HU-VEN` y saldos `HU-CXC`; probar reversión y concurrencia. |
| **Criterios de salida** | 1. Si falla una parte de una operación que debe confirmarse junta, la prueba demuestra que no permanece un cambio parcial.<br>2. La existencia consultada se deriva de movimientos y una corrección sensible conserva actor, momento, motivo y valores necesarios.<br>3. Las pruebas de concurrencia de los recorridos afectados no permiten sobreventa ni saldo negativo silencioso. |
| **Tareas** | fijar propietario de cada dato; definir restricciones y límites transaccionales por funcionalidad; añadir auditoría donde el requisito la exige. |
| **Prueba prevista** | integración PostgreSQL, reversión de fallos y concurrencia proporcional al riesgo. |
| **Dependencias** | HT-GEN-001, RNF-DAT-001, RNF-AUD-001; P-04, P-05 y P-09 para excepciones dependientes. |
| **Estado** | Línea base |

### Historia técnica 7 — Preparar captura local protegida

| Campo | Dato |
|---|---|
| **Número** | 7 |
| **Código de referencia** | `HT-GEN-005` |
| **Nombre** | Preparar captura local protegida |
| **Tipo** | infraestructura de producto |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4–S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | preparar recursos esenciales y persistir operaciones habilitadas en el dispositivo como pendientes, aisladas por cuenta y diferenciadas de una confirmación remota. |
| **Relación con HU o fuentes** | Habilita `HU-PWA-001` y `HU-PWA-002` para operaciones autorizadas; P-13/P-14 pendientes. |
| **Criterios de salida** | 1. En un dispositivo preparado, un flujo habilitado permanece disponible durante un corte de red.<br>2. Una operación habilitada guardada localmente sigue pendiente tras recargar y no se presenta como aceptada por el servidor.<br>3. Una cuenta distinta no puede consultar la cola local de otra usuaria. |
| **Tareas** | precisar acciones y datos mínimos; diseñar almacenamiento y estados; probar corte y cambio de cuenta. |
| **Prueba prevista** | recorrido sin red y aislamiento en dispositivo compartido. |
| **Dependencias** | HT-GEN-002, RF-PWA-001, RF-PWA-002, RNF-CON-001; decisiones P-13 y P-14 antes de cerrar el diseño. |
| **Estado** | Línea base |

### Historia técnica 8 — Sincronizar sin duplicados

| Campo | Dato |
|---|---|
| **Número** | 8 |
| **Código de referencia** | `HT-GEN-006` |
| **Nombre** | Sincronizar sin duplicados |
| **Tipo** | arquitectura e infraestructura de producto |
| **Prioridad técnica** | Crítica (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4–S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | enviar operaciones pendientes al volver la conexión, reconocer reintentos y volver a comprobar reglas y permisos en el servidor. El resultado debe distinguir aceptación, rechazo y conflicto. |
| **Relación con HU o fuentes** | Habilita `HU-PWA-003`; probar reintento, permiso revocado y conflicto sin cambios parciales. |
| **Criterios de salida** | 1. Reenviar una operación con la misma identidad después de perder la respuesta produce un único registro.<br>2. Un permiso revocado o dato inválido causa rechazo sin cambios parciales ni lectura de resultados ajenos.<br>3. La persona puede distinguir qué operaciones siguen pendientes, cuáles fueron aceptadas y cuáles requieren revisión. |
| **Tareas** | definir identidad y contrato de operación; aplicar reglas propietarias; probar reintentos, conflictos y revocación. |
| **Prueba prevista** | integración con respuesta perdida, reintento y cambio de permisos. |
| **Dependencias** | HT-GEN-003, HT-GEN-005, RF-PWA-003; P-13 y P-14 para tiempos, orden y conflictos. |
| **Estado** | Línea base |

### Historia técnica 9 — Generar reportes PDF verificables

| Campo | Dato |
|---|---|
| **Número** | 9 |
| **Código de referencia** | `HT-GEN-007` |
| **Nombre** | Generar reportes PDF verificables |
| **Tipo** | infraestructura de producto |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | obtener reportes desde datos autorizados y generar PDF con periodo, filtros, unidades y totales que puedan conciliarse con su origen. |
| **Relación con HU o fuentes** | Habilita `HU-REP-001` a `HU-REP-005`; contrastar totales con datos fuente y permisos. |
| **Criterios de salida** | 1. Un PDF generado contiene título, fecha, periodo, filtros, unidades y totales que coinciden con los registros fuente.<br>2. La información se entiende sin depender solo del color y no incluye datos fuera del permiso de quien lo solicita.<br>3. El logo aparece únicamente si se dispone del archivo autorizado. |
| **Tareas** | definir consultas por reporte; preparar formato común; verificar totales y permisos. |
| **Prueba prevista** | comparar PDF con registros conocidos y revisar legibilidad visual. |
| **Dependencias** | RNF-PDF-001, HT-GEN-002 y datos confirmados de las funciones que cada reporte consulta. Habilita HU-REP-001 a HU-REP-005. |
| **Estado** | Línea base |

## Historias técnicas propuestas

### Historia técnica 10 — Levantar y consolidar entrevistas, observación y documentos disponibles.

| Campo | Dato |
|---|---|
| **Número** | 10 |
| **Código de referencia** | `HT-PRE-001` |
| **Nombre** | Levantar y consolidar entrevistas, observación y documentos disponibles. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S1 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Levantar y consolidar entrevistas, observación y documentos disponibles. |
| **Relación con HU o fuentes** | Fuentes de los RF y de todas las HU; actas de campo. |
| **Criterios de salida** | Cada necesidad registra fuente, fecha, actor, duda y evidencia; no se atribuye aprobación a una nota informal. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 11 — Validar alcance, requisitos, reglas y criterios de aceptación con las personas competentes.

| Campo | Dato |
|---|---|
| **Número** | 11 |
| **Código de referencia** | `HT-PRE-002` |
| **Nombre** | Validar alcance, requisitos, reglas y criterios de aceptación con las personas competentes. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Crítica (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S1 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Validar alcance, requisitos, reglas y criterios de aceptación con las personas competentes. |
| **Relación con HU o fuentes** | `CAT-REQ-001`, `HU-ACC` a `HU-PUB`; decisiones P abiertas. |
| **Criterios de salida** | Separar confirmado, propuesto y pendiente; conservar acta o decisión de cada validación. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 12 — Preparar arquitectura, modelo conceptual y límites de datos por módulo.

| Campo | Dato |
|---|---|
| **Número** | 12 |
| **Código de referencia** | `HT-PRE-003` |
| **Nombre** | Preparar arquitectura, modelo conceptual y límites de datos por módulo. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S1 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Preparar arquitectura, modelo conceptual y límites de datos por módulo. |
| **Relación con HU o fuentes** | Diseño para `HU-ACC`, `HU-PLA`, `HU-ASI`, `HU-TRA`, `HU-INV`, `HU-VEN` y `HU-REP`. |
| **Criterios de salida** | Entidades, dueños de escritura, relaciones, permisos y operaciones conjuntas trazados a requisitos. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 13 — Diseñar recorridos móviles y preparación PWA sin afirmar que la aplicación ya funciona.

| Campo | Dato |
|---|---|
| **Número** | 13 |
| **Código de referencia** | `HT-PRE-004` |
| **Nombre** | Diseñar recorridos móviles y preparación PWA sin afirmar que la aplicación ya funciona. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S1 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Diseñar recorridos móviles y preparación PWA sin afirmar que la aplicación ya funciona. |
| **Relación con HU o fuentes** | `RNF-UX-001` a `003`; `HU-PWA-001` a `003`. |
| **Criterios de salida** | Pantallas y estados de error revisables; límites de datos locales, corte y sincronización pendientes identificados. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 14 — Refinar historias, pila, dependencias, estimaciones y calendario con capacidad real.

| Campo | Dato |
|---|---|
| **Número** | 14 |
| **Código de referencia** | `HT-PRE-005` |
| **Nombre** | Refinar historias, pila, dependencias, estimaciones y calendario con capacidad real. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S1 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Refinar historias, pila, dependencias, estimaciones y calendario con capacidad real. |
| **Relación con HU o fuentes** | 51 HU, 9 HT base y candidatas; sprint backlog. |
| **Criterios de salida** | Cada elemento que pase a un sprint tiene criterio, dependencia, tamaño y decisión de inclusión registrados. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 15 — Preparar pruebas de planificación y regresión de permisos sobre actividades y encargos.

| Campo | Dato |
|---|---|
| **Número** | 15 |
| **Código de referencia** | `HT-S3-001` |
| **Nombre** | Preparar pruebas de planificación y regresión de permisos sobre actividades y encargos. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S3 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Preparar pruebas de planificación y regresión de permisos sobre actividades y encargos. |
| **Relación con HU o fuentes** | `HU-PLA-001` a `005`; `HU-ACC-001` a `004`. |
| **Criterios de salida** | Una asignación válida funciona y una inválida no cambia datos; el acceso anterior sigue funcionando. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 16 — Precisar y probar QR, alternativa de registro y operaciones de asistencia sin red antes de implementarlas.

| Campo | Dato |
|---|---|
| **Número** | 16 |
| **Código de referencia** | `HT-S4-001` |
| **Nombre** | Precisar y probar QR, alternativa de registro y operaciones de asistencia sin red antes de implementarlas. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S4 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Precisar y probar QR, alternativa de registro y operaciones de asistencia sin red antes de implementarlas. |
| **Relación con HU o fuentes** | `HU-ASI-001` a `007`; `HU-PWA-001` a `003`; P-02/P-13/P-14. |
| **Criterios de salida** | Casos de entrada, salida, duplicado, dispositivo compartido y corte/reintento documentados; reglas abiertas visibles. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 17 — Probar la cadena productiva y las operaciones comerciales que entren realmente al sprint.

| Campo | Dato |
|---|---|
| **Número** | 17 |
| **Código de referencia** | `HT-S5-001` |
| **Nombre** | Probar la cadena productiva y las operaciones comerciales que entren realmente al sprint. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Crítica (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S5 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Probar la cadena productiva y las operaciones comerciales que entren realmente al sprint. |
| **Relación con HU o fuentes** | `HU-TRA`, `HU-INV`, `HU-VEN`, `HU-CXC`, `HU-GAS`; `HT-GEN-003`. |
| **Criterios de salida** | Movimientos y totales concilian; fallo o concurrencia no deja stock ni saldos incoherentes. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 18 — Ejecutar integración, pruebas funcionales y de uso, continuidad aprobada y regresión.

| Campo | Dato |
|---|---|
| **Número** | 18 |
| **Código de referencia** | `HT-S6-001` |
| **Nombre** | Ejecutar integración, pruebas funcionales y de uso, continuidad aprobada y regresión. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Crítica (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Ejecutar integración, pruebas funcionales y de uso, continuidad aprobada y regresión. |
| **Relación con HU o fuentes** | Todas las HU efectivamente entregadas; `HT-GEN-009`. |
| **Criterios de salida** | Resultados reales, defectos, correcciones y nueva prueba registrados; sesión con usuarias cuando ocurra. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

### Historia técnica 19 — Preparar manuales, capacitación y acta de validación final.

| Campo | Dato |
|---|---|
| **Número** | 19 |
| **Código de referencia** | `HT-S6-002` |
| **Nombre** | Preparar manuales, capacitación y acta de validación final. |
| **Tipo** | Trabajo técnico |
| **Prioridad técnica** | Alta (propuesta) |
| **Riesgo en desarrollo** | Pendiente de evaluar |
| **Puntos estimados** | Pendiente de estimar |
| **Sprint propuesto** | S6 y cierre |
| **Responsable** | Pendiente de asignar |
| **Descripción** | Preparar manuales, capacitación y acta de validación final. |
| **Relación con HU o fuentes** | Recorridos entregados de `HU-ACC` a `HU-PUB`; hito final del Gantt. |
| **Criterios de salida** | Manual refleja la versión comprobada; capacitación y validación tienen fecha, participantes y observaciones, o constan pendientes. |
| **Tareas** | Pendiente de desglosar |
| **Prueba prevista** | Pendiente de ejecución |
| **Dependencias** | Por confirmar |
| **Estado** | Propuesta |

## Historial de cambios

| Versión | Fecha | Cambio |
|---|---|---|
| 1.4 | 2026-10-13 | Clasificación y relación con S1–S6. |
| 1.5 | 2026-10-13 | Ficha individual con campos separados para 9 HT de base y 10 propuestas. |
