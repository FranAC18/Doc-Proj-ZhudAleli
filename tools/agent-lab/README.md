# Laboratorio del agente Python

Este directorio conserva el prototipo educativo recibido. Demuestra un bucle de herramientas,
memoria SQLite, notas Obsidian y un adaptador de Chat Completions. No tiene herramientas de
filesystem, shell, Git o edición de código, por lo que no es el agente que construye la
aplicación.

Se mantiene para estudiar y comparar decisiones de arnés sin contaminar el proyecto Django.

## Ejecutar pruebas

Desde la raíz:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e "tools/agent-lab[dev]"
pytest -q tools/agent-lab/tests
```

## Ejecutar el chat experimental

```bash
cp tools/agent-lab/.env.example .env
agent-harness
```

También funciona:

```bash
python -m agent_harness.cli
```

No uses datos personales ni claves de producción. Las notas existentes no se sobrescriben y
un checkpoint `completed` exige 100 %, ausencia de pendientes/bloqueos y evidencia.
