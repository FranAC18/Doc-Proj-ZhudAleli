import { createRequire } from "node:module";
import { readFile } from "node:fs/promises";
import { resolve } from "node:path";
import { pathToFileURL } from "node:url";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const file = resolve("cronograma-interactivo/index.html");
const html = await readFile(file, "utf8");
const url = "https://gantt.local/";
const browser = await chromium.launch({
  executablePath: "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
  headless: true,
  args: ["--no-sandbox", "--disable-gpu"],
});
try {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 }, acceptDownloads: true });
  await page.route(url, route => route.fulfill({ body: html, contentType: "text/html" }));
  await page.addInitScript(() => {
    window.showSaveFilePicker = async () => (await navigator.storage.getDirectory()).getFileHandle("seguimiento_sprints_zhud_aleli.json", { create: true });
  });
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  await page.goto(url);
  await page.waitForSelector("#sprint-cards .sprint-card");
  if (await page.locator("#metric-tasks").innerText() !== "27") throw Error("Conteo de tareas incorrecto");
  if (await page.locator("#gantt .gantt-row").count() !== 34) throw Error("Filas iniciales incorrectas");
  await page.screenshot({ path: "cronograma-interactivo/vista-escritorio.png", fullPage: true });

  await page.locator('[data-open="SB-S2-01"]').first().click();
  await page.selectOption("#edit-status", "verificada");
  await page.locator("#status-form button[type=submit]").click();
  if (!(await page.locator("#form-error").innerText()).includes("evidencia")) throw Error("Faltó exigir evidencia");
  await page.fill("#edit-evidence", "Prueba de acceso revisada");
  await page.fill("#edit-reviewer", "Revisión local de prueba");
  await page.fill("#edit-date", "2026-10-13");
  await page.locator("#status-form button[type=submit]").click();
  if (await page.locator("#metric-verified").innerText() !== "1") throw Error("No se actualizó el avance");
  await page.waitForFunction(() => document.querySelector("#file-status").textContent.includes("Archivo actualizado"));
  const written = await page.evaluate(async () => {
    const handle = await (await navigator.storage.getDirectory()).getFileHandle("seguimiento_sprints_zhud_aleli.json");
    return JSON.parse(await (await handle.getFile()).text());
  });
  if (written.updates["SB-S2-01"]?.status !== "verificada") throw Error("El botón Guardar no actualizó el archivo");
  await page.evaluate(() => localStorage.removeItem("zhud-aleli-gantt-v1"));
  await page.reload();
  await page.waitForFunction(() => document.querySelector("#metric-verified").textContent === "1");
  if (!(await page.locator("#file-status").innerText()).includes("Archivo cargado")) throw Error("El index no recuperó el archivo");
  await page.locator('[data-kind="hu"]').check();
  if (await page.locator("#gantt .gantt-row").count() !== 85) throw Error("No se mostraron las 51 HU");
  for (const kind of ["ht", "rf", "rnf"]) await page.locator(`[data-kind="${kind}"]`).check();
  if (await page.locator("#gantt .gantt-row").count() !== 164) throw Error("No se mostraron todos los requisitos e historias");
  await page.locator('[data-tab="matrix"]').click();
  if (await page.locator("#task-table tr").count() !== 27) throw Error("La matriz no muestra las 27 tareas");
  await page.locator('[data-tab="pending"]').click();
  if (await page.locator(".pending-card").count() !== 24) throw Error("Faltan decisiones o propuestas");
  await page.locator('[data-tab="gantt"]').click();
  await page.evaluate(() => {
    HTMLAnchorElement.prototype.click = function () { window.__ganttExportUrl = this.href; };
  });
  await page.locator("#export-button").click();
  const exported = await page.evaluate(async () => (await fetch(window.__ganttExportUrl)).text());
  const exportData = JSON.parse(exported);
  if (exportData.format !== "zhud-aleli-gantt-v1" || exportData.updates["SB-S2-01"]?.status !== "verificada") throw Error("Exportación incorrecta");
  const restored = await browser.newPage();
  await restored.route(url, route => route.fulfill({ body: html, contentType: "text/html" }));
  await restored.goto(url);
  if (await restored.locator("#metric-verified").innerText() !== "0") throw Error("El contexto nuevo heredó datos locales");
  await restored.locator("#import-file").setInputFiles({
    name: "seguimiento.json", mimeType: "application/json", buffer: Buffer.from(exported),
  });
  if (await restored.locator("#metric-verified").innerText() !== "1") throw Error("La importación no restauró el seguimiento");
  await restored.close();
  if (errors.length) throw Error(errors.join(" | "));
  const mobile = await browser.newPage({ viewport: { width: 390, height: 844 } });
  await mobile.route(url, route => route.fulfill({ body: html, contentType: "text/html" }));
  mobile.on("pageerror", error => errors.push(error.message));
  await mobile.goto(url);
  await mobile.screenshot({ path: "cronograma-interactivo/vista-movil.png", fullPage: true });
  if (errors.length) throw Error(errors.join(" | "));
  const direct = await browser.newPage();
  await direct.goto(pathToFileURL(file).href);
  if (await direct.locator("#metric-tasks").innerText() !== "27") throw Error("El index no abrió directamente como archivo");
  const browserSupport = await direct.evaluate(() => ({ secure: isSecureContext, picker: typeof showSaveFilePicker, idb: typeof indexedDB }));
  if (!browserSupport.secure || browserSupport.picker !== "function" || browserSupport.idb !== "object") throw Error("Chrome no permite vincular un archivo desde file:// en este equipo");
  await direct.close();
  console.log("OK: Gantt, validación, guardado JSON, recuperación desde archivo al abrir index, exportación, importación, vista móvil y apertura file://.");
} finally {
  await browser.close();
}
