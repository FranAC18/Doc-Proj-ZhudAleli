---
title: Historial trasladado del estado activo
type: checkpoint
status: historical
date: 2026-10-27
source: docs/bitacora/ESTADO-ACTIVO.md
---

# Historial anterior del estado activo

Este archivo conserva sin recortes las secciones retiradas del estado operativo el 2026-10-27.

## Asignación aceptada de historias técnicas a S1 — 2026-10-21

El tesista aceptó la asignación a S1 de HT-PRE-001 a HT-PRE-005 conforme a la tabla
adjunta. La aceptación se registró después del cierre administrativo del 2026-10-20. Al
2026-10-21, S1 se mantenía cerrado y parcialmente completo; esa era la situación documentada
entonces. La decisión posterior del tesista del 2026-10-27 modifica el periodo y alcance de
definición de acceso/superadministración, según la sección anterior. Ninguna tarea se marca
terminada ni se sustituyen validaciones, evidencias, estimaciones o responsables pendientes.
El detalle y las ediciones documentales están en el
[[checkpoints/2026-10-21-aceptacion-ht-pre-s1|checkpoint de aceptación]].

## SB-S2-02 activo por decisión del tesista — 2026-10-20

El tesista confirmó que Sprint 2 incluye el login y autorizó continuar con `SB-S2-02`.
La tarea cubre el recorrido básico completo de `RF-ACC-001`: acceso y salida, protección
privada, cambio de contraseña, dashboard mínimo y vencimiento de sesión. La preparación
de `SB-S2-01` ya tiene Django, `accounts.User`, migraciones PostgreSQL, comando controlado
de primera cuenta y pruebas locales aprobadas; queda pendiente la comprobación de PWA en
navegador, que se hará cuando existan rutas privadas. `SB-S2-03` (administración de
membresías/responsabilidades) y `SB-S2-04` (actividades/pendientes/encargos propios) quedan
fuera del trabajo inmediato; ambas siguen en la pila para retomarse cuando su alcance esté
listo. La [hoja de ruta de Sprint 2](../sprints/SPRINT-02-HOJA-DE-RUTA.md) registra el
detalle acordado. No se hizo commit ni push.

## Ajuste de criterios de HU-ACC-001 — 2026-10-21

Por instrucción explícita del tesista, SPEC-001 incorpora los criterios CA-ACC-001-12/13:
tres fallos del mismo identificador normalizado dentro de tres minutos bloquean ese acceso
durante tres minutos; los mensajes son «Usuario incorrecto» para identificador inexistente o
cuenta inactiva y «Contraseña incorrecta» para una cuenta activa con clave errónea. El tesista
acepta expresamente que la diferencia permite inferir si el usuario corresponde a una cuenta
activa. El bloqueo es temporal y no desactiva la cuenta. Se actualizan spec, plan, tareas,
contrato HTTP, quickstart, modelo de datos, índice de funcionalidad y `app/docs/current_context.md`.
La implementación de `SB-S2-02` añade estado temporal con HMAC y la migración
`0002_loginthrottle`, aplicada correctamente en `zhud_aleli_dev`. Pasan `manage.py check`,
`makemigrations --check`, Ruff y formato. Las pruebas funcionales/seguridad y la revisión de
navegador quedan pendientes; no se ejecutaron pruebas en esta tarea. No se hace commit ni push.

La implementación local de `SB-S2-02` ya incorpora formularios, vistas y rutas de login,
logout, bienvenida privada y cambio de contraseña obligatorio/voluntario. También implementa
los mensajes diferenciados de CA-ACC-001-02/03, protección no-caché y bloqueo transaccional
de la fila durante el cambio.
Se alinearon las rutas y el texto de rechazo con el contrato HTTP aprobado de SPEC-001, y el
formulario conserva el nombre de usuario normalizado tras un error. Pasaron Ruff,
comprobación de formato y `manage.py check`; las pruebas funcionales y la revisión de
interfaz/navegador siguen pendientes. No se creó una cuenta real.

El tesista informa que el login ya funciona. Se aplicó una primera pasada visual a acceso,
bienvenida y cambio de contraseña basada en la guía de estilo: tokens locales, superficies,
botones, campos táctiles, alertas accesibles y foco en el resumen de errores. A solicitud
del tesista, el login ahora toma como referencia una composición dividida con ilustración
botánica original, formulario minimalista y adaptación móvil; la ilustración se agregó al
caché público de la PWA. No se añadieron accesos sociales ni recuperación de contraseña,
porque no están implementados. Pasaron `manage.py check`, la compilación de la plantilla
login y la validación XML del SVG. La vista del sitio en navegador queda pendiente porque
el control de acceso rechazó abrir `localhost`; no se reintentó por otra superficie.

