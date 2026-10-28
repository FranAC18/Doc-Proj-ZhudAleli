---
titulo: Sprint backlog preliminar de Zhud Alelí
version: "1.1"
fecha: 2026-10-13
autor: Tesista
estado: plan-preliminar-sin-compromiso-de-capacidad
fuentes: "Gantt y fechas confirmados por el tesista; HU v2.4; HT v1.4; pila de producto v1.4; plan de sprints v1.2"
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Sprint backlog preliminar

Este backlog convierte el [plan S1–S6](plan_sprints_v1.2_2026-10-13.md) en trabajo comprobable. Cada fila conecta **historias de usuario (HU)**, **historias técnicas (HT)**, tareas y prueba de salida. Las 51 HU y las 9 HT de la [pila base de 60](../pila_producto/pila_producto_v1.4_2026-10-13.md) conservan sus IDs. Las diez HT nuevas de la [edición técnica v1.4](../historias/tecnicas/historias_tecnicas_v1.4_2026-10-13.md) son **propuestas identificadas**, separadas de esa línea base.

**Estado al 13 de octubre:** ningún sprint de desarrollo está demostrado como terminado. La documentación de S1 existe en parte, pero quedan revisiones y decisiones. Todas las filas son **candidatas**, con esfuerzo y responsable por fijar en la planificación real. Una fila no equivale a promesa de completar todas sus HU en 14 días.

La columna **prioridad de planificación** ordena la atención a la tarea; es propuesta y no sustituye la importancia de cada HU, visible en [historias de usuario v2.4](../historias/usuario/historias_usuario_v2.4_2026-10-13.md). Los IDs de tarea conservan la secuencia de dependencias.

## Criterio para seleccionar y cerrar trabajo

| Antes de seleccionar | Para cerrar una historia |
|---|---|
| Requisito y actor identificados; regla material resuelta; dependencia disponible; tamaño estimado; responsable y tiempo real acordados. | Recorrido o documento verificable, criterios cumplidos, prueba con resultado real, permisos y regresión aplicables, evidencia y estado actualizado en la pila. |

Cuando falte una puerta, la fila permanece **bloqueada o candidata**. Al planificar se anotan estimación, responsable, fecha y HU elegidas. Al revisar se anotan resultado, diferencia y trabajo restante; no se marca «hecho» por el paso de la fecha.

## S1  Requisitos y diseño  15 sep–12 oct

**Objetivo:** producir una línea base rastreable y un diseño revisable para iniciar el desarrollo sin inventar reglas. Es el bloque de requisitos y diseño del Gantt. No contiene HU implementadas.

| Prioridad | Tarea y vínculos | Cierre verificable |
|---|---|---|
| **Alta** | `SB-S1-01` Consolidar entrevistas, observación y documentos fuente.<br>`HT-PRE-001`; origen de todas las HU. | Registro con actor, fecha, necesidad y dudas; cotejo con catálogo.<br>Estado: Evidencia parcial. |
| **Esencial** | `SB-S1-02` Separar y validar alcance, RF/RNF y decisiones abiertas.<br>`HT-PRE-002`; catálogo y `HU-ACC` a `HU-PUB`. | Matriz confirmado/propuesto/pendiente y acta cuando exista; P-02 a P-14 visibles.<br>Estado: Validación académica pendiente. |
| **Alta** | `SB-S1-03` Preparar arquitectura, datos, permisos y operaciones conjuntas.<br>`HT-PRE-003`; diseño de los cinco módulos. | Modelo conceptual trazado a RF, dueños de escritura y dependencias; revisión de la Directiva según alcance.<br>Estado: Diseño por verificar. |
| **Alta** | `SB-S1-04` Revisar recorridos móviles y preparar diseño de PWA.<br>`HT-PRE-004`; `HU-PWA-001` a `003`, `RNF-UX`. | Pantallas, errores y límites de datos locales; P-13/P-14 visibles.<br>Estado: Validación de interfaz pendiente. |
| **Alta** | `SB-S1-05` Ordenar, estimar y relacionar historias con sprints y pruebas.<br>`HT-PRE-005`, `HT-GEN-008`; pila y factibilidad. | Prioridades, dependencias y capacidad revisadas; exploración de entorno y recuperación sin aprobar P-11.<br>Estado: Estimación pendiente. |

