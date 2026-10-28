---
title: Hoja de ruta operativa del Sprint 2
type: sprint-roadmap
status: in-progress
date: 2026-10-20
updated: 2026-10-27
source: decisión del tesista y backlog vigente
---

# Sprint 2 — hoja de ruta operativa

**Actualización de alcance, 2026-10-27:** el tesista pidió incluir en S2 acceso,
cuentas, superadministración, estructura y permisos previstos, y desarrollar las
funciones de otros módulos en S3-S5. La
[[PLAN-HASTA-2026-12-23|hoja de ruta viva hasta diciembre]] contiene la propuesta
de fechas y capacidad. Las exclusiones y diferimientos descritos abajo registran
el alcance anterior de `SB-S2-02` y no vetan la nueva planificación. Ninguna operación
nueva de `RF-ACC-005` se declara aprobada o implementada por este ajuste.

El tesista cerró el periodo del sprint 1 y decidió comenzar el sprint 2 por `SB-S1-01`, pendiente trasladada. El cierre no declara completadas las tareas arrastradas. En el calendario actual, `SPEC-001` se ejecuta en S2 aunque sus artefactos conservan la etiqueta histórica `S1`.

## Ampliación de acceso aceptada — 2026-10-28

El tesista aceptó correo por código, passkeys y WhatsApp configurable para S2, con recuperación y seguridad común. SPEC-003 y RF-ACC-006 a 009 gobiernan este incremento; SB-S2-05 a 09 descomponen las cinco fases. La activación real de WhatsApp depende de proveedor, plantilla, consentimiento, costo y prueba de entrega. El ingreso necesita conexión y el registro WebAuthn se verifica en dispositivos con HTTPS. Las exclusiones históricas de recuperación y los mensajes diferenciados de SB-S2-02 no vetan el alcance nuevo aceptado; la implementación actual se adaptará con regresión.

Se conserva el avance anterior y el cierre propuesto de S2; no se inventan nuevas fechas, estimaciones ni terminaciones. El backlog v1.5 registra las tareas pendientes. Cada cambio relevante sincroniza requisitos, historias, pila, backlog y gestor local.

## Orden de trabajo

| Orden | Porción | Resultado comprobable | Límite |
|---:|---|---|---|
| 1 | `SB-S1-01` / `HT-PRE-001` | Cotejo de fuentes con actor, fecha, necesidad, duda y requisito del catálogo; diferencias y evidencia ausente identificadas. | No reabrir S1 ni atribuir validación organizacional directa sin acta o fuente primaria. |
| 2 | `SB-S2-01` / `HT-GEN-001/009` / base PWA | Proyecto Django reproducible, `accounts.User` antes de la primera migración, PostgreSQL comprobado, prueba acotada de cuenta activa/inactiva, README y base PWA pública. | La preparación local está hecha; la instalación y modo sin conexión de PWA aún requieren comprobación en navegador. |
| 3 | `SB-S2-02` / `RF-ACC-001` | Completar el acceso básico: login, logout, protección del espacio privado, cambio de contraseña y dashboard mínimo, con los criterios CA-ACC-001-01 a 13. | No incluye administrar membresías, definir permisos de otros módulos ni mostrar actividades/encargos aún no implementados. |
| 4 | `SB-S2-03` / `RF-ACC-002/003` | Refinar el alcance de membresías y responsabilidades descrito en `HU-ACC-002/003`, incluida la matriz de permisos P-01. | Diferido por decisión del tesista. Las HU existen en la pila v1.7 y las fichas v2.5; prioridad y sprint siguen propuestos, la revisión académica está pendiente y P-01 aún no define autorizaciones implementables. |
| 5 | `SB-S2-04` / `RF-ACC-004` | Mostrar actividades, pendientes y encargos propios. | Diferido por decisión del tesista hasta que existan planificación y asignaciones. No se confunde con el dashboard mínimo de bienvenida de `RF-ACC-001`. |

## Alcance acordado para continuar S2 — 2026-10-20

El tesista confirmó continuar con `SB-S2-02` después de preparar la base de `SB-S2-01`.
Por tanto, **el login sí forma parte del Sprint 2** y es la siguiente porción de código.
La base de `SB-S2-01` y el modelo de cuenta funcionan localmente; esa porción no se
presenta como cerrada mientras siga pendiente la comprobación en navegador de la
instalación y funcionamiento sin red de la PWA. Se comprobará cuando existan rutas
privadas, para verificar que no se almacenan páginas ni formularios de autenticación.

### Contenido concreto de `SB-S2-02`

- Permitir login solo a cuentas activas. Según CA-ACC-001-02/03 de SPEC-001, mostrar
  «Contraseña incorrecta.» para una cuenta activa con contraseña errónea y «Usuario
  incorrecto.» para un identificador inexistente o una cuenta inactiva.
- Proteger páginas privadas ante accesos directos sin sesión; cerrar sesión por `POST`
  con CSRF e impedir reutilizar la sesión cerrada.
- Completar el recorrido de `RF-ACC-001`: cambio voluntario y obligatorio de contraseña,
  dashboard de bienvenida sin opciones simuladas y vencimiento tras 30 minutos de
  inactividad.
- Aplicar interfaz móvil y accesible a las pantallas del recorrido. No agregar
  administración de cuentas, actividades, pendientes ni encargos.
- Verificar la política PWA después de crear páginas privadas: los recursos públicos
  pueden estar disponibles sin conexión, pero la autenticación y el contenido privado
  no se cachean.