El tesista entregó el emblema floral y el logotipo horizontal oficiales. Se copiaron los
originales sin alteración a `app/static/brand/`; el emblema reemplaza los iconos PWA y se
generaron tamaños 192, 512, Apple Touch y favicon con fondo claro y margen seguro. El
logotipo se usa en el acceso y encabezado; el service worker pasó a caché v4 para refrescar
los recursos públicos. Se verificaron hashes idénticos de los originales, dimensiones,
manifest JSON, `manage.py check` y compilación de plantillas. No se hizo commit ni push.

## Versiones blancas del logotipo para fondos oscuros — 2026-10-21

Se generaron `zhud-aleli-emblem-white.png` y `zhud-aleli-wordmark-white.png` recoloreando
únicamente los píxeles RGB de los originales; las dimensiones y el canal alfa se conservaron
exactamente. El acceso usa ahora el logotipo horizontal blanco sin tarjeta, sobre el panel
botánico oscuro; el encabezado mantiene la versión vino sobre superficie clara. El service
worker pasa a caché v5 e incorpora ambas variantes públicas. La comprobación de alfa y color
resultó correcta. Pasaron `manage.py check`, la compilación de las plantillas login/base, la
comprobación de los 16 recursos del precache y `git diff --check` del estado documental. No se
hizo commit ni push.

## SB-S2-01 preparado localmente — 2026-10-20

El tesista autorizó avanzar con `SB-S2-01` mientras `SB-S1-01` conserva estado en curso. En la raíz Git independiente de `app/` se creó la rama `feature/RF-ACC-001-base-proyecto` sin commit inicial. Se prepararon proyecto Django, `accounts.User`, migración inicial, Bootstrap 5 local y base PWA pública. PostgreSQL 18 ya está conectado; las migraciones se aplicaron y cinco pruebas de cuentas aprobaron en una base temporal. También pasaron Django check, makemigrations check, Ruff, tres pruebas PWA sin base de datos y cinco rutas públicas HTTP 200. La instalación PWA y el corte de red siguen sin verificar porque el navegador de la herramienta rechazó el origen local. El [[checkpoints/2026-10-20-sb-s2-01-pre-commit|checkpoint de SB-S2-01]] conserva los resultados y límites; el incremento aún no está integrado en Git.

## Sprint 2 iniciado por decisión del tesista — 2026-10-20

El tesista cerró el periodo de S1 y decidió comenzar S2 por `SB-S1-01`, pendiente trasladada.
La [hoja de ruta de S2](../sprints/SPRINT-02-HOJA-DE-RUTA.md) corrige el prompt de `SB-S2-01` antes de implementar código. El [cotejo de fuentes](checkpoints/2026-10-20-sb-s1-01-cotejo-fuentes.md) registra los doce temas disponibles con actor, fecha, dudas y cobertura en el catálogo, sin atribuir acta o validación directa no recibida. `SB-S1-01` sigue en curso; `SB-S2-01` es la siguiente porción de producto. Los cambios locales de la separación de repositorios continúan sin commit.

## Separación de repositorios preparada — 2026-10-20

El tesista confirmó el plan de separación. La constitución 2.0.0 y ADR-0008 están
editados localmente; el checkpoint
[[checkpoints/2026-10-20-separacion-repositorios-pre-commit|pre_commit]] registra
las rutas, verificaciones y pendientes. `app/` es una raíz Git local independiente,
ignorada por el repo general, con solo `.gitignore` y sin commits. El remoto de la app
figura vacío. No se hizo commit, push, tag ni extracción de historial.

## Autoridad de cierre de sprints aclarada - 2026-10-20

Por solicitud explícita del tesista, la constitución 1.0.0 y el
[[../decisions/ADR-0007-autoridad-del-tesista-para-cierre-de-sprints|ADR-0007]] reconocen su
autoridad exclusiva para cerrar/reabrir un periodo y avanzar sin acta ni aprobación adicional.
El resultado y los pendientes se anotan en el registro operativo existente para continuidad;
no es una precondición y no marca como completado el trabajo pendiente.

## Timebox de Sprint 1 cerrado con resultado parcial - 2026-10-20

