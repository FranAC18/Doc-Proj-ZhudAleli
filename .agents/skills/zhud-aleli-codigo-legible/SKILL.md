---
name: zhud-aleli-codigo-legible
description: Aplica la organización modular de backend y frontend, los nombres y los comentarios de Zhud Alelí al crear, modificar o revisar código, plantillas y recursos de la app Django.
---

# Código legible de Zhud Alelí

Aplica esta skill al trabajar con código de producto, pruebas, plantillas y recursos fuente de
`App-zhudaleli`. Su objetivo es que el tesista pueda localizar una responsabilidad, entenderla
sin depender del historial de conversación y pedir cambios posteriores con facilidad.

## Antes de editar

1. Confirma la raíz Git de la app y la del repositorio general; consulta en el vault el requisito,
   sprint y criterios aplicables según `AGENTS.md`.
2. Revisa los archivos vecinos y sigue sus convenciones cuando sean compatibles con estas reglas.
   Evita crear otro archivo si la responsabilidad ya tiene un módulo claro.
3. Limita el cambio a la porción solicitada. No hagas renombres masivos ni refactorizaciones que
   dificulten revisar qué cambió.
4. Identifica el módulo propietario y comprueba cómo Django descubre sus modelos, plantillas y
   estáticos. La convención aprobada se aplica mediante cambios funcionales y verificables;
   una tarea sobre reglas o documentación no autoriza por sí sola a trasladar código existente.

## Organización modular aprobada

El tesista aprobó esta convención el 2026-10-28. La referencia arquitectónica es
[`ARQUITECTURA-OBJETIVO.md`](../../../docs/architecture/ARQUITECTURA-OBJETIVO.md), incluida su
adenda de esa fecha. La aplicación conserva Django MTV, PostgreSQL y una entrega conjunta.

- Organiza primero por módulo de negocio en `apps/<modulo>/`. Cada módulo reúne sus datos,
  operaciones, permisos, presentación y pruebas. Una pantalla nueva se incorpora a su módulo;
  no exige otra app Django.
- Conserva el backend nativo dentro de cada app. No introduzcas una carpeta global `backend/`
  que concentre reglas de todos los módulos ni muevas modelos o migraciones fuera de sus puntos
  de descubrimiento para lograr simetría con el frontend.
- Cada módulo controla las escrituras y las invariantes de sus entidades. La colaboración
  entre módulos usa operaciones públicas y lecturas autorizadas, con dependencias explícitas
  y sin ciclos. Conserva las relaciones que protegen la integridad de datos.
- Crea archivos y capas cuando exista una responsabilidad concreta. No anticipes apps,
  paquetes, servicios, repositorios genéricos sobre el ORM ni un `core` que acumule reglas.

## Backend: ubicar cada responsabilidad

| Ubicación | Responsabilidad |
|---|---|
| `models.py` o `models/` | Entidades, relaciones, restricciones e invariantes locales. |
| `forms.py` | Interpretación y validación de entrada de formularios; configuración de campos. |
| `views.py` | Coordinación HTTP, selección de formularios y operaciones, respuesta o redirección. |
| `services.py`, cuando haga falta | Operaciones con reglas, reutilización o coordinación que justifican su extracción. |
| `urls.py` | Rutas y nombres públicos de la app. |
| `migrations/` | Evolución del esquema mediante los mecanismos nativos de Django. |
| `tests/` | Pruebas del módulo, sus autorizaciones y recorridos. |

- Un recorrido pequeño puede usar las herramientas nativas de Django sin pasar siempre por
  un servicio. Extrae una operación cuando haya reglas o reutilización reales.
- Las operaciones de negocio reutilizables reciben datos y una identidad confiable; evitan
  depender de `HttpRequest`, plantillas o respuestas HTTP. Los adaptadores de autenticación
  pueden usar `request` cuando lo requiere el contrato de Django.
- Mantén autorización y validaciones de negocio en backend, también para entradas alternativas.
  El frontend puede ayudar a validar, pero no decide permisos ni garantiza integridad.
