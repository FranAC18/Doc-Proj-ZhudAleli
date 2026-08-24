# ONBOARDING-IA: Guía de Contexto para Modelos y Agentes de IA

> **DOCUMENTO DE LECTURA OBLIGATORIA PARA CUALQUIER IA / ASISTENTE / MOTOR QUE INICIE SESIÓN EN ESTE REPOSITORIO**
>
> Si eres una IA (OpenCode, Codex, Gemini, Claude, ChatGPT, Cursor, Aider o cualquier CLI/IDE), **lee este archivo completo antes de proponer código o cambios**.

---

## 1. Prompt de Inicialización Rápida

Cuando abras este proyecto en una nueva herramienta o con un nuevo modelo (ej. OpenCode, Codex, Claude, ChatGPT), puedes iniciar la conversación pegando este mensaje:

```text
Actúa como ingeniero de software y asistente de tesis para el proyecto Zhud Alelí.
Lee obligatoriamente `ONBOARDING-IA.md` y `AGENTS.md` para situarte en el contexto actual, estado del sprint y reglas de operación antes de responder.
Indica en qué fase nos encontramos y cuál es el próximo paso permitido.
```

---

## 2. Identidad y Misión del Proyecto

* **Proyecto**: Aplicación web de titulación de Ingeniería de Software para el **Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud** y su unidad productiva **Zhud Alelí**.
* **Objetivo**: Gestión organizacional comunitaria y trazabilidad productiva (acopio, secado, lotes, mermas, inventario y venta de plantas medicinales y té).
* **Enfoque Sociotécnico**: Diseño adaptado a la realidad comunitaria (controles táctiles amplios, baja alfabetización digital, contraste AA, conectividad intermitente). No imponer procesos burocráticos ajenos a su organización.
* **Stack Tecnológico Aprobado**:
  * **Backend**: Python 3.12 + Django (Monolito Modular con arquitectura MTV).
  * **Base de Datos**: PostgreSQL (transaccional, integridad referencial y auditoría estricta).
  * **Frontend**: HTML5 renderizado en servidor + Bootstrap 5 + JavaScript vanilla puntual para interacciones concretas.
  * **Gobernanza y Vault**: Obsidian (Markdown con YAML frontmatter y Wikilinks en `docs/`).

---

## 3. Estado Actual del Repositorio (Al 15 de Agosto de 2026)

