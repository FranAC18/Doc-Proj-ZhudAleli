import logging
import os
from typing import Any

from .adapters.base import ModelAdapter
from .capabilities import CapabilityValidator
from .models import (
    IncompatibleModelError,
    Message,
    ModelCapability,
    ModelError,
    ModelResponse,
)

logger = logging.getLogger(__name__)


class ModelRouter:
    """Enrutador dinámico de modelos con verificación de capacidades y soporte de fallback."""

    def __init__(self, default_model: str = "gpt-5.6-luna", default_provider: str = "openai"):
        self.default_model = default_model
        self.default_provider = default_provider
        self._registry: dict[str, ModelAdapter] = {}

    def register(self, key: str, adapter: ModelAdapter) -> None:
        """Registra un adaptador bajo una clave unívoca (ej. 'openai:gpt-5.6-luna' o 'deepseek-v4')."""
        self._registry[key.lower().strip()] = adapter

    def get_registered_models(self) -> list[dict[str, Any]]:
        """Lista todos los modelos registrados con sus capacidades."""
        return [
            {
                "key": key,
                "model_id": adapter.model_id,
                "provider": adapter.provider_name,
                "capabilities": sorted(c.value for c in adapter.capabilities),
            }
            for key, adapter in sorted(self._registry.items())
        ]

    def resolve(
        self,
        model_name: str | None = None,
        agent_name: str | None = None,
        required_capabilities: set[ModelCapability] | None = None,
    ) -> ModelAdapter:
        """Resuelve el adaptador adecuado según parámetros, configuración de agente o variables de entorno."""
        target_key = None

        if model_name:
            target_key = model_name
        elif agent_name:
            env_var = f"MODEL_AGENT_{agent_name.upper().replace('-', '_')}"
            target_key = os.getenv(env_var)

        if not target_key:
            target_key = os.getenv("MODEL_NAME", self.default_model)

        target_key_clean = target_key.lower().strip()
        adapter = self._registry.get(target_key_clean)

        # Si no se encuentra por clave exacta, buscar por model_id o prefijo
        if not adapter:
            for key, ad in self._registry.items():
                if ad.model_id.lower() == target_key_clean or key.endswith(f":{target_key_clean}"):
                    adapter = ad
                    break

        if not adapter:
            available = ", ".join(sorted(self._registry.keys())) or "ninguno"
            raise ValueError(
                f"Modelo '{target_key}' no registrado en el Router. Modelos disponibles: [{available}]"
            )

        if required_capabilities:
            CapabilityValidator.validate(adapter, required_capabilities)

        return adapter

    def execute_with_fallback(
        self,
        messages: list[Message] | list[dict[str, Any]],
        fallback_chain: list[str],
        tools: list[dict[str, Any]] | None = None,
        required_capabilities: set[ModelCapability] | None = None,
        **kwargs: Any,
    ) -> ModelResponse:
        """Ejecuta una solicitud intentando sucesivamente la cadena de modelos ante fallos recuperables."""
        last_error: Exception | None = None

        for model_key in fallback_chain:
            try:
                adapter = self.resolve(model_name=model_key, required_capabilities=required_capabilities)
                return adapter.complete(messages, tools=tools, **kwargs)
            except IncompatibleModelError as exc:
                logger.warning("Modelo '%s' descartado por incompatibilidad de capacidades: %s", model_key, exc)
                last_error = exc
                continue
            except ModelError as exc:
                logger.warning("Fallo recuperable en modelo '%s': %s. Intentando siguiente fallback...", model_key, exc)
                last_error = exc
                continue

        raise RuntimeError(f"Cadena de fallbacks agotada: {fallback_chain}. Último error: {last_error}")
