from pathlib import Path

from agent_harness.config import Settings


def test_config_registers_declared_gemini_models():
    root = Path(__file__).resolve().parents[3]
    settings = Settings(project_root=str(root), obsidian_vault_dir=str(root))
    router = settings.build_router()
    registered = {item["model_id"] for item in router.get_registered_models()}

    assert {
        "gemini-3.7-flash",
        "gemini-3.6-flash",
        "gemini-3.5-flash",
        "gemini-3.1-pro",
    } <= registered


def test_documenter_model_can_be_selected_by_agent_environment(monkeypatch):
    root = Path(__file__).resolve().parents[3]
    settings = Settings(project_root=str(root), obsidian_vault_dir=str(root))
    router = settings.build_router()
    monkeypatch.setenv("MODEL_AGENT_DOCUMENTER", "gemini-3.1-pro")

    adapter = router.resolve(agent_name="documenter")

    assert adapter.model_id == "gemini-3.1-pro"
