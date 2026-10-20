---
codigo: ZA-ALC-003
titulo: Alcance del módulo de planificación de actividades
modulo: Planificación de actividades
fase: Fase 1 — Documento de alcance del módulo
version: 1.0
fecha: 2026-10-13
autor: Franklin Acero (tesista)
analista: Codex (asistencia de redacción)
estado: propuesta-para-revision
publicacion: no-preparado
prioridad_modulo: Sprint 2 según el plan aprobado
fuentes_requisitos: "CAT-REQ-001 v1.2; requisitos generales v2.0; priorización v1.3"
revision_directora: pendiente
validacion_organizacional: no-atribuida-por-esta-edicion
related:
  - "[[../../../docs/requirements/CAT-REQ-001]]"
  - "[[../../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13]]"
  - "[[../../../documentacion/requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13]]"
  - "[[../diagramas-procesos/ZA-DG-001-diagramas-generales-por-proceso-v1.1-2026-10-13]]"
tags:
  - proyecto/tesis
  - tipo/alcance
  - sprint/s2
  - modulo/planificacion
---

<table style="width:100%;border-collapse:collapse;font-family:'Heebo Light',Heebo,Arial,sans-serif;">
<tr><td colspan="2" style="background:#642138;color:#F0EAC8;padding:14px;font-family:'Mallong Regular',Georgia,serif;font-size:22px;"><strong>[LOGO: Isotipo floral de 4 pétalos - ZHUD ALELÍ Productos Naturales]</strong><br>ZA-ALC-003 · Alcance del módulo de planificación de actividades</td></tr>
<tr><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Control documental</th><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Valor</th></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Módulo</td><td style="padding:7px;border:1px solid #AC6E40;">Planificación de actividades (<code>planning</code>)</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Fase / entregable</td><td style="padding:7px;border:1px solid #AC6E40;">Fase 1 — Documento de alcance del módulo</td></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Versión / fecha</td><td style="padding:7px;border:1px solid #AC6E40;">v1.0 / 13 de octubre de 2026</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Autor / analista</td><td style="padding:7px;border:1px solid #AC6E40;">Franklin Acero (tesista) / Codex (asistencia de redacción)</td></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Estado</td><td style="padding:7px;border:1px solid #AC6E40;">Propuesta interna para revisión; pendiente de aprobación del tesista</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Prioridad / orden</td><td style="padding:7px;border:1px solid #AC6E40;">Sprint 2 según el plan aprobado; requisitos de importancia alta y complementaria</td></tr>
</table>

**Identidad visual:** Verde Bosque `#4C5B4A`, Borgoña `#642138`, Terracota `#AC6E40` y Crema Natural `#F0EAC8`; Mallong Regular para títulos y Heebo Light para texto, con equivalentes serif/sans-serif si no están disponibles.

### Historial de revisiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| v1.0 | 13-10-2026 | Emisión inicial del alcance de Planificación a partir de los cinco requisitos confirmados y su priorización. | Franklin Acero; borrador asistido por Codex |

## 1. Propósito y descripción general del módulo

El módulo **Planificación de actividades** organiza jornadas y eventos del Comité, registra a las personas responsables y participantes, y permite consultar las actividades y pendientes que corresponden a cada socia. También delimita encargos temporales de producción o feria y registra planes semanales de producción para que los módulos operativos reciban instrucciones con responsables y cantidades previstas.

El alcance funcional comprende los cinco requisitos confirmados `RF-PLA-001` a `RF-PLA-005`: cuatro de importancia **alta** y uno **complementario**. El módulo es el Sprint 2 del plan aprobado. Sus actividades son la fuente de contexto para Asistencia; sus encargos y planes se integran con Producción, Inventario y Feria. Una planificación no registra asistencia, crea lotes ni altera existencias.

## 2. Objetivos de negocio y alineación con Zhud Alelí

- Dejar por escrito fechas, lugares, responsables, participantes y estados de jornadas y eventos, disminuyendo la dependencia de asignaciones verbales.
- Hacer visible a quién corresponde cada actividad o encargo y qué pendientes permanecen vigentes.
- Acotar temporalmente los encargos de producción o feria para que las operaciones respeten el periodo y el alcance asignados.
- Organizar semanalmente productos, cantidades objetivo, responsables e insumos previstos sin confundir una meta planificada con producción realizada.
- Dar a las socias consultas comprensibles y limitadas a las actividades y tareas que les corresponden.
- Conservar la historia de las asignaciones y cambios relevantes para que la organización pueda revisar qué se modificó y cuándo.

## 3. Entregables clave y funcionalidades incluidas (In-Scope)

