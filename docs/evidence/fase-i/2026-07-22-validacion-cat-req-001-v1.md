---
title: Validación humana de CAT-REQ-001 v1.0
type: evidence
status: recorded
date: 2026-07-22
phase: Fase I
module: transversal
source_type: human-validation
source_name: Levantamiento de requisitos 1.0
participants:
  - Tesista
  - Organización
  - Presidenta
related:
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[../../requirements/proposals/2026-07-22-catalogo-revisado-requisitos-r3]]"
  - "[[../../00-inicio/01-decisiones-pendientes]]"
tags:
  - proyecto/tesis
  - tipo/evidencia
  - modulo/transversal
  - estado/registrado
---

# Validación humana de CAT-REQ-001 v1.0

## Identificación

- Fecha normalizada: 2026-07-22.
- Fecha recibida: `22 07 26`.
- Participantes y roles declarados: tesista, organización y presidenta.
- Fuente o acta declarada: **Levantamiento de requisitos 1.0**.
- Medio registrado: instrucción humana recibida en la sesión de trabajo del repositorio.
- Archivo externo del acta: no fue adjuntado en esta sesión.

## Decisión recibida

- Confirmar `RF-ACC-001` a `RF-ACC-004`.
- Confirmar `RF-PLA-001` a `RF-PLA-005`.
- Confirmar `RF-ASI-001` a `RF-ASI-006`.
- Ajustar `RF-ASI-007` para permitir autorregistro bajo riesgo aceptado por la organización.
- Confirmar catálogo, producción e inventario, incluidas las reglas delimitadas que conservan
  excepciones o datos pendientes.
- Confirmar ventas, gastos, saldos y rendición, incluidos `RF-VEN-006`, `RF-VEN-008` y
  `RF-CXC-001` con sus decisiones de detalle todavía abiertas.
- Confirmar reportes, recordatorios, sitio público y requisitos no funcionales.
- Mantener pendientes únicamente `RF-COS-001` y `RNF-OPS-001` como requisitos activos.
- Conservar `RF-OFF-001`, `RF-OFF-002` y `RF-OFF-003` como sustituidos para v1.
- Autorizar la preparación del catálogo canónico CAT-REQ-001.
- Permitir evolución posterior de requisitos durante la construcción mediante cambios
  trazables, adiciones o retiros validados.

## Criterio de interpretación aplicado

La respuesta incluyó el bloque de ejemplo de “aceptar R3 sin ajustes”, aunque antes indicó
un ajuste a `RF-ASI-007`, confirmó toda la sección de ventas y nombró solo dos pendientes.
Para evitar una contradicción interna se aplicó este orden:

1. Las decisiones específicas escritas por los participantes prevalecen sobre el ejemplo
   copiado.
2. Las expresiones `001-4`, `001-5` y `001-6` se interpretan como rangos consecutivos.
3. `RF-VEN-005` se confirma como capacidad configurable porque toda la sección de ventas fue
   confirmada; P-08 conserva los valores y umbrales todavía no proporcionados.
4. Las reglas `RN-*` de R3 se absorben en sus RF correspondientes y se conservan como
   decisiones P abiertas, evitando duplicar requisitos activos.
5. Los parámetros abiertos no autorizan al equipo a inventar reglas de seguridad, dinero,
   datos o experiencia. Deben cerrarse en la spec correspondiente o excluirse de esa entrega.

## Resultado registrado

| Estado | Cantidad | Alcance |
|---|---:|---|
| `confirmed` | 57 | Requisitos funcionales y no funcionales aceptados, incluido `RF-VEN-005` |
| `proposed` | 2 | `RF-COS-001`, `RNF-OPS-001` |
| `superseded` | 12 | Tres requisitos offline y nueve reglas `RN-*` absorbidas en RF/P |

El detalle vinculante queda en [[../../requirements/CAT-REQ-001|CAT-REQ-001 v1.0]].

## Límite de la evidencia

Esta nota registra la validación declarada, pero no sustituye el archivo original de
**Levantamiento de requisitos 1.0**. Si se incorpora el acta al repositorio, debe enlazarse
sin datos personales innecesarios y sin reescribir retroactivamente esta evidencia.
