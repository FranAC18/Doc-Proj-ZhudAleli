---
titulo: Impacto documental del resumen de entrevista
version: "1.0"
fecha: 2026-10-12
autor: Codex, para revisión del tesista
estado: candidato-interno
fuente: EVID-ENT-2026-10-12-001
publicacion: no-autorizada
---

# Impacto documental del resumen de entrevista

## Regla de incorporación

Esta matriz separa tres cosas: **necesidad narrada en la entrevista**, **requisito ya
confirmado** y **detalle o capacidad nueva que falta validar**. El tesista identificó
a María Camas como tesorera entrevistada el 12/10/2026 y comunicó que la organización
aprobó los montos y reglas de asistencia. La aclaración final fija USD 0,01 por minuto,
USD 10 desde la primera falta y aviso a la tercera falta. Faltan acta, definiciones,
justificativos, autoridad y procedimiento de cobro. Por ello
no se altera `CAT-REQ-001 v1.1`, sus 60 requisitos ni las 51 HU y 9 HT que derivan de esa
línea base. La constitución 0.2.0 ya ordena vincular cada función con una fuente y no
automatizar reglas pendientes; el resumen no pide cambiar esos principios.

## Relación de los doce temas con la línea base

| Tema | Relación con requisitos vigentes | Cambio propuesto para estudiar | Prioridad de aclaración |
|---|---|---|---|
| 1. Menos papel, viajes y demoras | Objetivo general, planificación y trazabilidad. | Definir línea base y medidas de resultado antes de prometer ahorro. | Alta |
| 2. Pérdidas y costos declarados | Factibilidad económica y problema; montos aprobados según el tesista. | Comprobar base de cálculo y si cada cifra representa incidente, promedio o escenario. Para abogado: USD 500 por mes durante dos meses. | Alta |
| 3. Expediente documental y firmas | Reportes PDF cubren salidas, pero no un repositorio documental integral ni firma. | Proponer gestión documental con versiones, permisos, vencimiento y tipos; estudiar firma por separado. | Alta por privacidad; alcance por aprobar |
| 4. Alertas de vencimiento | `RF-NOT-001` cubre recordatorios internos, no vencimientos de documentos. | Definir tipos, fechas, anticipación de tres/seis meses y canal externo opcional. | Alta para diseño; alcance por aprobar |
| 5. QR y multas | `RF-ASI-001/006/007`, P-02 y P-03 cubren registro e inconsistencia. | Incorporar como propuesta la secuencia final comunicada: USD 0,01/min, USD 10 desde primera falta y aviso a tercera falta; resolver justificativos y autoridad antes de automatizar. | Inmediata por cambio respecto de regla vigente |
| 6. Agenda y WhatsApp | `RF-PLA-001/002/004`, `RF-NOT-001` cubren actividades y avisos internos. | Afinar reuniones/lugar/delegación; estudiar avisos uno/dos días antes y WhatsApp. | Alta; canal y calendario por aprobar |
| 7. Encargo de secado con evidencia | `RF-PLA-003`, `RF-TRA-002` cubren encargo y secado en partes. | Definir estados de tarea, quién acepta cierre, evidencia y nueva delegación. | Alta antes de diseñar flujo |
| 8. Inventarios | `RF-CAT-001`, `RF-INV-002/003/004`, `RF-TRA-004` cubren movimientos, lotes y stock de feria. | Distinguir stock personal y general; estudiar activos fijos y depreciación como alcance nuevo. | Alta para stock; depreciación por decidir |
| 9. Producción y alertas | `RF-PLA-005`, `RF-TRA-001/005`, `RF-INV-002` enlazan plan, insumos y resultado. | Validar receta/unidades del ejemplo y umbrales de materia por planta antes de alertas. | Alta para fórmulas; alertas por aprobar |
| 10. Página pública y contacto comercial | `RF-PUB-001/002` cubren contenido aprobado; `RF-VEN-001` cubre ventas internas. | Decidir si precios públicos y botón WhatsApp son contacto o pedido; P-12 sigue abierto. | Alta antes de publicar |
| 11. Feria y comisiones | `RF-INV-003/004`, `RF-VEN-001/006/008`, `RF-GAS-001`, `RF-CXC-003` cubren núcleo. | Separar gastos previstos/reales y definir reglas de comisión y reparto antes de calcular. | Alta para conciliación; fórmula por aprobar |
| 12. Venta mensual de socias | `RF-INV-003/004`, `RF-VEN-001/003/006`, `RF-CXC-001/002` cubren parte comercial. | Definir período, entrega, saldo, comisión individual, aviso y conexión de inventario. | Alta para flujo; reglas por aprobar |

