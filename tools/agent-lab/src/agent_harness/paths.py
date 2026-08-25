"""Resolución segura de la raíz del proyecto y sus rutas persistentes."""

from pathlib import Path


class ProjectRootError(ValueError):
    """Indica que no se pudo validar la raíz del proyecto o del vault."""


_PROJECT_MARKERS = (
    Path("AGENTS.md"),
    Path(".specify/memory/constitution.md"),
)


def _is_project_root(path: Path) -> bool:
    return all((path / marker).is_file() for marker in _PROJECT_MARKERS)


def discover_project_root(start: str | Path | None = None) -> Path:
    """Busca la raíz validada desde ``start`` hacia sus directorios padres."""

    origin = Path(start) if start is not None else Path.cwd()
    origin = origin.resolve()
    for candidate in (origin, *origin.parents):
        if _is_project_root(candidate):
            return candidate
    raise ProjectRootError(
        "No se encontró la raíz de Zhud Alelí. Define AGENT_PROJECT_ROOT "
        "o ejecuta el agente dentro de un repositorio que contenga "
        "AGENTS.md y .specify/memory/constitution.md."
    )


def resolve_project_root(configured: str | Path | None = None, *, start: str | Path | None = None) -> Path:
    """Resuelve y valida la raíz configurada o la descubre automáticamente.

    ``""`` y ``"."`` significan autodetección para que el ejemplo de entorno
    siga funcionando aunque el comando se ejecute desde una subcarpeta.
    """

    raw = str(configured).strip() if configured is not None else ""
    if raw in {"", "."}:
        return discover_project_root(start)

    base = Path(start) if start is not None else Path.cwd()
    candidate = Path(raw)
    if not candidate.is_absolute():
        candidate = base / candidate
    candidate = candidate.resolve()
    if not _is_project_root(candidate):
        raise ProjectRootError(
            f"La ruta configurada no es una raíz válida del proyecto: {candidate}. "
            "Debe contener AGENTS.md y .specify/memory/constitution.md."
        )
    return candidate


def resolve_vault_dir(configured: str | Path | None, project_root: Path) -> Path:
    """Resuelve el vault y exige que sea exactamente la raíz del proyecto."""

    raw = str(configured).strip() if configured is not None else ""
    if raw in {"", "."}:
        return project_root

    candidate = Path(raw)
    if not candidate.is_absolute():
        candidate = project_root / candidate
    candidate = candidate.resolve()
    if candidate != project_root:
        raise ProjectRootError(
            f"El vault debe coincidir con la raíz del repositorio: {project_root}. "
            f"Se recibió: {candidate}."
        )
    return candidate


def resolve_project_path(configured: str | Path, project_root: Path, *, label: str) -> Path:
    """Resuelve una ruta persistente y evita que escape del proyecto."""

    candidate = Path(configured)
    if not candidate.is_absolute():
        candidate = project_root / candidate
    candidate = candidate.resolve()
    if candidate != project_root and project_root not in candidate.parents:
        raise ProjectRootError(
            f"La ruta de {label} debe permanecer dentro del proyecto: {project_root}. "
            f"Se recibió: {candidate}."
        )
    return candidate
