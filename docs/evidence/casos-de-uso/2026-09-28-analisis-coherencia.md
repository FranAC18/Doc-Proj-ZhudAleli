---
title: Análisis de coherencia de casos de uso y SPEC-001
type: evidence
status: recorded
id: ANA-CU-001
date: 2026-09-28
task_id: CU-REVIEW-001
phase: pre_commit
commit: pending
branch: opencode/spec-001-fase-1-diseno
head: a6e842f63917b2ac28a64c80b00d68069ba2fabd
module: transversal
sprint: transversal
related:
  - "[[2026-09-28-cronograma-presupuesto-stack]]"
  - "[[../../requirements/proposals/2026-09-28-casos-de-uso]]"
  - "[[../../requirements/proposals/2026-09-28-diagramas-casos-de-uso]]"
  - "[[2026-09-28-factibilidad-aportada]]"
  - "[[../../../specs/001-acceso-usuarias-internas/spec]]"
  - "[[../../../specs/001-acceso-usuarias-internas/plan]]"
  - "[[../../../specs/001-acceso-usuarias-internas/tasks]]"
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[../../bitacora/checkpoints/2026-09-28-revision-casos-de-uso]]"
tags:
  - proyecto/tesis
  - tipo/evidencia
  - modulo/transversal
---

# Análisis de coherencia de casos de uso y SPEC-001

## Dictamen y alcance

El PDF contiene **21 casos, tres actores declarados y cinco diagramas por módulo**.
Es una base útil de interacción, pero no es una especificación completa ni consistente con
todos los criterios aprobados. Las principales brechas afectan acceso, autoridad organizativa,
encargos, secado, ventas, saldos, auditoría y reportes. No hay aplicación Django que permita
demostrar estos recorridos: esta revisión es documental.

Durante el análisis el tesista aportó la factibilidad y exigió guardar/sincronizar sin conexión.
Por ello **CU-OFF-01/02 se mantienen como obligatorios en el diseño solicitado**. La conclusión
inicial que los trataba como diferidos quedó superada para esta propuesta. Persiste una
inconsistencia de versiones con CAT-REQ-001, que todavía excluye la sincronización automática.
No se confunde esta instrucción con validación de la organización/directora ni con aprobación
de parámetros de reloj, permisos y conflictos que aún no están definidos.

Se aplicó `speckit-analyze` a la única funcionalidad activa que tiene spec/plan/tasks. Su
análisis no modifica esos artefactos. El informe se guarda mediante documenter porque el
tesista pidió expresamente documentar y enlazar los resultados. No se promueven propuestas
ni se reescriben documentos aprobados. La cobertura del producto se mide por separado de la
cobertura de tareas de SPEC-001.

**Actualización posterior del mismo día:** el tesista aportó el nuevo Gantt, presupuesto y
stack (F10). I4 e I5 quedan resueltos respecto de la referencia vigente: USD 2.869 y 16
semanas relativas. El informe conserva 22 hallazgos históricos de PDF/factibilidad, de los
cuales 20 siguen abiertos y 2 tienen esta resolución; los cuatro hallazgos de SPEC-001 no
cambian. No se deducen fechas calendario ni se da por probado el despliegue.

## Fuentes examinadas

