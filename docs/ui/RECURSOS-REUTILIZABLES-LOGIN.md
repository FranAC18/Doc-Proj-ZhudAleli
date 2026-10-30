---
title: Recursos reutilizables extraídos del login
type: ui-components
version: "1.7"
status: implemented-locally
date: 2026-10-28
source: login existente y solicitud expresa del tesista
requirement: RF-ACC-001; RNF-UX-001; RNF-UX-002; RNF-UX-003
sprint: S2
task: SB-S2-02; porción visual de HT-GEN-004
---

# Recursos reutilizables del login

El lenguaje visual que destaca en el login combina fotografía, capas orgánicas vinotinto,
una transición crema y blanca hacia el formulario y una versión horizontal para móvil.
El valor reutilizable son las formas y su composición discreta alrededor del contenido.
La fotografía y las proporciones de dos paneles corresponden a la pantalla de acceso.

La preferencia del tesista autoriza reutilizar estos adornos. La identidad cultural conserva
su validación pendiente; esta extracción no fija una identidad definitiva ni cambia requisitos.

## Inventario y propietario

Las rutas de producto siguientes pertenecen a la raíz Git independiente `app/`:

| Pieza | Fuente única | Uso y límite |
|---|---|---|
| Capas vinotinto | `templates/components/adornos/capas_vinotinto.html` | SVG original en tres capas; destellos opcionales. Se usa en login y cambio de contraseña. |
| Onda vertical | `templates/components/adornos/onda_vertical.html` | Transición lateral crema/blanca; admite `vista` para conservar el encuadre de cada pantalla. |
| Onda horizontal | `templates/components/adornos/onda_horizontal.html` | Transición al pie de una cabecera; el login la muestra en móvil. |
| Adorno para formulario | `templates/components/adornos/formulario.html` y `static/compartido/adornos-formulario.css` | Combina capas vinotinto y onda vertical detrás de un formulario; funciona sin `login.css`. Ya lo consume cambio de contraseña. |
| Mostrar/ocultar contraseña | `templates/components/formularios/alternar_contrasena.html` | Botón e iconos compartidos por login y cambio; recibe `campo`. Usa `password-toggle.js` y los estilos comunes de `formularios.css`. |
| Panel de contenido | `templates/components/panel.html` | Inicio, contactos, verificación y estado heredan marco y adornos. Las notificaciones se presentan desde la base común. |
| Resumen y error de campo | `templates/components/formularios/resumen_errores.html`, `error_campo.html` | Una notificación por formulario con errores; cada mensaje se representa una sola vez y enlaza el campo correspondiente. |
| Notificaciones | `static/compartido/notificaciones.css`, `notificaciones.js`, `templates/components/notificaciones/cerrar.html` | Modal arriba a la derecha; escritorio entra y sale por la derecha; móvil entra desde arriba y sale hacia arriba. Transiciones de 640 ms, overlay, foco contenido, Escape y cierre a los 3 segundos de reposo. Radio compartido con los campos. |
| Campos y acción de envío | `static/compartido/formularios.css` | Ya compartidos antes de esta tarea; el login aplica ajustes propios. No se copia toda su hoja de estilos a otras pantallas. |
| Mensajes y errores | `templates/components/messages.html`, `static/compartido/form-feedback.js` | Ya compartidos; los resúmenes de error siguen en cada pantalla por su contenido y campos. |
| Logotipos e identidad | `static/brand/` | Ya compartidos; el blanco requiere un fondo que permita distinguirlo. |

## Uso en un formulario nuevo

Cargar `compartido/adornos-formulario.css` desde el bloque de estilos de la pantalla.
El contenedor mantiene su fondo, tamaño, radio y espacio interior definidos por esa pantalla:

```django
{% load static %}
<link rel="stylesheet" href="{% static 'compartido/adornos-formulario.css' %}">

<section class="za-marco-formulario" aria-labelledby="titulo-formulario">
  {% include "components/adornos/formulario.html" only %}
  <div class="za-contenido-formulario">
    <h1 id="titulo-formulario">Título de la tarea</h1>
    <!-- Formulario real de la pantalla, con sus etiquetas, errores y acción. -->
  </div>
</section>
```

Para activar los destellos, pasar `with mostrar_destellos=True only`. Cada SVG también puede
incluirse por separado; `clase_svg` permite posicionarlo con el CSS de la pantalla. Los
componentes producen SVG inline procesados por Django; no son imágenes que requieran red
adicional ni se publican como plantillas estáticas.

