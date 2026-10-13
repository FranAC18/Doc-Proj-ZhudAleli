---
titulo: Estudio de factibilidad del proyecto Zhud Alelí
version: "1.3"
fecha: 2026-10-12
autor: Codex, para revisión del tesista
estado: candidato-interno
fuente_entrevista: EVID-ENT-2026-10-12-001
fuentes: "CAT-REQ-001 v1.1; EVID-FACT-001; EVID-PLAN-002; constitución 0.2.0; alcance v1.0"
revision_directora: pendiente
validacion_organizacion_ajustes_v1_1: no-registrada
publicacion: no-autorizada
---

# Estudio de factibilidad del proyecto Zhud Alelí

## 1. Resumen de la evaluación

El proyecto busca desarrollar una aplicación web para la gestión organizacional y la trazabilidad productiva del Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud. El alcance aprobado por el tesista reúne **51 requisitos funcionales y 9 no funcionales**, incluidos guardado local y sincronización de asistencia y pesajes habilitados. La aplicación Django todavía no existe; los diseños y laboratorios disponibles no demuestran funcionamiento del producto.

| Dimensión | Resultado a esta fecha | Fundamento y límite |
|---|---|---|
| Técnica | Posible en principio; **sin demostración completa** | La arquitectura Django/PostgreSQL/PWA está definida, pero falta probar despliegue de Django, sincronización segura y recuperación. |
| Operativa | Favorable en necesidad; **validación pendiente** | Los procesos y problemas constan en el levantamiento; la facilidad de uso y la aceptación de recorridos necesitan pruebas con las usuarias. |
| Económica | **Condicionada**: inversión de referencia USD 2.869; pérdidas actuales estimadas hasta USD 140/mes en tiempo y productos | El tesista estima un día perdido y cuatro inconsistencias por mes. El ahorro real dependerá de qué parte se evite; los escenarios de la sección 5 no son resultados observados y los costos de operación siguen sin verificarse. |
| Temporal | **Riesgo alto** para el plazo actual | El plan aportado de 16 semanas no cabe en el intervalo confirmado del 13/10 al 23/12/2026, que contiene 72 días calendario, equivalentes a 10 semanas y 2 días. Falta estimar las 60 entradas de la pila candidata. |
| Social y de uso | Potencialmente favorable; **por comprobar** | Móvil, lenguaje claro y accesibilidad están previstos; no hay prueba final con socias ni evidencia de capacitación completada. |

**Conclusión provisional:** la solución es plausible, pero su factibilidad de entrega completa **antes del 23 de diciembre de 2026 no está demostrada**. Se necesita estimar trabajo y capacidad, cerrar decisiones que bloquean diseño, probar el entorno de despliegue y acordar con el tesista cómo tratar cualquier diferencia entre alcance aprobado y tiempo disponible. Este estudio no aprueba recortes, cambios de fecha ni requisitos nuevos.

## 2. Alcance considerado

| Bloque | Qué debe cubrir la primera versión según la línea base | Condición importante |
|---|---|---|
| Acceso y planificación | Cuentas, permisos, actividades, responsabilidades y encargos. | SPEC-001 confirma solo una primera porción de acceso. |
| Asistencia | Entrada, salida, correcciones, inconsistencias y mecanismos QR/código/delegación. | P-02 y P-13 precisan QR y registros sin red. |
| Producción e inventario | Catálogo, acopio, secado, lotes, transformación y movimientos. | P-04 y P-05 precisan unidades y excepciones. |
| Ventas y rendición | Ventas, gastos, saldos, pagos, feria y contingencia manual. | P-07 a P-10 limitan reglas automáticas específicas. |
| Reportes y sitio público | Reportes PDF, recordatorios internos y contenido público autorizado. | P-12 impide publicar contenido no aprobado. |
| Continuidad sin conexión | Interfaz preparada, registros locales habilitados y sincronización sin duplicados. | P-13/P-14 definen alcance y política; guardado local no equivale a aceptación del servidor. |

