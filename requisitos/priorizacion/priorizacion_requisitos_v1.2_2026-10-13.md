---
titulo: Clasificación de requisitos y pendientes por importancia
version: "1.2"
fecha: 2026-10-13
autor: Tesista
estado: final-documental
fuente_entrevista: EVID-ENT-2026-10-12-001
fuente_principal: "CAT-REQ-001 v1.1"
alcance: "60 requisitos confirmados; 2 propuestos; decisiones P-02 a P-14"
prioridad: propuesta-por-validar
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Clasificación de requisitos y pendientes por importancia

## Propósito y forma de lectura

La clasificación ayuda a decidir **qué proteger primero cuando el tiempo es limitado**. No cambia el estado ni elimina ninguno de los 60 requisitos confirmados para la primera versión. Tampoco modifica el orden funcional ni las fechas: S1 cubre requisitos y diseño del 15 de septiembre al 12 de octubre; los cinco sprints de desarrollo son S2–S6. La prioridad de una historia en la pila de producto puede diferir de la importancia de su requisito: una dependencia técnica puede ejecutarse antes que una función más visible.

| Nivel propuesto | Significado | Regla para usarlo |
|---|---|---|
| Esencial | Sin esta capacidad, un recorrido central falla o hay riesgo grave de acceso, pérdida, duplicación o resultado incorrecto. | Diseñar y probar antes de declarar completo el recorrido al que pertenece. |
| Alta | Necesaria para completar los procesos y resultados acordados de la primera versión. | Planificar dentro del sprint correspondiente y verificar sus dependencias. |
| Complementaria | Mejora consulta, comodidad, comunicación o presentación, y sigue dentro del alcance aprobado. | Refinar después del núcleo del mismo bloque; un aplazamiento requeriría decisión humana y cambio de plan. |

La asignación es una **propuesta analítica** basada en impacto organizacional, integridad y seguridad de datos, dependencia de otras funciones, continuidad sin conexión y plazo. No es una nueva validación de la organización o de la directora. Todos los requisitos de las tablas siguientes figuran como `confirmed` en CAT-REQ-001 v1.1.

## Requisitos funcionales confirmados

### Acceso y planificación

| ID | Importancia | Motivo principal |
|---|---|---|
| `RF-ACC-001` | Esencial | Protege la entrada a los datos privados. |
| `RF-ACC-002` | Alta | Permite mantener cuentas vigentes sin borrar historia. |
| `RF-ACC-003` | Esencial | Impide operaciones fuera del cargo o encargo autorizado. |
| `RF-ACC-004` | Complementaria | Facilita encontrar las acciones y pendientes propios. |
| `RF-PLA-001` | Alta | Crea las jornadas y actividades que usan otros recorridos. |
| `RF-PLA-002` | Alta | Deja claras las personas responsables y participantes. |
| `RF-PLA-003` | Alta | Delimita encargos temporales de producción y feria. |
| `RF-PLA-004` | Complementaria | Mejora la consulta de actividades y pendientes. |
| `RF-PLA-005` | Alta | Organiza objetivos semanales y demanda un catálogo de productos. |

### Asistencia y participación

| ID | Importancia | Motivo principal |
|---|---|---|
| `RF-ASI-001` | Esencial | Registra entrada y salida con origen y tiempo diferenciados. |
| `RF-ASI-002` | Esencial | Evita duplicados y conserva inconsistencias para revisión. |
| `RF-ASI-003` | Esencial | Protege correcciones mediante autorización e historial. |
| `RF-ASI-004` | Complementaria | Permite consultar el historial según permisos. |
| `RF-ASI-005` | Complementaria | Añade participación distinta de la asistencia cuando haga falta. |
| `RF-ASI-006` | Alta | Permite resolver inconsistencias sin sanción automática. |
| `RF-ASI-007` | Alta | Aporta QR, código alternativo y delegación auditada; depende de P-02 y P-13. |

### Catálogo, trazabilidad e inventario