## Ajustes seguros

- Las variables `--za-adorno-vino-suave`, `--za-adorno-vino-profundo`,
  `--za-adorno-vino-frontal`, `--za-adorno-dorado`, `--za-adorno-crema`,
  `--za-adorno-crema-suave` y `--za-adorno-superficie` conservan los colores existentes
  como respaldo. Un cambio se define en el contenedor y se revisa por contraste.
- El adorno va detrás del contenido, recortado por su marco; no recibe eventos del puntero,
  foco de teclado ni nombres accesibles. No se coloca dentro de un campo ni encima de texto.
- Las animaciones del formulario solo se activan si la persona no pide movimiento reducido.
  Las animaciones de la composición fotográfica siguen siendo propias del login.
- No se generalizan automáticamente la fotografía, la contracción de cabecera al escribir,
  los tamaños con `cqw` ni las proporciones del login a formularios extensos.

## Verificación y alcance

### Corrección del login y notificaciones — 2026-10-28

El tesista reportó el control de contraseña descompuesto y mensajes repetidos, y solicitó
convertir el aviso rosado en una notificación inferior derecha para móvil y escritorio.
La nueva presentación sustituye el resumen dentro del formulario y el error duplicado
debajo del campo. Los campos mantienen `aria-invalid` y `aria-describedby`; las descripciones
apuntan al mensaje único de la notificación. Si fallan varios campos se distingue su etiqueta.

La notificación conserva icono, fondo rosado y borde lateral. Se enfoca al responder con
errores, sus enlaces enfocan el campo, y se cierra con botón de 44 px o Escape. No impide
interactuar con la página. Los mensajes Django de éxito, información, advertencia y error
comparten el mismo contenedor y cierre, con sus colores semánticos. No se añaden temporizadores.

Las URLs de estilos compartidos, estilos de login y script de feedback incorporan revisión
para evitar reutilizar hojas anteriores al traslado del control. La simulación con CSS
antiguo reproduce el fallo; la revisión nueva evita esa URL. No se inspeccionó la caché del
navegador del tesista, por lo que se registra como explicación reproducible y no como
observación directa de su caché. El autocompletado conserva el fondo de los campos.
La PWA final de esta corrección es v15. La composición fotográfica del login se conserva;
el relleno del formulario deja de transicionar al cambiar de ancho para evitar compresión.

Evidencia: [corrección y notificaciones](../evidence/frontend/2026-10-28-notificaciones/resumen.md).

### Ajuste de posición y duración — 2026-10-28

El tesista pidió mostrar la notificación arriba en móvil y escritorio, cerrarla tras 3 segundos
y permitir el cierre manual. El contenedor usa ahora el borde superior con respeto al área
segura del dispositivo. El aviso no tiene borde, incluso cuando recibe el foco; su estado se
comunica con fondo, icono y sombra. El contador se pausa durante hover o mientras el foco esté
en el botón o los enlaces para no interrumpir la interacción. La salida combina desvanecimiento
y desplazamiento suave durante 800 ms; respeta movimiento reducido. Escape y el botón de cierre
siguen disponibles. Los campos obligatorios usan mensajes concretos como «Escribe tu contraseña».
Se renuevan las URLs versionadas de los dos recursos compartidos afectados.

### Modal responsivo solicitado — 2026-10-28

El tesista precisó que el modal no debe tener ningún borde ni sombra y pidió animaciones de 360 ms por
dispositivo. Escritorio (desde 768 px): entrada desde la derecha y salida hacia la izquierda.
Móvil: entrada desde arriba y salida hacia arriba. El overlay acompaña ambas transiciones con
fade. `prefers-reduced-motion` elimina el desplazamiento y deja un fade corto. El diálogo
declara `aria-modal`, contiene el foco, bloquea el fondo con `inert` y se cierra con Escape.
El desmontaje ocurre al terminar la animación. Se conserva el cierre tras 3 segundos de reposo.

### Corrección de suavidad, desbordamiento y radios — 2026-10-28

La solicitud posterior sustituye las direcciones por breakpoint del apartado anterior:
en todos los dispositivos entra desde la derecha y sale por la izquierda, con 640 ms por
transición. El contenedor ocupa el viewport y oculta el desbordamiento horizontal; conserva
desplazamiento vertical para avisos largos. El foco inicial no desplaza el contenedor.
Si se cierra durante la entrada, la salida continúa desde la posición y opacidad actuales.

