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

| Token | Valor | Uso |
|---|---|---|
| `--primary` | `#B32276` | Marca, acciones principales, enlaces |
| `--primary-hover` | `#961961` | Hover y foco de acciones principales |
| `--primary-soft` | `#FBEDF9` | Fondos de énfasis suave de marca |
| `--accent-purple` | `#8A2BE2` | Acento secundario (detalles) |
| `--accent-blue` | `#4589FF` | Estado informativo |
| `--accent-yellow` | `#F8BE39` | Estado de atención (indicadores no textuales o texto oscuro) |
| `--accent-orange` | `#FF7A59` | Estado de advertencia |
| `--accent-cyan` | `#14B8A6` | Estado de éxito (indicadores) |
| `--bg-body` | `#FAF7FB` | Fondo general de página |
| `--bg-surface` | `#FFFFFF` | Tarjetas y superficies principales |
| `--bg-input` | `#F4EDF5` | Fondo de campos de formulario |
| `--border-light` | `#F0E6EF` | Bordes suaves |
| `--text-title` | `#1F1422` | Títulos y encabezados principales |
| `--text-body` | `#594D5D` | Texto general de párrafos |
| `--text-secondary` | `#6B616D` | Texto secundario accesible (contraste AA verificado) |
| `--text-muted` | `#9F93A3` | Solo decorativo (contraste < 4.5:1, no para texto informativo) |
| `--danger` | `#B31A4F` | Errores y acciones destructivas |
| `--danger-soft` | `#FCECF2` | Fondo de alertas de error |

La identidad visual es una **propuesta** tomada de la maqueta de referencia y validada con los componentes de `design/style-guide/`. Se confirmará con la organización antes de fijarla como definitiva.

### Tipografía y rendimiento

- **Familia principal**: `Poppins`, con respaldo en `"Segoe UI", system-ui, -apple-system, Roboto, sans-serif`.
- **Rendimiento y funcionamiento sin conexión (`RNF-CON-001`)**: En producción y despliegue Django, las fuentes deben servirse localmente desde `static/vendor/fonts/` (o la carpeta local correspondiente) para eliminar dependencias obligatorias hacia Google Fonts CDN y soportar conectividad inestable.

### Geometría, espaciado y objetivos táctiles

- **Espaciado (`--space-1..7`)**: 4, 8, 12, 16, 20, 24, 32 px.
- **Radios (`--radius-sm/md/lg/pill`)**: 10, 18, 24, 999 px.
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