**Hito del 12 de octubre:** documentos preparados y lista honesta de decisiones. La fecha no acredita que todos los puntos hayan sido aprobados.

## S2  Administración y acceso  13–26 oct

**Objetivo:** primer recorrido privado usable, con permisos comprobados en servidor. Corresponde al módulo 1 del Gantt. En SPEC-001 y su plan aprobados figura la etiqueta histórica `S1`; aquí se interpreta como S2 del calendario actualizado.

| Prioridad | Tarea y vínculos | Cierre verificable |
|---|---|---|
| **Esencial** | `SB-S2-01` Preparar proyecto, usuario y base de datos.<br>HU: `HU-ACC-001`<br>HT: `HT-GEN-001` Crítica; `HT-GEN-009` Crítica | Comprobación Django y migraciones PostgreSQL; vínculo RF–HU–prueba. |
| **Esencial** | `SB-S2-02` Entrar, salir y proteger contenido privado.<br>HU: `HU-ACC-001`<br>HT: `HT-GEN-002` Crítica | Cuenta activa accede; cuenta inactiva y petición directa sin permiso se rechazan. |
| **Alta** | `SB-S2-03` Administrar membresías y responsabilidades.<br>HU: `HU-ACC-002`, `HU-ACC-003`<br>HT: `HT-GEN-002` Crítica | Alta/baja autorizada y denegación sin cambios; permisos vigentes. |
| **Alta** | `SB-S2-04` Mostrar opciones propias en móvil y revisar regresión.<br>HU: `HU-ACC-004`<br>HT: `HT-GEN-004` Alta; `HT-GEN-009` Crítica | Inicio privado solo con acciones propias; teclado, 360 px y cierre de sesión probados. |

**Puerta:** completar el diseño y la autorización de implementación de la porción SPEC-001 antes de escribirla. `HU-ACC-002` a `004` entran solo si su detalle y capacidad están preparados.

## S3  Planificación  27 oct–9 nov

**Objetivo:** registrar actividades, asignaciones y encargos, manteniendo el acceso de S2. Corresponde al módulo 2 del Gantt.

| Prioridad | Tarea y vínculos | Cierre verificable |
|---|---|---|
| **Alta** | `SB-S3-01` Registrar y consultar actividades.<br>HU: `HU-PLA-001`, `HU-PLA-004`<br>HT: `HT-GEN-002` Crítica; `HT-S3-001` Alta, propuesta | Fecha, lugar y responsable válidos; socia ve únicamente sus actividades. |
| **Alta** | `SB-S3-02` Asignar personas y encargos vigentes.<br>HU: `HU-PLA-002`, `HU-PLA-003`<br>HT: `HT-S3-001` Alta, propuesta; `HT-GEN-009` Crítica | Cuenta activa se asigna; inactiva y sin permiso se rechazan; encargo vence. |
| **Alta** | `SB-S3-03` Preparar planificación de producción semanal.<br>HU: `HU-CAT-001` como dependencia; `HU-PLA-005`<br>HT: `HT-S3-001` Alta, propuesta | Catálogo mínimo identificado y plan consultable; P-04 resuelto para la porción elegida. |

**Dependencia:** `HU-CAT-001` conserva su bloque productivo principal en S5; se adelanta solo su parte mínima necesaria para `HU-PLA-005`, si se aprueba y estima. Se repiten las pruebas de acceso afectadas.

## S4  Asistencia y continuidad  10–23 nov

**Objetivo:** registrar asistencia y participación con historial; ensayar continuidad sin red solo para operaciones aprobadas. Corresponde al módulo 3 del Gantt.

