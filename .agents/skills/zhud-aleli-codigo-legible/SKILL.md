---
name: zhud-aleli-codigo-legible
description: Aplica las convenciones de nombres, estructura y comentarios del código de Zhud Alelí al crear, modificar o revisar código del proyecto.
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
