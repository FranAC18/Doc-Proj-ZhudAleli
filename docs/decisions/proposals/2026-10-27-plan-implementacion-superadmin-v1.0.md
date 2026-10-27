---
title: "Plan propuesto: Superpanel administrativo por módulos"
type: implementation-plan
status: proposed
date: 2026-10-27
version: 1.0
spec: "../../../specs/002-superadministracion/spec.md"
branch: "No creada; el nombre de rama es solo candidato"
write_owner: "Tesista decide alcance y ejecución"
requirement: "RF-ACC-005 candidato; código pendiente de confirmación"
sprint: "Sin asignación"
related:
  - "../../requirements/proposals/2026-10-27-CAT-REQ-001-v1.3-superadmin.md"
  - "../../requirements/proposals/2026-10-27-historias-usuario-v2.6-superadmin.md"
  - "../../requirements/proposals/2026-10-27-pila-producto-v1.8-superadmin.md"
  - "../../../specs/002-superadministracion/checklists/requirements.md"
---

# Plan propuesto: Superpanel administrativo por módulos

## Resumen

Se propone un panel unificado para administrar cuentas y accesos por módulo, conceder
autoridad delimitada, consultar el estado reciente de intentos de acceso y utilizar las
operaciones administrativas que cada módulo propietario exponga. El panel podrá facilitar
consultas y correcciones autorizadas dentro de flujos propios de cada módulo, pero no
concederá a una persona una facultad universal para leer o cambiar todos los datos. Las
correcciones conservarán el evento original y la auditoría.

El alcance nace de una solicitud que el tesista atribuye a la presidenta; la validación
directa de la presidenta está pendiente. La precisión vigente del tesista es que el
superpanel debe existir sin que el Superadministrador pueda cambiar cualquier dato. Por
tanto, `RF-ACC-005`, SPEC-002, las historias y este plan se conservan como propuestas.

No se asigna sprint ni prioridad, no se altera la línea base S1–S6 ni el alcance activo de
`SB-S2-02` / `SB-S2-03`, y no se inicia programación en esta tarea. La puerta actual es
validar el alcance y las decisiones que afectan autoridad, privacidad, seguridad y reglas
de negocio.

## Contexto técnico (Technical Context)

- **Lenguaje/runtime**: Python 3.12.
- **Framework**: Django 5.2 LTS, plantillas renderizadas por servidor y Bootstrap 5.
- **Persistencia**: PostgreSQL y ORM Django; migraciones nativas.
- **Pruebas futuras**: pruebas Django de servicio/vista, integración por módulo, permisos
  positivos y negativos, transacciones, concurrencia, fórmulas permitidas/rechazadas,
  accesibilidad y recorrido visual. No se ejecutan pruebas de aplicación para preparar este
  documento.
- **Módulo propietario**: el acceso (`apps/accounts` en el repositorio de aplicación)
  conserva cuentas, política de login y asignaciones de acceso que se confirmen. Cada módulo
  de negocio conserva sus catálogos, cálculos, correcciones, validaciones, escrituras y
  migraciones. La estructura y el contrato de composición del panel quedan por diseñar.
- **Estado observado**: el repositorio de aplicación tiene HEAD
  `903f1f9a55777992468ad88575d1f58463318516` en `feature/RF-ACC-001-base-proyecto`, sin PR ni
  tag de integración. La app contiene `accounts`; no se debe asumir que módulos productivos,
  operaciones administrativas o el superpanel están implementados o integrados.
- **Escala y datos**: número de cuentas pendiente de estimar; se manejan credenciales,
  identidades, responsabilidades y datos organizacionales/financieros/personales de distinta
  sensibilidad. La consulta se clasifica por finalidad, recurso y campos autorizados.
- **Restricciones**: autorización en backend por operación y recurso; aplicación móvil y
  accesible; tolerancia a conectividad limitada; panel y datos privados no cacheados por PWA;
  sin escritura directa a DB, CRUD genérico, `is_staff`/`is_superuser` como permiso de negocio,
  contraseñas visibles, secretos editables ni auditoría reescribible.
- **Dudas técnicas**: la arquitectura aprobada en constitución 2.0.0 y ADR-0006 obliga a
  operaciones públicas, escritura propiedad del módulo, lecturas autorizadas y transacciones
  explícitas. El límite concreto del servicio de autorización, la composición de UI, la
  representación de delegaciones y la política append-only de auditoría requieren diseño
  después de validar requisitos; no se crea una app vacía ni una tabla universal de ajustes.

