---
title: Revisión del frontend y definición de modularidad Django
type: session
status: documented
date: 2026-10-28
author: Codex
task_id: SB-S2-02
requirement: RF-ACC-001
phase: pre_commit
commit: pending
repository: ZhudAleli
branch: docs/requisitos-y-organizacion-del-vault
head: d0c47edc2b011be6c0ef76b3c9d6ddc563395bb5
published_definition_commit: d0c47edc2b011be6c0ef76b3c9d6ddc563395bb5
app_branch: feature/RF-ACC-001-base-proyecto
app_head: 8f19c0ea14e9f3209ff2bdc2599ed70c0126f746
app_changes_commit: pending
---

# Revisión del frontend y definición de modularidad Django

## Objetivo y resultado

El tesista pidió una organización que permita encontrar y modificar cada pantalla sin
perderse entre archivos sueltos. Se revisó el frontend existente, se implementó una primera
reorganización y después se precisó una convención que reúne HTML y recursos bajo una
carpeta por pantalla. También se investigó el backend y se incorporaron las reglas aprobadas
a las instrucciones de generación de código por IA.

La definición técnica está publicada en el repositorio general. La app conserva la primera
reorganización local; la ubicación final `frontend/` todavía no está implementada.

## Trabajo realizado y alcance real

| Etapa | Resultado | Estado al documentar |
|---|---|---|
| Análisis inicial | Revisión de plantillas, CSS, JS, configuración y consumidores de recursos. | Realizado sin modificar archivos en esa etapa. |
| Primera implementación autorizada | Carpetas por página en plantillas y estáticos de `accounts`; CSS compartido separado; carga de recursos por pantalla; rutas y precarga PWA actualizadas. | Implementada y verificada localmente, sin commit de app. |
| Ajuste de criterio con el tesista | Preferencia por reunir HTML, CSS, JS e imágenes exclusivos bajo la misma carpeta de pantalla. | Convención técnica aprobada; transición pendiente. |
| Investigación de backend | Revisión de modelos, formularios, vistas, servicios, rutas y arquitectura interna; contraste con documentación oficial Django 5.2. | Realizada; backend sin refactorización adicional. |
| Reglas para IA | Actualización de skill, referencia obligatoria en `AGENTS.md`, adenda arquitectónica y registro de aprobación. | Incluidas en el commit documental publicado. |
| Commit y push solicitados | Publicación de la definición de modularidad en `ZhudAleli`. | Verificada en el remoto. |

La primera implementación conserva los HTML en
`apps/accounts/templates/accounts/<pantalla>/` y sus recursos propios en
`apps/accounts/static/accounts/<pantalla>/`. Los estilos y scripts comunes están en
`static/compartido/`; el registro PWA quedó en `static/pwa/`. Se conservaron las tres
imágenes fuente del login y el contenido de los tres scripts trasladados.

Se detectó que las carpetas anteriores `static/css/`, `static/img/` y `static/js/` quedaron
vacías. Se identificó además una fragmentación poco útil: el CSS de cambio de contraseña
contiene únicamente el margen del formulario de salida. Son asuntos a revisar al adaptar
el frontend; no se retiraron ni se fusionaron durante el análisis posterior.

El detalle de la implementación y sus límites está en
[[../checkpoints/2026-10-28-frontend-por-pagina-pre-commit]]. Ese checkpoint describe la primera
reorganización, anterior a la definición final; no acredita que esta última esté implementada.

## Convención aprobada y fuentes

El tesista aprobó expresamente las reglas y después solicitó su commit y push. La aprobación
se limita a la organización técnica y no modifica requisitos, permisos de negocio ni sprints.
Las fuentes vigentes son la [adenda de arquitectura](../../architecture/ARQUITECTURA-OBJETIVO.md)
y la [skill de código legible](../../../.agents/skills/zhud-aleli-codigo-legible/SKILL.md).

- El módulo de negocio posee datos, reglas, permisos, operaciones, presentación y pruebas.
- El backend conserva los mecanismos nativos de Django. Servicios, consultas y políticas
  separados aparecen cuando una responsabilidad real justifica su extracción.
- La ubicación objetivo de una pantalla es
  `apps/<modulo>/frontend/<modulo>/<pantalla>/`: HTML y directorio `recursos/` con sus CSS,
  JS e imágenes exclusivos. Solo se crean archivos y subcarpetas con contenido justificado.
