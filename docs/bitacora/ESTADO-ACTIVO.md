---
title: Estado activo de continuidad
type: state
status: partially-complete
updated: 2026-10-13
task_id: DOC-ORG-001
active_task: DOC-ORG-001
phase: documentation-prepared-for-separate-git-review
branch: opencode/spec-001-fase-1-diseno
head: c2654519b041d8f96a2028482608c93ac9d8ea0b
last_commit: c265451
commit: pending
current_agent: codex
current_role: coordinator
decision_status: plan-authorized-by-tesista
constitution_current: 0.2.0
constitution_previous: 0.1.0
allowed_paths:
  - AGENTS.md
  - README.md
  - agents/tesis/OBSIDIAN_POLICY.md
  - docs/00-inicio/moc-documentacion.md
  - docs/context/context-index.md
  - docs/bitacora/ESTADO-ACTIVO.md
  - docs/bitacora/checkpoints/2026-10-12-inicio-organizacion-documental.md
  - docs/bitacora/checkpoints/2026-10-13-preparacion-publicacion-documental.md
  - documentacion/**
  - analisis/**
  - _archivo/**
  - .gitignore
blocked_paths:
  - .env
  - .venv/**
  - apps/**
  - config/**
  - design/**
  - specs/**
  - .agents/**
  - .codex/**
  - docs/decisions/ADR-000[1-5]*.md
next_action: Revisar el manifiesto exacto de los dos repositorios y obtener autorización específica de commit y push. La edición documental está preparada localmente; confirmar unidad de USD 15, costos de operación, P-03 y alcance ampliado. No atribuir publicación hasta verificarla.
blockers: []
---

# Estado activo de continuidad

## Edición documental preparada y separación de repositorios — 2026-10-13

Por solicitud del tesista se prepararon ediciones documentales de entrevista,
alcance, requisitos, prioridad, historias, pila, factibilidad, arquitectura,
diseño, sprints y plan de pruebas. El índice y control de cambios están en v2.0.
Las nuevas capacidades de la entrevista figuran como pendientes; los 51 RF,
9 RNF, 51 HU, 9 HT y 60 entradas de pila siguen trazables. La estimación de
ahorro no se presenta como ahorro realizado. `documentacion/` se excluye del
repositorio general con `.gitignore` y se copió a un clon local separado del
repositorio del docente para revisión. El repositorio remoto documental estaba
vacío al consultarlo. No se ha hecho commit ni push. El
[[checkpoints/2026-10-13-preparacion-publicacion-documental|manifiesto de preparación]]
registra los archivos y las comprobaciones.


## Tarea actual: organización documental DOC-ORG-001

El tesista aprobó separar las ediciones finales para el docente en `documentacion/`,
conservar los análisis internos en `analisis/` y reservar `_archivo/` para material
sustituido con motivo registrado. Eligió sincronizar mediante un clon separado y
confirmó el cronograma de cinco sprints del 13 de octubre al 23 de diciembre de 2026.
El 2026-10-12 autorizó iniciar el plan por pasos. El paso 1 prepara estructura y reglas;
no autoriza commit ni publicación. `.kimi-code/` permanece intacta.

El paso 1 quedó preparado y verificado: índices de `documentacion/`, `analisis/` y
`_archivo/`, registro de cambios y reglas de separación. No se movieron archivos.
El [[checkpoints/2026-10-12-inicio-organizacion-documental|checkpoint del paso 1]]
detalla rutas y comprobaciones. La tarea completa sigue `partially-complete`.

El paso 2 empieza por una edición candidata de requisitos funcionales dentro de
`analisis/`, a partir de CAT-REQ-001 v1.1 y las partes de R3 que incorpora. El
catálogo está confirmado por el tesista; la revisión de la directora y la
validación de la organización para los ajustes v1.1 no constan como realizadas.
La [[../../analisis/2026-10-12/requisitos/requisitos_funcionales_candidato_v1.0_2026-10-12|edición candidata]]
incluye 51 IDs funcionales, cotejados contra el catálogo sin faltantes, añadidos
ni duplicados. Permanece interna hasta revisión de contenido y estado académico.
El tesista aprobó su contenido y confirmó que la revisión de la directora aún no
se realizó. La promoción editorial no altera los requisitos aprobados ni atribuye
validación académica; la publicación sigue pendiente de confirmación separada.
La edición final del tesista está en
[[../../documentacion/requisitos/funcionales/requisitos_funcionales_v1.0_2026-10-12|requisitos funcionales v1.0]].
El índice público y el control de cambios se actualizaron a v1.1; no hubo publicación.
Se comprobó que sus 51 IDs coinciden con CAT-REQ-001 v1.1 y que todos los enlaces
locales de `documentacion/` resuelven. La
[[../../analisis/2026-10-12/requisitos/requisitos_no_funcionales_candidato_v1.0_2026-10-12|edición candidata RNF]]
incluye los 9 IDs confirmados sin faltantes ni añadidos. El tesista aprobó el
contenido y se preparó la [[../../documentacion/requisitos/no_funcionales/requisitos_no_funcionales_v1.0_2026-10-12|edición final RNF v1.0]];
`RNF-OPS-001` permanece propuesto, fuera de la tabla confirmada. El índice y el
control de cambios públicos están en v1.2, sin publicación ni commit. El siguiente
documento interno es el [[../../analisis/2026-10-12/alcance/alcance_candidato_v1.0_2026-10-12|candidato de alcance]],
aprobado editorialmente por el tesista. Su edición final está en
[[../../documentacion/alcance/alcance_v1.0_2026-10-12|alcance v1.0]]. El índice y
el control de cambios públicos están en v1.3, sin publicación ni commit. El
siguiente [[../../analisis/2026-10-12/historias/historias_usuario_candidato_v1.0_2026-10-12|candidato de historias de usuario]]
agrupa los 51 requisitos funcionales confirmados en 19 historias editoriales,
sin faltantes, añadidos ni duplicados. El tesista aprobó su redacción y la
[[../../documentacion/historias/usuario/historias_usuario_v1.0_2026-10-12|edición final de historias de usuario v1.0]]
quedó en `documentacion/`. El índice y control de cambios están en v1.4, sin
publicación ni commit. El
[[../../analisis/2026-10-12/historias/historias_tecnicas_candidato_v1.0_2026-10-12|candidato de 9 historias técnicas]]
deriva de los RNF confirmados, la constitución 0.2.0 y ADR-0006 y espera
revisión editorial del tesista.

El tesista aportó el material de la asignatura sobre historias de usuario,
historias técnicas y pila del producto y pidió rehacer los tres artefactos según
ese formato. Las 19 historias de usuario v1.0 publicables se conservan como
edición anterior; no se sobrescriben. Los nuevos candidatos internos están en
[[../../analisis/2026-10-12/historias/historias_usuario_candidato_v2.0_2026-10-12|historias de usuario v2.0]],
[[../../analisis/2026-10-12/historias/historias_tecnicas_candidato_v1.1_2026-10-12|historias técnicas v1.1]]
y [[../../analisis/2026-10-12/backlog/pila_producto_candidato_v1.0_2026-10-12|pila de producto v1.0]].
La redacción individual cubre los 51 RF confirmados; la pila reúne 51 HU y 9 HT.
El orden es propuesta, las estimaciones quedan pendientes y ningún candidato
se incorporó a `documentacion/` ni se publicó sin revisión editorial.

El tesista pidió presentar mejor el contenido mediante tablas. Las ediciones
actuales para revisión son [[../../analisis/2026-10-12/historias/historias_usuario_candidato_v2.1_2026-10-12|historias de usuario v2.1]],
[[../../analisis/2026-10-12/historias/historias_tecnicas_candidato_v1.2_2026-10-12|historias técnicas v1.2]]
y [[../../analisis/2026-10-12/backlog/pila_producto_candidato_v1.1_2026-10-12|pila de producto v1.1]].
Las versiones previas se conservan. Se cotejaron las 51 historias con su fuente
de datos y las 9 técnicas y 60 entradas de pila con sus candidatos anteriores;
los criterios, dependencias, prioridades y contenidos se conservaron. Estas
ediciones siguen siendo internas hasta la revisión editorial del tesista.

El tesista pidió clasificar los requisitos y pendientes por importancia y preparar
el estudio de factibilidad faltante. Los candidatos internos son
[[../../analisis/2026-10-12/requisitos/priorizacion_requisitos_candidato_v1.0_2026-10-12|clasificación v1.0]]
y [[../../analisis/2026-10-12/factibilidad/factibilidad_candidato_v1.0_2026-10-12|factibilidad v1.0]].
La clasificación cubre exactamente los 51 RF y 9 RNF confirmados, además de
identificar por separado los dos requisitos propuestos y P-02 a P-14. La
factibilidad utiliza el presupuesto aportado de USD 2.869 y confronta el Gantt
anterior de 16 semanas con los 72 días calendario del plazo confirmado
13/10–23/12/2026. Su conclusión es condicionada, con riesgo temporal alto,
sin cambiar alcance ni fechas y sin atribuir validación académica u organizacional.
Los dos candidatos siguen en `analisis/` hasta revisión editorial.

El tesista aportó un resumen de entrevista con 12 temas de gestión documental,
asistencia, inventario, producción, feria y venta mensual. Se registró como
[[../evidence/requirements/2026-10-12-resumen-entrevista-temas-organizacionales|evidencia EVID-ENT-2026-10-12-001]]
con entrevista fechada el 12/10/2026. El tesista identificó a María Camas como
tesorera entrevistada y comunicó que la organización aprobó los montos y reglas
de asistencia. Tras corregir dos formulaciones anteriores, precisó USD 0,01 por
minuto de atraso, USD 10 desde la primera falta y aviso a la tercera falta.
Quedan por definir justificativos, autoridad, redondeo y cobro; P-03 permanece
abierto en el catálogo. El abogado costó USD 500 por mes
durante dos meses según el tesista, es decir USD 1.000 referidos para el periodo.
No se recibió acta ni comprobante. La
[[../../analisis/2026-10-12/entrevista/impacto-documental-candidato_v1.0_2026-10-12|matriz de impacto]]
y [[../requirements/proposals/2026-10-12-temas-entrevista-para-validacion|propuesta PRO-ENT-001]]
mantienen separadas las necesidades nuevas de los 60 requisitos confirmados.
Las ediciones candidatas de alcance, RF, RNF, priorización, factibilidad, HU,
HT y pila incorporan la entrevista en versiones nuevas dentro de `analisis/`.
Las multas comunicadas siguen pendientes de P-03; no se activan sanciones,
mensajería externa ni reglas de comisión. La constitución 0.2.0 permanece
vigente porque el resumen no introduce un principio de gobierno nuevo.

La [[../../analisis/2026-10-12/factibilidad/factibilidad_candidato_v1.2_2026-10-12|factibilidad económica candidata v1.2]]
separa inversión de USD 2.869, costos de operación desconocidos, cifras de la
entrevista y beneficios aún no medidos. Presenta fórmula y escenarios ilustrativos,
sin contar los USD 20.000 eventuales ni los USD 1.000 históricos del abogado como
ahorro automático. En esa edición aún faltaba la frecuencia mensual de tiempo
perdido e inconsistencias para un estimado propio de la asociación.

El tesista precisó luego aproximadamente un día perdido (USD 80) y cuatro
inconsistencias (USD 15 por cada una como supuesto de cálculo) por mes, además
de indicar que se volvería a pagar al abogado si los documentos siguen
desordenados. La [[../../analisis/2026-10-12/factibilidad/factibilidad_candidato_v1.3_2026-10-12|factibilidad candidata v1.3]]
calcula una pérdida recurrente de referencia de USD 140/mes y muestra
reducciones ilustrativas del 50 % y 100 %. Separa los USD 1.000 de un posible
periodo futuro de abogado; aún no hay ahorro real observado.

La tarea ARCH-ADOPT-001 queda registrada abajo como estado anterior. Su rama y `HEAD`
coinciden con los verificados al iniciar DOC-ORG-001. Sus cambios locales siguen sin commit.

## Estado anterior: aceptación de arquitectura y sincronización

El tesista confirmó el 2026-10-08 que se mantiene el monolito modular y pidió documentar
alta cohesión, bajo acoplamiento, comportamiento de la aplicación, mantenimiento,
incorporación de capacidades y entregas incrementales. La condición humana previa para
enmendar la constitución está satisfecha. Se registra la decisión sin aprobar requisitos
nuevos, proveedores de despliegue, políticas PWA pendientes o implementación de SPEC-001.

ARCH-ADOPT-001 aplica una enmienda MINOR 0.1.0 → 0.2.0 y sincroniza las fuentes pertinentes.
La confirmación no autoriza commit, push ni publicación de la aplicación.

La decisión se registra en [[../decisions/ADR-0006-monolito-modular-y-entrega-incremental|ADR-0006]]
y la guía [[../architecture/ARQUITECTURA-OBJETIVO|ARQUITECTURA-OBJETIVO]]. Constitución 0.2.0
aplicada; templates y contexto sincronizados. SPEC-001 conserva alcance, plan y tareas.
El reviewer cerró sin hallazgos accionables; la
[[../evidence/architecture/2026-10-08-aceptacion-monolito-modular|evidencia de aceptación]] y el
[[checkpoints/2026-10-08-aceptacion-monolito-modular|checkpoint]] conservan revisión y comprobaciones.
Los estados anteriores que siguen se preservan como historia previa a esta confirmación.

## Aclaración anterior preservada, previa a la confirmación

El 2026-10-08 el tesista aclaró su objetivo mediante capacidades hipotéticas: incorporar
facturación electrónica, después gestión de clientes o funciones relacionadas con ARCSA,
manteniendo facilidad de cambios. Quiere registrar avances por módulo en el repositorio y
publicar versiones utilizables para probarlas con las socias.

ARCH-REVIEW-004 concreta cómo un monolito modular admite ese flujo, qué límites deben
respetarse y cómo distinguir versionado de código, publicación de la aplicación y despliegue
independiente de servicios. Los ejemplos no aprueban nuevos módulos ni cambian SPEC-001.
La aclaración no constituye aceptación arquitectónica ni autorización para publicar ahora.

La [[../decisions/proposals/2026-10-08-evolucion-modular-y-versiones-piloto|propuesta PRO-ARCH-004]]
describe propiedad de datos, gestión de clientes posterior, historial de documentos y capas
internas. Distingue repositorio, versión piloto conjunta y servicios independientes. El
arquitecto entregó su análisis y el reviewer cerró sin hallazgos accionables pendientes.
La [[../evidence/architecture/2026-10-08-evolucion-modular-y-versiones-piloto|evidencia]] y el
[[checkpoints/2026-10-08-evolucion-modular-y-versiones-piloto|checkpoint]] registran esta revisión.
Se recomienda evolución modular por incrementos; no se aprobó una arquitectura nueva ni
se aplicó una enmienda. No hay implementación o publicación en esta tarea.

## Comparación previa preservada

El tesista pidió ampliar el análisis a microservicios y otras alternativas. Quiere terminar
un incremento de un módulo, probarlo con las socias, añadir el siguiente y facilitar cambios
y módulos futuros. Todavía no decide si necesita publicar cada capacidad por separado o si
le basta una aplicación publicada conjuntamente. Esa respuesta no aprueba PRO-ARCH-002.

ARCH-REVIEW-003 contrasta entrega incremental, límites de dominio, cambios compatibles,
despliegue, operación, integridad y validación con socias. La constitución 0.1.0 conserva su
vigencia; no hay elección arquitectónica ni enmienda aplicada.

La [[../decisions/proposals/2026-10-07-alternativas-arquitectura-entrega-incremental|adenda PRO-ARCH-003]]
compara monolito modular con capas, puertos/adaptadores selectivos, servicios de capacidades
amplias y microservicios. Distingue organización interna de distribución y entrega incremental
de publicación independiente. La recomendación del análisis es provisional; no asigna
prioridades al tesista ni promete velocidad, rendimiento o extracción automática.

La revisión independiente quedó cerrada tras aclarar que agregar una función puede ampliar
su módulo o servicio propietario; no exige crear uno nuevo. No hay hallazgos documentales
accionables pendientes. La [[../evidence/architecture/2026-10-07-alternativas-entrega-incremental|evidencia]]
y el [[checkpoints/2026-10-07-alternativas-entrega-incremental|checkpoint de alternativas]]
registran el análisis y sus límites. La selección humana continúa abierta; no corresponde
aplicar todavía el candidato constitucional de PRO-ARCH-002.

## Revisión anterior preservada

El tesista pidió analizar capas dentro de cada módulo para facilitar crecimiento funcional,
bajo acoplamiento y alta cohesión. Autorizó agentes especializados y documentación; condicionó
el cambio constitucional a estar de acuerdo con la arquitectura.

La [[../decisions/proposals/2026-10-07-monolito-modular-con-capas|propuesta PRO-ARCH-002]]
recomienda un monolito modular Django con capas internas pragmáticas, ORM nativo, integridad
relacional y casos de uso transaccionales cuando existe comportamiento que los justifica.
Incluye alternativas, fuentes oficiales, riesgos del diseño anterior, límites de evidencia,
texto candidato del principio IV y mapa de sincronización constitucional.

El arquitecto entregó su análisis y el reviewer cerró la revisión documental sin hallazgos
accionables pendientes después de corregir la autorización para resultados idempotentes.
Eso no equivale a aceptar la arquitectura. El registro operativo queda en el
[[checkpoints/2026-10-07-revision-arquitectura-monolito-capas|checkpoint de revisión]] y la
[[../evidence/architecture/2026-10-07-revision-monolito-capas|evidencia documental]].

La constitución 0.1.0 permanece intacta. La versión 0.2.0 es candidata para PRO-ARCH-002; su aplicación,
fecha de enmienda y propagación dependen del acuerdo explícito del tesista. La revisión
académica sigue pendiente donde corresponda. No hay pruebas de carga, código Django nuevo,
commit ni push en esta tarea.

## Continuidad previa preservada

REQ-APPROVAL-001 quedó completada. [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.1]] sigue
vigente con 60 confirmed, 2 proposed y 12 históricos; v1.0 conserva su evidencia original.
P-01 se cerró para acceso básico. La revisión académica, las specs futuras, P-13/P-14 y el
despliegue conservan sus pendientes; las 37 tareas de SPEC-001 no se ejecutaron en esta revisión.

- [[../evidence/casos-de-uso/2026-09-28-aprobacion-requisitos-v1-1|Aprobación de requisitos]].
- [[checkpoints/2026-09-28-aprobacion-requisitos-v1-1|Checkpoint anterior]].
- [[checkpoints/2026-09-28-cierre-p-01|Registro de P-01]].
- [[checkpoints/2026-09-28-coherencia-integral|Revisión previa DOC-COHERENCE-001]].
- [[checkpoints/2026-09-28-estado-previo-coherencia|Continuidad previa de HARNESS-ARCH-001]].

El estado anterior tenía HEAD `a6e842f63917b2ac28a64c80b00d68069ba2fabd` y `last_commit: 6355bc5`.
Se actualiza al HEAD local comprobado `c2654519b041d8f96a2028482608c93ac9d8ea0b`; esto no crea
un commit ni demuestra una publicación remota. Los cambios locales previos de UI, Obsidian
y artefactos de SPEC-001 se preservan.