Por solicitud del tesista se cerró administrativamente el timebox de S1. El resultado
permanece `partially-complete`: el cierre del periodo no convierte las tareas pendientes
en completadas ni aprueba requisitos, criterios o decisiones sin su evidencia. El
[[checkpoints/2026-10-20-cierre-sprint-1-parcial|checkpoint de cierre parcial de S1]]
registra el inventario de trabajo y la continuidad.

La numeración queda explicitada: el S1 del calendario es requisitos y diseño; el `S1`
histórico de SPEC-001 es acceso y corresponde al S2 del calendario. El estado de
SPEC-001 y su puerta T012 se mantienen sin cambio.

El 2026-10-20 el tesista identificó a Maria Camas, encargada de la organización, como
quien autorizó verbalmente, y a Julio Santillan, profesor de Aplicaciones Informáticas 2,
como quien dio el visto bueno durante una presentación. El tesista aclara que no existen
actas ni constancias. La fecha de cada autorización, la versión expuesta y el alcance
exacto no están identificados; no se presume que cubrieran todas las tareas, requisitos
o decisiones de S1. El reporte no cambia por sí solo el resultado parcial del timebox.

El [[checkpoints/2026-10-20-reconciliacion-gantt-sprint-1|cotejo del Gantt local]] corrigió
las cinco marcas `verificada` que no coincidían con el backlog v1.7: ahora tres tareas
figuran `en_curso`, dos `bloqueada` y ninguna `verificada`. El estado detallado del backlog
se conserva sin cambios. La fecha original de SB-S1-05 se retiró del campo de verificación
activo y queda pendiente de aclaración; sus estados parciales, las validaciones y las
brechas de trazabilidad siguen abiertos.

## Arquitectura detallada v1.1 documentada - 2026-10-19

El tesista aprobó la edición documental v1.1 de arquitectura, derivada de la base de ADR-0006.
Se creó en `documentacion/arquitectura/`; el índice y el control de cambios avanzan a v4.3.
La edición no modifica requisitos ni decisiones abiertas, y no declara implementación, revisión académica,
validación organizacional o transferencia. Se mantienen siete RF sin referencia en historias/pila,
seis criterios ampliados por cotejar y la ratificación pendiente de propietarios para RF-DOC-001/RF-AST-001.
La arquitectura v1.0 se conserva como historial. No se hizo commit ni push.

## Edición académica de seguimiento preparada - 2026-10-19

Por solicitud del tesista se prepararon en `documentacion/seguimiento/` el informe
de cierre de Sprint 0 y continuidad v1.0 y el registro de pendientes de trazabilidad v1.0.
El índice y el control de cambios pasan a v4.2; las ediciones anteriores se conservan.
Los documentos registran el cierre histórico aprobado y los pendientes posteriores sin
declarar completados S1, SPEC-001 ni las validaciones académicas u organizacionales.

Se comprobaron los cuatro archivos de la entrega: cero enlaces rotos, cero enlaces locales
fuera de `documentacion/` y cero espacios finales. La carpeta separada `F:\Tesis\Doc Tesis`
no fue accesible (`Permission denied`); no se copiaron archivos allí ni se hizo commit/push.
El conjunto exacto y los resultados constan en
[[checkpoints/2026-10-19-edicion-docente-seguimiento]]. La transferencia sigue pendiente.

## Sprint 0 verificado como cerrado - 2026-10-18

La revisión de las fuentes canónicas confirma que Sprint 0 (preparación) ya está
`completed`, cerrado por el tesista el 2026-07-21 y versionado en `9276813b44e399ef56c2ddb4c3bc74d4f65bb28f`.
El commit es ancestro de HEAD y de la referencia local de seguimiento de la rama remota.
La consulta remota nueva falló por resolución de red; no se afirma verificación online.

Se corrige la equiparación errónea hecha por el asistente entre Sprint 0 y S1 de requisitos
y diseño. Los pendientes de S1 y DOC-ORG-001 no reabren S0 ni impiden continuar el trabajo
permitido por las puertas de cada tarea. La numeración técnica histórica S1 de SPEC-001
corresponde a acceso, S2 en el calendario público; son referencias distintas.

El [[checkpoints/2026-10-18-verificacion-cierre-sprint-0|checkpoint de verificación]]
registra la revisión independiente, la evidencia Git y los pendientes posteriores.
El commit/push nuevo sigue bloqueado por escritura denegada en `.git`; no por falta
de autorización del tesista. No se intentan rutas alternativas para eludir ese límite.

## Cierre de sesión y pendientes - 2026-10-18

Se documentó la pausa por solicitud del tesista. El detalle y los criterios para retomar
están en [[checkpoints/2026-10-18-cierre-sesion-pendientes]]. DOC-ORG-001 sigue parcialmente
completa; este cierre corresponde únicamente a la sesión.

