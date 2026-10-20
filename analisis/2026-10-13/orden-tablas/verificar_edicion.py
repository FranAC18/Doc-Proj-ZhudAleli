from __future__ import annotations

import re
from pathlib import Path

from docx import Document


root = Path(r"F:\Tesis\App Tesis\documentacion")
old = (root / "historias/usuario/historias_usuario_v2.3_2026-10-13.md").read_text(encoding="utf-8")
new = (root / "historias/usuario/historias_usuario_v2.4_2026-10-13.md").read_text(encoding="utf-8")
priority = (root / "requisitos/priorizacion/priorizacion_requisitos_v1.2_2026-10-13.md").read_text(encoding="utf-8")
levels = dict(re.findall(r"^\| `(RF-[A-Z]+-\d+)` \| (Esencial|Alta|Complementaria) \|", priority, re.M))
rows = [line.strip().strip("|").split("|") for line in old.splitlines() if line.startswith("| **`HU-")]
assert len(rows) == 51
assert len(set(re.findall(r"^#### (HU-[A-Z]+-\d+) —", new, re.M))) == 51
for row in rows:
    fields = [part.strip() for part in row]
    match = re.search(r"`(HU-[A-Z]+-\d+)` — .*?Origen: `(RF-[A-Z]+-\d+)`", fields[0])
    assert match, fields[0]
    hu, rf = match.groups()
    section = new.split(f"#### {hu} —", 1)[1].split("\n#### ", 1)[0].split("\n## ", 1)[0]
    assert f"**Importancia:** {levels[rf]}" in section, hu
    assert fields[1] in section, hu
    for criterion in fields[2].split("<br>"):
        assert criterion in section, (hu, criterion)
    deps = fields[3].split("Dependencias: ", 1)[1]
    assert deps in section, (hu, deps)

old_tasks = set(re.findall(r"SB-S[1-6]-\d{2}", (root / "sprints/sprint_backlog_v1.0_2026-10-13.md").read_text(encoding="utf-8")))
new_tasks = set(re.findall(r"SB-S[1-6]-\d{2}", (root / "sprints/sprint_backlog_v1.1_2026-10-13.md").read_text(encoding="utf-8")))
assert old_tasks == new_tasks and len(new_tasks) == 27
pile = (root / "pila_producto/pila_producto_v1.4_2026-10-13.md").read_text(encoding="utf-8")
assert sorted(set(map(int, re.findall(r"^\| (\d+) \|", pile, re.M)))) == list(range(1, 61))
doc = Document(root / "sprints/plan_incremental_y_sprint_backlog_v1.3_2026-10-13.docx")
doc_text = "\n".join(cell.text for table in doc.tables for row in table.rows for cell in row.cells)
for hu in re.findall(r"^#### (HU-[A-Z]+-\d+) —", new, re.M):
    assert hu in doc_text, hu
for task in old_tasks:
    assert task in doc_text, task

md_files = [
    root / "README.md",
    root / "control_de_cambios/registro_v2.4_2026-10-13.md",
    root / "historias/usuario/historias_usuario_v2.4_2026-10-13.md",
    root / "pila_producto/pila_producto_v1.4_2026-10-13.md",
    root / "sprints/plan_sprints_v1.2_2026-10-13.md",
    root / "sprints/sprint_backlog_v1.1_2026-10-13.md",
]
for path in md_files:
    text = path.read_text(encoding="utf-8")
    assert "\ufffd" not in text, path
    assert not any(line.rstrip() != line for line in text.splitlines()), path
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if target.startswith(("http:", "https:")):
            continue
        assert (path.parent / target.split("#", 1)[0]).exists(), (path, target)

print("HU completas: 51; prioridad contra RF: 51; criterios y dependencias: 51")
print("Tareas conservadas: 27; posiciones de pila: 60; Word: 51 HU y 27 tareas")
print("Enlaces locales, caracteres y espacios finales: correctos")
