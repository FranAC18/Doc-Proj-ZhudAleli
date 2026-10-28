---
title: Matriz de trazabilidad del proyecto
type: traceability
status: in-progress
date: 2026-07-25
tags:
  - proyecto/tesis
  - tipo/trazabilidad
---

# Matriz de trazabilidad

Esta matriz es un índice de enlaces, no una copia de los requisitos. Se completa cuando una
especificación es confirmada y se actualiza al implementar, probar y validar.

## Objetivos a incrementos

| Objetivo del anteproyecto | Capacidad prevista | Sprint | Spec aprobada | Estado |
|---|---|---|---|---|
| OE-01 Analizar procesos y requerimientos | Product Backlog validado | Fase I | Pendiente | `in-progress` |
| OE-02 Desarrollar módulos y control de acceso | Acceso básico de usuarias internas | S1 | [[../../specs/001-acceso-usuarias-internas/spec\|SPEC-001 `confirmed`]] | `in-progress` |
| OE-02 Desarrollar módulos y control de acceso | Planificación | S2 | Pendiente | `planned` |
| OE-02 Desarrollar módulos y control de acceso | Asistencia y participación | S3 | Pendiente | `planned` |
| OE-02 Desarrollar módulos y control de acceso | Trazabilidad productiva | S4 | Pendiente | `planned` |
| OE-02 Desarrollar módulos y control de acceso | Reportes e información | S5 | Pendiente | `planned` |
| OE-03 Evaluar adecuación funcional | Evaluación ISO/IEC 25010:2023 | Fase IV | Pendiente | `planned` |

## Requisitos