- Coordina en una transacción las escrituras que deban completarse juntas y considera los
  bloqueos necesarios. Un cambio visual no altera esas garantías.
- Añade `queries.py` para consultas complejas o reutilizadas, y `policies.py` para autorización
  reutilizable, solo cuando el comportamiento lo justifique; conserva los permisos nativos útiles.
- Si un archivo crece, divide por responsabilidades, sin umbrales arbitrarios de líneas.
  Al convertir `models.py` en `models/`, importa explícitamente los modelos en `__init__.py`
  y verifica el registro de la app, las migraciones y los consumidores existentes.
- Cuando se implemente una entrada offline aprobada, reutiliza la operación del módulo y
  valida identidad, permisos y reglas en servidor al sincronizar.

## Frontend: una carpeta por pantalla dentro de su módulo

La ubicación objetivo es `apps/<modulo>/frontend/<modulo>/<pantalla>/`. El segundo nombre del
módulo identifica las plantillas y evita colisiones; no representa copias de archivos.
Ejemplo de una pantalla con recursos propios:

```text
apps/accounts/
├── models.py
├── forms.py
├── views.py
├── urls.py
├── migrations/
├── tests/
└── frontend/
    └── accounts/
        └── login/
            ├── login.html
            └── recursos/
                ├── login.css
                └── imagenes/
```

- Reúne el HTML y sus recursos exclusivos bajo la carpeta de la pantalla. `recursos/` delimita
  los archivos públicos; solo se crea si existe contenido. Conserva nombres públicos y de
  archivos existentes cuando sean compatibles con la tarea; usa español para nombres propios nuevos.
- Un CSS o JS propio puede estar directamente en `recursos/`. Crea `css/` o `js/` dentro de
  `recursos/` cuando agrupen varios archivos con responsabilidades claras. Mantén las reglas
  adaptables junto a los componentes que modifican y conserva el orden de la cascada.
- No crees `login.js`, un CSS ni carpetas vacías para completar un árbol. Tampoco fragmentes
  unas pocas reglas relacionadas en archivos separados sin mejorar su responsabilidad.
- Lo usado por varias pantallas tiene un único propietario compartido: estructura HTML en
  `templates/base.html` y `templates/components/`; estilos y comportamientos comunes en
  `static/compartido/`; identidad en `static/brand/`; PWA en `static/pwa/`; terceros en
  `static/vendor/`. No copies estos recursos en cada pantalla ni mezcles reglas de negocio allí.
- La base carga lo general; cada pantalla declara los estilos y scripts que utiliza mediante
  bloques de plantilla. Conserva JavaScript progresivo y el funcionamiento del formulario.

### Descubrimiento y transición

- Configura las raíces de plantillas y los directorios estáticos con prefijos de módulo y
  pantalla, preferentemente con los mecanismos nativos de Django. Comprueba las rutas que
  realmente resuelven los cargadores y los buscadores; la existencia física no basta.
- Publica únicamente los directorios `recursos/` y los estáticos compartidos. No registres todo
  `frontend/` como estático: las plantillas deben procesarse en servidor y quedar fuera de
  los recursos públicos, tanto en desarrollo como durante `collectstatic`.
- El árbol existente `templates/<modulo>/` y `static/<modulo>/` puede coexistir durante una
  transición. Completa una pantalla con sus consumidores y configuración antes de continuar;
  conserva una sola fuente activa por plantilla o recurso y evita rutas ambiguas.
- No generes una pantalla en la ubicación objetivo sin configurar y verificar su descubrimiento
  en la misma porción de implementación. No conviertas un ajuste acotado en una migración masiva.
- Al mover archivos, actualiza vistas, referencias estáticas, enlaces CSS, pruebas y recursos
  precargados de la PWA. Actualiza su versión de caché cuando cambie ese conjunto y conserva
  la exclusión de páginas privadas y formularios de acceso.

## Idioma y nombres

- Usa español para los nombres nuevos del dominio y del código propio: archivos de dominio,
  funciones, variables, clases, constantes, comentarios y textos de interfaz.
