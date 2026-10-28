import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";

const html = await readFile(new URL("./index.html", import.meta.url), "utf8");
const scripts = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map((match) => match[1]);
const dataScript = scripts.find((script) => script.includes("window.APP_DATA="));
const appScript = scripts.find((script) => script.includes("var DATA=window.APP_DATA"));
assert.ok(dataScript, "Los datos del proyecto están integrados en el HTML.");
assert.ok(appScript, "La aplicación está implementada en JavaScript nativo.");
new vm.Script(appScript, { filename: "dashboard-inline.js" });

const appData = JSON.parse(dataScript.slice("window.APP_DATA=".length).replace(/;\s*$/, ""));
const project = appData.project;
const normalizerStart = appScript.indexOf("function reconcilePlan(");
const normalizerEnd = appScript.indexOf("function migrate(", normalizerStart);
assert.ok(normalizerStart >= 0 && normalizerEnd > normalizerStart, "El tablero concilia el calendario nuevo con el avance local.");
const normalizerContext = { projectItems: project.items };
vm.createContext(normalizerContext);
vm.runInContext(appScript.slice(normalizerStart, normalizerEnd), normalizerContext);
const savedProgress = {
  taskOverrides: { "SB-S2-01": { sprint: "S2", start: "2026-10-13", end: "2026-10-26", status: "progress", evidence: "evidencia local" } },
  storyOverrides: { "HU-REP-001": { sprint: "S6", start: "2026-12-08", end: "2026-12-21" } },
  requirementOverrides: {},
};
normalizerContext.reconcilePlan(savedProgress);
assert.equal(savedProgress.taskOverrides["SB-S2-01"].end, undefined, "La fecha vieja cede al plan vigente.");
assert.equal(savedProgress.taskOverrides["SB-S2-01"].status, "progress", "El avance guardado se conserva.");
assert.equal(savedProgress.taskOverrides["SB-S2-01"].evidence, "evidencia local", "La evidencia guardada se conserva.");
assert.equal(savedProgress.storyOverrides["HU-REP-001"].sprint, undefined, "La asignación guardada a S6 deja de ocultar el nuevo sprint propuesto.");
const count = (kind) => project.items.filter((item) => item.kind === kind).length;
assert.deepEqual([count("hu"), count("rf"), count("rnf"), count("ht"), count("task")], [56, 59, 9, 19, 27]);
assert.equal(project.pending.length, 27, "Se conservan los pendientes previos y se añaden las decisiones de superadministración.");
assert.ok(project.pending.find((item) => item.id === "SA-AUT-01"), "La autorización inicial de superadministración sigue visible como pendiente de evidencia.");
assert.ok(!project.pending.find((item) => item.id === "P-12").priority.includes("Sprint 6"), "El contenido público no figura en un S6 inexistente.");
assert.deepEqual(project.sprints.map((sprint) => [sprint.id, sprint.end]), [
  ["S1", "2026-10-27"], ["S2", "2026-11-08"], ["S3", "2026-11-19"],
  ["S4", "2026-11-30"], ["S5", "2026-12-20"], ["Cierre", "2026-12-23"],
], "El calendario vigente contiene S1–S5 y la entrega del 23 de diciembre.");
assert.ok(project.items.every((item) => !String(item.sprint || "").includes("S6")), "S6 no figura como sprint vigente en historias o tareas.");
assert.ok(project.items.filter((item) => item.id.startsWith("SB-S6-")).every((item) => !item.sprint && item.legacySprint), "Las tareas de S6 se conservan como historial pendiente de replanificación.");
assert.ok(appData.tracking.updates?.["SB-S1-01"], "Se integra el seguimiento local existente.");
assert.ok(appData.tracking.sprintStates?.S1?.closed, "Se conserva el cierre previamente registrado.");
const s1 = appData.resources.sprints.find((sprint) => sprint.id === "S1");
assert.equal(s1.planningInputs.allUserStoriesAsInput, false, "Las cinco HU candidatas nuevas no se incorporan retrospectivamente a S1.");
assert.equal(s1.planningInputs.requirementScope, "all", "El catálogo RF/RNF completo queda disponible para la revisión de alcance de S1.");
assert.deepEqual(s1.planningInputs.spotlightUserStories.map((story) => story.id), ["HU-PWA-001"], "S1 destaca la HU móvil del plan.");
assert.deepEqual(s1.planningInputs.technicalStoryIds, ["HT-PRE-001", "HT-PRE-002", "HT-PRE-003", "HT-PRE-004", "HT-PRE-005", "HT-GEN-008"]);
assert.deepEqual(s1.planningInputs.storyIds, project.items.filter((item) => item.kind === "hu" && !/^HU-ACC-00[5-9]$/.test(item.id)).map((story) => story.id), "S1 conserva los 51 insumos originales.");
for (const id of s1.planningInputs.technicalStoryIds) {
  const technicalStory = project.items.find((item) => item.kind === "ht" && item.id === id);
  assert.ok(technicalStory, `${id} existe en la pila de historias técnicas.`);
  assert.ok(technicalStory.tasks.every((taskId) => project.items.some((item) => item.kind === "task" && item.id === taskId)), `${id} apunta a tareas SB existentes.`);
}
assert.ok(project.items.find((item) => item.id === "HT-GEN-008").tasks.includes("SB-S6-05"), "HT-GEN-008 conserva el vínculo histórico con SB-S6-05.");
const pwaStory = project.items.find((item) => item.id === "HU-PWA-001");
assert.ok(pwaStory.tasks.includes("SB-S1-04") && pwaStory.sprint.includes("S4"), "La revisión PWA en S1 conserva el sprint de entrega S4-S5 de HU-PWA-001.");
assert.equal(s1.status, "Periodo concluido · resultado parcial", "El periodo S1 no declara completados sus pendientes.");
const requirementIds = new Set(project.items.filter((item) => ["rf", "rnf"].includes(item.kind)).map((item) => item.id));
const storyIds = new Set(project.items.filter((item) => item.kind === "hu").map((item) => item.id));
const taskIds = new Set(project.items.filter((item) => item.kind === "task").map((item) => item.id));
assert.ok(project.items.filter((item) => item.kind === "hu").every((story) => story.rf.every((id) => requirementIds.has(id))), "Cada HU referencia requisitos existentes.");
assert.ok(project.items.filter((item) => item.kind === "hu").every((story) => story.tasks.every((id) => taskIds.has(id))), "Cada tarea referenciada desde una HU existe.");
assert.ok(project.items.filter((item) => item.kind === "task").every((task) => task.hu.every((id) => storyIds.has(id))), "Cada relación tarea → HU apunta a una historia existente.");
const technicalStoryIds = new Set(project.items.filter((item) => item.kind === "ht").map((item) => item.id));
assert.ok(project.items.filter((item) => item.kind === "task").every((task) => (task.ht || []).every((id) => technicalStoryIds.has(id))), "Cada relación tarea → HT apunta a una historia técnica existente.");
const s1TaskRelations = Object.fromEntries(project.items.filter((item) => item.kind === "task" && item.sprint === "S1").map((task) => [task.id, { hu: task.hu, ht: task.ht }]));
assert.deepEqual(s1TaskRelations["SB-S1-01"], { hu: [], ht: ["HT-PRE-001"] });
assert.deepEqual(s1TaskRelations["SB-S1-02"], { hu: [], ht: ["HT-PRE-002"] });
assert.deepEqual(s1TaskRelations["SB-S1-03"], { hu: [], ht: ["HT-PRE-003"] });
assert.deepEqual(s1TaskRelations["SB-S1-04"], { hu: ["HU-PWA-001"], ht: ["HT-PRE-004"] }, "La revisión móvil S1 mantiene HU-PWA-001 y su HT sin cambiar su sprint de entrega.");
assert.deepEqual(s1TaskRelations["SB-S1-05"], { hu: [], ht: ["HT-PRE-005", "HT-GEN-008"] });
assert.ok(html.includes('id="task-relation-options"') && html.includes("function fillTaskRelations") && html.includes("taskRelationDraft"), "El formulario deja ver y editar las relaciones HU y HT.");
assert.ok(html.includes('.task-relation-option input[type=checkbox]{flex:0 0 16px') && html.includes('.requirement-option input[type=checkbox]{flex:0 0 16px'), "Los selectores de relaciones y requisitos mantienen casillas compactas.");
assert.ok(html.includes('data-task-relation-filter="s1"') && appScript.includes('taskRelationKind=sprintId==="S1"?"s1":"all"'), "Las tareas de S1 abren el filtro de insumos correspondiente.");
assert.ok(html.includes('.task-card-relations .story-relation-chip{') && appScript.includes("function relationMeta(item)"), "Las relaciones muestran contexto en el selector y en las tarjetas del Kanban.");
assert.ok(appScript.includes('optgroup label="Sprint de entrega"') && appScript.includes('optgroup label="Alcance de revisión"') && appScript.includes("S1 no tiene HUs de entrega asignadas"), "El filtro de backlog distingue la entrega del análisis de S1 y explica la lista vacía.");
assert.ok(appScript.includes("function taskTechnicalStoryIds") && appScript.includes("ht:relations.ht"), "El tablero y el guardado conservan las relaciones con HT.");
assert.ok(appScript.includes('taskTechnicalStoryIds(t)') && appScript.includes('storyHasSprint(story,t.sprint)'), "Las HT aparecen en cronograma y los vínculos de revisión no mueven el sprint de entrega de una HU.");


