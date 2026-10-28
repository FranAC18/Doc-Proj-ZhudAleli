---
title: Separación de identidad e inicio privado
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
general_head: 6c09fc3d8fa5228249185ab7e3e93d5a8c29104e
---

# Identidad en accounts e inicio privado en portal

El tesista pidió implementar la separación propuesta después de revisar la seguridad
y los alcances de SPEC-001 y RF-ACC-004. La autorización corresponde a esta
separación técnica; no agrega operaciones ni declara construido el inicio operativo.

## Resultado revisado

- `apps.accounts` conserva usuario, autenticación, control de intentos, salida,
  contraseñas y sesiones. Modelos, formularios, servicio de autenticación y
  migraciones no se alteran.
- `apps.portal` posee la vista `VistaInicio`, su URL, sus pruebas, el HTML y el
  CSS de bienvenida. No tiene tablas, migraciones, servicios ni capas vacías.
- La página se traslada a `apps/portal/frontend/portal/inicio/dashboard.html`,
  con el CSS en `recursos/inicio.css`. Se retiran las carpetas anteriores vacías.
- `/acceso/`, `/inicio/`, `/salir/` y la URL de cambio de contraseña se conservan.
  `portal:inicio` sustituye al nombre interno `accounts:dashboard`; todos sus
  consumidores activos se actualizaron. No se mantiene un alias duplicado.
- `LOGIN_REDIRECT_URL` configura el destino de acceso y cambio de contraseña.
  Cuentas no importa vistas ni código Python del portal. La sesión es única.
- La vista trasladada conserva `LoginRequiredMixin`, la redirección por contraseña
  temporal y `never_cache`. Continúan vigentes el vencimiento, CSRF y el control
  de cuenta activa de Django.
- La PWA v10 sustituye el CSS anterior por `/static/portal/inicio/inicio.css`,
  precarga 19 recursos públicos y mantiene las páginas privadas fuera de caché.
- El README, la arquitectura, el contrato HTTP, una adenda al plan y el índice
  de funcionalidad registran la separación. Los criterios de la spec no cambian.

La existencia de dos apps no se presenta como una barrera de seguridad autónoma.
Las guardas siguen ejecutándose en backend. `portal` contiene la bienvenida
mínima actual; no se añadieron menús ficticios, actividades, encargos, reportes,
administración ni otras funciones pendientes de sus módulos.

## Verificación

- Línea base: 22 pruebas PostgreSQL correctas antes de modificar archivos.
- `uv run python manage.py test --settings=config.settings.test --noinput`:
  26 pruebas correctas. Las cuatro nuevas de portal verifican acceso permitido y
  denegado, propiedad de `/inicio/`, caché, origen único y publicación de recursos.
- Se conservan los recorridos de cuenta activa e inactiva, bloqueo temporal,
  contraseña inicial, vencimiento, salida con CSRF y `next` seguro.
- `manage.py check`: sin incidencias; `makemigrations --check --dry-run`: sin
  cambios detectados, ambos con `config.settings.test`.
- `ruff check .`, `ruff format --check .`, `node --check` del Service Worker y
  `git diff --check`: correctos.
- Pruebas de estáticos: CSS de portal encontrado y servido en desarrollo;
  `collectstatic` publica sus recursos y excluye su HTML. Ya no existen las
  fuentes ni el CSS anteriores bajo `accounts/inicio`.

### Navegador con sesión Django real de prueba

Se creó una base PostgreSQL aislada mediante `DiscoverRunner`, con cuentas
ficticias. Se sirvió Django por WSGI con su manejador de estáticos y se ejecutó
Chromium mediante Playwright. Al terminar se cerraron los servidores y se eliminó
la base de prueba. No se modificó la base de desarrollo ni se usaron datos reales.

- Login válido redirige a `/inicio/` y mantiene la sesión.
- Cambio de contraseña por formulario real redirige al portal y muestra su
  confirmación. Mostrar/ocultar contraseña funciona.
- Salir y volver a colocar la cookie anterior no permite abrir `/inicio/`.
- Una petición anónima al inicio vuelve al acceso; la contraseña temporal obliga
  al cambio, también mediante una URL directa al inicio.
- Login, inicio y cambio de contraseña a 360 y 1440 píxeles: las seis parejas de
  capturas, previas al traslado y posteriores sobre Django, son idénticas por
  SHA-256. Sin desbordamiento ni errores de recursos o JavaScript.
- El HTML sensible devuelve `Cache-Control` con `no-store`.
- La PWA instala v10, elimina la caché v9 preparada para la comprobación,
  precarga 19 recursos públicos y muestra la alternativa pública sin conexión
  al intentar navegar al inicio sin red.

Informe: [[../../evidence/frontend/2026-10-28-portal/verificacion.json]].
Estas pruebas con datos ficticios no equivalen a aceptación con usuarias de la
organización, despliegue real ni ejecución en Linux. El alcance no completa
RF-ACC-004 ni las operaciones administrativas candidatas.

## Continuidad

La separación está implementada localmente y SB-S2-02 continúa activo. No hubo
commit, push ni publicación. La edición académica para el docente conserva su
versión previa; su actualización y publicación se revisan por separado.
