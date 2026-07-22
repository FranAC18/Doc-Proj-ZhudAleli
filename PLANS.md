# Planes de ejecución

Los planes de funcionalidades viven junto con su especificación en
`specs/<id-funcionalidad>/plan.md` y se generan con la plantilla activa de Spec Kit. Este
archivo define los mínimos para cualquier plan manual o trabajo transversal.

## Encabezado

- Objetivo verificable.
- ID de requisito y enlace a la especificación aprobada.
- Rama o worktree previsto.
- Estado y fecha.

## Contexto revisado

- Fuentes y requisitos.
- Código y pruebas inspeccionados.
- ADR relacionados.
- Supuestos y decisiones todavía abiertas.

## Diseño

- Actor y recorrido principal.
- Entidades, relaciones y reglas de negocio.
- Permisos y casos de denegación.
- Operaciones transaccionales y auditoría.
- Vistas, formularios y estados de interfaz.
- Impacto en rendimiento, conectividad y accesibilidad.

## Tareas

Cada tarea debe tener un ID, rutas exactas, dependencia, agente escritor y verificación
esperada. Marca como paralelas únicamente tareas que no compartan archivos ni estado.

## Verificación

- [ ] Criterios de aceptación cubiertos por pruebas.
- [ ] Permisos positivos y negativos revisados.
- [ ] `python manage.py check` cuando exista Django.
- [ ] Migraciones verificadas.
- [ ] Pruebas automatizadas relevantes.
- [ ] Recorrido visual responsivo revisado.
- [ ] `git diff --check` y diff completo revisados.
- [ ] Evidencia y trazabilidad actualizadas.

## Riesgos, reversión y pendientes

Documenta fallos posibles, mitigación, reversión de datos y cualquier decisión que requiera
confirmación humana antes de ejecutar.
