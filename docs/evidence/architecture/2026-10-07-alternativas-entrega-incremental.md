---
title: Evidencia de alternativas de arquitectura para entrega incremental
type: evidence
id: EVID-ARCH-003
status: partially-complete
date: 2026-10-07
task_id: ARCH-REVIEW-003
phase: pre_commit
commit: pending
commit_hash: null
branch: opencode/spec-001-fase-1-diseno
head: c2654519b041d8f96a2028482608c93ac9d8ea0b
sprint: S1
project_phase: Fase-II-diseno
module: transversal
objective: Registrar alternativas y condiciones para entregar incrementos útiles y facilitar cambios futuros.
decision_status: alternatives-under-evaluation
technical_review: completed-no-open-findings
constitution_current: 0.1.0
constitution_action: deferred-until-architecture-agreement
universal_final_validation: passed-with-inherited-warnings
requirement_ids:
  - RF-ACC-001
  - RF-ACC-002
  - RF-ACC-003
  - RF-ACC-004
  - RF-VEN-001
  - RF-PWA-002
  - RF-PWA-003
  - RNF-SEC-001
  - RNF-AUD-001
  - RNF-DAT-001
  - RNF-PRV-001
changed_files:
  - docs/decisions/proposals/2026-10-07-alternativas-arquitectura-entrega-incremental.md
  - docs/bitacora/ESTADO-ACTIVO.md
  - docs/evidence/architecture/2026-10-07-alternativas-entrega-incremental.md
  - docs/bitacora/checkpoints/2026-10-07-alternativas-entrega-incremental.md
related:
  - "[[../../decisions/proposals/2026-10-07-alternativas-arquitectura-entrega-incremental]]"
  - "[[../../bitacora/checkpoints/2026-10-07-alternativas-entrega-incremental]]"
  - "[[2026-10-07-revision-monolito-capas]]"
  - "[[../../decisions/proposals/2026-10-07-monolito-modular-con-capas]]"
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[../../architecture/MODULOS-DETALLADOS]]"
  - "[[../../sprints/ROADMAP-ANTEPROYECTO]]"
  - "[[../../../specs/001-acceso-usuarias-internas/plan]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
  - sprint/s1
---

# Evidencia de alternativas de arquitectura para entrega incremental

## Resultado y aclaración del tesista

Se registra [[../../decisions/proposals/2026-10-07-alternativas-arquitectura-entrega-incremental|PRO-ARCH-003]],
adenda solicitada por el tesista para ampliar la comparación a microservicios. Quiere
terminar un incremento utilizable, probarlo con las socias, incorporar otro y facilitar
correcciones y capacidades futuras. Todavía no decide si necesita publicar capacidades
por separado o si le basta publicar una aplicación conjunta.

Esta aclaración no acepta PRO-ARCH-002 ni su texto constitucional candidato. Selección,
ADR aceptado y enmienda siguen pendientes. La constitución vigente permanece en 0.1.0;
la candidata 0.2.0 anterior corresponde a PRO-ARCH-002 y no se aplica automáticamente a
una arquitectura distribuida. Tampoco se modifican requisitos, roadmap o SPEC-001 desde
esta documentación.

Según el handoff final del coordinador, el reviewer cerró PRO-ARCH-003 sin hallazgos
accionables pendientes tras un ajuste P3. Ese cierre técnico no acepta la arquitectura.
La fase es `pre_commit`, con `commit: pending`; el HEAD identifica la base local y no
un commit nuevo de esta tarea.

## Comparación ampliada

| Alternativa | Aporte a la entrega y evolución | Condiciones o límites |
|---|---|---|
| Monolito modular con capas internas | Permite recorridos útiles por incrementos y cambios localizados según los límites de módulo. | Publicación conjunta, recursos y esquema compartidos; exige controlar dependencias y regresiones. |
| Puertos/adaptadores selectivos dentro del monolito | Puede aislar una regla o integración que requiere sustitución; conserva la entrega incremental. | Añade interfaces y mapeos; no da publicación independiente ni extracción automática. |
| Servicios alrededor de capacidades amplias | Permite autonomía de algunas capacidades que agrupan varias funciones cohesivas. | Requiere contratos remotos, propiedad de datos, permisos, recuperación y operación; cambios dentro del mismo servicio siguen agrupados. |
| Microservicios autónomos por capacidades de negocio | Puede permitir publicación, recursos y recuperación independientes. | La autonomía depende de contratos, datos y operación; añade fronteras distribuidas, versiones coexistentes y fallos parciales. |

