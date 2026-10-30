"""Consolidación documental solicitada; conserva estados y evidencia previa del gestor."""
from pathlib import Path
import json, re, urllib.request, uuid, datetime, copy

ROOT = Path(__file__).resolve().parents[4]
OUT = Path(__file__).parent
MAIN = 'arquitectura/diseno_base_datos_v2.0_2026-10-30.md'
RF = {
'RF-VEN-001': ('C01-C03, C14-C15', 'Venta pagada antes de entrega; distinguir contexto feria/individual y origen individual/compartido. Dueña, vendedora y registradora diferentes; Superadministradora no vende.'),
'RF-VEN-002': ('C01, C15', 'Sin crédito al comprador. Resumen de feria sin datos de cliente obligatorios y nota opcional; precio, base y política históricos por línea.'),
'RF-VEN-007': ('C01', 'Venta institucional identificada, pago completo antes de entregar y sin excedente individual; la prohibición de venta personal incluye a Superadministración.'),
'RF-CXC-001': ('C01, C04-C05', 'Custodia sin deuda. Base acumulada visible y obligación interna al cierre del periodo, con fuente por venta o resolución de faltante. No crédito externo.'),
'RF-CXC-002': ('C04-C05', 'Entregas de dinero durante jornada o al final, aplicadas una sola vez al periodo y liquidación. Abonos internos sin duplicar cobro ni saldo.'),
'RF-CXC-003': ('C07-C12', 'Conciliación de cancelaciones, devoluciones, sobrepagos y faltantes; autorización separada de ejecución. Defecto de fabricación a cargo de asociación sin recuperar excedente de socia.'),
'RF-ACC-005': ('C13', 'Superadministradora ejecuta, aprueba y sustituye cargos sin permiso previo; no vende personalmente. Actor y autoridad auditados. Concesión/revocación conserva D19.'),
'RF-TRA-002': ('C16', 'Secado de un solo acopio, consumos efectivos, lote húmedo/seco y linaje conservado.'),
'RF-TRA-003': ('C16-C17', 'Transformación por receta autorizada o kit por variante, referencia 50 L y salida real separada. Fórmula secreta de shampoo no se almacena.'),
'RF-TRA-004': ('C16-C17', 'Lotes y consumos conservan origen; unidades compatibles, etiqueta oficial del kit sin fórmula secreta.'),
'RF-TRA-005': ('C16', 'Salida de venta por lote y presentación permite reconstruir acopio o kit, sin ciclos ni origen inventado.'),
'RF-INV-003': ('C01-C03', 'Entrega en custodia conserva lote, presentación, titular, feria y condición. No crea deuda ni venta.'),
'RF-INV-004': ('C05, C14', 'Conciliar stock físico, capturas y dinero al cierre; provisional compartido offline conserva diferencias hasta resolución, sin stock confirmado negativo.'),
'RF-INV-005': ('C08, C12, C14', 'Retorno segregado; faltante solo causa cargo tras responsabilidad decidida; transferencias y correcciones auditadas, sin borrar hechos.'),
'RF-ASI-003': ('C13', 'Cargo competente o sustitución por Superadministradora decide con actor real, motivo y evidencia; no suplantar autoridad ajena.'),
'RF-ASI-006': ('C13', 'Justificaciones e impugnaciones conservan su revisión y evidencia; Superadministradora puede sustituir la decisión y deja auditoría.'),
'RF-ASI-007': ('C13', 'Secretaria o Superadministradora opera fases QR; vigencia y correcciones auditadas, tokens protegidos.'),
'RF-VEN-006': ('C03, C06, C18', 'Repartir solo fondo compartido: proporcional a ventas compartidas por vendedora o montos negociados. Excedente individual de dueña excluido; suma exacta al cierre.'),
'RF-VEN-009': ('C06, C18', 'Cuotas por socia y versión, acuerdo y pago separados; cambios exigen nuevas aceptaciones. Redondeo por restos y desempate por ID de asignación. Sin pago duplicado.')}
HU_MAP = {
'HU-VEN-001':'RF-VEN-001','HU-VEN-002':'RF-VEN-002','HU-VEN-007':'RF-VEN-007',
'HU-VEN-006':'RF-VEN-006','HU-VEN-008':'RF-VEN-002',
'HU-CXC-001':'RF-CXC-001','HU-CXC-002':'RF-CXC-002',
'HU-TRA-002':'RF-TRA-002','HU-TRA-003':'RF-TRA-003','HU-TRA-004':'RF-TRA-004','HU-TRA-005':'RF-TRA-005',
'HU-ACC-005':'RF-ACC-005','HU-ACC-006':'RF-ACC-005','HU-ACC-007':'RF-ACC-005','HU-ACC-008':'RF-ACC-005','HU-ACC-009':'RF-ACC-005',
'HU-ASI-003':'RF-ASI-003','HU-ASI-006':'RF-ASI-006','HU-ASI-007':'RF-ASI-007'}
HU = {h: RF[r] for h,r in HU_MAP.items()}
HU['HU-ACC-005'] = ('C13','Administrar permisos existentes sin concesión por módulo; autoridad organizacional separada de is_superuser. No habilitar venta personal.')
HU['HU-ACC-006'] = ('C13','Concesión/revocación con autorización presidencial D19 y evidencia; varias administradoras posibles, sin autoconcesión.')
HU['HU-ACC-007'] = ('C13','Conservar historial de concesión/revocación y actor real; la autonomía operativa no cambia la designación del rol.')
HT = {'HT-PRE-003': ('C01-C18 / DB-01 a DB-20', 'Preparar esquema por módulo con identidades, flujos de stock y dinero, cierre periódico, devoluciones, reparto, políticas e idempotencia; pruebas PostgreSQL y migraciones pendientes.')}
TASKS = {
'SB-S1-03': 'Diseño consolidado v2.0 y 20 casos definidos. Trabajo documental listo para diseño físico; no certifica implementación ni cierre de tarea.',
'SB-S5-01': 'Catálogo, valores versionados, recetas conocidas y kits 50 L sin fórmula secreta; parámetros incompletos inactivos.',
'SB-S5-02': 'Acopio, secado único y lotes; cantidades efectivas y conversiones compatibles.',
'SB-S5-03': 'Transformación, kits y movimientos; linaje hasta salida, stock por titular/feria/condición.',
'SB-S5-04': 'Custodia sin deuda; rendición periódica y anticipos; conciliación de capturas provisionales y stock.',
'SB-S5-05': 'Ventas pagadas, resúmenes de feria, delegación y propiedad del excedente; permisos y prohibición de venta Superadministradora.',
'SB-S5-06': 'Dinero, gastos, reembolsos, faltantes y reparto compartido exacto; ejecución separada de autorización y acuerdo.'}

