from pathlib import Path

import pytest

from agent_harness.config import Settings
from agent_harness.obsidian import ObsidianStore
from agent_harness.paths import ProjectRootError, discover_project_root


def make_project_root(tmp_path: Path) -> Path:
    root = tmp_path / "project"
    (root / ".specify/memory").mkdir(parents=True)
    (root / "AGENTS.md").write_text("contrato", encoding="utf-8")
    (root / ".specify/memory/constitution.md").write_text("constitucion", encoding="utf-8")
    return root


def test_discovers_root_from_nested_working_directory(tmp_path, monkeypatch):
    root = make_project_root(tmp_path)
    nested = root / "tools" / "agent-lab"
    nested.mkdir(parents=True)
    monkeypatch.chdir(nested)

    assert discover_project_root() == root.resolve()


def test_settings_anchors_vault_database_and_profile_to_project_root(tmp_path):
    root = make_project_root(tmp_path)
    settings = Settings(
        project_root=str(root),
        obsidian_vault_dir=".",
        db_path="data/agent.sqlite3",
        agent_profile_dir="agents/tesis",
    )

    assert Path(settings.project_root) == root.resolve()
    assert Path(settings.obsidian_vault_dir) == root.resolve()
    assert Path(settings.db_path) == root / "data/agent.sqlite3"
    assert Path(settings.agent_profile_dir) == root / "agents/tesis"


def test_settings_autodetects_root_when_started_in_nested_directory(tmp_path, monkeypatch):
    root = make_project_root(tmp_path)
    nested = root / "tools" / "agent-lab"
    nested.mkdir(parents=True)
    monkeypatch.chdir(nested)

    settings = Settings(project_root=".", obsidian_vault_dir=".")

    assert Path(settings.project_root) == root.resolve()
    assert Path(settings.obsidian_vault_dir) == root.resolve()


def test_settings_rejects_vault_outside_project_root(tmp_path):
    root = make_project_root(tmp_path)

    with pytest.raises(ProjectRootError, match="debe coincidir"):
        Settings(project_root=str(root), obsidian_vault_dir=str(tmp_path / "other-vault"))


def test_store_writes_to_project_root_when_started_elsewhere(tmp_path, monkeypatch):
    root = make_project_root(tmp_path)
    nested = root / "tools" / "agent-lab"
    nested.mkdir(parents=True)
    monkeypatch.chdir(nested)
    store = ObsidianStore(".", project_root=str(root))

    result = store.write_note("docs/nota-segura.md", {"type": "test"}, "contenido")

    assert result == "docs/nota-segura.md"
    assert (root / result).is_file()
    assert not (nested / "docs/nota-segura.md").exists()


def test_store_rejects_vault_different_from_project_root(tmp_path):
    root = make_project_root(tmp_path)

    with pytest.raises(ProjectRootError, match="debe coincidir"):
        ObsidianStore(str(tmp_path / "other-vault"), project_root=str(root))