- Escribe identificadores sin espacios, tildes ni `ñ`, para facilitar su uso en herramientas y
  rutas. Mantén la ortografía normal del español en comentarios, documentación y textos visibles.
- Usa `snake_case` para archivos Python, funciones, métodos propios y variables; `PascalCase` para
  clases propias; y `UPPER_SNAKE_CASE` para constantes.
- Elige nombres concretos que expresen el concepto del requisito. Evita abreviaturas locales,
  traducciones distintas del mismo término y nombres genéricos como `utils.py` si el archivo puede
  nombrar su responsabilidad.
- Conserva los nombres requeridos por Django, Python, Bootstrap, paquetes, protocolos y contratos
  externos. Por ejemplo, no traduzcas `models.py`, `views.py`, `urls.py`, `clean()`, `dispatch()`,
  `form_valid()` ni campos cuyo nombre forme parte de una integración.
- Conserva los nombres existentes de rutas, modelos, campos y símbolos públicos salvo que la tarea
  autorice el cambio y se hayan revisado sus importaciones, datos y consumidores. No renombres un
  identificador solo para traducirlo.

## Estructura y funciones

- Agrupa cada función y archivo según una responsabilidad identificable dentro del módulo dueño de
  esa operación. No crees capas, módulos o abstracciones vacías para anticipar necesidades futuras.
- Mantén las funciones enfocadas. Extrae una operación cuando mejore la lectura, evite duplicación
  real o facilite probar una regla; no dividas código mecánicamente.
- Prefiere flujo explícito y nombres comprensibles a lógica compacta que obligue al lector a
  reconstruir varios pasos mentalmente.
- Para cada función propia no trivial, especialmente reglas de negocio y operaciones reutilizables,
  añade un docstring breve en español que explique su propósito. Incluye condiciones, efectos o
  garantías solo cuando no sean evidentes por la firma y el cuerpo.
- No añadas docstrings vacíos ni comentarios a adaptadores triviales cuando el nombre ya describe
  claramente su única acción.

## Comentarios

- Escribe comentarios breves en español y nunca uses emojis.
- Explica por qué existe una decisión, una invariante, una protección, una restricción de
  concurrencia o un comportamiento poco obvio. En funciones no triviales, el docstring puede
  explicar qué hace; un comentario junto a una línea explica por qué ese detalle es necesario.
- No narres cada instrucción ni repitas el nombre de la variable en otras palabras. Si el código
  requiere comentarios para seguir una secuencia larga, simplifica o separa la lógica cuando el
  cambio lo permita.
- Mantén los comentarios sincronizados con el comportamiento. Elimina o corrige los que queden
  falsos después de un cambio.
- Deja decisiones extensas, requisitos y procedimientos en la fuente documental correspondiente,
  no en comentarios de implementación.

## Al terminar

Revisa el diff y pregúntate si alguien que no conoce esta conversación puede encontrar el archivo
por su nombre y entender cada función importante a partir de su nombre, firma y docstring. Asegura
que los comentarios expliquen decisiones no obvias, que el idioma sea consistente y que no se hayan
introducido emojis o renombres fuera del alcance. Informa al tesista qué archivos y
responsabilidades cambiaron con palabras sencillas.

En cambios de organización, revisa además lo afectado:

- Backend: importaciones, nombres públicos, registro de modelos, permisos, transacciones y
  compatibilidad de migraciones y datos. Ejecuta los controles Django y pruebas pertinentes;
  comprueba migraciones pendientes si cambian modelos, importaciones o descubrimiento.
- Frontend: renderizado de las pantallas, resolución de sus recursos y `collectstatic` con
  destino aislado cuando cambie su configuración. Verifica que los HTML fuente no se publiquen
  como estáticos. Comprueba estilos y comportamiento en móvil y escritorio si se trasladan
  estilos, plantillas o scripts; revisa caché y alternativa offline si afecta a la PWA.
- Revisa el diff y ejecuta `git diff --check`. Separa hechos verificados de pendientes; no
  presentes la convención aprobada como una reorganización ya aplicada.