| ID | Importancia | Motivo principal |
|---|---|---|
| `RF-CAT-001` | Esencial | Define productos, materias y unidades usados por otros registros. |
| `RF-INV-001` | Esencial | Conserva precios y valores base históricos de las operaciones. |
| `RF-TRA-001` | Esencial | Registra origen y pesaje del acopio para la trazabilidad. |
| `RF-TRA-002` | Esencial | Registra las medidas y tiempos básicos del secado. |
| `RF-TRA-003` | Alta | Calcula duración y merma con fórmula y unidad visibles. |
| `RF-TRA-004` | Esencial | Mantiene procedencia de lotes y diferencia cierre de agotamiento. |
| `RF-TRA-005` | Esencial | Registra transformación y consumo que sustentan el producto final. |
| `RF-INV-002` | Esencial | Toda variación de existencias necesita un movimiento verificable. |
| `RF-INV-003` | Alta | Relaciona entregas de feria con socia, lote y modalidad. |
| `RF-INV-004` | Alta | Concilia cantidades físicas sin confundirlas con deudas. |

### Ventas, gastos y cuentas por cobrar

| ID | Importancia | Motivo principal |
|---|---|---|
| `RF-VEN-001` | Esencial | Registra ventas contra stock autorizado y calcula el total. |
| `RF-VEN-002` | Alta | Identifica al comprador cuando el crédito o contrato lo exige. |
| `RF-VEN-003` | Esencial | Congela valor base y precio para explicar el excedente bruto. |
| `RF-VEN-004` | Esencial | Controla excepciones de venta bajo el valor base. |
| `RF-VEN-005` | Complementaria | Habilita descuentos, pero sus parámetros siguen abiertos en P-08. |
| `RF-VEN-006` | Alta | Separa stock individual y compartido por línea de venta. |
| `RF-VEN-007` | Alta | Cubre ventas institucionales desde stock general. |
| `RF-VEN-008` | Alta | Permite contingencia manual de feria con conciliación posterior; P-10 sigue abierto. |
| `RF-GAS-001` | Alta | Conserva gastos que explican los resultados económicos. |
| `RF-GAS-002` | Complementaria | Resume ingresos y gastos desde registros existentes. |
| `RF-CXC-001` | Esencial | Separa custodia, deuda de socia y crédito externo. |
| `RF-CXC-002` | Esencial | Registra abonos y evita saldos falsos. |
| `RF-CXC-003` | Alta | Cierra la rendición de feria mostrando diferencias. |

### Reportes, recordatorios y sitio público

| ID | Importancia | Motivo principal |
|---|---|---|
| `RF-REP-001` | Alta | Permite revisar asistencia y correcciones por periodo. |
| `RF-REP-002` | Alta | Muestra actividades y encargos pendientes. |
| `RF-REP-003` | Alta | Explica producción, lotes y merma con origen. |
| `RF-REP-004` | Alta | Permite conciliar existencias con movimientos. |
| `RF-REP-005` | Alta | Separa ventas, deudas y pagos en la rendición económica. |
| `RF-REP-006` | Complementaria | Ofrece a cada socia una vista privada de su situación. |
| `RF-NOT-001` | Complementaria | Recuerda tareas y pendientes dentro del sistema. |
| `RF-PUB-001` | Complementaria | Muestra información pública solo después de aprobar el contenido. |
| `RF-PUB-002` | Complementaria | Ordena la publicación y retirada del contenido autorizado. |

### Continuidad sin conexión

| ID | Importancia | Motivo principal |
|---|---|---|
| `RF-PWA-001` | Esencial | Abre la interfaz preparada cuando se corta la red. |
| `RF-PWA-002` | Esencial | Conserva asistencia y pesajes habilitados como pendientes locales. |
| `RF-PWA-003` | Esencial | Sincroniza con revalidación y sin duplicar operaciones. |

## Requisitos no funcionales confirmados

