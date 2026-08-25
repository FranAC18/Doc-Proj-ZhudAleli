"""Validate the repository contract shared by Codex, OpenCode and Antigravity.

This command is deliberately read-only. It does not change Git, the vault or any host
configuration. It can be run from the repository root or any child directory.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
import tomllib
from pathlib import Path


ROLE_NAMES = (
    "requirements",
    "architect",
    "ux",
    "implementer",
    "reviewer",
    "documenter",
    "git-manager",
)


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


def validate(root: Path) -> dict[str, object]:
    required = [
        "AGENTS.md",
        ".specify/memory/constitution.md",
        "docs/00-inicio/00-dashboard.md",
        "docs/bitacora/ESTADO-ACTIVO.md",
        "docs/templates/PLANTILLA-HANDOFF-UNIVERSAL.md",
        "docs/architecture/CONTRATO-UNIVERSAL-ORQUESTADORES.md",
        "docs/architecture/RUTAS-MODELOS-IA.md",
        "tools/agent-routes.toml",
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
    missing = [path for path in required if not (root / path).is_file()]

    canonical_roles = [
        f"agents/tesis/roles/{name}.md" for name in ROLE_NAMES
    ]
    missing.extend(path for path in canonical_roles if not (root / path).is_file())

    opencode_agents = [
        f".opencode/agents/{name}.md" for name in ROLE_NAMES
    ]
    missing.extend(path for path in opencode_agents if not (root / path).is_file())

    route_error = None
    route_file = root / "tools" / "agent-routes.toml"
    if route_file.is_file():
        try:
            with route_file.open("rb") as handle:
                routes = tomllib.load(handle)
            route_names = set(routes.get("routes", {}))
            if route_names != {
                "coordinator",
                "requirements",
                "architect",
                "ux",
                "implementer",
                "reviewer",
                "documenter",
                "git_manager",
            }:
                route_error = "Las rutas no cubren exactamente los roles universales."
            else:
                for route_name, route in routes["routes"].items():
                    for lane in ("primary", "fallback"):
                        if not all(key in route.get(lane, {}) for key in ("host", "provider", "model")):
                            route_error = f"Falta host/provider/model en routes.{route_name}.{lane}."
                            break
                    if route_error:
                        break
        except (OSError, tomllib.TOMLDecodeError) as exc:
            route_error = f"No se pudo leer tools/agent-routes.toml: {exc}"

    status = git_value(root, "status", "--short", "--branch")
    branch = git_value(root, "branch", "--show-current")
    result = {
        "ok": not missing,
        "root": str(root),
        "vault": str(root),
        "branch": branch,
        "missing": missing,
        "route_error": route_error,
        "git_status": status,
        "hosts": {
            "codex": (root / ".codex" / "agents").is_dir(),
            "opencode": (root / ".opencode" / "agents").is_dir(),
            "openchamber": (root / ".opencode" / "agents").is_dir(),
            "antigravity": (root / ".agents" / "rules").is_dir(),
        },
    }
    result["ok"] = not missing and route_error is None
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
        print("Hosts configurados: " + ", ".join(
            name for name, enabled in payload["hosts"].items() if enabled
        ))
        if payload["missing"]:
            print("Faltantes:")
            for path in payload["missing"]:
                print(f"- {path}")
        if payload["route_error"]:
            print(f"Rutas: {payload['route_error']}")
        if not payload["missing"] and not payload["route_error"]:
            print("Contrato universal: OK")
    return 0 if payload["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