`RF-COS-001` y `RNF-OPS-001` continúan **propuestos** y no se cuentan entre los 60 confirmados. Los 12 IDs históricos sustituidos tampoco se cuentan como trabajo adicional. La revisión de la directora y la validación de la organización para los ajustes v1.1 no constan realizadas.

## 3. Factibilidad técnica

| Recurso o decisión | Situación respaldada | Verificación que falta |
|---|---|---|
| Desarrollo | Se prevén Python, Django, PostgreSQL, plantillas Django, Bootstrap 5 y un monolito modular. Hay Python 3.12 y PostgreSQL local disponibles según el estado del proyecto. | Crear la aplicación, base de desarrollo, migraciones y un recorrido funcional probado. |
| Equipo y red | La fuente del proyecto describe una laptop de desarrollo, dos computadoras existentes, Wi-Fi e Internet casi estable. El sistema debe usarse también fuera de la organización. | Probar en dispositivos reales y en cortes de red representativos. |
| Base de datos | PostgreSQL es la persistencia prevista; Supabase figura en la factibilidad aportada como opción de servicio administrado. | Confirmar configuración, conexión, límites del servicio, protección de datos y costos efectivos. |
| Ejecución del servidor | La fuente presupuestaria menciona Vercel y Supabase, pero no demuestra dónde ni cómo se ejecutará Django. | Elegir y probar un entorno compatible con Django, archivos, HTTPS, migraciones y operación de sincronización. |
| PWA | Manifest, Service Worker, Cache Storage e IndexedDB están previstos para continuidad esencial. | Prototipo de captura offline, aislamiento por cuenta, reintento sin duplicados, rechazo y conflictos según P-13/P-14. |
| Integridad y acceso | La constitución exige autorización en backend, movimientos auditables y transacciones cuando corresponda. | Pruebas de permisos positivos y negativos, reversión, concurrencia y recuperación de fallos. |
| Respaldo y restauración | `RNF-OPS-001` continúa propuesto. | Cerrar P-11; ensayar una restauración y registrar pérdidas y tiempos tolerables antes de afirmar capacidad operativa. |

La arquitectura elegida evita dividir el producto en servicios independientes, pero no elimina el esfuerzo de los módulos, la PWA ni sus pruebas. La disponibilidad de una tecnología o de un plan gratuito **no demuestra** que la solución completa esté desplegada o sea suficiente para el uso previsto.

## 4. Factibilidad operativa y social

El levantamiento describe asignaciones verbales, omisiones de asistencia y poca trazabilidad de pesajes, secado, lotes e inventario. Centralizar registros responde a necesidades identificadas. Directiva, socias operarias y visitantes tienen usos distintos; las primeras dos clases requieren permisos según cargos o encargos, y el público solo ve contenido aprobado.

| Condición de uso | Medida prevista | Evidencia pendiente |
|---|---|---|
| Uso en teléfonos y distintos niveles de experiencia | Formularios breves, lenguaje cotidiano, controles táctiles, mensajes claros y accesibilidad. | Recorridos con usuarias en dispositivos reales, observaciones y correcciones. |
| Conectividad variable | Recursos esenciales locales, pendientes visibles y sincronización posterior. | Prueba de cortes durante asistencia y pesaje, recuperación y conciliación. |
| Correcciones y decisiones comunitarias | Historial con responsable y motivo; inconsistencias de asistencia esperan decisión de la asamblea. | Validar el procedimiento real y los permisos detallados de cada función. |
| Adopción | Capacitación y manuales previstos. | Material de capacitación, asistencia de participantes y evaluación de comprensión. |
| Privacidad | Datos mínimos, separación público/privado y autorización en servidor. | Revisión de flujos y pruebas de acceso denegado, incluso con sincronización. |