| Prioridad | Tarea y vínculos | Cierre verificable |
|---|---|---|
| **Esencial** | `SB-S4-01` Entrada, salida, duplicados y consulta.<br>HU: `HU-ASI-001`, `HU-ASI-002`, `HU-ASI-004`<br>HT: `HT-GEN-003` Crítica; `HT-GEN-002` Crítica | Entrada y salida separadas; duplicado rechazado; historial privado. |
| **Esencial** | `SB-S4-02` Correcciones, participación e inconsistencias.<br>HU: `HU-ASI-003`, `HU-ASI-005`, `HU-ASI-006`<br>HT: `HT-GEN-003` Crítica; `HT-GEN-009` Crítica | Actor, motivo y cambio conservados; no se calculan multas automáticamente con P-03 abierta. |
| **Alta** | `SB-S4-03` QR o alternativa de registro.<br>HU: `HU-ASI-007`<br>HT: `HT-S4-001` Alta, propuesta | Decidir P-02/P-13; probar dispositivo, entrada/salida y alternativa. |
| **Esencial** | `SB-S4-04` Preparar captura local y sincronización.<br>HU: `HU-PWA-001`, `HU-PWA-002`, `HU-PWA-003`<br>HT: `HT-GEN-005` Alta; `HT-GEN-006` Crítica; `HT-S4-001` Alta, propuesta | Corte, guardado pendiente, reintento único, permiso revocado y conflicto; P-13/P-14 resueltos. |

**Regla pendiente:** el registro de entrevista comunica USD 0,01 por minuto de atraso, USD 10 desde la primera falta y aviso a la tercera falta. La autoridad, justificativos y procedimiento siguen pendientes de P-03; no se incluye sanción automática en el cierre de S4.

## S5  Trazabilidad productiva y rendición  24 nov–7 dic

**Objetivo:** seguir una cadena verificable desde materia prima hasta existencias. El bloque comercial del Gantt se incorpora según reglas resueltas y capacidad medida. Es el sprint con mayor carga propuesta.

| Prioridad | Tarea y vínculos | Cierre verificable |
|---|---|---|
| **Esencial** | `SB-S5-01` Confirmar catálogo y valores históricos.<br>HU: `HU-CAT-001`, `HU-INV-001`<br>HT: `HT-GEN-003` Crítica | Unidades y valores con vigencia; P-04 resuelto. |
| **Esencial** | `SB-S5-02` Acopio, secado, merma y lotes.<br>HU: `HU-TRA-001`, `HU-TRA-002`, `HU-TRA-003`, `HU-TRA-004`<br>HT: `HT-GEN-003` Crítica; `HT-S5-001` Crítica, propuesta | Pesos, tiempos, procedencia y mermas concilian; P-05 resuelto. |
| **Esencial** | `SB-S5-03` Transformación y existencias.<br>HU: `HU-TRA-005`, `HU-INV-002`<br>HT: `HT-GEN-003` Crítica; `HT-S5-001` Crítica, propuesta | Lote y movimientos explican el saldo; fallo no deja cambios parciales. |
| **Alta** | `SB-S5-04` Entrega y conciliación de feria.<br>HU: `HU-INV-003`, `HU-INV-004`<br>HT: `HT-GEN-003` Crítica; `HT-S5-001` Crítica, propuesta | Custodia, vendido, devuelto y diferencia visibles; sin saldo negativo. |
| **Alta** | `SB-S5-05` Venta y reglas comerciales.<br>HU: `HU-VEN-001`, `HU-VEN-002`, `HU-VEN-003`, `HU-VEN-004`, `HU-VEN-005`, `HU-VEN-006`, `HU-VEN-007`, `HU-VEN-008`<br>HT: `HT-GEN-003` Crítica; `HT-S5-001` Crítica, propuesta | Precio, autorización, stock y valores históricos probados; P-07/P-08/P-10 según el caso. |
| **Alta** | `SB-S5-06` Gastos, saldos y rendición.<br>HU: `HU-GAS-001`, `HU-GAS-002`, `HU-CXC-001`, `HU-CXC-002`, `HU-CXC-003`<br>HT: `HT-GEN-003` Crítica; `HT-S5-001` Crítica, propuesta | Gastos, abonos y cuentas conciliados; P-09 resuelto para la porción incluida. |

