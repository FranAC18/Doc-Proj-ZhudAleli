---
title: Catálogo canónico de requisitos v1.0
type: requirement
status: confirmed
id: CAT-REQ-001
version: 1.0
created: 2026-07-22
approved: 2026-07-22
phase: Fase I
sprint: transversal
priority: high
module: transversal
approval_scope: baseline-with-pending-items
confirmed_requirements: 57
proposed_requirements: 2
superseded_requirements: 12
validated_by:
  - Tesista
  - Organización
  - Presidenta
validation_source: Levantamiento de requisitos 1.0
supersedes: CAT-REQ-001-R3
pending_requirements:
  - RF-COS-001
  - RNF-OPS-001
related:
  - "[[proposals/2026-07-22-catalogo-revisado-requisitos-r3]]"
  - "[[../evidence/fase-i/2026-07-22-validacion-cat-req-001-v1]]"
  - "[[../00-inicio/01-decisiones-pendientes]]"
  - "[[../sprints/ROADMAP-ANTEPROYECTO]]"
  - "[[../architecture/ARQUITECTURA-OBJETIVO]]"
  - "[[../ui/SISTEMA-DISENO]]"
  - "[[../traceability/MATRIZ-TRAZABILIDAD]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - estado/confirmado
  - sprint/fase-i
---

# CAT-REQ-001 — Catálogo canónico de requisitos v1.0

## Estado y alcance de la aprobación

Esta es la primera línea base aprobada del catálogo de requisitos de la aplicación para el
Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud y su unidad productiva Zhud Alelí.
Fue validada el 2026-07-22 por el tesista, la organización y la presidenta, con la fuente
declarada **Levantamiento de requisitos 1.0**.

El estado global `confirmed` significa que la línea base y su alcance fueron aceptados. No
convierte en confirmados los dos requisitos identificados como `proposed`, ni resuelve por
sí solo los parámetros abiertos P-01 a P-12. La aprobación tampoco autoriza todavía código,
migraciones o despliegue: cada funcionalidad debe pasar por spec, aclaración, plan y tareas.

## Línea base incorporada

Se incorporan como definición aprobada el actor/problema, la regla, los criterios mínimos y
las fuentes de cada requisito candidato de
[[proposals/2026-07-22-catalogo-revisado-requisitos-r3|CAT-REQ-001-R3]], excepto por los
cambios expresos de este documento. R3 queda congelado como antecedente histórico y no debe
editarse para introducir requisitos nuevos.

Interpretación de la validación recibida:

- `RF-ACC-001-4`, `RF-PLA-001-5` y `RF-ASI-001-6` se interpretan como rangos consecutivos.
- La instrucción “confirmar” bajo los encabezados de Sprint 4, Sprint 5 y requisitos no
  funcionales confirma todos sus candidatos, salvo los dos pendientes nombrados.
- La lista explícita `RF-COS-001, RNF-OPS-001` prevalece sobre el bloque de ejemplo de R3 que
  fue copiado después en la respuesta.
- `RF-VEN-005` queda confirmado como capacidad configurable; sus umbrales y valores siguen
  abiertos en P-08 y no pueden inventarse durante la implementación.
- Las preguntas P-01 a P-12 se conservan como decisiones de detalle. No impiden aprobar el
  catálogo, pero sí bloquean la parte de una spec que necesite el dato aún no resuelto.

## Solución organizacional aprobada

1. Aplicación Django modular, ligera, móvil y principalmente en línea; sin sincronización
   offline automática en la primera versión.
2. Asistencia con entrada y salida separadas, hora del servidor, QR temporal, código
   alternativo y registro delegado auditable.
3. Inconsistencias de asistencia pendientes hasta que la asamblea las resuelva; no existen
   sanciones automáticas ni una ventana automática de tres días.
4. Perfiles Directiva, Socia operaria y Visitante. Los cargos y encargos limitan operaciones;
   el soporte técnico no recibe autoridad organizacional ni permiso de negocio ilimitado.
