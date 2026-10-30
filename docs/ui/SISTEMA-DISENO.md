---
title: Sistema de diseño y criterios UX
type: design-system
status: proposed
date: 2026-07-21
tags:
  - proyecto/tesis
  - tipo/diseno
  - modulo/transversal
---

# Sistema de diseño y criterios UX

## Reglas obligatorias de ejecución — 2026-10-28

La instrucción expresa del tesista se concreta en
[REGLAS-DISENO-INTERFACES.md](REGLAS-DISENO-INTERFACES.md), versión 1.0: carga,
adaptación, jerarquía, tokens, componentes, accesibilidad, estados e interacción.
Se aplica a cada pantalla nueva y a la parte modificada de las existentes. El estado
`proposed` de esta guía se conserva para su dirección visual; no rebaja esas reglas.
La paleta y la identidad cultural siguen pendientes de validación con la organización.

## Intención

La aplicación debe sentirse cercana, tranquila y confiable, no como un panel corporativo
genérico. La belleza vendrá de jerarquía, espacio, tipografía, color y componentes
consistentes; no de animaciones pesadas ni decoraciones que dificulten el trabajo.

La dirección visual es una propuesta. Colores, imágenes, nombre visible y cualquier elemento
cultural se validan con la organización. No se usan patrones o símbolos indígenas como
decoración sin contexto y autorización.

## Principios

1. **Una acción principal por pantalla**: lo más importante se distingue de inmediato.
2. **Reconocer antes que recordar**: navegación, etiquetas y estados siempre visibles.
3. **Móvil primero**: formularios y listados funcionan desde 360 px sin desplazamiento
   horizontal accidental.
4. **Poco peso**: plantillas del servidor, recursos optimizados y JavaScript progresivo.
5. **Errores recuperables**: conservar datos válidos y explicar qué falta y cómo corregir.
6. **Estado comprensible**: texto + icono + color; nunca color solo.
7. **Consistencia**: una misma operación usa el mismo verbo, componente y ubicación.

## Dirección visual provisional

| Token | Valor | Uso |
|---|---|---|
| `--primary` | `#642138` | Vinotinto del login aplicado localmente a acciones y enlaces |
| `--primary-hover` | `#4C192B` | Hover de acciones principales |
| `--primary-soft` | `#F6F0F1` | Fondos de énfasis suave de marca |
| `--accent-purple` | `#8A2BE2` | Acento secundario (detalles) |
| `--accent-blue` | `#4589FF` | Estado informativo |
| `--accent-yellow` | `#F8BE39` | Estado de atención (indicadores no textuales o texto oscuro) |
| `--accent-orange` | `#FF7A59` | Estado de advertencia |
| `--accent-cyan` | `#14B8A6` | Estado de éxito (indicadores) |
| `--bg-body` | `#F7F4F1` | Fondo general de página |
| `--bg-surface` | `#FFFFFF` | Tarjetas y superficies principales |
| `--bg-input` | `#FFFDFA` | Fondo de campos de formulario |
| `--border-light` | `#E8DED9` | Bordes suaves de superficies |
| `--border-control` | `#9B8177` | Borde de campos, contraste superior a 3:1 sobre el fondo de campo |
| `--text-title` | `#1F1422` | Títulos y encabezados principales |
| `--text-body` | `#594D5D` | Texto general de párrafos |
| `--text-secondary` | `#6B616D` | Texto secundario accesible (contraste AA verificado) |
| `--text-muted` | `#9F93A3` | Solo decorativo (contraste < 4.5:1, no para texto informativo) |
| `--danger` | `#B31A4F` | Errores y acciones destructivas |
| `--danger-soft` | `#FCECF2` | Fondo de alertas de error |

La identidad visual es una **propuesta** tomada de la maqueta de referencia y validada con los componentes de `design/style-guide/`. Se confirmará con la organización antes de fijarla como definitiva.

### Tipografía y rendimiento

- **Pantallas actuales**: `"Segoe UI", system-ui, -apple-system, sans-serif`, siguiendo el login y sin descarga de fuentes. `Poppins` permanece como propuesta anterior de identidad; no es una dependencia de las vistas actuales.
- **Rendimiento y funcionamiento sin conexión (`RNF-CON-001`)**: En producción y despliegue Django, las fuentes deben servirse localmente desde `static/vendor/fonts/` (o la carpeta local correspondiente) para eliminar dependencias obligatorias hacia Google Fonts CDN y soportar conectividad inestable.

### Geometría, espaciado y objetivos táctiles

- **Espaciado (`--space-1..7`)**: 4, 8, 12, 16, 20, 24, 32 px.
- **Radios (`--radius-sm/md/lg/pill`)**: 10, 18, 24, 999 px.
- **Radio de controles y notificaciones (`--za-radius-control`)**: 12 px; se conserva
  al enfocar y en móvil, incluidos los campos y el botón del login.
- **Objetivo táctil (`--touch-target`)**: mínimo 44 × 44 px en controles interactivos.
- **Sombras**: `--card-shadow: 0 4px 20px rgba(36, 17, 38, 0.03)` y `--card-hover-shadow: 0 10px 30px rgba(179, 34, 118, 0.07)`.

## Shell responsivo propuesto

- Encabezado con nombre del sistema, perfil y salida.
- Navegación inferior compacta en móvil para tres a cinco destinos prioritarios.
- Barra lateral en escritorio para los mismos destinos, sin duplicar nombres.
- Título, contexto y acción principal en la zona superior de cada vista.
- Contenido en un ancho legible; tablas grandes cambian a tarjetas o filas resumidas en móvil.

