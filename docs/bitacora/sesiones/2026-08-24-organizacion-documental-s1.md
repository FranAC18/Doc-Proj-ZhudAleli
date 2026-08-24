---
title: Organización documental y alcance de Sprint 1
type: session
status: completed
date: 2026-08-24
sprint: S1
module: transversal
related:
  - "[[../../00-inicio/00-dashboard]]"
  - "[[../../../specs/001-acceso-usuarias-internas/tasks]]"
  - "[[../../architecture/REPRODUCIBILIDAD-ENTORNO]]"
tags:
  - proyecto/tesis
  - tipo/sesion
  - sprint/s1
  - modulo/transversal
---

# Organización documental y alcance de Sprint 1

## Objetivo

Dejar explícitos el vault documental, el agente de requisitos, el alcance de Sprint 1 y las
condiciones iniciales de reproducibilidad del entorno.

## Confirmaciones del tesista

- Los nombres de usuario se limitarán a una forma sencilla y controlada para evitar diferencias
  entre la normalización de Python y PostgreSQL.
- PostgreSQL ya está instalado; el servicio local está activo.
- Sprint 1 implementará únicamente `accounts` y acceso.
- La documentación y los artefactos deben permanecer organizados dentro del vault raíz.
- Se autoriza crear el commit de documentación de esta sesión y revisar después la ramificación.

## Trabajo realizado

- Corregida la propiedad duplicada de `design/style-guide/index.html` entre T001 y T004.
- Ajustadas las dependencias y la descripción de paralelismo de `tasks.md`.
- Marcado el modelo de módulos futuros como conceptual y `proposed`, sin bloquear S1.
- Añadidas tareas y criterios para CI, PostgreSQL, accesibilidad, conectividad y evidencia UX.
- Corregidas las rutas de lectura obligatoria del contrato `AGENTS.md`.
- Documentadas las ubicaciones canónicas de Obsidian y el comportamiento read-only del agente
  `requirements`.
- Creada la guía de reproducibilidad del entorno.

## Verificación del entorno

- Python 3.12.2 disponible.
- uv 0.10.9 disponible.
- PostgreSQL 18.4 disponible.
- Servicio `postgresql-x64-18` en ejecución.
- `localhost:5432` acepta conexiones mediante `pg_isready`.
- La aplicación Django aún no existe; no se ejecutan todavía comprobaciones Django.

## Próximo paso permitido

Revisar el commit documental y la rama; después iniciar T013–T015 para crear el entorno raíz
reproducible de Django, sin implementar módulos futuros.
