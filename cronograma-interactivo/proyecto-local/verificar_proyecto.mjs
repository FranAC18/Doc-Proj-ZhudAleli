import { spawn } from "node:child_process";
import { createRequire } from "node:module";
import { mkdtemp, readFile, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join, resolve } from "node:path";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const root = resolve("cronograma-interactivo/proyecto-local");
const python = process.env.PYTHON || "python";
const chrome = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe";
const temporary = await mkdtemp(join(tmpdir(), "zhud-gantt-test-"));
const statePath = join(temporary, "seguimiento.json");
const processes = [];

function startServer(path) {
  return new Promise((resolveStart, rejectStart) => {
    const child = spawn(python, [join(root, "servidor.py"), "--no-browser", "--state-file", path], { cwd: root });
    processes.push(child);
    let output = "";
    let failure = "";
    child.stderr.on("data", chunk => { failure += chunk.toString(); });
    const timeout = setTimeout(() => rejectStart(Error("El servidor no arrancó.")), 10000);
    child.stdout.on("data", chunk => {
      output += chunk.toString();
      const match = output.match(/http:\/\/127\.0\.0\.1:\d+/);
      if (match) { clearTimeout(timeout); resolveStart({ child, url: match[0] }); }
    });
    child.on("error", error => { clearTimeout(timeout); rejectStart(error); });
    child.on("exit", code => {
      if (!output.includes("http://127.0.0.1:")) {
        clearTimeout(timeout);
        rejectStart(Error(`El servidor terminó con código ${code}. ${failure}`));
      }
    });
  });
}