La tarjeta, los campos y el botón de login usan `--za-radius-control` (12 px). Se elimina
la variación local de 14 px en móvil y se evita que el foco global cambie el radio del aviso.
El cierre libera el teclado: Tab y Escape vuelven a funcionar en el formulario.
Se conserva overlay, autocierre, pausa por interacción y movimiento reducido.
URLs renovadas y PWA v16. Verificación y límites:
[movimiento suave](../evidence/frontend/2026-10-28-notificaciones/movimiento-suave.md).

### Corrección de direcciones por dispositivo — 2026-10-28

El tesista corrige la dirección de salida y recupera el comportamiento vertical de móvil:
escritorio entra desde la derecha y sale hacia la derecha; por debajo de 768 px entra de
arriba hacia abajo y sale de abajo hacia arriba. Conserva 640 ms, curvas suaves, radio de
12 px, prevención de desbordamiento y cierre desde la posición actual. CSS versionado v6
y PWA v17. Esta precisión sustituye el recorrido hacia la izquierda del apartado anterior.
Evidencia: [direcciones por dispositivo](../evidence/frontend/2026-10-28-notificaciones/direcciones.md).

### Aplicación a las vistas actuales — 2026-10-28

Por instrucción expresa del tesista, los componentes se aplican a login, cambio de
contraseña, contactos de acceso, verificación de correo, inicio y estado del sistema.
El HTML offline conserva el mismo lenguaje visual con estilos internos para no depender
de la red. El login mantiene su composición fotográfica; los demás paneles usan curvas
discretas en sus márgenes. No se añaden operaciones de negocio ni permisos.

La apariencia del control de contraseña vive ahora en `static/compartido/formularios.css`;
se conservan sus clases existentes por compatibilidad. El CSS del listado de contactos
pertenece a `accounts/contactos/recursos/contactos.css`, registrado con su prefijo estático.
Los mensajes se muestran una sola vez en los paneles compartidos. Correo y código conservan
su valor tras un error. Los formularios indican envío, bloquean doble envío y restauran el
botón al volver mediante el historial. El envío real y su resultado siguen en el backend.

La base aplica el vinotinto del login, fondos cálidos y una sola escala de controles.
El borde de campo `#9b8177` supera 3:1 sobre `#fffdfa`; el foco usa el vinotinto.
La tipografía usa los recursos del sistema, sin nuevas fuentes o dependencias externas.
La identidad visual conserva su validación organizacional pendiente.

La PWA final de esta porción es v13, con 21 recursos públicos, incluidos los estilos de
contactos. La revisión está en
[evidencia de las vistas](../evidence/frontend/2026-10-28-componentes-vistas/resumen.md).
No se declara completo el acceso multicanal, SB-S2-02 ni HT-GEN-004.

### Verificación conservada de la extracción v1.0

Se compararon capturas de login normal y con errores, cambio de contraseña y primer acceso
a 360, 375, 768, 1280 y 1440 px: veinte parejas idénticas con movimiento reducido,
sin desbordamiento horizontal ni errores de JavaScript o recursos. Son plantillas Django
renderizadas con datos ficticios, no aceptación con usuarias ni prueba de autenticación visual.
Las pruebas de acceso verifican por separado los recorridos con PostgreSQL.

La PWA v11 añade la hoja compartida a sus recursos públicos; las páginas privadas y de
acceso siguen fuera de caché. Esta porción no completa SB-S2-02 ni HT-GEN-004.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-28 | Extracción de SVG, adorno de formulario e iconos de contraseña. |
| 1.1 | 2026-10-28 | Aplicación a las vistas actuales, panel compartido, errores accesibles y controles coherentes. |
| 1.2 | 2026-10-28 | Corrección del control de contraseña, eliminación de mensajes repetidos y notificaciones flotantes solicitadas por el tesista. |
| 1.3 | 2026-10-28 | Notificaciones superiores con cierre a los 3 segundos y pausa accesible durante interacción. |
| 1.4 | 2026-10-28 | Eliminación de bordes, mensajes obligatorios específicos y salida animada de 800 ms. |
| 1.5 | 2026-10-28 | Modal con overlay y foco contenido; entrada y salida responsivas según breakpoint de 768 px. |
| 1.6 | 2026-10-28 | Recorrido horizontal suave de 640 ms, sin scroll horizontal; radios compartidos y teclado liberado al cerrar. |
| 1.7 | 2026-10-28 | Escritorio entra y sale por la derecha; móvil entra desde arriba y vuelve hacia arriba al salir. |
