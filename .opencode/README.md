# Adaptación de OpenCode/OpenChamber

OpenChamber proporciona la interfaz; OpenCode ejecuta el agente. Los agentes personalizados
de OpenCode viven en `.opencode/agents/` y apuntan a los contratos canónicos de
`agents/tesis/roles/`. OpenChamber no es fuente de configuración ni de verdad.

No se fija un identificador concreto de modelo en cada agente o comando. El perfil de capacidad
se declara una sola vez en `tools/agent-routes.toml`; el proveedor y el modelo real se eligen
en el runtime de OpenCode y pueden cambiar sin rediseñar el routing.

## Agentes

Roles disponibles en OpenCode:

- `architect`: arquitectura y propuestas autorizadas.
- `implementer`: tareas de implementación acotadas.
- `frontend`: UI móvil y accesible.
- `reviewer`: revisión read-only.
- `researcher`: investigación read-only y propuestas documentales autorizadas.
- `requirements`, `ux`, `documenter` y `git-manager`: roles universales existentes.

## Comandos

OpenCode descubre estos comandos nativos desde `.opencode/commands/`:

| Comando | Agente | Resultado |
|---|---|---|
| `/route` | `plan` | Clasificación sin implementación. |
| `/architect` | `architect` | Propuesta arquitectónica. |
| `/implement` | `implementer` | Tarea previamente especificada. |
| `/frontend` | `frontend` | Tarea UI asignada. |
| `/review` | `reviewer` | Revisión sin edición. |
| `/research` | `researcher` | Informe trazable. |

Todos reciben argumentos mediante `$ARGUMENTS`. En OpenCode 1.18.x `subtask` no se usa como
garantía de sesión hija: los comandos ejecutan su plantilla en la sesión actual. La delegación
real depende del permiso `task` y del agente primario que la invoque.

Antes de editar, OpenCode lee el contexto mínimo de `AGENTS.md`,
`docs/context/context-index.md` y `docs/bitacora/ESTADO-ACTIVO.md`; el resto se recupera según
el tipo de tarea. Los agentes especializados tienen `task: deny` para evitar delegación
recursiva accidental.
