from typing import Any, Iterator, Protocol, runtime_checkable

from ..models import (
    Message,
    ModelCapability,
    ModelError,
    ModelResponse,
    ProviderAuthError,
    RateLimitError,
    Role,
)


def normalize_messages(messages: list[Message] | list[dict[str, Any]]) -> list[Message]:
    """Convierte listas de diccionarios heredados a instancias canónicas de Message."""
    normalized: list[Message] = []
    for msg in messages:
        if isinstance(msg, Message):
            normalized.append(msg)
        elif isinstance(msg, dict):
            role_str = msg.get("role", "user")
            try:
                role = Role(role_str)
            except ValueError:
                role = Role.USER
            normalized.append(
                Message(
                    role=role,
                    content=msg.get("content") or "",
                    name=msg.get("name"),
                    tool_call_id=msg.get("tool_call_id"),
                )
            )
    return normalized


@runtime_checkable
class ModelAdapter(Protocol):
    """Protocolo canónico para todos los adaptadores de modelos de lenguaje."""

    @property
    def model_id(self) -> str:
        """Identificador del modelo (ej. 'gpt-5.6-luna', 'deepseek-v4')."""
        ...

    @property
    def provider_name(self) -> str:
        """Nombre del proveedor (ej. 'openai', 'deepseek', 'glm', 'google')."""
        ...

    @property
    def capabilities(self) -> set[ModelCapability]:
        """Conjunto de capacidades soportadas por este modelo/adaptador."""
        ...

    def complete(
        self,
        messages: list[Message] | list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> ModelResponse:
        """Genera una respuesta síncrona/bloqueante a partir de los mensajes y herramientas."""
        ...

    def stream(
        self,
        messages: list[Message] | list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> Iterator[ModelResponse]:
        """Genera respuestas en streaming unificado."""
        ...


class BaseHTTPAdapter:
    """Clase base auxiliar para adaptadores que consumen APIs HTTP."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        model_name: str,
        timeout: float = 60.0,
    ):
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.model_name = model_name
        self.timeout = timeout

    @property
    def model_id(self) -> str:
        return self.model_name

    def _handle_http_error(self, exc: Exception, status_code: int | None = None) -> None:
        """Mapea excepciones HTTP a errores de dominio normalizados."""
        if status_code == 401 or status_code == 403:
            raise ProviderAuthError(f"Error de autenticación con el proveedor ({self.model_id}): {exc}") from exc
        if status_code == 429:
            raise RateLimitError(f"Límite de tasa o cuota excedida ({self.model_id}): {exc}") from exc
        raise ModelError(f"Error en llamada a modelo ({self.model_id}): {exc}") from exc
