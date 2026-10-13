---
title: Temas de entrevista para validar como requisitos
type: requirement-proposal
status: proposed
id: PRO-ENT-001
version: 0.1
date: 2026-10-12
task_id: DOC-ORG-001
phase: Fase I y revisión de alcance
sprint: transversal
module: transversal
commit: pending
related:
  - "[[../../evidence/requirements/2026-10-12-resumen-entrevista-temas-organizacionales]]"
  - "[[../CAT-REQ-001]]"
  - "[[../../../analisis/2026-10-12/entrevista/impacto-documental-candidato_v1.0_2026-10-12]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - estado/proposed
  - modulo/transversal
---

# Temas de entrevista para validar como requisitos

## Estado

La entrevista del 12/10/2026 (EVID-ENT-2026-10-12-001) aporta necesidades y ejemplos.
El tesista comunica que la organización aprobó los montos y reglas de asistencia.
La aclaración final fija USD 0,01 por minuto de atraso, USD 10 desde la primera falta
y aviso a la tercera falta. No se recibió acta ni están definidos justificativos,
autoridad y forma de cobro. Tampoco consta decisión
de incluir nuevas capacidades en la entrega de diciembre. Esta nota
es una **propuesta**, no una versión nueva del catálogo canónico. Los 60 requisitos
confirmados y las decisiones P-02 a P-14 siguen vigentes.

| Bloque candidato | Necesidad de campo | Relación con la línea base | Antes de proponer un RF concreto |
|---|---|---|---|
| Gestión documental | Encontrar y relacionar documentos de asociación y producción; considerar vencimientos. | Reportes PDF actuales son salidas, no un expediente documental. | Definir tipos, permisos, conservación, tamaño y quién responde por cada documento. |
| Firma documental | Firmar documentos desde el sistema. | No hay función equivalente aprobada. | Aclarar tipo de firma, efecto esperado y verificación jurídica; no prometer validez legal. |
| Avisos externos | Informar por WhatsApp o celular sobre vencimientos, reuniones y encargos. | RF-NOT-001 confirma avisos dentro del sistema. | Elegir canal, consentimiento, destinatarios, costos, fallos y ventanas de aviso. |
| Revisión de asistencia | Considerar USD 0,01 por minuto de atraso, USD 10 desde la primera falta y aviso a la tercera falta, según el tesista. | RF-ASI-006 exige decisión de asamblea; P-03 bloquea sanciones automáticas. | Registrar acuerdo/reglamento, definir falta y atraso, justificativos, autoridad, redondeo, cobro e impugnación. |
| Tareas delegadas | Confirmar secado con evidencia y reencargar si no termina. | RF-PLA-003 y RF-TRA-002 cubren encargo y secado por separado. | Definir estados, responsable, aceptación, evidencia y efecto sobre lote. |
| Inventario ampliado | Diferenciar stock personal/general y activos patrimoniales. | RF-INV-002/003/004 cubren movimientos y stock de feria. | Definir propiedad, transferencias y si depreciación entra al alcance. |
| Alertas productivas | Avisar mínimos por planta e insumo; relacionar recetas y resultado. | RF-PLA-005, RF-TRA-005 y RF-INV-002 aportan datos de base. | Confirmar recetas, unidades, umbrales, mermas y momento de alerta. |
| Sitio comercial | Mostrar precios y abrir contacto por WhatsApp. | RF-PUB-001/002 solo muestran contenido aprobado; P-12 abierto. | Determinar si es consulta o pedido, precio vigente y contenido autorizado. |
| Feria ampliada | Preparar gastos, cerrar cuentas y calcular comisiones. | Feria, gastos y rendición tienen cobertura parcial. | Definir gastos previstos/reales, reparto y fórmulas con P-07/P-09. |
| Venta mensual de socias | Entregar productos a cada socia, rendir valor a la asociación y conservar comisión. | Hay ventas, stock individual y saldos, pero no esta periodicidad ni comisión definida. | Confirmar obligación, período, valor base, conciliación y devoluciones. |

Los USD 15, 20.000, 80 por día y 500 por mes son montos comunicados como aprobados por la
organización, pero aún falta su base de cálculo. Para el abogado se aclaró USD 500
por mes durante dos meses (USD 1.000 referidos para el periodo). Se usan como preguntas para
factibilidad, nunca como beneficio calculado. El ejemplo de
50 litros/100 champús tampoco se adopta como receta.

## Puerta de decisión

Para cada bloque se necesita actor, problema, dato, regla, criterio verificable, fuente y
aprobación de alcance. Si afecta el anteproyecto o el calendario, se registra además la
revisión académica correspondiente. Solo entonces se propone un ID RF/RNF y una HU/HT
planificable. La constitución 0.2.0 ya establece esta puerta y no se enmienda por esta nota.