| Clave | Fuente y condición |
|---|---|
| F1 | [PDF de casos de uso](<F:/Software/8vo Semestre/Aplicaciones Informaticas II/Acero_Franklin_7402_CasosDeUso_Aplicaciones II.pdf>), 25/09/2026, 23 páginas. Texto completo extraído; diagramas pp. 5–7 y fichas críticas revisados visualmente. |
| F2 | [[../../requirements/CAT-REQ-001|CAT-REQ-001 v1.0]]: 57 confirmed, 2 proposed, 12 superseded. |
| F3 | [[../../requirements/proposals/2026-07-22-catalogo-revisado-requisitos-r3|R3 histórico]], exclusivamente reglas incorporadas por F2; no se heredan sus recomendaciones históricas frente al ajuste canónico. |
| F4 | [[../../evidence/fase-i/2026-07-22-validacion-cat-req-001-v1|Validación del catálogo]] y [[../../evidence/fase-i/2026-07-25-acta-levantamiento-requisitos-1-0|ACT-REQ-001]]. |
| F5 | [[../../00-inicio/01-decisiones-pendientes|D-003 a D-011 y P-01 a P-12]]. |
| F6 | [[../../../specs/001-acceso-usuarias-internas/spec|SPEC-001]], [[../../../specs/001-acceso-usuarias-internas/plan|plan]] y [[../../../specs/001-acceso-usuarias-internas/tasks|36 tareas]]. |
| F7 | [[../../architecture/PLAN-DESDE-CERO|Plan maestro del 22/09]] y [[../../decisions/proposals/2026-09-22-arquitectura-modular-desacoplada|propuesta arquitectónica]]. Cambios preexistentes; roadmap proposed, revisión de directora pendiente, PWA por operación condicionada. |
| F8 | [[2026-09-28-factibilidad-aportada|Texto de factibilidad e instrucción expresa del tesista]], recibidos durante esta sesión. No se recibió archivo original firmado. |
| F9 | [[../../../.specify/memory/constitution|Constitución 0.1.0]], [[../../traceability/MATRIZ-TRAZABILIDAD|matriz global]], contexto y políticas del vault. |
| F10 | [[2026-09-28-cronograma-presupuesto-stack|Nuevo Gantt, presupuesto y stack aportados por el tesista]]: 16 semanas, USD 2.869 y 14 entradas tecnológicas; tres imágenes preservadas. |

Huella SHA-256 de F1:
`2dd8b9cf9e0fe6ae9545559536f623a3dd48155cfe76594c4edf16b6e1153647`.
El PDF externo no se copia a Git; no se reproducen identidades de aprobadores ni firmas.
El enlace a F1 depende de la ruta local; las fichas y la evidencia son portables dentro del vault.

Fuentes técnicas complementarias consultadas el 28/09/2026:

- [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1): referencia normativa de notación.
  La página de especificación se consultó; el visor web no pudo cargar el PDF normativo por tamaño.
