---
title: SB-S2-01 — base Django y PWA, comprobación previa a Git
type: checkpoint
status: in-progress
date: 2026-10-20
task_id: SB-S2-01
phase: pre_commit
repository: App-zhudaleli
branch: feature/RF-ACC-001-base-proyecto
commit: pending
---

# SB-S2-01 — evidencia previa a Git

La tarea técnica de [[../../sprints/SPRINT-02-HOJA-DE-RUTA|Sprint 2]] se ejecuta mientras
`SB-S1-01` continúa con el cotejo de fuentes. El tesista cerró administrativamente el
periodo de Sprint 1; ese cierre no acredita la culminación de `SB-S1-01` ni de las
historias de acceso. Esta nota registra archivos locales de la rama indicada, todavía
sin commit ni PR.

## Alcance preparado

- Proyecto Django 5.2 con Python 3.12, configuración por entorno, PostgreSQL, `uv.lock`,
  README técnico y CI previsto con PostgreSQL.
- `accounts.User(AbstractUser)` y `AUTH_USER_MODEL` definidos antes de la primera
  migración. La migración `apps/accounts/migrations/0001_initial.py` contiene la
  restricción canónica de username de [[../../../specs/001-acceso-usuarias-internas/data-model|SPEC-001]].
- Comando interactivo de primera cuenta y pruebas aisladas de modelo y comando. No se
  creó una cuenta real y todavía no hay login ni logout de producto.
- Manifiesto, Service Worker, página pública sin conexión e iconos provisionales.
  Bootstrap 5.3.8 se incluye localmente con licencia MIT. El Service Worker solo
  precarga recursos públicos; no persiste páginas privadas ni formularios.

## Comprobaciones ejecutadas

| Comprobación | Resultado observado | Límite |
|---|---|---|
| `uv sync --locked` | Dependencias instaladas desde `uv.lock`. | Entorno local; CI aún no ejecutada. |
| `uv run ruff check .` y `uv run ruff format --check .` | Sin hallazgos; 27 archivos Python con formato correcto. | No sustituye pruebas funcionales. |
| `uv run python manage.py check --settings=config.settings.development` | Cero problemas. | No valida por sí solo los recorridos de acceso. |
| `uv run python manage.py makemigrations --check --dry-run --settings=config.settings.development` | Sin cambios de modelo detectados. | Ejecutado después de conectar PostgreSQL. |
| `uv run python manage.py migrate --noinput` | Aplicó correctamente las migraciones de `contenttypes`, `auth`, `accounts` y `sessions` en `zhud_aleli_dev`. | No crea una cuenta inicial real. |
| `uv run python manage.py test apps.accounts.tests --settings=config.settings.test` | Cinco pruebas aprobadas en una base PostgreSQL temporal; Django la creó y eliminó correctamente. | No incluye todavía el recorrido de login/logout, que corresponde a la siguiente porción. |
| `uv run python manage.py test tests.test_pwa --settings=config.settings.test` | Tres pruebas aprobadas sin base de datos. | No comprueba instalación ni corte de red en navegador. |
| Solicitudes HTTP locales a `/`, `/service-worker.js`, `/static/manifest.json`, hoja Bootstrap y `/static/pwa/offline.html` | Todas respondieron 200 mediante servidor WSGI temporal de desarrollo. | No se ejecutó el `runserver` estándar porque exige revisar migraciones en PostgreSQL. |

El servicio PostgreSQL 18 está activo en `localhost:5432`. `app/.env` contiene la
configuración local y está ignorado por Git; no se copió ningún secreto a la evidencia.
La primera conexión rechazó la contraseña configurada. Después se corrigieron las
credenciales locales y se asignó `zhud_aleli` como propietario de `zhud_aleli_dev`;
la migración y las pruebas de cuentas pasaron con esa configuración.

La apertura de `http://127.0.0.1:8765/` en el navegador de la herramienta fue rechazada
por su control automático de autorización para ese origen. No se intentó abrirlo por
otra superficie del navegador. La instalación PWA y el uso tras cortar la red quedan
pendientes de una comprobación autorizada.

## Estado y siguiente paso

La base técnica y `accounts.User` de `SB-S2-01` quedaron comprobados localmente: migración
aplicada y cinco pruebas de cuentas aprobadas en PostgreSQL. No se creó una cuenta real,
ni se implementó todavía el recorrido de login/logout. La base PWA está preparada, pero
la instalación y el corte de red siguen pendientes de una prueba en navegador autorizada.
La rama permanece sin commit ni PR.
