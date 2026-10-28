---
title: Cotejo de fuentes de SB-S1-01 trasladada a Sprint 2
type: checkpoint
status: in-progress
date: 2026-10-20
task_id: SB-S1-01
sprint_execution: S2
source: EVID-ENT-2026-10-12-001
---

# `SB-S1-01` — cotejo de necesidades y catálogo

## Procedencia y método

El tesista informó una entrevista del **12/10/2026** a una **tesorera de la organización** y entregó un resumen de doce temas. El documento disponible es [EVID-ENT-2026-10-12-001](../../evidence/requirements/2026-10-12-resumen-entrevista-temas-organizacionales.md); el [registro de entrevista v1.1](../../../documentacion/levantamiento/registro_entrevista_v1.1_2026-10-13.md) lo coteja con [CAT-REQ-001 v1.2](../../requirements/CAT-REQ-001.md). No constan acta, audio ni transcripción de la entrevista; la identidad y el rol de la entrevistada proceden del reporte del tesista. El acta de julio corresponde a otro levantamiento.

La tabla explicita, para cada necesidad comunicada, actor y fecha de origen, duda pendiente y enlace al catálogo. **Tesorera\*** significa «tesorera según resumen comunicado por el tesista», no validación directa comprobada. Las citas de RF indican cobertura del catálogo, no que todos los detalles de la entrevista estén aprobados para implementar.

| Nº | Actor y fecha comunicados | Necesidad o dato | Duda o límite pendiente | Cotejo con catálogo v1.2 |
|---:|---|---|---|---|
| 1 | Tesorera\*, 12/10/2026 | Reunir documentos y datos para reducir papel, traslados y demoras. | Indicadores y línea base de tiempo, viajes y papel. | Problema y objetivos; no hay RF ni ahorro medido. |
| 2 | Tesorera\*, 12/10/2026 | Costos y pérdidas estimados por tiempo, inconsistencias, asesoría y proyectos. | Frecuencia, unidad de USD 15, comprobantes y parte evitable; USD 20.000 es eventual. | Insumo de factibilidad; `RF-COS-001` sigue propuesto y no convierte estas cifras en ahorro observado. |
| 3 | Tesorera\*, 12/10/2026 | Organizar y versionar documentos organizacionales y productivos. | Tipos, metadatos, responsables, retención y datos personales. | `RF-DOC-001`, `RNF-PRV-001`; propietario modular aún pendiente. |
| 4 | Tesorera\*, 12/10/2026 | Avisar antes del vencimiento de documentos. | Plazos por tipo, destinatario, canal y consentimiento; tres/seis meses son ejemplos por validar. | Aviso interno en `RF-DOC-001`; canal externo condicionado por `RF-NOT-002`. |
| 5 | Tesorera\*, 12/10/2026 | QR de asistencia, faltas y justificación; valores de multa y atraso comunicados. | P-02/P-03: tiempos, autoridad, justificación, redondeo, impugnación y cobro. | `RF-ASI-001/006/007`; la falta al cierre no aplica automáticamente una multa. |
| 6 | Tesorera\*, 12/10/2026 | Agenda, encargos y recordatorios de actividades. | Destinatarios, momentos, cambios y canal externo. | `RF-PLA-001/002/004`, `RF-NOT-001`; WhatsApp depende de `RF-NOT-002`. |
| 7 | Tesorera\*, 12/10/2026 | Delegar secado, confirmar encargo, registrar cierre y reasignar. | Actor que acepta/reasigna, plazos, evidencia y confirmación tardía. | `RF-PLA-003` y relación con `RF-TRA-002`. |
| 8 | Tesorera\*, 12/10/2026 | Separar activos, lotes, materia prima y custodia individual. | Propiedad, movimientos, conciliación y depreciación. | `RF-AST-001`, `RF-INV-002/003/004/005`; depreciación fuera de alcance actual. |
| 9 | Tesorera\*, 12/10/2026 | Relacionar insumos con productos y alertar mínimos. | Recetas, unidades, merma y umbrales; 50 litros/100 champús no es fórmula aprobada. | `RF-TRA-001/005`, `RF-PLA-005`, `RF-INV-006`. |
| 10 | Tesorera\*, 12/10/2026 | Publicar precios aprobados y abrir consulta comercial por WhatsApp. | Vigencia y autorización del precio; contacto no equivale a pedido. | `RF-PUB-001/002/003`; canal y datos según criterio aprobado. |
| 11 | Tesorera\*, 12/10/2026 | Registrar stock, gastos y rendición de ferias. | Fórmula de comisiones, responsables y conciliación. | `RF-INV-003/004`, `RF-VEN-006/009`, `RF-GAS-001`, `RF-CXC-003`. |
| 12 | Tesorera\*, 12/10/2026 | Cierre mensual por socia de entregas, ventas, devoluciones y pagos. | Periodo, costo/base, comisiones y conciliación. | `RF-REP-005`, `RF-INV-005`, `RF-VEN-003/006`; fórmula de comisión no aprobada. |

## Resultado y continuidad

El cotejo documental de los **doce temas disponibles** queda explícito. La aprobación del tesista de los requisitos generales y `CAT-REQ-001` v1.2 se conserva según su evidencia propia; no se atribuye a la organización una validación directa de cada novedad. **No se marca `SB-S1-01` como terminada:** faltan fuente primaria de la entrevista y, si se solicita para esta tarea, validación organizacional directa y revisión académica. Estas ausencias no impiden comenzar una porción independiente de `RF-ACC-001` en S2.

La siguiente acción de `SB-S1-01` es incorporar acta/audio/transcripción o confirmar expresamente su inexistencia definitiva, y registrar cualquier contraste directo posterior con fecha, versión y alcance. No se modifica retroactivamente el cierre administrativo del sprint 1.
