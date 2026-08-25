from .adapters.base import ModelAdapter
from .models import IncompatibleModelError, ModelCapability


class CapabilityValidator:
    """Validador estricto de capacidades de modelos para evitar errores en tiempo de ejecución."""

    @staticmethod
    def validate(adapter: ModelAdapter, required: set[ModelCapability]) -> None:
        """Verifica que el adaptador soporte todas las capacidades requeridas por el agente."""
        if not required:
            return

        supported = adapter.capabilities
        missing = required - supported
        if missing:
            missing_names = ", ".join(sorted(c.value for c in missing))
            supported_names = ", ".join(sorted(c.value for c in supported))
            raise IncompatibleModelError(
                f"El modelo '{adapter.model_id}' ({adapter.provider_name}) no satisface las capacidades requeridas: [{missing_names}]. "
                f"Capacidades soportadas: [{supported_names}]"
            )