No se cuantifican ahorros de tiempo, ingresos ni aceptación de usuarias porque no hay mediciones antes y después. Los beneficios son **esperados**, sujetos a evaluación.

## 5. Factibilidad económica

### 5.1 Inversión necesaria según el presupuesto recibido

El presupuesto más reciente aportado por el tesista suma **USD 2.869,00**. Es una
estimación para cuatro meses de trabajo, no una factura ni un costo anual de operación.
La cifra anterior de USD 1.845,00 queda como antecedente histórico.

| Categoría | Importe presupuestado (USD) | Observación para decidir |
|---|---:|---|
| Hardware | 1.527,00 | Incluye una laptop de USD 1.512 y cables por USD 15; confirmar si la compra es nueva o si el equipo ya está disponible. |
| Software y servicios | 20,00 | Corresponde al dominio; hosting y base de datos figuran en cero, sin garantía de costo futuro. |
| Desarrollo e implementación | 1.200,00 | Cuatro meses a USD 300 según la fuente; revisar su ajuste al plazo actual. |
| Materiales | 19,00 | Papel, impresiones y útiles del proyecto. |
| Energía, Internet y transporte | 103,00 | Costos presupuestados para ejecutar el proyecto, no gasto anual de la asociación. |
| **Total de inversión de referencia** | **2.869,00** | Suma verificada; no incluye operación posterior comprobada. |

No se cuenta como ahorro de la asociación el papel o transporte de esta misma tabla:
son **costos de desarrollar el proyecto**. El costo posterior de alojamiento, archivos,
mensajería, copias, mantenimiento, soporte y capacitación todavía debe cotizarse.
Tampoco se presume que la laptop pueda eliminarse del presupuesto.
El plazo actual de desarrollo es menor que los cuatro meses presupuestados;
no se ajusta ninguna partida por simple proporción sin revisar recursos y trabajo.

### 5.2 Problema económico que podría reducir el sistema

El tesista atribuye a la entrevista con la tesorera del 12/10/2026 los importes
siguientes y comunica que la organización los aprobó. Aclaró después una frecuencia
aproximada de **un día perdido y cuatro inconsistencias por mes**. Falta el acta,
la base de cálculo y una medición de cuánto reduciría el sistema cada pérdida.

| Situación informada | Valor comunicado | Beneficio que sería razonable medir | ¿Se cuenta hoy como ahorro demostrado? |
|---|---:|---|---|
| Tiempo perdido en trámites, búsquedas o coordinación | Un día aproximadamente por mes × USD 80 = **USD 80/mes**, **USD 960/año** | Días equivalentes recuperados al ordenar documentos, agenda, encargos y registros. Es valor de tiempo y puede no reducir una salida de caja. | No: la frecuencia es estimada y falta medir reducción antes/después. |
| Inconsistencia de productos | Cuatro aproximadamente por mes × USD 15 = **USD 60/mes**, **USD 720/año**, si USD 15 corresponde a cada caso | Casos evitados mediante movimientos, lotes y conciliación. | No: confirmar unidad, causa y reducción observada. |
| Pérdida en un proyecto grande | USD 20.000 comunicados | Menor riesgo de perder documentación o seguimiento; requiere demostrar frecuencia y cuánto de esa pérdida sería evitable. | No: un caso o monto de riesgo no equivale a beneficio recurrente. |
| Abogado para ordenar papeles | USD 500 por mes durante dos meses; **USD 1.000 por periodo** | El tesista indica que volvería a pagarse si los documentos siguen desordenados. Podría evitarse un nuevo periodo solo si la gestión documental aprobada sustituye esa labor administrativa. | No: no se conoce cada cuánto se repite ni qué parte del trabajo del abogado es evitable. |

Las dos pérdidas mensuales estimadas suman **USD 140/mes** o **USD 1.680 en doce meses**
si ambas frecuencias se mantienen. Esta es la **pérdida actual de referencia**, no el
ahorro logrado por una aplicación que todavía no existe. De los USD 140, USD 80
representan valor de tiempo y USD 60 son pérdidas de producto bajo el supuesto
de USD 15 por cada inconsistencia.

