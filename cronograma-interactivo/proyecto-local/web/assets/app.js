(async()=>{
    "use strict";
    const [data,resourceCatalog]=await Promise.all(["/datos-proyecto.json","/recursos-sprints.json"].map(url=>fetch(url,{cache:"no-store"}).then(response=>{if(!response.ok)throw Error("No se pudieron cargar los datos del cronograma.");return response.json()})));
    let byId=new Map(data.items.map(item=>[item.id,item]));
    const sprintById=new Map(data.sprints.map(item=>[item.id,item]));
    const sourceTasks=data.items.filter(item=>item.kind==="task");
    let tasks=[...sourceTasks];
    const validStatuses=new Set(["sin_verificar","en_curso","bloqueada","realizada","verificada"]);
    const names={sin_verificar:"Sin verificar",en_curso:"En curso",bloqueada:"Bloqueada",realizada:"Realizada",verificada:"Verificada"};
    const colors={sin_verificar:"#a69aa5",en_curso:"#2769a8",bloqueada:"#a82048",realizada:"#a05a00",verificada:"#087a70"};
    const kindNames={sprint:"Sprint",task:"Tarea",hu:"Historia de usuario",ht:"Historia técnica",rf:"Requisito funcional",rnf:"Requisito no funcional"};
    const state={updates:{},resources:[],customTasks:[],taskEdits:{},sprintStates:{},audit:[],q:"",sprint:"all",status:"all",dayWidth:15,kinds:new Set(["sprint","task"]),activeId:null,activeSprint:null};
    const el=id=>document.getElementById(id);
    const date=iso=>new Date(iso+"T00:00:00Z");
    const dayMs=86400000;
    const projectStart=date(data.window.start),projectEnd=date(data.window.end);
    const totalDays=Math.round((projectEnd-projectStart)/dayMs)+1;
    const dayIndex=iso=>Math.round((date(iso)-projectStart)/dayMs);
    const fmt=iso=>new Intl.DateTimeFormat("es-EC",{day:"numeric",month:"short",timeZone:"UTC"}).format(date(iso));
    const localToday=()=>{const parts=Object.fromEntries(new Intl.DateTimeFormat("en-US",{timeZone:"America/Guayaquil",year:"numeric",month:"2-digit",day:"2-digit"}).formatToParts(new Date()).filter(part=>part.type!=="literal").map(part=>[part.type,part.value]));return `${parts.year}-${parts.month}-${parts.day}`};
    const norm=value=>String(value||"").normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase();
    const esc=value=>String(value??"").replace(/[&<>"']/g,char=>({"&":"&amp;","<":"&lt;",">":"&gt;","\"":"&quot;","'":"&#39;"}[char]));
    const classKind=kind=>kindNames[kind]||kind;
    let toastTimer;
    function notify(message){const node=el("toast");node.textContent=message;node.hidden=false;clearTimeout(toastTimer);toastTimer=setTimeout(()=>node.hidden=true,4500)}
    async function requestJson(url, options={}) {
      const response=await fetch(url,{cache:"no-store",...options});
      const result=await response.json().catch(()=>({error:"Respuesta no válida del servidor."}));
      if(!response.ok)throw Error(result.error||"No se pudo completar la operación.");
      return result;
    }
    async function load() {
      try {
        const saved=await requestJson("/api/seguimiento");
        state.updates=saved.updates||{};
        state.resources=saved.resources||[];
        state.customTasks=saved.customTasks||[];
        state.taskEdits=saved.taskEdits||{};
        state.sprintStates=saved.sprintStates||{};
        state.audit=saved.audit||[];
        refreshTaskList();
        renderAll();
        fileStatus("Avance cargado desde el archivo local del proyecto.");
      } catch(error) {
        fileStatus("No se pudo leer el archivo de avance. " + error.message);
        notify("Comprueba que el servidor local sigue abierto.");
      }
    }
    function fileStatus(message){el("file-status").textContent=message}
    function refreshTaskList(){
      const adjusted=sourceTasks.map(item=>({...item,...(state.taskEdits[item.id]||{}),kind:"task",custom:false,source:true}));
      tasks=[...adjusted,...state.customTasks.map(item=>({...item,kind:"task",custom:true,source:false}))];
      byId=new Map([...data.items,...tasks].map(item=>[item.id,item]));
    }
    const taskStatus=id=>state.updates[id]?.status||"sin_verificar";
    const taskCount=sprint=>tasks.filter(item=>item.sprint===sprint).length;
    const verifiedCount=sprint=>tasks.filter(item=>item.sprint===sprint&&taskStatus(item.id)==="verificada").length;
    function sprintResourceCount(id){const sprint=resourceCatalog.sprints.find(item=>item.id===id);return (sprint?.resources.length||0)+state.resources.filter(item=>item.sprint===id).length}
    function safeEvidenceHref(value){const raw=String(value||"").trim();if(/^\/(fuentes|evidencias)\/[A-Za-z0-9_./-]+$/.test(raw)&&!raw.split("/").includes(".."))return raw;try{const parsed=new URL(raw);if(["http:","https:"].includes(parsed.protocol)&&parsed.hostname&&!parsed.username&&!parsed.password)return parsed.href}catch{}return ""}
    async function saveResource(event){event.preventDefault();const form=event.currentTarget,button=form.querySelector('button[type="submit"]');button.disabled=true;el("resource-error").textContent="";try{const saved=await requestJson("/api/recursos",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({action:"add",sprint:el("resource-sprint").value,label:el("resource-label").value,url:el("resource-url").value})});state.resources=saved.resources||[];state.audit=saved.audit||state.audit;renderOverview();renderAudit();showResourceDrawer(state.activeSprint);notify("Acceso agregado al sprint.")}catch(error){el("resource-error").textContent=error.message;button.disabled=false}}
    async function removeResource(id){const sprint=state.activeSprint;try{const saved=await requestJson("/api/recursos",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({action:"remove",id})});state.resources=saved.resources||[];state.audit=saved.audit||state.audit;renderOverview();renderAudit();showResourceDrawer(sprint);notify("Acceso quitado del sprint.")}catch(error){notify("No se pudo quitar el acceso: "+error.message)}}
    // Componentes de navegación y seguimiento por sprint.
    function resourceControl(value,label){
      const href=safeEvidenceHref(value);
      if(!href)return "";
      if(href.startsWith("/fuentes/")||href.startsWith("/evidencias/")){
        return '<button type="button" class="open-resource-button" data-open-resource-file="'+esc(href)+'">'+esc(label)+' <span aria-hidden="true">↗</span></button>';
      }
      const externalLabel=label==="Abrir en carpeta"?"Abrir enlace web":label;
      return '<a class="open-resource-link" href="'+esc(href)+'" target="_blank" rel="noopener">'+esc(externalLabel)+' <span aria-hidden="true">↗</span></a>';
    }

    function renderOverview(){
      el("metric-sprints").textContent="6";
      el("metric-tasks").textContent=tasks.length;
      el("metric-verified").textContent=tasks.filter(item=>taskStatus(item.id)==="verificada").length;
      el("metric-requirements").textContent=data.items.filter(item=>item.kind==="rf"||item.kind==="rnf").length;
      const track=el("sprint-cards");
      const oldScroll=track.scrollLeft;
      track.innerHTML=resourceCatalog.sprints.map(sprint=>{
        const planned=sprintById.get(sprint.id),count=planned?taskCount(sprint.id):0;
        const done=planned?verifiedCount(sprint.id):0,accessCount=sprintResourceCount(sprint.id);
        const actionLabel=count?"Tareas ("+count+") · Documentos ("+accessCount+")":"Documentos y evidencias ("+accessCount+")";
        const progress=planned?'<span class="sprint-progress-label">'+done+' de '+count+' tareas verificadas en el seguimiento local</span><div class="mini-progress" role="img" aria-label="'+done+' de '+count+' tareas verificadas"><i style="width:'+(count?done/count*100:0)+'%"></i></div>':"";
        const localState=state.sprintStates[sprint.id];
        const displayStatus=localState?localState.closed?"Cerrado":"En curso":sprint.status;
        const gantt=planned?'<button type="button" class="secondary" data-sprint-card="'+esc(sprint.id)+'">Ver Gantt</button>':"";
        return '<article class="sprint-card"><div class="sprint-card-top"><span class="sprint-status">'+esc(displayStatus)+'</span><span class="sprint-period">'+esc(sprint.period)+'</span></div><h3>'+esc(sprint.id)+' · '+esc(sprint.title)+'</h3><p class="sprint-card-summary">'+esc(sprint.statusDetail)+'</p>'+progress+'<div class="sprint-card-actions"><button type="button" class="primary" data-open-resources="'+esc(sprint.id)+'">'+actionLabel+'</button>'+gantt+'</div></article>';
      }).join("");
      track.scrollLeft=oldScroll;
      updateCarouselPosition();
    }

    function resourceRows(items,removable=false){
      return items.map(item=>{
        if(!safeEvidenceHref(item.url))return "";
        const remove=removable?'<button type="button" class="remove-resource" data-remove-resource="'+esc(item.id)+'" aria-label="Quitar '+esc(item.label)+'">Quitar</button>':"";
        return '<article class="resource-row"><div class="resource-row-main"><strong>'+esc(item.label)+'</strong>'+(item.note?'<p>'+esc(item.note)+'</p>':"")+'</div><div class="resource-row-actions">'+resourceControl(item.url,"Abrir en carpeta")+remove+'</div></article>';
      }).join("");
    }

    function showResourceDrawer(id,focusTasks=false){
      const sprint=resourceCatalog.sprints.find(item=>item.id===id);
      if(!sprint)return;
      state.activeSprint=id;state.activeId=null;
      el("drawer-kind").textContent=id+" · "+sprint.status;
      el("drawer-title").textContent=sprint.title;
      const groups=new Map();
      for(const item of sprint.resources){if(!groups.has(item.group))groups.set(item.group,[]);groups.get(item.group).push(item)}
      const sprintTasks=tasks.filter(task=>task.sprint===id);
      const taskRows=sprintTasks.map(task=>{
        const status=taskStatus(task.id),evidence=state.updates[task.id]?.evidence||"";
        const evidenceAccess=resourceControl(evidence,"Abrir evidencia");
        return '<article class="sprint-task-row"><div class="sprint-task-copy"><span class="sprint-task-code">'+esc(task.id)+'</span><span class="sprint-task-status" style="--dot:'+colors[status]+'">'+esc(names[status])+'</span><span class="sprint-task-title">'+esc(task.title)+'</span>'+(evidenceAccess?'<div class="task-evidence-access">'+evidenceAccess+'</div>':"")+'</div><div class="sprint-task-actions"><button type="button" class="secondary" data-open="'+esc(task.id)+'">Editar tarea</button></div></article>';
      }).join("");
        const sprintState=state.sprintStates[id];
        const sprintClosed=sprintState?sprintState.closed:sprint.status==="Cerrado";
        const sprintStatusLabel=sprintState?(sprintClosed?"Cerrado":"En curso"):sprint.status;
        let html='<p class="resource-status-note">'+esc(sprint.period)+' · '+esc(sprint.statusDetail)+'</p><section class="detail-section sprint-controls-detail"><span class="status-pill" style="--dot:'+(sprintClosed?"#8795a6":"#10b981")+'">'+esc(sprintStatusLabel)+'</span><button type="button" class="secondary" data-toggle-sprint="'+esc(id)+'" data-closed="'+String(sprintClosed)+'">'+(sprintClosed?"Reabrir sprint":"Cerrar sprint")+'</button></section><section class="detail-section" id="sprint-task-list"><h3>Tareas del sprint ('+sprintTasks.length+')</h3><p class="hint">Cambia el estado, registra observaciones o añade el acceso a la evidencia.</p>';
      html+=sprintTasks.length?'<div class="task-list">'+taskRows+'</div>':'<p class="hint">Esta etapa no tiene tareas del Gantt. Consulta su cierre y evidencias abajo.</p>';
      html+='</section>';
      for(const [group,items] of groups)html+='<section class="detail-section"><h3>'+esc(group)+'</h3><div class="resource-list">'+resourceRows(items)+'</div></section>';
      const added=state.resources.filter(item=>item.sprint===id);
      html+='<section class="detail-section"><h3>Accesos añadidos ('+added.length+')</h3>'+(added.length?'<div class="resource-list">'+resourceRows(added,true)+'</div>':'<p class="hint">Todavía no has agregado accesos a este sprint.</p>')+'</section>';
      html+='<section class="detail-section"><details class="resource-add-panel"><summary>Agregar documento o evidencia</summary><p class="hint">Agrega una URL web o una ruta local, como <code>/evidencias/.../archivo.md</code> o <code>/fuentes/seguimiento/archivo.md</code>. El acceso se guarda en este equipo.</p><form id="resource-form"><input type="hidden" id="resource-sprint" value="'+esc(id)+'"><div class="form-grid"><div class="field wide"><label for="resource-label">Nombre del acceso</label><input id="resource-label" maxlength="120" required placeholder="Ej. Acta de revisión"></div><div class="field wide"><label for="resource-url">URL o ruta del documento</label><input id="resource-url" maxlength="1200" required placeholder="https://… o /evidencias/…/archivo.md"></div></div><p class="error" id="resource-error" role="alert"></p><button type="submit" class="primary">Guardar acceso</button></form></details></section>';
      el("drawer-content").innerHTML=html;
      el("scrim").hidden=false;el("drawer").hidden=false;document.body.style.overflow="hidden";
      el("close-drawer").focus();
      el("resource-form").addEventListener("submit",saveResource);
      if(focusTasks)el("sprint-task-list").scrollIntoView({block:"start"});
    }

    function renderSources(){
      el("source-list").innerHTML=data.sources.map(item=>'<div class="source-item"><strong>'+esc(item.label)+'</strong>'+resourceControl(item.url,"Abrir en carpeta")+'</div>').join("");
    }

     function showDrawer(id){
      const item=byId.get(id)||sprintById.get(id);
      if(!item)return;
      state.activeId=id;
      el("drawer-kind").textContent=item.kind?classKind(item.kind):"Sprint";
      el("drawer-title").textContent=id+" · "+item.title;
      const isSprint=!item.kind,status=item.kind==="task"?taskStatus(id):null;
      let html='<dl class="meta"><div><dt>Ventana planificada</dt><dd>'+fmt(item.start)+'-'+fmt(item.end)+' de 2026</dd></div><div><dt>Prioridad o estado</dt><dd>'+esc(isSprint?"Plan propuesto":item.priority||item.sourceState||"-")+'</dd></div></dl>';
      if(item.kind==="task"&&state.activeSprint)html+='<div class="detail-section"><button type="button" class="secondary" data-return-sprint="'+esc(state.activeSprint)+'">← Volver a '+esc(state.activeSprint)+'</button></div>';
      html+='<div class="detail-section"><h3>'+(isSprint?"Objetivo":"Descripción o resultado esperado")+'</h3><p>'+esc(item.description||item.goal||"-")+'</p></div>';
      if(item.pilePosition)html+='<p class="hint">Posición en la pila de producto: '+item.pilePosition+' de 60 (orden propuesto).</p>';
      if(isSprint){
        const own=tasks.filter(task=>task.sprint===id);
        html+='<div class="detail-section"><h3>Avance registrado</h3><p>'+verifiedCount(id)+' de '+own.length+' tareas verificadas. Abre una tarea para ver su evidencia.</p>'+relatedButtons(own.map(task=>task.id))+'</div>';
      }else{
        html+='<div class="detail-section"><h3>Estado en el documento fuente</h3><p>'+esc(item.sourceState||"Sin estado fuente")+'</p></div>';
        if(item.criteria?.length)html+='<div class="detail-section"><h3>Criterios o comprobación prevista</h3><ol class="detail-list">'+item.criteria.map(c=>'<li>'+esc(c)+'</li>').join("")+'</ol></div>';
        for(const [field,label] of [["rf","Requisito de origen"],["hu","Historias de usuario"],["ht","Historias técnicas"],["tasks","Tareas vinculadas"]]){
          if(field in item)html+='<div class="detail-section"><h3>'+label+'</h3>'+relatedButtons(item[field])+'</div>';
        }
        if(item.related)html+='<div class="detail-section"><h3>Relación descrita</h3><p>'+esc(item.related)+'</p></div>';
        if(item.source)html+='<div class="detail-section"><h3>Documento fuente</h3>'+resourceControl(item.source,"Abrir en carpeta")+'</div>';
      }
      if(item.kind==="task"){
        const record=state.updates[id]||{};
         html+='<div class="detail-section"><h3>Registrar seguimiento de esta tarea</h3><p class="hint">Realizada requiere evidencia. Verificada requiere además fecha y nombre de quien revisó. El avance se guarda automáticamente en el archivo local.</p><form id="status-form"><div class="form-grid"><div class="field"><label for="edit-status">Estado</label><select id="edit-status">'+Object.entries(names).map(([value,label])=>'<option value="'+value+'" '+(status===value?"selected":"")+'>'+label+'</option>').join("")+'</select></div><div class="field"><label for="edit-date">Fecha de comprobación</label><input id="edit-date" type="date" value="'+esc(record.date||"")+'"></div><div class="field"><label for="edit-points">Story points</label><input id="edit-points" type="number" min="0" max="100" step="1" value="'+esc(record.points??"")+'" placeholder="Sin estimar"></div><div class="field"><label for="edit-reviewer">Persona que verificó</label><input id="edit-reviewer" type="text" value="'+esc(record.reviewer||"")+'" placeholder="Nombre o cargo"></div><div class="field wide"><label for="edit-evidence">Evidencia (acta, archivo, prueba o URL)</label><input id="edit-evidence" type="text" value="'+esc(record.evidence||"")+'" placeholder="https://… o /evidencias/…/archivo.md"><span class="hint">Para archivos locales, usa la ruta /fuentes/… o /evidencias/…</span></div><div class="field wide"><label for="edit-notes">Observaciones</label><textarea id="edit-notes">'+esc(record.notes||"")+'</textarea></div></div><p class="error" id="form-error" role="alert"></p><button type="submit" class="primary">Guardar seguimiento</button>'+(record.updatedAt?'<p class="hint">Última modificación local: '+esc(new Date(record.updatedAt).toLocaleString("es-EC"))+'</p>':"")+'</form>';
        const evidenceAccess=resourceControl(record.evidence,"Abrir evidencia");
        if(evidenceAccess)html+='<div class="task-evidence-access">'+evidenceAccess+'</div>';
        html+='</div>';
      }
      el("drawer-content").innerHTML=html;
      el("scrim").hidden=false;el("drawer").hidden=false;document.body.style.overflow="hidden";
      el("close-drawer").focus();
      if(item.kind==="task")el("status-form").addEventListener("submit",saveTask);
    }


    function months(){const result=[];let cursor=new Date(Date.UTC(2026,8,1));while(cursor<=projectEnd){const start=new Date(Math.max(cursor,projectStart));const next=new Date(Date.UTC(cursor.getUTCFullYear(),cursor.getUTCMonth()+1,1));const finish=new Date(Math.min(next.getTime()-dayMs,projectEnd.getTime()));const left=Math.round((start-projectStart)/dayMs);const days=Math.round((finish-start)/dayMs)+1;result.push({label:new Intl.DateTimeFormat("es-EC",{month:"long",year:"numeric",timeZone:"UTC"}).format(cursor),left,days});cursor=next}return result}
    function weekMarks(){const out=[];for(let i=0;i<totalDays;i++){const d=new Date(projectStart.getTime()+i*dayMs);if(d.getUTCDay()===1||i===0)out.push({left:i,label:fmt(d.toISOString().slice(0,10))})}return out}
    function overlaps(item,sprint){if(sprint==="all")return true;const window=sprintById.get(sprint);return item.start<=window.end&&item.end>=window.start}
    function matches(item){if(!item.start||!item.end||!state.kinds.has(item.kind)||!overlaps(item,state.sprint))return false;if(state.q&&!norm(item.id+" "+item.title+" "+(item.description||"")).includes(norm(state.q)))return false;if(state.status!=="all"){if(item.kind!=="task"||taskStatus(item.id)!==state.status)return false}return true}
    function displayRows(){const rows=[];for(const sprint of data.sprints){if(state.kinds.has("sprint")&&state.status==="all"&&(!state.q||norm(sprint.id+" "+sprint.title).includes(norm(state.q)))&&overlaps(sprint,state.sprint))rows.push({...sprint,kind:"sprint",sprint:sprint.id,description:sprint.goal});for(const kind of ["task","hu","ht","rf","rnf"]){const source=kind==="task"?tasks:data.items.filter(item=>item.kind===kind);rows.push(...source.filter(item=>item.kind===kind&&item.sprint===sprint.id&&matches(item)).sort((a,b)=>a.id.localeCompare(b.id)))}}return rows}
    function timelineHeader(width){const monthHtml=months().map(m=>`<div class="month" style="left:${m.left*state.dayWidth}px;width:${m.days*state.dayWidth}px">${esc(m.label)}</div>`).join("");const weekHtml=weekMarks().map(w=>`<div class="week" style="left:${w.left*state.dayWidth}px">${esc(w.label)}</div>`).join("");return `<div class="gantt-head"><div class="gantt-label-head">Elemento · abre para ver detalle</div><div class="gantt-head-track" style="width:${width}px">${monthHtml}${weekHtml}</div></div>`}
    function renderGantt(){const width=totalDays*state.dayWidth;document.documentElement.style.setProperty("--day-width",state.dayWidth+"px");const rows=displayRows();const today=localToday(),showToday=today>=data.window.start&&today<=data.window.end;const nowLeft=dayIndex(today)*state.dayWidth;el("gantt").innerHTML=timelineHeader(width)+(rows.length?rows.map(item=>{const x=dayIndex(item.start)*state.dayWidth+2,w=(dayIndex(item.end)-dayIndex(item.start)+1)*state.dayWidth-4;const status=item.kind==="task"?taskStatus(item.id):"sin_verificar";const small=item.kind==="sprint"?`${fmt(item.start)}–${fmt(item.end)}`:`${item.id} · ${item.sprint}`;const label=item.kind==="sprint"?item.title:item.title;return `<div class="gantt-row ${item.kind==="sprint"?"sprint-row":""}"><div class="gantt-label"><span class="type-icon ${item.kind}" aria-hidden="true">${item.kind==="sprint"?"S":item.kind==="task"?"T":item.kind.toUpperCase()}</span><button type="button" class="row-button" data-open="${esc(item.id)}" title="${esc(item.id+" · "+item.title)}"><b>${esc(label)}</b><small>${esc(small)}</small></button>${item.kind==="task"?`<span class="status-dot" style="--dot:${colors[status]}" title="${names[status]}"></span>`:""}</div><div class="track" style="width:${width}px">${showToday?`<div class="today-line" style="left:${nowLeft}px" title="Hoy"></div>`:""}<button type="button" class="bar ${item.kind} ${item.kind==="task"?"state-"+status:""} ${status==="verificada"?"verified":""} ${status==="bloqueada"?"blocked":""}" data-open="${esc(item.id)}" style="left:${x}px;width:${Math.max(w,8)}px" title="${esc(item.id+" · "+item.title+" · ventana "+fmt(item.start)+" a "+fmt(item.end))}">${w>115?esc(item.kind==="sprint"?item.id+" · "+item.title:item.id):""}</button></div></div>`}).join(""):`<div class="empty">No hay elementos para estos filtros. Prueba otro tipo, sprint o búsqueda.</div>`);el("gantt-count").textContent=`${rows.length} filas visibles. Los requisitos no funcionales aparecen como transversales y no tienen relación individual obligatoria con las tareas.`}
    function renderMatrix(){const filtered=tasks.filter(item=>(state.sprint==="all"||item.sprint===state.sprint)&&(!state.q||norm(item.id+" "+item.title).includes(norm(state.q)))&&(state.status==="all"||taskStatus(item.id)===state.status));el("task-table").innerHTML=filtered.map(item=>{const status=taskStatus(item.id);return `<tr><td><button type="button" class="text-button" data-open="${item.id}">${item.id}</button></td><td><b>${item.sprint}</b> · ${esc(item.title)}</td><td>${esc(item.priority)}</td><td class="code-list">${esc(item.hu.join(", ")||"Relación general")}</td><td class="code-list">${esc(item.ht.join(", ")||"Por seleccionar")}</td><td><span class="status-pill" style="--dot:${colors[status]}">${names[status]}</span></td></tr>`}).join("")||`<tr><td colspan="6" class="empty">No hay tareas con estos filtros.</td></tr>`}
    function renderPending(){el("pending-grid").innerHTML=data.pending.map(item=>`<article class="pending-card"><small>${esc(item.type)} · ${esc(item.priority)} · ${esc(item.id)}</small><h3>${esc(item.title)}</h3><p>${esc(item.detail)}</p></article>`).join("")}
    function relatedButtons(ids){return ids?.length?`<div class="links">${ids.map(id=>`<button type="button" data-open="${esc(id)}">${esc(id)}</button>`).join("")}</div>`:`<p class="hint">Sin relación directa registrada.</p>`}
    function closeDrawer(){el("drawer").hidden=true;el("scrim").hidden=true;document.body.style.overflow="";state.activeId=null;state.activeSprint=null}
    async function saveTask(event) {
      event.preventDefault();
      const id=state.activeId;
      const status=el("edit-status").value;
      const evidence=el("edit-evidence").value.trim();
      const reviewer=el("edit-reviewer").value.trim();
      const dateValue=el("edit-date").value;
       const notes=el("edit-notes").value.trim();
       const points=el("edit-points").value===""?null:Number(el("edit-points").value);
      let error="";
       if(points!==null&&(!Number.isInteger(points)||points<0||points>100))error="Los puntos deben ser un número entero entre 0 y 100.";
       else if(["realizada","verificada"].includes(status)&&!evidence)error="Para indicar que se realizó, agrega una evidencia concreta.";
      else if(status==="verificada"&&(!reviewer||!dateValue))error="Para verificar, agrega la persona que revisó y la fecha.";
      else if(dateValue&&dateValue>localToday())error="La fecha de comprobación no puede ser futura.";
      el("form-error").textContent=error;
      if(error)return;
      const button=event.submitter;
      button.disabled=true;
      try {
        const returnSprint=state.activeSprint;
        const saved=await requestJson("/api/seguimiento",{
          method:"POST",
          headers:{"Content-Type":"application/json"},
           body:JSON.stringify({id,record:{status,evidence,reviewer,date:dateValue,notes,points}})
        });
         state.updates=saved.updates||{};state.audit=saved.audit||state.audit;state.sprintStates=saved.sprintStates||state.sprintStates;
         refreshTaskList();renderAll();
        fileStatus("Avance guardado en el archivo local del proyecto.");
        notify("Seguimiento guardado para " + id + ".");
        if(returnSprint)showResourceDrawer(returnSprint,true);else closeDrawer();
      } catch(saveError) {
        el("form-error").textContent="No se pudo guardar: " + saveError.message;
        fileStatus("No se pudo escribir el archivo de avance. Revisa el mensaje en la tarea.");
        button.disabled=false;
      }
    }
    async function exportUpdates(){try{const current=await requestJson("/api/seguimiento");state.updates=current.updates||{};state.resources=current.resources||[];state.customTasks=current.customTasks||[];state.taskEdits=current.taskEdits||{};state.sprintStates=current.sprintStates||{};state.audit=current.audit||[];refreshTaskList();renderAll();const blob=new Blob([JSON.stringify(current,null,2)],{type:"application/json"});const url=URL.createObjectURL(blob);const anchor=document.createElement("a");anchor.href=url;anchor.download="seguimiento_sprints_zhud_aleli.json";document.body.appendChild(anchor);anchor.click();anchor.remove();setTimeout(()=>URL.revokeObjectURL(url),60000);notify("Copia de avance, tareas y bitácora descargada en JSON.")}catch(error){notify("No se pudo exportar: "+error.message)}}
    async function importUpdates(file) {
      if(!file)return;
      try {
        const parsed=JSON.parse(await file.text());
        const result=await requestJson("/api/importar",{
          method:"POST",
          headers:{"Content-Type":"application/json"},
          body:JSON.stringify(parsed)
        });
        state.updates=result.tracking.updates||{};
        state.resources=result.tracking.resources||[];
        state.customTasks=result.tracking.customTasks||[];
        state.taskEdits=result.tracking.taskEdits||{};
        state.sprintStates=result.tracking.sprintStates||{};
        state.audit=result.tracking.audit||[];
        refreshTaskList();renderAll();
        fileStatus("Archivo de avance actualizado en el proyecto.");
        notify("Se incorporaron " + result.count + " registros.");
      } catch(error) {
        notify("No se pudo importar: " + error.message);
      } finally {
        el("import-file").value="";
      }
    }
    document.addEventListener("click",event=>{const opener=event.target.closest("[data-open-resources]");if(opener){showResourceDrawer(opener.dataset.openResources);return}const remover=event.target.closest("[data-remove-resource]");if(remover)removeResource(remover.dataset.removeResource)});
    function switchTab(name){for(const tab of document.querySelectorAll(".tab")){const active=tab.dataset.tab===name;tab.setAttribute("aria-selected",String(active));el("panel-"+tab.dataset.tab).hidden=!active}if(name==="matrix")renderMatrix()}
    function renderAll(){renderOverview();renderGantt();renderMatrix();renderPending();renderSources()}
    for(const sprint of data.sprints){const option=document.createElement("option");option.value=sprint.id;option.textContent=sprint.id+" · "+sprint.title;el("sprint-filter").appendChild(option)}renderAll();load();
    el("search").addEventListener("input",event=>{state.q=event.target.value;renderGantt();renderMatrix()});el("sprint-filter").addEventListener("change",event=>{state.sprint=event.target.value;renderGantt();renderMatrix()});el("status-filter").addEventListener("change",event=>{state.status=event.target.value;renderGantt();renderMatrix()});el("zoom").addEventListener("change",event=>{state.dayWidth=Number(event.target.value);renderGantt()});for(const box of document.querySelectorAll("[data-kind]"))box.addEventListener("change",event=>{const kind=event.target.dataset.kind;if(event.target.checked)state.kinds.add(kind);else state.kinds.delete(kind);renderGantt()});
    document.addEventListener("click",event=>{const tab=event.target.closest("[data-tab]");if(tab){switchTab(tab.dataset.tab);return}const card=event.target.closest("[data-sprint-card]");if(card){state.sprint=card.dataset.sprintCard;el("sprint-filter").value=state.sprint;switchTab("gantt");renderGantt();el("gantt-wrap").scrollIntoView({block:"nearest"});return}const opener=event.target.closest("[data-open]");if(opener)showDrawer(opener.dataset.open)});el("close-drawer").addEventListener("click",closeDrawer);el("scrim").addEventListener("click",closeDrawer);document.addEventListener("keydown",event=>{if(event.key==="Escape"&&!el("drawer").hidden)closeDrawer()});el("export-button").addEventListener("click",exportUpdates);el("import-file").addEventListener("change",event=>importUpdates(event.target.files[0]));
    async function openResourceFile(url){
      try{
        await requestJson("/api/abrir-documento",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({url})});
        notify("Se abrió la carpeta del documento en el Explorador.");
      }catch(error){notify("No se pudo abrir el documento: "+error.message)}
    }

    function visibleSprintIndex(){
      const track=el("sprint-cards"),cards=[...track.querySelectorAll(".sprint-card")];
      if(!cards.length)return 0;
      const start=track.getBoundingClientRect().left;
      const index=cards.findIndex(card=>card.getBoundingClientRect().right>start+1);
      return index<0?cards.length-1:index;
    }

    function updateCarouselPosition(){
      const track=el("sprint-cards"),cards=track.querySelectorAll(".sprint-card"),position=visibleSprintIndex();
      if(!cards.length){el("carousel-position").textContent="Sin sprints";el("sprint-prev").disabled=true;el("sprint-next").disabled=true;return}
      const trackEnd=track.getBoundingClientRect().right;
      const lastVisible=[...cards].reduce((last,card,index)=>card.getBoundingClientRect().left<trackEnd-1?index:last,position);
      el("carousel-position").textContent=position===lastVisible?"Sprint "+(position+1)+" de "+cards.length:"Sprints "+(position+1)+"–"+(lastVisible+1)+" de "+cards.length;
      el("sprint-prev").disabled=track.scrollLeft<=1;
      el("sprint-next").disabled=track.scrollLeft>=track.scrollWidth-track.clientWidth-1;
    }

    function moveCarousel(direction){
      const track=el("sprint-cards"),cards=track.querySelectorAll(".sprint-card"),index=visibleSprintIndex();
      const target=Math.max(0,Math.min(cards.length-1,index+direction));
      if(cards[target])cards[target].scrollIntoView({behavior:matchMedia("(prefers-reduced-motion: reduce)").matches?"auto":"smooth",block:"nearest",inline:"start"});
    }

    el("sprint-prev").addEventListener("click",()=>moveCarousel(-1));
    el("sprint-next").addEventListener("click",()=>moveCarousel(1));
    el("sprint-cards").addEventListener("scroll",()=>requestAnimationFrame(updateCarouselPosition),{passive:true});
    el("sprint-cards").addEventListener("keydown",event=>{
      if(event.key==="ArrowLeft"||event.key==="ArrowRight"){event.preventDefault();moveCarousel(event.key==="ArrowRight"?1:-1)}
    });
    window.addEventListener("resize",updateCarouselPosition);
    document.addEventListener("click",event=>{
      const openFile=event.target.closest("[data-open-resource-file]");
      if(openFile){openResourceFile(openFile.dataset.openResourceFile);return}
      const returnSprint=event.target.closest("[data-return-sprint]");
      if(returnSprint){showResourceDrawer(returnSprint.dataset.returnSprint,true);return}
    });
    function boardGroups(){
      return [
        {id:"todo",label:"Por hacer",statuses:["sin_verificar","bloqueada"],color:"#7890aa"},
        {id:"progress",label:"En progreso",statuses:["en_curso"],color:"#3b82f6"},
        {id:"review",label:"En revisión",statuses:["realizada"],color:"#a78bfa"},
        {id:"done",label:"Completado",statuses:["verificada"],color:"#10b981"},
      ];
    }
    function taskEvidence(task){return state.updates[task.id]?.evidence||task.evidence||""}
    function renderKanban(){
      const filter=el("board-sprint-filter"),selected=filter.value||"all";
      const sprints=resourceCatalog.sprints;
      filter.innerHTML='<option value="all">Todos los sprints</option>'+sprints.map(item=>'<option value="'+esc(item.id)+'">'+esc(item.id+" · "+item.title)+'</option>').join("");
      filter.value=sprints.some(item=>item.id===selected)||selected==="all"?selected:"all";
      const query=norm(el("board-search").value), groups=boardGroups();
      el("kanban-board").innerHTML=groups.map(group=>{
        const rows=tasks.filter(task=>group.statuses.includes(taskStatus(task.id))&&(filter.value==="all"||task.sprint===filter.value)&&(!query||norm(task.id+" "+task.title+" "+(task.description||"")).includes(query)));
        const cards=rows.map(task=>{
          const record=state.updates[task.id]||{}, evidence=taskEvidence(task), evidenceButton=resourceControl(evidence,"Ver evidencia");
          const blocked=taskStatus(task.id)==="bloqueada"?'<span class="priority-tag blocked-tag">Bloqueada</span>':"";
          return '<article class="kanban-card" draggable="true" data-drag-task="'+esc(task.id)+'"><div class="kanban-card-top"><span class="task-code">'+esc(task.id)+'</span><span class="priority-tag">'+esc(task.priority||"Media")+'</span></div><h3>'+esc(task.title)+'</h3><p>'+esc(task.description||"Sin descripción disponible.")+'</p><div class="kanban-tags"><span class="sprint-tag">'+esc(task.sprint||"Sin sprint")+'</span>'+blocked+'<span class="points-tag">'+(record.points==null?"Sin estimar":esc(String(record.points))+" pts")+'</span></div><div class="kanban-card-foot"><span>'+esc(task.start&&task.end?fmt(task.start)+"–"+fmt(task.end):"Fechas pendientes")+'</span><div class="kanban-card-actions">'+(evidenceButton||"")+'<button type="button" class="secondary compact-button" data-edit-task="'+esc(task.id)+'">Editar</button></div></div></article>';
        }).join("");
        return '<section class="kanban-column" data-drop-status="'+group.id+'" aria-label="'+group.label+'"><header><span><i style="--column:'+group.color+'"></i>'+group.label+'</span><b>'+rows.length+'</b></header><div class="kanban-cards">'+(cards||'<div class="kanban-empty">Suelta una tarea aquí</div>')+'</div></section>';
      }).join("");
    }
    function renderBacklog(){
      const query=norm(el("backlog-search").value),kind=el("backlog-kind-filter").value,status=el("backlog-status-filter").value;
      const rows=[...data.items.filter(item=>item.kind!=="task"),...tasks].filter(item=>{
        if(kind!=="all"&&item.kind!==kind)return false;
        if(query&&!norm(item.id+" "+item.title+" "+(item.description||"")).includes(query))return false;
        if(status!=="all"&&(item.kind!=="task"||taskStatus(item.id)!==status))return false;
        return true;
      }).sort((a,b)=>a.id.localeCompare(b.id,"es"));
      el("backlog-body").innerHTML=rows.map(item=>{
        const isTask=item.kind==="task",record=isTask?state.updates[item.id]||{}:{},taskState=isTask?names[taskStatus(item.id)]:"—";
        const kindLabel=kindNames[item.kind]||item.kind,assigned=item.sprint||"—",points=record.points==null?"—":record.points;
        return '<tr data-backlog-id="'+esc(item.id)+'" data-backlog-kind="'+esc(item.kind)+'"><td><span class="code-cell">'+esc(item.id)+'</span></td><td><strong>'+esc(item.title)+'</strong><small>'+esc(item.description||"")+'</small></td><td><span class="type-pill '+esc(item.kind)+'">'+esc(kindLabel)+'</span></td><td>'+esc(item.priority||"—")+'</td><td>'+esc(taskState)+'</td><td>'+esc(assigned)+'</td><td>'+esc(String(points))+'</td><td>'+esc(item.start&&item.end?fmt(item.start)+"–"+fmt(item.end):"—")+'</td><td>'+(isTask?'<button type="button" class="secondary compact-button" data-edit-task="'+esc(item.id)+'">Editar</button>':'—')+'</td></tr>';
       }).join("")||'<tr><td class="empty" colspan="9">No hay elementos con esos filtros.</td></tr>';
      el("backlog-count").textContent=rows.length+" elementos visibles · "+tasks.length+" tareas con seguimiento.";
    }
    function renderAudit(){
      const entries=[...state.audit].sort((a,b)=>new Date(b.at)-new Date(a.at));
      el("audit-count").textContent=entries.length+(entries.length===1?" evento":" eventos");
      el("audit-list").innerHTML=entries.length?entries.map(item=>{
        const when=new Date(item.at),time=Number.isNaN(when.getTime())?"Fecha desconocida":new Intl.DateTimeFormat("es-EC",{dateStyle:"medium",timeStyle:"short"}).format(when);
        return '<article class="audit-row"><span class="audit-marker '+esc(item.kind||"edit")+'"></span><div><strong>'+esc(item.title||"Actividad")+'</strong><p>'+esc(item.detail||"")+'</p></div><time datetime="'+esc(item.at||"")+'">'+esc(time)+'</time></article>';
      }).join(""):'<p class="empty">La bitácora registrará cambios al editar tareas, evidencias o estados de sprint.</p>';
    }
    function taskIdForNew(){
      const used=new Set(tasks.map(task=>task.id));
      let id;
      do{id="LOC-"+Math.floor(Math.random()*0x100000000).toString(16).toUpperCase().padStart(8,"0")}while(used.has(id));
      return id;
    }
    function fillTaskSprintOptions(selected){
      const options=resourceCatalog.sprints.map(item=>'<option value="'+esc(item.id)+'">'+esc(item.id+" · "+item.title)+'</option>').join("");
      el("task-sprint").innerHTML='<option value="">Sin asignar</option>'+options;
      el("task-sprint").value=selected||"";
    }
    function openTaskDialog(id){
      const task=id?tasks.find(item=>item.id===id):null,record=task?state.updates[task.id]||{}:{};
      const localId=task?.id||taskIdForNew();
      el("task-form").reset();
      el("task-dialog-id").value=localId;
      el("task-display-id").value=localId;
      el("task-dialog-title").textContent=task?"Editar tarea":"Nueva tarea local";
      el("task-title").value=task?.title||"";
      el("task-description").value=task?.description||"";
      el("task-priority").value=task?.priority||"Media";
      el("task-points").value=record.points??"";
      const currentSprint=data.sprints.find(item=>item.start<=localToday()&&item.end>=localToday());
      fillTaskSprintOptions(task?.sprint||state.activeSprint||currentSprint?.id||"");
      el("task-status").value=task?taskStatus(task.id):"sin_verificar";
      el("task-start").value=task?.start||"";
      el("task-end").value=task?.end||"";
      el("task-evidence").value=taskEvidence(task||{id:localId});
      el("task-reviewer").value=record.reviewer||"";
      el("task-date").value=record.date||"";
      el("task-notes").value=record.notes||"";
      el("task-delete-button").hidden=!task?.custom;
      el("task-dialog-error").textContent="";
      el("task-start").min=data.window.start;el("task-start").max=data.window.end;
      el("task-end").min=data.window.start;el("task-end").max=data.window.end;
      el("task-dialog").showModal();
      setTimeout(()=>el("task-title").focus(),30);
    }
    function closeTaskDialog(){el("task-dialog").close()}
    async function saveTaskDialog(event){
      event.preventDefault();
      const id=el("task-dialog-id").value,title=el("task-title").value.trim(),start=el("task-start").value,end=el("task-end").value;
      const status=el("task-status").value,evidence=el("task-evidence").value.trim(),reviewer=el("task-reviewer").value.trim(),dateValue=el("task-date").value;
      const points=el("task-points").value===""?null:Number(el("task-points").value),error=el("task-dialog-error");
      let message="";
      if(!title)message="El título es obligatorio.";
      else if(points!==null&&(!Number.isInteger(points)||points<0||points>100))message="Los puntos deben ser un entero entre 0 y 100.";
      else if(start&&end&&end<start)message="La fecha de fin debe ser igual o posterior al inicio.";
      else if((start&&start<data.window.start)||(end&&end>data.window.end))message="Las fechas deben estar dentro del cronograma del proyecto.";
      else if(evidence&&!safeEvidenceHref(evidence))message="Usa una URL http/https o una ruta local /fuentes/ o /evidencias/.";
      else if(["realizada","verificada"].includes(status)&&!evidence)message="Agrega una evidencia antes de marcar la tarea como realizada.";
      else if(status==="verificada"&&(!reviewer||!dateValue))message="Para completar, registra a la persona verificadora y la fecha.";
      else if(dateValue&&dateValue>localToday())message="La fecha de comprobación no puede ser futura.";
      error.textContent=message;if(message)return;
      const task={id,title,description:el("task-description").value.trim(),priority:el("task-priority").value,sprint:el("task-sprint").value,start,end,status,evidence,reviewer,date:dateValue,notes:el("task-notes").value.trim(),points};
      const action=tasks.some(item=>item.id===id)?"update":"create";
      const button=el("task-form").querySelector('button[type="submit"]');button.disabled=true;
      try{
        const saved=await requestJson("/api/tareas",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({action,task})});
        state.updates=saved.updates||{};state.customTasks=saved.customTasks||[];state.taskEdits=saved.taskEdits||{};state.audit=saved.audit||[];refreshTaskList();renderAll();closeTaskDialog();notify(action==="create"?"Tarea local creada.":"Tarea actualizada en el seguimiento local.");
      }catch(errorSave){error.textContent=errorSave.message;button.disabled=false}
    }
    async function deleteLocalTask(){
      const id=el("task-dialog-id").value,task=tasks.find(item=>item.id===id);
      if(!task?.custom)return;
      if(!window.confirm('¿Eliminar la tarea local "'+id+" · "+task.title+'"? Esta acción no se puede deshacer.'))return;
      try{
        const saved=await requestJson("/api/tareas",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({action:"delete",id})});
        state.updates=saved.updates||{};state.customTasks=saved.customTasks||[];state.audit=saved.audit||[];refreshTaskList();renderAll();closeTaskDialog();notify("Tarea local eliminada.");
      }catch(error){el("task-dialog-error").textContent=error.message}
    }
    async function moveKanbanTask(id,column){
      const task=tasks.find(item=>item.id===id);if(!task)return;
      const next={todo:"sin_verificar",progress:"en_curso",review:"realizada",done:"verificada"}[column];
      if(!next||next===taskStatus(id))return;
      const current=state.updates[id]||{},evidence=taskEvidence(task);
      if(["realizada","verificada"].includes(next)&&!evidence){showDrawer(id);notify("Agrega evidencia antes de pasar la tarea a revisión.");return}
      if(next==="verificada"&&(!current.reviewer||!current.date)){showDrawer(id);notify("Completa persona verificadora y fecha para cerrar la tarea.");return}
      try{
        const saved=await requestJson("/api/seguimiento",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({id,record:{...current,status:next,evidence}})});
        state.updates=saved.updates||{};state.audit=saved.audit||[];renderAll();notify(id+" pasó a "+names[next]+".");
      }catch(error){notify("No se pudo mover la tarea: "+error.message)}
    }
    async function toggleSprintState(id,closed){
      try{
        const saved=await requestJson("/api/sprints",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({sprint:id,closed:!closed})});
        state.sprintStates=saved.sprintStates||{};state.audit=saved.audit||[];renderOverview();renderAudit();showResourceDrawer(id);notify("Sprint "+id+(closed?" reabierto.":" cerrado."));
      }catch(error){notify("No se pudo actualizar el sprint: "+error.message)}
    }
    const baseRenderAll=renderAll;
    renderAll=function(){baseRenderAll();renderKanban();renderBacklog();renderAudit()};
    const baseSwitchTab=switchTab;
    switchTab=function(name){baseSwitchTab(name);if(name==="kanban")renderKanban();if(name==="backlog")renderBacklog();if(name==="log")renderAudit()};
    for(const id of ["new-task-button","new-backlog-task"])el(id).addEventListener("click",()=>openTaskDialog());
    el("board-sprint-filter").addEventListener("change",renderKanban);
    el("board-search").addEventListener("input",renderKanban);
    el("backlog-search").addEventListener("input",renderBacklog);
    el("backlog-kind-filter").addEventListener("change",renderBacklog);
    el("backlog-status-filter").addEventListener("change",renderBacklog);
    el("task-form").addEventListener("submit",saveTaskDialog);
    el("task-delete-button").addEventListener("click",deleteLocalTask);
    el("task-dialog-close").addEventListener("click",closeTaskDialog);
    el("task-cancel-button").addEventListener("click",closeTaskDialog);
    document.addEventListener("click",event=>{
      const edit=event.target.closest("[data-edit-task]");
      if(edit){openTaskDialog(edit.dataset.editTask);return}
      const row=event.target.closest("[data-backlog-id]");
      if(row){const task=tasks.find(item=>item.id===row.dataset.backlogId);if(task?.custom)openTaskDialog(task.id);else showDrawer(row.dataset.backlogId);return}
      const sprint=event.target.closest("[data-toggle-sprint]");
      if(sprint){toggleSprintState(sprint.dataset.toggleSprint,sprint.dataset.closed==="true");return}
    });
    el("kanban-board").addEventListener("dragstart",event=>{
      const card=event.target.closest("[data-drag-task]");if(!card)return;
      event.dataTransfer.effectAllowed="move";event.dataTransfer.setData("text/plain",card.dataset.dragTask);
    });
    el("kanban-board").addEventListener("dragover",event=>{const column=event.target.closest("[data-drop-status]");if(column){event.preventDefault();event.dataTransfer.dropEffect="move";column.classList.add("drag-over")}});
    el("kanban-board").addEventListener("dragleave",event=>{const column=event.target.closest("[data-drop-status]");if(column&&!column.contains(event.relatedTarget))column.classList.remove("drag-over")});
    el("kanban-board").addEventListener("drop",event=>{const column=event.target.closest("[data-drop-status]");if(!column)return;event.preventDefault();column.classList.remove("drag-over");moveKanbanTask(event.dataTransfer.getData("text/plain"),column.dataset.dropStatus)});
    el("kanban-board").addEventListener("dragend",()=>document.querySelectorAll(".kanban-column.drag-over").forEach(node=>node.classList.remove("drag-over")));
    el("task-dialog").addEventListener("click",event=>{if(event.target===el("task-dialog"))closeTaskDialog()});
    renderKanban();renderBacklog();renderAudit();
  })();
