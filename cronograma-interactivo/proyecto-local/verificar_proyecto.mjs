import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import vm from "node:vm";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));
const python = process.env.PYTHON || "python";
const temporary = await mkdtemp(join(tmpdir(), "zhud-dashboard-test-"));
const statePath = join(temporary, "seguimiento.json");
const dashboardStatePath = join(temporary, "dashboard_v5.json");
let server;

function startServer() {
  return new Promise((resolveStart, rejectStart) => {
    const child = spawn(python, [join(root, "servidor.py"), "--no-browser", "--port", "0", "--state-file", statePath, "--dashboard-state-file", dashboardStatePath], { cwd: root, windowsHide: true });
    server = child;
    let output = "";
    let failure = "";
    const timeout = setTimeout(() => rejectStart(Error("El servidor local no arrancó.")), 10000);
    child.stdout.on("data", chunk => {
      output += chunk.toString();
      const match = output.match(/http:\/\/127\.0\.0\.1:\d+/);
      if (match) { clearTimeout(timeout); resolveStart(match[0]); }
    });
    child.stderr.on("data", chunk => { failure += chunk.toString(); });
    child.on("error", error => { clearTimeout(timeout); rejectStart(error); });
    child.on("exit", code => {
      if (!output.includes("http://127.0.0.1:")) {
        clearTimeout(timeout);
        rejectStart(Error(`El servidor terminó con código ${code}. ${failure}`));
      }
    });
  });
}