Son evaluaciones de diseño, no resultados de rendimiento. Capas y puertos/adaptadores pueden
existir dentro de una aplicación integrada o de servicios. Servicios amplios y microservicios
son variantes de distribución; no se distinguen por un tamaño o número arbitrario. Pantalla,
tabla y app Django no definen automáticamente un servicio autónomo.

La propuesta considera también una evolución híbrida cuando aparece una necesidad concreta.
Un worker que ejecuta el mismo código y escribe las mismas tablas no es automáticamente un
microservicio. La recomendación provisional favorece el monolito con capas para los objetivos
expresados, con aislamiento selectivo donde se justifique. Las alternativas distribuidas
ganarían peso con una necesidad comprobada de autonomía y capacidad para operarlas. El
tesista todavía no seleccionó una alternativa.

## Dependencias, integridad y experiencia común

- La venta multiproducto debe confirmarse completa o revertirse completa; su auditoría se
  guarda en la misma transacción, conforme a CAT-REQ-001. Separar venta, inventario y saldo
  arbitrariamente exige resolver esta garantía. Una compensación no equivale por sí sola
  a la atomicidad aprobada; relajarla requiere validación de requisito.
- Las operaciones sensibles comprueban permisos vigentes en backend, incluidas llamadas
  internas y sincronización. Autenticación común y gateway no sustituyen autorización
  por recurso. La sesión prevista en SPEC-001 no resuelve automáticamente identidad y
  revocación entre servicios.
- Django admite una aplicación integrada o proyectos separados. El backend distribuido
  puede conservar una interfaz común SSR/Bootstrap; no obliga a microfrontends, SPA ni
  repositorios separados. Un cambio de pantalla puede requerir publicar el frontend común.
- Contratos, migraciones y consumidores con versiones coexistentes necesitan compatibilidad.
  La PWA puede conservar operaciones capturadas con una versión anterior: revalidación,
  dependencias y rechazo recuperable pertenecen a sus specs y P-13/P-14. No se descartan
  pendientes silenciosamente ni se conceden permisos por conservar una operación antigua.
- Publicación independiente, aislamiento de fallos y capacidad de carga son atributos
  distintos de desarrollo incremental. En servicios se verifican además lentitud, caída,
  respuesta perdida, reintento y versiones diferentes; las pruebas de integración siguen
  siendo necesarias en todos los enfoques.

## Incrementos y validación con socias

El [[../../sprints/ROADMAP-ANTEPROYECTO|roadmap vigente]] permite pruebas parciales y
solapamientos según dependencias. Un incremento necesita alcance confirmado, datos,
permisos, pantalla, pruebas, integración y evidencia. La propuesta describe probar tareas
representativas con socias, corregir hallazgos y registrar la versión antes de avanzar.
Ese proceso está propuesto para ejecución futura; esta tarea no realizó un piloto con socias.

SPEC-001 entrega acceso básico, sesión y bienvenida privada; **no completa S1**. RF-ACC-002/003
requieren sus specs y RF-ACC-004 consume datos de capacidades posteriores. Asistencia depende
de identidades, actividades y permisos; reportes dependen de sus fuentes. El sitio público
puede avanzar con contenido aprobado sin exponer datos privados. Se conservan las puertas
de SPEC-001 y su protocolo SC-002; no se inventan muestra ni criterios de validación.

## Participación, hallazgo y revisión

El coordinador preparó la adenda y contrastó documentación oficial y análisis de sus autores.
El reviewer independiente encontró un único **P3**: una capacidad nueva no requiere siempre
crear un servicio nuevo. El coordinador corrigió la sección 6 para permitir ampliar el
servicio propietario o crear otro solo con frontera de negocio y autonomía justificadas.
El reviewer confirmó el ajuste y cerró sin hallazgos accionables pendientes, según el handoff.

El arquitecto también participó en ARCH-REVIEW-003 en modo read-only, según el handoff final.
Entregó el contraste de las cuatro alternativas, incrementos frente a despliegue independiente,
dependencias del roadmap/SPEC-001, datos, permisos y PWA. Su recomendación provisional no
constituye aceptación. Documenter creó esta evidencia y su checkpoint; la revisión previa
de ARCH-REVIEW-002 se conserva como antecedente.

