from typing import Any
import json
import uuid
from pathlib import Path

from .adapters.base import ModelAdapter
from .memory import MemoryStore
from .models import Message, ModelError, ModelResponse, Role
from .tools import ToolRegistry


SYSTEM_PROMPT = """Eres un agente de estudio y desarrollo de software.
Responde en español, con precisión y sin inventar resultados de herramientas.
Puedes usar herramientas cuando aporten valor.
Reglas de memoria:
- Busca memoria antes de afirmar una preferencia del usuario.
- Guarda solo datos estables, útiles y explícitamente confirmados.
- Si ocurre un error, propone una lección concreta; nunca cambies tus reglas de forma silenciosa.
Reglas de seguridad:
- No ejecutes acciones destructivas ni externas en esta versión.
- Si una petición necesita permisos, datos sensibles o una acción irreversible, pide confirmación.
- Distingue hechos, inferencias y dudas.
"""


class Agent:
    def __init__(
        self,
        model: ModelAdapter | Any,
        memory: MemoryStore,
        tools: ToolRegistry,
        user_id: str,
        max_steps: int = 8,
        profile_dir: str | None = None,
        project_root: str | None = None,
    ):
        self.model = model
        self.memory = memory
        self.tools = tools
        self.user_id = user_id
        self.max_steps = max_steps
        self.profile_dir = Path(profile_dir) if profile_dir else None
        self.project_root = Path(project_root) if project_root else None

    def _profile_context(self) -> str:
        sections = []
        if self.project_root:
            project_files = [
                "AGENTS.md",
                ".specify/memory/constitution.md",
                "docs/00-inicio/00-dashboard.md",
            ]
            for relative in project_files:
                path = self.project_root / relative
                if path.is_file():
                    sections.append(f"## {relative}\n{path.read_text(encoding='utf-8')}")

            sprint_dir = self.project_root / "docs/sprints"
            if sprint_dir.is_dir():
                for path in sorted(sprint_dir.glob("SPRINT-*.md")):
                    content = path.read_text(encoding="utf-8")
                    if "status: in-progress" in content or "status: partially-complete" in content:
                        sections.append(f"## {path.relative_to(self.project_root)}\n{content}")

        if self.profile_dir:
            files = ["AGENT.md", "PROJECT_CONTEXT.md", "KNOWLEDGE_POLICY.md", "OBSIDIAN_POLICY.md"]
            for filename in files:
                path = self.profile_dir / filename
                if path.is_file():
                    sections.append(f"## {filename}\n{path.read_text(encoding='utf-8')}")
        return "\n\n".join(sections)

    def _messages(self, user_text: str) -> list[Message]:
        lessons = self.memory.approved_lessons(self.user_id)
        context = (
            "Lecciones aprobadas:\n" + json.dumps(lessons, ensure_ascii=False)
            if lessons
            else "No hay lecciones aprobadas."
        )
        profile = self._profile_context()
        system_content = (
            SYSTEM_PROMPT
            + "\n\n"
            + context
            + ("\n\nCONTEXTO DEL PROYECTO:\n" + profile if profile else "")
        )

        messages: list[Message] = [Message(role=Role.SYSTEM, content=system_content)]
        for turn in self.memory.recent_turns(self.user_id):
            role = Role.USER if turn["role"] == "user" else Role.ASSISTANT
            messages.append(Message(role=role, content=turn["content"]))
        messages.append(Message(role=Role.USER, content=user_text))
        return messages

    def run(self, user_text: str) -> str:
        run_id = str(uuid.uuid4())
        messages = self._messages(user_text)
        self.memory.add_turn(self.user_id, "user", user_text)

        for step in range(self.max_steps):
            try:
                reply: ModelResponse = self.model.complete(messages, self.tools.schemas())
            except ModelError as exc:
                self.memory.record_event(
                    self.user_id,
                    "model_error",
                    {"run_id": run_id, "step": step, "error": str(exc)},
                )
                raise

            assistant_msg = Message(
                role=Role.ASSISTANT,
                content=reply.content,
                tool_calls=reply.tool_calls,
                reasoning_content=reply.reasoning_content,
            )
            messages.append(assistant_msg)

            if not reply.tool_calls:
                final = reply.content.strip() or "El modelo no devolvió contenido."
                self.memory.add_turn(self.user_id, "assistant", final)
                self.memory.record_event(
                    self.user_id,
                    "run_completed",
                    {
                        "run_id": run_id,
                        "steps": step + 1,
                        "usage": {
                            "prompt_tokens": reply.usage.prompt_tokens,
                            "completion_tokens": reply.usage.completion_tokens,
                            "total_tokens": reply.usage.total_tokens,
                        },
                    },
                )
                return final

            for call in reply.tool_calls:
                try:
                    result = self.tools.execute(call.name, call.arguments)
                    self.memory.record_event(
                        self.user_id, "tool_completed", {"run_id": run_id, "tool": call.name}
                    )
                except Exception as exc:  # el error vuelve al modelo para que pueda recuperarse
                    result = {"error": str(exc), "tool": call.name}
                    self.memory.record_event(
                        self.user_id,
                        "tool_error",
                        {"run_id": run_id, "tool": call.name, "error": str(exc)},
                    )
                    self.memory.add_lesson(
                        self.user_id,
                        f"falló {call.name}",
                        f"Validar argumentos y permisos antes de usar {call.name}",
                    )

                messages.append(
                    Message(
                        role=Role.TOOL,
                        name=call.name,
                        tool_call_id=call.id,
                        content=json.dumps(result, ensure_ascii=False, default=str),
                    )
                )

        raise RuntimeError(
            f"El agente alcanzó el máximo de {self.max_steps} pasos; posible bucle de herramientas"
        )
