"""Módulo provider.py conservado por compatibilidad hacia atrás.

Redirige a la nueva capa de adaptadores en agent_harness.adapters.
"""
from typing import Any, Protocol

from .adapters.openai import OpenAIAdapter
from .models import ModelReply


class ChatModel(Protocol):
    def complete(self, messages: list[dict[str, Any]], tools: list[dict[str, Any]]) -> ModelReply:
        ...


class OpenAICompatibleModel(OpenAIAdapter):
    """Alias para compatibilidad hacia atrás con OpenAICompatibleModel."""