try {
  const html = await readFile(join(root, "web", "index.html"), "utf8");
  const sourceHtml = await readFile(join(root, "..", "index.html"), "utf8");
  assert.ok(html.includes('id="view-backlog"') && html.includes('id="view-requirements"') && html.includes('id="view-kanban"') && html.includes('id="view-gantt"') && html.includes('id="view-audit"'), "La copia local contiene las cinco vistas del dashboard v5.");
  assert.ok(html.includes('data-open-evidence=') && html.includes("local-evidence-bridge"), "La copia incluye el puente para abrir evidencias locales.");
  assert.ok(html.includes("window.APP_SERVER_STATE") && html.includes("saveServerSnapshot") && html.includes("/api/dashboard-state"), "El dashboard lee y sincroniza el estado con el servidor local.");
  const getData = input => {
    const match = input.match(/window\.APP_DATA\s*=\s*(\{[\s\S]*?\})\s*;\s*<\/script>/);
    assert.ok(match, "El HTML integra los datos del proyecto.");
    return JSON.parse(match[1]);
  };
  assert.deepEqual(getData(html), getData(sourceHtml), "La copia local conserva exactamente los datos integrados en el dashboard fuente.");
  for (const [index, match] of [...html.matchAll(/<script(?=[\s>])([^>]*)>([\s\S]*?)<\/script>/gi)].entries()) {
    if (/\bsrc\s*=/.test(match[1])) continue;
    new vm.Script(match[2], { filename: `inline-${index}.js` });
  }

  const url = await startServer();
  const response = await fetch(url);
  assert.equal(response.status, 200, "El servidor entrega el dashboard local.");
  const csp = response.headers.get("content-security-policy") || "";
  assert.match(csp, /script-src[^;]*'nonce-[^']+'/i, "El servidor permite los scripts en línea con nonce CSP.");
  assert.doesNotMatch(csp, /script-src[^;]*unsafe-inline/i, "La política de scripts no habilita unsafe-inline.");
  const servedHtml = await response.text();
  const nonceMatch = csp.match(/'nonce-([^']+)'/);
  assert.ok(nonceMatch, "El CSP contiene un nonce de esta respuesta.");
  const scriptTags = [...servedHtml.matchAll(/<script(?=[\s>])([^>]*)>/gi)];
  assert.ok(scriptTags.length > 0 && scriptTags.every(match => match[1].includes(`nonce="${nonceMatch[1]}"`)), "El nonce se aplica a todos los scripts del dashboard servido.");
  assert.ok(servedHtml.includes("local-evidence-bridge"));

  const snapshot = {
    schema: "tesis_scrum_multireq_v1",
    selectedSprint: "S1",
    taskOverrides: {},
    customTasks: [],
    customSprints: [],
    sprintStates: { S1: { closed: true } },
    storyOverrides: { "HU-TEST": { title: "<script>alert(1)</script>" } },
    customStories: [],
    requirementOverrides: {},
    customRequirements: [],
    criteriaDone: {},
    storyOrder: ["HU-01", "HU-02"],
    audit: [],
  };
  const saved = await fetch(url + "/api/dashboard-state", {
    method: "POST",
    headers: { "Content-Type": "application/json", Origin: url },
    body: JSON.stringify({ state: snapshot }),
  });
  assert.equal(saved.status, 200, `El servidor guarda el snapshot del dashboard. Respuesta: ${await saved.text()}`);
  const stored = await (await fetch(url + "/api/dashboard-state")).json();
  assert.deepEqual(stored.state, snapshot, "El snapshot queda persistido en el JSON local.");
  const unsafeState = await fetch(url + "/api/dashboard-state", {
    method: "POST",
    headers: { "Content-Type": "application/json", Origin: url },
    body: JSON.stringify({ state: { ...snapshot, schema: "otro-formato" } }),
  });
  assert.equal(unsafeState.status, 400, "El servidor rechaza snapshots con formato desconocido.");

  const sourceResponse = await fetch(url + "/fuentes/sprints/sprint_backlog_v1.4_2026-10-21.md");
  assert.equal(sourceResponse.status, 200, "Los documentos fuente siguen disponibles.");
  const unsafe = await fetch(url + "/api/abrir-documento", {
    method: "POST",
    headers: { "Content-Type": "application/json", Origin: url },
    body: JSON.stringify({ url: "/fuentes/../secreto.md" }),
  });
  assert.equal(unsafe.status, 400, "El servidor rechaza rutas que salen de las carpetas permitidas.");
  const loadedPage = await (await fetch(url + "/")).text();
  assert.ok(loadedPage.includes("window.APP_SERVER_STATE="), "El servidor carga el seguimiento guardado al servir la aplicación.");
  assert.ok(!loadedPage.includes("<script>alert(1)</script>"), "El estado guardado se escapa al integrarse al HTML.");
  const external = await fetch(url + "/api/abrir-documento", {
    method: "POST",
    headers: { "Content-Type": "application/json", Origin: "http://example.org" },
    body: JSON.stringify({ url: "/fuentes/alcance" }),
  });
  assert.equal(external.status, 403, "El servidor rechaza solicitudes que no vienen del dashboard local.");
  const oldUrl = url;
  const stopped = new Promise(resolveStop => server.once("exit", resolveStop));
  server.kill();
  await stopped;
  const restartedUrl = await startServer();
  assert.notEqual(restartedUrl, oldUrl, "La prueba vuelve a abrir el servidor en un puerto distinto.");
  const restored = await (await fetch(restartedUrl + "/api/dashboard-state")).json();
  assert.deepEqual(restored.state, snapshot, "Los cambios sobreviven el reinicio del servidor y el cambio de puerto.");
  const restoredHtml = await (await fetch(restartedUrl + "/")).text();
  assert.ok(restoredHtml.includes("window.APP_SERVER_STATE="), "El dashboard recibe el estado persistido en la reapertura.");
  console.log("OK: estado JSON persistente entre reinicios/puertos, carga al reabrir, CSP con nonce, cinco vistas y rutas locales seguras.");
} finally {
  if (server && server.exitCode === null && server.signalCode === null) {
    const stopped = new Promise(resolveStop => server.once("exit", resolveStop));
    server.kill();
    await stopped;
  }
  await rm(temporary, { recursive: true, force: true });
}
