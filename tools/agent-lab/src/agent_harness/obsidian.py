from datetime import date
from pathlib import Path
import re
from typing import Any

from .paths import resolve_vault_dir


class ObsidianStore:
    """Puente seguro y pequeño entre el arnés y un vault Markdown."""

    def __init__(self, vault_dir: str, *, project_root: str | Path | None = None):
        if project_root is not None:
            project = Path(project_root).resolve()
            self.root = resolve_vault_dir(vault_dir, project)
        else:
            self.root = Path(vault_dir).resolve()
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, relative_path: str) -> Path:
        candidate = (self.root / relative_path).resolve()
        if candidate != self.root and self.root not in candidate.parents:
            raise ValueError("La nota está fuera del vault permitido")
        if candidate.suffix.lower() != ".md":
            raise ValueError("Solo se permiten notas Markdown")
        return candidate

    @staticmethod
    def _slug(value: str) -> str:
        value = value.lower().strip()
        value = re.sub(r"[^a-z0-9áéíóúñü]+", "-", value)
        return value.strip("-") or "nota"

    @staticmethod
    def _frontmatter(properties: dict[str, Any]) -> str:
        lines = ["---"]
        for key, value in properties.items():
            if isinstance(value, list):
                lines.append(f"{key}:")
                lines.extend(f"  - {item}" for item in value)
            else:
                safe = str(value).replace("\n", " ").replace("\r", " ")
                lines.append(f"{key}: {safe}")
        lines.append("---")
        return "\n".join(lines)

    def write_note(
        self,
        relative_path: str,
        properties: dict[str, Any],
        body: str,
        *,
        overwrite: bool = False,
    ) -> str:
        path = self._path(relative_path)
        if path.exists() and not overwrite:
            raise FileExistsError(f"La nota ya existe y no se sobrescribirá: {relative_path}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(self._frontmatter(properties) + "\n\n" + body.strip() + "\n", encoding="utf-8")
        return path.relative_to(self.root).as_posix()

    def save_session_summary(self, sprint: str, title: str, summary: str, next_steps: list[str]) -> dict[str, Any]:
        today = date.today().isoformat()
        slug = self._slug(title)
        relative = f"docs/bitacora/sesiones/{today}-{slug}.md"
        body = f"""# {title}

## Resumen

{summary}

## Próximos pasos permitidos

""" + "\n".join(f"- [ ] {step}" for step in next_steps)
        path = self.write_note(relative, {
            "title": title,
            "type": "session",
            "sprint": sprint,
            "status": "closed",
            "date": today,
            "tags": ["session", sprint.lower()],
        }, body)
        return {"saved": True, "path": path}

    def save_progress_checkpoint(
        self,
        sprint: str,
        title: str,
        status: str,
        progress: int,
        completed: list[str],
        remaining: list[str],
        blockers: list[str],
        next_action: str,
        evidence: list[str] | None = None,
    ) -> dict[str, Any]:
        allowed = {"planned", "in-progress", "partially-complete", "blocked", "completed", "cancelled"}
        if status not in allowed:
            raise ValueError(f"Estado inválido: {status}")
        if not 0 <= progress <= 100:
            raise ValueError("El progreso debe estar entre 0 y 100")
        evidence = evidence or []
        if status == "completed":
            if progress != 100:
                raise ValueError("Un checkpoint completed debe tener progreso 100")
            if remaining or blockers:
                raise ValueError("Un checkpoint completed no puede tener pendientes ni bloqueos")
            if not completed or not evidence:
                raise ValueError("Un checkpoint completed requiere trabajo completado y evidencia")
        today = date.today().isoformat()
        slug = self._slug(title)
        relative = f"docs/bitacora/checkpoints/{today}-{slug}.md"
        completed_text = "\n".join(f"- [x] {item}" for item in completed) or "- Ninguno."
        remaining_text = "\n".join(f"- [ ] {item}" for item in remaining) or "- Ninguno."
        blockers_text = "\n".join(f"- {item}" for item in blockers) if blockers else "- Ninguno."
        evidence_text = "\n".join(f"- {item}" for item in evidence) if evidence else "- Pendiente."
        body = f"""# Checkpoint - {title}

## Estado

`{status}` - {progress}% orientativo

## Completado

{completed_text}

## Pendiente

{remaining_text}

## Bloqueos

{blockers_text}

## Evidencia

{evidence_text}

## Próxima acción

{next_action}
"""
        path = self.write_note(relative, {
            "title": title,
            "type": "checkpoint",
            "status": status,
            "sprint": sprint,
            "progress": progress,
            "date": today,
            "tags": ["checkpoint", sprint.lower()],
        }, body)
        return {"saved": True, "path": path, "status": status, "progress": progress}

    def propose_requirement(self, identifier: str, title: str, actor: str, description: str, criteria: list[str]) -> dict[str, Any]:
        slug = self._slug(title)
        relative = f"docs/requirements/proposals/{identifier}-{slug}.md"
        body = f"""# {identifier} - {title}

## Actor

{actor}

## Descripción propuesta

{description}

## Criterios de aceptación propuestos

""" + "\n".join(f"- [ ] {criterion}" for criterion in criteria) + "\n\n## Validación\n\nPendiente de confirmar con la organización y la dirección de tesis."
        path = self.write_note(relative, {
            "id": identifier,
            "title": title,
            "type": "requirement",
            "status": "proposed",
            "source": "agent-detected",
        }, body)
        return {"saved": True, "status": "proposed", "path": path}

    def propose_decision(self, identifier: str, title: str, question: str, impact: str) -> dict[str, Any]:
        slug = self._slug(title)
        relative = f"docs/decisions/proposals/{identifier}-{slug}.md"
        body = f"""# {identifier} - {title}

## Pregunta o decisión propuesta

{question}

## Impacto

{impact}

## Estado

Pendiente de aprobación del tesista y, cuando corresponda, de la directora u organización.
"""
        path = self.write_note(relative, {
            "id": identifier,
            "title": title,
            "type": "decision",
            "status": "proposed",
            "source": "agent-detected",
        }, body)
        return {"saved": True, "status": "proposed", "path": path}
