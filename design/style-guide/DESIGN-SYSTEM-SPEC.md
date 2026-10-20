---
title: Especificación Técnica del Design System — Zhud Alelí
type: design-system-spec
status: consolidated
version: 1.0.0
updated: 2026-08-25
authorities:
  principles_and_ux: docs/ui/SISTEMA-DISENO.md
  visual_reference: design/zhud_aleli_exact_dashboard.html
  patterns_reference: design/dashboard-html/
  wireframes_reference: design/style-guide/WIREFRAMES.md
tags:
  - proyecto/tesis
  - tipo/especificacion
  - modulo/frontend
  - sistema/diseno
---

# Especificación Técnica del Design System — Zhud Alelí

## 1. Misión, Alcance y Reglas de Autoridad

### 1.1 Misión
Construir una base visual y de componentes modular, accesible, liviana y coherente sobre **Bootstrap 5** para la aplicación web de gestión organizacional y trazabilidad productiva del Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud y su unidad productiva Zhud Alelí.

### 1.2 Reglas de Autoridad
En caso de discrepancia visual, conceptual o de interacción, rige la siguiente jerarquía:
1. **`docs/ui/SISTEMA-DISENO.md`**: Autoridad para principios de UX, accesibilidad, tipografía, contrastes WCAG AA y criterios de diseño para usuarias reales.
2. **`design/zhud_aleli_exact_dashboard.html`**: Autoridad para la dirección visual, paleta cromática, radios, superficies sólidas, sombras suaves y proporciones del dashboard.
3. **`design/dashboard-html/`**: Referencia secundaria exclusiva para patrones de composición y layout; **no** constituye autoridad de identidad visual ni paleta cromática.
4. **`design/style-guide/WIREFRAMES.md`**: Especificación de flujos de interacción, orden de foco y composición de pantallas (ej. acceso, cambio de clave, dashboard inicial).

### 1.2.1 Identidad visual provisional

El color primario `#b32276` y la identidad visual derivada de
`design/zhud_aleli_exact_dashboard.html` constituyen la **IDENTIDAD VISUAL PROVISIONAL**
del proyecto y quedan pendientes de validación con la organización. La referencia visual
actual se conserva como base de implementación mientras no exista una decisión posterior;
no se sustituye por los colores provisionales de `docs/ui/SISTEMA-DISENO.md`.

La implementación futura debe consumir el color primario y sus valores derivados mediante
tokens `--za-*`. Los componentes deben referenciar esos tokens, nunca fijar directamente
estos valores, para que la identidad pueda sustituirse sin modificar los componentes.

### 1.3 Límites y Gobernanza
- **Sin invención cultural**: No se incorporan textiles, simbología indígena o decoraciones ancestrales sin previa validación y autorización explícita de la organización.
- **Sin invención de reglas de negocio**: Los componentes deben ser agnósticos y flexibles; no se predefinen lógicas comerciales, permisos o flujos productivos no aprobados.
- **No glassmorphism ni animaciones pesadas**: Toda superficie debe ser sólida (`#ffffff`, `#faf7fb`, `#f4edf5`) para garantizar rendimiento y legibilidad.

---

## 2. Principios de Experiencia e Interacción (UX)

1. **Una acción principal por pantalla**: La jerarquía visual debe destacar inequívocamente la acción primaria mediante `.btn-primary`.
2. **Reconocer antes que recordar**: Menús, etiquetas, migas de pan y estados deben ser explícitos y visibles.
3. **Móvil primero (Mobile-first desde 360 px)**: Ningún componente o tabla debe generar desplazamiento horizontal accidental en pantallas estrechas.
4. **Poco peso y funcionamiento local (`RNF-CON-001`)**: Arquitectura CSS optimizada sin dependencias externas obligatorias en producción. Las fuentes se servirán localmente desde `static/vendor/fonts/`.
5. **Errores recuperables**: Preservar siempre los datos válidos en formularios tras un fallo.
6. **Estado comprensible**: Todo estado debe comunicarse mediante la tríada `Texto + Icono + Color`. Nunca depender del color en solitario.
7. **Consistencia interactiva**: El mismo verbo y acción deben usar el mismo componente y posicionamiento en toda la suite.

---

## 3. Arquitectura de Tokens de Diseño

