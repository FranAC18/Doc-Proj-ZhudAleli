# Constitución de ingeniería de Zhud Alelí

- **Estado**: [PROPOSED_OR_RATIFIED]
- **Versión**: [SEMANTIC_VERSION]
- **Propuesta/Ratificación**: [DATE]

## Principios centrales

### I. Valor validado antes que volumen de código

Cada funcionalidad resuelve un problema identificado para un actor y enlaza una fuente. Una
propuesta de IA no se convierte en requisito aprobado.

### II. Portabilidad del proceso

Requisitos, especificaciones, decisiones, tareas, pruebas y evidencias son artefactos abiertos
versionados. Cambiar de motor no cambia el alcance ni la definición de terminado.

### III. Calidad demostrable

Cada tarea funcional tiene criterios y pruebas proporcionales. Marcarla terminada requiere
verificación y evidencia; la falta de evidencia no impide que el tesista cierre el periodo
con resultado parcial. La declaración de un agente no es una prueba.

### IV. Arquitectura modular, cohesión e integridad de datos

Se usa un monolito modular Django con PostgreSQL y una unidad de entrega. Cada módulo agrupa
su responsabilidad y posee escrituras, invariantes y migraciones. HTTP, casos de uso/reglas
y datos se separan con mecanismos nativos; servicios/consultas solo cuando hay comportamiento
que los justifica. Dependencias, operaciones públicas y lecturas autorizadas son explícitas;
se evitan ciclos y se conservan relaciones justificadas. Se protegen transacciones comunes,
movimientos e historial. Incrementos verifican compatibilidad y recorridos afectados antes de
publicar. Complejidad adicional requiere necesidad y ADR; carga exige mediciones.

### V. Experiencia digna y accesible

La interfaz es móvil, clara, responsiva, ligera, navegable por teclado y de contraste AA. Se
valida con perfiles reales.

### VI. Trazabilidad académica continua

Cada requisito enlaza objetivo, fuente, sprint, diseño, código, prueba, evidencia y evaluación.
Obsidian muestra los mismos archivos de Git.

### VII. Control humano y privacidad

El tesista controla el cierre, reapertura y avance entre sprints, sin permiso de terceros ni
acta adicional. Registra fecha, resultado y pendientes en el estado, backlog o checkpoint que
ya use. El cierre no completa tareas ni aprueba requisitos o entregables. El tesista controla
alcance y Git. No se publican credenciales ni datos personales. Cambios irreversibles o externos
requieren autorización explícita.

## Restricciones técnicas

- Python 3.12, Django 5.2 LTS, PostgreSQL, Bootstrap 5 y MTV.
- Monolito modular y usuario personalizado desde el inicio.
- Autorización en backend y pruebas negativas.
- Modelos/migraciones nativos, `core` mínimo y ausencia de capas/apps vacías anticipadas.
- Versiones incrementales conjuntas con migraciones compatibles y recuperación verificable.
- Configuración y secretos fuera de Git.
- [ADDITIONAL_APPROVED_CONSTRAINTS]

## Puertas de calidad

1. Requisito validado.
2. Plan de datos, permisos, UX y pruebas.
3. Tareas acotadas y propiedad de archivos.
4. Implementación probada y revisada.
5. Cierre administrativo decidido por el tesista, con registro breve del resultado y los
   pendientes; no requiere una revisión previa, aprobación adicional ni acta formal.

El cierre del periodo puede ser parcial o bloqueado. La evidencia sigue siendo necesaria para
marcar tareas, criterios y entregables como terminados.

## Gobierno

[GOVERNANCE_AND_AMENDMENT_RULES]

**Versión**: [SEMANTIC_VERSION] | **Ratificada**: [RATIFICATION_DATE] | **Modificada**: [LAST_AMENDED_DATE]
