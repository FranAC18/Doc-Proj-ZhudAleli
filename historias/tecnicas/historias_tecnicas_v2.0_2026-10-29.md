---
titulo: Historias técnicas: adenda de integridad de datos
version: "2.0"
fecha: 2026-10-29
autor: Codex
estado: propuesto-para-revision
publicacion: pendiente
base: historias_tecnicas_v1.9_2026-10-28.md
fuente: D-24 a D-30; respuestas directas del tesista
---

# Historias técnicas: adenda de integridad de datos

**Edición por adenda:** conserva la [edición base](historias_tecnicas_v1.9_2026-10-28.md) y modifica únicamente lo indicado abajo. No sustituye aprobaciones anteriores ni acredita validación organizacional o académica nueva. Fuente canónica de la propuesta: [enmienda de datos](../../../docs/requirements/proposals/2026-10-29-enmienda-datos-sin-credito-y-administracion.md).

HT-PRE-003 conserva identidad y sprint planificado S1; esta revisión ocurre durante S2 sin reabrir ni cerrar periodos.

| Criterio de salida de HT-PRE-003 | Evidencia propuesta |
|---|---|
| Propietarios y relaciones | Diseño revisión 0.2: lote de materia/producto, cuenta por presentación/ámbito y salida por lote. |
| Integridad | Recetas con nulos, comprobante exclusivo, intervalos y FKs coherentes. |
| Transacciones y concurrencia | Padres existentes y orden de bloqueo; cobro/entrega/rendición separados. |
| Autorización | Matriz rol/operación corregida con D-25/D-28 y pruebas negativas. |
| Pruebas | DAT-01 a DAT-15 definidos; ejecución futura en PostgreSQL por incremento. |

Mantener evidencia de avance y pendientes; definir pruebas no significa ejecutarlas. No añadir una historia técnica ficticia ni declarar HT-PRE-003 terminada.

## Historial de esta edición

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 2.0 | 2026-10-29 | Codex | Adenda solicitada por tesista para corregir diseño de datos; fuentes e impacto descritos arriba. | Revisión pendiente; sin publicación. |