**Cómo ayudaría el sistema:** una carpeta documental con permisos y vencimientos
podría reducir búsquedas y renovaciones tardías; agenda y encargos podrían evitar
viajes o tiempo de coordinación; movimientos de materia prima, lotes e inventario
podrían detectar diferencias antes de una feria o venta; y rendiciones conectadas
podrían facilitar la revisión de dinero y productos. Estas relaciones son
**hipótesis de beneficio** hasta medir el proceso actual y probar el sistema con
la organización. La gestión documental completa, WhatsApp y otras novedades de
la entrevista todavía no están aprobadas para la primera entrega.

### 5.3 Cálculo reproducible del ahorro posible

La estimación de partida es **un día y cuatro inconsistencias por mes**. Se aplica
una proporción de reducción a esas pérdidas, sin suponer que el sistema las
eliminará por completo. Si ambas bajan en la misma proporción, el cálculo es:

**Beneficio económico mensual = (USD 80 + 4 × USD 15) × proporción evitada
= USD 140 × proporción evitada.** El ahorro de caja por productos sería,
como máximo bajo estos datos, USD 60/mes; los otros USD 80 son valor de tiempo
recuperado y solo serían ahorro de caja si se demuestra un gasto que deja de pagarse.

Para un análisis con reducciones distintas: **beneficio mensual = USD 80 × proporción
de tiempo evitado + USD 60 × proporción de inconsistencias evitadas**.
Luego se restan los costos mensuales de operación y la inversión inicial. El gasto
del abogado se añade solo en el periodo futuro en que se demuestre que se evitó.

La tabla supone **costo operativo adicional USD 0** y **ningún nuevo periodo del
abogado evitado** para mostrar el efecto aislado de los datos mensuales. Son
supuestos de cálculo, no condiciones verificadas ni una predicción. La columna de
recuperación divide USD 2.869 entre el beneficio mensual y no promete una fecha.

| Reducción ilustrativa de ambas pérdidas | Beneficio por tiempo/mes | Pérdida de producto evitada/mes | Beneficio económico/mes (USD) | Beneficio en 12 meses (USD) | Diferencia frente a USD 2.869 (USD) | Recuperación simple |
|---|---:|---:|---:|---:|---:|---:|
| 0 % | 0 | 0 | 0 | 0 | −2.869 | No recupera |
| 50 % | 40 | 30 | 70 | 840 | −2.029 | 40,99 meses |
| 100 % | 80 | 60 | 140 | 1.680 | −1.189 | 20,49 meses |

**Posible gasto futuro del abogado, por separado.** El tesista señala que se
volverían a pagar USD 500 por mes durante dos meses si no se ordenan los papeles.
Si se demuestra que una función documental aprobada evita **un** nuevo periodo
completo, el beneficio adicional de ese episodio sería USD 1.000. No se conoce
cada cuánto ocurriría ni si la aplicación puede reemplazar todo ese trabajo.

| Supuesto adicional durante los primeros 12 meses | Beneficio de tiempo y producto en 12 meses | Abogado evitado una vez | Beneficio económico total (USD) | Diferencia frente a USD 2.869 (USD) |
|---|---:|---:|---:|---:|
| Reducción del 50 % y un periodo futuro de abogado totalmente evitable | 840 | 1.000 | 1.840 | −1.029 |
| Reducción del 100 % y un periodo futuro de abogado totalmente evitable | 1.680 | 1.000 | 2.680 | −189 |

