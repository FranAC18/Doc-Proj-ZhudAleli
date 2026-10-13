---
title: Revisión de casos de uso, factibilidad y esquemas enlazados
type: checkpoint
status: partially-complete
date: 2026-09-28
task_id: CU-REVIEW-001
phase: pre_commit
commit: pending
branch: opencode/spec-001-fase-1-diseno
head: a6e842f63917b2ac28a64c80b00d68069ba2fabd
module: transversal
sprint: transversal
write_owner: agente-raiz
related:
  - "[[../../evidence/casos-de-uso/2026-09-28-cronograma-presupuesto-stack]]"
  - "[[../ESTADO-ACTIVO]]"
  - "[[../../requirements/proposals/2026-09-28-casos-de-uso]]"
  - "[[../../requirements/proposals/2026-09-28-diagramas-casos-de-uso]]"
  - "[[../../evidence/casos-de-uso/2026-09-28-analisis-coherencia]]"
  - "[[../../evidence/casos-de-uso/2026-09-28-factibilidad-aportada]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - modulo/transversal
---

# Revisión de casos de uso, factibilidad y esquemas enlazados

## Solicitud y alcance

Documentar el PDF de casos de uso, contrastarlo con la documentación aplicable, guardar los
esquemas y enlazar fuentes, hallazgos y propuestas para corregirlos progresivamente.
Clasificación: `review` + `documentation`, con lectura de fuentes de `research`.
Skills aplicadas: zhud-aleli-context, zhud-aleli-documenter, speckit-analyze y pdf.

Raíz/vault verificados: `F:/Tesis/App Tesis`, con AGENTS.md, constitución y `.obsidian`.
Rama/HEAD reales coinciden con ESTADO-ACTIVO. La tarea previa HARNESS-ARCH-001 y sus cambios
permanecen conservados. Los archivos PROJECT_CONTEXT/KNOWLEDGE_POLICY/OBSIDIAN_POLICY que
la skill nombra sin ruta se localizaron en `agents/tesis/` siguiendo los enlaces del dashboard.

Rutas de esta revisión autorizadas por la solicitud y el contrato documenter:
`docs/requirements/proposals/`, `docs/evidence/`, `docs/bitacora/checkpoints/`.
El coordinador agrega únicamente un enlace de continuidad en ESTADO-ACTIVO; no reemplaza
el trabajo arquitectónico previo. No se modifica código, spec/plan/tasks, catálogo aprobado,
roadmap, matriz global ni PDF externo. No hay commit/push.

## Resultado documental

- Fichas de los 21 casos originales con página, actor, pre/postcondiciones, flujo, alternos,
  fuente, ajuste y criterio; 15 IDs complementarios propuestos.
- Siete vistas de diagramas en un único índice Markdown, siete SVG visibles sin plugin y
  un archivo PlantUML editable, todos con el mismo inventario de 36 IDs.
- Informe con 22 hallazgos sobre PDF/factibilidad y 4 sobre spec/plan/tasks; cobertura de
  los 57 requisitos confirmed del catálogo y de las 21 claves RF/RNF/SC de SPEC-001.
- Registro estructurado de la factibilidad aportada y de la instrucción expresa del tesista:
  guardar y sincronizar sin conexión es obligatorio en el diseño solicitado.

## Decisiones y pendientes

La incorporación de offline al diseño **no se deja a elección futura**: está exigida por el
tesista. Sigue pendiente reconciliar la línea base anterior, formalizar criterios por operación
y registrar validaciones de alcance que correspondan. No se atribuye aceptación de la
organización/directora a la instrucción recibida.

Prioridades: C1 (versiones de alcance), C2 (hora/QR/permisos offline), C3 (mensajes de acceso),
U3 (sincronización y duplicados); luego asistencia/encargos, secado, ventas/deudas y reportes.
La aportación posterior del nuevo Gantt, presupuesto y stack resuelve I4/I5 como referencia:
USD 2.869 y 16 semanas relativas. Queda propagar esos datos a futuras versiones documentales;
ya no se necesita escoger entre las cifras/plazos anteriores. U4 sigue abierto para precisar
dónde se ejecuta Django en el despliegue propuesto.

La revisión documental está entregada; el estado global es `partially-complete` porque
las correcciones canónicas y validaciones siguen pendientes. No declara terminado un sprint.
La revisión fue realizada por el agente raíz; no se presenta como dictamen de un revisor
independiente ni como aprobación humana de las propuestas.

## Verificaciones

