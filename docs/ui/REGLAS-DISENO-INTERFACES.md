---
title: Reglas obligatorias de diseño de interfaces
type: ui-rules
version: "1.0"
status: active
date: 2026-10-28
source: solicitud expresa del tesista y ocho referencias visuales del 2026-10-28
scope: diseño, implementación y revisión de interfaces de Zhud Alelí
organization_visual_validation: pending
---

# Reglas obligatorias de diseño de interfaces

Estas reglas concretan la instrucción del tesista del 2026-10-28: interfaces coherentes,
claras y cuidadas sin tener que repetir las mismas correcciones a la IA. Se aplican a toda
pantalla nueva y a la parte afectada de una pantalla modificada. Desarrollan RNF-UX-001,
RNF-UX-002, RNF-UX-003 y RNF-CON-001; no crean permisos ni funcionalidades de negocio.

Las ocho imágenes aportadas son referencias de principios. Sus colores, composiciones,
ejemplos comerciales y modo oscuro no se adoptan como identidad del producto. La paleta,
tipografía e identidad cultural conservan el estado provisional del
[sistema de diseño](SISTEMA-DISENO.md). La validación con usuarias sigue pendiente.

## Ocho reglas y cómo comprobarlas

| ID | Regla obligatoria | Criterio de revisión |
|---|---|---|
| UI-01 | Carga comprensible | Cuando se cargue contenido de forma asíncrona, usar un esqueleto que anticipe su estructura y reserve su espacio. Una acción breve puede mostrar progreso en su botón con texto. Evitar pantallas vacías, un spinner genérico para todo y esperas artificiales. |
| UI-02 | Adaptación real a cada pantalla | Reorganizar navegación, columnas, formularios y listados para móvil, tablet y escritorio. Comprobar 360 y 375 px, 768 px, 1280 y 1440 px, sin texto cortado, solapamientos ni desplazamiento horizontal accidental. No reducir toda la versión de escritorio a escala. |
| UI-03 | Jerarquía y contenido útil | Distinguir una acción principal por pantalla o paso, con secundarios subordinados. Título, datos y siguiente acción deben poder identificarse al escanear. Usar verbos concretos y textos breves; eliminar explicaciones de la propia interfaz, datos ficticios y adornos sin función. |
| UI-04 | Tokens compartidos | Resolver colores semánticos, tipografías, tamaños, espaciados, bordes, radios, sombras y foco con tokens comunes. Reutilizar los valores del sistema vigente; documentar una excepción necesaria antes de multiplicarla. No inventar una paleta o escala distinta por pantalla. |
| UI-05 | Componentes consistentes | La misma acción conserva nombre, estilo, tamaño relativo y comportamiento. Reutilizar botones, campos, avisos, tarjetas, tablas y modales existentes. Si un tema oscuro forma parte del alcance solicitado, definir y verificar todos sus tokens y estados; esta regla no solicita crearlo. |
| UI-06 | Accesibilidad comprobable | HTML semántico, etiquetas persistentes, nombres accesibles, alternativas para imágenes informativas, foco visible, teclado y contraste AA. No transmitir información solo con color o hover. Revisar zoom al 200 % y objetivos táctiles de al menos 44 × 44 px, criterio del proyecto. |
| UI-07 | Estados completos | Definir contenido normal, vacío, sin resultados por filtro, error y éxito, además de carga y falta de conexión cuando correspondan. Cada estado explica qué ocurrió y ofrece una salida válida para los permisos de la persona. Conservar los datos válidos al corregir o reintentar. |
| UI-08 | Interacción visible | Diseñar estados normal, hover, focus-visible, active y disabled cuando apliquen; añadir seleccionado, expandido, inválido y envío según el control. Ninguna acción depende solo de hover. Deshabilitar debe impedir la operación realmente y explicar la condición cuando no sea evidente. |

Los anchos son puntos de comprobación, no una obligación de crear un breakpoint en cada uno.
Las tablas que requieran comparar columnas pueden usar desplazamiento dentro de un contenedor
identificado, sin provocar desplazamiento de toda la página ni perder acciones esenciales.

### Carga y conectividad

- El esqueleto representa contenido pendiente, nunca datos ya recibidos ni una ausencia real.
  El HTML servido con contenido completo no necesita una carga ficticia.
- Marcar la región ocupada con `aria-busy` mientras carga; ocultar las formas decorativas del
  esqueleto a lectores de pantalla y ofrecer un anuncio breve de carga o resultado sin repetirlo.
- Al fallar, sustituir la carga por un error y una recuperación posible; evitar cargas infinitas
  sin explicación. Un reintento de escritura no debe duplicar registros.
- Un envío informa que está en curso y previene duplicados. Mostrar éxito solo tras la
  confirmación correspondiente; conservar la distinción entre guardado local y sincronizado
  de los recorridos offline aprobados.
- La animación es opcional, ligera y respeta `prefers-reduced-motion`. No agregar librerías,
  imágenes pesadas o dependencias de red para dibujar un esqueleto.

### Accesibilidad y errores

- Priorizar elementos nativos (`button`, `a`, `label`, campos) y su semántica. Un icono de
  acción sin texto necesita nombre accesible; una imagen decorativa usa alternativa vacía.
- Mantener el contraste del texto en todos sus estados aplicables: al menos 4.5:1 para texto
  normal y 3:1 para texto grande (24 px, o aproximadamente 18.67 px en negrita). La información
  visual necesaria para identificar controles y estados activos requiere 3:1 frente al color
  adyacente, con las excepciones del criterio. Fuentes:
  [W3C, contraste de texto](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) y
  [W3C, contraste no textual](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
- Asociar errores al campo y explicar cómo corregirlos; el placeholder no reemplaza la etiqueta.
  Si hay un resumen de errores tras enviar, llevar el foco allí y enlazar los campos afectados.
- Los mensajes de éxito y progreso se anuncian sin robar el foco innecesariamente. Si se usa
  un modal, comprobar entrada y retorno de foco, teclado y salida apropiada a la operación.

## Forma de trabajar y evidencia

Antes de implementar una pantalla, identificar su tarea, persona, contenido real, acción
principal y estados aplicables. Consultar los tokens y componentes existentes. Mantener la
organización de archivos de `zhud-aleli-codigo-legible`; esta guía no autoriza reorganizaciones.

Para cerrar una porción con cambios visuales, registrar una comprobación por cada fila:

| Comprobación | Evidencia mínima |
|---|---|
| Adaptación | Vista renderizada en los anchos de UI-02; sin pérdidas de contenido u operación. |
| Jerarquía y coherencia | Acción principal reconocible, textos necesarios, tokens y componentes reutilizados. |
| Estados de contenido | Estado normal y cada estado aplicable reproducido, incluido error y recuperación. |
| Interacción | Teclado, foco y estados de los controles modificados; doble envío cuando corresponda. |
| Accesibilidad | Contraste medido, nombres/etiquetas comprobados y zoom al 200 %. |
| Resultado funcional | Recorrido real con datos y permisos adecuados; sin errores nuevos de consola ni recursos rotos. |

Indicar **verificado**, **pendiente** o **no aplica**, con motivo para este último. Un estado
pendiente no se presenta como verificado. Una captura del caso ideal no acredita el resto.
La revisión visual no sustituye pruebas funcionales ni validación con usuarias; tampoco exige
rehacer pantallas ajenas al cambio. Esta actualización documental no acredita cumplimiento
de ninguna pantalla existente.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-28 | Ocho reglas solicitadas por el tesista y criterios de comprobación por pantalla. |
