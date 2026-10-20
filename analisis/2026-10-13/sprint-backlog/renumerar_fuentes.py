from pathlib import Path
import re

root = Path(r"F:\Tesis\App Tesis\documentacion")
files = [
    (root / "historias/usuario/historias_usuario_v2.3_2026-10-13.md", "2.2", "2.3"),
    (root / "pila_producto/pila_producto_v1.3_2026-10-13.md", "1.2", "1.3"),
]

for path, old_version, new_version in files:
    text = path.read_text(encoding="utf-8-sig")
    text = text.replace(f'version: "{old_version}"', f'version: "{new_version}"', 1)
    text = text.replace("fecha: 2026-10-12", "fecha: 2026-10-13", 1)
    text = re.sub(r"\bS([1-5])\b", lambda m: f"S{int(m.group(1)) + 1}", text)
    text = re.sub(r"\bSprint ([1-5])\b", lambda m: f"Sprint {int(m.group(1)) + 1}", text)
    path.write_text(text, encoding="utf-8", newline="\n")
    print(path)
