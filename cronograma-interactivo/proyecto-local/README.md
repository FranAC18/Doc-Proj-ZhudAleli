---
titulo: Cronograma interactivo local de Zhud Aleli
tipo: herramienta-interna
version: "5.1"
fecha: 2026-10-27
estado: herramienta-local
publicacion: no-destinada-al-repositorio-docente
---

# Cronograma interactivo local

El acceso directo **Abrir cronograma de sprints** inicia esta aplicación en el navegador y sirve el dashboard de trazabilidad v5.1. Incluye Product Backlog, Catálogo de Requisitos, Kanban, Gantt y Bitácora. La vista **Historias HU y HT** reúne 56 historias de usuario (cinco candidatas de superadministración) y 19 técnicas. El calendario vigente muestra S1–S5 e integración hasta el 23 de diciembre; S6 permanece solo como referencia histórica en las tareas que aún requieren selección. La constancia v1.2 conserva el cierre parcial de S1 sin declarar pendientes completados.

## Abrir

1. Tener Python 3.9 o posterior instalado en Windows.
2. Abrir [Abrir cronograma.cmd](Abrir%20cronograma.cmd) con doble clic.
3. Se abre el navegador en `http://127.0.0.1:55478/`. Dejar abierta la ventana del servidor mientras se usa la aplicación.

El servidor escucha solo en `127.0.0.1`. Además de servir el HTML, permite abrir rutas locales permitidas de `documentacion/` y `docs/evidence/` en el Explorador de archivos. Los enlaces web de evidencia se abren en una pestaña nueva.

## Actualizar el dashboard local

Los JSON de `web/` son las fuentes del calendario. Después de regenerar `../index.html`, ejecuta desde esta carpeta:

```powershell
python actualizar_dashboard_local.py
```

El actualizador copia el HTML actualizado a `web/index.html` y conserva el puente local de apertura de evidencias. Las fechas antiguas guardadas para tareas e historias conocidas se concilian con el plan nuevo; el avance, la evidencia y las ediciones propias permanecen. El servidor aplica un nonce CSP a los scripts en línea y mantiene la política restrictiva para el resto del contenido.

## Guardado y migración

Los cambios se guardan en dos lugares: en `localStorage` con la clave `tesis_scrum_multireq_v1` y en `estado/dashboard_v5.json`, mediante el servidor local. El archivo JSON es el respaldo persistente del proyecto. Al iniciar, el dashboard carga ese archivo y lo combina con los datos del navegador. También conserva la importación y exportación de respaldos JSON.

El archivo histórico `estado/seguimiento_sprints_zhud_aleli.json` se conserva intacto; la versión v5 guarda en `dashboard_v5.json`. La carpeta `estado/` no se publica en Git. Para mover el progreso a otro equipo o perfil, exporta un respaldo desde la aplicación y luego impórtalo.

## Archivos principales

| Ruta | Función |
|---|---|
| `Abrir cronograma.cmd` | Inicia el servidor local para abrir el dashboard. |
| `servidor.py` | Sirve el dashboard y abre archivos/carpetas permitidos en el Explorador. |
| `actualizar_dashboard_local.py` | Sincroniza el último HTML raíz y añade el puente de evidencias local. |
| `web/index.html` | Copia local autocontenida del dashboard v5. |
| `web/datos-proyecto.json` y `recursos-sprints.json` | Fuentes vigentes del calendario, historias, requisitos y enlaces documentales. |
| `estado/dashboard_v5.json` | Cambios del dashboard v5, guardados en el equipo y reutilizados entre sesiones. |
| `estado/seguimiento_sprints_zhud_aleli.json` | Seguimiento histórico del dashboard anterior; se conserva sin cambios. |
| `verificar_proyecto.mjs` | Prueba de persistencia entre reinicios y puertos, servidor, CSP y rutas seguras. |

## Verificación

Ejecuta:

```powershell
python actualizar_dashboard_local.py
node ..\verificar_dashboard.mjs
node verificar_proyecto.mjs
```

Google Fonts y Lucide Icons se cargan desde CDN. Sin conexión, la aplicación conserva la lógica y los datos integrados, y usa tipografía del sistema.