## Documentos que reciben impacto

| Documento | Incorporación correcta ahora | Condición para edición final nueva |
|---|---|---|
| Alcance | Anotar las capacidades nuevas y su estado pendiente, especialmente expediente, activos, alertas externas y comisiones. | Aprobación de inclusión y límites por tesista y revisión académica donde afecte anteproyecto. |
| Requisitos funcionales y no funcionales | Mantener los 51 RF/9 RNF; crear propuestas separadas para expediente, vencimientos, canal externo, tareas, activos/alertas y venta mensual. | Validar actor, regla, datos, permisos y criterios; resolver conflictos P-03, P-07, P-08, P-12. |
| Historias de usuario | Mantener 51 historias canónicas; añadir fichas candidatas identificadas como propuestas, sin mezclarlas en el total confirmado. | Requisito aprobado y criterios verificables. |
| Historias técnicas | Analizar protección de documentos, canal de avisos, programación temporal y cálculo económico; sin prometer proveedor o firma legal. | Alcance y políticas aprobadas; estimación técnica. |
| Pila de producto | Crear una bandeja de descubrimiento distinta de las 60 entradas base. | Prioridad con representantes, estimación y decisión de entrada a sprint. |
| Priorización | Priorizar **aclarar** sanciones, privacidad, comisiones y fechas, no ejecutar automáticamente ideas nuevas. | Decisión trazable sobre cada tema. |
| Factibilidad | Registrar aprobación de montos comunicada por el tesista, sin tratarlos como ahorro medido; estimar costo y carga de nuevas capacidades. | Evidencia de base de cálculo, alcance, calendario y recursos revisados. |
| Arquitectura y diseño | Evaluar archivos, permisos, auditabilidad, temporalidad y mensajería solo al aprobar el alcance. | ADR o specs de las funciones aprobadas; no cambia la constitución por esta nota. |
| Sprints y pruebas | Registrar riesgo de carga y escenarios de prueba futuros. | Replanificación humana; prohibido prometer inclusión automática en el calendario actual. |
| Control de cambios e índice final | Registrar la nueva versión solo cuando exista una edición final revisada. | Revisión editorial y autorización separada para commit/publicación. |

## Preguntas que bloquean decisiones

| Nº | Pregunta concreta | Por qué importa |
|---:|---|---|
| 1 | ¿Hay acta o constancia del acuerdo sobre los montos y las reglas de asistencia? | Procedencia verificable de la aprobación comunicada. |
| 2 | ¿Qué constituye falta o atraso, cuándo se justifica, quién decide y cómo se cobra? ¿El aviso a la tercera falta se emite antes o después de aplicar la multa de ese evento? | P-03 y prevención de sanciones incorrectas. |
| 3 | ¿Se administrarán copias de cédulas y firmas, o basta un registro de existencia y ubicación? ¿Quién accede y por cuánto tiempo? | Privacidad y volumen de datos sensibles. |
| 4 | ¿Qué base de cálculo tienen USD 15, 20.000 y 80/día? ¿Hay comprobantes de los USD 500 mensuales durante dos meses? | Factibilidad y beneficios calculables. |
| 5 | ¿WhatsApp será un enlace abierto por la usuaria o mensajes enviados automáticamente por el sistema? | Permisos, consentimiento, costos y esfuerzo técnico. |
| 6 | ¿Cómo se calculan y aprueban comisiones de feria y venta mensual, y cómo se distinguen costo, valor base y excedente? | Resultados económicos confiables y P-07/P-06. |
| 7 | ¿Activos fijos/depreciación y gestión documental completa son parte de la entrega de diciembre o un incremento posterior? | Alcance y calendario. |
| 8 | ¿La fórmula de 50 litros y 100 champús es un ejemplo o una receta oficial? ¿Qué mermas y unidades se admiten? | Evitar inventario y producción equivocados. |

## Historial

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.0 | 2026-10-12 | Mapa de cobertura, conflictos y propagación documental del resumen de entrevista. | Candidato interno |