La referencia documental actual es `documentacion/README.md` v4.1: requisitos generales
v2.0 y CAT-REQ-001 v1.2, con 58 RF y 9 RNF confirmados. Las menciones a 51 RF y CAT v1.1
en las secciones históricas inferiores describen la línea base anterior. Se debe cotejar
la cobertura de las novedades en historias y pila antes de declarar coherencia integral.

Quedan pendientes la revisión académica formal, la validación organizacional directa de
las novedades, el acta formal, la revisión del alcance general v1.3, los alcances modulares
propuestos y las decisiones abiertas, incluida P-03. Sprint 1 y SPEC-001 no se declaran
terminados; se conserva la puerta de validación humana del diseño registrada en sus tareas.

Rama y HEAD comprobados: `docs/requisitos-y-organizacion-del-vault`, `5ccbe09dda2ebf435e979888e64c6b9dbdc4b1db`.
Hay cambios locales anteriores. No se realizó commit, push ni verificación remota nueva.
Retomar por los índices canónicos y el checkpoint, sin cargar todo el historial.

## Publicación de requisitos generales v2.0 y priorización v1.3 — 2026-10-14

El tesista autorizó expresamente transferir estos dos documentos al repositorio documental,
hacer commit y push. El commit `de8cd18d56743e821ab69021aa6904cde02f7624` se publicó en
`main`; `git ls-remote` confirmó el mismo hash en `origin/main` y el clon documental quedó
limpio. El checkpoint [[checkpoints/2026-10-14-publicacion-requisitos-v2.0-pre-commit]]
registra el manifiesto y las verificaciones previas; el
[[checkpoints/2026-10-14-publicacion-requisitos-v2.0-post-commit|checkpoint post_commit]]
registra el resultado remoto. La revisión académica formal y la validación organizacional
directa de las novedades permanecen pendientes. Esta operación no incluye commit ni push del
repositorio general, cuyo árbol de trabajo conserva cambios ajenos.

## Organización documental modular — 2026-10-13

Los alcances modulares ZA-ALC-001 a ZA-ALC-003 y sus versiones históricas se centralizaron en
`analisis/2026-10-13/alcances-modulos/`, incluido el Word histórico ZA-ALC-001 v1.0 que estuvo
bloqueado temporalmente. La carpeta `documentacion/alcance/modulos/` queda sin alcances mientras
las propuestas no estén aprobadas para entrega; sus ediciones no aprobadas se retiraron del
índice de entregables finales. El índice modular registra el orden del Plan de sprints v1.2:
S2 Acceso, S3 Planificación, S4 Asistencia, S5 Trazabilidad productiva y rendición, S6 Reportes
e información. El alcance general del proyecto permanece diferenciado en `documentacion/alcance/`.
El catálogo general usa ZA-DG-001; ZA-CU queda para especificaciones detalladas. Las ediciones
modulares continúan como propuestas y no implican aprobación ni publicación.

## Publicación documental verificada — 2026-10-13

El tesista autorizó los conjuntos exactos del manifiesto y el push documental.
El repositorio general recibió el commit local `09f4318106fd85d10c3095d592c177c33972c1ff`
de 38 archivos; **no** se publicó ese repositorio. El repositorio del docente
recibió en `main` el commit `20f42279a769b3aefc6d52a0efde79e4c707e498`
de 24 archivos Markdown. Se comprobó que el hash remoto coincide. El
[[checkpoints/2026-10-13-publicacion-documental-verificada|checkpoint post_commit]]
registra archivos, pruebas y límites. Las decisiones de alcance y la revisión
académica siguen pendientes.

La nota de preparación que sigue conserva el estado anterior a los commits.

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

## Commit, integración y publicación del lote DOC-ORG-001 - 2026-10-20

El commit `aacabeeab9f41287ea9f431f1fccdbb37d947089` incluyó 182 archivos. Se integraron los
commits remotos `7e3a25406cb007dc770777c45bc1db83acd02843` y
`310cd914e8c2b5d5a844314919f4667ed68432a2`; los 15 conflictos del cronograma quedaron
resueltos en el merge commit `58d9b1f344feda2e5d8db2b01f61ab74cc9d8ea9`. El push a
`origin/docs/requisitos-y-organizacion-del-vault` terminó correctamente. La
[[checkpoints/2026-10-20-commit-push-worktree-post-commit|evidencia post-commit]] registra la
resolución, verificaciones y alcance publicado.