5. Inventario, lotes, entregas, ventas, devoluciones, pagos y ajustes se registran mediante
   movimientos que conservan historia.
6. Lote productivo cerrado y stock agotado son conceptos distintos. Solo una mezcla física
   crea un lote derivado con procedencia.
7. Las ferias pueden usar stock individual y compartido, identificado por línea de venta.
   No se distribuye automáticamente el excedente compartido sin una decisión aprobada.
8. Custodia física, deuda de una socia, cuenta por cobrar externa y excedente bruto son
   conceptos separados.
9. Ante falta de Internet se utiliza comprobante manual identificable y registro tardío
   auditado, no una promesa de sincronización automática.
10. El sitio público muestra únicamente contenido aprobado y no expone datos internos ni
    afirmaciones sanitarias.

## Ajuste aprobado a RF-ASI-007

**Estado:** `confirmed` con ajuste.

**Regla canónica:** la organización puede habilitar fases QR distintas para entrada y salida.
Cada socia puede autorregistrar su propio evento y la organización acepta el riesgo operativo
de este mecanismo. La secretaria puede supervisar, facilitar un código alternativo o realizar
un registro delegado cuando corresponda. El token es temporal, usa hora del servidor y no
contiene datos personales.

**Criterios mínimos:**

- Un token vencido, repetido o destinado a otra acción no modifica la asistencia.
- El autorregistro identifica a la socia y conserva el origen `self`.
- El registro delegado identifica a la secretaria o persona autorizada, a la socia y el motivo.
- El sistema distingue autorregistro, código alternativo y registro delegado.
- El QR no se presenta como prueba biométrica o infalible de presencia.
- Una inconsistencia queda pendiente para revisión; no genera automáticamente una sanción.

P-02 conserva únicamente los parámetros aún abiertos: duración del token, responsables de
habilitar cada fase y casos autorizados de delegación.

## Requisitos confirmados

Los siguientes 57 IDs tienen estado `confirmed`. Salvo RF-ASI-007, mantienen exactamente la
regla y los criterios mínimos definidos en R3.

| Módulo | IDs confirmados | Cantidad |
|---|---|---:|
| Administración y acceso — S1 | `RF-ACC-001`, `RF-ACC-002`, `RF-ACC-003`, `RF-ACC-004` | 4 |
| Planificación — S2 | `RF-PLA-001`, `RF-PLA-002`, `RF-PLA-003`, `RF-PLA-004`, `RF-PLA-005` | 5 |
| Asistencia y participación — S3 | `RF-ASI-001`, `RF-ASI-002`, `RF-ASI-003`, `RF-ASI-004`, `RF-ASI-005`, `RF-ASI-006`, `RF-ASI-007` | 7 |
| Catálogo, producción e inventario — S4 | `RF-CAT-001`, `RF-INV-001`, `RF-TRA-001`, `RF-TRA-002`, `RF-TRA-003`, `RF-TRA-004`, `RF-TRA-005`, `RF-INV-002`, `RF-INV-003`, `RF-INV-004` | 10 |
| Ventas, gastos, saldos y rendición — S4 | `RF-VEN-001`, `RF-VEN-002`, `RF-VEN-003`, `RF-VEN-004`, `RF-VEN-005`, `RF-VEN-006`, `RF-VEN-007`, `RF-VEN-008`, `RF-GAS-001`, `RF-GAS-002`, `RF-CXC-001`, `RF-CXC-002`, `RF-CXC-003` | 13 |
| Reportes, recordatorios y sitio público — S5 | `RF-REP-001`, `RF-REP-002`, `RF-REP-003`, `RF-REP-004`, `RF-REP-005`, `RF-REP-006`, `RF-NOT-001`, `RF-PUB-001`, `RF-PUB-002` | 9 |
| No funcionales transversales | `RNF-UX-001`, `RNF-UX-002`, `RNF-UX-003`, `RNF-CON-001`, `RNF-SEC-001`, `RNF-AUD-001`, `RNF-DAT-001`, `RNF-PRV-001`, `RNF-PDF-001` | 9 |
| **Total** |  | **57** |

