"""Validate the shared Codex/OpenCode repository contract.

The validator is deliberately read-only. It checks structure, routing, operational state and
selected navigation links; it never changes Git, the vault or host configuration.
"""

from __future__ import annotations

import argparse
import ast
import json
import re
import subprocess
import sys
import tomllib
from pathlib import Path


ROLE_NAMES = (
    "requirements",
    "architect",
    "ux",
    "frontend",
    "implementer",
    "reviewer",
    "researcher",
    "documenter",
    "git-manager",
)
TASK_TYPES = (
    "architecture",
    "planning",
    "implementation",
    "frontend",
    "debugging",
    "research",
    "review",
    "documentation",
)
MODEL_PROFILES = {
    "reasoning_max",
    "coding_efficient",
    "frontend_strong",
    "research_efficient",
    "documentation_economy",
}
COMMAND_NAMES = ("route", "architect", "implement", "frontend", "review", "research")
ACTIVE_STATUSES = {"in-progress", "in_progress", "partially-complete", "partially_complete"}
IGNORED_LINK_PARTS = {".git", "node_modules", ".venv", ".pytest_cache"}


def discover_root(start: Path) -> Path | None:
    current = start.resolve()
    for candidate in (current, *current.parents):
        if (candidate / "AGENTS.md").is_file() and (
            candidate / ".specify" / "memory" / "constitution.md"
        ).is_file():
            return candidate
    return None