* **Fase Actual**: Fase I — Levantamiento, especificación y diseño técnico de la primera funcionalidad.
* **Sprint 0 (Preparación)**: **CERRADO** con evidencia y validación técnica.
* **Catálogo de Requisitos**: [`docs/requirements/CAT-REQ-001.md`](file:///f:/Tesis/App%20Tesis/docs/requirements/CAT-REQ-001.md) versión 1.0 aprobada (57 requisitos confirmados).
* **Primera Funcionalidad**: [`specs/001-acceso-usuarias-internas/`](file:///f:/Tesis/App%20Tesis/specs/001-acceso-usuarias-internas/) con spec `confirmed` y plan `approved` (2026-08-24); listo para generar tareas de implementación.
* **Aplicación Django**: **Aún no creada**. No asumas que Django ya está configurado ni generes código de producción hasta que las tareas (`tasks.md`) estén aprobadas.
* **Arnés de IA (`tools/agent-lab/`)**: Completamente migrado a arquitectura multi-modelo agnóstica con enrutador dinámico (`ModelRouter`), adaptadores (OpenAI, DeepSeek, GLM, Gemini) y telemetría SQLite.

---

## 4. Orden Obligatorio de Lectura para la IA

Para no sobrecargar tu contexto, lee los archivos en este orden estricto:

```text
1. ONBOARDING-IA.md (Este documento: visión rápida y reglas operativas)
      ↓
2. AGENTS.md (Contrato rector de ingeniería y gobernanza)
      ↓
3. .specify/memory/constitution.md (Principios de calidad y puertas de avance)
      ↓
4. agents/tesis/PROJECT_CONTEXT.md (Detalle del dominio comunitario de Zhud Alelí)
      ↓
5. docs/00-inicio/00-dashboard.md (Tablero de control en tiempo real)
      ↓
6. Si la tarea es de una funcionalidad específica:
   Lee specs/<id-funcionalidad>/spec.md y plan.md
```

---

## 5. Reglas Inquebrantables de Operación (Guardrails)

1. **Fuentes de Verdad**:
   * Una conversación o inferencia de IA **NUNCA aprueba un requisito**. Los requisitos solo se aprueban por validación humana del tesista/directora/organización.
2. **Desarrollo Guiado por Especificación**:
   * No implementes código sin una especificación confirmada (`spec.md`), un plan aprobado (`plan.md`) y tareas desglosadas (`tasks.md`).
3. **Seguridad y Git**:
   * **NUNCA** hagas `git commit`, `git push`, `git merge`, `git rebase` ni borres ramas de forma autónoma. Solo prepara el diff y solicita confirmación al tesista.
   * **CERO SECRETOS**: Nunca escribas claves de API, contraseñas ni datos personales en archivos versionados.
4. **Seguridad en Backend**:
   * Toda regla de autorización y permiso (RBAC) debe validarse en el backend (vistas/servicios Django), no solo ocultando botones en las plantillas.
5. **Trazabilidad de Datos**:
   * En inventario, acopio y asistencia, registra **movimientos históricos**. Nunca reemplaces un stock con un número mutable sin rastro de autor, fecha y motivo.
6. **Arquitectura Limpia**:
   * Mantén un monolito modular Django. No propongas Single Page Applications (React/Vue), microservicios ni colas complejas (Celery/Redis) sin un ADR que demuestre una necesidad real.

---

## 6. Ecosistema de Herramientas y Motores Soportados

| Entorno / Motor | Cómo se inicializa | Dónde lee contexto |
| :--- | :--- | :--- |
| **OpenCode** | `opencode --model <modelo>` | Lee `.agents/skills/`, `AGENTS.md` y `ONBOARDING-IA.md` automáticamente. |
| **Codex App / CLI** | `.\scripts\agent.ps1 codex` | Lee `.codex/agents/*.toml`, `.agents/skills/` y `AGENTS.md`. |
| **Kimi Code CLI** | `.\scripts\agent.ps1 kimi` | Descubre `.agents/skills/` y comandos `/skill:speckit-*`. |
| **Antigravity / Cursor / VS Code** | Abrir la carpeta raíz del workspace | Carga las skills de Spec Kit y reglas rectoras. |
| **Arnés Python Autónomo** | `python -m agent_harness.cli --model <nombre>` | Ejecuta agentes con memoria SQLite y puente a Obsidian. |

---

## 7. Flujo de Trabajo para una Funcionalidad (Spec Kit)

Cuando se trabaje en una nueva funcionalidad, sigue el ciclo estándar de GitHub Spec Kit (invocable como `$speckit-*` o `/skill:speckit-*`):

1. `speckit-specify`: Genera el borrador inicial de la especificación a partir del requisito.
2. `speckit-clarify`: Identifica y formula preguntas para resolver ambigüedades.
3. *Aprobación humana del tesista*.
4. `speckit-plan`: Diseña la arquitectura, modelo de datos, contratos HTTP y plan de pruebas.
5. `speckit-tasks`: Genera la lista ordenada de tareas dependientes (`tasks.md`).
6. `speckit-analyze`: Verifica la coherencia entre spec, plan y tasks antes de codificar.
7. `speckit-implement`: Implementa tareas verticales acotadas con pruebas automatizadas.

---

## 8. Comandos de Verificación Técnica

Antes de dar por terminada cualquier sesión o tarea, ejecuta:

```bash
# 1. Pruebas del arnés y adaptadores de IA:
& "f:\Tesis\App Tesis\tools\agent-lab\.venv\Scripts\python.exe" -m pytest tools/agent-lab/tests

# 2. Control de integridad del diff de Git:
git diff --check

# 3. Cuando exista la base Django:
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

---

## 9. Próximo Paso Permitido en el Proyecto

* **Estado Actual**: Plan técnico de [`specs/001-acceso-usuarias-internas/plan.md`](file:///f:/Tesis/App%20Tesis/specs/001-acceso-usuarias-internas/plan.md) `approved` por el tesista.
* **Acción Inmediata**: Ejecutar `speckit-tasks` y `speckit-analyze` para generar las tareas de implementación de SPEC-001, preparar la estructura inicial del proyecto Django y localizar/instalar PostgreSQL.
