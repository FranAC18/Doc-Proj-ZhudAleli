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

| Token | Valor provisional | Uso |
|---|---|---|
| `--color-brand-700` | `#285B4D` | encabezados, acciones principales |
| `--color-brand-100` | `#E6F1EC` | fondos de énfasis suave |
| `--color-accent-500` | `#C8872B` | detalles y estados de atención |
| `--color-surface` | `#FFFDF8` | fondo cálido principal |
| `--color-text` | `#17231F` | texto principal |
| `--color-muted` | `#5E6D67` | texto secundario con contraste verificado |
| `--color-danger` | `#B42318` | errores y acciones destructivas |

Antes de consolidarlos se verificará contraste WCAG AA y se compararán con la identidad real.
La tipografía inicial será la pila del sistema para evitar descargas y mejorar velocidad.

## Shell responsivo propuesto

- Encabezado con nombre del sistema, perfil y salida.
- Navegación inferior compacta en móvil para tres a cinco destinos prioritarios.
- Barra lateral en escritorio para los mismos destinos, sin duplicar nombres.
- Título, contexto y acción principal en la zona superior de cada vista.
- Contenido en un ancho legible; tablas grandes cambian a tarjetas o filas resumidas en móvil.

La navegación concreta depende de la matriz de permisos y se prueba con cada perfil.

## Componentes mínimos

- Botones primario, secundario, enlace y destructivo con estados focus/disabled/loading.
- Campos de texto, fecha, hora, número, selección y ayuda contextual.
- Resumen de errores al inicio y error junto al campo.
- Tarjeta de tarea/actividad/lote con metadatos esenciales.
- Badge de estado con texto e icono.
- Tabla responsiva con filtros y alternativa legible en móvil.
- Estado vacío con explicación y acción posible.
- Confirmación para acciones sensibles, indicando consecuencia.
- Toast solo para confirmaciones no críticas; los errores importantes permanecen visibles.
- Breadcrumb cuando exista profundidad real, no por costumbre.

Cada componente se implementa una vez en `templates/components/` y se documenta con ejemplos
de uso. No se crean variantes locales sin revisar si el componente común puede resolverlas.

## Formularios

- Etiqueta persistente sobre cada campo; placeholder solo como ejemplo.
- Unidad junto al valor (`kg`, `h`, `%`) y reglas de redondeo visibles.
- Orden que siga el proceso real de trabajo.
- Valores predeterminados únicamente cuando sean seguros y comprensibles.
- Botón principal describe la acción: “Registrar asistencia”, no “Aceptar”.
- En error, foco en el resumen y enlaces a campos inválidos.
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