Todos los tokens se declaran bajo el namespace `--za-*` en `:root` y se mapean a las variables nativas de Bootstrap 5 (`--bs-*`). Los valores de la identidad visual provisional deben consumirse mediante estos tokens para permitir su sustitución sin modificar los componentes.

### 3.1 Color y Superficies

```css
:root {
  /* IDENTIDAD VISUAL PROVISIONAL: referencia de zhud_aleli_exact_dashboard.html */
  --za-primary: #b32276;
  --za-primary-hover: #961961;
  --za-primary-soft: #fbedf9;
  --za-primary-glow: rgba(179, 34, 118, 0.2);

  /* Acentos secundarios del Dashboard */
  --za-accent-purple: #8a2be2;
  --za-accent-purple-soft: #f2e6fc;
  --za-accent-blue: #4589ff;
  --za-accent-blue-soft: #eaf2ff;
  --za-accent-yellow: #f8be39;
  --za-accent-yellow-soft: #fef7e6;
  --za-accent-orange: #ff7a59;
  --za-accent-orange-soft: #ffefe8;
  --za-accent-cyan: #14b8a6;
  --za-accent-cyan-soft: #e5f9f6;

  /* Semántica de Error / Peligro */
  --za-danger: #b31a4f;
  --za-danger-soft: #fcecf2;

  /* Superficies sólidas */
  --za-bg-body: #faf7fb;         /* Fondo general pastel */
  --za-bg-surface: #ffffff;      /* Tarjetas y paneles */
  --za-bg-input: #f4edf5;        /* Fondo de campos y controles */
  --za-bg-hover: #f7eff8;        /* Hover en filas y elementos */

  /* Textos y Bordes */
  --za-text-title: #1f1422;      /* Encabezados y datos fuertes */
  --za-text-body: #594d5d;       /* Párrafos y contenido general */
  --za-text-secondary: #6b616d;  /* Texto secundario e informativo (AA verificado) */
  --za-text-muted: #9f93a3;      /* Exclusivo para elementos decorativos (Ratio < 4.5:1) */
  --za-border-light: #f0e6ef;    /* Delimitadores suaves */
}
```

### 3.2 Escala de Espaciado y Geometría

| Token | Valor | Aplicación |
| :--- | :--- | :--- |
| `--za-space-1` | `4px` | Micro-espacios, gaps de badges |
| `--za-space-2` | `8px` | Márgenes internos de botones, separadores |
| `--za-space-3` | `12px` | Paddings de celdas de tabla, gaps de filtros |
| `--za-space-4` | `16px` | Padding estándar de cards, separador de párrafos |
| `--za-space-5` | `20px` | Márgenes de secciones, espaciado de grids |
| `--za-space-6` | `24px` | Padding de tarjetas principales y modales |
| `--za-space-7` | `32px` | Separación mayor de bloques de página |
| `--za-radius-sm` | `10px` | Inputs, botones secundarios, thumbnails |
| `--za-radius-md` | `18px` | Tarjetas base, paneles de estadísticas, alertas |
| `--za-radius-lg` | `24px` | Modales, diálogos y contenedores mayores |
| `--za-radius-pill` | `999px` | Botones de acción, badges, date-pills |
| `--za-shadow-sm` | `0 4px 20px rgba(36, 17, 38, 0.03)` | Tarjetas en reposo, date-pills |
| `--za-shadow-hover`| `0 10px 30px rgba(179, 34, 118, 0.07)` | Tarjetas y botones interactivos en hover |
| `--za-shadow-md` | `0 20px 40px rgba(36, 17, 38, 0.12)` | Modales y diálogos emergentes |

### 3.3 Tipografía

- **Familia principal**: `Poppins`, con respaldo del sistema `"Segoe UI", system-ui, -apple-system, Roboto, sans-serif`.
- **Estrategia de carga**:
  - En entorno de diseño: Google Fonts CDN.
  - En producción Django (`RNF-CON-001`): Archivos `.woff2` locales servidos desde `static/vendor/fonts/`.
- **Jerarquía y Pesos**:
  - `h1` / Display: `700` (Bold), line-height `1.2`.
  - `h2`, `h3`, `h4`: `600` / `700`, color `--za-text-title`.
  - Body: `400` (Regular) / `500` (Medium), line-height `1.55`.
  - Controles y Botones: `600` (Semi-bold).
  - Metadatos y Badges: `500` / `600`, font-size `0.78rem` – `0.85rem`.

