---
title: Componentes del login aplicados a las vistas existentes
type: frontend-evidence
status: verified-locally
date: 2026-10-28
requirement: RF-ACC-001; RF-ACC-006; RNF-UX-001; RNF-UX-002; RNF-UX-003
sprint: S2
task: SB-S2-02; porción de HT-GEN-004 y presentación de contactos existente
commit: pending
---

# Aplicación de componentes a las vistas existentes

El tesista solicitó implementar los componentes extraídos del login en las vistas y HTML
actuales. Login y cambio de contraseña conservan su composición y reutilizan los errores,
iconos y controles compartidos. Contactos, verificación, inicio y estado heredan un panel
con adornos discretos y una única presentación de mensajes. La pantalla sin conexión
adopta colores y controles consistentes mediante estilos internos, sin depender de la red.

Los campos tienen errores asociados con IDs únicos, foco en el resumen y conservación
del correo o código tras un error. El envío indica progreso y evita repetir la petición;
volver por el historial restaura el botón. No se cambian las reglas de acceso, seguridad,
correo, código ni operaciones de backend. El listado de contactos posee su CSS bajo la
pantalla y su registro de estáticos; el resto de los componentes reside en las rutas comunes.

## Verificación

- 31 pruebas PostgreSQL correctas, incluidas autenticación, contactos, permisos, cambio
  inicial y voluntario de contraseña, descubrimiento y `collectstatic`, y PWA.
- Django `check` y `makemigrations --check --dry-run`: sin incidencias ni migraciones nuevas.
- Ruff lint y format correctos; sintaxis JavaScript y `git diff --check` correctos.
- 60 capturas de 12 estados en cinco anchos: 360, 375, 768, 1280 y 1440 px, con sesión
  Django real sobre WSGI y una base PostgreSQL aislada. Sin desbordamiento, imágenes rotas,
  IDs duplicados, referencias accesibles inexistentes ni errores de JavaScript o recursos.
- Login permitido y acceso anónimo denegado; mostrar/ocultar contraseña por teclado;
  correo emitido en memoria, código inválido con recuperación y código correcto con
  confirmación única; cambio de contraseña, primer acceso y salida comprobados.
- Revisión adicional con zoom al 200 %, dirección de correo larga, foco visible,
  estado de envío, prevención de doble envío y restauración del botón desde el historial.
- Borde de campo `#9b8177` sobre `#fffdfa`: 3.56:1; texto primario `#642138` sobre
  el mismo fondo: 11.38:1. Los adornos se excluyen del foco y del árbol accesible.
- PWA v13: 21 recursos públicos, retirada de la caché anterior, alternativa offline y
  reintento correcto al restaurar conexión. Las páginas privadas siguen fuera de caché.

Detalle: [verificacion.json](verificacion.json). Ejemplos: [contactos en móvil](contactos-vacio-375.png),
[contactos en escritorio](contactos-vacio-1440.png) e [inicio](inicio-1440.png).

## Límites y continuidad

Se usan cuentas ficticias y correo en memoria. No se envían correos reales ni se modifica
la base de desarrollo. La base aislada se elimina al cerrar la comprobación. La revisión
en Chrome no acredita validación con usuarias ni todos los navegadores o dispositivos.
Los estados de envío se comprueban interceptando una petición del entorno de pruebas.

Esta porción aplica el diseño a la presentación existente; no completa RF-ACC-006 ni
todo el acceso multicanal, SB-S2-02 o HT-GEN-004. No cambia requisitos, historias,
prioridades, fechas ni estados de terminación de la pila o del backlog. La identidad
visual sigue pendiente de validación organizacional. Sin commit, push ni publicación.