Para recuperar los USD 2.869 **en los primeros doce meses**, sin costo operativo,
se necesitarían al menos **USD 239,09 de beneficio por mes**. Las dos pérdidas
mensuales comunicadas suman como máximo USD 140/mes si se evitan por completo;
incluso añadiendo un periodo de abogado totalmente evitable, el beneficio del
primer año sería USD 2.680, **USD 189 menos** que la inversión. Cada USD 10/mes
de operación reduciría el resultado de doce meses en USD 120. No se incluye la
posible pérdida de USD 20.000 por faltar frecuencia y probabilidad.

### 5.4 Dictamen económico y comprobación posterior

**Ahorro económico potencial medible:** hasta USD 140 por mes o USD 1.680 por año
en los dos problemas recurrentes descritos, **solo si el sistema elimina ambos
por completo** y se confirma USD 15 por cada inconsistencia. De ese total,
USD 60/mes corresponderían a pérdidas de producto evitadas y USD 80/mes al valor
del tiempo recuperado. El gasto futuro del abogado podría añadir USD 1.000 por
un periodo de dos meses evitado, una sola vez por episodio demostrado. **Ahorro
real observado: todavía USD 0 documentados**, porque la aplicación no existe.

La factibilidad económica es **condicionada**: con las pérdidas periódicas hoy
descritas, ni siquiera evitarlas al 100 % recuperaría la inversión en el primer
año. Un periodo de abogado evitable acercaría el punto de recuperación, pero no
lo alcanzaría en ese año y requiere una función documental cuyo alcance y costo
adicional todavía no están aprobados. Sin ese gasto, la recuperación simple de
20,49 meses exige sostener la eliminación completa de ambas pérdidas y no tener
costos operativos adicionales, condiciones que aún no se han demostrado.

Antes de presentar una cifra de ahorro a la asociación o a la directora:

1. Verificar durante meses comparables el día perdido y las cuatro inconsistencias
   mensuales aproximadas; confirmar que USD 15 corresponde a cada caso.
2. Registrar esos mismos indicadores después de usar el sistema; separar causas
   ajenas a la aplicación y comprobar qué funciones estaban disponibles.
3. Verificar inversión efectivamente pagada y cotizar operación, archivos,
   mensajes, copias y mantenimiento.
4. Calcular por separado **ahorro de caja** y **valor del tiempo recuperado**.
   Contar un nuevo gasto de abogado solo si se prueba que se habría repetido y
   que el sistema lo evitó. No sumar la pérdida eventual de USD 20.000 como
   beneficio anual automático.

Como referencia metodológica, la guía oficial de evaluación del Tesoro británico
distingue costos iniciales y operativos, beneficios en efectivo y no monetarios,
y aconseja comprobar la sensibilidad de los resultados a supuestos inciertos:
[The Green Book (2026)](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026).
Se usa para ordenar el análisis, **no** como norma aplicable a la organización.

## 6. Factibilidad temporal

La evidencia anterior muestra un Gantt de **16 semanas relativas**. El calendario confirmado después por el tesista fija diseño y requisitos hasta el **13/10/2026**, desarrollo del **13/10 al 23/12/2026** y cinco sprints. Son dos referencias distintas; el Gantt de 16 semanas no demuestra que las mismas actividades quepan en el nuevo plazo.

| Tramo del calendario vigente | Fechas | Duración calendario | Resultado esperado para comprobar avance |
|---|---|---:|---|
| Sprint 1 | 13–26 oct | 14 días | Acceso verificable y base técnica. |
| Sprint 2 | 27 oct–9 nov | 14 días | Planificación y encargos verificables. |
| Sprint 3 | 10–23 nov | 14 días | Asistencia y continuidad que le corresponde, con pruebas. |
| Sprint 4 | 24 nov–7 dic | 14 días | Producción, inventario y operación comercial según alcance refinado. |
| Sprint 5 | 8–21 dic | 14 días | Reportes, información y sitio público aprobado; integración y regresión. |
| Cierre | 22–23 dic | 2 días | Evidencia final, revisión y entrega documental. |
| **Total** | **13 oct–23 dic** | **72 días = 10 semanas y 2 días** | Requiere capacidad estimada y seguimiento por sprint. |

