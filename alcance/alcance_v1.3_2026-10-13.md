---
titulo: Alcance general del proyecto Zhud Alelí
codigo: ZA-ALC-GEN-001
modulo: Alcance general del proyecto
fase: Requisitos y diseño — Sprint 1
version: "1.3"
fecha: 2026-10-13
autor: Franklin Acero, con asistencia documental de Codex
estado: preparado-para-revision-del-tesista
fuente_principal: CAT-REQ-001 v1.2 y requisitos generales v2.0
revision_tesista_de_esta_edicion: pendiente
revision_docente_en_clase: reportada-por-el-tesista-para-requisitos; alcance-v1.3-no-revisado
revision_academica_formal: pendiente
revision_directora: pendiente
validacion_organizacional_directa_de_novedades: pendiente
acta_formal_entrevista: pendiente-sin-evidencia
publicacion: pendiente-de-confirmacion
---

<style>
body { font-family: "Heebo Light", Heebo, Arial, sans-serif; color: #292929; }
h1 { color: #4C5B4A; font-family: "Mallong Regular", Georgia, serif; }
h2, h3 { color: #642138; font-family: "Mallong Regular", Georgia, serif; }
table { border-collapse: collapse; width: 100%; }
th { background: #4C5B4A; color: #F0EAC8; }
th, td { border: 1px solid #AC6E40; padding: 6px 8px; vertical-align: top; }
tbody tr:nth-child(even) { background: #F0EAC8; }
blockquote { background: #F0EAC8; border-left: 4px solid #AC6E40; padding: 8px 12px; }
</style>

> **[LOGO: Isotipo floral de 4 pétalos — ZHUD ALELÍ Productos Naturales]**

<table>
<thead><tr><th colspan="2">CONTROL DOCUMENTAL — ZHUD ALELÍ</th></tr></thead>
<tbody>
<tr><td><strong>Código</strong></td><td>ZA-ALC-GEN-001</td></tr>
<tr><td><strong>Nombre del módulo</strong></td><td>Alcance general del proyecto</td></tr>
<tr><td><strong>Fase / entregable</strong></td><td>Requisitos y diseño — Sprint 1</td></tr>
<tr><td><strong>Versión y fecha</strong></td><td>v1.3 — 13 de octubre de 2026</td></tr>
<tr><td><strong>Autor / analista</strong></td><td>Franklin Acero, con asistencia documental de Codex</td></tr>
<tr><td><strong>Estado</strong></td><td>Preparado para revisión del tesista; esta edición aún no está aprobada</td></tr>
</tbody>
</table>

## Historial de revisiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| 1.1 | 2026-10-12 | Se incorporó el resumen de entrevista como necesidades todavía pendientes, sin ampliar la línea base. | Tesista |
| 1.2 | 2026-10-13 | Se aclaró que SPEC-001 corresponde al S2 de desarrollo del calendario vigente. | Tesista |
| 1.3 | 2026-10-13 | Se alinea el alcance con CAT-REQ-001 v1.2, requisitos generales v2.0, su priorización y el plan de sprints v1.2; se separan las revisiones reportadas de las validaciones formales pendientes. | Preparado con asistencia de Codex; revisión del tesista pendiente |

# Alcance general del proyecto

## 1. Propósito y descripción general

El proyecto comprende el análisis, diseño, construcción incremental y verificación de una
aplicación web para apoyar la gestión organizacional y la trazabilidad productiva del Comité
de Mujeres Indígenas “Tránsito Amaguaña” de Zhud y su unidad productiva Zhud Alelí.

Esta edición define el límite funcional general con base en los requisitos vigentes. No
afirma que la aplicación esté implementada, desplegada, probada ni validada por la
organización. La línea base de referencia contiene **58 requisitos funcionales (RF) y 9
requisitos no funcionales (RNF) confirmados**. Además, mantiene **2 requisitos propuestos**
fuera de la línea base y **12 identificadores históricos**.

La edición general de requisitos v2.0 fue aprobada por el tesista. El tesista informa que
los requisitos también fueron revisados en clase por el docente de Aplicaciones II; se
registra como reporte del tesista, sin atribuir fecha, versión exacta revisada,
resultado formal ni constancia documental que no estén disponibles. La revisión académica
formal —incluida la de la directora— sigue pendiente. La validación organizacional directa
de las novedades de entrevista y el acta formal de entrevista también siguen pendientes.
Este alcance v1.3 es una nueva edición preparada y todavía requiere revisión del tesista.

## 2. Objetivos de negocio y alineación con Zhud Alelí

- Centralizar información de actividades, participación, producción, inventario, ventas y
  rendición con permisos correspondientes a la organización.
- Conservar la procedencia y el historial de los registros relevantes para reconstruir
  movimientos, correcciones, aprobaciones y excepciones.
- Facilitar el uso cotidiano desde dispositivos móviles y reducir errores de digitación,
  conciliación y consulta, sin presentar como medidos beneficios que todavía no se han
  comprobado.
- Separar datos organizacionales privados del contenido que la organización apruebe para
  visitantes.
- Permitir continuidad controlada ante conectividad limitada para las operaciones
  expresamente habilitadas; mantener identificables las operaciones pendientes hasta su
  confirmación por el servidor.
- Acompañar el trabajo de la Directiva, las socias operarias y las visitantes sin otorgar
  autoridad organizacional al soporte técnico por el solo hecho de mantener el sistema.

## 3. Personas y perfiles considerados

| Grupo | Participación dentro del alcance |
|---|---|
| Directiva | Administra y consulta información según permisos y cargos organizativos. Presidenta, Tesorera y Secretaria son cargos dentro de la organización, no perfiles técnicos independientes por defecto. |
| Socias operarias | Consultan información propia y registran o confirman tareas cuando tienen el permiso o encargo correspondiente. |
| Visitantes | Consultan únicamente la información pública aprobada por la organización. |
| Soporte técnico | Mantiene el sistema; no adquiere por ello autoridad para aprobar, sancionar, asignar responsabilidades o validar operaciones de negocio. |

La matriz de autorizaciones detallada debe quedar especificada por operación. El alcance
no concede a una persona permisos por cargo que todavía no se hayan definido y aprobado.

## 4. Funcionalidades incluidas y relación con el calendario

Las capacidades siguientes pertenecen al alcance funcional aprobado por el tesista a
través de la línea base de requisitos generales v2.0. El sprint indicado es la ubicación
del plan vigente, no una confirmación de estimación, capacidad, compromiso de desarrollo ni
entrega realizada. La importancia cualitativa está en [requisitos generales v2.0](../requisitos/requisitos_generales_v2.0_2026-10-13.md)
y [priorización v1.3](../requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13.md).

| Bloque de alcance | Funcionalidad incluida | Requisitos funcionales | Ubicación del plan vigente |
|---|---|---|---|
| Acceso y administración | Inicio y cierre de sesión, gestión de cuentas y membresías, permisos básicos y página privada con información pertinente a cada usuaria. | RF-ACC-001 a RF-ACC-004 | S2: 13–26 oct |
| Planificación | Registro y consulta de jornadas y eventos, asignación de participantes y responsables, encargos temporales con aceptación/cierre y planificación semanal de producción. | RF-PLA-001 a RF-PLA-005 | S3: 27 oct–9 nov |
| Asistencia y participación | Entrada y salida por instancia, historial, correcciones auditadas, participación cuando aplique, QR/código alternativo y generación automática de faltas al cierre de actividades. La justificación tiene un máximo de tres días hábiles; la Tesorera valida una multa antes de aplicarla. Valores comunicados: USD 10 por falta, USD 0,01 por minuto de atraso y aviso a la tercera falta. | RF-ASI-001 a RF-ASI-007 | S4: 10–23 nov |
| Catálogo, producción e inventario | Catálogo con unidades y presentaciones, valores con vigencia, acopio, secado, cálculo de merma, trazabilidad de lotes, transformación según receta aprobada, movimientos, entregas, conciliación, inventario bajo custodia y alertas con umbrales aprobados. | RF-CAT-001; RF-TRA-001 a RF-TRA-005; RF-INV-001 a RF-INV-006 | S5: 24 nov–7 dic; confirmar selección y capacidad en el backlog |
| Ventas, gastos, cuentas y rendición | Registro de ventas individuales, compartidas e institucionales; excepciones y descuentos configurados; gastos previstos y reales; cuentas por cobrar y saldos separados; abonos; rendición de feria y preparación de comisiones cuando exista fórmula aprobada. | RF-VEN-001 a RF-VEN-009; RF-GAS-001 a RF-GAS-002; RF-CXC-001 a RF-CXC-003 | S5: según capacidad y dependencias; confirmar en el backlog |
| Reportes, recordatorios e información pública | Consultas de asistencia, actividades, producción, inventario, ventas y saldos; resúmenes privados; avisos internos; contenido público autorizado y precios vigentes aprobados. | RF-REP-001 a RF-REP-006; RF-NOT-001 a RF-NOT-002; RF-PUB-001 a RF-PUB-003 | S6: 8–21 dic; el envío externo permanece condicionado |
| Continuidad y PWA | Instalación/recursos esenciales, almacenamiento local de operaciones habilitadas y sincronización idempotente con revalidación del servidor. Asistencia y pesajes son flujos sujetos a sus decisiones; no se incluye autenticación offline. | RF-PWA-001 a RF-PWA-003; RNF-CON-001 | Transversal; S4/S5 para los flujos aprobados, según decisiones y capacidad |
| Gestión documental | Registro, consulta y versionado de documentos organizacionales y productivos, con acceso autorizado y avisos internos de vencimiento. | RF-DOC-001; RNF-PRV-001 | Capacidad transversal confirmada; sprint de ejecución por asignar en backlog |
| Activos organizacionales | Registro e historial de activos separado de existencias consumibles. | RF-AST-001 | Capacidad confirmada en la línea base; sprint de ejecución por asignar en backlog |

Los nueve RNF aplican transversalmente: RNF-UX-001, RNF-UX-002, RNF-UX-003,
RNF-CON-001, RNF-SEC-001, RNF-AUD-001, RNF-DAT-001, RNF-PRV-001 y RNF-PDF-001.
Cubren uso móvil, accesibilidad, lenguaje claro, continuidad, autorización en servidor,
auditoría, integridad transaccional, privacidad y claridad/trazabilidad de PDF.

Los grupos y fechas de desarrollo conservan el [plan de sprints v1.2](../sprints/plan_sprints_v1.2_2026-10-13.md):
S1 es trabajo de requisitos y diseño (15 sep–12 oct); S2–S6 son incrementos de desarrollo
hasta el 21 de diciembre; el cierre planificado es 22–23 de diciembre. El S1 figura como
**partially-complete** en el estado operativo. Esta edición no lo marca como completo ni
cambia el backlog, las fechas, las estimaciones o la capacidad.

## 5. Exclusiones explícitas y límites

- No se incluye una afirmación de cumplimiento de registro sanitario ni la gestión de
  trámites ante ARCSA.
- RF-COS-001 (registro de consumos y costos directos conocidos) y RNF-OPS-001 (copias
  protegidas y restauración demostrable) siguen propuestos, fuera de los 67 requisitos
  confirmados.
- Las ausencias se generan automáticamente al cierre de la actividad según RF-ASI-006.
  La multa monetaria no se aplica automáticamente: requiere validación previa de la
  Tesorera. El procedimiento completo continúa limitado por P-03.
- No se envían mensajes externos hasta definir canal, proveedor, costos, contenido,
  destinatarios y consentimiento conforme a RF-NOT-002.
- El enlace contextual de WhatsApp de RF-PUB-003 inicia una consulta; no crea por sí solo
  un pedido, una reserva ni una venta.
- No se distribuyen comisiones de feria hasta que la organización apruebe fórmula,
  destinatarios y excepciones; RF-VEN-009 permite preparar la distribución trazable.
- No se adopta como receta aprobada la equivalencia de 50 litros con 100 unidades de
  champú. La transformación usa una composición y versión de receta aprobadas.
- RF-AST-001 no incorpora depreciación hasta que se aprueben método y vida útil.
- No se incluyen firma electrónica o legal, funcionalidades tributarias ni manejo de
  datos personales sin autorización, propósito, acceso y conservación definidos.
- No se habilita autenticación offline. La captura local solo aplica a operaciones
  expresamente habilitadas y conserva su estado provisional hasta validación del servidor.
- Este alcance no compromete que todos los requisitos se desarrollen dentro de una
  capacidad aún no estimada. Los elementos de S5 asignados según capacidad y las
  capacidades transversales requieren prioridad/dependencias y asignación verificable en
  el backlog, sin reducir la línea base por inferencia.

## 6. Restricciones, supuestos y dependencias

| Tipo | Condición | Efecto en el alcance |
|---|---|---|
| Confirmado | La aplicación objetivo usa Python, Django, PostgreSQL, Bootstrap 5 y plantillas MTV dentro de un monolito modular. | Se respeta ADR-0006 y la constitución vigente; no se reabre la decisión arquitectónica. |
| Confirmado | SPEC-001 define acceso básico de usuarias internas; no cubre operaciones de negocio ni autenticación offline. | S2 desarrolla la base de acceso y no sustituye las especificaciones de planificación o módulos posteriores. |
| Confirmado | La revisión del tesista sobre requisitos y el reporte de revisión en clase son antecedentes distintos de una revisión académica formal. | La revisión formal/directora permanece pendiente; alcance v1.3 requiere revisión propia. |
| Confirmado | S1 terminó según calendario, pero su cierre está registrado como parcial y faltan evidencias/validaciones. | Este documento no cambia el estado del sprint ni abre la puerta de implementación. |
| Supuesto de planificación | Las fechas de S2–S6 son el calendario objetivo, sujetas a capacidad y disponibilidad real. | El backlog debe confirmar estimaciones, dependencias y compromiso antes de iniciar cada trabajo. |
| Dependencia organizacional | Faltan definiciones de políticas, fórmulas, umbrales, permisos, contenido público y operación sin conexión. | Solo se especifican o automatizan las partes cuyas reglas estén resueltas. |
| Dependencia documental | El acta formal de la entrevista del 12/10/2026 no fue proporcionada. | El registro de necesidades se limita al resumen comunicado por el tesista; acta y cotejo formal continúan pendientes. |

La entrevista y las decisiones abiertas se consultan en el [registro v1.1](../levantamiento/registro_entrevista_v1.1_2026-10-13.md)
y en CAT-REQ-001. Los pendientes P-02 a P-14 son:

| Decisión | Tema abierto | Límite que debe conservarse |
|---|---|---|
| P-02 | Duración del QR, responsables y delegaciones. | No inventar tiempos ni autoridades. |
| P-03 | Inicio del plazo de justificación, canal, resolución, redondeo, impugnación y cobro de multas. | La falta se genera automáticamente; la Tesorera valida la multa; no se aplica una sanción monetaria sin esa validación. |
| P-04 / P-05 | Presentaciones, unidades, conversiones, plantas y excepciones de lotes. | No convertir unidades incompatibles ni fusionar lotes sin mezcla física autorizada. |
| P-06 a P-09 | Costos, distribución de stock compartido, descuentos y ajustes monetarios. | No presentar excedente bruto como utilidad neta ni distribuir importes sin fórmula aprobada. |
| P-10 / P-11 | Custodia y conciliación del comprobante manual; política de respaldos. | La contingencia manual no reemplaza la sincronización PWA; RNF-OPS-001 sigue propuesto. |
| P-12 | Contenido público y responsables de aprobación. | No publicar información final no aprobada. |
| P-13 / P-14 | Operaciones offline, tiempo, conflictos, dispositivo compartido y retención local. | No confirmar al servidor una captura provisional ni admitir autenticación offline. |

P-01 está cerrado únicamente para el acceso básico. El estado de las demás decisiones se
conserva en CAT-REQ-001 y sus registros; este alcance no las cierra.

## 7. Validación y cierre del alcance

Para aprobar esta edición se requiere revisión del tesista del contenido, trazabilidad de
los requisitos y correspondencia del calendario. La revisión académica formal debe
registrarse por separado, identificando quién revisó, cuándo y el resultado. Las novedades
de entrevista necesitan validación organizacional directa y el acta formal permanece
pendiente.

El cierre de cada bloque exige especificación, autorización, implementación y pruebas
verificables acordes con sus dependencias. El S1 no se considera terminado por la
preparación de este documento. No hay implementación Django acreditada mediante esta
edición.

## 8. Fuentes de referencia

- [CAT-REQ-001 v1.2](../../docs/requirements/CAT-REQ-001.md), catálogo interno vigente.
- [Requisitos generales v2.0](../requisitos/requisitos_generales_v2.0_2026-10-13.md), lista completa de 58 RF y 9 RNF.
- [Priorización de requisitos v1.3](../requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13.md).
- [Registro de entrevista v1.1](../levantamiento/registro_entrevista_v1.1_2026-10-13.md); acta formal pendiente.
- [Evidencia de aprobación del tesista](../../docs/evidence/requirements/2026-10-13-aprobacion-propuesta-requisitos-generales-v2-2.md).
- [Reporte de revisión docente en clase](../../docs/evidence/requirements/2026-10-13-reporte-revision-docente-en-clase.md), limitado a lo comunicado por el tesista.
- [Plan de sprints v1.2](../sprints/plan_sprints_v1.2_2026-10-13.md) y sprint backlog v1.2.
- [SPEC-001 — Acceso de usuarias internas](../../specs/001-acceso-usuarias-internas/spec.md).
- [ADR-0006 — Monolito modular y entrega incremental](../../docs/decisions/ADR-0006-monolito-modular-y-entrega-incremental.md).

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.1 | 2026-10-12 | Se integra la entrevista como necesidades pendientes, sin ampliar la línea base confirmada. | Edición documental; revisión académica pendiente |
| 1.2 | 2026-10-13 | Se aclara la correspondencia de SPEC-001 con S2 del calendario actualizado. | Sin cambio de alcance; revisión pendiente |
| 1.3 | 2026-10-13 | Se alinea con CAT v1.2 y requisitos generales v2.0; se corrige la ubicación de capacidades por sprint y se registra por separado el reporte de revisión docente y las validaciones pendientes. | Preparado para revisión del tesista; no aprobado en esta edición |
