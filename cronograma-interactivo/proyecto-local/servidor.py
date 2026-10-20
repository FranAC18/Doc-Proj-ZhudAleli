"""Servidor local del cronograma. Solo escucha en 127.0.0.1."""

from __future__ import annotations

import argparse
import json
import msvcrt
import mimetypes
import os
import re
import secrets
import subprocess
import tempfile
import threading
import webbrowser
from datetime import date, datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit


HERE = Path(__file__).resolve().parent
WEB = HERE / "web"
DOCUMENTACION = HERE.parents[1] / "documentacion"
EVIDENCIAS = HERE.parents[1] / "docs" / "evidence"
STATE_FILE = HERE / "estado" / "seguimiento_sprints_zhud_aleli.json"
FORMAT = "zhud-aleli-gantt-v1"
MAX_BODY = 2_000_000
STATUSES = {"sin_verificar", "en_curso", "bloqueada", "realizada", "verificada"}
PRIORITIES = {"Esencial", "Alta", "Media", "Baja", "Complementaria"}
LOCAL_RESOURCE_PREFIXES = ("/fuentes/", "/evidencias/")
DOCUMENT_SUFFIXES = {".md", ".txt", ".json", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".png", ".jpg", ".jpeg"}


def resolve_local_document(url: object) -> Path:
    """Resuelve únicamente documentos locales permitidos para mostrarlos en Explorer."""
    if not isinstance(url, str) or not url.startswith(LOCAL_RESOURCE_PREFIXES):
        raise ValueError("Selecciona una ruta local /fuentes/ o /evidencias/.")
    parsed = urlsplit(url)
    if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
        raise ValueError("La ruta debe apuntar directamente a un documento local.")
    decoded = unquote(parsed.path)
    if (
        not re.fullmatch(r"/(fuentes|evidencias)/[A-Za-z0-9_./-]+", decoded)
        or any(part in {".", ".."} for part in decoded.split("/"))
        or Path(decoded).suffix.lower() not in DOCUMENT_SUFFIXES
    ):
        raise ValueError("La ruta debe apuntar a un documento permitido.")
    root = DOCUMENTACION if decoded.startswith("/fuentes/") else EVIDENCIAS
    source = (root / decoded.split("/", 2)[2]).resolve()
    if not source.is_relative_to(root.resolve()) or not source.is_file():
        raise ValueError("No se encontró el documento en su carpeta local.")
    return source


def open_local_document(url: object) -> Path:
    """Abre Explorer con el documento local seleccionado, sin shell ni rutas arbitrarias."""
    if os.name != "nt":
        raise ValueError("Abrir la carpeta está disponible en Windows.")
    source = resolve_local_document(url)
    subprocess.Popen(
        ["explorer.exe", f"/select,{source}"],
        stdin=subprocess.DEVNULL,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        close_fds=True,
    )
    return source


def project_data() -> dict:
    return json.loads((WEB / "datos-proyecto.json").read_text(encoding="utf-8"))


def timestamp() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def clean_record(raw: object, *, imported: bool = False) -> dict:
    if not isinstance(raw, dict) or raw.get("status") not in STATUSES:
        raise ValueError("Estado de tarea no válido.")
    record = {"status": raw["status"]}
    for field, limit in (("evidence", 1000), ("reviewer", 160), ("date", 10), ("notes", 4000)):
        value = raw.get(field, "")
        if not isinstance(value, str) or len(value) > limit:
            raise ValueError(f"Campo {field} no válido.")
        record[field] = value.strip()
    points = raw.get("points")
    if points in (None, ""):
        record["points"] = None
    elif isinstance(points, bool) or not isinstance(points, int) or not 0 <= points <= 100:
        raise ValueError("Los puntos deben ser un número entero entre 0 y 100.")
    else:
        record["points"] = points
    if record["status"] in {"realizada", "verificada"} and not record["evidence"]:
        raise ValueError("La tarea realizada necesita evidencia.")
    if record["status"] == "verificada" and not (record["reviewer"] and record["date"]):
        raise ValueError("La tarea verificada necesita responsable y fecha.")
    if record["date"]:
        try:
            checked = date.fromisoformat(record["date"])
        except ValueError as error:
            raise ValueError("Fecha no válida.") from error
        if checked > date.today():
            raise ValueError("La fecha de comprobación no puede ser futura.")
    if imported:
        value = raw.get("updatedAt", "")
        if not isinstance(value, str) or len(value) > 40:
            raise ValueError("Fecha de actualización no válida.")
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError
        except ValueError as error:
            raise ValueError("Fecha de actualización no válida.") from error
        record["updatedAt"] = parsed.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    else:
        record["updatedAt"] = timestamp()
    return record


