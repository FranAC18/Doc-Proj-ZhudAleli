from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent
SOURCE = ROOT.parent / "index.html"
TARGET = ROOT / "web" / "index.html"

patches = [
    (
        '''function evidenceControl(value){var v=String(value||"").trim();if(!v)return "";if(safeUrl(v))return '<a class="evidence-link" href="'+esc(v)+'" target="_blank" rel="noopener noreferrer"><i data-lucide="external-link"></i> Evidencia</a>';return '<button class="evidence-link" type="button" data-copy-evidence="'+esc(v)+'"><i data-lucide="copy"></i> Copiar ruta</button>'}''',
        '''function evidenceControl(value){var v=String(value||"").trim();if(!v)return "";if(safeUrl(v))return '<a class="evidence-link" href="'+esc(v)+'" target="_blank" rel="noopener noreferrer"><i data-lucide="external-link"></i> Evidencia</a>';return '<button class="evidence-link" type="button" data-open-evidence="'+esc(v)+'"><i data-lucide="folder-open"></i> Abrir evidencia</button>'}''',
    ),
    (
        '''function combine(base,extra){return {schema:KEY,selectedSprint:extra.selectedSprint||base.selectedSprint,taskOverrides:Object.assign({},base.taskOverrides,extra.taskOverrides),customTasks:extra.customTasks.length?extra.customTasks:base.customTasks,customSprints:extra.customSprints.length?extra.customSprints:base.customSprints,sprintStates:Object.assign({},base.sprintStates,extra.sprintStates),storyOverrides:Object.assign({},base.storyOverrides,extra.storyOverrides),customStories:extra.customStories.length?extra.customStories:base.customStories,requirementOverrides:Object.assign({},base.requirementOverrides,extra.requirementOverrides),customRequirements:extra.customRequirements.length?extra.customRequirements:base.customRequirements,criteriaDone:Object.assign({},base.criteriaDone,extra.criteriaDone),storyOrder:extra.storyOrder.length?extra.storyOrder:base.storyOrder,audit:extra.audit.length?extra.audit:base.audit}}''',
        '''function combine(base,extra,complete){return {schema:KEY,selectedSprint:complete?extra.selectedSprint:(extra.selectedSprint||base.selectedSprint),taskOverrides:Object.assign({},base.taskOverrides,extra.taskOverrides),customTasks:complete?extra.customTasks:(extra.customTasks.length?extra.customTasks:base.customTasks),customSprints:complete?extra.customSprints:(extra.customSprints.length?extra.customSprints:base.customSprints),sprintStates:Object.assign({},base.sprintStates,extra.sprintStates),storyOverrides:Object.assign({},base.storyOverrides,extra.storyOverrides),customStories:complete?extra.customStories:(extra.customStories.length?extra.customStories:base.customStories),requirementOverrides:Object.assign({},base.requirementOverrides,extra.requirementOverrides),customRequirements:complete?extra.customRequirements:(extra.customRequirements.length?extra.customRequirements:base.customRequirements),criteriaDone:Object.assign({},base.criteriaDone,extra.criteriaDone),storyOrder:complete?extra.storyOrder:(extra.storyOrder.length?extra.storyOrder:base.storyOrder),audit:complete?extra.audit:(extra.audit.length?extra.audit:base.audit)}}''',
    ),
    (
        '''function load(){var base=migrate(DATA.tracking||{}),raw=null;try{raw=localStorage.getItem(KEY)||localStorage.getItem("thesis_agile_traceability_v1")||localStorage.getItem("tesis_scrum_app_v2")||localStorage.getItem("tesis_scrum_light_v1")||localStorage.getItem("zhud-aleli-gantt-v1");if(raw)state=combine(base,migrate(JSON.parse(raw)));else state=base}catch(e){state=base;toast("No se pudieron leer datos guardados; se cargó el modelo del proyecto.")};if(!state.sprintStates)state.sprintStates={};if(!state.selectedSprint||!getSprint(state.selectedSprint)){var open=getSprints().find(function(s){return !isClosed(s.id)});state.selectedSprint=open?open.id:(getSprints()[0]||{}).id||BACKLOG}state.view="backlog";state.query="";persist()}''',
        '''function load(){var base=migrate(DATA.tracking||{}),serverRaw=window.APP_SERVER_STATE,server=migrate(serverRaw||{}),raw=null;try{state=serverRaw?combine(base,server,true):base;raw=localStorage.getItem(KEY)||localStorage.getItem("thesis_agile_traceability_v1")||localStorage.getItem("tesis_scrum_app_v2")||localStorage.getItem("tesis_scrum_light_v1")||localStorage.getItem("zhud-aleli-gantt-v1");if(raw){var stored=JSON.parse(raw);state=combine(state,migrate(stored),!!stored&&stored.schema===KEY)}}catch(e){state=serverRaw?combine(base,server,true):base;toast("No se pudieron leer datos guardados; se cargó el respaldo local del proyecto.")};if(!state.sprintStates)state.sprintStates={};if(!state.selectedSprint||!getSprint(state.selectedSprint)){var open=getSprints().find(function(s){return !isClosed(s.id)});state.selectedSprint=open?open.id:(getSprints()[0]||{}).id||BACKLOG}state.view="backlog";state.query="";persist()}''',
    ),
    (
        '''function persist(){try{localStorage.setItem(KEY,JSON.stringify(snapshot()));return true}catch(e){toast("No se pudo guardar el avance. Descarga un respaldo para conservarlo.");return false}}''',
        '''function saveServerSnapshot(data,exiting){if(location.protocol!=="http:"||location.hostname!=="127.0.0.1")return;var payload=JSON.stringify({state:data});if(exiting&&navigator.sendBeacon&&payload.length<60000&&navigator.sendBeacon("/api/dashboard-state",new Blob([payload],{type:"application/json"})))return;window.__zhudDashboardSaveQueue=(window.__zhudDashboardSaveQueue||Promise.resolve()).then(function(){return fetch("/api/dashboard-state",{method:"POST",headers:{"Content-Type":"application/json"},body:payload,keepalive:!!exiting})}).then(function(response){if(!response.ok)throw new Error("No se pudo guardar el seguimiento local.")}).catch(function(){toast("No se pudo guardar el avance en el archivo local. Mantén abierto el servidor e inténtalo de nuevo.")})}function persist(){var data=snapshot(),localSaved=true;try{localStorage.setItem(KEY,JSON.stringify(data))}catch(e){localSaved=false}saveServerSnapshot(data,false);if(!localSaved)toast("No se pudo guardar en el navegador; se intentará conservar en el archivo local.");return localSaved}''',
    ),
    (
        '''window.addEventListener("load",icons);window.addEventListener("beforeunload",persist)''',
        '''window.addEventListener("load",icons);window.addEventListener("beforeunload",function(){var data=snapshot();try{localStorage.setItem(KEY,JSON.stringify(data))}catch(e){}saveServerSnapshot(data,true)})''',
    ),
]

