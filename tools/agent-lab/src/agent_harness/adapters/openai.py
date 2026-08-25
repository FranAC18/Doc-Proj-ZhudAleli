from typing import Any, Iterator
import json

import httpx

from ..models import (
    Message,
    ModelCapability,
    ModelError,
    ModelResponse,
    Role,
    ToolCall,
    UsageInfo,
)
from .base import BaseHTTPAdapter, normalize_messages


class OpenAIAdapter(BaseHTTPAdapter):
    """Adaptador para OpenAI (GPT-5.6 Sol / GPT-5.6 Luna / GPT-4o) y APIs compatibles con /chat/completions."""

    def __init__(
        self,
        base_url: str = "https://api.openai.com/v1",
        api_key: str = "",
        model_name: str = "gpt-5.6-luna",
        timeout: float = 60.0,
    ):
        super().__init__(base_url=base_url, api_key=api_key, model_name=model_name, timeout=timeout)
        self.endpoint = f"{self.base_url}/chat/completions"

    @property
    def provider_name(self) -> str:
        return "openai"

    @property
    def declared_capabilities(self) -> set[ModelCapability]:
        return {
            ModelCapability.TOOL_CALLING,
            ModelCapability.PARALLEL_TOOL_CALLING,
            ModelCapability.STRUCTURED_OUTPUTS,
            ModelCapability.NATIVE_JSON_SCHEMA,
            ModelCapability.SYSTEM_MESSAGES,
            ModelCapability.REASONING_TOKENS,
            ModelCapability.STREAMING,
        }

    @property
    def verified_capabilities(self) -> set[ModelCapability]:
        return {
            ModelCapability.TOOL_CALLING,
            ModelCapability.SYSTEM_MESSAGES,
        }

    def _format_messages(self, messages: list[Message]) -> list[dict[str, Any]]:
        formatted = []
        for msg in messages:
            entry: dict[str, Any] = {"role": msg.role.value}
            if isinstance(msg.content, str):
                entry["content"] = msg.content
            elif isinstance(msg.content, list):
                # Soporte para ContentPart estructurado
                entry["content"] = [
                    {"type": p.type, "text": p.text} if p.type == "text" else p.media_data
                    for p in msg.content
                ]

            if msg.name:
                entry["name"] = msg.name
            if msg.tool_call_id:
                entry["tool_call_id"] = msg.tool_call_id
            if msg.tool_calls:
                entry["tool_calls"] = [
                    {
                        "id": call.id,
                        "type": "function",
                        "function": {
                            "name": call.name,
                            "arguments": json.dumps(call.arguments, ensure_ascii=False)
                            if isinstance(call.arguments, dict)
                            else str(call.arguments),
                        },
                    }
                    for call in msg.tool_calls
                ]
            formatted.append(entry)
        return formatted

    def complete(
        self,
        messages: list[Message] | list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> ModelResponse:
        norm_messages = normalize_messages(messages)
        payload: dict[str, Any] = {
            "model": self.model_name,
            "messages": self._format_messages(norm_messages),
            "temperature": kwargs.get("temperature", 0.2),
        }
        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = kwargs.get("tool_choice", "auto")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }

        try:
            response = httpx.post(
                self.endpoint,
                headers=headers,
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json()
            choice = data["choices"][0]
            message = choice["message"]
        except httpx.HTTPStatusError as exc:
            self._handle_http_error(exc, status_code=exc.response.status_code)
        except (httpx.HTTPError, KeyError, IndexError, ValueError) as exc:
            raise ModelError(f"Fallo al consultar el modelo OpenAI ({self.model_name}): {exc}") from exc

        calls: list[ToolCall] = []
        for call in message.get("tool_calls", []) or []:
            func = call.get("function", {})
            raw_args = func.get("arguments", {})
            if isinstance(raw_args, str):
                try:
                    arguments = json.loads(raw_args)
                except json.JSONDecodeError as exc:
                    raise ModelError(f"Argumentos JSON inválidos para {func.get('name')}") from exc
            elif isinstance(raw_args, dict):
                arguments = raw_args
            else:
                raise ModelError(f"Los argumentos de {func.get('name')} no son válidos")

            calls.append(
                ToolCall(
                    id=call.get("id", func.get("name", "unknown")),
                    name=func.get("name", ""),
                    arguments=arguments,
                )
            )

        usage_raw = data.get("usage", {})
        usage = UsageInfo(
            prompt_tokens=usage_raw.get("prompt_tokens", 0),
            completion_tokens=usage_raw.get("completion_tokens", 0),
            total_tokens=usage_raw.get("total_tokens", 0),
            reasoning_tokens=usage_raw.get("completion_tokens_details", {}).get("reasoning_tokens", 0),
        )

        return ModelResponse(
            content=message.get("content") or "",
            tool_calls=calls,
            reasoning_content=message.get("reasoning_content"),
            finish_reason=choice.get("finish_reason", "stop"),
            usage=usage,
            raw=data,
        )

    def stream(
        self,
        messages: list[Message] | list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> Iterator[ModelResponse]:
        # Para compatibilidad streaming
        full_res = self.complete(messages, tools, **kwargs)
        yield full_res
