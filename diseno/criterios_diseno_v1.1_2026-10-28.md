---
titulo: Criterios obligatorios de diseño de la interfaz
version: "1.1"
fecha: 2026-10-28
autor: Codex
estado: reglas-solicitadas-por-tesista-revision-academica-pendiente
fuentes: constitucion-2.0.0; CAT-REQ-001-v1.3; instruccion-expresa-tesista-2026-10-28
revision_usuarias: pendiente
publicacion: pendiente-de-confirmacion
---

# Criterios de diseño de la interfaz — v1.1

Esta edición conserva los criterios de [v1.0](criterios_diseno_v1.0_2026-10-12.md) y
precisa las ocho pautas exigidas por el tesista el 2026-10-28. Desarrolla RNF-UX-001 a
003 y RNF-CON-001. La identidad visual sigue siendo provisional; el modo oscuro solo
se diseña si forma parte del alcance solicitado. No se acredita cumplimiento de pantallas
ni validación con usuarias por registrar estas reglas.

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

## Verificación por pantalla

Registrar vistas móviles (360 y 375 px), tablet (768 px) y escritorio (1280 y 1440 px),
estados aplicables, jerarquía, coherencia de componentes, teclado, foco, contraste medido,
zoom al 200 % y resultado del recorrido real. Marcar cada comprobación como verificada,
pendiente o no aplicable con motivo. Reproducir errores y recuperación; conservar datos
válidos y prevenir doble envío. La carga no se simula si el contenido ya está disponible.
El éxito requiere confirmación de la operación; el guardado local y la sincronización
se distinguen en los recorridos offline habilitados.

Las imágenes informativas tienen alternativa y las decorativas alternativa vacía; los
controles tienen etiqueta o nombre accesible. Contraste mínimo de texto normal 4.5:1 y
texto grande 3:1; las señales necesarias de controles y estados activos, 3:1 frente al
color adyacente, con las excepciones de los criterios del W3C:
[texto](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) y
[controles](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html).
El proyecto conserva objetivos táctiles de al menos 44 × 44 px.

## Trazabilidad y estado

HT-GEN-004 incorpora estos patrones; las HU con interfaz los aplican en la porción que
se implemente o modifique. SB-S1-04 mantiene su corte histórico y SB-S2-02 conserva su
avance operativo. No se alteran prioridades, estimaciones, responsables, fechas, permisos
ni estados de terminación. Revisión académica, validación con usuarias y publicación pendientes.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| 1.0 | 2026-10-12 | Criterios iniciales; identidad visual pendiente. |
| 1.1 | 2026-10-28 | Ocho pautas expresas del tesista con comprobaciones por pantalla. |
