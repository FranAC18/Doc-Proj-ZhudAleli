from dataclasses import dataclass
import ast
import json
import operator
from typing import Any, Callable

from .memory import MemoryStore
from .obsidian import ObsidianStore


@dataclass
class Tool:
    name: str
    description: str
    parameters: dict[str, Any]
    handler: Callable[..., Any]
    requires_approval: bool = False

    def schema(self) -> dict[str, Any]:
        """Esquema por defecto compatible con formato estándar de function calling."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.parameters,
            },
        }

    def to_gemini_declaration(self) -> dict[str, Any]:
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters,
        }


def _sanitize_arguments(arguments: Any) -> dict[str, Any]:
    """Sanitiza argumentos para garantizar que se entreguen como diccionario válido."""
    if isinstance(arguments, dict):
        return arguments
    if isinstance(arguments, str):
        arguments = arguments.strip()
        if not arguments:
            return {}
        try:
            parsed = json.loads(arguments)
            if isinstance(parsed, dict):
                return parsed
        except json.JSONDecodeError:
            pass
    return {"raw_input": str(arguments)}


class ToolRegistry:
    def __init__(self, tools: list[Tool]):
        self.tools = {tool.name: tool for tool in tools}

    def schemas(self) -> list[dict[str, Any]]:
        return [tool.schema() for tool in self.tools.values()]

    def gemini_declarations(self) -> list[dict[str, Any]]:
        return [tool.to_gemini_declaration() for tool in self.tools.values()]

    def execute(self, name: str, arguments: dict[str, Any] | str) -> Any:
        tool = self.tools.get(name)
        if not tool:
            raise ValueError(f"Herramienta desconocida: {name}")
        if tool.requires_approval:
            raise PermissionError(f"La herramienta {name} requiere aprobación humana")
        sanitized = _sanitize_arguments(arguments)
        return tool.handler(**sanitized)


def _safe_calculator(expression: str) -> str:
    allowed = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow,
        ast.USub: operator.neg,
    }

    def visit(node: ast.AST) -> float:
        if isinstance(node, ast.Expression):
            return visit(node.body)
        if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
            return node.value
        if isinstance(node, ast.UnaryOp) and type(node.op) in allowed:
            return allowed[type(node.op)](visit(node.operand))
        if isinstance(node, ast.BinOp) and type(node.op) in allowed:
            left, right = visit(node.left), visit(node.right)
            if isinstance(node.op, ast.Pow) and abs(right) > 10:
                raise ValueError("Exponente demasiado grande")
            return allowed[type(node.op)](left, right)
        raise ValueError("Expresión no permitida")

    tree = ast.parse(expression, mode="eval")
    result = visit(tree)
    return str(result)


def build_tools(memory: MemoryStore, user_id: str, obsidian: ObsidianStore | None = None) -> ToolRegistry:
    tools = [
        Tool(
            name="calculate",
            description="Calcula operaciones aritméticas simples. No uses funciones ni variables.",
            parameters={
                "type": "object",
                "properties": {"expression": {"type": "string"}},
                "required": ["expression"],
                "additionalProperties": False,
            },
            handler=_safe_calculator,
        ),
        Tool(
            name="search_memory",
            description="Busca recuerdos explícitos del usuario. Úsala antes de afirmar preferencias personales.",
            parameters={
                "type": "object",
                "properties": {"query": {"type": "string"}},
                "required": ["query"],
                "additionalProperties": False,
            },
            handler=lambda query: memory.search(user_id, query),
        ),
        Tool(
            name="remember_fact",
            description="Guarda un dato estable que el usuario haya confirmado o pedido conservar.",
            parameters={
                "type": "object",
                "properties": {"key": {"type": "string"}, "value": {"type": "string"}},
                "required": ["key", "value"],
                "additionalProperties": False,
            },
            handler=lambda key, value: (memory.remember(user_id, key, value), {"saved": True})[1],
        ),
        Tool(
            name="propose_lesson",
            description="Registra una lección candidata después de un error. Queda pendiente de aprobación humana.",
            parameters={
                "type": "object",
                "properties": {"trigger": {"type": "string"}, "lesson": {"type": "string"}},
                "required": ["trigger", "lesson"],
                "additionalProperties": False,
            },
            handler=lambda trigger, lesson: {"lesson_id": memory.add_lesson(user_id, trigger, lesson)},
        ),
    ]
    if obsidian:
        tools.extend([
            Tool(
                name="save_session_summary",
                description="Guarda el resumen de la sesión actual en el vault Obsidian.",
                parameters={
                    "type": "object",
                    "properties": {
                        "sprint": {"type": "string"},
                        "title": {"type": "string"},
                        "summary": {"type": "string"},
                        "next_steps": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["sprint", "title", "summary", "next_steps"],
                    "additionalProperties": False,
                },
                handler=obsidian.save_session_summary,
            ),
            Tool(
                name="save_progress_checkpoint",
                description="Guarda un avance parcial, bloqueo o cierre de tarea en el vault Obsidian.",
                parameters={
                    "type": "object",
                    "properties": {
                        "sprint": {"type": "string"},
                        "title": {"type": "string"},
                        "status": {
                            "type": "string",
                            "enum": ["planned", "in-progress", "partially-complete", "blocked", "completed", "cancelled"],
                        },
                        "progress": {"type": "integer", "minimum": 0, "maximum": 100},
                        "completed": {"type": "array", "items": {"type": "string"}},
                        "remaining": {"type": "array", "items": {"type": "string"}},
                        "blockers": {"type": "array", "items": {"type": "string"}},
                        "next_action": {"type": "string"},
                        "evidence": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["sprint", "title", "status", "progress", "completed", "remaining", "blockers", "next_action", "evidence"],
                    "additionalProperties": False,
                },
                handler=obsidian.save_progress_checkpoint,
            ),
            Tool(
                name="propose_requirement",
                description="Guarda un requisito detectado como propuesta pendiente de validación.",
                parameters={
                    "type": "object",
                    "properties": {
                        "identifier": {"type": "string"},
                        "title": {"type": "string"},
                        "actor": {"type": "string"},
                        "description": {"type": "string"},
                        "criteria": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["identifier", "title", "actor", "description", "criteria"],
                    "additionalProperties": False,
                },
                handler=obsidian.propose_requirement,
            ),
            Tool(
                name="propose_decision",
                description="Guarda una decisión detectada como propuesta pendiente de aprobación.",
                parameters={
                    "type": "object",
                    "properties": {
                        "identifier": {"type": "string"},
                        "title": {"type": "string"},
                        "question": {"type": "string"},
                        "impact": {"type": "string"},
                    },
                    "required": ["identifier", "title", "question", "impact"],
                    "additionalProperties": False,
                },
                handler=obsidian.propose_decision,
            ),
        ])
    return ToolRegistry(tools)