class Store:
    def __init__(
        self,
        path: Path,
        task_ids: set[str],
        edition: str,
        sprint_ids: set[str],
        default_closed_sprints: set[str] | None = None,
    ):
        self.path = path
        self.task_ids = task_ids
        self.edition = edition
        self.sprint_ids = sprint_ids
        self.default_closed_sprints = default_closed_sprints or set()
        self.lock = threading.RLock()

    def read(self) -> dict:
        with self.lock:
            if not self.path.exists():
                return {
                    "format": FORMAT,
                    "edition": self.edition,
                    "exportedAt": timestamp(),
                    "updates": {},
                    "resources": [],
                    "customTasks": [],
                    "taskEdits": {},
                    "sprintStates": {},
                    "audit": [],
                }
            data = json.loads(self.path.read_text(encoding="utf-8"))
            if data.get("format") != FORMAT or not isinstance(data.get("updates"), dict):
                raise ValueError("El archivo de avance tiene un formato desconocido.")
            if not isinstance(data.get("resources", []), list):
                raise ValueError("La lista de accesos a documentos no es válida.")
            if not isinstance(data.get("customTasks", []), list):
                raise ValueError("La lista de tareas locales no es válida.")
            if not isinstance(data.get("taskEdits", {}), dict):
                raise ValueError("Las ediciones locales de tareas no son válidas.")
            if not isinstance(data.get("sprintStates", {}), dict):
                raise ValueError("Los estados locales de sprint no son válidos.")
            if not isinstance(data.get("audit", []), list):
                raise ValueError("La bitácora local no es válida.")
            data.setdefault("resources", [])
            data.setdefault("customTasks", [])
            data.setdefault("taskEdits", {})
            data.setdefault("sprintStates", {})
            data.setdefault("audit", [])
            return data

    @staticmethod
    def _audit(data: dict, title: str, detail: str, *, kind: str = "edit", task_id: str = "") -> None:
        data["audit"].insert(0, {
            "id": secrets.token_hex(8),
            "at": timestamp(),
            "kind": kind,
            "taskId": task_id,
            "title": title[:180],
            "detail": detail[:1000],
        })
        data["audit"] = data["audit"][:500]

    def _clean_task(self, raw: object, *, creating: bool) -> dict:
        if not isinstance(raw, dict):
            raise ValueError("La tarea enviada no es válida.")
        task_id = raw.get("id")
        if not isinstance(task_id, str) or not re.fullmatch(r"(?:LOC-[A-F0-9]{8}|SB-[A-Z0-9-]{2,40})", task_id):
            raise ValueError("El identificador de tarea no es válido.")
        is_local = task_id.startswith("LOC-")
        if is_local and task_id in self.task_ids:
            raise ValueError("El identificador de tarea ya existe.")
        if not is_local and task_id not in self.task_ids:
            raise ValueError("La tarea no pertenece al backlog del proyecto.")
        if creating and not is_local:
            raise ValueError("Las tareas nuevas deben usar un identificador local.")
        title = raw.get("title")
        description = raw.get("description", "")
        priority = raw.get("priority", "Media")
        sprint = raw.get("sprint", "")
        start = raw.get("start", "")
        end = raw.get("end", "")
        if not isinstance(title, str) or not 1 <= len(title.strip()) <= 120:
            raise ValueError("El título debe tener entre 1 y 120 caracteres.")
        if not isinstance(description, str) or len(description) > 500:
            raise ValueError("La descripción no puede superar 500 caracteres.")
        if priority not in PRIORITIES:
            raise ValueError("Selecciona una prioridad válida.")
        if not isinstance(sprint, str) or (sprint and sprint not in self.sprint_ids):
            raise ValueError("Selecciona un sprint válido.")
        for label, value in (("inicio", start), ("fin", end)):
            if not isinstance(value, str) or (value and len(value) != 10):
                raise ValueError(f"La fecha de {label} no es válida.")
            if value:
                try:
                    date.fromisoformat(value)
                except ValueError as error:
                    raise ValueError(f"La fecha de {label} no es válida.") from error
        if start and end and end < start:
            raise ValueError("La fecha de fin debe ser igual o posterior a la fecha de inicio.")
        return {
            "id": task_id,
            "title": title.strip(),
            "description": description.strip(),
            "priority": priority,
            "sprint": sprint,
            "start": start,
            "end": end,
            "kind": "task",
            "custom": is_local,
            "hu": [],
            "ht": [],
            "updatedAt": timestamp(),
        }

    def modify_task(self, action: object, raw: object) -> dict:
        if not isinstance(raw, dict):
            raise ValueError("Solicitud de tarea no válida.")
        task_id = raw.get("id") if action == "delete" else (raw.get("task") or {}).get("id") if isinstance(raw.get("task"), dict) else None
        with self.lock:
            data = self.read()
            if action == "delete":
                local = next((item for item in data["customTasks"] if item.get("id") == task_id), None)
                if local is None:
                    raise ValueError("Solo se pueden eliminar tareas agregadas localmente; conserva la trazabilidad del backlog fuente.")
                data["customTasks"] = [item for item in data["customTasks"] if item.get("id") != task_id]
                data["updates"].pop(task_id, None)
                self._audit(data, f"Tarea {task_id} eliminada", local.get("title", ""), kind="delete", task_id=task_id)
            elif action in {"create", "update"}:
                task = self._clean_task(raw.get("task"), creating=action == "create")
                current_custom = next((item for item in data["customTasks"] if item.get("id") == task["id"]), None)
                is_custom = task["custom"]
                if action == "create" and (current_custom or task["id"] in data["taskEdits"]):
                    raise ValueError("Ya existe una tarea con ese identificador.")
                if action == "update" and is_custom and current_custom is None:
                    raise ValueError("No se encontró la tarea local que intentas editar.")
                record_raw = raw["task"]
                record = clean_record({
                    "status": record_raw.get("status", "sin_verificar"),
                    "evidence": record_raw.get("evidence", ""),
                    "reviewer": record_raw.get("reviewer", ""),
                    "date": record_raw.get("date", ""),
                    "notes": record_raw.get("notes", ""),
                    "points": record_raw.get("points"),
                })
                previous_task = (current_custom or {}) if is_custom else data["taskEdits"].get(task["id"], {})
                previous_record = data["updates"].get(task["id"], {})
                labels = {
                    "title": "título",
                    "description": "descripción",
                    "priority": "prioridad",
                    "sprint": "sprint",
                    "start": "fecha de inicio",
                    "end": "fecha de fin",
                }
                changed = [label for field, label in labels.items() if previous_task.get(field) != task[field]]
                record_labels = {
                    "status": "estado",
                    "evidence": "evidencia",
                    "reviewer": "persona verificadora",
                    "date": "fecha de comprobación",
                    "notes": "observaciones",
                    "points": "estimación",
                }
                changed.extend(label for field, label in record_labels.items() if previous_record.get(field) != record[field])
                data["updates"][task["id"]] = record
                if is_custom:
                    if action == "create":
                        data["customTasks"].append(task)
                    else:
                        data["customTasks"] = [task if item.get("id") == task["id"] else item for item in data["customTasks"]]
                else:
                    data["taskEdits"][task["id"]] = {key: value for key, value in task.items() if key not in {"id", "kind", "custom", "hu", "ht"}}
                verb = "creada" if action == "create" else "actualizada"
                details = f'{task["title"]} · {task["sprint"] or "Sin sprint"} · {record["points"] if record["points"] is not None else "Sin estimar"} pts'
                if changed:
                    details += " · cambios: " + ", ".join(changed)
                elif action == "update":
                    details += " · sin cambios en los campos"
                self._audit(data, f"Tarea {task['id']} {verb}", details, kind="create" if action == "create" else "edit", task_id=task["id"])
            else:
                raise ValueError("Elige crear, actualizar o eliminar una tarea.")
            data["exportedAt"] = timestamp()
            return self._write(data)

    def set_sprint_state(self, sprint: object, closed: object) -> dict:
        if not isinstance(sprint, str) or sprint not in self.sprint_ids or not isinstance(closed, bool):
            raise ValueError("Sprint o estado no válido.")
        with self.lock:
            data = self.read()
            previous = data["sprintStates"].get(sprint, {}).get(
                "closed", sprint in self.default_closed_sprints
            )
            data["sprintStates"][sprint] = {"closed": closed, "closedAt": timestamp() if closed else None, "updatedAt": timestamp()}
            if previous != closed:
                self._audit(data, f"Sprint {sprint} {'cerrado' if closed else 'reabierto'}", "Cambio de estado registrado en la bitácora.", kind="sprint")
            data["exportedAt"] = timestamp()
            return self._write(data)

    def _clean_resource(self, sprint: object, label: object, url: object, resource_id: object = None) -> dict:
        if not isinstance(sprint, str) or sprint not in self.sprint_ids:
            raise ValueError("Selecciona un sprint válido.")
        if not isinstance(label, str) or not 1 <= len(label.strip()) <= 120:
            raise ValueError("El nombre debe tener entre 1 y 120 caracteres.")
        if not isinstance(url, str):
            raise ValueError("La dirección del acceso no es válida.")
        label, url = label.strip(), url.strip()
        if not url or len(url) > 1200 or "\\" in url or any(ord(char) < 32 for char in url):
            raise ValueError("La dirección del acceso no es válida.")
        parsed = urlsplit(url)
        if url.startswith(LOCAL_RESOURCE_PREFIXES):
            if parsed.scheme or parsed.netloc or parsed.query or parsed.fragment:
                raise ValueError("La ruta local debe apuntar directamente a un documento.")
            decoded = unquote(parsed.path)
            if ".." in decoded.split("/") or Path(decoded).suffix.lower() not in DOCUMENT_SUFFIXES:
                raise ValueError("La ruta local debe apuntar a un documento disponible dentro de su carpeta.")
            if not re.fullmatch(r"/(fuentes|evidencias)/[A-Za-z0-9_./-]+", decoded):
                raise ValueError("La ruta local solo admite letras, números, guiones y guiones bajos.")
            root = DOCUMENTACION if decoded.startswith("/fuentes/") else EVIDENCIAS
            source = (root / decoded.split("/", 2)[2]).resolve()
            if not source.is_relative_to(root.resolve()) or not source.is_file():
                raise ValueError("No se encontró el documento en esa ruta local.")
        elif parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
            raise ValueError("Usa una URL http/https o una ruta local /fuentes/ o /evidencias/.")
        if resource_id is None:
            resource_id = secrets.token_hex(8)
        elif not isinstance(resource_id, str) or not re.fullmatch(r"[a-f0-9]{16}", resource_id):
            raise ValueError("El identificador del acceso no es válido.")
        return {"id": resource_id, "sprint": sprint, "label": label, "url": url, "updatedAt": timestamp()}

    def add_resource(self, sprint: str, label: str, url: str) -> dict:
        resource = self._clean_resource(sprint, label, url)
        with self.lock:
            data = self.read()
            if any(item.get("sprint") == resource["sprint"] and item.get("url") == resource["url"] for item in data["resources"]):
                raise ValueError("Ese acceso ya está registrado en este sprint.")
            if len(data["resources"]) >= 200:
                raise ValueError("Se alcanzó el límite de accesos guardados.")
            data["resources"].append(resource)
            self._audit(data, "Acceso agregado al sprint " + sprint, label, kind="evidence")
            data["exportedAt"] = timestamp()
            return self._write(data)

    def remove_resource(self, resource_id: str) -> dict:
        if not isinstance(resource_id, str) or not re.fullmatch(r"[a-f0-9]{16}", resource_id):
            raise ValueError("El acceso que se quiere quitar no es válido.")
        with self.lock:
            data = self.read()
            remaining = [item for item in data["resources"] if item.get("id") != resource_id]
            if len(remaining) == len(data["resources"]):
                raise ValueError("No se encontró el acceso guardado.")
            data["resources"] = remaining
            self._audit(data, "Acceso documental quitado", resource_id, kind="evidence")
            data["exportedAt"] = timestamp()
            return self._write(data)

    def _write(self, data: dict) -> dict:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        descriptor, temporary = tempfile.mkstemp(prefix="seguimiento-", suffix=".tmp", dir=self.path.parent)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                json.dump(data, stream, ensure_ascii=False, indent=2)
                stream.write("\n")
                stream.flush()
                os.fsync(stream.fileno())
            os.replace(temporary, self.path)
        finally:
            if os.path.exists(temporary):
                os.unlink(temporary)
        return data

    def save_task(self, task_id: str, raw: object) -> dict:
        with self.lock:
            data = self.read()
            custom_ids = {item.get("id") for item in data.get("customTasks", [])}
            if task_id not in self.task_ids and task_id not in custom_ids:
                raise ValueError("La tarea no pertenece al cronograma.")
            record = clean_record(raw)
            previous = data["updates"].get(task_id, {})
            data["updates"][task_id] = record
            if previous != record:
                title = f"Seguimiento de {task_id} actualizado"
                field_labels = {
                    "status": "estado",
                    "evidence": "evidencia",
                    "reviewer": "persona verificadora",
                    "date": "fecha de comprobación",
                    "notes": "observaciones",
                    "points": "estimación",
                }
                changes = [label for field, label in field_labels.items() if previous.get(field) != record.get(field)]
                detail = "Cambios: " + ", ".join(changes) if changes else "Seguimiento guardado."
                self._audit(data, title, detail, kind="status", task_id=task_id)
            data["exportedAt"] = timestamp()
            return self._write(data)

    def import_updates(self, raw: object) -> tuple[dict, int]:
        if not isinstance(raw, dict) or raw.get("format") != FORMAT or not isinstance(raw.get("updates"), dict):
            raise ValueError("El archivo importado no es un seguimiento del cronograma.")
        raw_resources = raw.get("resources", [])
        if not isinstance(raw_resources, list) or len(raw_resources) > 200:
            raise ValueError("La lista de accesos importada no es válida.")
        incoming_resources = []
        for resource in raw_resources:
            if not isinstance(resource, dict):
                raise ValueError("Hay un acceso documental no válido en el archivo.")
            incoming_resources.append(self._clean_resource(resource.get("sprint"), resource.get("label"), resource.get("url"), resource.get("id")))
        raw_custom = raw.get("customTasks", [])
        if not isinstance(raw_custom, list) or len(raw_custom) > 300:
            raise ValueError("La lista de tareas locales importada no es válida.")
        incoming_custom = [self._clean_task(item, creating=True) for item in raw_custom]
        custom_ids = [item["id"] for item in incoming_custom]
        if len(set(custom_ids)) != len(custom_ids):
            raise ValueError("El archivo contiene identificadores duplicados de tareas locales.")
        raw_edits = raw.get("taskEdits", {})
        if not isinstance(raw_edits, dict) or len(raw_edits) > len(self.task_ids):
            raise ValueError("Las ediciones de tareas importadas no son válidas.")
        incoming_edits = {}
        for task_id, edit in raw_edits.items():
            if task_id not in self.task_ids or not isinstance(edit, dict):
                raise ValueError("El respaldo contiene una edición de tarea desconocida.")
            cleaned = self._clean_task({"id": task_id, **edit}, creating=False)
            incoming_edits[task_id] = {
                key: value for key, value in cleaned.items()
                if key not in {"id", "kind", "custom", "hu", "ht"}
            }
        raw_sprints = raw.get("sprintStates", {})
        if not isinstance(raw_sprints, dict):
            raise ValueError("Los estados de sprint importados no son válidos.")
        incoming_sprints = {}
        for sprint_id, sprint_state in raw_sprints.items():
            if sprint_id not in self.sprint_ids or not isinstance(sprint_state, dict) or not isinstance(sprint_state.get("closed"), bool):
                raise ValueError("El respaldo contiene un estado de sprint no válido.")
            incoming_sprints[sprint_id] = sprint_state
        incoming_audit = raw.get("audit", [])
        if not isinstance(incoming_audit, list) or len(incoming_audit) > 500:
            raise ValueError("La bitácora importada no es válida.")
        with self.lock:
            data = self.read()
            allowed_task_ids = self.task_ids | {item.get("id") for item in data["customTasks"]} | set(custom_ids)
            if len(raw["updates"]) > len(self.task_ids) + 300:
                raise ValueError("El archivo contiene demasiadas tareas.")
            incoming = {}
            for task_id, record in raw["updates"].items():
                if task_id not in allowed_task_ids:
                    raise ValueError(f"Tarea desconocida: {task_id}.")
                incoming[task_id] = clean_record(record, imported=True)
            count = 0
            for task_id, record in incoming.items():
                current = data["updates"].get(task_id)
                if current is None or record["updatedAt"] > current.get("updatedAt", ""):
                    data["updates"][task_id] = record
                    count += 1
            for resource in incoming_resources:
                duplicate = any(item.get("id") == resource["id"] or (item.get("sprint") == resource["sprint"] and item.get("url") == resource["url"]) for item in data["resources"])
                if not duplicate:
                    data["resources"].append(resource)
                    count += 1
            for item in incoming_custom:
                current_index = next((index for index, task in enumerate(data["customTasks"]) if task.get("id") == item["id"]), None)
                if current_index is None:
                    data["customTasks"].append(item)
                    count += 1
                elif data["customTasks"][current_index] != item:
                    data["customTasks"][current_index] = item
                    count += 1
            for task_id, edit in incoming_edits.items():
                if data["taskEdits"].get(task_id) != edit:
                    data["taskEdits"][task_id] = edit
                    count += 1
            for sprint_id, sprint_state in incoming_sprints.items():
                if data["sprintStates"].get(sprint_id) != sprint_state:
                    data["sprintStates"][sprint_id] = sprint_state
                    count += 1
            known = {entry.get("id") for entry in data["audit"] if isinstance(entry, dict)}
            new_audit = []
            for entry in incoming_audit:
                if not isinstance(entry, dict) or not isinstance(entry.get("id"), str) or not re.fullmatch(r"[a-f0-9]{16}", entry["id"]) or entry["id"] in known:
                    continue
                if not isinstance(entry.get("at"), str) or not isinstance(entry.get("title"), str) or not isinstance(entry.get("detail", ""), str):
                    continue
                new_audit.append({
                    "id": entry["id"],
                    "at": entry["at"][:40],
                    "kind": entry.get("kind", "edit") if entry.get("kind") in {"edit", "create", "delete", "sprint", "evidence", "status", "import"} else "edit",
                    "taskId": entry.get("taskId", "")[:80] if isinstance(entry.get("taskId", ""), str) else "",
                    "title": entry["title"][:180],
                    "detail": entry.get("detail", "")[:1000],
                })
                known.add(entry["id"])
            if new_audit:
                data["audit"] = (new_audit + data["audit"])[:500]
                count += len(new_audit)
            if count:
                self._audit(data, "Respaldo importado", f"{count} registros incorporados o actualizados.", kind="import")
                data["exportedAt"] = timestamp()
                self._write(data)
            return data, count


