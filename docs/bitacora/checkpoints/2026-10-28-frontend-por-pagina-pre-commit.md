---
title: Organización del frontend por módulo y página
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
---

# Frontend por módulo y página

El tesista solicitó analizar la organización y después autorizó implementar la
propuesta por módulo y página. Se conserva el comportamiento vigente de acceso;
esta reorganización no incorpora requisitos ni declara terminado SB-S2-02.

## Resultado revisado

- Plantillas de `accounts` agrupadas en `login/`, `inicio/` y `cambio_contrasena/`.
  Se conservan los nombres de archivo y los nombres públicos de rutas y vistas.
- Recursos exclusivos en `apps/accounts/static/accounts/<pagina>/`; imágenes
  activas y alternativas del login junto a su CSS.
- CSS compartido separado en `static/compartido/base.css` y `formularios.css`.
  El CSS de inicio y el margen de salida de cambio de contraseña tienen su dueño.
- Los bloques `estilos_pagina` y `scripts_pagina` de `base.html` permiten cargar
  cada recurso donde se utiliza. Los scripts de contraseñas y errores se comparten
  sin duplicarlos; su contenido se conserva idéntico.
- Registro PWA en `static/pwa/pwa-register.js`. La caché pasa de la versión local
  v7 a v8 y actualiza las rutas; solo precarga la imagen de login utilizada.
  Las otras dos imágenes se conservan como archivos fuente.
- README técnico actualizado. Dos pruebas de regresión verifican la composición
  de páginas y el descubrimiento de todos los recursos precargados por la PWA.

Los cambios locales previos del login, CSS, imágenes y Service Worker se tomaron
como punto de partida. Las tres imágenes y los tres scripts movidos conservan
sus hashes SHA-256 respecto de ese estado previo.

## Verificaciones realizadas

- Línea base: 17 pruebas PostgreSQL correctas antes de modificar archivos.
- Resultado: `uv run python manage.py test --settings=config.settings.test --noinput`:
  19 pruebas correctas en PostgreSQL.
- `uv run python manage.py check --settings=config.settings.test`: sin incidencias.
- `uv run ruff check .` y `uv run ruff format --check .`: correctos.
- `node --check` de los cuatro JavaScript propios: correcto.
- `findstatic`: localiza CSS compartido, CSS de las tres pantallas y la imagen activa.
- `collectstatic` con destino temporal fuera de Git: copia 25 recursos, incluidos
  los recursos del módulo, sin modificar la configuración permanente.
- Chromium mediante Playwright: login, inicio y cambio de contraseña a 360 y
  1440 píxeles; las seis capturas PNG antes/después son idénticas por SHA-256.
  También coinciden geometría y estilos calculados de los elementos de cada
  contenido principal; no hay desbordamiento horizontal ni errores de recursos o JS.
- Navegador: mostrar/ocultar contraseña actualiza tipo de campo y `aria-pressed`;
  un resumen de errores de login recibe el foco.
- PWA en servidor temporal local: instala el Service Worker v8, precarga 20
  recursos públicos y muestra la alternativa pública «Sin conexión» al navegar
  sin red. La caché no contiene las páginas HTML de acceso ni páginas privadas.
- Revisión de diff y `git diff --check`: sin errores de espacios.

Las comprobaciones de navegador usan HTML renderizado por Django con una usuaria
ficticia sin persistencia, servido desde carpetas temporales. No sustituyen una
aceptación del recorrido autenticado completo ni un despliegue real; el recorrido
de negocio se verificó con las pruebas Django. Las herramientas de navegador no
se añadieron a las dependencias del producto.

## Pendientes y próximo paso

Revisar con el tesista la organización y continuar las comprobaciones pendientes
de SB-S2-02 indicadas en [[../ESTADO-ACTIVO]]. No hubo commit, push ni publicación.
Los archivos nuevos y las reubicaciones siguen sin preparar en Git.