## Comprobación de la constitución (Constitution Check)

| Puerta | Evidencia en esta propuesta | Resultado |
|---|---|---|
| Requisito confirmado | `RF-ACC-005` sigue candidato y la validación directa de la presidenta no consta | `fail`; no iniciar alcance dependiente |
| Portabilidad | Markdown en el repo general; propuesta tecnológica estándar, dependiente de arquitectura aprobada | `pass` |
| Pruebas y permisos | SPEC-002 propone matriz actor→acción→recurso→resultado y pruebas permitidas/denegadas | `partial`; decisiones y pruebas quedan pendientes |
| Simplicidad e integridad | Panel coordinador; cada módulo es dueño de reglas y escrituras; no CRUD ni `core` universal | `pass` como límite propuesto |
| Cohesión y dependencias | Acceso dueño de asignación y política; módulos dueños de catálogos/cálculos/correcciones | `partial`; confirmar contratos por módulo |
| Entrega incremental | Secuencia técnica recomendada sin sprint, fecha ni prioridad asignados | `partial`; tesista decide un sprint posterior |
| UX/accesibilidad | Móvil, teclado, foco, estados y prueba con usuarias señalados | `partial`; falta validación de recorridos |
| Trazabilidad | Catálogo/HU/SPEC/plan enlazados; la evidencia de validación organizacional falta | `partial` |
| Control humano/privacidad | El alcance amplio y los datos personales están explícitamente pendientes | `partial`; definir propósito, campos y retención |
| Raíz y remoto de código | Docs en `ZhudAleli`; cualquier código futuro solo en la raíz Git de app | `pass` como regla; no hay cambio de código |

La propuesta de plan no aprueba el requisito. El resultado `fail` para la puerta de requisito
significa que no se debe implementar esta funcionalidad hasta que exista una fuente validada,
decisiones materiales suficientes y una asignación futura; no altera la autoridad del tesista
para cerrar o avanzar sprints según decida.

## Discrepancias y tratamiento propuesto

| ID | Fuente / hecho verificable | Solicitud reportada o diferencia | Tratamiento propuesto | Estado |
|---|---|---|---|---|
| D-SUP-01 | SPEC-001 confirma acceso propio de usuarias y excluye la administración de cuentas; los valores de login son 3 fallos en 3 minutos, bloqueo 3 minutos, inactividad 30 minutos. | El superpanel reportado incluye administración de otras cuentas y pide parámetros editables. | Mantener la funcionalidad en SPEC-002 separada. No cambiar SPEC-001 salvo revisión y validación propia antes de activar parámetros. | Pendiente de validación |
| D-SUP-02 | RF-ACC-002 cubre membresía; RF-ACC-003 cubre permisos por perfil/responsabilidad. HU-ACC-002/003 están en el material de S2, mientras `SB-S2-03` permanece diferida. | Solicitud reportada añade asignar módulos y autoridad administrativa. | Refinar historias como propuesta; no incorporar su trabajo al alcance activo ni moverlo a S2. | Registrada; plan/sprint sin cambios |
| D-SUP-03 | El tesista precisa que no desea una autoridad global que pueda cambiar cualquier dato. | La solicitud reportada pide autoridad administrativa global y revisar datos de cualquier módulo según un alcance que todavía debe validarse; no define la consulta por categorías ni las correcciones permitidas. | Interpretar «global» únicamente como panel central. Se excluye la edición universal; consultas y correcciones se delimitan por permiso, módulo, recurso y operación. La amplitud de lectura queda pendiente. | Propuesta para validación directa |
| D-SUP-04 | Constitución 2.0.0/ADR-0006 establece monolito modular, escrituras por propietario y operaciones públicas. | Un panel central podría sugerir escritura transversal genérica. | El panel llama operaciones administrativas explícitas; cada módulo valida, escribe y migra sus datos. Se prohíbe el acceso ORM/DB genérico. | Límite arquitectónico aprobado; API concreta pendiente |
| D-SUP-05 | `RNF-AUD-001` conserva una regla de auditoría; las operaciones con varias entidades usan transacción común. | Se solicita corregir datos desde la interfaz y registrar quién cambió campos. | Las correcciones pasan por servicios del módulo; movimientos y registros con historia se rectifican como eventos vinculados, nunca se sobrescribe su origen. | Límite de diseño propuesto; flujos por módulo pendientes |
| D-SUP-06 | La implementación local de `LoginThrottle` guarda huella HMAC y estado temporal, no eventos históricos legibles por cuenta. | Se pide revisar el número de intentos fallidos por cuenta. | Exponer solamente el estado/cuenta temporal que realmente se pueda resolver y autorizar; decidir aparte si se requiere historial, retención e identidad visible. | Pendiente de privacidad/datos |
| D-SUP-07 | Fórmulas productivas y comisión tienen reglas pendientes; los módulos propietarios aún no exponen en el alcance actual un administrador genérico. | Se pide editar fórmulas de pesaje y catálogos. | No inventar fórmulas; el módulo propietario define gramática restringida, validaciones, unidades, pruebas, aprobador y vigencia. Evitar código arbitrario y recálculo retroactivo. | Pendiente por módulo |
| D-SUP-08 | `is_staff` y `is_superuser` son flags técnicos Django; soporte técnico no es autoridad de negocio por defecto. | El nombre “superadmin” podría confundirse con privilegio de plataforma. | Definir rol organizacional propio; separar permisos técnicos de los organizacionales y denegar acceso de negocio al soporte salvo decisión expresa. | Regla de diseño recomendada |
| D-SUP-09 | La regla confirmada prohíbe inventar evidencia/aprobación y no se ha recibido validación directa de la presidenta. | La fuente original se atribuye a la presidenta por relato del tesista. | Etiquetar todo el alcance nuevo como solicitud reportada/propuesta hasta obtener decisión verificable. | Pendiente de validación |

