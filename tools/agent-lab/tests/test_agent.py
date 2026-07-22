from pathlib import Path

from agent_harness.agent import Agent
from agent_harness.memory import MemoryStore
from agent_harness.models import ModelReply, ToolCall
from agent_harness.obsidian import ObsidianStore
from agent_harness.tools import build_tools


class FakeModel:
    def __init__(self, replies):
        self.replies = iter(replies)
        self.seen = []

    def complete(self, messages, tools):
        self.seen.append((messages, tools))
        return next(self.replies)


def make_agent(tmp_path: Path, model: FakeModel) -> Agent:
    memory = MemoryStore(str(tmp_path / "agent.sqlite3"))
    return Agent(model, memory, build_tools(memory, "test-user"), "test-user")


def test_agent_executes_tool_and_returns_final_answer(tmp_path):
    model = FakeModel([
        ModelReply(tool_calls=[ToolCall("1", "calculate", {"expression": "2 + 3 * 4"})]),
        ModelReply(content="El resultado es 14."),
    ])
    agent = make_agent(tmp_path, model)
    assert agent.run("¿Cuánto es 2 + 3 * 4?") == "El resultado es 14."
    assert len(model.seen) == 2


def test_tool_error_is_recorded_as_candidate_lesson(tmp_path):
    model = FakeModel([
        ModelReply(tool_calls=[ToolCall("1", "calculate", {"expression": "os.system('bad')"})]),
        ModelReply(content="No puedo calcular esa expresión porque no es segura."),
    ])
    agent = make_agent(tmp_path, model)
    assert "segura" in agent.run("hazlo")
    lessons = agent.memory.db.execute("SELECT lesson, status FROM lessons").fetchall()
    assert len(lessons) == 1
    assert lessons[0]["status"] == "pending"


def test_memory_is_persistent(tmp_path):
    path = str(tmp_path / "agent.sqlite3")
    first = MemoryStore(path)
    first.remember("u", "lenguaje", "Python")
    first.close()
    second = MemoryStore(path)
    assert second.search("u", "lenguaje")[0]["value"] == "Python"
    second.close()


def test_obsidian_store_creates_proposal_with_frontmatter(tmp_path):
    store = ObsidianStore(str(tmp_path / "vault"))
    result = store.propose_requirement(
        "RF-P-001", "Registrar asistencia", "Directiva", "Registrar entrada y salida", ["Guardar fecha"]
    )
    path = tmp_path / "vault" / result["path"]
    content = path.read_text(encoding="utf-8")
    assert result["status"] == "proposed"
    assert "status: proposed" in content
    assert "Registrar entrada y salida" in content


def test_obsidian_store_rejects_path_escape(tmp_path):
    store = ObsidianStore(str(tmp_path / "vault"))
    try:
        store.write_note("../fuera.md", {"type": "test"}, "no")
    except ValueError as exc:
        assert "fuera" in str(exc)
    else:
        raise AssertionError("Se permitió escribir fuera del vault")


def test_obsidian_store_records_partial_checkpoint(tmp_path):
    store = ObsidianStore(str(tmp_path / "vault"))
    result = store.save_progress_checkpoint(
        "S0", "Preparar vault", "partially-complete", 60,
        ["Crear estructura"], ["Abrir en Obsidian"], [], "Abrir la carpeta raíz como vault"
    )
    content = (tmp_path / "vault" / result["path"]).read_text(encoding="utf-8")
    assert "status: partially-complete" in content
    assert "progress: 60" in content
    assert "Abrir la carpeta raíz como vault" in content


def test_obsidian_store_does_not_overwrite_existing_note(tmp_path):
    store = ObsidianStore(str(tmp_path / "vault"))
    store.write_note("docs/nota.md", {"type": "test"}, "primera versión")

    try:
        store.write_note("docs/nota.md", {"type": "test"}, "segunda versión")
    except FileExistsError as exc:
        assert "no se sobrescribirá" in str(exc)
    else:
        raise AssertionError("Se sobrescribió una nota sin autorización")


def test_completed_checkpoint_requires_evidence_and_no_pending_work(tmp_path):
    store = ObsidianStore(str(tmp_path / "vault"))

    try:
        store.save_progress_checkpoint(
            "S0",
            "Cerrar preparación",
            "completed",
            90,
            ["Crear estructura"],
            ["Validar Obsidian"],
            [],
            "Solicitar validación",
            [],
        )
    except ValueError as exc:
        assert "progreso 100" in str(exc)
    else:
        raise AssertionError("Se aceptó completed sin cumplir la definición de terminado")


def test_completed_checkpoint_records_evidence(tmp_path):
    store = ObsidianStore(str(tmp_path / "vault"))
    result = store.save_progress_checkpoint(
        "S0",
        "Preparación verificada",
        "completed",
        100,
        ["Crear estructura", "Validar enlaces"],
        [],
        [],
        "Esperar autorización para la base Django",
        ["pytest: 9 passed", "revisión del diff sin hallazgos"],
    )
    content = (tmp_path / "vault" / result["path"]).read_text(encoding="utf-8")
    assert "pytest: 9 passed" in content
    assert "status: completed" in content


def test_agent_loads_repository_contract_and_active_sprint(tmp_path):
    root = tmp_path / "project"
    (root / ".specify/memory").mkdir(parents=True)
    (root / "docs/00-inicio").mkdir(parents=True)
    (root / "docs/sprints").mkdir(parents=True)
    (root / "AGENTS.md").write_text("CONTRATO-RAIZ", encoding="utf-8")
    (root / ".specify/memory/constitution.md").write_text("CONSTITUCION", encoding="utf-8")
    (root / "docs/00-inicio/00-dashboard.md").write_text("DASHBOARD", encoding="utf-8")
    (root / "docs/sprints/SPRINT-00.md").write_text(
        "---\nstatus: in-progress\n---\nSPRINT-ACTIVO", encoding="utf-8"
    )

    model = FakeModel([ModelReply(content="Contexto leído.")])
    memory = MemoryStore(str(tmp_path / "agent.sqlite3"))
    agent = Agent(model, memory, build_tools(memory, "u"), "u", project_root=str(root))

    assert agent.run("resume") == "Contexto leído."
    system_prompt = model.seen[0][0][0]["content"]
    assert "CONTRATO-RAIZ" in system_prompt
    assert "CONSTITUCION" in system_prompt
    assert "DASHBOARD" in system_prompt
    assert "SPRINT-ACTIVO" in system_prompt
