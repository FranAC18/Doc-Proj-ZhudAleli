# Constitución de ingeniería de Zhud Alelí

- **Estado**: Aprobada por el tesista
- **Versión**: 0.1.0
- **Propuesta**: 2026-07-21
- **Ratificación**: 2026-07-21 por el tesista

## Principios centrales

### I. Valor validado antes que volumen de código

Cada funcionalidad debe resolver un problema identificado para un actor real y enlazar una
fuente. Una propuesta de IA no se convierte en requisito ni en alcance aprobado. No se
implementan reglas organizativas, fórmulas, permisos o reportes que dependan de decisiones de
campo pendientes. Cuando falte una decisión material, la funcionalidad permanece en borrador
o bloqueada.

### II. Portabilidad del proceso, no dependencia del modelo

Requisitos, especificaciones, decisiones, tareas, pruebas y evidencias deben ser Markdown,
código o datos abiertos versionados en Git. Ningún comportamiento esencial depende del
historial privado de un proveedor. `AGENTS.md` es el contrato común; los directorios de cada
motor solo lo adaptan a su interfaz. Cambiar de Codex a Kimi o GLM no puede cambiar el alcance
aprobado ni la definición de terminado.

### III. Calidad demostrable

Toda tarea funcional debe tener criterios de aceptación y pruebas proporcionales al riesgo.
Los permisos requieren casos positivos y negativos. Los cambios de esquema incluyen
migraciones y verificación. “El agente dijo que funciona” no es evidencia. El cierre exige
comandos ejecutados, resultado, revisión del diff y vínculo a evidencia reproducible.

### IV. Arquitectura simple e integridad de datos

La aplicación será un monolito modular Django con PostgreSQL y límites de dominio claros.
Se prefiere la solución nativa y directa del framework. Operaciones que afectan varias
entidades usan transacciones. Inventario, pesajes, secado y lotes conservan movimientos e
historial según el requisito; no se destruye trazabilidad actualizando totales sin respaldo.
Microservicios, SPA, colas y capas genéricas requieren ADR y una necesidad comprobada.

### V. Experiencia digna y accesible

La interfaz se diseña para móvil, conectividad limitada y distintos niveles de alfabetización
digital. Debe ser consistente, clara, responsiva, navegable por teclado y con contraste AA.
Los estados usan texto además de color; los formularios explican errores y recuperación. La
interfaz principal no será el Django Admin y se validarán recorridos con usuarias reales.

### VI. Trazabilidad académica continua

Cada requisito aprobado enlaza objetivo específico, fuente, sprint, diseño, código, prueba,
evidencia y resultado de evaluación ISO/IEC 25010:2023 cuando corresponda. La documentación
se actualiza durante el desarrollo, no al final. Obsidian visualiza los mismos archivos del
repositorio; no crea una segunda fuente de verdad.

### VII. Control humano, privacidad y cambios reversibles

El tesista conserva control de alcance, aprobación, Git y publicación. Ningún agente hace
`commit`, `push`, `merge`, reescritura de historia ni acciones irreversibles sin solicitud
explícita. No se versionan credenciales ni datos personales innecesarios. Las afirmaciones de
cumplimiento normativo necesitan fuente oficial y validación humana.

## Restricciones técnicas

- Python 3.12 y Django 5.2 LTS como base propuesta para iniciar la aplicación.
- PostgreSQL en desarrollo integrado y producción; SQLite solo puede usarse en pruebas
  unitarias que no oculten diferencias relevantes.
- Bootstrap 5, plantillas Django y JavaScript progresivo mínimo.
- Apps de dominio previstas: `accounts`, `planning`, `attendance`, `traceability`, `reports`
  y `public_site`, más un `core` transversal pequeño.
- Usuario Django personalizado antes de la primera migración estable.
- Configuración por entorno y secretos fuera de Git.
- CI con comprobación Django, migraciones, pruebas, lint y revisión de artefactos cuando
  existan esas herramientas.

## Puertas del flujo

1. **Puerta de requisito**: fuente, actor, alcance, criterios y dudas materiales resueltas.
2. **Puerta de plan**: datos, permisos, interfaz, pruebas, riesgos y trazabilidad definidos.
3. **Puerta de implementación**: tareas con rutas y un escritor asignado.
4. **Puerta de revisión**: pruebas pasan, diff revisado y hallazgos críticos resueltos.
5. **Puerta de cierre**: evidencia, matriz y documentación actualizadas; aprobación humana
   cuando el sprint o requisito la exija.

Si una puerta falla, el estado es `blocked` o `partially-complete`, nunca `completed`.

## Gobierno

- Esta constitución guía los planes y revisiones una vez aprobada.
- Un cambio de principio requiere ADR, motivo, impacto y aprobación del tesista.
- Los cambios de alcance o metodología que afecten el anteproyecto también requieren revisión
  de la directora.
- Las instrucciones específicas pueden añadir restricciones, pero no rebajar estas puertas.
- Los agentes deben señalar una contradicción en vez de escoger silenciosamente una fuente.

**Versión**: 0.1.0 | **Propuesta**: 2026-07-21 | **Última modificación**: 2026-07-21
