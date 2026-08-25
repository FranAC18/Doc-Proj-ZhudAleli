from dataclasses import dataclass, field
from datetime import datetime, timezone
import time
from typing import Any
import uuid

from .models import UsageInfo


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


# Precios referenciales por 1M tokens (USD)
MODEL_PRICING_PER_1M = {
    # OpenAI
    "gpt-5.6-luna": {"input": 2.50, "output": 10.00},
    "gpt-5.6-sol": {"input": 1.25, "output": 5.00},
    "gpt-4o": {"input": 2.50, "output": 10.00},
    "gpt-4o-mini": {"input": 0.15, "output": 0.60},
    # DeepSeek
    "deepseek-chat": {"input": 0.14, "output": 0.28},
    "deepseek-reasoner": {"input": 0.55, "output": 2.19},
    "deepseek-v4": {"input": 0.20, "output": 0.50},
    # GLM (Z.AI)
    "glm-4": {"input": 0.10, "output": 0.10},
    "glm-5.2": {"input": 0.15, "output": 0.20},
    # Google Gemini
    "gemini-2.5-pro": {"input": 1.25, "output": 5.00},
    "gemini-2.5-flash": {"input": 0.075, "output": 0.30},
}


def estimate_cost(model_name: str, prompt_tokens: int, completion_tokens: int) -> float:
    """Calcula el costo estimado en USD a partir de tokens y tarifario."""
    clean_name = model_name.lower().strip()
    pricing = None
    for key, p in MODEL_PRICING_PER_1M.items():
        if key in clean_name:
            pricing = p
            break
    if not pricing:
        pricing = {"input": 1.0, "output": 2.0}

    cost_in = (prompt_tokens / 1_000_000) * pricing["input"]
    cost_out = (completion_tokens / 1_000_000) * pricing["output"]
    return round(cost_in + cost_out, 6)


@dataclass
class ExecutionTrace:
    trace_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    run_id: str = ""
    agent_name: str = "thesis-agent"
    provider: str = "unknown"
    model_name: str = "unknown"
    timestamp_utc: str = field(default_factory=utc_now)
    latency_ms: float = 0.0
    input_tokens: int = 0
    output_tokens: int = 0
    reasoning_tokens: int = 0
    estimated_cost_usd: float = 0.0
    tool_calls_count: int = 0
    status: str = "success"  # "success", "tool_error", "model_error", "timeout"
    error_message: str | None = None


class TelemetrySpan:
    """Context manager para medir latencias y capturar trazas de ejecución."""

    def __init__(self, trace: ExecutionTrace):
        self.trace = trace
        self.start_time = 0.0

    def __enter__(self) -> "TelemetrySpan":
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> None:
        self.trace.latency_ms = round((time.perf_counter() - self.start_time) * 1000, 2)
        if exc_val is not None:
            self.trace.status = "model_error"
            self.trace.error_message = str(exc_val)

    def record_usage(self, usage: UsageInfo) -> None:
        self.trace.input_tokens = usage.prompt_tokens
        self.trace.output_tokens = usage.completion_tokens
        self.trace.reasoning_tokens = usage.reasoning_tokens
        self.trace.estimated_cost_usd = estimate_cost(
            self.trace.model_name, usage.prompt_tokens, usage.completion_tokens
        )