- PDF: 23 páginas extraídas con pypdf; 23 páginas renderizadas con Poppler; inspección visual
  de los cinco diagramas en pp. 5–7 y fichas/tabla de aprobación relevantes. SHA-256 en informe.
- Prerequisitos Spec Kit: exit 0 tras reintento de Bash; funcionalidad y tasks resueltos.
- Integridad de documentación: 5 Markdown nuevos, 96 enlaces locales y 38 enlaces a encabezados
  comprobados; 0 errores. Se comprobó además el enlace nuevo desde ESTADO-ACTIVO.
- Inventario: 21 casos originales y 15 complementarios = 36 IDs únicos; aparecen exactamente
  una vez en las siete vistas SVG y coinciden con los siete bloques PlantUML.
- XML SVG válido, elipses dentro del límite del sistema, renderizado con Sharp e inspección
  visual de las siete vistas; ajustados márgenes y separación de actores. PlantUML no se
  compiló con su motor; se comprobó estructura e inventario, sin declarar compilación.
- Matriz de producto: 57 IDs confirmed únicos, 31 coberturas parciales, 24 ausencias y
  2 contradicciones respecto a la línea base comparada. No se declara cobertura completa.
- Matriz SPEC-001: 21 claves con tarea asociada, 36 tareas sin completar; no son pruebas ejecutadas.
- Suma de presupuesto: USD 2.869; diferencia con la cifra de prosa USD 1.024.
- `python tools/validate-universal.py --json`: exit 0, `ok: true`, 0 errores; cuatro
  advertencias heredadas (MOC contra commit antiguo y tres enlaces no resueltos).
- `git diff --check -- docs/bitacora/ESTADO-ACTIVO.md`: exit 0; los nuevos archivos también
  se comprobaron expresamente porque Git aún los muestra como untracked.
- `git diff --check` global: exit 1 por espacios finales en `design/style-guide/tokens.html`,
  líneas 19 y 75, archivo ajeno a esta revisión. No se corrigió ni se incluyó en la entrega.
- Comparación SHA-256 de los archivos modificados al tomar el inventario: sin cambios por
  esta revisión salvo la inserción de continuidad documentada en ESTADO-ACTIVO.
- Revisión final de contenido y diff documental: fuentes/cambios propuestos distinguidos,
  alcance offline actualizado por la respuesta del tesista, sin promoción canónica ni Git write.

## Próximo paso permitido

Usar las fichas y hallazgos para una revisión por módulo. Preparar la actualización trazable
del catálogo y una especificación PWA que concrete operaciones, reloj, sesión, permisos,
idempotencia, conflictos y recuperación; conservar el historial previo. Antes de implementar
SPEC-001, corregir S1–S4 y repetir el análisis de tareas.

## Continuación — nuevo cronograma, presupuesto y stack

Solicitud adicional del tesista: registrar las tres imágenes y la tabla tecnológica como
nueva referencia. Clasificación `documentation` con comprobación de coherencia; rama y HEAD
permanecen sin cambios. Se conserva el alcance de escritura de esta revisión.

Se añadió EVID-PLAN-002 con 18 actividades, cuatro hitos, 14 partidas presupuestarias y 14
entradas de stack. Las tres imágenes fuente se copiaron sin editar a `docs/evidence/casos-de-uso/assets/`.
Se actualizaron el informe, la evidencia previa, el índice de fichas y el enlace de continuidad.
I4/I5 se conservan como hallazgos históricos resueltos en la selección de la referencia;
la documentación anterior no se presenta como fuente actual de presupuesto/duración.

Se distinguieron los solapamientos de módulos en S6/S7, las pruebas integradas offline de
S13–S14 frente a su construcción incremental y los manuales finales frente a la documentación
continua. No se inventaron fechas calendario, validaciones realizadas ni un despliegue funcional.

Verificación de esta continuación: seis Markdown revisados, 111 enlaces locales (38 a
encabezados), cero errores; inventario de 36 casos y siete vistas conservado. Se comprobaron
18 rangos de actividad dentro de S1–S16, las 14 multiplicaciones del presupuesto y su suma
USD 2.869,00, las 14 entradas tecnológicas y la identidad SHA-256 de las tres imágenes
copiadas respecto de los adjuntos. La revisión de contenido distingue fuente nueva e historia.
`git diff --check -- docs/bitacora/ESTADO-ACTIVO.md` pasó; la comprobación global continúa
señalando únicamente los espacios finales de `design/style-guide/tokens.html:19` y `:75`,
ajenos a esta revisión. Los Markdown nuevos/modificados pasaron comprobación explícita
de espacios y enlaces, incluidos los archivos aún untracked. Sin commit ni cambios funcionales.