Los objetivos de la tabla son una **referencia para evaluar viabilidad**, no compromisos de completar todas las funciones sin estimación. La pila candidata contiene **51 historias de usuario y 9 técnicas**, todas sin estimación del equipo. Además, Sprint 4 concentra catálogo, acopio, secado, lotes, inventario, ventas, gastos y cuentas por cobrar; esto representa un riesgo de carga particularmente alto. La PWA debe diseñarse e integrarse con los recorridos afectados y no reservarse solo para la revisión final.

El cierre de requisitos y diseño fijado para el 13/10 también necesita comprobarse: la revisión de la directora no consta realizada y las tareas de diseño de SPEC-001 permanecen planificadas en el estado consultado. No se presenta esa fase como cerrada por el solo hecho de existir documentos.

Para sostener el 23/12 se necesita, antes de dar por factible el calendario: estimar historias, conocer disponibilidad real del tesista y participantes, resolver dependencias críticas, reservar tiempo para pruebas y validación, y comparar capacidad por sprint con el alcance confirmado. Si la comparación no cierra, cualquier ajuste de fecha, recursos, entrega o alcance debe registrarse y aprobarse por la autoridad correspondiente; este documento no lo decide.

## 7. Riesgos y acciones de comprobación

| Riesgo | Impacto | Acción de comprobación | Estado |
|---|---|---|---|
| 16 semanas planificadas frente a 10 semanas y 2 días disponibles | No completar o no probar todo el alcance | Estimar pila y capacidad; revisar por sprint la brecha. | Abierto; alto |
| Cierre de diseño previsto para el 13/10 sin evidencia completa | Empezar desarrollo con decisiones o revisión académica pendientes | Revisar entregables y puertas de diseño; registrar qué está aprobado y qué sigue abierto. | Abierto; alto |
| P-13/P-14 sin resolver | Errores de tiempo, privacidad, duplicados o conflictos offline | Cerrar políticas con fuente y probar cortes/reintentos antes de aceptar resultados. | Abierto; alto |
| Entorno Django no verificado | Demora o imposibilidad de publicar una versión utilizable | Probar despliegue mínimo, conexión PostgreSQL, HTTPS, archivos y migración. | Abierto; alto |
| P-11 y restauración sin política | Pérdida de datos o recuperación incierta | Definir responsabilidades y ensayar restauración. | Abierto; alto |
| Reglas de negocio pendientes P-02, P-04, P-05 y P-07 a P-10 | Rehacer funciones o producir resultados erróneos | Resolver cada decisión antes de su parte afectada; no inventar valores. | Abierto |
| Servicios presupuestados en cero | Costo de operación superior al presupuestado | Verificar condiciones, límites y costos efectivos del entorno elegido. | Abierto |
| Validación con usuarias y directora no registrada para ajustes v1.1 | Diseño o documentación sin revisión suficiente | Programar revisión académica y recorridos con usuarias; conservar actas. | Abierto |

## 8. Condiciones para emitir un dictamen final

| Condición | Evidencia mínima esperada |
|---|---|
| Alcance y prioridades revisados | Requisitos y pila refinada sin confundir 60 requisitos con 60 historias. |
| Tiempo calculado | Estimaciones de las historias, disponibilidad del equipo y capacidad por sprint. |
| Operación técnica demostrada | Despliegue mínimo Django/PostgreSQL; prueba PWA y sincronización en un recorrido real. |
| Integridad y recuperación comprobadas | Casos de permisos, duplicados, transacciones y restauración conforme a la política aprobada. |
| Uso validado | Pruebas de recorridos móviles y accesibles con usuarias y registro de observaciones. |
| Economía actualizada | Inversión y operación verificadas; días e inconsistencias antes/después, ahorro de caja separado de valor de tiempo y escenarios recalculados. |
| Revisión académica | Pronunciamiento de la directora cuando corresponda, sin atribuirlo antes de tener evidencia. |