| ID | Importancia | Motivo principal |
|---|---|---|
| `RNF-UX-001` | Esencial | El teléfono es un medio principal para completar tareas. |
| `RNF-UX-002` | Esencial | La accesibilidad permite usar los recorridos esenciales. |
| `RNF-UX-003` | Alta | Reduce errores por lenguaje técnico y cálculos manuales. |
| `RNF-CON-001` | Esencial | La continuidad y los estados locales son obligatorios. |
| `RNF-SEC-001` | Esencial | La autorización debe comprobarse en el servidor. |
| `RNF-AUD-001` | Esencial | Permite reconstruir cambios sensibles. |
| `RNF-DAT-001` | Esencial | Evita movimientos, saldos y registros parciales incorrectos. |
| `RNF-PRV-001` | Esencial | Impide exponer datos privados o recogerlos innecesariamente. |
| `RNF-PDF-001` | Alta | Hace verificables y comprensibles los reportes acordados. |

## Requisitos todavía propuestos, ordenados por importancia

Estos dos **no integran los 60 confirmados**. Su importancia propuesta sirve para decidir qué información aclarar primero; no autoriza construirlos ni convertirlos en requisitos aprobados.

| Orden de atención | ID y estado | Importancia potencial | Motivo y condición para avanzar |
|---:|---|---|---|
| 1 | `RNF-OPS-001` — `proposed` | Alta | La pérdida de datos afectaría la continuidad. P-11 debe definir política, responsables y recuperación antes de confirmar el requisito. La prueba de despliegue también depende de una estrategia verificable. |
| 2 | `RF-COS-001` — `proposed` | Media | Los costos directos conocidos pueden mejorar el análisis económico, pero P-06 debe definir valoración y límites. No se debe presentar costo desconocido como cero ni excedente bruto como ganancia neta. |

## Decisiones abiertas, ordenadas por urgencia de aclaración

Aquí **importancia** significa cuánto afecta al diseño correcto; **urgencia** expresa cuándo conviene resolverla para no bloquear el sprint relacionado. P-01 está cerrado para acceso básico y no aparece como decisión abierta. El orden es propuesto; no constituye resolución de ninguna P.

| Orden | Pendiente | Urgencia | Por qué y qué bloquea |
|---:|---|---|---|
| 1 | `P-03` — consecuencias de faltas y atrasos | Inmediata | La entrevista aporta USD 0,01/min, USD 10 desde la primera falta y aviso a la tercera falta. Faltan justificativos, autoridad, redondeo y cobro; la línea base aún impide sanciones automáticas. |
| 2 | `P-14` — dispositivo, sesión, retención, conflictos, orden y descarte de pendientes | Inmediata | Determina la seguridad y la integridad de la sincronización obligatoria. Bloquea su plan y criterios completos. |
| 3 | `P-13` — acciones offline y reglas de tiempo, QR y secado | Inmediata | Define qué se puede capturar sin red y cuándo se acepta; bloquea las specs de asistencia y pesajes offline. |
| 4 | `P-04` — productos, presentaciones, unidades y conversiones | Inmediata | Afecta el catálogo que necesita la planificación y los movimientos productivos. |
| 5 | `P-11` — política y operación de respaldos | Inmediata | Mantiene propuesto `RNF-OPS-001` y limita la decisión de recuperación del despliegue. |
| 6 | `P-02` — duración del QR, fases y delegación | Alta | Debe cerrarse en la spec de asistencia antes de implementar el QR. |
| 7 | `P-05` — mezclas, divisiones, bajas y cierres excepcionales | Alta | Debe cerrarse antes de automatizar excepciones de lote. |
| 8 | `P-09` — devoluciones, pérdidas, anulaciones y sobrepagos | Alta | Debe cerrarse antes de automatizar ajustes monetarios. |
| 9 | `P-10` — numeración y conciliación del comprobante manual | Alta | Evita doble registro en la contingencia de feria. |
| 10 | `P-08` — condiciones y límites de descuentos | Alta | Impide activar una política de descuento sin valores completos. |
| 11 | `P-12` — contenido y publicadores del sitio | Alta para Sprint 6 | Permite preparar la estructura, pero bloquea la publicación final del contenido. |
| 12 | `P-07` — distribución del excedente compartido | Diferible dentro de su función | No bloquea registrar ventas; bloquea la distribución automática. |
| 13 | `P-06` — fórmula de costo completo | Diferible dentro de su función | Mantiene `RF-COS-001` propuesto; no impide los registros económicos confirmados. |

