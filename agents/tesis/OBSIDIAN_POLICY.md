# Política de integración con Obsidian

## Propósito

Obsidian es la memoria documental persistente del proyecto. El agente puede crear y
enlazar notas dentro del vault, pero debe conservar la diferencia entre una propuesta y una
decisión aprobada.

## Tipos de notas

- `session`: resumen de una sesión de trabajo.
- `requirement`: requisito funcional o no funcional.
- `decision`: decisión de arquitectura, alcance o negocio.
- `bug`: error reproducible.
- `meeting`: reunión o validación con la organización.
- `checkpoint`: avance parcial de una tarea.

## Escritura automática permitida

- Resúmenes de sesión.
- Pendientes detectados.
- Errores técnicos reproducibles.
- Requisitos en carpeta `docs/requirements/proposals/` con estado `proposed`.
- Decisiones en carpeta `docs/decisions/proposals/` con estado `proposed`.

## Escritura que requiere aprobación

- Cambiar el alcance del proyecto.
- Convertir una propuesta en requisito confirmado.
- Convertir una propuesta en decisión aceptada.
- Modificar el roadmap de sprints.
- Eliminar o sobrescribir una nota aprobada.

## Convenciones

- Usar nombres de archivo en minúsculas y con guiones.
- Cada nota debe tener propiedades YAML.
- Enlazar notas relacionadas con Wikilinks de Obsidian.
- Relacionar cada tarea, error, avance o decisión con su `sprint` y `module` cuando aplique.
- Usar `related` para enlaces directos a requisitos, tareas, sesiones, decisiones o errores.
- No guardar credenciales, cédulas, teléfonos ni información personal innecesaria.
- El dashboard debe enlazar el sprint y los documentos principales, pero no acumular todo
  el contenido del proyecto.

## Cierre de sesión

Al cerrar una sesión, el agente debe intentar registrar:

1. Objetivo.
2. Trabajo realizado.
3. Decisiones propuestas.
4. Requisitos detectados.
5. Errores o bloqueos.
6. Próximo paso permitido.

## Estados de trabajo

Usar estos estados para tareas y checkpoints:

- `planned`: planificada, aún no iniciada.
- `in-progress`: en ejecución.
- `partially-complete`: tiene avance, pero falta trabajo verificable.
- `blocked`: no puede continuar por una dependencia o decisión pendiente.
- `completed`: cumple el criterio de terminado.
- `cancelled`: descartada con motivo documentado.

No usar `completed` solo porque se escribió código. Debe existir evidencia: prueba, revisión,
decisión aprobada o validación correspondiente.

## Etiquetas y relaciones

No etiquetar cada palabra. Usar entre 2 y 5 etiquetas por nota, normalmente una de cada
grupo:

- Proyecto: `proyecto/tesis`.
- Tipo: `tipo/tarea`, `tipo/error`, `tipo/decision`, `tipo/checkpoint`.
- Sprint: `sprint/s0`, `sprint/s1`, etc.
- Módulo: `modulo/acceso`, `modulo/planificacion`, `modulo/asistencia`,
  `modulo/trazabilidad`, `modulo/reportes` o `modulo/transversal`.
- Estado: solo cuando facilite una vista, por ejemplo `estado/bloqueado`.

Las etiquetas clasifican. Los Wikilinks relacionan. Por ejemplo, un error debe enlazar la
tarea, requisito o módulo que afecta; una decisión debe enlazar el sprint y las notas que
dependen de ella.

## Cadencia de registro

- Inicio de una tarea: registrar `planned` o `in-progress`.
- Cambio importante o pausa: crear un `checkpoint`.
- Bloqueo: crear un `checkpoint` con `blocked` y la dependencia.
- Fin de sesión: crear un resumen de sesión.
- Fin de sprint: cerrar formalmente solo después de revisar evidencias.