bridge = r'''<script id="local-evidence-bridge">
(function(){
  "use strict";
  var timer;
  function message(text){var box=document.getElementById("toast"),label=document.getElementById("toast-message");if(!box||!label)return;label.textContent=text;box.hidden=false;window.clearTimeout(timer);timer=window.setTimeout(function(){box.hidden=true},3300)}
  function routeFor(value){
    var raw=String(value||"").trim().replace(/^"(.*)"$/,"$1");
    if(/^\/(fuentes|evidencias)\//.test(raw))return raw;
    var normalized=raw.replace(/\//g,"\\");
    var roots=[
      {path:"F:\\Tesis\\App Tesis\\documentacion",route:"/fuentes"},
      {path:"F:\\Tesis\\App Tesis\\docs\\evidence",route:"/evidencias"}
    ];
    var lower=normalized.toLocaleLowerCase();
    for(var i=0;i<roots.length;i++){
      var root=roots[i],base=root.path.toLocaleLowerCase();
      if(lower.indexOf(base+"\\")===0){var tail=normalized.slice(root.path.length+1);return root.route+"/"+tail.split("\\").map(encodeURIComponent).join("/")}
    }
    return null;
  }
  function copyFallback(path){if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(path).then(function(){message("No se pudo abrir la ruta local; se copió al portapapeles.")},function(){message(path)});else message(path)}
  document.addEventListener("click",function(event){
    var button=event.target.closest&&event.target.closest("[data-open-evidence]");
    if(!button)return;
    event.preventDefault();event.stopPropagation();event.stopImmediatePropagation();
    var path=button.dataset.openEvidence.replace(/^"(.*)"$/,"$1"),route=routeFor(path);
    if(!route){copyFallback(path);return}
    fetch("/api/abrir-documento",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({url:route})})
      .then(function(response){return response.json().then(function(data){if(!response.ok)throw new Error(data.error||"No se pudo abrir la evidencia.");return data})})
      .then(function(){message("Evidencia abierta en el Explorador de archivos.")})
      .catch(function(){copyFallback(path)});
  },true);
})();
</script>'''

if not SOURCE.is_file():
    raise SystemExit(f"No se encontró el dashboard principal: {SOURCE}")
html = SOURCE.read_text(encoding="utf-8")
for old, new in patches:
    if old in html:
        html = html.replace(old, new, 1)
    elif new not in html:
        raise SystemExit("No se reconoció una función de la versión fuente; se canceló la sincronización.")
html = re.sub(r'\n?<script id="local-evidence-bridge">[\s\S]*?</script>\n?', "\n", html)
if '</body>' not in html:
    raise SystemExit("El HTML fuente no contiene el cierre de body.")
html = html.replace('</body>', bridge + '\n</body>', 1)
if 'id="view-backlog"' not in html or 'tesis_scrum_multireq_v1' not in html:
    raise SystemExit("El HTML fuente no parece ser el dashboard de trazabilidad más reciente.")
TARGET.parent.mkdir(parents=True, exist_ok=True)
TARGET.write_text(html, encoding="utf-8")
print(f"Dashboard actualizado: {TARGET}")