La navegación concreta depende de la matriz de permisos y se prueba con cada perfil.

## Componentes mínimos

Actualización del 2026-10-28: por solicitud del tesista se aplican los recursos del login
a las vistas existentes. El panel común resuelve marco, adornos y mensajes; formularios
comparte los controles y errores. Los colores de la tabla reflejan esa implementación
local, con validación organizacional de identidad pendiente. No cambia el alcance funcional.

El [inventario de recursos extraídos del login](RECURSOS-REUTILIZABLES-LOGIN.md)
describe los SVG orgánicos, el adorno independiente para formularios y el botón de
contraseña compartido. Conservan el aspecto existente; su reutilización no obliga
a repetir la composición fotográfica del acceso en otras pantallas.

- Botones primario, secundario, enlace y destructivo con estados focus/disabled/loading.
- Campos de texto, fecha, hora, número, selección y ayuda contextual.
- Notificación de resultado en la esquina superior derecha, adaptada a móvil;
  cada error se muestra una sola vez y enlaza el campo afectado.
- Tarjeta de tarea/actividad/lote con metadatos esenciales.
- Badge de estado con texto e icono.
- Tabla responsiva con filtros y alternativa legible en móvil.
- Estado vacío con explicación y acción posible.
- Confirmación para acciones sensibles, indicando consecuencia.
- Por solicitud del tesista del 2026-10-28, la notificación compartida se comporta como un
  modal accesible, con overlay oscuro, `aria-modal`, foco contenido y Escape. En escritorio
  entra desde la derecha y sale hacia la derecha. En móvil (menos de 768 px), entra de
  arriba hacia abajo y sale de abajo hacia arriba.
  Entrada y salida duran 640 ms; el overlay acompaña la transición y el aviso conserva su
  opacidad hasta el tramo final de salida. El recorrido usa el viewport completo y recorta
  el desbordamiento horizontal, sin una barra lateral ni desaparición prematura. El radio
  usa `--za-radius-control`, también con foco. Respeta `prefers-reduced-motion`, con fade de
  120 ms sin desplazamiento. La tarjeta no tiene bordes ni
  sombras; usa el fondo y el icono. Se cierra tras 3 segundos de reposo, botón o Escape; pausa al interactuar
  con el aviso. Los errores requeridos nombran el dato que falta, por ejemplo «Escribe tu
  contraseña».
- Breadcrumb cuando exista profundidad real, no por costumbre.

Cada componente reutilizable tiene un propietario y ejemplos de uso. Su ubicación sigue la
skill `zhud-aleli-codigo-legible`: frontend por pantalla y recursos comunes cuando exista
reutilización real. La referencia anterior a `templates/components/` no obliga a crear esa
carpeta ni sustituye la convención aprobada del 2026-10-28. No se crean variantes locales
sin revisar si el componente común puede resolverlas.

## Formularios

- Etiqueta persistente sobre cada campo; placeholder solo como ejemplo.
- Unidad junto al valor (`kg`, `h`, `%`) y reglas de redondeo visibles.
- Orden que siga el proceso real de trabajo.
- Valores predeterminados únicamente cuando sean seguros y comprensibles.
- Botón principal describe la acción: “Registrar asistencia”, no “Aceptar”.
- En error, foco en la notificación y enlaces a campos inválidos. El campo conserva su
  marca y asociación accesible, sin repetir el mensaje debajo. Cerrar el aviso devuelve
  el foco al campo afectado cuando corresponde; Escape también permite cerrarlo.
- Prevención de doble envío en operaciones productivas.

## Accesibilidad verificable

- Contraste AA para texto y controles.
- Área táctil mínima aproximada de 44 × 44 px.
- Foco visible y orden lógico de teclado.
- HTML semántico y encabezados jerárquicos.
- Texto alternativo útil para imágenes informativas.
- Errores asociados mediante atributos accesibles.
- Zoom al 200 % sin pérdida de operación.
- No depender de hover, gestos ocultos o iconos aislados.

## Evidencia por funcionalidad

Cada historia con interfaz debe guardar:

- vista móvil y escritorio del recorrido principal;
- estado vacío, error y éxito;
- resultado de revisión por teclado/contraste;
- prueba del rol autorizado y del rol denegado;
- observaciones de validación con usuarias, fecha y cambios derivados.

Una pantalla visualmente pulida no está terminada si el recorrido no funciona con datos y
permisos reales.

## Continuidad offline — requisitos aprobados, diseño por concretar

Fuente: [[../requirements/CAT-REQ-001|CAT-REQ-001 v1.1 aprobado por el tesista]] y
[[../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack|stack actualizado]].
Los formularios esenciales priorizan seleccionar, tocar y confirmar; pesos y cantidades
usan entrada numérica con unidad. Evitar que seleccionar un valor recurrente sustituya
una medición real. Indicadores y reportes muestran solo información útil y explicable.

Los recorridos de asistencia/pesajes deben distinguir “Guardado en este dispositivo”,
“Pendiente de sincronizar”, “Sincronizado” y “Necesita revisión”, con texto y acción de
recuperación. Un error de almacenamiento no muestra éxito. El usuario debe comprender
qué falta por enviar y qué fue rechazado; la política de salida y dispositivo compartido
se define en P-14 sin borrar pendientes silenciosamente ni exponerlos a otra cuenta.

La maqueta visual no demuestra guardado, sincronización ni permisos. SPEC-001 conserva
sus pantallas de acceso en línea y no-caché privado. La futura PWA necesita interfaz local
específica para las operaciones aprobadas, sin guardar páginas privadas indiscriminadamente.
