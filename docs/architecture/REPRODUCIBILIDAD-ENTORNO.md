---
title: Reproducibilidad del entorno de desarrollo
type: architecture
status: proposed
date: 2026-08-24
sprint: S1
module: transversal
related:
  - "[[../../specs/001-acceso-usuarias-internas/plan]]"
  - "[[../../specs/001-acceso-usuarias-internas/tasks]]"
  - "[[../00-inicio/GIT-Y-GITHUB]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - sprint/s1
  - modulo/transversal
---

# Reproducibilidad del entorno de desarrollo

## Propósito

La aplicación debe poder instalarse y verificarse en otra máquina sin depender de paquetes
instalados manualmente en el entorno global ni de rutas privadas del equipo del tesista.

## Estado actual

- Python 3.12.2 y `uv` 0.10.9 están disponibles en el equipo actual.
- PostgreSQL 18 está instalado y el servicio `postgresql-x64-18` está activo.
- `psql` y `pg_isready` no están todavía disponibles directamente en `PATH`, aunque existen
  dentro de la instalación de PostgreSQL.
- La aplicación Django aún no tiene `pyproject.toml`, `uv.lock` ni base de datos propia.
- `tools/agent-lab/` conserva su propio `pyproject.toml` y bloqueo; no es el entorno de la
  aplicación Django.

## Regla de entorno

La aplicación tendrá un `pyproject.toml` y `uv.lock` en la raíz. Las dependencias de producción
y desarrollo se instalarán con `uv sync --locked`. El entorno virtual será local, estará
excluido por Git y no será una fuente de archivos del proyecto.

```powershell
uv sync --locked
uv run python manage.py check
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py test
```

No se versionan `.venv`, `.env`, bases locales, `media/`, `staticfiles/` ni credenciales.

## PostgreSQL

La ruta del cliente debe resolverse mediante documentación de instalación o configuración
del entorno; no se codifica una ruta absoluta del equipo actual en Django. La guía de instalación
debe indicar cómo crear un usuario y una base de desarrollo, además de una base temporal para
pruebas. Las migraciones y pruebas que dependan de restricciones PostgreSQL no se validan solo
con SQLite.

## Criterio de terminado

La reproducibilidad queda demostrada cuando una máquina limpia puede sincronizar el bloqueo,
cargar variables desde `.env.example`, conectarse a PostgreSQL y ejecutar las comprobaciones
del plan sin modificar manualmente el código.
