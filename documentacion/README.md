---
titulo: Índice de documentación final de Zhud Alelí
version: "5.11"
fecha: 2026-10-30
autor: Tesista
estado: preparado-para-revision-academica
publicacion: parcialmente-publicada
---

# Documentación final de Zhud Alelí

## Diseño de base de datos — 2026-10-30

La [base consolidada v2.1](arquitectura/diseno_base_datos_v2.1_2026-10-30.md), el [ER integral v2.1](arquitectura/modelo_er_integral_v2.1_2026-10-30.md) y la [nota de correspondencia con las tablas Django](arquitectura/uso_tablas_django_login_en_diseno_v1.0_2026-10-30.md) están preparados para revisión. El ER distingue las 13 tablas físicas verificadas de las entidades de negocio propuestas y documenta la reutilización de las cuentas y permisos técnicos.

Control de cambios: [registro v5.11](control_de_cambios/registro_v5.11_2026-10-30.md). La implementación de dominio y la publicación al docente siguen pendientes.

Este índice reúne las ediciones documentales del proyecto de la materia Aplicaciones
Informáticas II. Cada documento indica versión, fecha, autor, estado e historial.
Las ediciones anteriores se conservan y aquí se señala la vigente. El estado de publicación
es parcial: requisitos generales v2.0 y priorización v1.3 se publicaron con autorización del
tesista el 2026-10-14; el compendio Word v1.6 y el plan/backlog Word v1.7 ya se habían publicado.
Los demás documentos de esta tabla conservan su estado de revisión o publicación indicado.
**Preparado** no significa revisado por la directora. Las ediciones actualizadas el 2026-10-21 y los planes de sprints y superadministración del 2026-10-27 permanecen preparados localmente para revisión; no se han transferido al repositorio documental del docente. La edición actual registra que la Superadministradora realizará las acciones normales de todos los módulos y administrará sus registros y opciones publicadas desde un panel, según decisión expresa del tesista; los detalles por módulo siguen en propuesta.

La edición de seguimiento del 19 de octubre documenta el cierre histórico de S0 y los pendientes posteriores; está preparada para revisión y pendiente de transferencia al repositorio del docente. La arquitectura detallada v1.1 fue aprobada por el tesista para documentación; su transferencia sigue pendiente. El informe de S1 v1.2 registra el cierre administrativo parcial y la aceptación del tesista del 2026-10-21 para asignar HT-PRE-001 a HT-PRE-005 a S1, con los estados y pendientes registrados entonces. El 2026-10-27 el tesista decidió extender hasta ese día la definición documental de acceso y superadministración en S1 y concentrar login, cuentas, permisos y estructura de módulos en S2. Las funciones de los módulos se distribuyen entre S3 y S5. El cierre propuesto de S2 es el 8 de noviembre; las fechas intermedias están sujetas a revisión. El periodo de S1 se registra concluido por calendario; la finalización de sus entregables requiere cotejo y evidencia. El tesista comunicó una disponibilidad de 16–25 horas semanales, aún no convertida en estimaciones por historia.

La edición del 2026-10-28 incorpora arquitectura v1.2 con la organización modular de backend y frontend aprobada por el tesista. Conserva las ediciones anteriores y diferencia esa aprobación técnica de la revisión de la nueva edición completa. La aplicación cuenta con desarrollo local parcial; la adaptación más reciente del frontend no se presenta como una entrega aceptada. Esta edición se publica en el repositorio documental para revisión docente. La publicación no equivale a aprobación académica.

## Actualización local de acceso — 2026-10-28

El tesista aceptó la ampliación de acceso por correo, passkeys y WhatsApp configurable. Las ediciones nuevas contienen ese alcance aceptado y pendiente de implementación; su revisión académica y transferencia al docente siguen pendientes. Las aprobaciones y publicaciones anteriores conservan su alcance histórico.

