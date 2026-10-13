---
titulo: Estudio de factibilidad del proyecto Zhud Alelí
version: "1.2"
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
| Económica | **Condicionada**: inversión de referencia USD 2.869; ahorro real aún no medido | La entrevista aporta USD 80 por día perdido y USD 15 por inconsistencia, pero falta conocer frecuencia y reducción atribuible al sistema. Los escenarios de la sección 5 son ilustrativos; servicios y mantenimiento siguen sin costo verificado. |
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
siguientes y comunica que la organización los aprobó. Falta el acta y la base de
cálculo. Su existencia no significa que el sistema evitará el 100 % de cada pérdida.

| Situación informada | Valor comunicado | Beneficio que sería razonable medir | ¿Se cuenta hoy como ahorro demostrado? |
|---|---:|---|---|
| Tiempo perdido en trámites, búsquedas o coordinación | USD 80 por día | Días equivalentes recuperados al ordenar documentos, agenda, encargos y registros. Puede ser valor de tiempo, aunque no reduzca una salida de caja. | No: faltan días mensuales y medición antes/después. |
| Inconsistencia de productos | USD 15; se supone por caso solo para los ejemplos | Casos evitados mediante movimientos, lotes y conciliación. | No: falta confirmar la unidad, frecuencia, causa y reducción observada. |
| Pérdida en un proyecto grande | USD 20.000 comunicados | Menor riesgo de perder documentación o seguimiento; requiere demostrar frecuencia y cuánto de esa pérdida sería evitable. | No: un caso o monto de riesgo no equivale a beneficio recurrente. |
| Abogado para ordenar papeles | USD 500 por mes durante dos meses; USD 1.000 en ese periodo | Evitar un gasto futuro comparable, solo si se repite y el sistema sustituye efectivamente ese trabajo. | No: el gasto relatado ya ocurrió; no se convierte retroactivamente en ahorro. |

**Cómo ayudaría el sistema:** una carpeta documental con permisos y vencimientos
podría reducir búsquedas y renovaciones tardías; agenda y encargos podrían evitar
viajes o tiempo de coordinación; movimientos de materia prima, lotes e inventario
podrían detectar diferencias antes de una feria o venta; y rendiciones conectadas
podrían facilitar la revisión de dinero y productos. Estas relaciones son
**hipótesis de beneficio** hasta medir el proceso actual y probar el sistema con
la organización. La gestión documental completa, WhatsApp y otras novedades de
la entrevista todavía no están aprobadas para la primera entrega.

### 5.3 Cálculo reproducible del ahorro posible

Para no inventar una cifra única, se usan variables que la organización puede
medir durante un mes comparable:

| Símbolo | Dato que se necesita | Unidad |
|---|---|---|
| d | Días de pérdida de tiempo que el sistema **realmente evita** por mes. | días/mes |
| i | Casos de inconsistencia que el sistema **realmente evita** por mes, si se confirma que USD 15 corresponde a cada caso. | casos/mes |
| c | Costo mensual adicional de operar y mantener el sistema. | USD/mes |
| a | Gasto futuro comprobado de abogado que se evita en los primeros doce meses. Se fija en cero hasta tener evidencia. | USD/año |

**Beneficio económico mensual bruto = USD 80 × d + USD 15 × i.**
El primer término puede representar tiempo recuperado y no necesariamente dinero
que entra en caja. **Beneficio neto simple de los primeros doce meses de operación
= 12 × (80d + 15i − c) + a − 2.869.** Esta cuenta no aplica descuento temporal,
solo compara la inversión inicial con un año de operación; debe recalcularse
cuando se conozcan d, i, c y a. La inversión presupuestada tampoco contempla
de forma verificada todas las funciones nuevas mencionadas en la entrevista.
No se incluye el riesgo de USD 20.000 por carecer de frecuencia y probabilidad.

La tabla siguiente **no pronostica** resultados. Muestra qué arrojaría la fórmula
si, únicamente para ilustrar la sensibilidad, c = 0 y a = 0. Los servicios
y el mantenimiento podrían hacer que el resultado real sea menor.
La recuperación simple divide USD 2.869 para el beneficio mensual ilustrativo;
no es una fecha de recuperación comprometida.

| Escenario ilustrativo | Días evitados/mes (d) | Incidentes evitados/mes (i) | Beneficio económico/mes (USD) | Beneficio en 12 meses (USD) | Diferencia frente a USD 2.869 (USD) | Recuperación simple |
|---|---:|---:|---:|---:|---:|---:|
| Sin mejora medida | 0 | 0 | 0 | 0 | −2.869 | No recupera |
| Ejemplo prudente | 1 | 1 | 95 | 1.140 | −1.729 | 30,20 meses |
| Ejemplo intermedio | 3 | 2 | 270 | 3.240 | +371 | 10,63 meses |
| Ejemplo alto | 5 | 4 | 460 | 5.520 | +2.651 | 6,24 meses |

Para recuperar los USD 2.869 **en los primeros doce meses**, sin gasto operativo
adicional ni otros beneficios, se necesitan al menos **USD 239,09 de beneficio
neto por mes**, redondeando al centavo hacia arriba (2.869 ÷ 12 = 239,0833…).
Por ejemplo, tres días equivalentes recuperados por mes aportarían USD 240/mes
según la valoración comunicada; esto superaría el umbral en USD 0,91/mes y
**no** demostraría ahorro de caja. Si aparece un costo operativo
mensual, el beneficio requerido sube en esa misma cantidad.

### 5.4 Dictamen económico y comprobación posterior

**Con los datos disponibles no puede afirmarse una cantidad de ahorro real ni una
rentabilidad garantizada.** La inversión de referencia es conocida; el ahorro
depende de días e incidentes evitados y de costos operativos no medidos. Los ejemplos
muestran que el proyecto podría recuperar la inversión si produce mejoras
suficientes, pero el escenario prudente no lo hace durante el primer año.

Antes de presentar una cifra de ahorro a la asociación o a la directora:

1. Registrar durante un periodo comparable días perdidos, viajes, impresiones,
   inconsistencias y gastos efectivamente pagados.
2. Registrar esos mismos indicadores después de usar el sistema; separar causas
   ajenas a la aplicación y comprobar qué funciones estaban disponibles.
3. Verificar inversión efectivamente pagada y cotizar operación, archivos,
   mensajes, copias y mantenimiento.
4. Calcular por separado **ahorro de caja** y **valor del tiempo recuperado**.
   No sumar una pérdida eventual de USD 20.000 ni un gasto histórico de USD 1.000
   como si fueran beneficios anuales automáticos.

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
| EVID-ENT-2026-10-12-001 | Entrevista con la tesorera, montos comunicados como aprobados y problemas que el sistema podría reducir. | No hay acta, frecuencia de pérdidas ni prueba de ahorro atribuible. |
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
