from pathlib import Path
import tomllib


PROJECT_ROOT = Path(__file__).resolve().parents[3]


def test_universal_contract_has_canonical_roles_and_host_adapters():
    required = [
        "AGENTS.md",
        ".specify/memory/constitution.md",
        "docs/architecture/CONTRATO-UNIVERSAL-ORQUESTADORES.md",
        "docs/architecture/RUTAS-MODELOS-IA.md",
        "docs/templates/PLANTILLA-HANDOFF-UNIVERSAL.md",
        "docs/bitacora/ESTADO-ACTIVO.md",
        "docs/context/context-index.md",
        "docs/context/feature-index.md",
        ".agents/rules/00-zhud-aleli-context.md",
        ".agents/rules/10-zhud-aleli-handoff.md",
        ".agents/skills/zhud-aleli-context/SKILL.md",
        ".agents/skills/zhud-aleli-handoff/SKILL.md",
        ".agents/skills/zhud-aleli-documenter/SKILL.md",
        ".agents/skills/zhud-aleli-git-manager/SKILL.md",
        ".opencode/README.md",
        "tools/agent-routes.toml",
    ]
    role_names = (
        "requirements",
        "architect",
        "ux",
        "implementer",
        "reviewer",
        "documenter",
        "git-manager",
        "frontend",
        "researcher",
    )

    missing = [path for path in required if not (PROJECT_ROOT / path).is_file()]
    missing.extend(
        f"agents/tesis/roles/{name}.md"
        for name in role_names
        if not (PROJECT_ROOT / "agents" / "tesis" / "roles" / f"{name}.md").is_file()
    )
    missing.extend(
        f".opencode/agents/{name}.md"
        for name in role_names
        if not (PROJECT_ROOT / ".opencode" / "agents" / f"{name}.md").is_file()
    )

    assert not missing, "Faltan artefactos del contrato universal: " + ", ".join(missing)

    with (PROJECT_ROOT / "tools" / "agent-routes.toml").open("rb") as handle:
        routes = tomllib.load(handle)["routes"]
    expected_routes = set(role_names) | {"coordinator"}
    assert set(routes) == expected_routes
    for route in routes.values():
        for lane in ("primary", "fallback"):
            assert {"host", "provider", "model"} <= set(route[lane])

    config = tomllib.load((PROJECT_ROOT / "tools" / "agent-routes.toml").open("rb"))
    assert {
        "architecture",
        "planning",
        "implementation",
        "frontend",
        "debugging",
        "research",
        "review",
        "documentation",
    } == set(config["task_types"])
    assert {
        "reasoning_max",
        "coding_efficient",
        "frontend_strong",
        "research_efficient",
        "documentation_economy",
    } <= set(config["model_profiles"])
    for command in ("route", "architect", "implement", "frontend", "review", "research"):
        command_file = PROJECT_ROOT / ".opencode" / "commands" / f"{command}.md"
        assert command_file.is_file()
        assert "$ARGUMENTS" in command_file.read_text(encoding="utf-8")

    selected_models = {
        lane["model"]
        for route in routes.values()
        for lane in (route["primary"], route["fallback"])
    }
    assert {
        "reasoning_max",
        "coding_efficient",
        "frontend_strong",
        "research_efficient",
        "documentation_economy",
    } <= selected_models
    assert "openchamber" not in {
        lane["host"]
        for route in routes.values()
        for lane in (route["primary"], route["fallback"])
    }