| Área | Nueva edición de consulta | Versión | Estado |
|---|---|---|---|
| requisitos | [requisitos_generales_v2.2_2026-10-28.md](requisitos/requisitos_generales_v2.2_2026-10-28.md) | 2.2 | Alcance de acceso aceptado por el tesista; preparado para revisión, sin implementación acreditada. |
| hu | [historias_usuario_v2.7_2026-10-28.md](historias/usuario/historias_usuario_v2.7_2026-10-28.md) | 2.7 | Alcance de acceso aceptado por el tesista; preparado para revisión, sin implementación acreditada. |
| ht | [historias_tecnicas_v1.8_2026-10-28.md](historias/tecnicas/historias_tecnicas_v1.8_2026-10-28.md) | 1.8 | Alcance de acceso aceptado por el tesista; preparado para revisión, sin implementación acreditada. |
| pila | [pila_producto_v1.9_2026-10-28.md](pila_producto/pila_producto_v1.9_2026-10-28.md) | 1.9 | Alcance de acceso aceptado por el tesista; preparado para revisión, sin implementación acreditada. |
| backlog | [sprint_backlog_v1.5_2026-10-28.md](sprints/sprint_backlog_v1.5_2026-10-28.md) | 1.5 | Alcance de acceso aceptado por el tesista; preparado para revisión, sin implementación acreditada. |
| Control de cambios | [Registro v5.2](control_de_cambios/registro_v5.2_2026-10-28.md) | 5.2 | Preparado localmente; publicación pendiente. |

La tabla siguiente conserva el corte anterior y los estados de publicación históricos; para acceso se consultan las nuevas ediciones anteriores. Los formatos Word conservan su corte previo.

## Corte documental anterior y publicaciones conservadas