const relationStart = appScript.indexOf("function taskRelations(");
const relationEnd = appScript.indexOf("function storyTasks(", relationStart);
assert.ok(relationStart >= 0 && relationEnd > relationStart, "Está implementada la lectura de relaciones HU/HT.");
const relationContext = {
  state: { taskOverrides: {} },
  allStories: () => project.items.filter((item) => item.kind === "hu"),
  allTechnicalStories: () => project.items.filter((item) => item.kind === "ht"),
  getStory: (id) => project.items.find((item) => item.kind === "hu" && item.id === id),
  getTechnicalStory: (id) => project.items.find((item) => item.kind === "ht" && item.id === id),
};
vm.createContext(relationContext);
vm.runInContext(appScript.slice(relationStart, relationEnd), relationContext);
for (const id of ["SB-S1-01", "SB-S1-02", "SB-S1-03", "SB-S1-04", "SB-S1-05"]) {
  const task = project.items.find((item) => item.id === id);
  assert.deepEqual(JSON.parse(JSON.stringify(relationContext.taskRelations(task))), { hu: task.hu, ht: task.ht }, "Relaciones fuente de " + id + " se muestran completas.");
}

const viewNames = ["backlog", "requirements", "kanban", "gantt", "audit"];
for (const view of viewNames) assert.ok(html.includes(`id="view-${view}"`), `Existe la vista ${view}.`);
assert.equal((html.match(/data-view="(?:backlog|requirements|kanban|gantt|audit)"/g) || []).length, 5);
assert.ok(html.includes('KEY="tesis_scrum_multireq_v1"'));
assert.ok(html.includes('localStorage.setItem(KEY') && html.includes('localStorage.getItem("thesis_agile_traceability_v1")') && html.includes('localStorage.getItem("tesis_scrum_app_v2")'));
assert.ok(html.includes("function fallbackProject()") && ["RF-01", "RF-02", "RNF-01", "HU-01", "HU-02", "HU-03", "TSK-101", "TSK-104"].every((id) => html.includes(id)));
assert.ok(html.includes('id="story-requirement-options"') && html.includes("data-req-option"), "La HU permite seleccionar varios requisitos con búsqueda.");
assert.ok(html.includes('id="global-progress"') && html.includes('id="global-points"') && html.includes('id="global-covered"'), "Se muestran métricas globales de puntos y cobertura.");
assert.ok(html.includes('id="overview-technical-stories"') && appScript.includes('technicalStories=state.selectedSprint===BACKLOG'), "El resumen del sprint separa las HUs de entrega de las HT vinculadas.");
assert.ok(html.includes('id="overview-sprint-toggle"') && appScript.includes('el("overview-sprint-toggle").addEventListener("click",toggleSprint)'), "El resumen visible ofrece un botón para cerrar o reabrir el sprint con la lógica y confirmación existentes.");
assert.ok(appScript.includes('overviewToggle.querySelector("span").textContent=s?(overviewClosed?"Abrir Sprint":"Cerrar Sprint")') && appScript.includes('overviewToggle.disabled=!s'), "El botón visible muestra el estado correcto y se deshabilita en el backlog general.");
assert.ok(appScript.includes("function requirementCoverage") && appScript.includes("function renderGlobalProgress") && appScript.includes("function storyRequirementIds"));
assert.ok(html.includes('id="requirement-sprint-filter"') && html.includes('id="requirement-sprint-context"') && html.includes("Sprint relacionado"), "El catálogo incluye filtros rotulados por sprint y el alcance contextual de S1.");
assert.ok(html.includes('data-view-s1-input') && appScript.includes('setView("backlog");el("backlog-sprint-filter").value=S1_INPUT'), "El panel S1 permite abrir directamente las HUs vinculadas en Product Backlog.");
assert.ok(appScript.includes("function requirementMatchesSprint") && appScript.includes("function storiesInRequirementScope") && appScript.includes("function renderSprintInputContext"));
assert.ok(appScript.includes('percent===null?"—"') && appScript.includes("Sin calcular: no hay Story Points estimados"), "Los porcentajes sin estimaciones se muestran como no calculables, no como 0%.");
assert.ok(appScript.includes('optgroup label="Alcance de revisi\u00f3n"') && appScript.includes('value="\'+S1_INPUT+\'"') && appScript.includes("function sprintInputBadge"), "El backlog separa el alcance de revisi\u00f3n S1 del sprint de entrega.");
assert.ok(html.includes('requirementIds:["RF-01","RNF-01"]') && html.includes('requirementIds:["RF-01","RF-02"]'), "El fallback y el modelo de HU admiten relaciones múltiples.");