def write(path, text):
 p=ROOT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text,encoding='utf-8')

def table(mapping):
 return '| ID | Reglas | Criterio vigente de esta revisión |\n|---|---|---|\n' + ''.join(f'| {k} | {v[0]} | {v[1]} |\n' for k,v in mapping.items())

def edition(path,title,version,body,relative_main):
 write('documentacion/'+path,f'''---
titulo: {title}
version: "{version}"
fecha: 2026-10-30
autor: Codex por instrucción del tesista
estado: consolidado-para-revision
validacion_organizacional: evidencia-directa-pendiente
publicacion: pendiente
---

# {title}

Esta edición consolida el alcance afectado por el diseño de datos; reemplaza los criterios incompatibles de la edición previa, conserva IDs, estimaciones, prioridades, fechas y estados. Los requisitos no afectados mantienen sus fuentes y evidencia. No acredita validación organizacional nueva ni implementación.

Referencia única de reglas, entidades y pruebas: [diseño de datos v2.0]({relative_main}). Los códigos C01–C18 son reglas de esta revisión, no requisitos nuevos; DB-01–DB-20 son casos definidos, no pruebas ejecutadas.

{body}

## Control de edición

{version}, 2026-10-30: consolidación solicitada por el tesista; reemplaza criterios del corte del 29/10 y las precisiones intermedias del 30/10. S1 permanece cerrado por calendario y S2 activo; ningún avance técnico se certifica por escribir esta edición. Publicación y Git documental pendientes.
''')