| ID e importancia | Entregable o capacidad incluida | Requisito(s) relacionado(s) | Límite o condición |
|---|---|---|---|
| P1 · Alta | Registrar jornadas y eventos con instancia, fecha, hora, lugar, responsable, participantes y estado; validar datos y permitir corregir errores de captura. | `RF-PLA-001`; RNF de integridad, auditoría y UX | La lista cerrada de tipos y transiciones de estado se define en la especificación si no está validada en la fuente. |
| P2 · Alta | Asignar responsables y participantes, comprobar que sus cuentas estén activas y delimitar el alcance de cada asignación. | `RF-PLA-002`; `RF-ACC-002/003`; RNF de seguridad y privacidad | Las operaciones permitidas por cargo o encargo se detallan por acción; no se presume una matriz universal. |
| P3 · Alta | Crear y consultar encargos temporales de producción o feria asociados a una actividad, con periodo, alcance, responsable, aceptación y cierre con evidencia; permitir reasignación cuando no exista confirmación según reglas que se acuerden. | `RF-PLA-003`; RNF de auditoría, integridad y privacidad | El plazo de aceptación, autoridad de reasignación, evidencia admisible y aceptación del resultado continúan abiertos en el catálogo. |
| P4 · Complementaria | Consultar actividades y pendientes mediante filtros claros, con vistas autorizadas para Directiva y vistas individuales para las socias. | `RF-PLA-004`; `RF-ACC-004`; RNF de UX, seguridad y privacidad | Una socia accede solo a información propia o compartida con ella mediante una asignación válida. |
| P5 · Alta | Registrar planes semanales de producción con producto, cantidad objetivo, responsables e insumos previstos; mostrar el plan a las personas asignadas y conservar cambios. | `RF-PLA-005`; `RF-CAT-001`; RNF de auditoría e integridad | Un plan no registra producción realizada ni genera lotes, movimientos o existencias. Productos, unidades y reglas no definidas dependen de decisiones de Catálogo/Producción. |
| T1 — RNF | Aplicar controles transversales a formularios, lecturas, cambios, asignaciones y consultas del módulo. | `RNF-UX-001/002/003`; `RNF-CON-001`; `RNF-SEC-001`; `RNF-AUD-001`; `RNF-DAT-001`; `RNF-PRV-001` | La captura offline, su retención y reconciliación no se amplían por este alcance; se rigen por las decisiones y requisitos transversales vigentes. |

La prioridad del **requisito** no cambia el orden del plan aprobado: Planificación se mantiene en Sprint 2. En particular, `RF-PLA-001`, `RF-PLA-002`, `RF-PLA-003` y `RF-PLA-005` tienen importancia alta; `RF-PLA-004` es complementario. T1 no es un requisito funcional adicional: reúne condiciones de calidad aplicables.

### Entregables de análisis para la fase siguiente

- Especificación de casos de uso por los recorridos de actividad, asignación, encargo, consulta y plan semanal.
- Reglas de autorización y trazabilidad asociadas a cada operación, coordinadas con Acceso.
- Criterios de aceptación y flujos alternativos que cubran validaciones, cuentas inactivas, cambios de asignación y consultas vacías.
- Registro explícito de las decisiones de detalle que permanezcan abiertas; su existencia no autoriza a completar una regla por inferencia.

## 4. Exclusiones explícitas (Out-of-Scope)

- Registrar entradas, salidas, participaciones, faltas, justificaciones o multas; pertenecen a Asistencia, que consume actividades y participantes de este módulo.
- Registrar acopio, pesajes, tiempos de secado, transformación, lotes, mermas, movimientos de inventario o producción efectivamente realizada; corresponden a Producción y Trazabilidad.
- Administrar el catálogo maestro de plantas, productos, presentaciones, unidades, recetas, existencias o valores comerciales; este módulo los consulta por contratos permitidos.
- Registrar ventas, gastos, pagos, cuentas por cobrar, cierres de caja, rendiciones o reportes generales.
- Enviar avisos externos por WhatsApp, SMS o correo. Los recordatorios internos aprobados en `RF-NOT-001` pertenecen al alcance de Notificaciones; aquí Planificación proporciona los datos de actividad y destinatarios autorizados que se definan.
- Definir por inferencia el plazo para aceptar o cerrar encargos, quién valida su resultado, qué evidencia es obligatoria, cuándo se reasigna o el orden de aprobación de actividades.
- Definir recurrencia automática de reuniones, calendario compartido, reservas de espacios, presupuestos de producción o gestión de compras si no existe requisito aprobado que los incorpore.
- Construir o desplegar el sistema. Este documento establece alcance y no afirma que el módulo esté implementado o probado.

## 5. Restricciones, supuestos y dependencias técnicas

### 5.1 Restricciones y supuestos