- Los componentes generales conservan un único propietario compartido. Se mantiene el
  renderizado Django, Bootstrap, JavaScript progresivo y la entrega conjunta del monolito modular.
- Se configuran por separado las raíces de plantillas y los directorios públicos; no se
  publica `frontend/` completo. Cada transición conserva rutas, lógica, datos y autorizaciones
  y verifica descubrimiento de plantillas, estáticos y compatibilidad PWA.

La investigación se apoyó en las fuentes oficiales de
[aplicaciones autocontenidas](https://docs.djangoproject.com/en/5.2/intro/reusable-apps/),
[cohesión y dependencias](https://docs.djangoproject.com/en/5.2/misc/design-philosophies/),
[cargadores de plantillas](https://docs.djangoproject.com/en/5.2/ref/templates/api/#loader-types),
[directorios estáticos](https://docs.djangoproject.com/en/5.2/ref/settings/#staticfiles-dirs),
[organización de modelos](https://docs.djangoproject.com/en/5.2/topics/db/models/#organizing-models-in-a-package)
y [transacciones](https://docs.djangoproject.com/en/5.2/topics/db/transactions/).

## Verificaciones y evidencia

En la primera implementación se ejecutaron 17 pruebas PostgreSQL como línea base y 19 tras
incorporar dos regresiones: composición de recursos por pantalla y descubrimiento de los
recursos precargados. Pasaron Django, Ruff, comprobación de sintaxis de los cuatro JS propios,
`findstatic`, recopilación de 25 estáticos en un destino aislado y revisión del diff.

Las comprobaciones en Chromium cubrieron login, inicio y cambio de contraseña a 360 y 1440 px.
Los seis pares de capturas conservaron el mismo SHA-256. Se comprobó mostrar/ocultar contraseña,
foco en errores y ausencia de desbordamiento horizontal y errores de recursos o JS. La PWA v8
instaló 20 recursos públicos y mostró la alternativa «Sin conexión» sin almacenar las páginas
HTML de acceso o privadas. Estas pruebas usaron HTML renderizado con una usuaria ficticia y
un servidor temporal; no sustituyen el recorrido autenticado completo en un navegador real.

Evidencia persistida desde los resultados originales, sin volver a ejecutar el recorrido:

- [Informe de navegador](../../evidence/frontend/2026-10-28-modularidad/verificacion_navegador.json).
- [Informe PWA](../../evidence/frontend/2026-10-28-modularidad/verificacion_pwa.json).
- [Comparación SHA-256 de capturas](../../evidence/frontend/2026-10-28-modularidad/capturas_sha256.json).

Al actualizar las reglas se validó la skill con `quick_validate.py`, sus enlaces locales,
bloques Markdown y `git diff --check`. Durante esta documentación se revalidaron la skill,
el estado Git y el hash remoto; se conservaron los JSON originales y se recomprobaron los
seis pares de hashes. No se repitieron las pruebas funcionales del producto.

## Publicación y pendientes

El [commit d0c47ed](https://github.com/FranAC18/ZhudAleli/commit/d0c47edc2b011be6c0ef76b3c9d6ddc563395bb5)
se publicó en `docs/requisitos-y-organizacion-del-vault`. Su conjunto exacto y verificación
posterior están en [[../checkpoints/2026-10-28-definicion-modularidad-post-commit]].

1. Implementar una primera pantalla bajo la convención aprobada, con su configuración y
   verificaciones completas; después extender el patrón a las demás.
2. Resolver las carpetas vacías y la fragmentación mínima del CSS dentro de esa porción,
   conservando el diseño y el comportamiento existentes.
3. Completar las verificaciones pendientes de SB-S2-02. La definición de modularidad no
   marca terminada la funcionalidad ni implementa administración u otros módulos.
4. Mantener separados los cambios de app, documentos y archivos locales ajenos. La app
   continúa sin commit de estos cambios; tampoco se creó PR, tag ni despliegue.
5. Sincronizar los metadatos operativos de [[../ESTADO-ACTIVO]] en una tarea del coordinador:
   aún contienen el HEAD anterior y el apunte previo al commit. Este registro conserva el
   estado posterior comprobado sin sobrescribir el corte anterior.

La presente sesión, el checkpoint posterior y la evidencia añadida siguen sin commit.
La solicitud de documentación no se interpretó como autorización para otra publicación Git.