## Fronteras y evolución modular

1. **Módulo de acceso**: administra cuentas, estados, permisos y la política de autenticación
   que se confirmen. Define operaciones explícitas como asignar/revocar módulo, activar/
   desactivar cuenta, delegar autoridad y modificar política validada. La operación vuelve a
   comprobar autoridad vigente y registra el actor.
2. **Módulos propietarios**: ofrecen operaciones administrativas para las configuraciones
   que la persona responsable del módulo permita. Cada operación valida el dominio, unidades,
   versión, impacto y permisos; no expone un `update any row` ni una bolsa genérica de
   clave/valor.
3. **Módulos con historia**: asistencia, pesajes, lotes, ventas, saldos y finanzas conservan
   eventos originales y cambios derivados. La corrección es un evento nuevo vinculado; su
   módulo decide transacción y efectos de reportes.
4. **Composición del panel**: una interfaz organizacional puede reunir accesos, estado de
   cuentas, configuración y resultados de servicios autorizados. El mecanismo de composición
   y consultas multi-módulo se especifica cuando el requisito y los primeros módulos se
   validen; no se crea un módulo de dominio `admin` que se apropie de escrituras ajenas.
5. **Auditoría**: el módulo que confirma la operación conserva la evidencia de cambio dentro
   de la transacción cuando aplique; si se comparte una interfaz de auditoría, esta no
   concede edición. El almacenamiento, retención y lecturas autorizadas se diseñan con ADR si
   la decisión cruza módulos.
6. **Aislamiento**: formularios, rutas, API internas, sincronización y comandos de gestión
   revalidan permiso en backend. No se obtiene autoridad por URL, botón visible, sesión
   antigua, `is_staff` o pertenencia al panel.
7. **Configuración de login**: la app `accounts` conserva el comportamiento de SPEC-001. Un
   campo de configuración no puede activar valores que esa spec no permite hasta revisar y
   validar su nueva versión.

### Catálogos y fórmulas

- El módulo propietario registra explícitamente qué parámetro es configurable, tipos,
  unidades, rangos, dependencias, validadores, responsable de aprobación y resultado visible.
- Una fórmula se expresa en una gramática restringida de operaciones y variables aprobadas.
  La propuesta prohíbe `eval`/ejecución de código, Python, SQL, plantillas, llamadas libres o
  acceso a red/archivos. El evaluador produce solo valores del dominio y no efectos laterales.
- Antes de activar una versión: revisar sintaxis, variables, unidad compatible, precisión,
  redondeo, límites, casos de prueba y ejemplo de resultado; la persona aprobadora aún debe
  ser elegida por la organización.
