from typing import Any, Iterator
import uuid

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


class GeminiAdapter(BaseHTTPAdapter):
    """Adaptador para Google Gemini API con nombre de modelo configurable."""

    def __init__(
        self,
        base_url: str = "https://generativelanguage.googleapis.com/v1beta",
        api_key: str = "",
        model_name: str = "gemini-2.5-pro",
        timeout: float = 60.0,
    ):
        super().__init__(base_url=base_url, api_key=api_key, model_name=model_name, timeout=timeout)
        self.endpoint = f"{self.base_url}/models/{self.model_name}:generateContent"

    @property
    def provider_name(self) -> str:
        return "google"

    @property
    def declared_capabilities(self) -> set[ModelCapability]:
        return {
            ModelCapability.TOOL_CALLING,
            ModelCapability.PARALLEL_TOOL_CALLING,
            ModelCapability.STRUCTURED_OUTPUTS,
            ModelCapability.NATIVE_JSON_SCHEMA,
            ModelCapability.SYSTEM_MESSAGES,
            ModelCapability.REASONING_TOKENS,
            ModelCapability.VISION,
            ModelCapability.EXTENDED_CONTEXT_1M,
            ModelCapability.STREAMING,
        }

    @property
    def verified_capabilities(self) -> set[ModelCapability]:
        return {
            ModelCapability.TOOL_CALLING,
            ModelCapability.SYSTEM_MESSAGES,
        }

    def _convert_tools_to_declarations(self, tools: list[dict[str, Any]]) -> list[dict[str, Any]]:
        declarations = []
        for t in tools:
            func = t.get("function", t)
            decl = {
                "name": func.get("name", ""),
                "description": func.get("description", ""),
                "parameters": func.get("parameters", {}),
            }
            declarations.append(decl)
        return [{"functionDeclarations": declarations}]

    def _format_contents(self, messages: list[Message]) -> tuple[dict[str, Any] | None, list[dict[str, Any]]]:
        system_instruction = None
        contents = []

        for msg in messages:
            if msg.role == Role.SYSTEM:
                content_text = msg.content if isinstance(msg.content, str) else "\n".join(
                    p.text for p in msg.content if p.type == "text" and p.text
                )
                system_instruction = {"parts": [{"text": content_text}]}
                continue

            role = "model" if msg.role == Role.ASSISTANT else "user"
            parts: list[dict[str, Any]] = []

            if isinstance(msg.content, str) and msg.content:
                parts.append({"text": msg.content})
            elif isinstance(msg.content, list):
                for p in msg.content:
                    if p.type == "text" and p.text:
                        parts.append({"text": p.text})

            if msg.role == Role.TOOL:
                role = "user"
                content_val = msg.content
                if isinstance(content_val, str):
                    try:
                        import json
                        content_val = json.loads(content_val)
                    except Exception:
                        pass
                parts.append({
                    "functionResponse": {
                        "name": msg.name or "unknown",
                        "response": {"output": content_val},
                    }
                })

            for call in msg.tool_calls:
                parts.append({
                    "functionCall": {
                        "name": call.name,
                        "args": call.arguments,
                    }
                })

            if parts:
                contents.append({"role": role, "parts": parts})

        return system_instruction, contents

    def complete(
        self,
        messages: list[Message] | list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> ModelResponse:
        norm_messages = normalize_messages(messages)
        system_instruction, contents = self._format_contents(norm_messages)

        payload: dict[str, Any] = {
            "contents": contents,
            "generationConfig": {
                "temperature": kwargs.get("temperature", 0.2),
            },
        }
        if system_instruction:
            payload["systemInstruction"] = system_instruction
        if tools:
            payload["tools"] = self._convert_tools_to_declarations(tools)

        headers = {
            "Content-Type": "application/json",
            "x-goog-api-key": self.api_key,
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
            candidate = data["candidates"][0]
            parts = candidate.get("content", {}).get("parts", [])
        except httpx.HTTPStatusError as exc:
            self._handle_http_error(exc, status_code=exc.response.status_code)
        except (httpx.HTTPError, KeyError, IndexError, ValueError) as exc:
            raise ModelError(f"Fallo al consultar el modelo Gemini ({self.model_name}): {exc}") from exc

        text_parts = []
        calls = []
        for part in parts:
            if "text" in part:
                text_parts.append(part["text"])
            if "functionCall" in part:
                fc = part["functionCall"]
                calls.append(
                    ToolCall(
                        id=str(uuid.uuid4()),
                        name=fc.get("name", ""),
                        arguments=fc.get("args", {}),
                    )
                )

        usage_raw = data.get("usageMetadata", {})
        usage = UsageInfo(
            prompt_tokens=usage_raw.get("promptTokenCount", 0),
            completion_tokens=usage_raw.get("candidatesTokenCount", 0),
            total_tokens=usage_raw.get("totalTokenCount", 0),
        )

        return ModelResponse(
            content="".join(text_parts),
            tool_calls=calls,
            finish_reason=candidate.get("finishReason", "STOP").lower(),
            usage=usage,
            raw=data,
        )

    def stream(
        self,
        messages: list[Message] | list[dict[str, Any]],
        tools: list[dict[str, Any]] | None = None,
        **kwargs: Any,
    ) -> Iterator[ModelResponse]:
        full_res = self.complete(messages, tools, **kwargs)
        yield full_res