class LocalServer(ThreadingHTTPServer):
    daemon_threads = True

    def __init__(self, store: Store):
        super().__init__(("127.0.0.1", 0), Handler)
        self.store = store
        self.base_url = f"http://127.0.0.1:{self.server_port}"


class Handler(BaseHTTPRequestHandler):
    server: LocalServer

    def log_message(self, format: str, *args: object) -> None:
        print(f"{self.address_string()} - {format % args}")

    def _send(self, status: int, body: bytes, content_type: str) -> None:
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Content-Security-Policy", "default-src 'self'; style-src 'self' 'unsafe-inline' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; script-src 'self'; object-src 'none'; base-uri 'none'")
        self.end_headers()
        self.wfile.write(body)

    def _json(self, status: int, value: object) -> None:
        self._send(status, json.dumps(value, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def _allowed_host(self) -> bool:
        return self.headers.get("Host") == f"127.0.0.1:{self.server.server_port}"

    def do_GET(self) -> None:
        if not self._allowed_host():
            self._json(403, {"error": "Acceso local no permitido."})
            return
        path = urlsplit(self.path).path
        try:
            if path == "/api/seguimiento":
                self._json(200, self.server.store.read())
                return
            fixed = {
                "/": (WEB / "index.html", "text/html; charset=utf-8"),
                "/index.html": (WEB / "index.html", "text/html; charset=utf-8"),
                "/assets/app.js": (WEB / "assets" / "app.js", "text/javascript; charset=utf-8"),
                "/assets/styles.css": (WEB / "assets" / "styles.css", "text/css; charset=utf-8"),
                "/assets/interaction.css": (WEB / "assets" / "interaction.css", "text/css; charset=utf-8"),
                "/datos-proyecto.json": (WEB / "datos-proyecto.json", "application/json; charset=utf-8"),
                "/recursos-sprints.json": (WEB / "recursos-sprints.json", "application/json; charset=utf-8"),
            }
            if path in fixed:
                source, mime = fixed[path]
            elif path.startswith("/fuentes/"):
                relative = unquote(path[len("/fuentes/"):])
                if not relative or not re.fullmatch(r"[A-Za-z0-9_./-]+", relative):
                    raise FileNotFoundError
                source = (DOCUMENTACION / relative).resolve()
                if not source.is_relative_to(DOCUMENTACION.resolve()) or source.suffix.lower() not in DOCUMENT_SUFFIXES:
                    raise FileNotFoundError
                mime = "text/plain; charset=utf-8" if source.suffix.lower() in {".md", ".txt"} else mimetypes.guess_type(source.name)[0] or "application/octet-stream"
            elif path.startswith("/evidencias/"):
                relative = unquote(path[len("/evidencias/"):])
                if not relative or not re.fullmatch(r"[A-Za-z0-9_./-]+", relative):
                    raise FileNotFoundError
                source = (EVIDENCIAS / relative).resolve()
                if not source.is_relative_to(EVIDENCIAS.resolve()) or source.suffix.lower() not in DOCUMENT_SUFFIXES:
                    raise FileNotFoundError
                mime = "text/plain; charset=utf-8" if source.suffix.lower() in {".md", ".txt"} else mimetypes.guess_type(source.name)[0] or "application/octet-stream"
            else:
                raise FileNotFoundError
            self._send(200, source.read_bytes(), mime)
        except FileNotFoundError:
            self._json(404, {"error": "Página o documento no encontrado."})
        except (OSError, ValueError) as error:
            self._json(500, {"error": str(error)})

    def do_POST(self) -> None:
        if not self._allowed_host() or self.headers.get("Origin") != self.server.base_url:
            self._json(403, {"error": "Solicitud externa no permitida."})
            return
        if self.headers.get("Content-Type", "").split(";")[0].strip().lower() != "application/json":
            self._json(415, {"error": "Se necesita contenido JSON."})
            return
        try:
            size = int(self.headers.get("Content-Length", "0"))
            if size < 2 or size > MAX_BODY:
                raise ValueError("El archivo enviado tiene un tamaño no permitido.")
            data = json.loads(self.rfile.read(size))
            path = urlsplit(self.path).path
            if path == "/api/seguimiento":
                if not isinstance(data, dict):
                    raise ValueError("Solicitud no válida.")
                saved = self.server.store.save_task(data.get("id", ""), data.get("record"))
                self._json(200, saved)
            elif path == "/api/recursos":
                if not isinstance(data, dict):
                    raise ValueError("Solicitud no válida.")
                if data.get("action") == "add":
                    saved = self.server.store.add_resource(data.get("sprint", ""), data.get("label", ""), data.get("url", ""))
                elif data.get("action") == "remove":
                    saved = self.server.store.remove_resource(data.get("id", ""))
                else:
                    raise ValueError("Elige agregar o quitar un acceso.")
                self._json(200, saved)
            elif path == "/api/tareas":
                if not isinstance(data, dict):
                    raise ValueError("Solicitud de tarea no válida.")
                saved = self.server.store.modify_task(data.get("action"), data)
                self._json(200, saved)
            elif path == "/api/sprints":
                if not isinstance(data, dict):
                    raise ValueError("Solicitud de sprint no válida.")
                saved = self.server.store.set_sprint_state(data.get("sprint"), data.get("closed"))
                self._json(200, saved)
            elif path == "/api/abrir-documento":
                if not isinstance(data, dict):
                    raise ValueError("Solicitud no válida.")
                open_local_document(data.get("url"))
                self._json(200, {"ok": True})
            elif path == "/api/importar":
                saved, count = self.server.store.import_updates(data)
                self._json(200, {"count": count, "tracking": saved})
            else:
                self._json(404, {"error": "Operación no encontrada."})
        except (ValueError, UnicodeError, json.JSONDecodeError) as error:
            self._json(400, {"error": str(error)})
        except OSError as error:
            self._json(500, {"error": f"No se pudo guardar el archivo: {error}"})


def make_server(state_file: Path = STATE_FILE) -> LocalServer:
    data = project_data()
    task_ids = {item["id"] for item in data["items"] if item["kind"] == "task"}
    resource_data = json.loads((WEB / "recursos-sprints.json").read_text(encoding="utf-8"))
    sprint_ids = {item["id"] for item in data["sprints"]} | {item["id"] for item in resource_data["sprints"]}
    closed_sprints = {item["id"] for item in resource_data["sprints"] if item.get("status") == "Cerrado"}
    return LocalServer(Store(state_file, task_ids, data["edition"], sprint_ids, closed_sprints))


def instance_lock(state_file: Path):
    """Impide dos servidores escribiendo el mismo seguimiento en Windows."""
    state_file.parent.mkdir(parents=True, exist_ok=True)
    lock_path = state_file.with_suffix(".lock")
    stream = lock_path.open("a+b")
    if lock_path.stat().st_size == 0:
        stream.write(b"0")
        stream.flush()
    stream.seek(0)
    try:
        msvcrt.locking(stream.fileno(), msvcrt.LK_NBLCK, 1)
    except OSError:
        stream.close()
        return None
    return stream


def main() -> None:
    parser = argparse.ArgumentParser(description="Abre el cronograma local en un puerto libre.")
    parser.add_argument("--no-browser", action="store_true", help="Inicia solo el servidor (uso de pruebas).")
    parser.add_argument("--state-file", type=Path, default=STATE_FILE, help=argparse.SUPPRESS)
    args = parser.parse_args()
    lock = instance_lock(args.state_file)
    url_file = args.state_file.with_suffix(".url")
    if lock is None:
        if url_file.exists():
            url = url_file.read_text(encoding="utf-8").strip()
            print(f"El cronograma ya está abierto en {url}", flush=True)
            if not args.no_browser:
                webbrowser.open(url)
        else:
            print("El cronograma ya está abierto. Vuelve a la ventana del navegador.", flush=True)
        return
    server = make_server(args.state_file)
    url_file.write_text(server.base_url + "\n", encoding="utf-8")
    print(f"Cronograma disponible en {server.base_url}", flush=True)
    print("Cierra esta ventana o pulsa Ctrl+C para detenerlo.", flush=True)
    if not args.no_browser:
        timer = threading.Timer(0.7, lambda: webbrowser.open(server.base_url))
        timer.daemon = True
        timer.start()
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
        lock.close()


if __name__ == "__main__":
    main()