- Registrar versión, autor, motivo, fechas de vigencia y pruebas realizadas. No reescribir el
  cálculo histórico; una reconstrucción/corrección retroactiva sería una operación
  extraordinaria y requiere requisito propio, permiso, evidencia y decisión organizacional.
- Datos iniciales y fórmulas no se inventan. El panel no habilita valores de comisión,
  porcentaje, receta, merma o rendimiento sin su fuente validada.

## Diseño conceptual de autorización

Un permiso se evalúa para una combinación **actor + sesión vigente + operación + recurso +
módulo + contexto organizacional**, en cada solicitud al servidor. La decisión incluye:

1. cuenta activa y sesión válida;
2. concesión vigente de acceso al módulo;
3. autoridad para la operación solicitada;
4. permiso para el recurso/campo y finalidad;
5. reglas y estado del módulo propietario;
6. consistencia de cualquier aprobación/versión necesaria.

El panel no crea una excepción de “root” que salte la política. Conceder autoridad a una
persona no se deriva automáticamente de ser Superadministradora: el actor debe tener un
permiso específico de delegación, sujeto a identidad inicial, transferencia y doble
aprobación aún sin definir. Se deniega la autoelevación.

La verificación en backend ocurre antes de lectura y escritura. Si el permiso deja de estar
vigente, toda operación posterior debe denegarse cuando vuelva a verificarse; el tiempo de
propagación, las sesiones ya emitidas y la PWA deben quedar definidos antes de aprobar el
criterio de revocación.

## Diseño conceptual de datos

No es un esquema aprobado. Solo identifica conceptos que habrá que asignar al dueño correcto:

| Concepto | Propietario | Invariantes por definir |
|---|---|---|
| Estado de cuenta | Acceso | Desactivación, reactivación, acceso restante e impacto en operaciones relacionadas |
| Asignación de módulo | Acceso | Unicidad, quien concede/revoca, vigencia y permisos heredados |
| Delegación de autoridad | Acceso | Emisor, receptor, alcance, fechas, transferencia y aprobación múltiple |
| Política de intentos | Acceso | Rango y versión validados, aplicación coordinada y recuperación segura |
| Contador de intento reciente | Acceso | Identificador minimizado, ventana, visibilidad, retención, reset y protección contra bloqueo malicioso |
| Configuración/catálogo | Módulo dueño | Tipado, restricciones, estado y esquema de migración |
| Fórmula versionada | Módulo dueño | Expresión segura, unidades, precisión, vigencia, caso de prueba y vínculo de cálculo |
| Rectificación | Módulo dueño | Referencia al original, motivo, evidencia, autorización y cascada derivada |
| Evento de auditoría | Operación propietaria con mecanismo compartido solo si se decide | Escritura atómica, inmutabilidad de aplicación, acceso de lectura, retención y respaldo |

No se recomienda un modelo genérico que permita guardar y ejecutar configuraciones con tipo,
expresión y tabla de destino elegidas libremente. Las migraciones permanecen bajo el módulo
que posee el dato y el cambio de esquema.

## Interfaz

- Navegación con acceso visible únicamente a paneles autorizados. La visibilidad no es la
  única barrera de seguridad.
- Separar pestañas o recorridos para cuentas, módulos, políticas de acceso y configuraciones
  del módulo; las capacidades que no se habiliten no se muestran como activas.
- Antes de cambiar autoridad, cuenta o configuración, mostrar objetivo, alcance y vigencia,
  solicitar motivo y presentar resultado de forma legible.
- En corrección, presentar el valor previo, propuesta, razón y efecto antes de confirmar;
  nunca ofrecer borrar la auditoría o el evento base.
- Estados de vacío, carga, éxito, error de validación, denegación, revocación, conflicto de
  versión y sesión vencida deben ser distinguibles en texto y recuperar el flujo.
- Móvil, teclado y tecnologías de asistencia; probar con usuarias. No guardar páginas ni
  datos administrativos privados en caché PWA o IndexedDB sin requisito de continuidad,
  minimización y aislamiento aprobado.

## Estrategia de pruebas futura

No se ejecuta en esta tarea. Al implementarse, trazar criterio → prueba → evidencia:

- Autenticación, cuenta activa/inactiva, sesión caducada y permiso retirado antes de cada
  acción; probar rutas directas y fallos al servidor, no solo UI.
- Matriz positiva/negativa para actor, operación, recurso, módulo y dato personal; ningún
  permiso técnico Django sustituye permiso organizacional.
