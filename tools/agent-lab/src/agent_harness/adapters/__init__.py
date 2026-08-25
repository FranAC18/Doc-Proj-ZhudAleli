from .base import BaseHTTPAdapter, ModelAdapter, normalize_messages
from .deepseek import DeepSeekAdapter
from .gemini import GeminiAdapter
from .glm import GLMAdapter
from .openai import OpenAIAdapter


def create_adapter(
    provider: str,
    model_name: str,
    api_key: str = "",
    base_url: str | None = None,
    timeout: float = 60.0,
) -> ModelAdapter:
    """Factoría para instanciar adaptadores según proveedor y modelo."""
    prov = provider.lower().strip()
    if prov in {"openai", "chatgpt"}:
        url = base_url or "https://api.openai.com/v1"
        return OpenAIAdapter(base_url=url, api_key=api_key, model_name=model_name, timeout=timeout)
    if prov in {"deepseek", "deepseek-ai"}:
        url = base_url or "https://api.deepseek.com/v1"
        return DeepSeekAdapter(base_url=url, api_key=api_key, model_name=model_name, timeout=timeout)
    if prov in {"glm", "zhipu", "zai"}:
        url = base_url or "https://api.z.ai/api/coding/paas/v4"
        return GLMAdapter(base_url=url, api_key=api_key, model_name=model_name, timeout=timeout)
    if prov in {"google", "gemini"}:
        url = base_url or "https://generativelanguage.googleapis.com/v1beta"
        return GeminiAdapter(base_url=url, api_key=api_key, model_name=model_name, timeout=timeout)
    raise ValueError(f"Proveedor no soportado: '{provider}'. Opciones válidas: openai, deepseek, glm, google.")


__all__ = [
    "ModelAdapter",
    "BaseHTTPAdapter",
    "OpenAIAdapter",
    "DeepSeekAdapter",
    "GLMAdapter",
    "GeminiAdapter",
    "create_adapter",
    "normalize_messages",
]
