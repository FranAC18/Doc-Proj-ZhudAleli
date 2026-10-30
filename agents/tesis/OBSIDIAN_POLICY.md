# Política de integración con Obsidian

## Propósito

Obsidian es la memoria documental persistente del proyecto. El agente puede crear y
enlazar notas dentro del vault, pero debe conservar la diferencia entre una propuesta y una
decisión aprobada.

## Límite del vault y escritura controlada

El vault es la raíz del repositorio `F:\Tesis\App Tesis`. No se consideran documentación
del proyecto los archivos creados fuera de esa raíz ni las salidas temporales de una terminal,
IDE, proveedor o modelo.

La ubicación canónica es:

- `documentacion/`: ediciones académicas con estado explícito; solo archivos revisados
  se incorporan de forma selectiva al repositorio general para posible publicación.
- `analisis/`: trabajo interno organizado por fecha y tema.
- `_archivo/`: material sustituido o retirado con un registro de motivo y reemplazo.
- `docs/bitacora/`: sesiones y checkpoints.
- `docs/requirements/`: requisitos y propuestas.
- `docs/decisions/`: ADR y decisiones propuestas.
- `docs/evidence/`: evidencia reproducible y anonimizada.
- `docs/architecture/`, `docs/ui/`, `docs/sprints/` y `docs/traceability/`: diseño y gobierno.
- `specs/<id-funcionalidad>/`: especificación y artefactos técnicos de la funcionalidad.
- `agents/tesis/`: contexto y políticas estables.

`docs/` y `specs/` conservan las fuentes aprobadas y el trabajo técnico. La edición en
`documentacion/` cita esas fuentes y no se modifica como requisito paralelo. Solo se
sincroniza la edición final revisada; el tesista autoriza cada publicación. Los nombres
versionados de `documentacion/` usan `tema_vM.m_aaaa-mm-dd.md`; esta convención es una
excepción a los guiones de las notas internas de Obsidian.

Los agentes `requirements`, `architect`, `ux` y `reviewer` son de lectura y propuesta. El
`documenter` es el único escritor delegado para documentación operativa, usando solo las
rutas permitidas y sin sobrescribir notas aprobadas. El agente raíz conserva la responsabilidad
de dashboard, sprint, matriz global, specs confirmadas y decisiones aceptadas.

Los hosts Codex, OpenCode/OpenChamber y Antigravity comparten los mismos Markdown, pero sus
archivos internos no son intercambiables automáticamente. La fuente canónica de roles está en
`agents/tesis/roles/`; los cambios de host deben usar un handoff en
`docs/bitacora/checkpoints/`. Obsidian visualiza ese estado persistido y no depende del
historial privado de ningún modelo.

## Recuperación de memoria

La continuidad se recupera con `docs/context/context-index.md` y el estado breve en
`docs/bitacora/ESTADO-ACTIVO.md`. Antes de escribir se consulta el archivo indicado
por `scope_file`. Los requisitos y decisiones conservan sus fuentes canónicas; un
resumen nunca las sustituye. El historial se consulta por tarea o duda concreta.

Obsidian muestra y enlaza estos archivos; esta política no configura búsqueda semántica
ni inyección automática de todo el vault en la IA. El laboratorio `tools/agent-lab/`
es independiente. La memoria privada de cada host sigue siendo contexto auxiliar.
Reutiliza lecturas vigentes dentro del chat y recupera solo lo necesario al retomarlo.

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
- Checkpoints y evidencias de una tarea después de pruebas y revisión.
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

Al cerrar una sesión con trabajo relevante, el agente debe intentar registrar en una
nota o checkpoint (un mismo registro puede cumplir ambas funciones):

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
El cierre administrativo de un periodo es una decisión separada del tesista y no cambia los
estados de las tareas ni exige que todas estén `completed`.

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

- Inicio de una tarea: reutilizar el estado operativo si ya representa la tarea;
  actualizarlo cuando cambie, sin crear una nota por cada mensaje o comando.
- Cambio importante o pausa: crear un `checkpoint`.
- Bloqueo: crear un `checkpoint` con `blocked` y la dependencia.
- Fin de sesión: registrar resultado, evidencia, pendientes y siguiente acción; enlazar
  el checkpoint de la tarea si ya los contiene, sin crear un resumen duplicado.
- Estado activo: conservar solo el resultado vigente, pendientes y siguiente acción con
  enlaces; llevar el relato histórico a checkpoints identificando origen y reemplazo.
- Cambios de RF, criterios, prioridades o estado: conservar la sincronización exigida
  por AGENTS.md. Un ajuste de contexto no declara avance funcional ni exige nuevas
  ediciones académicas de documentos cuyo contenido no cambia.
- Fin de sprint: el tesista decide cuándo cerrar o reabrir el periodo. Basta actualizar el
  registro operativo existente con fecha, resultado y pendientes para dar continuidad; el
  apunte no es precondición. No se requiere acta, revisión previa completa ni aprobación
  adicional. Las evidencias informan el resultado, no vetan el cierre. Las tareas sin
  verificación siguen pendientes y pueden trasladarse.
