---
titulo: Dashboard ágil y trazabilidad del proyecto Zhud Alelí
tipo: herramienta-interna
version: "5.0"
fecha: 2026-10-20
---

# Dashboard ágil del proyecto

El acceso directo de Windows está en [../Abrir cronograma de sprints.lnk](../Abrir%20cronograma%20de%20sprints.lnk)
y abre [`proyecto-local/Abrir cronograma.cmd`](proyecto-local/Abrir%20cronograma.cmd). El
lanzador requiere Python 3.9 o posterior e inicia el servidor local, que guarda el avance
en `proyecto-local/estado/` fuera de Git. Para una vista autónoma sin servidor, abre este
[`index.html`](index.html) directamente; el seguimiento de esa vista se guarda en el navegador.

## Modelo de trazabilidad

El flujo de trabajo relaciona:

1. **Requisitos funcionales y no funcionales (RF/RNF):** código, módulo, especificación, criterio global de conformidad e historias relacionadas.
2. **Historias de usuario (HU):** Product Backlog vertical ordenado por prioridad, requisito asociado, formato Como/Quiero/Para, estimación Fibonacci, criterios de aceptación y destino.
3. **Tareas técnicas:** vinculadas a una HU y a un sprint; incluyen estado, fechas y evidencia. Al comprometer una historia sin tareas en un sprint, se genera su tarea técnica inicial.

Las vistas son Product Backlog, Catálogo de Requisitos, Kanban, Gantt y Bitácora. El panel de detalle permite navegar entre HU y requisito con una pila de historial y volver al elemento anterior conservando la posición dentro del panel. El tablero acepta arrastrar y soltar. El reordenamiento de historias, checklist de aceptación, CRUD, creación/cierre de sprints, respaldo e importación se guardan en el navegador.

Cerrar un sprint solicita confirmación; las tareas no completadas y las historias aún no aceptadas pasan al Backlog General. El Gantt permite editar fechas en un modal compacto y requiere registrar el motivo en la bitácora. Al reabrir el sprint, sus elementos permanecen en el destino al que se movieron; se pueden reasignar desde el backlog.

## Datos del proyecto

El HTML integra `proyecto-local/web/datos-proyecto.json`, `recursos-sprints.json` y `proyecto-local/estado/seguimiento_sprints_zhud_aleli.json`. El catálogo actual incluye siete sprints, 51 HUs, 51 RF, nueve RNF, 19 historias técnicas y 27 tareas del backlog. Los puntos que no constan en las fuentes empiezan como **Sin estimar**; no se inventan estimaciones. Las fechas planificadas no demuestran por sí solas ejecución ni aceptación académica.

La clave de guardado es `tesis_scrum_multireq_v1`. Migra el seguimiento de `thesis_agile_traceability_v1`, `tesis_scrum_app_v2`, `tesis_scrum_light_v1` y `zhud-aleli-gantt-v1`. Cada HU conserva una colección de requisitos asociados; los estados de cobertura se calculan desde las historias enlazadas. El avance global y el del sprint se miden por Story Points, sin inventar estimaciones ausentes. Los datos son locales al perfil y navegador. Las URL `http/https` abren en una pestaña nueva; las rutas de evidencia ya registradas se conservan y se pueden copiar desde la tarjeta.

Si el HTML se usa sin un catálogo integrado, incluye un fallback de demostración con RF-01, RF-02, RNF-01, tres historias con relaciones múltiples y cuatro tareas de Sprint 1. En este proyecto se carga primero el catálogo real integrado.

## Regenerar y validar

Edita `dashboard_template.html` para cambiar la interfaz. Ejecuta:

```powershell
python generar_dashboard.py
node verificar_dashboard.mjs
```

El generador integra los JSON fuente en `index.html` y crea `cronograma_interactivo_v5.0_2026-10-20.html`. Los cambios del backlog fuente requieren regenerar el HTML; los cambios locales guardados en el navegador se respaldan desde la aplicación.

Google Fonts y Lucide Icons se cargan vía CDN; si no hay conexión, la tipografía usa fuentes del sistema y la aplicación mantiene su lógica y datos integrados.