- Autoelevación, concesión por actor sin permiso, persona delegada, transferencia de cargo,
  cuentas concurrentes y doble aprobación cuando se determine.
- Desactivación/revocación concurrente con operaciones abiertas; verificar atomicidad y
  alcance de sesiones, reintentos y sincronización offline.
- Toda actualización multientidad aborta por completo si falla una validación; pruebas de
  integridad, concurrencia y migración.
- Fórmulas: gramática permitida, entradas y unidades inválidas, división por cero, valores
  extremos, precisión, redondeo, vista previa, vigencia futura, reversión de versión y
  preservación de cálculos históricos; entradas de código/SQL arbitrario nunca se evalúan.
- Correcciones: original inmutable, rectificación ligada, actor/motivo, repetición/idempotencia,
  efectos de reportes y transacción atómica.
- Intentos: límites inferior/superior, ventana, tiempo de bloqueo, reset, éxito de login,
  concurrencia, datos minimizados y abuso de bloqueo para denegar servicio.
- No-cache y ausencia de contenido privado en recursos PWA; navegación sin sesión; limpieza
  en cambio de cuenta únicamente si el recorrido PWA se valida.
- Interfaz móvil, teclado, lector de pantalla, contraste, foco, mensajes y recuperación ante
  error; evidencia con participantes autorizadas y datos anonimizados.

## Secuencia recomendada para implementación futura

Los incrementos siguientes son dependencias técnicas, **no sprints ni prioridad aprobados**.
Los puede cambiar el tesista cuando decida el alcance.

| Fase | Alcance técnico recomendado | Puerta para entrar |
|---|---|---|
| 0. Validación organizacional | Acordar actor real, límites de lectura/escritura, delegación, correcciones, privacidad y prioridad | RF-ACC-005 y SPEC-002 validados; decisiones materiales cerradas |
| 1. Contrato de permisos | Traducir matriz a permisos por operación/recurso; definir auditoría y política de sesión/revocación | Revisión de arquitectura/ADR si cruza módulos; permisos permitidos/denegados aprobados |
| 2. Cuentas y acceso modular | Activar/desactivar cuenta, asignar/revocar módulo, delegación con proceso aprobado | Identidad/autoridad inicial y transferencia resueltas; migraciones del módulo de acceso aprobadas |
| 3. Administración por módulo | Exponer uno por uno catálogos/configuración reales del propietario | Dueño, entradas, validadores, aprobador, historial y pruebas definidos por módulo |
| 4. Fórmulas seguras | Parser restringido, vista previa, pruebas, versiones/vigencia, preservar histórico | Fórmula de dominio validada; unidades, precisión, redondeo, entradas y responsable acordados |
| 5. Consultas y rectificaciones | Búsqueda y corrección por operación propietaria, limitada por categoría/campo y registro append-only | Política de datos/retención y regla de corrección aprobadas por cada módulo |
| 6. Política de login | Consultar estado reciente; permitir configuración después de revisar SPEC-001 | Rango, bloqueo, recuperación y sesión acordados; nueva versión de SPEC-001 validada |
| 7. Verificación y adopción | Regresión, seguridad, PWA, accesibilidad, piloto y guía de usuarias | Criterios, participantes, entorno y evidencia definidos; entrega del código se gestiona en el repo de app |

No se debe iniciar una fase posterior si su puerta depende de una decisión pendiente. El
tesista puede decidir una porción independiente y un sprint después de validar el requisito;
esta secuencia no predetermina la decisión.

## Entrega, documentación y repositorios

- Las fuentes de requisito, plan, decisiones y evidencia permanecen en el repositorio general.
- El código, las migraciones y pruebas futuras se editan solo desde la raíz Git del
  repositorio `app/`; no se copia esta spec ni el plan de proceso a la app.
- Cualquier cambio de código usa un requisito y sprint vigentes, una rama nombrada con ID
  real, verificación proporcional, revisión y PR; el plan documental no es autorización de
  commit de aplicación, push, publicación o despliegue.
- Antes de declarar integrado un incremento se verifica el estado de GitHub y se enlaza
  requisito → sprint → PR/tag en la matriz cuando corresponda. El código local actual no se
  presenta como una entrega de este superpanel.
- `documentacion/` solo recibe una edición académica revisada cuando el tesista la incorpore
  expresamente; estas fuentes permanecen como propuestas internas.

## Riesgos y reversión