const helperStart = appScript.indexOf("function storyHasSprint(");
const helperEnd = appScript.indexOf("function selectedSprint(", helperStart);
assert.ok(helperStart >= 0 && helperEnd > helperStart, "Están presentes los helpers de sprint y progreso.");
const sprintContext = { storyProgress: (story) => ({ complete: story.complete }) };
vm.createContext(sprintContext);
vm.runInContext(appScript.slice(helperStart, helperEnd), sprintContext);
assert.equal(sprintContext.storyHasSprint({ sprint: "S4–S5 (transversal)" }, "S4"), true, "La asignación transversal se filtra por S4.");
assert.equal(sprintContext.storyHasSprint({ sprint: "S4–S5 (transversal)" }, "S5"), true, "La asignación transversal se filtra por S5.");
assert.equal(sprintContext.storyHasSprint({ sprint: "S2–S5 (transversal)" }, "S4"), true, "Los rangos transversales incluyen los sprints intermedios.");
const unestimated = sprintContext.pointMetrics([{ storyPoints: null, complete: false }, { storyPoints: 0, complete: true }]);
assert.equal(unestimated.total, 0);
assert.equal(unestimated.percent, null, "Sin puntos estimados no se calcula un porcentaje ficticio.");
const estimated = sprintContext.pointMetrics([{ storyPoints: 3, complete: true }, { storyPoints: 2, complete: false }]);
assert.equal(estimated.accepted, 3);
assert.equal(estimated.percent, 60, "El avance se calcula como puntos aceptados sobre puntos comprometidos.");
const scopeStart = appScript.indexOf("function requirementMatchesSprint(");
const scopeEnd = appScript.indexOf("function renderSprintInputContext(", scopeStart);
const scopeContext = {
  BACKLOG: "__BACKLOG__",
  requirementStories: (id) => ({ linked: [{ sprint: "S2" }, { sprint: "S3" }], empty: [] }[id] || []),
  getSprintResource: (id) => id === "S1" ? { planningInputs: { requirementScope: "all", allUserStoriesAsInput: true } } : null,
  storyHasSprint: (story, id) => story.sprint.split(/[^A-Z0-9]+/i).filter(Boolean).includes(id),
};
vm.createContext(scopeContext);
vm.runInContext(appScript.slice(scopeStart, scopeEnd), scopeContext);
assert.equal(scopeContext.requirementMatchesSprint({ id: "linked" }, "S2"), true);
assert.equal(scopeContext.requirementMatchesSprint({ id: "linked" }, "S4"), false);
assert.equal(scopeContext.requirementMatchesSprint({ id: "empty" }, "S1"), true, "S1 permite revisar el catálogo completo, incluso RNF aún sin HU.");
assert.equal(scopeContext.requirementMatchesSprint({ id: "empty" }, "__BACKLOG__"), true, "El filtro sin sprint conserva requisitos todavía no vinculados.");

