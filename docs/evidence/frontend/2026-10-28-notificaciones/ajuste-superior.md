# Notificación modal responsiva — 2026-10-28

## Solicitud y resultado

El tesista pidió una tarjeta sin bordes, mensajes claros para datos faltantes y transiciones
distintas para escritorio y móvil. La notificación ahora es un diálogo modal con overlay oscuro.
En escritorio (≥768 px) entra desde la derecha y sale hacia la izquierda; en móvil (<768 px)
entra desde arriba y sale hacia arriba. Las transiciones del diálogo y el fade del overlay duran
360 ms y usan `cubic-bezier(.22, 1, .36, 1)`. Con `prefers-reduced-motion: reduce` solo hay un
fade de 120 ms. El DOM oculta la tarjeta después del evento de fin de animación, con un respaldo
posterior.

El contorno, los bordes y las sombras se eliminan en todos los estados. El diálogo usa `role="dialog"`,
`aria-modal="true"`, foco contenido, Escape y `inert` en el contenido de fondo. Conserva el
autocierre después de 3 segundos de reposo, el botón de cierre y el vínculo de error al campo.
Un campo obligatorio de login muestra instrucciones específicas, como «Escribe tu contraseña».

## Verificación realizada

- Chromium con base de datos PostgreSQL aislada y usuarias ficticias; el servidor temporal fue
detenido y su base eliminada al terminar.
- Escritorio 1280 px y móvil 375 px: keyframes de entrada/salida, overlay activo, tarjeta sin
  border/outline computados, `aria-modal`, `inert`, Escape y retorno del foco al campo inválido.
- Navegación con Tab/Mayús+Tab: el foco se mantiene y envuelve dentro del diálogo.
- Autocierre en reposo: overlay y `inert` se retiran y el foco vuelve al formulario.
- Movimiento reducido: entrada de solo fade, sin transform.
- Capturas: [escritorio](modal-escritorio.png) · [móvil](modal-movil.png).
- Sintaxis JavaScript y Python, Ruff para `forms.py` y `git diff --check`: correctos.
- La suite funcional completa no se ejecutó para este ajuste.

SB-S2-02 y requisitos/historias conservan su estado abierto.