| ID                                                                     | Fuente validada                  | Spec                                                                       | Sprint                      | Diseño/ADR                                                                                                                                                                                                                                                                                                                                                            | Código                              | Prueba                                                                                                     | Evidencia                                                                                                                                                                                                                                                                                                                                                                                                          | ISO 25010                                                                            | Estado                                                   |                                                               |
| ---------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------------------------------- | --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | -------------------------------------------------------- | ------------------------------------------------------------- |
| [[../requirements/CAT-REQ-001                                          | CAT-REQ-001]]                    | F1-F9; tesista, organización y presidenta; Levantamiento de requisitos 1.0 | Pendiente por funcionalidad | Fase I                                                                                                                                                                                                                                                                                                                                                                | D-001 a D-010; P-01 a P-12 visibles | —                                                                                                          | —                                                                                                                                                                                                                                                                                                                                                                                                                  | [[../evidence/fase-i/2026-07-22-validacion-cat-req-001-v1]]                          | Completitud y pertinencia                                | Línea base `confirmed`: 57 IDs; 2 `proposed`; 12 `superseded` |
| [[../requirements/proposals/2026-07-22-catalogo-revisado-requisitos-r3 | CAT-REQ-001-R3]]                 | F1-F9; propuesta previa                                                    | —                           | Fase I                                                                                                                                                                                                                                                                                                                                                                | Sustituido por CAT-REQ-001          | —                                                                                                          | —                                                                                                                                                                                                                                                                                                                                                                                                                  | [[../evidence/fase-i/2026-07-22-respuestas-tesista-cat-req-001-r3]]                  | Completitud y pertinencia                                | `superseded`                                                  |
| `RF-ACC-001`                                                           | CAT-REQ-001; tesista; D-011      | [[../../specs/001-acceso-usuarias-internas/spec\|SPEC-001 `confirmed`]]    | S1                          | [[../decisions/ADR-0003-estructura-raiz-aplicacion-django\|ADR-0003]]; [[../../specs/001-acceso-usuarias-internas/plan\|plan `approved`]]; [[../../specs/001-acceso-usuarias-internas/research\|investigación]]; [[../../specs/001-acceso-usuarias-internas/data-model\|modelo de datos]]; [[../../specs/001-acceso-usuarias-internas/contracts/http\|contrato HTTP]] | —                                   | Checklist 16/16; estrategia CA-01 a CA-11 definida en el plan; tareas pendientes                           | [[../evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0\|ACT-REQ-001]]; [[../evidence/fase-i/2026-07-25-confirmacion-spec-001\|EVID-SPEC-001]]; [[../evidence/fase-i/2026-08-24-aprobacion-plan-spec-001\|EVID-PLAN-001]]; [[../bitacora/checkpoints/2026-07-25-plan-spec-001-borrador\|checkpoint del plan]]; [[../bitacora/checkpoints/2026-08-24-aprobacion-plan-spec-001\|checkpoint de aprobación]] | Completitud, corrección, pertinencia, operabilidad, accesibilidad y confidencialidad | Plan técnico `approved` el 2026-08-24; tareas pendientes |                                                               |
| `RNF-UX-001`                                                           | CAT-REQ-001; SPEC-001 confirmada | [[../../specs/001-acceso-usuarias-internas/spec\|SPEC-001]]                | S1                          | [[../../specs/001-acceso-usuarias-internas/plan#Interfaz\|interfaz móvil]]                                                                                                                                                                                                                                                                                            | —                                   | Recorrido a 360 px y formularios sin desbordamiento; tareas pendientes                                     | [[../bitacora/checkpoints/2026-07-25-plan-spec-001-borrador\|checkpoint del plan]]; [[../bitacora/checkpoints/2026-08-24-aprobacion-plan-spec-001\|checkpoint de aprobación]]                                                                                                                                                                                                                                      | Interacción: operabilidad y accesibilidad                                            | Plan `approved`                                          |                                                               |
| `RNF-UX-002`                                                           | CAT-REQ-001; SPEC-001 confirmada | [[../../specs/001-acceso-usuarias-internas/spec\|SPEC-001]]                | S1                          | [[../../specs/001-acceso-usuarias-internas/plan#Interfaz\|accesibilidad]]                                                                                                                                                                                                                                                                                             | —                                   | Contraste, teclado, foco, zoom 200 %, errores y cajas 44 × 44 px; tareas pendientes                        | [[../bitacora/checkpoints/2026-07-25-plan-spec-001-borrador\|checkpoint del plan]]; [[../bitacora/checkpoints/2026-08-24-aprobacion-plan-spec-001\|checkpoint de aprobación]]                                                                                                                                                                                                                                      | Interacción: accesibilidad                                                           | Plan `approved`                                          |                                                               |
| `RNF-UX-003`                                                           | CAT-REQ-001; SPEC-001 confirmada | [[../../specs/001-acceso-usuarias-internas/spec\|SPEC-001]]                | S1                          | [[../../specs/001-acceso-usuarias-internas/plan#Interfaz\|lenguaje y recorrido común]]                                                                                                                                                                                                                                                                                | —                                   | Comprensión sin roles, permisos ni términos técnicos; tareas pendientes                                    | [[../bitacora/checkpoints/2026-07-25-plan-spec-001-borrador\|checkpoint del plan]]; [[../bitacora/checkpoints/2026-08-24-aprobacion-plan-spec-001\|checkpoint de aprobación]]                                                                                                                                                                                                                                      | Interacción: operabilidad y capacidad de aprendizaje                                 | Plan `approved`                                          |                                                               |
| `RNF-CON-001`                                                          | CAT-REQ-001; SPEC-001 confirmada | [[../../specs/001-acceso-usuarias-internas/spec\|SPEC-001]]                | S1                          | [[../../specs/001-acceso-usuarias-internas/plan#Interfaz\|recursos locales y recuperación]]                                                                                                                                                                                                                                                                           | —                                   | Corte durante cada `POST`, reintento seguro y ausencia de recursos remotos obligatorios; tareas pendientes | [[../bitacora/checkpoints/2026-07-25-plan-spec-001-borrador\|checkpoint del plan]]; [[../bitacora/checkpoints/2026-08-24-aprobacion-plan-spec-001\|checkpoint de aprobación]]                                                                                                                                                                                                                                      | Eficiencia de desempeño y fiabilidad                                                 | Plan `approved`                                          |                                                               |
| `RNF-SEC-001`                                                          | CAT-REQ-001; SPEC-001 confirmada | [[../../specs/001-acceso-usuarias-internas/spec\|SPEC-001]]                | S1                          | [[../../specs/001-acceso-usuarias-internas/plan#Autorización y privacidad\|autorización]]; [[../../specs/001-acceso-usuarias-internas/contracts/http\|contrato HTTP]]                                                                                                                                                                                                 | —                                   | Casos positivos/negativos, CSRF, sesión, concurrencia, caché y salida; tareas pendientes                   | [[../bitacora/checkpoints/2026-07-25-plan-spec-001-borrador\|checkpoint del plan]]; [[../bitacora/checkpoints/2026-08-24-aprobacion-plan-spec-001\|checkpoint de aprobación]]                                                                                                                                                                                                                                      | Seguridad: confidencialidad e integridad                                             | Plan `approved`                                          |                                                               |
| `RNF-PRV-001`                                                          | CAT-REQ-001; SPEC-001 confirmada | [[../../specs/001-acceso-usuarias-internas/spec\|SPEC-001]]                | S1                          | [[../../specs/001-acceso-usuarias-internas/plan#Autorización y privacidad\|minimización y privacidad]]                                                                                                                                                                                                                                                                | —                                   | Revisión de campos, respuestas, logs y evidencia anonimizada; tareas pendientes                            | [[../bitacora/checkpoints/2026-07-25-plan-spec-001-borrador\|checkpoint del plan]]; [[../bitacora/checkpoints/2026-08-24-aprobacion-plan-spec-001\|checkpoint de aprobación]]                                                                                                                                                                                                                                      | Seguridad: confidencialidad                                                          | Plan `approved`                                          |                                                               |

## Reglas

1. No añadir un RF/RNF como confirmado sin fuente y evidencia de validación.
2. Enlazar rutas relativas o Wikilinks al artefacto exacto.
3. Un requisito puede tener varias pruebas, pero cada criterio de aceptación debe quedar
   cubierto por al menos una evidencia o una limitación documentada.
4. “Implementado” significa código integrado y pruebas ejecutadas; “validado” requiere la
   evidencia humana o técnica definida.
5. Para adecuación funcional registrar la subcaracterística evaluada: completitud,
   corrección o pertinencia/apropiación funcional, según el instrumento aprobado.

## Cierre de sprint

El tesista decide cuándo cerrar el periodo. Revisar las filas, enlaces, pruebas, evidencias y
defectos informa el resultado, pero no es una condición previa ni requiere aprobación aparte.
Anotar el resultado y los pendientes en el estado operativo o backlog existente para dar
continuidad; el apunte no es precondición. Cerrar el periodo no marca como terminadas las
tareas, criterios o requisitos que sigan sin verificación.

## Entregas del repositorio de aplicación

### Incremento de S2 en rama de aplicación — `SB-S2-01` / avance `SB-S2-02`

Esta tabla registra el incremento de aplicación en su rama feature, aún sin integrar mediante PR a `main`; no sustituye la tabla de entregas por PR/tag. El commit inicial de la app es `903f1f9a55777992468ad88575d1f58463318516`. El checkpoint post_commit conserva los archivos y verificaciones de ese commit. El 2026-10-27 pasaron 17 pruebas PostgreSQL, incluidas nueve nuevas del acceso; la revisión de interfaz y PWA en navegador sigue pendiente. Estas pruebas locales aún no forman parte de un commit.

| RF | HU | HT | Spec y criterio | Código o prueba local | Resultado real |
|---|---|---|---|---|---|
| `RF-ACC-001` | `HU-ACC-001` | `HT-GEN-001`, `HT-GEN-009` | `SPEC-001`, CA-ACC-001-01 a 13 | `app/apps/accounts/models.py`, `app/apps/accounts/migrations/0001_initial.py`, `app/apps/accounts/migrations/0002_loginthrottle.py`, `app/apps/accounts/forms.py`, `app/apps/accounts/services.py`, `app/apps/accounts/views.py`, `app/apps/accounts/urls.py`, `app/apps/accounts/templates/accounts/`, `app/apps/accounts/tests/test_flujo_acceso.py` | Migraciones y comprobación de esquema aprobadas en PostgreSQL. Nueve pruebas nuevas verifican acceso, salida, errores, bloqueo, cambio de contraseña, sesión vencida, cuenta desactivada, caché y CSRF; pasan las 17 pruebas de la app. Interfaz y PWA en navegador pendientes; el nuevo archivo de prueba no está en commit. |
| `RF-ACC-001` | `HU-ACC-001` | `HT-GEN-001` | `SPEC-001`, primera cuenta controlada | `app/apps/accounts/management/commands/create_initial_account.py`, `app/apps/accounts/tests/test_management_command.py` | Pruebas del comando aprobadas en PostgreSQL aislado. No se creó una cuenta real. |
| `RF-PWA-001` | `HU-PWA-001` | Base transversal de S2 | Requisito confirmado; interfaz esencial pública, sin caché privado | `app/static/manifest.json`, `app/static/pwa/service-worker.js`, `app/tests/test_pwa.py` | Tres pruebas de respuestas/archivos sin BD: ejecutadas y aprobadas. Instalación y corte de red en navegador: pendientes. |

La ruta `app/` identifica el checkout anidado de la app, ignorado por el Git general. El commit inicial fue autorizado y publicado en la rama feature del remoto independiente; la app aún no tiene PR ni tag, por lo que no se registra como integrada a `main`.

La referencia de código apunta a `FranAC18/App-zhudaleli`; la evidencia de requisitos
y el estado del sprint permanecen en este repositorio general. Se agrega una fila por
RF entregado al integrarse un PR. Un commit intermedio de app no exige una actualización
documental previa. No se registran PR, hash ni tag antes de que existan realmente.

| Requisito | Sprint | PR de app | Tag de app | Hash integrado | Estado |
|---|---|---|---|---|---|
| `RF-ACC-001` | S1 | — | — | — | Sin entrega de código; S1 cerrado administrativamente con resultado parcial. |

Al cerrar un sprint con código integrado, registrar `sprint-N` en la app y actualizar
esta tabla con PR, tag y hash reales. Para S0 no hubo aplicación Django: sin entrega
de código ni tag de app.
Si `RF-ACC-001` se implementa en un sprint posterior al cierre de S1, se agrega
otra fila con el sprint real de ejecución y se conserva esta fila histórica de S1.
El `S1` de SPEC-001 en artefactos antiguos corresponde al S2 del calendario actual;
el commit usa el sprint del calendario en que se ejecuta el cambio.

## Reconciliación documental del 2026-09-28

La [[../evidence/casos-de-uso/2026-09-28-coherencia-integral|matriz de auditoría integral]]
complementa las filas anteriores: comprueba los 57 IDs aprobados contra su regla fuente,
módulo y caso de uso propuesto. No acredita código ni pruebas funcionales ejecutadas.

| Cambio | Fuente | Diseño afectado | Estado real |
|---|---|---|---|
| Continuidad offline obligatoria | EVID-FACT-001 y EVID-PLAN-002 | [[../requirements/proposals/2026-09-28-catalogo-v1-1|Revisión v1.1]], CU-OFF-01/02 | Requisitos y criterios aprobados por el tesista en v1.1; políticas P-13/P-14 pendientes |
| RNF-CON-001, asistencia y pesajes | v1.0 + revisión v1.1 | P-13/P-14; futuras specs attendance/traceability/PWA | Aprobación propia del tesista el 28/09; acceso básico de SPEC-001 conserva su alcance |
| 16 semanas / USD 2.869 / stack | [[../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack|EVID-PLAN-002]] | Plan maestro, módulos, contexto y roadmap | Referencia actual aportada; no es evidencia de viabilidad ya probada |
| Tareas de SPEC-001 | Plan aprobado y hallazgos S1–S4 | T008/T013/T014/T033/T037 | Orden y CI corregidos; tareas aún pendientes |

## Promoción de requisitos a v1.1

Fuente: [[../evidence/casos-de-uso/2026-09-28-aprobacion-requisitos-v1-1|EVID-REQ-APP-001]].
Catálogo vigente: [[../requirements/CAT-REQ-001|60 confirmed, 2 proposed, 12 históricos]].
El corte de 57 de la auditoría anterior se conserva como historial.

| ID | Casos y módulo | Estado | Prueba y evidencia de implementación |
|---|---|---|---|
| RF-PWA-001 | CU-OFF-01; interfaz esencial transversal | `confirmed` por el tesista | Apertura con corte tras preparación; pendiente de spec y ejecución |
| RF-PWA-002 | CU-OFF-01, ASI-01, TRA-01/02; attendance/traceability | `confirmed` por el tesista | Persistencia al recargar, fallo local e aislamiento entre cuentas; pendiente de spec y ejecución |
| RF-PWA-003 | CU-OFF-02; sincronización y módulos propietarios | `confirmed` por el tesista | Respuesta perdida/reintento, revocación, conflicto y reversión atómica; pendiente de spec y ejecución |

Los ajustes de RNF-CON-001, RF-ASI-001/007, RF-TRA-001/002 y P-10 están en el catálogo.
Esta aprobación no acredita código ni resultados de pruebas, y no resuelve P-13/P-14.