**Orden de selección:** `SB-S5-01` a `03` forman la cadena mínima candidata; `04` a `06` requieren estimación propia y decisiones comerciales. El plazo no autoriza declarar terminadas las 23 HU de este bloque. Se repiten pruebas de permisos, integridad, móvil y sincronización cuando afecte pesajes aprobados.

## S6  Reportes, integración y preparación de cierre  8–21 dic

**Objetivo:** producir información desde los recorridos realmente entregados y ejecutar integración, pruebas de uso y preparación de validación. Corresponde al módulo 5 y al inicio del cierre del Gantt.

| Prioridad | Tarea y vínculos | Cierre verificable |
|---|---|---|
| **Alta** | `SB-S6-01` Generar reportes conciliables.<br>HU: `HU-REP-001`, `HU-REP-002`, `HU-REP-003`, `HU-REP-004`, `HU-REP-005`<br>HT: `HT-GEN-007` Alta; `HT-GEN-002` Crítica | PDF, filtros, unidades, totales y permisos contrastados con registros fuente. |
| **Complementaria** | `SB-S6-02` Resumen privado y avisos internos.<br>HU: `HU-REP-006`, `HU-NOT-001`<br>HT: `HT-GEN-002` Crítica; `HT-GEN-009` Crítica | Socia ve solo lo propio; recordatorio identifica pendiente permitido. |
| **Complementaria** | `SB-S6-03` Publicar información autorizada.<br>HU: `HU-PUB-002`, `HU-PUB-001`<br>HT: `HT-GEN-002` Crítica; `HT-GEN-004` Alta | Solo contenido aprobado visible; P-12 y permisos de publicación resueltos. |
| **Esencial** | `SB-S6-04` Integrar y corregir.<br>HU: HU realmente entregadas de S2–S6<br>HT: `HT-S6-001` Crítica, propuesta; `HT-GEN-009` Crítica | Pruebas funcionales, usabilidad, offline aprobado y regresión; defectos registrados y reprobados. |
| **Alta** | `SB-S6-05` Preparar entrega con usuarias.<br>HU: Recorridos entregados<br>HT: `HT-S6-002` Alta, propuesta; `HT-GEN-008` Alta | Manuales fieles a la versión, sesión y capacitación acordadas; evidencia o pendiente explícito. |

## Cierre  22–23 dic

No se abre un nuevo sprint. Se registra lo que fue validado con usuarias, lo que se corrigió y volvió a probarse, los manuales y la capacitación realizada o pendiente. La entrega identifica versión, historias completas, parciales y bloqueadas, sin convertir una demostración en prueba de todas las funciones.

## Control de capacidad y trazabilidad

| Control | Registro exigido al iniciar y revisar cada sprint |
|---|---|
| Selección | IDs HU/HT elegidos, prioridad, estimación, capacidad y responsable. |
| Dependencias | RF, decisión P, diseño, datos y permisos necesarios. |
| Seguimiento | Tarea, estado, bloqueo, esfuerzo restante y cambio de alcance autorizado. |
| Evidencia | Prueba, resultado, revisión con usuarias si ocurre, retrospectiva y versión documental. |

La [pila de producto v1.4](../pila_producto/pila_producto_v1.4_2026-10-13.md) conserva el orden global; este documento muestra cómo se **candidatan** elementos por sprint. Si S5 o S6 supera la capacidad, se revisan recursos, alcance o fecha con el tesista y, cuando corresponda, la directora. Ninguna historia se desplaza ni se marca completa sin registrar la decisión.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.0 | 2026-10-13 | Se prepara el backlog preliminar S1–S6 con 51 HU, 9 HT base y 10 HT candidatas vinculadas a tareas y pruebas. | Sin estimación ni compromiso de capacidad. |
| 1.1 | 2026-10-13 | Se ordenan tablas con prioridad visible, tarea y vínculos HU/HT en una sola columna y cierre separado. | Preparado; sin estimación ni compromiso. |