let browser;
try {
  const first = await startServer(statePath);
  const second = await startServer(join(temporary, "otro-estado.json"));
  if (first.url === second.url) throw Error("Los dos proyectos eligieron el mismo puerto.");
  second.child.kill();
  const duplicate = await startServer(statePath);
  if (duplicate.url !== first.url) throw Error("Se abrió otro servidor para el mismo archivo.");
  await new Promise(resolveWait => duplicate.child.exitCode !== null ? resolveWait() : duplicate.child.once("exit", resolveWait));

  browser = await chromium.launch({ executablePath: chrome, headless: true, args: ["--no-sandbox"] });
  const page = await browser.newPage({ viewport: { width: 1360, height: 900 } });
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  await page.goto(first.url);
  await page.waitForFunction(() => document.querySelector("#file-status").textContent.includes("Avance cargado"));
  if (await page.locator("#metric-tasks").innerText() !== "27") throw Error("Faltan tareas.");
  const sprintSummary = page.locator("#sprint-overview > summary");
  await sprintSummary.click();
  if (await page.locator("#sprint-cards").isVisible()) throw Error("El resumen de sprints no se colapsó.");
  await sprintSummary.click();
  await page.locator("#sprint-next").click();
  await page.waitForFunction(() => document.querySelector("#sprint-cards").scrollLeft > 0);
  await page.locator("#sprint-prev").click();
  await page.locator("#tab-matrix").click();
  if (!(await page.locator("#panel-matrix").isVisible())) throw Error("El menú no abrió el seguimiento de tareas.");
  await page.locator("#tab-gantt").click();
  await page.locator('[data-open-resources="S1"]').click();
  if (!(await page.locator(".sprint-task-row").count())) throw Error("El detalle del sprint no muestra sus tareas.");
  await page.locator('[data-open="SB-S1-01"]').first().click();
  if (!(await page.locator("#status-form").isVisible())) throw Error("No se pudo editar una tarea desde el sprint.");
  await page.locator("#close-drawer").click();
  const catalog = await (await page.request.get(first.url + "/recursos-sprints.json")).json();
  if (!catalog.sprints.some(item => item.id === "S0") || !catalog.sprints.some(item => item.id === "S1")) throw Error("Faltan accesos de S0 o S1.");
  const evidence = await page.request.get(first.url + "/evidencias/S0/2026-07-21-verificacion-cierre-sprint-0.md");
  if (evidence.status() !== 200) throw Error("No se pudo abrir una evidencia de Sprint 0.");

  await page.locator('[data-open="SB-S2-01"]').first().click();
  await page.selectOption("#edit-status", "en_curso");
  await page.locator("#edit-evidence").fill("https://example.org/evidencia-sb-s2-01");
  await page.locator("#status-form button[type=submit]").click();
  await page.waitForFunction(() => document.querySelector("#file-status").textContent.includes("Avance guardado"));
  const written = JSON.parse(await readFile(statePath, "utf8"));
  if (written.updates["SB-S2-01"]?.status !== "en_curso") throw Error("El avance no llegó al archivo.");
  await page.locator('[data-open-resources="S0"]').click();
  await page.locator(".resource-add-panel > summary").click();
  await page.locator("#resource-label").fill("Acceso de prueba");
  await page.locator("#resource-url").fill("https://example.org/evidencia-s0");
  await page.locator('#resource-form button[type="submit"]').click();
  await page.waitForFunction(() => document.querySelector("#toast").textContent.includes("Acceso agregado"));
  const withResource = JSON.parse(await readFile(statePath, "utf8"));
  if (withResource.resources?.[0]?.sprint !== "S0") throw Error("El acceso de evidencia no se guardó.");
  await page.locator("#close-drawer").click();
  const [download] = await Promise.all([
    page.waitForEvent("download"),
    page.locator("#export-button").click(),
  ]);
  const exported = JSON.parse(await readFile(await download.path(), "utf8"));
  if (exported.updates["SB-S2-01"]?.status !== "en_curso") throw Error("La copia exportada no contiene el avance guardado.");
  if (!exported.resources?.some(item => item.label === "Acceso de prueba")) throw Error("La copia exportada no contiene los accesos por sprint.");

  const invalid = await page.request.post(first.url + "/api/seguimiento", {
    headers: { "Content-Type": "application/json" },
    data: JSON.stringify({ id: "SB-S2-01", record: { status: "verificada" } }),
  });
  if (invalid.status() !== 403) throw Error("El servidor aceptó una solicitud sin origen local.");
  const invalidDocument = await page.request.post(first.url + "/api/abrir-documento", {
    headers: { "Content-Type": "application/json", Origin: first.url },
    data: JSON.stringify({ url: "/fuentes/../secreto.md" }),
  });
  if (invalidDocument.status() !== 400) throw Error("El servidor aceptó una ruta documental insegura.");
  const source = await page.request.get(first.url + "/fuentes/sprints/sprint_backlog_v1.3_2026-10-14.md");
  if (source.status() !== 200) throw Error("No se pudo abrir una fuente documental.");
  await page.close();
  first.child.kill();
  await new Promise(resolveWait => first.child.once("exit", resolveWait));

  const restarted = await startServer(statePath);
  const reopened = await browser.newPage();
  reopened.on("pageerror", error => errors.push(error.message));
  await reopened.goto(restarted.url);
  await reopened.waitForFunction(() => document.querySelector("#file-status").textContent.includes("Avance cargado"));
  await reopened.locator('[data-open="SB-S2-01"]').first().click();
  if (await reopened.locator("#edit-status").inputValue() !== "en_curso") throw Error("El avance no se recuperó tras reiniciar.");
  if (await reopened.locator(".task-evidence-access a").getAttribute("href") !== "https://example.org/evidencia-sb-s2-01") throw Error("El enlace de evidencia no quedó clicable.");
  await reopened.locator("#close-drawer").click();
  await reopened.locator('[data-open-resources="S0"]').click();
  if (!(await reopened.locator(".resource-row").filter({ hasText: "Acceso de prueba" }).count())) throw Error("El acceso del sprint no se recuperó al reiniciar.");

  const imported = {
    format: "zhud-aleli-gantt-v1", edition: "1.1", exportedAt: new Date().toISOString(),
    updates: { "SB-S2-02": { status: "en_curso", evidence: "", reviewer: "", date: "", notes: "Desde el HTML anterior", updatedAt: new Date().toISOString() } },
  };
  await reopened.locator("#import-file").setInputFiles({
    name: "seguimiento-anterior.json", mimeType: "application/json", buffer: Buffer.from(JSON.stringify(imported)),
  });
  await reopened.waitForFunction(() => document.querySelector("#toast").textContent.includes("1 registros"));
  const afterImport = JSON.parse(await readFile(statePath, "utf8"));
  if (afterImport.updates["SB-S2-02"]?.notes !== "Desde el HTML anterior") throw Error("La importación no llegó al archivo.");
  if (!afterImport.resources?.some(item => item.label === "Acceso de prueba")) throw Error("La importación alteró los accesos existentes.");
  await reopened.locator('[data-remove-resource]').click();
  await reopened.waitForFunction(() => document.querySelector("#toast").textContent.includes("Acceso quitado"));
  const removed = JSON.parse(await readFile(statePath, "utf8"));
  if (removed.resources.some(item => item.label === "Acceso de prueba")) throw Error("El acceso quitado todavía está guardado.");
  if (errors.length) throw Error(errors.join(" | "));
  console.log("OK: carrusel plegable, menú, tareas por sprint, accesos S0/S1, alta/baja de enlaces, evidencia clicable, persistencia, importación, exportación y protección local.");
} finally {
  if (browser) await browser.close();
  for (const process of processes) {
    if (process.exitCode === null && process.signalCode === null) {
      const stopped = new Promise(resolveWait => process.once("exit", resolveWait));
      process.kill();
      await stopped;
    }
  }
  await rm(temporary, { recursive: true, force: true });
}