La prioridad **no implica permiso para inventar** una respuesta. Cada decisión requiere fuente, participantes, fecha y efecto sobre su especificación. La revisión académica de la directora y la validación de la organización para los ajustes v1.1 siguen pendientes y deben registrarse aparte.

## Relación con la pila de producto

La pila de producto de 60 elementos reúne 51 historias de usuario y 9 técnicas; **no equivale** a los 60 requisitos confirmados (51 RF y 9 RNF). Esta clasificación cubre los requisitos canónicos. El orden de la pila queda sin cambios hasta refinarlo con esta propuesta y estimar el trabajo. Ningún nivel de importancia declara una función implementada.

## Fuentes de trabajo

| Fuente | Uso |
|---|---|
| CAT-REQ-001 v1.1, aprobado por el tesista el 28/09/2026 | Estados `confirmed` y `proposed`, reglas y decisiones P-01 a P-14. |
| Requisitos funcionales y no funcionales v1.0, ediciones del 12/10/2026 | Redacción de los 51 RF y 9 RNF. |
| Alcance v1.0 y SPEC-001 | Límites de la primera versión y primer recorrido de acceso. |
| pila de producto vigente v1.1 | Dependencias y secuencia propuesta, sin adoptar su orden como importancia aprobada. |

## Prioridad de aclaración de la entrevista

Los niveles anteriores de los 60 requisitos confirmados no cambian por el resumen.
P-03 pasó del puesto 13 al 1 en la tabla de decisiones tras la aclaración de la
entrevista. La tabla siguiente prioriza **decidir** las novedades, no implementarlas.

| Orden | Tema pendiente | Urgencia para aclarar | Motivo |
|---:|---|---|---|
| 1 | Multas, faltas, atrasos y justificativos | Inmediata | La entrevista precisa USD 0,01/min, USD 10 desde la primera falta y aviso a la tercera falta; P-03 aún requiere autoridad, justificativos y procedimiento antes de automatizar. |
| 2 | Datos de cédulas, firmas y justificativos | Inmediata | Hay riesgo de privacidad si se diseña un repositorio sin permisos ni retención definidos. |
| 3 | Comisiones, costo y valor base en feria y venta mensual | Inmediata | Cálculos erróneos afectarían rendición; relacionar con P-06/P-07/P-09. |
| 4 | Alcance de gestión documental, activos y depreciación | Alta | Puede aumentar mucho el trabajo del calendario vigente. |
| 5 | WhatsApp y avisos al celular | Alta | Cambia el canal confirmado de RF-NOT-001 y añade permisos, costo y fallos. |
| 6 | Inventario personal/general, recetas y mínimos | Alta | Depende de unidades, movimientos y parámetros validados. |
| 7 | Cierre y nueva delegación del secado con evidencia | Alta | Afecta responsabilidades e historial de producción. |
| 8 | Precios públicos y botón de contacto | Alta antes de publicar | Requiere P-12 y definir si es consulta o pedido. |
| 9 | Montos de pérdidas y ahorro esperado | Alta para factibilidad | No hay periodo ni comprobantes para calcular retorno. |

Fuente: EVID-ENT-2026-10-12-001. El orden de la pila de 60 elementos permanece sin cambio hasta una decisión humana.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.1 | 2026-10-12 | Se clasifican los requisitos confirmados y las decisiones abiertas, con impacto de entrevista. | Edición documental; revisión académica pendiente |
| 1.2 | 2026-10-13 | Se alinea la referencia temporal a S1 de diseño y S2–S6 de desarrollo. | Misma clasificación; revisión pendiente |
