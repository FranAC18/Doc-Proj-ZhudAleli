from datetime import datetime, timezone
import json
from pathlib import Path
import sqlite3
from typing import Any

from .telemetry import ExecutionTrace


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class MemoryStore:
    """Memoria explícita: no se confía en que el LLM recuerde por sí solo."""

    def __init__(self, path: str):
        self.path = path
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        self.db = sqlite3.connect(path)
        self.db.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        self.db.executescript("""
        CREATE TABLE IF NOT EXISTS turns (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            kind TEXT NOT NULL,
            memory_key TEXT NOT NULL,
            value TEXT NOT NULL,
            confidence REAL NOT NULL DEFAULT 0.7,
            source TEXT NOT NULL,
            created_at TEXT NOT NULL,
            updated_at TEXT NOT NULL,
            UNIQUE(user_id, kind, memory_key)
        );
        CREATE TABLE IF NOT EXISTS lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            trigger TEXT NOT NULL,
            lesson TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'pending',
            source TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            event_type TEXT NOT NULL,
            payload TEXT NOT NULL,
            created_at TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS telemetry (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            trace_id TEXT NOT NULL,
            run_id TEXT NOT NULL,
            agent_name TEXT NOT NULL,
            provider TEXT NOT NULL,
            model_name TEXT NOT NULL,
            latency_ms REAL NOT NULL,
            input_tokens INTEGER NOT NULL,
            output_tokens INTEGER NOT NULL,
            reasoning_tokens INTEGER NOT NULL,
            estimated_cost_usd REAL NOT NULL,
            tool_calls_count INTEGER NOT NULL,
            status TEXT NOT NULL,
            error_message TEXT,
            created_at TEXT NOT NULL
        );
        """)
        self.db.commit()

    def add_turn(self, user_id: str, role: str, content: str) -> None:
        self.db.execute(
            "INSERT INTO turns(user_id, role, content, created_at) VALUES (?, ?, ?, ?)",
            (user_id, role, content, utc_now()),
        )
        self.db.commit()

    def recent_turns(self, user_id: str, limit: int = 12) -> list[dict[str, str]]:
        rows = self.db.execute(
            "SELECT role, content FROM turns WHERE user_id=? ORDER BY id DESC LIMIT ?",
            (user_id, limit),
        ).fetchall()
        return [{"role": row["role"], "content": row["content"]} for row in reversed(rows)]

    def remember(self, user_id: str, key: str, value: str, source: str = "agent") -> None:
        now = utc_now()
        self.db.execute("""
            INSERT INTO memories(user_id, kind, memory_key, value, source, created_at, updated_at)
            VALUES (?, 'fact', ?, ?, ?, ?, ?)
            ON CONFLICT(user_id, kind, memory_key) DO UPDATE SET
                value=excluded.value, source=excluded.source, updated_at=excluded.updated_at
        """, (user_id, key, value, source, now, now))
        self.db.commit()

    def search(self, user_id: str, query: str, limit: int = 8) -> list[dict[str, Any]]:
        terms = [term.strip().lower() for term in query.split() if term.strip()]
        if not terms:
            return []
        clauses = " OR ".join("lower(memory_key) LIKE ? OR lower(value) LIKE ?" for _ in terms)
        params: list[Any] = [user_id]
        for term in terms:
            like = f"%{term}%"
            params.extend([like, like])
        rows = self.db.execute(
            f"SELECT memory_key, value, confidence, source FROM memories WHERE user_id=? AND ({clauses}) ORDER BY updated_at DESC LIMIT ?",
            (*params, limit),
        ).fetchall()
        return [dict(row) for row in rows]

    def add_lesson(self, user_id: str, trigger: str, lesson: str, source: str = "tool-error") -> int:
        cur = self.db.execute(
            "INSERT INTO lessons(user_id, trigger, lesson, source, created_at) VALUES (?, ?, ?, ?, ?)",
            (user_id, trigger, lesson, source, utc_now()),
        )
        self.db.commit()
        return int(cur.lastrowid)

    def approved_lessons(self, user_id: str, limit: int = 8) -> list[dict[str, str]]:
        rows = self.db.execute(
            "SELECT trigger, lesson FROM lessons WHERE user_id=? AND status='approved' ORDER BY id DESC LIMIT ?",
            (user_id, limit),
        ).fetchall()
        return [dict(row) for row in rows]

    def pending_lessons(self, user_id: str) -> list[dict[str, Any]]:
        rows = self.db.execute(
            "SELECT id, trigger, lesson, source, created_at FROM lessons WHERE user_id=? AND status='pending' ORDER BY id",
            (user_id,),
        ).fetchall()
        return [dict(row) for row in rows]

    def approve_lesson(self, user_id: str, lesson_id: int) -> bool:
        cur = self.db.execute(
            "UPDATE lessons SET status='approved' WHERE id=? AND user_id=? AND status='pending'",
            (lesson_id, user_id),
        )
        self.db.commit()
        return cur.rowcount == 1

    def record_event(self, user_id: str, event_type: str, payload: dict[str, Any]) -> None:
        self.db.execute(
            "INSERT INTO events(user_id, event_type, payload, created_at) VALUES (?, ?, ?, ?)",
            (user_id, event_type, json.dumps(payload, ensure_ascii=False), utc_now()),
        )
        self.db.commit()

    def record_telemetry(self, trace: ExecutionTrace) -> None:
        self.db.execute(
            """
            INSERT INTO telemetry(
                trace_id, run_id, agent_name, provider, model_name,
                latency_ms, input_tokens, output_tokens, reasoning_tokens,
                estimated_cost_usd, tool_calls_count, status, error_message, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                trace.trace_id,
                trace.run_id,
                trace.agent_name,
                trace.provider,
                trace.model_name,
                trace.latency_ms,
                trace.input_tokens,
                trace.output_tokens,
                trace.reasoning_tokens,
                trace.estimated_cost_usd,
                trace.tool_calls_count,
                trace.status,
                trace.error_message,
                trace.timestamp_utc,
            ),
        )
        self.db.commit()

    def get_telemetry_summary(self) -> list[dict[str, Any]]:
        rows = self.db.execute(
            """
            SELECT
                provider,
                model_name,
                COUNT(*) as total_calls,
                ROUND(AVG(latency_ms), 2) as avg_latency_ms,
                SUM(input_tokens) as total_input_tokens,
                SUM(output_tokens) as total_output_tokens,
                ROUND(SUM(estimated_cost_usd), 4) as total_cost_usd
            FROM telemetry
            GROUP BY provider, model_name
            ORDER BY total_calls DESC
            """
        ).fetchall()
        return [dict(row) for row in rows]

    def close(self) -> None:
        self.db.close()