def main():
 if (OUT/'gestor-despues.json').exists():
  raise SystemExit('Consolidación ya ejecutada: no sobrescribir snapshots ni repetir cambios del gestor.')
 rfpath='requisitos/requisitos_generales_v2.5_2026-10-30.md'
 hupath='historias/usuario/historias_usuario_v3.0_2026-10-30.md'
 htpath='historias/tecnicas/historias_tecnicas_v2.1_2026-10-30.md'
 pilepath='pila_producto/pila_producto_v2.2_2026-10-30.md'
 sprintpath='sprints/sprint_backlog_v1.8_2026-10-30.md'
 edition(rfpath,'Requisitos afectados: consolidación de datos','2.5',table(RF)+'\nCatálogo completo no afectado: [base v2.3](requisitos_generales_v2.3_2026-10-28.md). RF-ACC-005 conserva estado propuesto. No se cancela CXC: mantiene rendición interna.\n','../'+MAIN)
 edition(hupath,'Historias de usuaria: criterios consolidados de datos','3.0',table(HU)+'\nFichas, puntos y dependencias no afectados: [base v2.8](historias_usuario_v2.8_2026-10-28.md). Reembolsos/conciliación conservan RF-CXC-003; no se inventa HU inexistente para aparentar cobertura.\n','../../'+MAIN)
 edition(htpath,'Historia técnica del modelo de datos','2.1',table(HT)+'\nHT-PRE-003 conserva sprint S1; revisión durante S2. Criterios: entidades con propietario; claves y cardinalidades; invariantes BD/servicio; casos concurrentes; permisos positivos/negativos; trazabilidad de saldos y pruebas físicas antes de cierre. [Base de historias técnicas](historias_tecnicas_v1.9_2026-10-28.md).\n','../../'+MAIN)
 tasktable='| Tarea | Contenido consolidado |\n|---|---|\n'+''.join(f'| {k} | {v} |\n' for k,v in TASKS.items())
 edition(pilepath,'Pila de producto: alcance de datos consolidado','2.2',table(HT)+table(HU)+'\nSe conserva orden, puntos y prioridad de la [base v2.0](pila_producto_v2.0_2026-10-28.md). Dependencias técnicas: catálogo/unidades → producción/stock → venta pagada → rendición → cierre/reparto y ajustes. No mueve S5 a S2.\n','../'+MAIN)
 edition(sprintpath,'Sprint backlog: alcance de datos consolidado','1.8',tasktable+'\n[Base de compromisos v1.6](sprint_backlog_v1.6_2026-10-28.md). No se modifican SB-S2-02 ni tareas de acceso multicanal. Gestor: SB-S1-03 figura done en dashboard y en_curso en seguimiento; discrepancia histórica conservada, no cierre inferido.\n','../'+MAIN)
 proposal='''---
title: Consolidación de reglas para diseño de datos
status: proposed
date: 2026-10-30
author: Codex por instrucción expresa del tesista
organization_validation: pending-direct-evidence
task_id: SB-S1-03
commit: pending
---

# Consolidación de requisitos y decisiones

Fuente: decisiones expresas del tesista del 30/10, incluyendo 1A, 2B, 3B, 4A, 5A, 6A, 7A, 8B, y solicitud de consolidar. [Diseño único v2.0](../../../documentacion/arquitectura/diseno_base_datos_v2.0_2026-10-30.md) contiene reglas C01–C18, entidades y 20 casos de verificación. Reemplaza la enmienda del 29/10 para estos temas; no altera evidencia de aprobación del CAT.

## Discrepancias resueltas para el diseño

- D28 administración sin negocio: sustituido por ejecución/aprobación y sustitución de cargos; sigue prohibida venta personal. D19 designación presidencial se conserva.
- D29 ajustes desconocidos: cancelación sin entrega, defecto, sobrepago y faltante ahora definidos. Daño de otra causa requiere decisión económica específica.
- Deuda por cada venta: saldo acumulado visible, liquidación formal periódica y anticipos aplicables una sola vez.
- Reparto igualitario: sustituido por proporcional a ventas compartidas o manual negociado; cerrar exige asignación exacta.
- Stock compartido solo online: sustituido por contingencia provisional conciliada.
- Receta secreta aplazada: retirada del almacenamiento; kit por variante y resultado real.
- Factura/comprador por venta de feria: resumen por vendedora/producto/origen, nota opcional, evidencia de verificación para retornos.

## Requisitos

'''+table(RF)+'\n## Historias\n\n'+table(HU)+'\n## Trabajo técnico y sprint\n\n'+table(HT)+tasktable+'''
## Verificación y estados

Las reglas sustituyen los criterios de diseño anteriores, no el estado de validación organizacional. Las discrepancias del CAT confirmado quedan expresamente identificadas arriba para reconciliación puntual antes de implementar. No se reabren decisiones ya contestadas ni se inventan IDs o aprobaciones. Pruebas de producto pendientes. Configuraciones concretas y responsabilidad por daños no fabriles se delimitan en §12 del diseño, sin impedir modelar los flujos definidos.

Ediciones sincronizadas: requisitos 2.5, HU 3.0, HT 2.1, pila 2.2, backlog 1.8; índice/control 5.8. Evidencia de persistencia del gestor y controles documentales en [verificación](../../evidence/architecture/2026-10-30-consolidacion/verificacion.json).
'''
 write('docs/requirements/proposals/2026-10-30-consolidacion-reglas-diseno-datos.md',proposal)
 # Reconciliar el aviso obsoleto sin reescribir aprobación o contenido histórico.
 for path in ['specs/002-superadministracion/spec.md','docs/context/feature-index.md']:
  p=ROOT/path; s=p.read_text(encoding='utf-8')
  if path.startswith('specs'):
   start=s.index('## Corrección de alcance pendiente de reconciliación')
   end=s.find('\n## ',start+3)
   if end<0: raise ValueError('No se encontró siguiente sección SPEC-002')
   s=s[:start]+'''## Criterio de diseño consolidado — 2026-10-30

Las respuestas expresas posteriores sustituyen D28: Superadministradora puede ejecutar, aprobar y sustituir decisiones de negocio sin autorización previa, pero no vender personalmente. Toda actuación conserva actor real, autoridad usada y evidencia. La concesión/revocación del rol mantiene autorización presidencial D19, sin autoconcesión. Esta spec conserva estado propuesto y no acredita validación organizacional ni implementación. Los criterios detallados de esta revisión están en la [consolidación](../../docs/requirements/proposals/2026-10-30-consolidacion-reglas-diseno-datos.md); cualquier escenario histórico inferior se interpreta dentro de esos límites.
''' + s[end:]
  else:
   s=re.sub(r'\*\*Precisión posterior 2026-10-29:\*\*[^\n]*', '**Consolidación 2026-10-30:** Superadministradora ejecuta y aprueba negocio y puede sustituir cargos con auditoría; no vende personalmente. D19 conserva designación presidencial. Regla anterior D28 sustituida; RF-ACC-005 sigue propuesto. Referencia: [[../requirements/proposals/2026-10-30-consolidacion-reglas-diseno-datos|consolidación de datos]] y [[../../documentacion/arquitectura/diseno_base_datos_v2.0_2026-10-30|diseño v2.0]].',s)
  p.write_text(s,encoding='utf-8')
 p=ROOT/'documentacion/README.md'; s=p.read_text(encoding='utf-8').replace('version: "5.7"','version: "5.8"',1)
 start=s.index('## Diseño de base de datos'); end=s.index('## Adendas locales',start)
 s=s[:start]+'''## Diseño de base de datos — referencia consolidada del 2026-10-30

El [diseño de datos v2.0](arquitectura/diseno_base_datos_v2.0_2026-10-30.md) es la referencia de trabajo vigente: reglas, entidades, relaciones, integridad y 20 casos para implementar. Sustituye v1.0 y adendas v1.1/v1.2; estas quedan como antecedentes, sin necesidad de combinarlas para determinar la regla actual. No acredita migraciones ni validación organizacional nueva.

Ediciones afectadas: [requisitos 2.5](requisitos/requisitos_generales_v2.5_2026-10-30.md), [HU 3.0](historias/usuario/historias_usuario_v3.0_2026-10-30.md), [HT 2.1](historias/tecnicas/historias_tecnicas_v2.1_2026-10-30.md), [pila 2.2](pila_producto/pila_producto_v2.2_2026-10-30.md), [backlog 1.8](sprints/sprint_backlog_v1.8_2026-10-30.md) y [control 5.8](control_de_cambios/registro_v5.8_2026-10-30.md). Las secciones inferiores conservan el historial de ediciones previas; sus reglas sustituidas no son la referencia actual.

''' + s[end:]; p.write_text(s,encoding='utf-8')
 write('documentacion/control_de_cambios/registro_v5.8_2026-10-30.md','''---
version: "5.8"
fecha: 2026-10-30
autor: Codex por solicitud del tesista
estado: preparado-para-revision
publicacion: pendiente
---

# Control de cambios 5.8

Consolidación de [diseño 2.0](../arquitectura/diseno_base_datos_v2.0_2026-10-30.md), requisitos 2.5, HU 3.0, HT 2.1, pila 2.2 y backlog 1.8. Actualiza referencia de SPEC-002 y contexto; conserva ediciones y validación anteriores. Sin código, migraciones, commit ni publicación. Evidencia local de controles y sincronización: [verificación](../../docs/evidence/architecture/2026-10-30-consolidacion/verificacion.json).
''')
 # Sincronización mediante API local, conservando snapshots completos y estados.
 base='http://127.0.0.1:55478/api/'
 def get(ep): return json.load(urllib.request.urlopen(base+ep,timeout=15))
 def post(ep,payload):
  req=urllib.request.Request(base+ep,json.dumps(payload,ensure_ascii=False).encode(),{'Content-Type':'application/json','Origin':'http://127.0.0.1:55478'},method='POST')
  return json.load(urllib.request.urlopen(req,timeout=20))
 original=get('dashboard-state'); follow=get('seguimiento')
 (OUT/'gestor-antes.json').write_text(json.dumps({'dashboard':original,'seguimiento':follow},ensure_ascii=False,indent=2),encoding='utf-8')
 s=copy.deepcopy(original['state'])
 for key,mapping,source in [('requirementOverrides',RF,rfpath),('storyOverrides',HU,hupath),('storyOverrides',HT,htpath)]:
  for ident,(rules,desc) in mapping.items():
   item=s[key][ident]
   item['beforeConsolidation20261030']=copy.deepcopy(item)
   item.update(description=desc,criteria=[desc, f'Ver reglas {rules} y casos DB del diseño v2.0; implementación no certificada.'],source='/fuentes/'+source,sourceState='Consolidación solicitada por tesista 2026-10-30; evidencia organizacional y pruebas de implementación pendientes.')
   if key=='requirementOverrides': item['title']=desc
   if 'conformance' in item: item['conformance']=desc
 for ident,note in TASKS.items():
  item=s['taskOverrides'].setdefault(ident,{})
  item['notesBeforeConsolidation20261030']=item.get('notes','')
  item['notes']=note+' Referencia vigente: /fuentes/'+MAIN+' Estados, fechas y evidencia de cumplimiento anteriores conservados.'
 s['audit'].append({'id':str(uuid.uuid4()),'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'kind':'evidence','title':'Consolidación de diseño de datos v2.0','detail':'Reglas C01-C18 y criterios DB-01 a DB-20. RF/HU/HT/pila/backlog sincronizados; sin acreditar pruebas de producto ni modificar estados. /fuentes/'+MAIN})
 post('dashboard-state',{'state':s})
 rec=copy.deepcopy(follow['updates']['SB-S1-03']); rec['notes']=TASKS['SB-S1-03']+' Referencia /fuentes/'+MAIN+'. Historial anterior conservado en evidencia gestor-antes.json. Dashboard done y seguimiento en_curso siguen discrepando; no se infiere terminación.'
 rec['evidence']=rec.get('evidence','')+' ; /fuentes/'+MAIN
 post('seguimiento',{'id':'SB-S1-03','record':rec})
 for label,url in [('Diseño de datos consolidado v2.0',MAIN),('Requisitos de datos v2.5',rfpath),('Historias de datos v3.0',hupath),('Historia técnica de datos v2.1',htpath),('Pila de datos v2.2',pilepath),('Backlog de datos v1.8',sprintpath)]:
  post('recursos',{'action':'add','sprint':'S1','label':label,'url':'/fuentes/'+url})
 after=get('dashboard-state'); af=get('seguimiento')
 assert after['state']==s, 'Persistencia dashboard distinta'
 for key in ['criteriaDone','sprintStates','selectedSprint','storyOrder']:
  assert s[key]==original['state'][key],key
 for key in ['taskOverrides','storyOverrides','requirementOverrides']:
  for ident,item in original['state'][key].items():
   for field in ['status','start','end','sprint','storyPoints','points','priority','reviewer','date']:
    assert item.get(field)==s[key][ident].get(field),(ident,field)
 assert af['updates']['SB-S1-03']['status']==follow['updates']['SB-S1-03']['status']
 for source in [MAIN,rfpath,hupath,htpath,pilepath,sprintpath]:
  with urllib.request.urlopen('http://127.0.0.1:55478/fuentes/'+source,timeout=10) as r: assert r.status==200
 (OUT/'gestor-despues.json').write_text(json.dumps({'dashboard':after,'seguimiento':af},ensure_ascii=False,indent=2),encoding='utf-8')
 print(json.dumps({'rf':len(RF),'hu':len(HU),'ht':len(HT),'tareas':len(TASKS),'api_persistida':True,'estados_conservados':True,'documentos_servidos':6}))

if __name__=='__main__': main()