| Área | Documento vigente | Versión | Qué representa |
|---|---|---:|---|
| Seguimiento | [Cierre de S0 y continuidad](seguimiento/cierre_sprint_0_y_continuidad_v1.0_2026-10-19.md) | 1.0 | Cierre histórico aprobado; correspondencia de etapas y pendientes. Preparado, no publicado. |
| Seguimiento | [Cierre de S1 y vistos buenos verbales](seguimiento/cierre_sprint_1_y_vistos_buenos_v1.2_2026-10-21.md) | 1.2 | Timebox cerrado con resultado parcial; registra la aceptación posterior de HT-PRE-001 a HT-PRE-005 para S1, sin cambiar sus estados de cumplimiento. Preparado para revisión, no publicado. |
| Seguimiento | [Cobertura y pendientes](seguimiento/pendientes_trazabilidad_v1.0_2026-10-19.md) | 1.0 | Siete RF sin referencia en HU/pila y ampliaciones por cotejar; pendientes posteriores a S0. |
| Levantamiento | [Registro de entrevista](levantamiento/registro_entrevista_v1.1_2026-10-13.md) | 1.1 | Cotejo de los doce temas con CAT-REQ-001 v1.2; acta formal y validaciones pendientes. |
| Alcance general del proyecto | [Markdown](alcance/alcance_v1.3_2026-10-13.md), [Word con formato ZHUD ALELÍ](alcance/alcance_v1.3_2026-10-13.docx) | 1.3 | Mismo contenido en ambos formatos; alineado con CAT v1.2, requisitos generales v2.0 y plan de sprints v1.2. Preparado para revisión del tesista, no aprobado en esta edición. |
| Requisitos | [Línea base aprobada](requisitos/requisitos_generales_v2.0_2026-10-13.md) | 2.0 | 58 RF y 9 RNF confirmados, RF-COS-001 y RNF-OPS-001 propuestos; aprobada por el tesista y publicada el 2026-10-14. |
| Requisitos | [Edición ampliada candidata](requisitos/requisitos_generales_v2.1_2026-10-27.md) | 2.1 | Conserva la línea base y añade RF-ACC-005 propuesto con alcance transversal de Superadministración; preparada para revisión, no publicada. |
| Requisitos | [Funcionales — detalle anterior](requisitos/funcionales/requisitos_funcionales_v1.1_2026-10-12.md) | 1.1 | Detalle de la línea base previa de 51 RF; la lista vigente y completa es la general v2.0. |
| Requisitos | [No funcionales — detalle anterior](requisitos/no_funcionales/requisitos_no_funcionales_v1.1_2026-10-12.md) | 1.1 | Detalle de los 9 RNF; consultar la general v2.0 para la redacción vigente y alcance actualizado. |
| Requisitos | [Importancia y pendientes](requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13.md) | 1.3 | Importancia aprobada por el tesista para la línea base y las novedades v2.0; publicada el 2026-10-14. El orden de trabajo no cambia. Revisión académica pendiente. |
| Historias | [Línea base de usuario](historias/usuario/historias_usuario_v2.5_2026-10-13.md) | 2.5 | 51 fichas de usuario conservadas. |
| Historias | [Edición ampliada candidata](historias/usuario/historias_usuario_v2.6_2026-10-27.md) | 2.6 | Conserva 51 fichas, refina acceso y añade cinco historias candidatas de Superadministración; preparada para revisión. |
| Historias | [Técnicas](historias/tecnicas/historias_tecnicas_v1.7_2026-10-21.md) | 1.7 | 19 fichas ordenadas por primer sprint previsto; incluye 9 HT de línea base, 5 aceptadas para S1 y 5 propuestas posteriores. |
| Historias y pila | [Compendio general Word, edición conservada](historias/historias_usuario_tecnicas_pila_v1.6_2026-10-14.docx) | 1.6 | Última edición Word existente; no se modificó en la actualización Markdown del 2026-10-21. |
| Planificación | [Pila de producto anterior](pila_producto/pila_producto_v1.7_2026-10-21.md) | 1.7 | 65 registros principales del corte anterior: 60 de línea base y 5 HT-PRE aceptadas. |
| Planificación | [Pila ampliada candidata](pila_producto/pila_producto_v1.8_2026-10-27.md) | 1.8 | Conserva las 65 filas de base, agrega cinco historias candidatas fuera de ella y muestra el orden de trabajo S2–S5; preparada para revisión. |
| Planificación | [Fases y sprints](sprints/plan_sprints_v1.6_2026-10-27.md) | 1.6 | Objetivo 2 hasta el 23 de diciembre; S2–S5 por complejidad y capacidad orientativa; flujo ágil y alcance transversal del panel. Fechas intermedias propuestas; preparado para revisión. |
| Planificación | [Sprint backlog, corte anterior](sprints/sprint_backlog_v1.4_2026-10-21.md) | 1.4 | 27 fichas S1–S6 del corte anterior. Sus compromisos no se mueven automáticamente; el backlog se actualizará por tareas seleccionadas. |
| Planificación | [Criterios de acceso y superadministración](sprints/plan_implementacion_superadmin_v1.4_2026-10-27.md) | 1.4 | Autoridad transversal y edición de registros, valores y opciones desde el panel, con criterios S2 y S3–S5. RF-ACC-005 y detalles por módulo siguen propuestos; evidencia presidencial pendiente. |
| Planificación | [Plan incremental y sprint backlog Word, edición conservada](sprints/plan_incremental_y_sprint_backlog_v1.7_2026-10-14.docx) | 1.7 | Última edición Word existente; no se modificó en la actualización Markdown del 2026-10-21. |
| Evaluación | [Factibilidad, corte anterior](factibilidad/factibilidad_v1.4_2026-10-13.md) | 1.4 | Costos y escenarios de ahorro conservados; su calendario S1–S6 corresponde al corte anterior y requiere revisión frente al plan v1.6. |
| Diseño | [Arquitectura detallada](arquitectura/arquitectura_v1.2_2026-10-28.md) | 1.2 | Backend por módulo y frontend por pantalla según convención aprobada; recursos compartidos y transición verificable. Implementación local parcial y adaptación presente sin acreditar entrega completa. Publicada para revisión académica; aceptación docente pendiente. |
| Diseño | [Criterios de interfaz](diseno/criterios_diseno_v1.0_2026-10-12.md) | 1.0 | Criterios de uso; identidad visual pendiente de validar. |
| Pruebas | [Plan de pruebas](pruebas/plan_pruebas_v1.0_2026-10-12.md) | 1.0 | Pruebas previstas; ningún resultado adelantado. |
| Gobierno | [Control de cambios](control_de_cambios/registro_v5.1_2026-10-28.md) | 5.1 | Registra arquitectura v1.2, la convención aprobada de modularidad y la diferencia entre diseño e implementación local; edición publicada para revisión académica. |

