---
titulo: Estudio de factibilidad del proyecto Zhud Alelí
version: "1.0"
fecha: 2026-10-12
autor: Codex, para revisión del tesista
estado: candidato-interno
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
| Económica | Presupuesto de referencia **USD 2.869,00**; costo real pendiente | La suma de la fuente está comprobada, pero los importes de servicios en cero y los costos efectivos no están verificados mediante contratación. |
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

La referencia económica más reciente aportada por el tesista es **USD 2.869,00**. La cifra anterior de USD 1.845,00 queda como antecedente histórico. Los importes siguientes son del presupuesto entregado, no cotizaciones actuales ni gastos ejecutados.

| Categoría | Importe de referencia (USD) | Qué debe comprobarse |
|---|---:|---|
| Hardware | 1.527,00 | Disponibilidad y necesidad real de la laptop, computadoras y cable. |
| Software y servicios | 20,00 | Dominio y condiciones efectivas de hosting, base de datos, almacenamiento y respaldo. Los servicios figuran en cero en la fuente. |
| Desarrollo e implementación | 1.200,00 | Dedicación real y ajuste al calendario vigente, distinto de los cuatro meses presupuestados. |
| Materiales | 19,00 | Consumo real durante documentación y capacitación. |
| Energía, Internet y transporte | 103,00 | Duración y viajes reales. |
| **Total de referencia** | **2.869,00** | La suma coincide con la fuente; no representa costo final garantizado. |

El presupuesto se construyó para **cuatro meses**. El periodo 13/10–23/12 comprende aproximadamente 10,3 semanas; no se debe prorratear automáticamente una partida ni afirmar ahorro. Antes de comprometer compras o publicación se necesita una actualización económica conforme al plan ejecutable y las condiciones reales de servicio.

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
| Economía actualizada | Servicios y gastos reales verificados; presupuesto reconciliado con el calendario vigente. |
| Revisión académica | Pronunciamiento de la directora cuando corresponda, sin atribuirlo antes de tener evidencia. |

**Dictamen de esta versión:** factibilidad **condicionada y con riesgo temporal alto**. Hay base de necesidades, arquitectura y recursos para continuar el diseño y las primeras verificaciones; aún no hay evidencia suficiente para asegurar la entrega completa ni la operación del producto dentro del plazo. El dictamen debe actualizarse al cerrar las condiciones anteriores.

## 9. Fuentes y límites de procedencia

| Fuente | Aporte a este estudio | Límite |
|---|---|---|
| CAT-REQ-001 v1.1 y alcance v1.0 | 60 requisitos confirmados, dos propuestos y decisiones pendientes. | Aprobación del tesista; revisión de directora y nueva validación organizacional pendientes para los ajustes. |
| EVID-FACT-001, 28/09/2026 | Texto de factibilidad aportado por el tesista. | No se recibió el archivo original firmado ni se verificó fecha interna. |
| EVID-PLAN-002, 28/09/2026 | Gantt relativo de 16 semanas, presupuesto USD 2.869 y pila tecnológica. | Imágenes y texto de referencia; no demuestran precios actuales ni despliegue. |
| Constitución de ingeniería 0.2.0 y ADR-0006 | Límites de seguridad, arquitectura modular y comprobación por incrementos. | Decisiones técnicas; no sustituyen pruebas ni validación funcional. |
| Calendario confirmado por el tesista para la materia | Inicio de desarrollo 13/10 y fin 23/12/2026. | No contiene estimaciones de capacidad por historia. |

## Historial de cambios

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Codex | Estudio propuesto con cinco dimensiones, presupuesto y discrepancia de plazo explícita. | Candidato interno para revisión del tesista |