## Verificaciones reales y límites

| Verificación | Resultado y procedencia |
|---|---|
| `git status --short --branch` y `git rev-parse HEAD` | Documenter comprobó rama/HEAD del YAML y cambios locales existentes. |
| `Test-Path` de los dos destinos documentales | Ambos devolvieron `False` al iniciar el handoff; no hubo conflicto de destino. |
| `Test-Path` de `manage.py`, `apps` y `config` | Los tres devolvieron `False`; todavía no hay aplicación Django del proyecto. |
| `git diff --exit-code -- .specify/memory/constitution.md` | Exit 0, ejecutado por documenter; constitución intacta. |
| SHA-256 de la constitución | `0E45B53EFCC32E154D8B54FF09DA24A4A6C46403C9328E74E54E6D919CA09C63`, comprobado por documenter. |
| `python tools/validate-universal.py --json`, coordinador | Exit 0, `ok: true`, `missing: []`, `errors: []`; conserva cuatro advertencias heredadas. |
| `git diff --check -- docs .specify/memory/constitution.md` | Exit 0, ejecutado por coordinador y documenter. |
| Comprobación directa con Python estándar, coordinador | Exit 0; 4 archivos y 43 enlaces locales Markdown/Wikilinks comprobados, sin problemas de destino ni espacios finales. |
| Comprobación directa de las dos notas nuevas, documenter | Exit 0; 19 Wikilinks y whitespace comprobados, sin problemas. |
| `git diff --check` global, coordinador | Exit 1 únicamente por espacios sobrantes preexistentes en `design/style-guide/tokens.html:19` y `:75`, preservados y fuera de tarea. |

Las cuatro advertencias heredadas corresponden al MOC frente a HEAD `73e3c0f` y a enlaces
de ejemplo de `ESTADOS-Y-PROGRESO` hacia `RF-001-autenticacion`, `Tarea-configurar-rbac` y
`SPRINT-01-acceso`. La verificación conjunta incluye PRO-ARCH-003, esta evidencia, su
checkpoint y el estado activo. El coordinador también repitió la comprobación de constitución
sin diff y con SHA-256 original. No se declaran limpios los cambios locales ajenos.

No se ejecutaron pruebas Django, migraciones, pruebas de carga ni despliegue. No se midieron
tiempos de implementación, concurrencia, latencia, costes operativos o facilidad de cambios.
Las ilustraciones de venta y evolución no son funcionalidades nuevas aprobadas ni fallos
observados en producción. Las 37 tareas de SPEC-001 no se ejecutaron en esta comparación.

## Fuentes y continuación

La propuesta enlaza CAT-REQ-001, módulos detallados, roadmap y plan de SPEC-001. Sus fuentes
consultadas incluyen [arquitectura de microservicios de Microsoft](https://learn.microsoft.com/en-us/azure/architecture/guide/architecture-styles/microservices),
[consideraciones de datos](https://learn.microsoft.com/en-us/azure/architecture/microservices/design/data-considerations),
[JsonResponse de Django 5.2](https://docs.djangoproject.com/en/5.2/ref/request-response/#jsonresponse-objects),
[Microservice Trade-Offs](https://martinfowler.com/articles/microservice-trade-offs.html) y
[Monolith First](https://martinfowler.com/bliki/MonolithFirst.html). Los argumentos de Fowler
son análisis del autor, no benchmarks ni garantías para Zhud Alelí. El cierre del reviewer
y su P3 corregido proceden del handoff del coordinador.

Pendientes: aclarar prioridades de autonomía, operación,
contratos, dependencias, disponibilidad y coste; seleccionar y aceptar una arquitectura;
registrar ADR y enmienda correspondiente solo tras acuerdo real. Siguen abiertas revisión
académica, P-11, P-13/P-14, specs futuras y despliegue donde corresponda. Un commit requiere
autorización explícita y validación de git-manager; `post_commit` requiere hash real y archivos
incluidos. El [[../../bitacora/checkpoints/2026-10-07-alternativas-entrega-incremental|checkpoint]]
conserva el próximo paso sin inferir aprobación.