### Catálogo inicial confirmado como estructura

| Categoría | Producto o variante | Tratamiento aprobado |
|---|---|---|
| Shampoo | Atuk sara, cebolla, romero y quinua | Producto elaborado con variantes |
| Acondicionador | Romero | Producto elaborado |
| Horchata o kit de hierbas “Zhud Alelí” | Mezcla de plantas indicada por la organización | Producto con receta/versiones; nombre y composición final se configuran con datos aprobados |
| Mashua seca | Sin variante informada | Producto elaborado o seco |
| Tónico capilar | Romero y cebolla | Producto elaborado con variantes |
| Libro de recetas “Zhud Alelí” | Producto editorial | Inventario comercial sin flujo obligatorio de acopio o secado |
| Kit por contrato | Composición específica del pedido | Versión vinculada al contrato sin alterar la composición estándar |

Gramos y mililitros son unidades informadas. Las presentaciones, conversiones y la lista
cerrada de plantas se completan en P-04 antes de implementar operaciones que las necesiten.

## Requisitos que permanecen propuestos

| ID | Estado | Alcance conservado | Condición para confirmar |
|---|---|---|---|
| `RF-COS-001` | `proposed` | Registrar consumos y costos directos conocidos, sin presentar entradas no valoradas como cero | Resolver P-06: valoración de plantas propias, trabajo comunitario, mano de obra, energía, transporte y gastos compartidos |
| `RNF-OPS-001` | `proposed` | Copias protegidas y restauración demostrable | Resolver P-11: responsables, proveedor, retención, RPO/RTO, frecuencia y autorización de restauración |

Estos IDs no pasan a specs de implementación hasta registrar la decisión faltante. Los demás
requisitos pueden avanzar respetando sus decisiones de detalle.

## IDs históricos sustituidos

| ID anterior | Estado | Sustitución o tratamiento actual |
|---|---|---|
| `RF-OFF-001`, `RF-OFF-002`, `RF-OFF-003` | `superseded` | `RNF-CON-001`, `RF-VEN-008` y contingencia manual para v1 |
| `RN-ACC-001` | `superseded` | Alcance absorbido por `RF-ACC-003`; detalle abierto P-01 |
| `RN-ASI-001` | `superseded` | Alcance absorbido por `RF-ASI-006`; detalle abierto P-03 |
| `RN-ASI-002` | `superseded` | Alcance absorbido por `RF-ASI-007`; detalle abierto P-02 |
| `RN-CAT-001` | `superseded` | Alcance absorbido por `RF-CAT-001`; datos abiertos P-04 |
| `RN-TRA-001` | `superseded` | Alcance absorbido por `RF-TRA-004`; excepciones abiertas P-05 |
| `RN-VEN-001` | `superseded` | Alcance absorbido por `RF-VEN-006`; fórmula abierta P-07 |
| `RN-CXC-001` | `superseded` | Alcance absorbido por `RF-CXC-001`; efectos abiertos P-09 |
| `RN-CON-001` | `superseded` | Alcance absorbido por `RF-VEN-008`; procedimiento abierto P-10 |
| `RN-PUB-001` | `superseded` | Alcance absorbido por `RF-PUB-001` y `RF-PUB-002`; contenido abierto P-12 |

`superseded` conserva la historia y evita duplicar una misma necesidad como dos requisitos
activos. No significa que la pregunta asociada esté resuelta.

## Decisiones de detalle abiertas