| Riesgo | Probabilidad/impacto | Mitigación | Señal | Reversión |
|---|---|---|---|---|
| Autoridad demasiado amplia o autoelevación | Alta/Crítica | Permisos acotados a actor/acción/recurso, denegar self-grant, aprobación humana y pruebas negativas | Una acción fuera de matriz produce mutación | Revocar delegación y restaurar permisos anteriores con evento auditado; preservar registros |
| Corrección borra evidencia o altera finanzas/historia | Media/Crítica | Flujo del propietario, rectificación ligada, transacción, motivo y autorización adicional cuando se acuerde | Diferencia sin original o auditoría | Suspender acción, reconciliar desde originales/rectificaciones; no borrar eventos |
| Fórmula incorrecta altera cálculo o dato histórico | Media/Alta | Expresión segura, pruebas previas, versión/vigencia y sin retroactividad | Desviación en resultado de prueba o producción | Retirar la nueva versión para operaciones futuras; conservar historia y recalcular solo con decisión separada |
| Bloqueo de cuentas abusado para denegación de servicio | Media/Alta | Rango validado, límites conservadores, supervisión y proceso de recuperación decidido | Picos de cuentas bloqueadas | Volver a política anterior aprobada mediante versión y registro; no desbloquear sin identidad verificada |
| Permiso revocado sigue operando desde sesión o PWA | Media/Alta | Revalidar en cada solicitud; definir invalidación, caché y sincronización | Acción aceptada tras revocación | Revocar en backend, invalidar sesiones/colas según regla aprobada y revisar registros afectados |
| Administradora ve demasiados datos personales | Media/Alta | Permisos por categoría/campo/finalidad, minimización y auditoría de consulta si se valida | Búsqueda/exportación fuera de finalidad | Restringir acceso, retener evidencia con acceso controlado y revisar exposición |
| Módulo pierde invariantes por un administrador genérico | Media/Crítica | Operaciones públicas del dueño, validación local, migraciones propias y contrato | Escritura no pasa por dueño | Detener operación global y migrar a operación propietaria preservando transacción/historia |
| Se activa una fórmula/cambio de política no aprobado | Media/Alta | Estado de borrador, validador, actor aprobador y fecha de vigencia explícitos | Sin aprobación/evidencia | Mantener versión previa activa y registrar intento; no activar por defecto |

## Decisiones pendientes

1. Confirmar con la presidenta que la petición existe y cuál es su finalidad y alcance.
2. Delimitar por módulo y categoría qué datos se pueden consultar y qué correcciones
   puntuales se permiten; mantener excluida toda facultad universal de edición y listar los
   campos personales y restricciones de finalidad.
3. Definir quién autoriza la primera cuenta administrativa, quién delega/revoca y cómo se
   transfiere autoridad cuando cambia la presidencia; decidir si dos personas deben aprobar.
4. Definir política de revocación y sesiones activas, incluida la PWA.
5. Elegir si se necesita solo estado temporal de bloqueo o historial por usuaria; definir
   privacidad, finalidad, retención y quién podrá consultarlo.
6. Determinar rangos de intentos y bloqueo con la organización; validar si ventana de tres
   minutos se conserva; cualquier cambio requiere revisar SPEC-001.
7. Enumerar configuración que expone cada módulo y asignar aprobador, gramática/valores,
   unidades, precisión y vigencia a cada fórmula real.
8. Definir correcciones y aprobaciones para asistencia, pesajes, lotes, ventas, inventario,
   pagos, finanzas e informes derivados, solo cuando aplique.
9. Diseñar recuperación de cuentas por separado, con canal, identidad, expiración, uso único,
   revocación y auditoría.
10. Elegir prioridad frente al trabajo vigente sin cambiar S1–S6 de manera implícita.

## Evidencia y control de cambios

La propuesta conserva cuatro estados separados: hecho confirmado, solicitud reportada,
tratamiento propuesto y decisión pendiente. La aprobación del tesista de este paquete autoriza
preparar y guardar borradores; no convierte la narración de la presidenta en evidencia ni
confirma `RF-ACC-005`, SPEC-002 o sus historias.

| Versión | Fecha | Estado | Cambio |
|---|---|---|---|
| 1.0 | 2026-10-27 | `proposed` | Primera propuesta de alcance, arquitectura, fases y discrepancias. Pendiente de validación organizacional y decisión de sprint. |