### 3.4 Interacción, Accesibilidad y Capas

- **Área táctil mínima (`--za-touch-target`)**: `44 × 44 px` para todo control interactivo en móviles y escritorio.
- **Foco visible accesible**:
  ```css
  :focus-visible {
    outline: 3px solid var(--za-primary) !important;
    outline-offset: 2px;
    border-radius: var(--za-radius-sm);
  }
  ```
- **Capas Z-Index (`--za-z-*`)**:
  - `base`: `1`
  - `sticky`: `10`
  - `dropdown`: `100`
  - `sidebar`: `1000`
  - `modal-backdrop`: `1040`
  - `modal`: `1050`
  - `toast`: `1090`

---

## 4. Estrategia de Integración con Bootstrap 5

El Design System no crea un framework CSS paralelo. Esta sección define únicamente estilos,
tokens y estructura de componentes; no decide la tecnología que implementará el comportamiento
interactivo. Personaliza y extiende Bootstrap 5 mediante tres niveles:
1. **Configuración de Variables Nativas**:
   ```css
   --bs-primary: var(--za-primary);
   --bs-primary-rgb: 179, 34, 118;
   --bs-danger: var(--za-danger);
   --bs-danger-rgb: 179, 26, 79;
   --bs-success: var(--za-accent-cyan);
   --bs-info: var(--za-accent-blue);
   --bs-warning: var(--za-accent-yellow);
   --bs-body-bg: var(--za-bg-body);
   --bs-body-color: var(--za-text-body);
   --bs-border-color: var(--za-border-light);
   --bs-border-radius: var(--za-radius-sm);
   ```
2. **Overrides Canónicos de Bootstrap**: Reescritura centralizada de `.btn`, `.form-control`, `.card`, `.table`, `.alert`, `.modal-content`, `.badge`.
3. **Clases Propias Namespace `.za-*`**: Componentes exclusivos de la aplicación que no existen de forma nativa en Bootstrap (ej. `.za-sidebar`, `.za-stat-card`, `.za-date-pill`, `.za-empty-state`).

---

## 5. Especificación de Componentes

### 5.1 App Shell y Navegación (`layout.html`)
- **`.za-shell`**: Contenedor maestro flex para la aplicación.
- **`.za-sidebar`**: Barra lateral fija de `90px` de ancho en escritorio, superficie `--za-bg-surface`, borde derecho `--za-border-light`.
  - Logo superior de 46×46px con radio de 14px (`.za-brand-logo`).
  - Navegación vertical `.za-nav-list` con botones cuadrados redondeados de 48×48px (`.za-nav-btn`), con estado activo (`.active`) sobre fondo `--za-primary-soft`.
  - Avatar de usuario inferior `.za-user-profile-btn` (44×44px, fondo púrpura suave).
  - **Comportamiento móvil (< 768px)**: La sidebar se convierte en una barra fija inferior (`bottom: 0`, altura `70px`), oculta el logo/avatar y distribuye los iconos horizontalmente (`order: 2`).
- **`.za-topbar`**: Encabezado superior flexible con título de vista y grupo de filtros/acciones.
- **`.za-date-pill`**: Control en píldora con fondo blanco, sombra suave y chevron para selección de periodos.

### 5.2 Botones y Acciones (`buttons.html`)
- **`.btn.btn-primary`**: Botón píldora (`--za-radius-pill`), fondo `--za-primary`, sombra `--za-primary-glow`, elevación de `-2px` en hover.
- **`.btn.btn-secondary`**: Fondo blanco, borde `--za-border-light`, texto `--za-primary`.
- **`.btn.btn-danger` / `.btn.btn-outline-danger`**: Acciones destructivas con confirmación visual.
- **`.btn.btn-link`**: Enlace textual subrayado accesible.
- **`.btn-loading`**: Estado deshabilitado con spinner giratorio en CSS que previene doble envío en operaciones transaccionales.