`SB-S2-03` y `SB-S2-04` permanecen en la pila, pero salen del trabajo inmediato de S2.
La página privada mínima de `SB-S2-02` muestra únicamente bienvenida, cambio de contraseña
y cierre de sesión; no completa `HU-ACC-004`.

### Alineación de criterios — 2026-10-23

La spec confirmada contiene CA-ACC-001-01 a CA-ACC-001-13; esa numeración prevalece sobre
la referencia anterior a CA-01–11 de esta hoja. La respuesta diferenciada de CA-02/03 es la
vigente para `SB-S2-02`. `PRO-SEC-001` permanece `proposed`: su recomendación de usar un
mensaje común para todos los fallos y su propuesta de limitar por origen no cambian la spec.
Si se desea adoptar alguna, primero se debe validar y actualizar el requisito afectado.

El panel administrativo general no forma parte de Sprint 2 ni tiene sprint asignado. El
análisis del panel no amplía `SB-S2-02`; las acciones sobre cuentas, membresías y permisos
requieren completar el alcance futuro de `RF-ACC-002/003`, mientras que las configuraciones
de otros dominios deben permanecer en sus módulos propietarios.

Las porciones 2 y 3 integran la primera base ejecutable del producto. Las decisiones P-03/P-04/P-05/P-13/P-14 se resolverán cuando una historia necesite sus datos; no detienen las porciones independientes de este sprint.

## Correcciones al prompt recibido para `SB-S2-01`

1. **Orden:** `SB-S2-01` no es el primer trabajo activo; va después de `SB-S1-01`, por decisión expresa del tesista.
2. **Fuentes:** consultar selectivamente el requisito, sprint, spec y secciones técnicas pertinentes. La constitución vigente es 2.0.0; ADR-0006 conserva el monolito modular. La arquitectura v1.1 y las ediciones académicas son referencias para discrepancias, no lecturas obligatorias completas antes de cada archivo.
3. **Configuración:** el plan aprobado de `SPEC-001` exige `base.py`, `development.py`, `test.py` y `production.py`, además de `.env.example` sin secretos. Python 3.12 y Django 5.2 LTS son la base técnica elegida en ese plan; PostgreSQL es el motor de integración.
4. **Primera cuenta:** usar el comando interactivo controlado de `SPEC-001`, sin contraseña en argumento, variable, archivo ni fixture. Las pruebas pueden crear cuentas ficticias aisladas; no se versiona una cuenta inicial real ni una fixture con credenciales.
5. **PWA:** la base PWA forma parte del primer incremento de código por decisión del tesista. Se implementa como porción transversal cercana a `SB-S2-01`, sin ampliar el alcance de autenticación de `SPEC-001` ni activar operaciones offline futuras.
6. **Repositorios:** código, migraciones, pruebas y README técnico breve van solo en `App-zhudaleli`; hoja de ruta, evidencias y matriz de trazabilidad quedan en el repo general. Se actualiza la matriz existente cuando haya prueba y resultado reales; no se crea una matriz paralela en la app.
7. **Git:** la futura rama de app sigue `feature/RF-ACC-001-...`; los commits, cuando el tesista los solicite expresamente, siguen `tipo(scope): descripción [RF-ACC-001][SPRINT-2]`. El formato `SB-S2-01: ...` y un `push` automático contradicen las reglas vigentes.
8. **Flujo:** el diagnóstico y la preparación no necesitan una aprobación adicional para empezar; se respetan los límites de la tarea. No se editan ADR, constitución ni SPEC aprobados para acomodar el código.

## Preparación exacta de la porción `SB-S2-01`

- **App:** `pyproject.toml`, `uv.lock`, `.env.example`, `manage.py`, `config/{__init__,urls,asgi,wsgi}.py`, `config/settings/{__init__,base,development,test,production}.py`, `apps/__init__.py`, `apps/accounts/{__init__,apps,admin,models}.py`, `apps/accounts/migrations/{__init__,0001_initial}.py`, `apps/accounts/management/commands/create_initial_account.py`, pruebas en `apps/accounts/tests/`, CI y README técnico. Los archivos se crean solo al ejecutar su subporción.
- **PWA base:** `static/manifest.json`, `static/pwa/service-worker.js`, `static/pwa/offline.html` y `static/js/pwa-register.js`, con alcance del Service Worker y política de caché definidos sin datos privados.
- **General:** registrar evidencia y, al existir pruebas reales, actualizar `docs/traceability/MATRIZ-TRAZABILIDAD.md` con RF, HU, HT, criterio, prueba y resultado. No anotar migración ni prueba aprobada antes de ejecutarla.
- **Riesgos:** repositorio de app aún sin commit inicial; `app/.gitignore` ignora `/docs/`; PostgreSQL local debe comprobarse con una conexión real; el remoto y la protección de `main` se verifican antes de cualquier publicación autorizada.

## Criterios de avance

`SB-S1-01` avanza con el cotejo documental de las doce necesidades disponibles, pero una fuente primaria ausente queda declarada como tal. `SB-S2-01` se evalúa con comprobación Django, migración desde PostgreSQL vacío, comprobación de migraciones pendientes y prueba de cuenta activa/inactiva en PostgreSQL. La base PWA se evalúa con y sin red, sin caché privado. Cada resultado se informa con el comando y salida reales; ningún criterio se marca cumplido por figurar en esta hoja.