- [PlantUML: diagramas de casos de uso](https://plantuml.com/use-case-diagram): sintaxis de actores,
  casos, asociaciones y límites empleada para los esquemas editables.
- [MDN: Background Synchronization](https://developer.mozilla.org/en-US/docs/Web/API/Background_Synchronization_API):
  disponibilidad limitada y contexto seguro. Motiva reintento con la aplicación abierta, sin
  prometer ejecución universal al cerrar el navegador.
- [Vercel: runtime Python](https://vercel.com/docs/functions/runtimes/python) y
  [Supabase: conexión a PostgreSQL](https://supabase.com/docs/guides/database/connecting-to-postgres):
  distinguen ejecución de Django de persistencia/conexión. No se probaron despliegue, cuotas ni costos.

## Hallazgos sobre PDF, factibilidad y línea base

Severidad: CRITICAL bloquea usar la documentación como base de implementación de la parte
afectada; HIGH exige corregir contrato, permisos o reglas; MEDIUM requiere precisión;
LOW es editorial. Las filas identifican conflictos comprobados o vacíos, no defectos de
código inexistente. Los IDs se conservan para futuras revisiones.

| ID | Categoría | Severidad | Localización | Hallazgo e impacto | Corrección propuesta |
|---|---|---|---|---|---|
| C1 | Inconsistencia de alcance | CRITICAL | F1 pp. 4, 12–13; F2 «Solución organizacional», puntos 1/9 e IDs offline; F7 §2; F8 §2.1 | Offline obligatorio por nueva instrucción, pero catálogo vigente lo excluye; implementar desde ambas fuentes produce contratos opuestos. | Versionar reconciliación; mantener OFF-01/02 en propuesta y especificar operaciones sin reactivar silenciosamente IDs históricos. |
| C2 | Tiempo y autorización offline | HIGH | F1 CU-ASI-01/OFF-01/OFF-02; F2 RF-ASI-007; F3 RF-ASI-001 y RF-TRA-002 | Hora del servidor y QR temporal no se preservan simplemente guardando hora local. Faltan política de sesión, permisos revocados y decisión sobre evento tardío. | Separar captura/recepción, evento provisional/aceptado; especificar QR offline, revalidación y revisión sin inventar hora ni tolerancias. |
| C3 | Seguridad de acceso | HIGH | F1 p. 10, alterno cuenta inactiva; F6 spec líneas 151–153 y CA-03 | El PDF anuncia cuenta inactiva; SPEC-001 exige respuesta equivalente a credenciales inválidas. | Mensaje no revelador común y prueba negativa. |
| G1 | Cobertura de acceso | HIGH | F1 ADM-01 a 04; F6 spec HU-03 y líneas 166–184 | Faltan cambio propio, cambio inicial obligatorio, vigencia de 30 minutos y procedimiento de primera cuenta. | Añadir ADM-05/06; reglas de sesión y procedimiento controlado según SPEC-001, sin dar administración técnica a Directiva. |
| I1 | Alcance de dashboard | MEDIUM | F1 ADM-02 p. 10 y REP-01 p. 22; F6 spec líneas 54–59, 173–175 | Inicio básico, inicio personalizado y dashboard consolidado se mezclan. El panel solo Directiva no cubre resumen de socia. | Separar ADM-06, RF-ACC-004 futuro, REP-01 y REP-03. |
| U1 | Permisos y encargos | HIGH | F1 pp. 7–8, ADM-04, PLA-02 y TRA-01 a 05; F3 RF-ACC-003/PLA-003 | «Según rol» no determina cargo, encargo, vigencia, alcance ni corrección. | Asociaciones de diagramas no conceden permisos; completar matriz por operación P-01 y encargo temporal PLA-04. |
| G2 | Planificación incompleta | MEDIUM | F1 PLA-01/02, pp. 13–14; F3 RF-PLA-001/003/005 | No define todos los datos de actividad/instancia ni encargo ni plan de producción con cantidades e insumos. | Completar fichas; PLA-04/05; planificación no crea existencias. |
| G3 | Asistencia y autoridad | HIGH | F1 ASI-01/02, pp. 15–16; F2 RF-ASI-007 ajustado; F3 RF-ASI-003/005/006 | No desarrolla QR/código/delegación; validación genérica de Directiva no documenta decisión de asamblea, corrección auditada ni participación adicional. | Precisar ASI-02 como registro de resolución, ASI-04/05, origen y motivo; sin sanción automática. |
| G4 | Secado | HIGH | F1 TRA-02 p. 18; F3 RF-TRA-002/003; F5 D-003 | Omite temperatura Celsius obligatoria, humedad opcional y tiempos automáticos; «merma cuando corresponda» es insuficiente. | Completar datos de inicio/cierre, fórmula/unidad, peso final mayor y política temporal offline. |
| G5 | Producción e historia | HIGH | F1 TRA-01/03/07; F3 RF-TRA-001/004/005 | Acopio sin unidad/valoración explícitas; lote no precisa composición, residuos, rendimiento, cierre frente a agotamiento y mezcla física. | Completar campos e invariantes; mantener P-04/P-05 sin inventar conversiones. |
| I2 | Consulta que muta inventario | HIGH | F1 TRA-04 p. 19, paso 5; F2 invariantes 2/3; F3 RF-INV-002 | La consulta incorpora generación de movimientos; podría implementarse stock dependiente de abrir pantalla. | Movimiento en transacción de operación origen; consulta pura; ajuste auditado independiente TRA-08. |
| G6 | Despacho y venta | HIGH | F1 TRA-05 p. 20 y catálogo pp. 8–9; F3 RF-INV-003 y RF-VEN-001 a 007 | Despacho no reemplaza venta; falta stock individual/compartido, recepción, venta multiproducto, comprador, valor base, excepción y políticas. | VEN-01 y subflujos; separar custodia/venta/deuda; registrar origen por línea. |
| G7 | Cuentas por cobrar | HIGH | F1 TRA-06 p. 21, paso 4; F3 RF-CXC-001/002/003 | Solo contempla deuda del despacho y «actualizar saldo»; no define deuda externa, movimiento de abono ni conciliación. | Saldo derivado, CXC-01/02, dos cuentas separadas; P-09 para efectos excepcionales. |
| G8 | Gastos y catálogos | MEDIUM | F1 lista completa pp. 8–9; F3 RF-CAT-001/INV-001/GAS-001/GAS-002 | No hay recorridos para catálogo histórico, valores vigentes ni gastos/resumen económico. | CAT-01/GAS-01; no presentar costos incompletos como cero o balance certificado. |
| G9 | Reportes y publicación | HIGH | F1 REP-02 p. 23, ADM-01 p. 9; F3 RF-REP-002/005/006, NOT-001, PUB-002, RNF-PDF-001 | Faltan descarga PDF explícita, resumen privado, recordatorios y flujo editorial; las familias actividades/encargos y ventas no tienen detalle suficiente. | Completar REP-02; REP-03/PUB-01; criterios de PDF y permiso por cargo. |
| U2 | Objetivos y relaciones UML | MEDIUM | F1 p. 5 y fichas PLA-02, TRA-02/05/06 | «uses/extends» se usa para dependencias de datos/orden, no reutilización o extensión precisa; TRA-06 dice extender despacho pero el diagrama no muestra esa relación. | No sustituir mecánicamente por include/extend. Actividad/acopio/stock previos son precondiciones; cobro posterior es caso independiente. |
| U3 | Sincronización insuficiente | HIGH | F1 pp. 11–13; F8 §2.1 | «Orden lógico» no define duplicados, pérdida de acuse, conflictos, equipos compartidos ni reintento compatible. | ID estable, resultado idempotente, atomicidad, aislamiento por cuenta, estados visibles y reintento con app abierta; probar corte después de commit y antes de acuse. |
| A1 | Aceptación ambigua | MEDIUM | F1 REP-01/02, pp. 22–23 | «Indicadores relevantes», «clara» o «actualizados» sin catálogo/fórmula/periodo/criterios comprobables. | Vincular cada indicador a fuente, unidad, filtro y criterio; no declarar validación UX sin usuarias. |
| I3 | Precondiciones y editorial | LOW | F1 índice p. 2, contenido pp. 7–9, ADM-01, ASI-03/TRA-07/REP-02 | Índice anuncia actores p. 9 y fichas p. 12; comienzan p. 7 y p. 9. «Opcional» confunde alcance público. Exigir datos contradice alternos vacíos. | Regenerar índice; separar prioridad de obligatoriedad; permitir consulta vacía. |
| I4 | Presupuesto de factibilidad | MEDIUM histórica | F8 §2.3; F10 presupuesto | Diferencia histórica entre USD 1.845 y USD 2.869. **Resuelto como referencia** por el nuevo presupuesto aportado: USD 2.869; suma comprobada. | Propagar 2.869 a futuras versiones académicas; conservar 1.845 como antecedente. No queda pendiente escoger importe. |
| I5 | Calendario de factibilidad | MEDIUM histórica | F8 §2.4/2.7; F10 Gantt | Diferencia histórica entre 16 semanas y septiembre–febrero. **Resuelto como referencia** por el nuevo Gantt relativo S1–S16. | Usar los rangos de F10, incluidos solapamientos. Las fechas calendario aún no aportadas no invalidan el cronograma relativo. |
| U4 | Despliegue sin responsabilidad clara | MEDIUM | F8 §2.1; F10 stack y presupuesto | Stack y plataformas identificados; «frontend Vercel/backend Supabase» todavía no precisa dónde ejecuta Django SSR y sus límites, ni prueba respaldo o costo cero. | Documentar ejecución Django, conexión PostgreSQL, estáticos y pruebas; mantener los importes como presupuesto, no como garantía comercial. |

La página 3 de F1 no presenta fecha/firma de aprobación completadas. Es un límite de evidencia,
no prueba de que el documento haya sido rechazado. No se atribuye validez normativa a la
frase del PDF que prioriza la factibilidad: la jerarquía se contrasta con los registros del vault.

## Análisis Spec Kit de la funcionalidad activa

Precondición comprobada con `.specify/scripts/bash/check-prerequisites.sh --json --require-tasks --include-tasks`.
Resultado: `FEATURE_DIR=/f/Tesis/App Tesis/specs/001-acceso-usuarias-internas`;
disponibles `research.md`, `data-model.md`, `contracts/`, `quickstart.md`, `tasks.md`.
Se comprobó también `spec.md`. No existe `.specify/extensions.yml`; no hay hooks que ejecutar.
La primera ejecución de Bash falló por permisos del entorno; el reintento autorizado terminó
con código 0. No se alteró `.specify/feature.json`.

| ID | Categoría | Severidad | Localización | Hallazgo | Recomendación concreta |
|---|---|---|---|---|---|
| S1 | Dependencia | HIGH | tasks.md líneas 81–88; dependencias 179; plan.md estructura | T013 exige que `manage.py check` pase antes de T014, que crea los settings; el resultado no puede reproducirse con el esqueleto descrito. | Mover el check a T014 o definir configuración mínima en T013 y su sustitución controlada. |
| S2 | Dependencia de revisión | HIGH | tasks.md líneas 156–158, 163–165 y 184 | T033 depende explícitamente de T024/T028/T031, pero no de T032 que crea login/cambio. El grafo permite revisar antes de terminar UI. | Añadir T032 a la dependencia de T033; conservar las demás puertas. |
| S3 | Cobertura técnica parcial | MEDIUM | plan.md líneas 321–334; tasks.md T013 y verificación final | T013 crea solo esqueleto CI. El checklist exige CI completa y lint, pero ninguna tarea asigna inequívocamente completarla, configurar lint y verificar su ejecución PostgreSQL. | Añadir tarea concreta de completar CI/ruff y prueba del workflow, sin presentar revisión T033 como implementación. |
| S4 | Referencia inconsistente | MEDIUM | tasks.md T008, líneas 59–63; docs/00-inicio/01-decisiones-pendientes.md | T008 invoca D-001 a D-012; el registro examinado llega a D-011. | Corregir rango o aportar el registro D-012. El mapa de módulos futuros conserva estado propuesto y no bloquea S1. |

No se detectó un conflicto crítico interno entre la spec, el plan y las tareas de acceso
básico. La nueva PWA necesita una especificación y reconciliación propias: no hace que las
operaciones futuras estén implementadas ni autoriza agregarlas silenciosamente a SPEC-001.

### Cobertura de requisitos a tareas

«Sí» indica al menos una tarea planificada asociada por contenido; no prueba ejecución ni
cobertura completa de cada borde. Se cuentan 10 IDs RF explícitos (incluido padre), 6 RNF y
5 SC verificables. SC-002 se vincula a construir/ejecutar el protocolo, no a dar por alcanzado
el resultado humano del 80 %.

| Clave | ¿Tarea? | IDs de tarea | Observación |
|---|---|---|---|
| RF-ACC-001 | Sí | T017–T032 | Requisito padre; no contar como funcionalidad adicional a sus hijos. |
| RF-ACC-001.1 | Sí | T021, T022, T026 | Acceso con credenciales. |
| RF-ACC-001.2 | Sí | T026, T033 | Respuesta equivalente. |
| RF-ACC-001.3 | Sí | T025, T027, T028 | Acceso privado y caché. |
| RF-ACC-001.4 | Sí | T022, T024, T028 | Cierre e invalidación. |
| RF-ACC-001.5 | Sí | T029, T030, T032 | Cambio propio. |
| RF-ACC-001.5a | Sí | T020, T025, T031 | Cambio obligatorio. |
| RF-ACC-001.6 | Sí | T022, T023 | Bienvenida y opciones disponibles. |
| RF-ACC-001.7 | Sí | T020, T033 | Creación controlada; entrega presencial debe quedar verificada al cierre. |
| RF-ACC-001.8 | Sí | T024, T033 | Inactividad 30 minutos. |
| RNF-UX-001 | Sí | T001, T003–T006, T032, T035 | 360 px. |
| RNF-UX-002 | Sí | T002–T006, T032, T035 | Teclado, foco, AA, zoom. |
| RNF-UX-003 | Sí | T005, T006, T032, T035 | Comprensión representativa. |
| RNF-CON-001 | Sí | T015, T035 | Recursos locales, cortes y recuperación. |
| RNF-SEC-001 | Sí | T017–T020, T024–T030, T033 | Casos permitidos y denegados. |
| RNF-PRV-001 | Sí | T020, T023, T026–T028, T033, T035 | Revisión de datos/respuestas/evidencia. |
| SC-001 | Sí | T033, T035 | Matriz CA-01 a CA-11. |
| SC-002 | Sí | T035 | Protocolo con usuarias, sin simulación de resultado. |
| SC-003 | Sí | T004, T005, T032, T035 | Pantallas, zoom y móvil. |
| SC-004 | Sí | T026, T033 | Intentos inválidos equivalentes. |
| SC-005 | Sí | T024, T028, T033 | Reutilización/URL tras salir. |

Tareas de soporte trazadas por finalidad: T007/T011/T012 a puertas de diseño; T008/T009/T010
al modelo de accounts y mapa conceptual futuro permitido; T013–T019 a infraestructura/datos;
T034 a corrección; T036 a cierre. No hay tarea funcional huérfana identificada. Las porciones
de T008/T009 sobre módulos futuros no implementan RF adicionales de SPEC-001.

### Métricas de SPEC-001

- 21 claves analizadas: 10 RF (9 hojas más padre), 6 RNF y 5 SC.
- 36 tareas, todas sin marcar como terminadas en `tasks.md`.
- Cobertura por existencia de tarea: 21/21 = 100 % (20/20 sin contar el padre).
- 0 duplicaciones materiales detectadas; 1 asignación ambigua de trabajo (S3).
- 4 hallazgos: 2 HIGH y 2 MEDIUM; 0 CRITICAL internos.
- No equivale a pruebas pasadas; S1/S2 deben resolverse antes de ejecutar el orden publicado.

## Cobertura del PDF frente al catálogo del producto

Esta matriz incluye los 57 IDs confirmed de F2. **Parcial** significa presencia del objetivo
con criterios importantes ausentes; **ausente** significa sin recorrido identificable;
**contradictoria** indica conducta opuesta a la fuente comparada. La nueva obligatoriedad
offline se registra aparte: no altera retroactivamente lo que decía F2.
La tabla no exige que todo RNF sea una elipse UML ni que cada RF tenga exactamente un CU.

| Requisito confirmed | Presencia en PDF | Evaluación | Hallazgo |
|---|---|---|---|
| RF-ACC-001 | CU-ADM-02/03 | Contradictoria | C3/G1 |
| RF-ACC-002 | CU-ADM-04 | Parcial | U1 |
| RF-ACC-003 | CU-ADM-04 y permisos genéricos | Parcial | U1 |
| RF-ACC-004 | CU-PLA-03; CU-REP-01 | Parcial | I1 |
| RF-PLA-001 | CU-PLA-01 | Parcial | G2 |
| RF-PLA-002 | CU-PLA-02 | Parcial | G2 |
| RF-PLA-003 | — | Ausente | U1/G2 |
| RF-PLA-004 | CU-PLA-03 | Parcial | G2 |
| RF-PLA-005 | — | Ausente | G2 |
| RF-ASI-001 | CU-ASI-01 | Parcial | C2/G3 |
| RF-ASI-002 | CU-ASI-01/02 | Parcial | G3 |
| RF-ASI-003 | — | Ausente | G3 |
| RF-ASI-004 | CU-ASI-03 | Parcial | G3 |
| RF-ASI-005 | — | Ausente | G3 |
| RF-ASI-006 | CU-ASI-02 | Parcial | G3 |
| RF-ASI-007 | — | Ausente | C2/G3 |
| RF-CAT-001 | — | Ausente | G8 |
| RF-INV-001 | — | Ausente | G8 |
| RF-TRA-001 | CU-TRA-01 | Parcial | G5 |
| RF-TRA-002 | CU-TRA-02 | Parcial | G4 |
| RF-TRA-003 | CU-TRA-02 | Parcial | G4 |
| RF-TRA-004 | CU-TRA-03/07 | Parcial | G5 |
| RF-TRA-005 | CU-TRA-03 | Parcial | G5 |
| RF-INV-002 | CU-TRA-03/04/05 | Parcial | I2 |
| RF-INV-003 | CU-TRA-05 | Parcial | G6 |
| RF-INV-004 | — | Ausente | G6/G7 |
| RF-VEN-001 | — | Ausente | G6 |
| RF-VEN-002 | — | Ausente | G6 |
| RF-VEN-003 | — | Ausente | G6 |
| RF-VEN-004 | — | Ausente | G6 |
| RF-VEN-005 | — | Ausente | G6 |
| RF-VEN-006 | — | Ausente | G6 |
| RF-VEN-007 | — | Ausente | G6 |
| RF-VEN-008 | — | Ausente | C1 |
| RF-GAS-001 | — | Ausente | G8 |
| RF-GAS-002 | — | Ausente | G8 |
| RF-CXC-001 | CU-TRA-05/06 | Parcial | G7 |
| RF-CXC-002 | CU-TRA-06 | Parcial | G7 |
| RF-CXC-003 | — | Ausente | G7 |
| RF-REP-001 | CU-REP-02 | Parcial | G9 |
| RF-REP-002 | CU-REP-01; referencia general | Parcial | G9 |
| RF-REP-003 | CU-REP-02 | Parcial | G9 |
| RF-REP-004 | CU-REP-02 | Parcial | G9 |
| RF-REP-005 | CU-REP-01/02; sin desglose | Parcial | G9 |
| RF-REP-006 | — | Ausente | I1/G9 |
| RF-NOT-001 | — | Ausente | G9 |
| RF-PUB-001 | CU-ADM-01 | Parcial | I3/G9 |
| RF-PUB-002 | — | Ausente | G9 |
| RNF-UX-001 | PDF p. 4; transversal | Parcial | A1 |
| RNF-UX-002 | PDF p. 4; transversal | Parcial | A1 |
| RNF-UX-003 | PDF p. 4; cálculos TRA-02 | Parcial | A1 |
| RNF-CON-001 | CU-OFF-01/02; distinto alcance | Contradictoria | C1 |
| RNF-SEC-001 | Permisos y alternos de denegación | Parcial | U1/U3 |
| RNF-AUD-001 | — | Ausente | G3/G5/G7 |
| RNF-DAT-001 | CU-TRA-03/04/05 | Parcial | I2/G6 |
| RNF-PRV-001 | CU-ADM-01, CU-ASI-03, CU-TRA-07 | Parcial | U3 |
| RNF-PDF-001 | — | Ausente | G9 |

Resultado conservador por criterios mínimos: 2 contradictoria, 31 parcial, 24 ausente.
No se acredita cobertura completa de los 57 requisitos: mencionar un módulo o un saldo no demuestra sus reglas ni aceptación.

RF-COS-001 y RNF-OPS-001 permanecen fuera del denominador: están proposed. Los 12 IDs
superseded tampoco se cuentan como requisitos activos. Los 15 casos complementarios de la
propuesta documentan cómo cerrar brechas, pero no se cuentan como cobertura del PDF original.

## Alineación constitucional y acciones

- Principio I y control humano: C1 impide implementar la parte offline sin reconciliar reglas
  opuestas; la exigencia actual se registra y se modela, sin inventar validaciones de campo.
- Principios III/IV: auditoría, autorización, atomicidad e idempotencia deben expresarse en
  criterios de las operaciones; la ausencia en el PDF no prueba que exista una implementación defectuosa.
- Principio V: preservar formularios móviles/táctiles; completar medidas de accesibilidad y
  escenarios de error. Una factibilidad favorable no sustituye validación con usuarias.
- Principio VI: los nuevos documentos enlazan fuentes, casos, hallazgos, esquemas y evidencia.
  No se declara cerrada la matriz global ni un sprint de implementación.

Orden propuesto: reconciliar alcance offline → ajustar acceso → precisar asistencia/encargos
→ completar producción/comercial → reportes y publicación → validar diagramas y fichas.
Para la ejecución futura de SPEC-001, corregir manualmente S1–S4 o usar `speckit-tasks` con
el diff revisado; después repetir `speckit-analyze`. Para PWA, preparar una spec específica
con `speckit-specify`, aclarar reloj/permisos/conflictos con `speckit-clarify` y planificar con
`speckit-plan`. No ejecutar `speckit-implement` como resultado de esta revisión documental.

Las modificaciones concretas están propuestas en las fichas; no se aplicaron al PDF, al
catálogo canónico ni a spec/plan/tasks. La siguiente iteración puede tomar C1–C3 y U3 como
primer bloque de corrección verificable.

## Validación de esta entrega

Tras incorporar F10 se verificaron 111 enlaces locales de los seis Markdown, incluidos 38 destinos a
encabezados; los 36 IDs de casos coinciden entre fichas/inventario, SVG y PlantUML. Se
inspeccionaron visualmente las siete vistas renderizadas y se corrigieron márgenes/espaciado.
La tabla de producto contiene exactamente 57 IDs confirmed. Estas comprobaciones verifican
la integridad documental, no funcionalidad de una aplicación.

El validador universal terminó `ok: true`, sin errores y con cuatro advertencias heredadas.
La revisión de espacios en archivos de esta tarea pasó; `git diff --check` global señala
espacios finales en `design/style-guide/tokens.html:19` y `:75`, ajeno a esta entrega.
El checkpoint enlazado conserva los comandos, resultados, limitaciones y próximo paso.

## Seguimiento posterior — auditoría integral

[[2026-09-28-coherencia-integral|AUD-COH-001]] registra el estado posterior a este análisis:
S1–S4 están corregidos documentalmente en tasks.md (37 tareas pendientes); no son pruebas
funcionales pasadas. El catálogo se contrasta requisito por requisito y la
[[../../requirements/proposals/2026-09-28-catalogo-v1-1|revisión v1.1]] concreta los cambios offline.
Las cifras de 36 tareas y la cobertura del PDF en este informe describen el corte anterior.
