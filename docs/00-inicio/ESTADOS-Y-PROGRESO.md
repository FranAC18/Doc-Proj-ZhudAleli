---
title: Estados y progreso del proyecto
type: guide
tags:
  - proyecto/tesis
  - tipo/guia
---

# Estados y progreso del proyecto

## Estados

| Estado | Significado |
|---|---|
| `planned` | La tarea existe, pero todavía no empieza |
| `in-progress` | Se está trabajando actualmente |
| `partially-complete` | Tiene avance verificable, pero falta trabajo |
| `blocked` | No puede continuar por una dependencia |
| `completed` | Cumple el criterio de terminado |
| `cancelled` | Se descartó con una razón documentada |

## Qué significa avance parcial

Una tarea está parcialmente completa cuando existe evidencia concreta, pero todavía no
cumple todos sus criterios. Por ejemplo:

```yaml
status: partially-complete
progress: 60
```

Eso debe acompañarse de:

- Qué se completó.
- Qué falta.
- Qué evidencia existe.
- Qué bloquea o habilita el siguiente paso.

El porcentaje es orientativo; el criterio de terminado es la autoridad.

## Etiquetas y relaciones

Usar etiquetas jerárquicas y pocas. No etiquetar cada palabra:

```text
#proyecto/tesis
#sprint/s0
#sprint/s1
#tipo/sesion
#tipo/requisito
#tipo/decision
#tipo/checkpoint
#estado/bloqueado
#modulo/acceso
#modulo/asistencia
#fuente/anteproyecto
#fuente/campo
```

Las propiedades YAML serán la fuente estructurada para filtros; las etiquetas servirán para
navegación rápida y agrupación temática. Los Wikilinks explicarán la relación concreta.

## Ejemplo de error relacionado

```yaml
type: error
status: blocked
sprint: S1
module: acceso
related:
  - "[[RF-001-autenticacion]]"
  - "[[Tarea-configurar-rbac]]"
  - "[[SPRINT-01-acceso]]"
tags:
  - proyecto/tesis
  - tipo/error
  - modulo/acceso
  - estado/bloqueado
```

Las etiquetas permiten filtrar todos los errores de acceso, mientras que los enlaces
permiten seguir exactamente qué requisito y tarea fueron afectados.

## Fechas y calendario

- `date`: fecha de creación o registro.
- `due`: fecha límite de una tarea.
- `scheduled`: fecha prevista para trabajarla.
- `completed`: fecha de finalización.

Una fecha de vencimiento no significa que exista una reunión en el calendario. Las reuniones
reales y recordatorios importantes deben mantenerse en el calendario externo que utilices.