const storyHelpersStart = appScript.indexOf("function sprintInputStories(");
const storyHelpersEnd = appScript.indexOf("function storyHasSprint(", storyHelpersStart);
const storyContext = {
  getSprintResource: (id) => id === "S1" ? s1 : null,
  allStories: () => project.items.filter((item) => item.kind === "hu"),
  getStory: (id) => project.items.find((item) => item.kind === "hu" && item.id === id),
  esc: (value) => String(value ?? ""),
};
vm.createContext(storyContext);
vm.runInContext(appScript.slice(storyHelpersStart, storyHelpersEnd), storyContext);
assert.equal(storyContext.sprintInputStories("S1").length, 51);
assert.equal(storyContext.isSprintInputStory("HU-ACC-001"), true, "Una HU del backlog queda etiquetada como insumo de S1.");
assert.equal(storyContext.isSprintInputStory("HU-PWA-001"), true);
assert.equal(storyContext.sprintSpotlight("HU-PWA-001").purpose, "Revisar recorridos móviles");

const backlogFilterStart = appScript.indexOf("function storiesForFilter(");
const backlogFilterEnd = appScript.indexOf("function renderBacklog(", backlogFilterStart);
const backlogContext = {
  BACKLOG: "__BACKLOG__",
  S1_INPUT: "__S1_INPUT__",
  state: { query: "" },
  el: () => ({ value: "__S1_INPUT__" }),
  orderedStories: () => project.items.filter((item) => item.kind === "hu"),
  isSprintInputStory: (id) => s1.planningInputs.storyIds.includes(id),
  storyHasSprint: (story, id) => story.sprint.split(/[^A-Z0-9]+/i).filter(Boolean).includes(id),
  storyRequirementIds: () => [],
  getRequirement: () => null,
};
vm.createContext(backlogContext);
vm.runInContext(appScript.slice(backlogFilterStart, backlogFilterEnd), backlogContext);
assert.equal(backlogContext.storiesForFilter().length, 51, "El filtro de S1 devuelve las HUs de insumo, no un backlog vacío.");
backlogContext.el = () => ({ value: "S1" });
assert.equal(backlogContext.storiesForFilter().length, 0, "El filtro de destino S1 permanece separado del filtro de insumos.");

