---
title: Frontend de cuentas agrupado por pantalla
type: checkpoint
status: verified-local
date: 2026-10-28
author: Codex
task_id: SB-S2-02
requirement: RF-ACC-001
phase: pre_commit
commit: pending
repository: App-zhudaleli
branch: feature/RF-ACC-001-base-proyecto
head: 8f19c0ea14e9f3209ff2bdc2599ed70c0126f746
general_head_at_start: d0c47edc2b011be6c0ef76b3c9d6ddc563395bb5
general_head_verified: 6c09fc3d8fa5228249185ab7e3e93d5a8c29104e
---

# Frontend agrupado por pantalla

El tesista solicitó implementar en la app la convención aprobada de organización
por módulo, backend nativo y frontend por pantalla. Se aplicó a las tres pantallas
existentes de `accounts`, sin ampliar requisitos de negocio.

## Cambios revisados

- Login, inicio y cambio de contraseña se ubican en
  `apps/accounts/frontend/accounts/<pantalla>/`.
- El HTML de cada pantalla está junto a `recursos/`, cuando necesita archivos
  propios. Login conserva su CSS e imágenes; inicio conserva su CSS. Se mantiene
  una sola fuente por archivo y se conservan sus nombres públicos y URLs.
- La única regla del antiguo CSS de cambio de contraseña, el margen del formulario
  de salida, se integró en `static/compartido/formularios.css`. No se crea un
  directorio de recursos vacío para esa pantalla.
- `TEMPLATES` añade la raíz `apps/accounts/frontend/`. `STATICFILES_DIRS` registra
  solo `recursos/` de login e inicio con los prefijos `accounts/login` y
  `accounts/inicio`. El árbol frontend completo no se publica.
- `config/estaticos.py` extiende `FileSystemFinder` y normaliza los separadores
  antes de delegar su búsqueda segura al buscador original. Fue necesario porque
  el buscador instalado concatena los prefijos con `os.sep`: en Windows no
  encontraba las URLs con `/`. La primera ejecución detectó seis fallos de
  resolución; la corrección se verificó con las mismas pruebas.
- La PWA pasa de v8 a v9 y retira de la precarga el CSS integrado en formularios.
- Se retiraron únicamente directorios antiguos confirmados vacíos: plantillas y
  estáticos del módulo, y `static/css`, `static/img`, `static/js` generales.
- README técnico actualizado con la estructura, configuración y pasos para añadir
  pantallas y módulos. No se crean apps, servicios ni capas futuras vacías.

Los archivos `models.py`, `forms.py`, `services.py`, `views.py`, `urls.py` y
`apps.py` de cuentas conservan hashes SHA-256 idénticos al inicio de esta tarea.
Se conservan las modificaciones locales previas al partir de su contenido real.
Las migraciones y las dependencias de producto no se modificaron.

## Verificación

- Línea base: 19 pruebas correctas antes de los traslados.
- `uv run python manage.py test --settings=config.settings.test --noinput`:
  22 pruebas correctas en PostgreSQL después de la adaptación.
- Las tres pruebas nuevas de `apps/accounts/tests/test_frontend.py` verifican
  el origen real de las plantillas, entrega de recursos en desarrollo y
  recopilación aislada para despliegue. Rechazan los HTML fuente como estáticos.
  Tras añadir dos rutas con `..`, se repitieron las tres y pasaron.
- `uv run python manage.py check --settings=config.settings.test`: sin incidencias.
- `uv run python manage.py makemigrations --check --dry-run --settings=config.settings.test`:
  sin cambios detectados.
- `ruff check .`, `ruff format --check .`, `node --check` del Service Worker y
  `git diff --check`: correctos.
- `findstatic` localiza los CSS bajo los nuevos directorios con los mismos nombres.
- `collectstatic` con destino temporal copia 24 archivos; no publica las plantillas
  del módulo. La alternativa pública `pwa/offline.html` sigue siendo estática.
- Chromium en Windows, a 360 y 1440 píxeles: las seis parejas de capturas antes y
  después son idénticas por SHA-256. Sin desbordamiento horizontal ni errores de
  recursos o JavaScript. Mostrar/ocultar contraseña y foco de errores funcionan.
- PWA: instala v9 y elimina la caché v8 preparada para la comprobación. Precarga
  19 recursos públicos; al navegar sin red muestra «Sin conexión». Las páginas
  HTML de login e inicio no entran en la caché.

Informe de navegador: [[../../evidence/frontend/2026-10-28-colocalizacion/verificacion.json]].
Las capturas se generaron sobre HTML renderizado con una usuaria ficticia sin
persistencia, servido desde carpetas temporales. La comprobación del recorrido
autenticado se apoya en las pruebas Django; no se declara aceptación del navegador
con sesión real ni verificación de despliegue o ejecución Linux.

## Continuidad

La organización objetivo está aplicada al frontend actual de `accounts`. Continúa
SB-S2-02 con sus verificaciones funcionales pendientes, sin marcar el sprint ni
la historia completos. No hubo commit, push ni publicación. Los directorios
compartidos conservan su propietario y no se duplican en las pantallas.

Durante la tarea el repositorio general avanzó por otro trabajo documental al
commit `6c09fc3d8fa5228249185ab7e3e93d5a8c29104e`. Ese commit solo afecta la
edición de arquitectura para el docente, su índice y su control de cambios;
se conservan sin modificación. El HEAD de producto permaneció estable.

La primera limpieza mediante enumeración de directorios fue bloqueada por la
política de ejecución. Se completó con rutas absolutas explícitas, verificadas
vacías, sin eliminación recursiva.