## Ediciones anteriores conservadas

El [compendio Word v1.0](historias/historias_usuario_tecnicas_pila_v1.0_2026-10-13.docx)
y el [plan Word v1.1](sprints/plan_incremental_y_sprints_v1.1_2026-10-13.docx)
usan la numeración anterior S1–S5 para desarrollo. Se conservan como historial;
para el calendario y las prioridades actuales se usan las ediciones vigentes de
la tabla.

También se conservan las ediciones HU v2.3–v2.4, HT v1.4, pila v1.3–v1.4,
sprint backlog v1.0–v1.1 y plan Word v1.2–v1.3. Las ediciones vigentes usan
fichas individuales y dejan los códigos como referencias secundarias.

Las arquitecturas [v1.0](arquitectura/arquitectura_v1.0_2026-10-12.md) y [v1.1](arquitectura/arquitectura_v1.1_2026-10-19.md) se conservan como ediciones anteriores. La v1.1 mantiene su aprobación editorial histórica; la v1.2 de la tabla es la edición actual publicada para revisión académica. El [control de cambios v5.0](control_de_cambios/registro_v5.0_2026-10-27.md) conserva el corte documental anterior.

El registro de entrevista v1.0 se conserva como antecedente; el registro vigente es v1.1,
cotejado con CAT-REQ-001 v1.2. El informe de S1 documenta los vistos buenos verbales que
el tesista atribuye a Maria Camas y Julio Santillan. Como no se precisaron fecha, versión,
alcance ni existe acta o constancia, no se asignan a cambios concretos del registro de
entrevista.

La autoría correcta de los documentos Word es Franklin Acero. Se corrigieron
las propiedades de las ediciones anteriores para evitar atribuciones erróneas.

El corte histórico publicado v2.0 contiene 58 RF y 9 RNF confirmados. La edición vigente local v2.2 y CAT-REQ-001 v1.3 contienen **62 RF y 9 RNF confirmados por el tesista**, además de RF-COS-001, RF-ACC-005 y RNF-OPS-001 propuestos. La ampliación de acceso del 2026-10-28 tiene implementación y validación de recorridos pendientes. El tesista aprobó la edición general v2.0 y CAT-REQ-001 v1.2; la revisión de la directora y la validación directa de la organización para las novedades siguen pendientes. Sprint 0 está cerrado desde el 21 de julio de 2026. S1 permanece parcial. La app tiene pruebas locales de acceso registradas en el estado operativo; eso no declara terminada la aplicación.

El reporte de revisión docente del 13 de octubre conserva lo conocido en esa fecha. El
informe de S1 del 20 de octubre incorpora la actualización del tesista: Julio Santillan,
profesor de Aplicaciones II, dio visto bueno durante una presentación. La versión exacta y
el alcance no están identificados; el informe no representa confirmación directa ni acta.
Maria Camas, encargada de la organización, también autorizó verbalmente, según el tesista,
sin fecha o alcance documentados. El alcance general v1.3 permanece preparado para revisión.

