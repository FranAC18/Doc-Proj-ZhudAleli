import pytest

from agent_harness.capabilities import CapabilityValidator
from agent_harness.models import (
    IncompatibleModelError,
    Message,
    ModelCapability,
    ModelError,
    ModelResponse,
    Role,
)
from agent_harness.router import ModelRouter


class DummyAdapter:
    def __init__(self, model_id: str, provider: str, capabilities: set[ModelCapability], will_fail: bool = False):
        self._model_id = model_id
        self._provider = provider
        self._capabilities = capabilities
        self.will_fail = will_fail
        self.calls_count = 0

    @property
    def model_id(self) -> str:
        return self._model_id

    @property
    def provider_name(self) -> str:
        return self._provider

    @property
    def capabilities(self) -> set[ModelCapability]:
        return self._capabilities

    def complete(self, messages, tools=None, **kwargs):
        self.calls_count += 1
        if self.will_fail:
            raise ModelError(f"Error simulado en {self.model_id}")
        return ModelResponse(content=f"Respuesta de {self.model_id}")

    def stream(self, messages, tools=None, **kwargs):
        yield self.complete(messages, tools, **kwargs)


def test_router_registration_and_resolution():
    router = ModelRouter(default_model="m1")
    adapter = DummyAdapter("m1", "p1", {ModelCapability.TOOL_CALLING})
    router.register("p1:m1", adapter)
    router.register("m1", adapter)

    resolved = router.resolve(model_name="m1")
    assert resolved.model_id == "m1"
    assert resolved.provider_name == "p1"


def test_capability_validator_accepts_compatible():
    adapter = DummyAdapter("m1", "p1", {ModelCapability.TOOL_CALLING, ModelCapability.STRUCTURED_OUTPUTS})
    CapabilityValidator.validate(adapter, {ModelCapability.TOOL_CALLING})


def test_capability_validator_rejects_incompatible():
    adapter = DummyAdapter("m1", "p1", {ModelCapability.TOOL_CALLING})
    with pytest.raises(IncompatibleModelError) as exc_info:
        CapabilityValidator.validate(adapter, {ModelCapability.TOOL_CALLING, ModelCapability.VISION})
    assert "vision" in str(exc_info.value).lower()


def test_router_fallback_execution():
    router = ModelRouter()
    failing_adapter = DummyAdapter("m-fail", "p1", {ModelCapability.TOOL_CALLING}, will_fail=True)
    working_adapter = DummyAdapter("m-ok", "p2", {ModelCapability.TOOL_CALLING}, will_fail=False)

    router.register("m-fail", failing_adapter)
    router.register("m-ok", working_adapter)

    res = router.execute_with_fallback(
        messages=[Message(role=Role.USER, content="hola")],
        fallback_chain=["m-fail", "m-ok"],
        required_capabilities={ModelCapability.TOOL_CALLING},
    )

    assert res.content == "Respuesta de m-ok"
    assert failing_adapter.calls_count == 1
    assert working_adapter.calls_count == 1


def test_router_fallback_skips_incompatible():
    router = ModelRouter()
    incompatible_adapter = DummyAdapter("m-no-tools", "p1", set(), will_fail=False)
    compatible_adapter = DummyAdapter("m-tools", "p2", {ModelCapability.TOOL_CALLING}, will_fail=False)

    router.register("m-no-tools", incompatible_adapter)
    router.register("m-tools", compatible_adapter)

    res = router.execute_with_fallback(
        messages=[Message(role=Role.USER, content="hola")],
        fallback_chain=["m-no-tools", "m-tools"],
        required_capabilities={ModelCapability.TOOL_CALLING},
    )

    assert res.content == "Respuesta de m-tools"
    assert incompatible_adapter.calls_count == 0
    assert compatible_adapter.calls_count == 1