def git_value(root: Path, *args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    return result.stdout.strip()


def parse_scalar(value: str) -> object:
    value = value.strip()
    if value in {"", "null", "Null", "NULL", "~"}:
        return None
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    try:
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value.strip('"\'')


def frontmatter(path: Path) -> dict[str, object]:
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return {}
    if not lines or lines[0].strip() != "---":
        return {}
    fields: dict[str, object] = {}
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = parse_scalar(match.group(2))
    return fields


def route_link_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("[[") and target.endswith("]]"):
        target = target[2:-2]
    target = target.split("|", 1)[0].split("#", 1)[0].strip()
    return target.replace("\\", "/")


def resolve_link(root: Path, source: Path, raw: str) -> Path | None:
    target = route_link_target(raw)
    if not target or target.startswith(("#", "http:", "https:", "mailto:", "{{", "<")):
        return None
    target_path = Path(target)
    candidates: list[Path] = []
    candidates.append(source.parent / target_path)
    candidates.append(root / target_path)
    if not target_path.suffix:
        candidates.extend(
            [source.parent / f"{target}.md", root / f"{target}.md", root / "docs" / f"{target}.md"]
        )
    for candidate in candidates:
        if candidate.is_file():
            return candidate.resolve()
        if not candidate.suffix and candidate.with_suffix(".md").is_file():
            return candidate.with_suffix(".md").resolve()
    name = target_path.name if target_path.suffix else f"{target_path.name}.md"
    for candidate in root.rglob(name):
        if candidate.is_file() and not any(part in IGNORED_LINK_PARTS for part in candidate.parts):
            return candidate.resolve()
    return None


def broken_links(root: Path, files: list[Path]) -> list[str]:
    issues: list[str] = []
    for path in files:
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        raw_links = re.findall(r"\[\[([^\]]+)\]\]|\]\(([^)]+)\)", text)
        for wikilink, markdown_link in raw_links:
            raw = wikilink or markdown_link
            target = route_link_target(str(raw))
            if not target or target.startswith(("#", "http:", "https:", "mailto:", "{{", "<")):
                continue
            if resolve_link(root, path, str(raw)) is None:
                issues.append(f"{path.relative_to(root)} -> {target}")
    return issues


def validate_routes(root: Path) -> tuple[str | None, list[str]]:
    route_file = root / "tools" / "agent-routes.toml"
    warnings: list[str] = []
    if not route_file.is_file():
        return "Falta tools/agent-routes.toml.", warnings
    try:
        with route_file.open("rb") as handle:
            config = tomllib.load(handle)
    except (OSError, tomllib.TOMLDecodeError) as exc:
        return f"No se pudo leer tools/agent-routes.toml: {exc}", warnings

    profiles = config.get("model_profiles", {})
    missing_profiles = MODEL_PROFILES - set(profiles)
    if missing_profiles:
        return f"Faltan perfiles de modelo: {', '.join(sorted(missing_profiles))}.", warnings

    task_types = config.get("task_types", {})
    if set(task_types) != set(TASK_TYPES):
        return "task_types no cubre exactamente las categorías requeridas.", warnings
    for task_name, task in task_types.items():
        required = ("agent", "risk", "reasoning", "model_profile", "context", "review", "delegation")
        missing = [key for key in required if key not in task]
        if missing:
            return f"Faltan campos en task_types.{task_name}: {', '.join(missing)}.", warnings
        if task["model_profile"] not in profiles:
            return f"Perfil inexistente en task_types.{task_name}: {task['model_profile']}.", warnings
        agent = task["agent"]
        if not (root / ".opencode" / "agents" / f"{agent}.md").is_file():
            return f"Agente OpenCode inexistente para task_types.{task_name}: {agent}.", warnings
        if not (root / ".codex" / "agents" / f"{agent}.toml").is_file():
            warnings.append(f"No existe adaptador Codex para el agente {agent}.")
        if not isinstance(task["context"], list) or not task["context"]:
            return f"Contexto vacío en task_types.{task_name}.", warnings

    expected_roles = set(ROLE_NAMES) | {"coordinator"}
    routes = config.get("routes", {})
    if set(routes) != expected_roles:
        return "Las rutas no cubren exactamente los roles universales.", warnings
    for route_name, route in routes.items():
        for lane in ("primary", "fallback"):
            if not all(key in route.get(lane, {}) for key in ("host", "provider", "model")):
                return f"Falta host/provider/model en routes.{route_name}.{lane}.", warnings
            if route[lane]["host"] == "openchamber":
                return "OpenChamber no puede ser host de configuración en agent-routes.toml.", warnings
            if route[lane]["model"] not in profiles:
                return f"Perfil de modelo inexistente en routes.{route_name}.{lane}.", warnings
    return None, warnings


def validate_state(root: Path) -> tuple[list[str], list[str], dict[str, object]]:
    errors: list[str] = []
    warnings: list[str] = []
    state_path = root / "docs" / "bitacora" / "ESTADO-ACTIVO.md"
    state = frontmatter(state_path)
    branch = git_value(root, "branch", "--show-current")
    head = git_value(root, "rev-parse", "HEAD")
    if not state:
        return ["No se pudo leer el frontmatter de ESTADO-ACTIVO.md."], warnings, {}

    documented_branch = state.get("branch")
    documented_head = state.get("head") or state.get("last_commit")
    if documented_branch and branch and documented_branch != branch:
        errors.append(f"Rama desincronizada: estado={documented_branch}, Git={branch}.")
    if documented_head and head and str(documented_head) != head:
        errors.append(f"HEAD desincronizado: estado={documented_head}, Git={head}.")

    status = str(state.get("status") or "")
    task_id = state.get("task_id")
    active_task = state.get("active_task")
    if status in ACTIVE_STATUSES and not task_id:
        errors.append("El estado activo requiere task_id cuando está en progreso.")
    if active_task not in {None, "", task_id}:
        errors.append("active_task y task_id no coinciden.")
    if status in ACTIVE_STATUSES and not state.get("next_action"):
        warnings.append("La tarea activa no tiene next_action.")

    last_handoff = state.get("last_handoff")
    checkpoint_path = resolve_link(root, state_path, str(last_handoff)) if last_handoff else None
    if last_handoff and checkpoint_path is None:
        errors.append(f"No se puede resolver last_handoff: {last_handoff}.")
    if checkpoint_path:
        checkpoint = frontmatter(checkpoint_path)
        if status in ACTIVE_STATUSES and checkpoint.get("status") == "completed":
            warnings.append(
                f"El último checkpoint está completed y no representa la tarea activa: "
                f"{checkpoint_path.relative_to(root)}."
            )
        if documented_branch and checkpoint.get("branch") and checkpoint["branch"] != documented_branch:
            warnings.append("El checkpoint enlazado pertenece a otra rama.")
        checkpoint_commit = checkpoint.get("commit_hash") or checkpoint.get("commit")
        if documented_head and checkpoint_commit and str(checkpoint_commit) not in {str(documented_head), "pending"}:
            warnings.append("El checkpoint enlazado pertenece a un commit anterior al HEAD documentado.")

    return errors, warnings, {
        "documented_branch": documented_branch,
        "documented_head": documented_head,
        "git_branch": branch,
        "git_head": head,
        "task_id": task_id,
        "status": status,
        "last_handoff": last_handoff,
    }


def validate_mocs(root: Path, head: str | None) -> list[str]:
    warnings: list[str] = []
    moc = root / "docs" / "00-inicio" / "moc-agentes-y-skills.md"
    if not moc.is_file():
        return ["Falta el MOC de agentes y skills."]
    text = moc.read_text(encoding="utf-8")
    verified = re.search(r"verified_against_commit:\s*[\"']?([0-9a-f]+)", text)
    if verified and head and not head.startswith(verified.group(1)):
        warnings.append(f"MOC de agentes/skills verificado contra commit antiguo: {verified.group(1)}.")
    actual_skills = sorted(
        path.parent.name
        for path in (root / ".agents" / "skills").glob("*/SKILL.md")
    )
    missing = [name for name in actual_skills if name not in text]
    if missing:
        warnings.append("MOC de skills omite: " + ", ".join(missing) + ".")
    return warnings


def validate(root: Path) -> dict[str, object]:
    required = [
        "AGENTS.md",
        ".specify/memory/constitution.md",
        "docs/context/context-index.md",
        "docs/context/feature-index.md",
        "docs/00-inicio/00-dashboard.md",
        "docs/bitacora/ESTADO-ACTIVO.md",
        "docs/templates/PLANTILLA-HANDOFF-UNIVERSAL.md",
        "docs/architecture/CONTRATO-UNIVERSAL-ORQUESTADORES.md",
        "docs/architecture/RUTAS-MODELOS-IA.md",
        ".agents/rules/00-zhud-aleli-context.md",
        ".agents/rules/10-zhud-aleli-handoff.md",
        ".agents/skills/zhud-aleli-context/SKILL.md",
        ".agents/skills/zhud-aleli-handoff/SKILL.md",
        ".agents/skills/zhud-aleli-documenter/SKILL.md",
        ".agents/skills/zhud-aleli-git-manager/SKILL.md",
        ".opencode/README.md",
        "scripts/agent.ps1",
        "scripts/agent.sh",
    ]
    required.extend(f"agents/tesis/roles/{name}.md" for name in ROLE_NAMES)
    required.extend(f".opencode/agents/{name}.md" for name in ROLE_NAMES)
    required.extend(f".codex/agents/{name}.toml" for name in ROLE_NAMES)
    required.extend(f".opencode/commands/{name}.md" for name in COMMAND_NAMES)
    missing = [path for path in required if not (root / path).is_file()]

    route_error, route_warnings = validate_routes(root)
    state_errors, state_warnings, state = validate_state(root)
    branch = state.get("git_branch") or git_value(root, "branch", "--show-current")
    head = state.get("git_head") or git_value(root, "rev-parse", "HEAD")

    link_files = [
        root / "docs" / "context" / "context-index.md",
        root / "docs" / "context" / "feature-index.md",
        root / "docs" / "bitacora" / "ESTADO-ACTIVO.md",
        root / "docs" / "00-inicio" / "00-dashboard.md",
        root / "docs" / "00-inicio" / "ESTADOS-Y-PROGRESO.md",
        root / "docs" / "architecture" / "RUTAS-MODELOS-IA.md",
    ]
    link_warnings = ["Enlace operativo no resuelto: " + issue for issue in broken_links(root, link_files)]
    warnings = route_warnings + state_warnings + validate_mocs(root, head) + link_warnings
    status = git_value(root, "status", "--short", "--branch")
    errors = state_errors
    if route_error:
        errors.append(route_error)
    result = {
        "ok": not missing and not errors,
        "root": str(root),
        "vault": str(root),
        "branch": branch,
        "head": head,
        "missing": missing,
        "errors": errors,
        "warnings": warnings,
        "state": state,
        "git_status": status,
        "hosts": {
            "codex": (root / ".codex" / "agents").is_dir(),
            "opencode": (root / ".opencode" / "agents").is_dir(),
            "openchamber": (root / ".opencode" / "agents").is_dir(),
            "antigravity": (root / ".agents" / "rules").is_dir(),
        },
    }
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="Imprime el resultado como JSON")
    args = parser.parse_args()

    root = discover_root(Path.cwd())
    if root is None:
        payload = {
            "ok": False,
            "root": None,
            "error": "No se encontró una raíz con AGENTS.md y .specify/memory/constitution.md.",
        }
        if args.json:
            print(json.dumps(payload, ensure_ascii=False, indent=2))
        else:
            print(payload["error"], file=sys.stderr)
        return 2

    payload = validate(root)
    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(f"Raíz universal: {payload['root']}")
        print(f"Vault Obsidian: {payload['vault']}")
        print(f"Rama: {payload['branch'] or 'no disponible'}")
        print(f"HEAD: {payload['head'] or 'no disponible'}")
        if payload["missing"]:
            print("Faltantes:")
            for path in payload["missing"]:
                print(f"- {path}")
        if payload["errors"]:
            print("Errores:")
            for error in payload["errors"]:
                print(f"- {error}")
        if payload["warnings"]:
            print("Advertencias:")
            for warning in payload["warnings"]:
                print(f"- {warning}")
        if not payload["missing"] and not payload["errors"]:
            print("Contrato universal: OK")
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