for (const id of ["story-dialog", "requirement-dialog", "task-dialog", "schedule-dialog", "sprint-dialog", "confirm-dialog", "detail-drawer"]) {
  assert.ok(html.includes(`id="${id}"`), `Existe la interacción modal ${id}.`);
}
for (const feature of ["navigationStack=[]", "navigationStack.push", "navigationStack.pop", "data-criterion-story", "data-reorder", "dragstart", "dataTransfer.getData", "schedule-reason", "data-navigate-requirement", "data-navigate-story"]) {
  assert.ok(appScript.includes(feature) || html.includes(feature), `Está implementado ${feature}.`);
}
assert.ok(html.includes("unpkg.com/lucide@latest"));
assert.ok(!/<link\s+rel="stylesheet"/i.test(html), "El CSS está dentro del HTML.");
assert.ok(!/(?:window\.)?(?:alert|prompt|confirm)\s*\(/.test(appScript), "No usa diálogos del navegador.");
assert.ok(!appScript.includes("fetch(") && !appScript.includes("/api/"), "No requiere backend ni endpoints.");

const staticMarkup = html.slice(0, html.indexOf("<script>window.APP_DATA"));
const ids = [...staticMarkup.matchAll(/\bid="([^"]+)"/g)].map((match) => match[1]);
assert.equal(new Set(ids).size, ids.length, "Los ID del HTML no se repiten.");
const idSet = new Set(ids);
const referencedIds = [...appScript.matchAll(/el\("([^"]+)"\)/g)].map((match) => match[1]);
const missingIds = [...new Set(referencedIds.filter((id) => !idSet.has(id)))];
assert.deepEqual(missingIds, [], "Cada referencia estática a un elemento encuentra su ID en el HTML.");
console.log("Dashboard v5 verificado: filtro RF/RNF por sprint, alcance y trazabilidad S1, porcentaje estimado por Story Points, cinco vistas, relaciones N:M, navegación, modales y persistencia.");
