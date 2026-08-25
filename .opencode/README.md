# Adaptación de OpenCode/OpenChamber

OpenChamber proporciona la interfaz; OpenCode ejecuta el agente. Los agentes personalizados
de OpenCode viven en `.opencode/agents/` y apuntan a los contratos canónicos de
`agents/tesis/roles/`.

No se fija un modelo en estos archivos para evitar forzar una cuota o proveedor. Selecciona
el modelo desde OpenCode/OpenChamber usando el proveedor disponible, por ejemplo
`opencode-go/<modelo>` cuando OpenCode Go esté activo.

OpenCode debe leer `AGENTS.md`, `.agents/skills/` y el último handoff antes de editar.
