---
title: Corrección del movimiento y radios de las notificaciones
date: 2026-10-28
status: verified-locally
requirement: RF-ACC-001; RNF-UX-001; RNF-UX-002; RNF-UX-003
sprint: S2
task: SB-S2-02
---

# Movimiento suave y geometría coherente

El tesista reportó entrada brusca, salida que desaparecía, scroll horizontal y radios
incoherentes con los campos. La versión anterior confinaba la animación a una columna
con scroll y recortaba el recorrido. Además, el foco podía desplazar ese contenedor y
una regla global cambiaba el radio de la tarjeta enfocada a 10 px.

La notificación entra desde la derecha y sale por la izquierda en todos los anchos;
cada transición dura 640 ms. El overlay acompaña el movimiento y la opacidad del aviso
se mantiene hasta el tramo final de salida. El contenedor permite recorrer el viewport
completo y oculta el desbordamiento horizontal. El foco inicial usa `preventScroll`;
cerrar durante la entrada continúa desde la posición y opacidad actuales.

La tarjeta, los campos y el botón del login usan el token `--za-radius-control`, de
12 px, también en móvil y con foco. Se mantienen ausencia de bordes y sombras, cierre
tras 3 segundos, pausa por interacción, botón de 44 px, Escape, foco contenido e `inert`.
Tras cerrar, el formulario recupera foco, Tab y Escape normales. Con movimiento reducido
solo hay fade de 120 ms. URLs de recursos renovadas y PWA v16, con 23 recursos públicos.

## Verificación

- 18 pruebas Django de frontend, flujo de acceso y PWA correctas sobre PostgreSQL aislado.
- `manage.py check`, sintaxis de JS y revisión de diff correctos.
- Navegador Edge/Chromium contra el servidor Django local. Envíos reales vacíos del login;
  no se usan cuentas ni credenciales reales.
- 360, 375, 768, 1280 y 1440 px: muestreo de keyframes de entrada/salida, tarjeta visible
  durante el recorrido, sin desbordamiento de página ni desplazamiento horizontal del
  contenedor; radio computado igual al campo. Capturas visibles y a mitad de salida.
- Escape, Tab dentro del modal y después de cerrarlo, retorno al campo, botón, enlace de
  error, autocierre y pausa por hover; sin errores JavaScript ni respuestas HTTP fallidas.
- 11 escenarios de navegador correctos, incluido cierre a mitad de entrada sin salto,
  pausa al enfocar un control y texto largo sintético con desplazamiento vertical.
  Reflujo a 720 × 450 px, equivalente al espacio de 1440 × 900 al 200 %; no sustituye
  la comprobación pendiente del zoom nativo del navegador.
- [Script reproducible](verificar-movimiento.cjs) y [resultados](movimiento-verificacion.json).
- [Móvil visible](suave-visible-360.png), [escritorio visible](suave-visible-1440.png) y
  [salida a mitad de recorrido](suave-salida-1440.png).

## Reglas de interfaz

| Regla | Resultado de esta porción |
|---|---|
| UI-01 Carga | No aplica: no se introduce carga asíncrona ni esperas artificiales. |
| UI-02 Adaptación | Verificada en los cinco anchos obligatorios, sin scroll horizontal durante ambas animaciones. |
| UI-03 Jerarquía | Verificada: se conserva título, errores concretos, enlaces y acción de cierre. |
| UI-04 Tokens | Verificada: radio compartido, incluso con foco; se conservan colores y tipografía. |
| UI-05 Consistencia | Verificada en el componente compartido y el login. Los recorridos autenticados de contactos/contraseña no se repiten en navegador. |
| UI-06 Accesibilidad | Teclado, retorno de foco, pausa por foco, movimiento reducido y reflujo verificados. Contraste y zoom nativo al 200 % no se vuelven a medir; evidencia anterior conservada. |
| UI-07 Estados | Error reproducido por POST real y retorno al formulario verificados. Mensajes de éxito conservan la misma clase compartida; no se reproduce una operación autenticada nueva. |
| UI-08 Interacción | Cierre manual, cierre durante entrada sin salto, Escape, enlaces, pausa por hover/foco y liberación del teclado verificados. |

Validación con usuarias pendiente. La documentación anterior conserva el corte histórico;
esta porción sustituye sus 360 ms y el movimiento vertical de móvil. RF, HU/HT, pila,
prioridades, criterios de negocio y estado abierto de SB-S2-02 se conservan. La evidencia
se enlaza en el gestor local; no se declara terminado el acceso ni se publica al docente.
