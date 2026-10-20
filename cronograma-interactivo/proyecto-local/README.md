---
titulo: Cronograma interactivo como proyecto local
tipo: analisis-interno
version: "2.1"
fecha: 2026-10-20
estado: herramienta-local
publicacion: no-destinada-al-repositorio-docente
---

# Cronograma local de Zhud Alelí

Esta herramienta interna integra en una sola aplicación el tablero Kanban,
Product Backlog, cronograma Gantt, matriz de trazabilidad, pendientes,
bitácora y gestión de evidencias. Consulta sprints, tareas, historias y
requisitos derivados de los documentos del proyecto, y registra cambios en
el seguimiento local. No es la aplicación Django de la asociación ni modifica
los documentos formales.

## Abrir con doble clic

1. Tener Python 3.9 o posterior instalado en Windows.
2. Abrir [Abrir cronograma.cmd](Abrir%20cronograma.cmd) con doble clic.
3. Se abrirá el navegador en `http://127.0.0.1:<puerto libre>`.
4. Dejar abierta la ventana negra mientras se usa el cronograma. Al cerrarla,
   se detiene el servidor. Abrir de nuevo el mismo archivo para continuar.

El puerto se elige automáticamente en cada inicio para evitar conflictos con
otros proyectos. Si se abre el lanzador dos veces, la segunda apertura muestra
la instancia existente en el navegador.

## Guardado del avance

**Guardar seguimiento** escribe en `estado/seguimiento_sprints_zhud_aleli.json`.
Al abrir de nuevo la herramienta, se lee ese archivo. La carpeta `estado/` se
crea al iniciar y el JSON al guardar la primera tarea; ambos quedan excluidos
de Git. **Exportar copia**
descarga un respaldo; **Importar seguimiento** incorpora un JSON anterior y
conserva el registro más reciente por tarea. El mismo JSON incluye tareas
locales, ediciones de planificación, estados de sprint y bitácora.

Si se registró avance en el HTML autónomo anterior, abrirlo, usar **Exportar
copia** y después importar ese JSON en este proyecto. El navegador impide que
un sitio en `localhost` lea automáticamente el almacenamiento de una página
abierta como `file://`.

## Organización

| Ruta | Qué contiene |
|---|---|
| `Abrir cronograma.cmd` | Acceso de doble clic para Windows. |
| `servidor.py` | Servidor local y guardado del avance. |
| `web/index.html` | Estructura de la pantalla. |
| `web/assets/styles.css` | Presentación visual. |
| `web/assets/app.js` | Interacción del Gantt y comunicación con el servidor. |
| `web/assets/interaction.css` | Tarjetas adaptables y panel de documentos por sprint. |
| `web/datos-proyecto.json` | Sprints, tareas y relaciones generadas desde los documentos. |
| `web/recursos-sprints.json` | Accesos documentales iniciales para S0–S6 y cierre. |
| `estado/` | Avance local; se crea al usar la herramienta y no se versiona. |
| `verificar_proyecto.mjs` | Prueba de puerto, guardado, reinicio e importación. |

Para actualizar las referencias documentales, ejecutar
`python ../generar_gantt.py` desde esta carpeta. Ese proceso regenera
`web/datos-proyecto.json` sin tocar `estado/`.

## Documentos y evidencias por sprint

El resumen de sprints es un carrusel horizontal desplegable. Usa las flechas, el teclado o el desplazamiento táctil para elegir una etapa. Cada tarjeta abre el detalle con su lista de tareas, el avance registrado y los accesos documentales. Desde cada fila se puede editar una tarea y regresar al sprint sin perder el contexto.

Los botones **Abrir en carpeta** y **Abrir evidencia** abren el Explorador de Windows y seleccionan el archivo local. Los documentos locales no se muestran dentro del navegador. Los enlaces web se abren en otra pestaña. La sección **Documentos fuente** usa el mismo comportamiento.

En cada tarjeta, **Tareas y documentos** abre el detalle del sprint. Sprint 0
incluye su cierre y pruebas históricas; S1 aparece como parcial, con sus
pendientes de revisión visibles. El formulario del panel permite agregar o
quitar enlaces web y rutas locales de `documentacion/` (`/fuentes/...`) o
`docs/evidence/` (`/evidencias/...`). Se admiten documentos comunes como
Markdown, PDF, Word, Excel, PowerPoint e imágenes. Los accesos agregados se
guardan junto al seguimiento local y se incluyen en **Exportar avance**.

En el detalle de una tarea, el campo de evidencia también acepta una URL o una
ruta documental. Si es local y válida, el botón **Abrir evidencia** selecciona
el archivo en su carpeta después de guardar. Los documentos fuente no se editan
desde el cronograma.

## Vistas y edición

La navegación superior permite cambiar entre **Kanban**, **Product Backlog**,
**Cronograma**, **Tareas y avance**, **Bitácora** y **Pendientes**. El Kanban
muestra el estado de cada tarea y permite cambiarlo arrastrando tarjetas. La
tabla del backlog reúne las historias, historias técnicas, requisitos y tareas
del proyecto. Las búsquedas y filtros de sprints facilitan localizar elementos.

El formulario **Nueva tarea** agrega tareas locales con prioridad, estimación,
sprint, fechas y evidencia. Las tareas fuente se pueden editar para registrar
su planificación y seguimiento local; no se reescriben las historias,
requisitos ni documentos de origen. Solo las tareas agregadas localmente se
pueden eliminar. El Gantt, las relaciones y la matriz conservan las tareas y
trazabilidad del documento fuente.

La bitácora registra cambios de estado, evidencia, estimación, tareas, accesos
y apertura o cierre de sprints. Los estados de cierre se guardan como datos de
seguimiento y no alteran el calendario planificado. Las tareas locales y sus
ediciones se incluyen en el respaldo de seguimiento.

## Verificación y límites

La prueba de navegador comprobó la carga de 27 tareas, un puerto libre,
guardado en JSON, recuperación tras reiniciar, importación, fuentes
documentales y rechazo de solicitudes ajenas a la página local. El servidor
escucha únicamente en `127.0.0.1`; no publica contenido en internet.

La herramienta está en `F:\Tesis\App Tesis\cronograma-interactivo`; el acceso directo está en la raíz del proyecto. El repositorio del docente recibe
solo los documentos finales de `documentacion/` tras confirmación específica.
