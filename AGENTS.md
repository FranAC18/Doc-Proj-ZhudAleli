# AGENTS.md — Zhud Alelí

## Misión

Construir una aplicación web funcional, clara y verificable para la gestión organizacional
y la trazabilidad productiva del Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud.
El arnés, los agentes y la documentación existen para servir a esa aplicación.

## Lectura obligatoria antes de trabajar

1. Lee este archivo.
2. Lee `.specify/memory/constitution.md`.
3. Lee `agents/tesis/AGENT.md`, `PROJECT_CONTEXT.md`, `KNOWLEDGE_POLICY.md` y
   `OBSIDIAN_POLICY.md`.
4. Lee `docs/00-inicio/00-dashboard.md` y el sprint actual.
5. Si existe una funcionalidad activa, lee todo su directorio en `specs/`, incluido
   `spec.md`, `plan.md` y `tasks.md`.
6. Inspecciona el código, las pruebas y el estado de Git antes de proponer cambios.

No cargues todo el repositorio sin necesidad. Empieza por estos índices y sigue sus enlaces.

## Fuentes de verdad

En caso de conflicto, aplica este orden y muestra la discrepancia:

1. Requisitos validados con la organización y evidencia de campo identificada.
2. Anteproyecto aprobado y decisiones confirmadas por el tesista/directora.
3. Especificaciones aprobadas en `specs/` y ADR aceptados en `docs/decisions/`.
4. Código, migraciones y pruebas del repositorio.
5. Documentación oficial vigente.
6. Propuestas del agente, siempre con estado `proposed`.

Una conversación, una inferencia o un borrador de IA nunca aprueban un requisito.

## Estado actual

La aplicación Django todavía no existe. Mientras el Sprint 0 no esté cerrado, solo se puede
trabajar en preparación, requisitos, diseño, evaluación del arnés y documentación. No se
debe presentar código de demostración como si fuera la aplicación funcional.

## Flujo obligatorio por funcionalidad

1. Especificar el problema, actor, fuente, alcance y criterios de aceptación.
2. Resolver las ambigüedades que cambien alcance, seguridad, datos o experiencia de uso.
3. Obtener confirmación humana y cambiar el estado de la especificación.
4. Diseñar arquitectura, datos, permisos, interfaz y estrategia de pruebas.
5. Dividir el trabajo en tareas pequeñas con rutas y criterios verificables.
6. Implementar una porción vertical mínima en una rama o worktree propio.
7. Ejecutar verificaciones, revisar permisos y revisar el diff.
8. Registrar evidencia, actualizar trazabilidad y documentar pendientes.
9. Solicitar confirmación antes de `commit`, `push` o `merge`.

No ejecutes `speckit-implement` sobre una especificación sin aprobar.

## Trabajo multiagente

Usa agentes especializados únicamente cuando el usuario autorice trabajo multiagente en la
solicitud actual y existan frentes realmente independientes. Roles disponibles en
`.codex/agents/`:

- `requirements`: analiza fuentes y redacta propuestas; no aprueba requisitos.
- `architect`: revisa arquitectura, datos y decisiones; no implementa.
- `ux`: diseña y revisa flujos e interfaz; no inventa identidad visual aprobada.
- `implementer`: modifica solo la tarea y los archivos asignados.
- `reviewer`: revisa comportamiento, seguridad, pruebas y trazabilidad sin editar.

Reglas de coordinación:

- Un solo agente escritor por archivo y por worktree.
- El agente raíz integra resultados y es el único que actualiza dashboard, sprint y matriz
  global durante una ejecución multiagente.
- Los agentes hijos reciben el ID de requisito, la tarea, las rutas permitidas y la prueba
  esperada; no se les entrega un objetivo abierto como “hacer todo el módulo”.
- No hay delegación recursiva ni fusiones automáticas.
- Un reporte de agente no sustituye pruebas ni revisión del diff.

## Arquitectura de implementación

- Stack aprobado: Python, Django, PostgreSQL, Bootstrap 5 y arquitectura MTV.
- Estilo: monolito modular; cada app representa una capacidad del dominio.
- Usa vistas, formularios y plantillas Django como primera opción. JavaScript adicional debe
  resolver una interacción concreta y conservar degradación razonable.
- Crea un usuario personalizado antes de la primera migración de producción.
- Usa transacciones para operaciones que cambien varias entidades.
- Para inventario, lotes y pesajes registra movimientos; no reemplaces historia con un
  número mutable sin evidencia.
- Las reglas de autorización viven en backend y tienen pruebas negativas.
- No agregues capas, repositorios, microservicios, colas o una SPA sin necesidad demostrada
  y ADR aceptado.

## Interfaz y experiencia

- Diseña primero para móvil y conectividad limitada.
- Usa Bootstrap 5 con componentes propios y tokens consistentes; evita páginas genéricas de
  administración como interfaz principal para las usuarias.
- Controles táctiles amplios, texto claro, etiquetas visibles e icono acompañado de texto.
- Contraste AA, navegación por teclado y mensajes de error que indiquen cómo corregir.
- No uses solo color para comunicar estado.
- Prueba los recorridos críticos con los perfiles reales y registra evidencia de validación.

## Git y GitHub

- `main` es estable. Trabaja en una rama por tarea o sprint.
- Revisa `git status`, rama y diff antes y después del cambio.
- No hagas `commit`, `push`, `merge`, `rebase`, force-push ni borres historia sin solicitud
  explícita del tesista.
- Usa la identidad Git del tesista. No agregues `Co-authored-by` de IA salvo solicitud.
- No cambies `user.name` ni `user.email`.
- No mezcles archivos ajenos a la tarea ni reviertas cambios existentes del usuario.
- Nunca incluyas secretos, bases locales, datos personales o artefactos generados.

## Verificación

Ejecuta solo comandos que correspondan al estado real del repositorio y reporta el resultado.
Cuando exista la aplicación Django, el mínimo será:

```bash
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

Para el laboratorio opcional actual:

```bash
pytest -q tools/agent-lab/tests
```

Antes de cerrar cualquier tarea ejecuta además `git diff --check` cuando haya un repositorio
Git disponible.

## Obsidian y tesis

La raíz es también el vault. Guarda conocimiento estable en Markdown, con YAML y Wikilinks.

- Propuestas de requisito: `docs/requirements/proposals/`, estado `proposed`.
- Especificación aprobada y plan: `specs/<id-funcionalidad>/`.
- Decisiones: `docs/decisions/` mediante ADR.
- Sesiones y checkpoints: `docs/bitacora/`.
- Evidencias: `docs/evidence/`, sin datos personales innecesarios.
- Trazabilidad global: `docs/traceability/MATRIZ-TRAZABILIDAD.md`.

No sobrescribas notas aprobadas. Si un nombre ya existe, crea una versión identificable o
detén la escritura y solicita decisión.

Interpreta `checkpoint`, `pausa aquí`, `cierra sesión` y `terminamos` según
`agents/tesis/OBSIDIAN_POLICY.md`.

## Definición de terminado

Una tarea solo está `completed` cuando:

- satisface criterios de aceptación identificados;
- tiene pruebas relevantes, incluidas autorización y casos negativos cuando aplican;
- migraciones y validaciones pasan;
- la interfaz fue revisada en los tamaños acordados;
- el diff no contiene cambios accidentales;
- documentación, ADR y matriz de trazabilidad están alineados;
- existe evidencia enlazada y no quedan bloqueos ocultos.