**Dictamen de esta versión:** factibilidad **condicionada y con riesgo temporal alto**. Hay base de necesidades, arquitectura y recursos para continuar el diseño y las primeras verificaciones; aún no hay evidencia suficiente para asegurar la entrega completa ni la operación del producto dentro del plazo. El dictamen debe actualizarse al cerrar las condiciones anteriores.

## 9. Fuentes y límites de procedencia

| Fuente | Aporte a este estudio | Límite |
|---|---|---|
| CAT-REQ-001 v1.1 y alcance v1.0 | 60 requisitos confirmados, dos propuestos y decisiones pendientes. | Aprobación del tesista; revisión de directora y nueva validación organizacional pendientes para los ajustes. |
| EVID-FACT-001, 28/09/2026 | Texto de factibilidad aportado por el tesista. | No se recibió el archivo original firmado ni se verificó fecha interna. |
| EVID-PLAN-002, 28/09/2026 | Gantt relativo de 16 semanas, presupuesto USD 2.869 y pila tecnológica. | Imágenes y texto de referencia; no demuestran precios actuales ni despliegue. |
| EVID-ENT-2026-10-12-001 | Entrevista con la tesorera, montos aprobados según el tesista y frecuencias mensuales aproximadas. | No hay acta ni medición antes/después que pruebe reducción atribuible al sistema. |
| [The Green Book (2026)](https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government/the-green-book-2026), HM Treasury | Método de referencia para separar costos y beneficios y examinar supuestos. | Guía externa de análisis; no es norma ecuatoriana ni valida importes de la asociación. |
| Constitución de ingeniería 0.2.0 y ADR-0006 | Límites de seguridad, arquitectura modular y comprobación por incrementos. | Decisiones técnicas; no sustituyen pruebas ni validación funcional. |
| Calendario confirmado por el tesista para la materia | Inicio de desarrollo 13/10 y fin 23/12/2026. | No contiene estimaciones de capacidad por historia. |

## 10. Impacto de la entrevista en otras dimensiones

| Dimensión | Nueva cuestión de factibilidad |
|---|---|
| Técnica | Archivos, firmas, avisos externos, reglas temporales, inventario personal y depreciación requieren diseño y pruebas propias. La validez legal de firma o notificación no está demostrada. |
| Operativa | Hay que comprobar quién mantiene documentos, resuelve justificativos, valida tareas, atiende mensajes y concilia comisiones. |
| Temporal | Incluir nuevas capacidades en la entrega del 23/12 ampliaría la brecha ya identificada entre 16 semanas de plan y 72 días disponibles. |
| Privacidad y confianza | Cédulas, firmas y justificativos exigen controles antes de almacenar datos reales. El tesista comunica una regla de USD 0,01/min de atraso, USD 10 desde la primera falta y aviso a la tercera falta; faltan registro formal, excepciones y procedimiento antes de implementarla. |

El dictamen general se mantiene **condicionado, con riesgo temporal alto**. La
evaluación económica detallada está en la sección 5. Cualquier ampliación de
alcance o cambio de plazo requiere decisión expresa y presupuesto/calendario
revisados.

## Historial de cambios

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Codex | Estudio propuesto con cinco dimensiones, presupuesto y discrepancia de plazo explícita. | Candidato interno para revisión del tesista |
| 1.1 | 2026-10-12 | Codex | Se incorporó el impacto del resumen de entrevista sin cambiar el alcance confirmado. | Candidato interno |
| 1.2 | 2026-10-12 | Codex | Se precisó inversión, beneficio posible, fórmulas, escenarios y punto de recuperación sin atribuir ahorro medido. | Candidato interno |
| 1.3 | 2026-10-12 | Codex | Se calcularon pérdidas mensuales comunicadas, escenarios de reducción y gasto futuro condicional de abogado. | Candidato interno |
