from typing import Any, Protocol
import json

import httpx

from .models import ModelError, ModelReply, ToolCall


class ChatModel(Protocol):
    def complete(self, messages: list[dict[str, Any]], tools: list[dict[str, Any]]) -> ModelReply:
        ...


class OpenAICompatibleModel:
    """Adaptador para APIs que implementan /chat/completions.

    El agente solo conoce este contrato. La URL, la clave y el nombre del modelo
    viven en configuración, no en la lógica de negocio.
    """

    def __init__(self, base_url: str, api_key: str, model_name: str, timeout: float = 60.0):
        self.url = base_url.rstrip("/") + "/chat/completions"
        self.api_key = api_key
        self.model_name = model_name
        self.timeout = timeout

    def complete(self, messages: list[dict[str, Any]], tools: list[dict[str, Any]]) -> ModelReply:
        payload: dict[str, Any] = {
            "model": self.model_name,
            "messages": messages,
            "temperature": 0.2,
        }
        if tools:
            payload["tools"] = tools
            payload["tool_choice"] = "auto"

        try:
            response = httpx.post(
                self.url,
                headers={"Authorization": f"Bearer {self.api_key}"},
                json=payload,
                timeout=self.timeout,
            )
            response.raise_for_status()
            data = response.json()
            message = data["choices"][0]["message"]
        except (httpx.HTTPError, KeyError, IndexError, ValueError) as exc:
            raise ModelError(f"Fallo al consultar el modelo: {exc}") from exc

        calls: list[ToolCall] = []
        for call in message.get("tool_calls", []) or []:
            function = call.get("function", {})
            arguments = function.get("arguments", {})
            if isinstance(arguments, str):
                try:
                    arguments = json.loads(arguments)
                except json.JSONDecodeError as exc:
                    raise ModelError(f"Argumentos JSON inválidos para {function.get('name')}") from exc
            if not isinstance(arguments, dict):
                raise ModelError(f"Los argumentos de {function.get('name')} no son un objeto JSON")
            calls.append(ToolCall(
                id=call.get("id", function.get("name", "unknown")),
                name=function.get("name", ""),
                arguments=arguments,
            ))

        return ModelReply(content=message.get("content") or "", tool_calls=calls, raw=data)
