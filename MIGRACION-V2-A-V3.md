# Integrar esta base en el repositorio existente

Esta entrega no contiene `.git` y no modifica GitHub. Integra los archivos sobre un clon
limpio del repositorio, conservando la historia.

## 1. Preparar la rama

```bash
git status
git switch main
git pull --ff-only
git switch -c chore/portable-harness
```

Si `git status` muestra trabajo sin guardar, detente y decide primero cómo preservarlo. No
uses `reset --hard` ni reemplaces esos archivos.

## 2. Copiar la entrega

Copia el contenido de este paquete a la raíz del clon, incluyendo los directorios ocultos:

- `.agents/`
- `.codex/`
- `.specify/`

No reemplaces ni copies una carpeta `.git`.

El arnés v2 fue movido de la raíz a `tools/agent-lab/`. Si aplicas los cambios a mano, usa
`git mv` para conservar mejor el historial:

```bash
mkdir -p tools/agent-lab
git mv src tools/agent-lab/src
git mv tests tools/agent-lab/tests
git mv pyproject.toml tools/agent-lab/pyproject.toml
git mv .env.example tools/agent-lab/.env.example
```

Después copia el resto de cambios del paquete.

## 3. Verificar

```bash
uv run --project tools/agent-lab --extra dev \
  pytest -q tools/agent-lab/tests

specify integration status
specify preset resolve spec-template
bash -n scripts/agent.sh
git diff --check
git status --short
```

Resultado esperado:

- 10 pruebas pasan.
- Spec Kit informa `Integration status: OK` y solo una integración instalada: `codex`.
- La plantilla resuelta proviene de `.specify/templates/overrides/spec-template.md`.
- No aparecen claves, bases SQLite, cachés ni archivos personales.

## 4. Revisar antes de publicar

```bash
git diff --stat
git diff
```

Revisa especialmente Constitución, ADR-0002, roles, flujo Git y decisiones pendientes. El
tesista decide si acepta, modifica o descarta estas propuestas. Solo después prepara el
commit y el push de manera explícita.

## 5. Primera prueba funcional del arnés

Inicia Codex o Kimi desde la raíz y ejecuta EVAL-01 y EVAL-02 de
`evals/providers/SMOKE-TEST.md`. Todavía no ejecutes implementación Django. El cierre del
Sprint 0 habilita la siguiente etapa.