### 5.3 Formularios y Captura (`forms.html`)
- **`.form-label`**: Etiqueta persistente, peso `600`, color `--za-text-title`. Prohibido depender únicamente del `placeholder`.
- **`.form-control` / `.form-select`**: Superficie `--za-bg-input`, borde transparente en reposo, radio `--za-radius-sm` (10px). En foco: fondo blanco, borde `--za-primary` y halo suave `--za-primary-soft`.
- **Input Groups con Unidades**: Controles con sufijo integrado visible (`kg`, `h`, `$`, `%`) para pesajes y lotes productivos.
- **`.error-summary`**: Bloque superior de resumen de errores (fondo `--za-danger-soft`, borde lateral 5px `--za-danger`) con lista de enlaces a cada campo inválido y foco automático al fallar la validación.

### 5.4 Tarjetas, Métricas y Visualización (`cards.html`)
- **`.card` / `.za-card`**: Superficie `--za-bg-surface`, radio `--za-radius-md` (18px), sombra `--za-shadow-sm`.
- **`.za-stat-card` (Métricas de Dashboard)**: Fila con icono circular de 54×54px en fondo tintado suave (`.za-stat-icon`), número en negrita `1.55rem` y etiqueta descriptiva en `--za-text-secondary`.
- **`.za-chart-card`**: Tarjeta contenedora de gráfico de curva/área SVG con `tooltip-tag` flotante para valores destacados.
- **`.za-donut-widget`**: Contenedor para gráfico de distribución con valor central (`.donut-center-text`) y fila de leyendas semánticas con puntos de color (`.legend-item` + `.legend-dot`).
- **`.za-featured-item`**: Fila de producto/lote con icon-box suave de 58×58px, título, calificación/estado y precio/total.

### 5.5 Tablas y Datos (`table.html`)
- **`.table-wrap` / `.table-responsive`**: Contenedor con scroll horizontal protegido y bordes redondeados.
- **`.table.table-hover`**: Encabezados en mayúsculas pequeñas, texto `--za-text-secondary`, filas con hover suave `--za-bg-hover`.
- **`.za-table-item`**: Celda compuesta con thumbnail de 38×38px en fondo suave + texto principal.
- **`.za-pill-counter`**: Badge en píldora con fondo cian suave (`#e6f9f6`) y texto cian oscuro (`#0d9488`) para cantidades y conteos.

### 5.6 Badges y Estados (`tokens.html` / `feedback.html`)
- Estructura obligatoria: `.badge` + `.badge-dot` + texto.
- Variantes de fondo suave:
  - Marca: `.bg-brand-soft`
  - Éxito / Completado: `.bg-success-soft`
  - Información / En proceso: `.bg-info-soft`
  - Atención / Pendiente: `.bg-warning-soft`
  - Error / Peligro: `.bg-danger` (texto blanco)

### 5.7 Feedback y Modales (`feedback.html`)
- **`.alert.alert-success` / `.alert.alert-danger`**: Alertas con borde izquierdo de 5px, icono identificativo y texto con contraste verificado.
- **`.za-empty-state`**: Contenedor con borde discontinuo `--za-border-light`, icono central, título, explicación y botón de acción primaria.
- **`.modal-content`**: Ventana modal sobre fondo sólido blanco, esquinas redondeadas `--za-radius-lg` (24px), sombra profunda `--za-shadow-md`, botón de cierre circular `.btn-close`.
- **`.za-tab-pills`**: Selector de pestañas tipo píldora dentro de modales y filtros para conmutar categorías (ej. Evento / Tarea / Recordatorio).

---

## 6. Verificación de Accesibilidad (WCAG 2.1 AA)

### 6.1 Matriz de Contrastes

| Elemento / Combinación | Ratio | Estado WCAG AA | Regla de Uso |
| :--- | :---: | :---: | :--- |
| Blanco sobre `--za-primary` (`#b32276`) | **6.16:1** | Cumple | Botón primario y encabezados de marca |
| `--za-primary` sobre `--za-primary-soft` (`#fbedf9`) | **5.45:1** | Cumple | Badges y botones activos de navegación |
| `--za-text-title` (`#1f1422`) sobre Blanco | **17.78:1** | Cumple | Títulos y etiquetas clave |
| `--za-text-body` (`#594d5d`) sobre Blanco | **7.94:1** | Cumple | Párrafos y contenido general |
| `--za-text-secondary` (`#6b616d`) sobre Blanco | **5.91:1** | Cumple | Texto secundario y metadatos |
| `--za-text-secondary` sobre `--za-bg-body` (`#faf7fb`) | **5.56:1** | Cumple | Texto secundario sobre fondo general |
| Blanco sobre `--za-danger` (`#b31a4f`) | **6.61:1** | Cumple | Botones y badges de error/destructivos |
| `--za-text-muted` (`#9f93a3`) sobre Blanco | **2.93:1** | **Falla AA** | **Prohibido para texto informativo**; restringido a iconos decorativos |

