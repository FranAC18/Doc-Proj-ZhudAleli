from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Role(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


class ModelCapability(str, Enum):
    TOOL_CALLING = "tool_calling"
    PARALLEL_TOOL_CALLING = "parallel_tool_calling"
    STRUCTURED_OUTPUTS = "structured_outputs"
    NATIVE_JSON_SCHEMA = "native_json_schema"
    SYSTEM_MESSAGES = "system_messages"
    REASONING_TOKENS = "reasoning_tokens"
    VISION = "vision"
    EXTENDED_CONTEXT_100K = "extended_context_100k"
    EXTENDED_CONTEXT_1M = "extended_context_1m"
    STREAMING = "streaming"


@dataclass(frozen=True)
class ContentPart:
    type: str  # "text", "image_url", "thinking"
    text: str | None = None
    media_data: dict[str, Any] | None = None


@dataclass(frozen=True)
class ToolCall:
    id: str
    name: str
    arguments: dict[str, Any]


@dataclass
class Message:
    role: Role
    content: str | list[ContentPart]
    name: str | None = None
    tool_call_id: str | None = None
    tool_calls: list[ToolCall] = field(default_factory=list)
    reasoning_content: str | None = None

    def __getitem__(self, item: str) -> Any:
        """Permite acceso como diccionario para compatibilidad hacia atrás."""
        if hasattr(self, item):
            val = getattr(self, item)
            if isinstance(val, Role):
                return val.value
            return val
        raise KeyError(item)


@dataclass(frozen=True)
class UsageInfo:
    prompt_tokens: int = 0
    completion_tokens: int = 0
    total_tokens: int = 0
    reasoning_tokens: int = 0
    estimated_cost_usd: float = 0.0


@dataclass
class ModelResponse:
    content: str = ""
    tool_calls: list[ToolCall] = field(default_factory=list)
    reasoning_content: str | None = None
    finish_reason: str = "stop"
    usage: UsageInfo = field(default_factory=UsageInfo)
    raw: dict[str, Any] = field(default_factory=dict)


# Alias para compatibilidad hacia atrás con código existente
ModelReply = ModelResponse


class ModelError(RuntimeError):
    """Error normalizado para que el arnés no dependa de un proveedor."""


class IncompatibleModelError(ModelError):
    """Lanzado cuando un modelo no cumple con las capacidades requeridas por el agente."""


class ProviderAuthError(ModelError):
    """Lanzado ante errores de autenticación o claves de API faltantes/inválidas."""


class RateLimitError(ModelError):
    """Lanzado cuando se alcanzan límites de tasa o cuotas del proveedor."""
