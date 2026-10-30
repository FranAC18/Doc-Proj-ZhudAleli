---
title: Corrección del login y notificaciones de resultado
type: frontend-evidence
status: verified-locally
date: 2026-10-28
requirement: RF-ACC-001; RNF-UX-001; RNF-UX-002; RNF-UX-003
sprint: S2
task: SB-S2-02; presentación de formularios actuales
commit: pending
---

# Corrección del login y notificaciones

El tesista reportó el control de contraseña sin formato y el mensaje de error repetido
en el resumen y debajo del campo. Durante la corrección solicitó una notificación flotante
en la esquina inferior derecha, con el diseño rosado de su referencia y adaptación móvil.

Se conserva la composición del login. El aviso de formulario reúne sus errores una sola
vez, con enlaces a los campos, asociación accesible y marcado visual. Los mensajes Django
comparten el contenedor inferior derecho. El cierre funciona por botón y Escape, sin
fondo bloqueante ni caducidad automática. El foco vuelve al campo cuando corresponde.

Las hojas y el script afectados tienen revisión en su URL. Servir una hoja anterior al
traslado de estilos reproduce el control roto; el HTML corregido solicita la revisión nueva.
La caché del tesista no fue inspeccionada directamente. Se estabiliza el relleno al cambiar
de ancho y se unifica el fondo de autocompletado, sin cambiar autenticación ni sus mensajes.

## Verificación

- 31 pruebas PostgreSQL correctas, incluidos acceso, contraseña, contactos y estáticos.
  Las comprobaciones de usuario y contraseña incorrectos exigen que el mensaje aparezca
  una sola vez.
- Revisión en Chrome con sesión Django real, cuentas ficticias y base PostgreSQL aislada.
  Capturas y geometría a 360, 375, 768, 1280, 1440 y 1580 px: notificación fija inferior
  derecha, controles de contraseña alineados, un icono visible y sin desbordamiento.
- Errores de usuario, contraseña, campos vacíos, bloqueo temporal, contraseña actual y
  contraseñas nuevas distintas; enlaces al campo, cierre, Escape y confirmación de correo.
- Sin IDs duplicados ni referencias accesibles inexistentes. Zoom al 200 % comprobado.
- CSS anterior reproducido de forma controlada; la hoja sin revisión no se solicita en el
  flujo corregido. La pseudo-clase de autocompletado se fuerza mediante CDP y conserva
  la superficie cálida en usuario y contraseña; no se usan contraseñas guardadas reales.
- PWA v15 con 23 recursos públicos y sustitución de la caché anterior.
- Ruff lint/format, sintaxis JavaScript y `git diff --check` revisados.

Detalle: [verificacion.json](verificacion.json). Ejemplos:
[escritorio](usuario-error-1580.png) y [móvil](usuario-error-375.png).

## Límites

La simulación de CSS antiguo explica una regresión posible sin afirmar que se observó
la caché particular del tesista. La revisión usa Chrome y anchos adaptables; no acredita
pruebas en dispositivos físicos ni validación con usuarias. La base aislada se elimina
al terminar; no se modifican datos de desarrollo ni se envían correos externos.

Se preservan cambios locales concurrentes del formulario de contraseña, incluida su
revisión CSS v9 y sus acciones inferiores. No se cambia el backend, sus reglas, las
prioridades ni el estado de terminación de RF/HU/HT o sprints. Sin commit ni publicación.
