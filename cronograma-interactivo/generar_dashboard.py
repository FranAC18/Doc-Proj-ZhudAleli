"""Genera el dashboard autocontenido desde la plantilla y los datos del proyecto."""

from __future__ import annotations

import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
WEB = HERE / "proyecto-local" / "web"
TEMPLATE = HERE / "dashboard_template.html"
TRACKING_FILE = HERE / "proyecto-local" / "estado" / "seguimiento_sprints_zhud_aleli.json"
OUTPUTS = [
    HERE / "index.html",
    HERE / "cronograma_interactivo_v5.0_2026-10-20.html",
]


def build_html() -> str:
    """Inserta una copia de los datos fuente en la plantilla de un solo archivo."""
    template = TEMPLATE.read_text(encoding="utf-8")
    data = json.loads((WEB / "datos-proyecto.json").read_text(encoding="utf-8"))
    resources = json.loads((WEB / "recursos-sprints.json").read_text(encoding="utf-8"))
    tracking = json.loads(TRACKING_FILE.read_text(encoding="utf-8")) if TRACKING_FILE.exists() else {}
    app_data = json.dumps(
        {"project": data, "resources": resources, "tracking": tracking},
        ensure_ascii=False,
        separators=(",", ":"),
    ).replace("</", "<\\/")
    if "__APP_DATA__" not in template:
        raise ValueError("La plantilla no contiene el marcador __APP_DATA__.")
    return template.replace("__APP_DATA__", app_data)


def main() -> None:
    html = build_html()
    for output in OUTPUTS:
        output.write_text(html, encoding="utf-8")
        print(output)
    print("Dashboard autónomo generado con datos integrados y persistencia local.")


if __name__ == "__main__":
    main()