---

## 7. Estructura de Archivos del Design System

```text
design/style-guide/
├── DESIGN-SYSTEM-SPEC.md    # Especificación consolidada (este documento)
├── WIREFRAMES.md             # Wireframes textuales de recorridos
├── tokens.html               # Catálogo visual de tokens y contraste
├── index.html                # Índice general de la guía de estilos
├── style.css                 # Tokens CSS + Overrides Bootstrap 5 + Clases .za-*
└── components/
    ├── layout.html           # Shell, Sidebar responsivo, Topbar y Layout general
    ├── buttons.html          # Botones, enlaces y estados de carga
    ├── forms.html            # Inputs, selects, validación y error-summary
    ├── cards.html            # Tarjetas base, Stat Cards, gráficos y listas
    ├── table.html            # Tablas responsivas y celdas enriquecidas
    └── feedback.html         # Alertas, modales, tab-pills y empty states
```

---

## 8. Registro de Decisiones y Contradicciones

### 8.1 Decisiones del sistema
1. **Bootstrap 5 como cimiento**: Se utiliza Bootstrap 5 mapeando sus variables SCSS/CSS a la arquitectura `--za-*`.
2. **Identidad visual provisional basada en `zhud_aleli_exact_dashboard.html`**: Se mantiene como referencia actual el color primario `#b32276`, las superficies sólidas pastel (`#faf7fb`) y los radios generosos (`18px`/`24px`), pendientes de validación con la organización y consumidos mediante tokens `--za-*`.
3. **Restricción de `--za-text-muted`**: Se estandariza `--za-text-secondary` (`#6b616d`) como el token obligatorio para metadatos informativos para asegurar cumplimiento WCAG AA.
4. **Sidebar híbrido responsivo**: Sidebar fijo de 90px en desktop que conmuta a barra de navegación inferior fija de 70px en pantallas < 768px.
5. **Componente de Error Summary obligatorio**: Se formaliza `.error-summary` para cumplir el principio de errores recuperables y accesibilidad en formularios Django.

### 8.2 Contradicciones Detectadas
1. **Divergencia cromática en referencias**: `design/dashboard-html/` utilizaba una paleta azul/púrpura (`#5864ff`) y tipografía `Plus Jakarta Sans`. Siguiendo la regla de autoridad, se descarta su estética y se conserva como referencia visual actual y provisional la dirección de `zhud_aleli_exact_dashboard.html` (`#b32276` y `Poppins`).
2. **Modal nativo vs Modal custom**: `zhud_aleli_exact_dashboard.html` implementaba un modal flotante con estructura HTML custom (`.modal-backdrop` y `.modal-box`), mientras que la spec del proyecto exige Bootstrap 5. Se consolida el uso de la estructura modal de Bootstrap (`.modal-dialog`, `.modal-content`) aplicando las clases visuales de la referencia.

### 8.3 Decisiones Pendientes (Criterio Humano / Tesista)
1. **Estrategia de iconos**: Determinar si se adoptará una librería SVG local unificada (ej. Feather / Lucide / Bootstrap Icons) o si se mantendrán SVGs inline/empaquetados en templates Django.
2. **Validación de identidad con la organización**: Confirmar si el tono magenta `#b32276` y el nombre visible reciben aprobación definitiva por parte del Comité de Mujeres de Zhud antes de fijarlos en código productivo.
3. **Tecnología de comportamiento interactivo fuera de alcance**: La decisión entre Bootstrap JavaScript, JavaScript vanilla, HTMX o Alpine.js se realizará posteriormente durante la implementación de la aplicación. Este Design System define únicamente estructura, apariencia, estados, responsive, accesibilidad y comportamiento esperado a nivel de interfaz.
