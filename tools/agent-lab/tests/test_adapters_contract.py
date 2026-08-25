import json
import httpx
import pytest

from agent_harness.adapters.deepseek import DeepSeekAdapter
from agent_harness.adapters.gemini import GeminiAdapter
from agent_harness.adapters.glm import GLMAdapter
from agent_harness.adapters.openai import OpenAIAdapter
from agent_harness.models import Message, ModelCapability, ModelResponse, ProviderAuthError, RateLimitError, Role


def test_openai_adapter_contract(monkeypatch):
    adapter = OpenAIAdapter(api_key="test-key", model_name="gpt-5.6-luna")
    assert adapter.provider_name == "openai"
    assert ModelCapability.TOOL_CALLING in adapter.capabilities

    mock_response = {
        "choices": [
            {
                "message": {
                    "content": "Respuesta OpenAI",
                    "tool_calls": [
                        {
                            "id": "call_1",
                            "type": "function",
                            "function": {
                                "name": "calculate",
                                "arguments": "{\"expression\": \"10 + 20\"}",
                            },
                        }
                    ],
                },
                "finish_reason": "tool_calls",
            }
        ],
        "usage": {"prompt_tokens": 15, "completion_tokens": 8, "total_tokens": 23},
    }

    def mock_post(url, **kwargs):
        request = httpx.Request("POST", url)
        return httpx.Response(200, json=mock_response, request=request)

    monkeypatch.setattr(httpx, "post", mock_post)

    messages = [Message(role=Role.USER, content="Calcula 10 + 20")]
    reply = adapter.complete(messages)

    assert isinstance(reply, ModelResponse)
    assert reply.content == "Respuesta OpenAI"
    assert len(reply.tool_calls) == 1
    assert reply.tool_calls[0].name == "calculate"
    assert reply.tool_calls[0].arguments == {"expression": "10 + 20"}
    assert reply.usage.total_tokens == 23


def test_deepseek_adapter_extracts_reasoning(monkeypatch):
    adapter = DeepSeekAdapter(api_key="test-key", model_name="deepseek-v4")
    assert adapter.provider_name == "deepseek"
    assert ModelCapability.REASONING_TOKENS in adapter.capabilities

    mock_response = {
        "choices": [
            {
                "message": {
                    "content": "Respuesta final después de pensar.",
                    "reasoning_content": "Paso 1: Analizar balance. Paso 2: Calcular merma.",
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {
            "prompt_tokens": 40,
            "completion_tokens": 20,
            "total_tokens": 60,
            "completion_tokens_details": {"reasoning_tokens": 15},
        },
    }

    def mock_post(url, **kwargs):
        request = httpx.Request("POST", url)
        return httpx.Response(200, json=mock_response, request=request)

    monkeypatch.setattr(httpx, "post", mock_post)

    messages = [Message(role=Role.USER, content="Analiza merma")]
    reply = adapter.complete(messages)

    assert reply.content == "Respuesta final después de pensar."
    assert reply.reasoning_content == "Paso 1: Analizar balance. Paso 2: Calcular merma."
    assert reply.usage.reasoning_tokens == 15


def test_glm_adapter_contract(monkeypatch):
    adapter = GLMAdapter(api_key="test-key", model_name="glm-5.2")
    assert adapter.provider_name == "glm"
    assert ModelCapability.EXTENDED_CONTEXT_1M in adapter.capabilities

    mock_response = {
        "choices": [
            {
                "message": {
                    "content": "Respuesta GLM",
                },
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15},
    }

    def mock_post(url, **kwargs):
        request = httpx.Request("POST", url)
        return httpx.Response(200, json=mock_response, request=request)

    monkeypatch.setattr(httpx, "post", mock_post)

    reply = adapter.complete([Message(role=Role.USER, content="hola")])
    assert reply.content == "Respuesta GLM"
    assert reply.usage.total_tokens == 15


def test_gemini_adapter_contract(monkeypatch):
    adapter = GeminiAdapter(api_key="test-key", model_name="gemini-2.5-pro")
    assert adapter.provider_name == "google"
    assert ModelCapability.VISION in adapter.capabilities

    mock_response = {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {"text": "Respuesta Gemini con llamada a tool"},
                        {
                            "functionCall": {
                                "name": "calculate",
                                "args": {"expression": "50 * 2"},
                            }
                        },
                    ]
                },
                "finishReason": "STOP",
            }
        ],
        "usageMetadata": {
            "promptTokenCount": 25,
            "candidatesTokenCount": 12,
            "totalTokenCount": 37,
        },
    }

    def mock_post(url, **kwargs):
        request = httpx.Request("POST", url)
        return httpx.Response(200, json=mock_response, request=request)

    monkeypatch.setattr(httpx, "post", mock_post)

    reply = adapter.complete([Message(role=Role.USER, content="Multiplica 50 por 2")])
    assert reply.content == "Respuesta Gemini con llamada a tool"
    assert len(reply.tool_calls) == 1
    assert reply.tool_calls[0].name == "calculate"
    assert reply.tool_calls[0].arguments == {"expression": "50 * 2"}
    assert reply.usage.total_tokens == 37


def test_adapter_auth_error_handling(monkeypatch):
    adapter = OpenAIAdapter(api_key="bad-key")

    def mock_post(url, **kwargs):
        request = httpx.Request("POST", url)
        return httpx.Response(401, json={"error": "Invalid API Key"}, request=request)

    monkeypatch.setattr(httpx, "post", mock_post)

    with pytest.raises(ProviderAuthError):
        adapter.complete([Message(role=Role.USER, content="test")])


def test_adapter_rate_limit_error_handling(monkeypatch):
    adapter = OpenAIAdapter(api_key="key")

    def mock_post(url, **kwargs):
        request = httpx.Request("POST", url)
        return httpx.Response(429, json={"error": "Rate limit exceeded"}, request=request)

    monkeypatch.setattr(httpx, "post", mock_post)

    with pytest.raises(RateLimitError):
        adapter.complete([Message(role=Role.USER, content="test")])