| ID | Decisión todavía necesaria | Efecto sobre el avance |
|---|---|---|
| P-01 | Matriz cargo por operación y acceso puntual de soporte | Cerrar antes de aprobar la spec de permisos u operaciones sensibles |
| P-02 | Duración del QR, habilitación de fases y casos de delegación | Cerrar durante la spec de asistencia antes de implementar el QR |
| P-03 | Consecuencias de faltas y autoridad que las decide | No bloquea asistencia; bloquea sanciones automáticas o económicas |
| P-04 | Presentaciones, unidades, conversiones, nombre de horchata/kit y lista de plantas | Cerrar antes de fórmulas y movimientos que requieran conversiones |
| P-05 | Compatibilidades de mezcla/división, bajas, mermas y cierres excepcionales | Cerrar antes de implementar esas excepciones de lote |
| P-06 | Fórmula de costo completo | Mantiene `RF-COS-001` en `proposed` |
| P-07 | Distribución del excedente de stock compartido | No bloquea ventas; bloquea distribución automática |
| P-08 | Umbral, precio/porcentaje, vigencia y límite de cada descuento | `RF-VEN-005` está confirmado; ninguna política se activa sin datos completos |
| P-09 | Efecto de devoluciones, pérdidas, bajas, anulaciones y sobrepagos | Cerrar antes de automatizar esos ajustes monetarios |
| P-10 | Numeración, custodia, digitación, verificación y plazo de contingencia | Cerrar en la spec de feria antes del flujo operativo final |
| P-11 | Política y operación de respaldos | Mantiene `RNF-OPS-001` en `proposed` |
| P-12 | Textos, imágenes, dirección, redes, teléfono y publicadores autorizados | No bloquea estructura; bloquea publicación del contenido final |

## Invariantes aprobadas

1. La autorización vive en backend y toda operación sensible tiene casos permitido y denegado.
2. La auditoría se guarda dentro de la misma transacción que el cambio.
3. Las existencias se derivan de movimientos; no existe un total editable sin evidencia.
4. Una venta multiproducto se aplica completa o se revierte completa.
5. Costo, valor base, precio sugerido y precio aplicado son conceptos distintos e históricos.
6. Un insumo sin valoración produce costo parcial, nunca costo cero silencioso.
7. Lote cerrado y lote agotado son estados distintos.
8. El QR no contiene datos personales y un token inválido no modifica datos.
9. El origen propio o delegado de asistencia siempre queda identificado.
10. El registro tardío conserva folio, momento real, digitación, actor y origen.
11. La interfaz separa custodia, deuda propia, deuda externa y excedente.
12. El sitio público no muestra recursos sin aprobación.

## Control de cambios durante la construcción

La línea base puede evolucionar, pero no se modifica de forma silenciosa:

1. Registrar la necesidad como propuesta de adición, ajuste o retiro, enlazada al ID afectado.
2. Indicar fuente, motivo, impacto en alcance, datos, permisos, UX, pruebas y cronograma.
3. Obtener validación humana proporcional al impacto.
4. Crear una versión identificable de CAT-REQ-001 y actualizar specs, tareas y trazabilidad.
5. Marcar un requisito retirado como `superseded` o `discarded`; no borrar su historia.

Una conversación o una decisión técnica durante la implementación no cambia por sí sola esta
línea base.

## Registro de aprobación

| Fecha | Participantes y roles | Fuente | Resultado | Evidencia |
|---|---|---|---|---|
| 2026-07-22 | Tesista; organización; presidenta | Levantamiento de requisitos 1.0 | 57 `confirmed`, 2 `proposed`, 12 `superseded`; RF-ASI-007 ajustado | [[../evidence/fase-i/2026-07-22-validacion-cat-req-001-v1]] |

## Próxima puerta

Crear specs por funcionalidad únicamente desde los IDs `confirmed`. Antes de implementar una
operación afectada por P-01 a P-12, su spec debe cerrar el dato o excluir expresamente esa
parte del alcance. `speckit-implement` continúa prohibido hasta aprobar la spec y sus tareas.
