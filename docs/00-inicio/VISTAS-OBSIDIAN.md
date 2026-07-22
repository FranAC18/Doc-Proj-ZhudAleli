---
title: Vistas recomendadas de Obsidian
type: guide
tags:
  - proyecto/tesis
  - tipo/guia
---

# Vistas recomendadas de Obsidian

## Plugins principales que conviene activar

- Daily notes.
- Templates.
- Properties view.
- Search.
- Bookmarks.
- Bases, si está disponible en tu versión.
- Graph view, de forma opcional.

Estas funciones permiten registrar notas diarias, reutilizar plantillas, buscar por
propiedades y construir vistas tipo tabla sin instalar extensiones externas.

## Vistas que crearemos después de probar el flujo

### Tareas activas

Filtrar notas con:

```yaml
type: task
status: in-progress
```

### Bloqueos

Filtrar:

```yaml
status: blocked
```

### Requisitos pendientes

Filtrar:

```yaml
type: requirement
status: proposed
```

### Avances parciales

Filtrar:

```yaml
type: checkpoint
status: partially-complete
```

### Errores por módulo

Filtrar:

```yaml
type: error
module: asistencia
```

La vista puede mostrar también `sprint`, `severity`, `related` y `date` para que el error
no quede aislado del trabajo que lo originó.

Bases puede mostrar, editar, ordenar y filtrar notas mediante sus propiedades; por eso
será la primera opción para un tablero de avance sin duplicar información. [Documentación
oficial de Bases](https://obsidian.md/help/bases)