- La aplicación futura sigue la constitución vigente: Python 3.12, Django 5.2 LTS, PostgreSQL, Bootstrap 5 y plantillas Django dentro de un monolito modular. Este documento no crea una aplicación funcional.
- Planificación posee las escrituras de actividades, asignaciones, encargos y planes que se definan para su responsabilidad; otros módulos usan operaciones públicas y lecturas autorizadas.
- La autorización se verifica en el backend para cada lectura y escritura, incluso ante acceso directo. Ocultar botones no sustituye la autorización.
- Los cambios sensibles de fechas, responsables, participantes, periodos, alcance, metas y cierres conservan los datos de auditoría exigidos, incluido actor, fecha y motivo cuando corresponda.
- La disponibilidad para móvil, teclado, contraste AA, texto además de color y recuperación de errores se aplica a los formularios y consultas del módulo.
- “Plan semanal” describe una intención y cantidad objetivo. No equivale a una orden de producción ejecutada, lote, consumo de insumos ni existencia disponible.
- No se presume que una asignación a una actividad otorgue automáticamente permisos de negocio sobre asistencia, inventario, ventas u otros módulos.

### 5.2 Dependencias

| Dependencia o decisión | Estado conocido | Efecto sobre el módulo |
|---|---|---|
| Acceso (`accounts`) / `RF-ACC-001` a `RF-ACC-003` | Línea base confirmada; los permisos concretos de operaciones se especifican en cada módulo. | Aporta identidad, estado de membresía y autorización; una cuenta inactiva no puede recibir una nueva asignación. |
| Asistencia (`attendance`) / `RF-ASI-001` a `RF-ASI-007` | Consume actividades y participantes definidos por Planificación. | La asistencia y las faltas se registran en el módulo de Asistencia; esta dependencia no delega sus escrituras. |
| Catálogo (`RF-CAT-001`) y producción (`RF-TRA-*`, `RF-INV-*`) | Requisitos confirmados; detalles de catálogo, unidades y reglas productivas mantienen decisiones propias abiertas. | El plan semanal referencia productos/unidades disponibles sin crear existencias, lotes, recetas o movimientos. |
| `RF-PLA-003` — ciclo de encargos | Aceptación, cierre con evidencia y posibilidad de reasignación incorporados; autoridad, plazos y tipos de evidencia siguen abiertos. | Precisar reglas de transición y permisos antes de cerrar los casos de uso afectados o implementarlos. |
| `RF-PLA-005` — planes semanales | Requisito confirmado; depende de catálogo de productos e insumos previstos. | Precisar unidades, versionado de metas y reglas de cambio cuando las fuentes de producto y producción estén definidas. |
| `RF-NOT-001` — recordatorios internos | La capacidad está confirmada, pero sus destinatarias y excepciones por tipo de actividad siguen pendientes. | El envío lo administra Notificaciones; la integración requiere resolver quién recibe cada aviso y en qué casos. |
| RNF transversales y PWA | Requisitos transversales confirmados; reglas de captura y sincronización no se detallan aquí. | Aplicar seguridad, auditoría, integridad, privacidad, accesibilidad y continuidad sin atribuir aceptación definitiva a cambios offline. |

### 5.3 Decisiones abiertas que no se resuelven en este alcance

- Tipos exactos de actividad, estados y transiciones permitidas.
- Quién puede crear, modificar, cancelar y cerrar cada clase de actividad, y bajo qué autorización organizacional.
- Plazo de confirmación de los encargos; autoridad de reasignación y evidencia suficiente para aceptar el cierre.
- Reglas para cambiar responsables, participantes, alcance o metas una vez iniciado el periodo.
- Unidades y referencias definitivas para productos e insumos previstos en la producción semanal.
- Destinatarios y excepciones de los recordatorios internos, según `RF-NOT-001`.
- Reglas de captura, conflicto y sincronización offline que afecten cambios de planificación.

## Fuentes y trazabilidad

- `CAT-REQ-001 v1.2`, fuente canónica para estado confirmado, Sprint 2, interacciones y decisiones abiertas.
- `requisitos_generales_v2.0_2026-10-13.md`, tabla completa de requisitos funcionales y criterios de comprobación.
- `priorizacion_requisitos_v1.3_2026-10-13.md`, clasificación de importancia de `RF-PLA-001` a `RF-PLA-005`.
- `ZA-DG-001-diagramas-generales-por-proceso-v1.1-2026-10-13.md`, diagrama general propuesto de Planificación para referencia visual, sin sustituir la especificación detallada.
- `ZA-ALC-001 v1.1` y `ZA-ALC-002 v1.0`, documentos de alcance previos usados como referencia de estructura y coherencia intermodular.
- `Formato Corregido.docx` y directrices de identidad visual aprobadas por el tesista.

**Estado de validación:** los cinco requisitos funcionales y su clasificación de importancia constan en las ediciones vigentes aprobadas por el tesista. Esta propuesta no atribuye revisión de la directora ni una nueva validación directa de la organización. La aceptación del tesista de este alcance queda pendiente.

**Puerta de avance:** revisar y aprobar este alcance antes de elaborar la Fase 2 — casos de uso detallados para Planificación. Este borrador no modifica la línea base de requisitos ni se sincroniza en `documentacion/`.
