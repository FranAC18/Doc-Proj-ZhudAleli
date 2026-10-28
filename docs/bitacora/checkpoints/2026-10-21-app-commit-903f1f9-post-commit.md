---
title: "Commit inicial de App-zhudaleli — post_commit"
type: checkpoint
status: pushed
date: 2026-10-21
task_id: SB-S2-02
phase: post_commit
repository: App-zhudaleli
app_root: "app/"
remote: "https://github.com/FranAC18/App-zhudaleli.git"
branch: feature/RF-ACC-001-base-proyecto
commit: 903f1f9a55777992468ad88575d1f58463318516
pull_request: none
tag: none
push: completed
---

# Commit inicial de la aplicación — evidencia post_commit

El tesista solicitó crear un commit con el contenido presente en el repositorio de la
aplicación. Se confirmó la raíz `app/`, el remoto de App-zhudaleli, la rama de trabajo y el
índice antes de confirmar los cambios. El repositorio no tenía commits previos; este es su
commit inicial. Incluye la base Django/PWA y el avance de acceso de `RF-ACC-001` en Sprint 2.
La referencia del requisito y sprint queda en el asunto; este checkpoint conserva el alcance
detallado. No declara HU-ACC-001 terminada.

## Resultado Git

| Campo | Resultado |
|---|---|
| Hash | `903f1f9a55777992468ad88575d1f58463318516` |
| Mensaje | `feat(accounts): commit inicial [RF-ACC-001][SPRINT-2]` |
| Rama | `feature/RF-ACC-001-base-proyecto` |
| Archivos | 62 añadidos; inventario completo abajo. |
| Estado posterior | Árbol limpio y rama alineada con `origin`. |
| Push | `origin/feature/RF-ACC-001-base-proyecto`; el hash publicado coincide con el local. |
| PR / tag | No creados. |

## Verificaciones y límites

- Antes del commit, `git diff --cached --check` no reportó errores de espacios.
- Antes del push se verificaron ruta, raíz Git, remoto, URL de push, rama y archivos del
  commit. El push normal creó la rama remota sin force push; `git ls-remote` confirmó el
  hash `903f1f9a55777992468ad88575d1f58463318516` en esa referencia.
- La búsqueda de secretos no detectó credenciales reales en los archivos incluidos. `.env`,
  `.venv`, cachés y `docs/` permanecen ignorados; `.env.example` contiene marcadores de
  sustitución.
- El estado operativo existente registra que, tras implementar el control de intentos,
  pasaron `manage.py check`, `makemigrations --check --dry-run`, Ruff y formato. Esos
  comandos no se volvieron a ejecutar durante esta operación de commit.
- Las pruebas funcionales de login, sesión, contraseña y bloqueo, así como la comprobación
  de PWA en navegador, siguen pendientes según el estado activo. No se afirma que HU-ACC-001
  esté completa.

## Archivos incluidos

```text
.env.example
.github/workflows/ci.yml
.gitignore
README.md
apps/__init__.py
apps/accounts/__init__.py
apps/accounts/admin.py
apps/accounts/apps.py
apps/accounts/forms.py
apps/accounts/management/__init__.py
apps/accounts/management/commands/__init__.py
apps/accounts/management/commands/create_initial_account.py
apps/accounts/migrations/0001_initial.py
apps/accounts/migrations/0002_loginthrottle.py
apps/accounts/migrations/__init__.py
apps/accounts/models.py
apps/accounts/services.py
apps/accounts/templates/accounts/dashboard.html
apps/accounts/templates/accounts/login.html
apps/accounts/templates/accounts/password_change_form.html
apps/accounts/tests/__init__.py
apps/accounts/tests/test_management_command.py
apps/accounts/tests/test_models.py
apps/accounts/urls.py
apps/accounts/views.py
config/__init__.py
config/asgi.py
config/pwa.py
config/settings/__init__.py
config/settings/base.py
config/settings/development.py
config/settings/production.py
config/settings/test.py
config/urls.py
config/wsgi.py
manage.py
pyproject.toml
static/brand/favicon-32.png
static/brand/zhud-aleli-emblem-white.png
static/brand/zhud-aleli-emblem.png
static/brand/zhud-aleli-wordmark-white.png
static/brand/zhud-aleli-wordmark.png
static/css/zhud-aleli.css
static/img/login-botanical.svg
static/js/form-feedback.js
static/js/password-toggle.js
static/js/pwa-register.js
static/manifest.json
static/pwa/icons/apple-touch-icon.png
static/pwa/icons/icon-192.png
static/pwa/icons/icon-512.png
static/pwa/offline.html
static/pwa/service-worker.js
static/vendor/bootstrap/LICENSE
static/vendor/bootstrap/bootstrap.bundle.min.js
static/vendor/bootstrap/bootstrap.min.css
templates/base.html
templates/components/messages.html
templates/public_status.html
tests/__init__.py
tests/test_pwa.py
uv.lock
```

## Próximo paso

Continuar `SB-S2-02`: completar las pruebas funcionales y de seguridad pendientes y revisar
en navegador el comportamiento PWA. Integrar a `main` mediante PR cuando corresponda.