El documento general v2.0 conserva su aprobación y publicación históricas; la **edición vigente local de consulta es v2.2**, con el acceso aceptado el 2026-10-28. Su revisión académica y transferencia siguen pendientes; RF-ACC-005 conserva estado propuesto. Las ediciones funcional y no funcional v1.1 conservan el detalle anterior. Los documentos derivan del catálogo interno CAT-REQ-001, que conserva la aprobación y los estados.
Una modificación aprobada de la línea base requiere una nueva versión del
documento general y actualizar este índice y el control de cambios; organizar
requisitos por sprint en otros documentos no reemplaza esa lista general.

## Regla de actualización

Todo cambio documental relevante genera una nueva versión del archivo, una
entrada en el control de cambios y la actualización de este índice. Solo el
contenido de esta carpeta se destina al repositorio documental del docente.
Cada publicación requiere revisión y confirmación del tesista.

## Historial de este índice

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-12 | Se establece el índice de ediciones finales. |
| 1.1 | 2026-10-12 | Se incorpora la edición de requisitos funcionales y el registro actualizado. |
| 1.2 | 2026-10-12 | Se incorpora la edición de requisitos no funcionales y el registro actualizado. |
| 1.3 | 2026-10-12 | Se incorpora la edición de alcance y el registro actualizado. |
| 1.4 | 2026-10-12 | Se incorpora la edición de historias de usuario y el registro actualizado. |
| 2.0 | 2026-10-12 | Se incorporan entrevista, actualización transversal, historias técnicas, pila, factibilidad, arquitectura, diseño, sprints y plan de pruebas. |
| 2.1 | 2026-10-13 | Se indexan las dos ediciones Word y se actualiza el control de cambios. |
| 2.2 | 2026-10-13 | Se señala como vigente el plan Word v1.1 adaptado al Gantt aportado. |
| 2.3 | 2026-10-13 | Se fijan S1 de requisitos y diseño y S2–S6 de desarrollo; se indexan prioridades técnicas, sprint backlog y correcciones temporales de alcance, requisitos y factibilidad. |
| 2.4 | 2026-10-13 | Se indexan historias de usuario, pila, sprint backlog y Word con tablas reorganizadas y prioridad cualitativa separada del orden de trabajo. |
| 2.5 | 2026-10-13 | Se adoptan fichas individuales basadas en la referencia visual para HU, HT y tareas; la pila separa sus columnas. |
| 2.6 | 2026-10-13 | Se corrige la autoría de los Word y se señalan como vigentes el compendio v1.2 y el plan v1.5. |
| 2.7 | 2026-10-13 | Se incorpora el plan Word v1.6 con tres tablas de resumen antes de las fichas de tareas. |
| 2.8 | 2026-10-13 | Se incorpora la lista general de requisitos en tablas y se explicita su relación con el catálogo fuente y las ediciones de detalle. |
| 2.9 | 2026-10-13 | Se señala como vigente la edición general v2.0 aprobada, CAT-REQ-001 v1.2 y priorización v1.3; publicación al docente pendiente. |
| 3.0 | 2026-10-13 | Se registró ZA-ALC-001 como borrador; sus versiones se conservan ahora en el índice común de alcances modulares mientras no sean aprobadas para entrega. |
| 3.1 | 2026-10-13 | Se incorporó la edición Word de ZA-ALC-001 con imagen de marca y se conservó la fuente Markdown; historial documental preservado. |
| 3.2 | 2026-10-13 | Se integró v1.1 de ZA-ALC-001 con formato borgoña consistente, títulos semánticos y paginación corregida; historial documental preservado. |
| 3.3 | 2026-10-13 | Se retira ZA-ALC-001 del índice de entregables finales mientras siga pendiente de aprobación; los alcances modulares de trabajo se centralizan en un único índice y carpeta interna. Se distingue el alcance general del proyecto. |
| 3.4 | 2026-10-13 | Se completa el traslado de ZA-ALC-001 v1.0 Word y se corrigen enlaces de ediciones anteriores del control de cambios; ya no queda ningún archivo modular en la carpeta académica mientras las propuestas estén pendientes de aprobación. |
| 3.5 | 2026-10-13 | Se señala como vigente el registro de entrevista v1.1, cotejado con CAT-REQ-001 v1.2; acta, validación organizacional directa y revisión académica siguen pendientes. |
| 3.6 | 2026-10-13 | Se indexa el alcance general v1.3, el reporte del tesista sobre revisión en clase y la actualización del dashboard; permanecen pendientes la revisión académica formal y la validación organizacional directa. |
| 3.7 | 2026-10-14 | Se agrega la edición Word del alcance general v1.3 con formato de marca ZHUD ALELÍ; conserva el estado preparado para revisión del tesista. |
| 3.9 | 2026-10-14 | Se ajustan las 51 historias funcionales del compendio Word a tablas individuales Campo/Dato según la fuente vigente; contenido, agrupación por sprint y trazabilidad preservados. Revisión visual y académica pendientes. |
| 4.0 | 2026-10-14 | Se asignan HT-PRE-001 a HT-PRE-005 a S1, se eliminan del grupo de propuestas y se actualizan las fichas, pila, plan y backlog sin declarar el sprint completo. |
| 4.1 | 2026-10-14 | Se registra la publicación autorizada de requisitos generales v2.0 y priorización v1.3; los pendientes académicos y organizacionales se mantienen explícitos. |
| 4.2 | 2026-10-19 | Se documentan cierre histórico de S0, correspondencia de etapas y brechas de cobertura; edición pendiente de revisión y transferencia. |
| 4.3 | 2026-10-19 | Se indexa arquitectura detallada v1.1 aprobada para documentación; v1.0 se conserva y la transferencia permanece pendiente. |
| 4.4 | 2026-10-20 | Se incorpora el cierre administrativo parcial de S1, se registra el reporte de vistos buenos verbales y se explican las discrepancias entre Gantt y backlog; transferencia pendiente. |
| 4.5 | 2026-10-20 | Se incorpora el informe de cierre S1 v1.1: se concilian los cinco estados locales con el backlog v1.7, se retira la fecha de verificación no sustentada de SB-S1-05 y se mantienen como pendientes las validaciones y aprobaciones sin evidencia específica. Transferencia pendiente. |
| 4.6 | 2026-10-21 | Se ordenan por sprint las historias técnicas y la pila desde S1, se integran las HT-PRE aceptadas en el listado principal y se explicita el orden S1–S6 del backlog. Word sin cambios; cierre parcial y transferencia pendiente. |
| 4.7 | 2026-10-27 | Se indexa el plan de definición e implementación de acceso y superadministración v1.2 aprobado por el tesista; se registra la nueva secuencia S1/S2 y se mantienen explícitos los límites de aprobación, evidencia, revisión y transferencia. |
| 4.8 | 2026-10-27 | Se indexan el plan de sprints v1.5 y los criterios de superadministración v1.3; el backlog v1.4 se identifica como corte anterior, sin alterar estados. |
| 4.9 | 2026-10-27 | Se indexan el plan v1.6 y los criterios v1.4 con autoridad transversal de la Superadministradora sobre todos los módulos y edición de registros y opciones desde el panel. |
| 5.0 | 2026-10-27 | Se incorporan ediciones académicas completas de requisitos v2.1, historias v2.6 y pila v1.8; línea base aprobada y ampliaciones propuestas permanecen diferenciadas. |
| 5.1 | 2026-10-28 | Se incorpora arquitectura v1.2 con backend por módulo, frontend por pantalla, recursos compartidos y verificación de transición. Se conserva v1.1 y se distinguen convención aprobada, implementación local parcial y revisión académica pendiente. |

| 5.2 | 2026-10-28 | Indexa requisitos v2.2, HU v2.7, HT v1.8, pila v1.9 y backlog v1.5 del acceso aceptado; revisión académica, implementación y transferencia pendientes. |
| 5.11 | 2026-10-30 | Indexa el diseño lógico y ER v2.1 y la nota de reutilización de las 13 tablas Django; implementación, revisión académica y publicación al docente pendientes. |
