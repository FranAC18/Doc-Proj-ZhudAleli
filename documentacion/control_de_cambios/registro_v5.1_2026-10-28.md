---
titulo: Registro de cambios documentales
version: "5.1"
fecha: 2026-10-28
autor: Franklin Acero
estado: preparado-para-revision-academica
publicacion: pendiente-de-transferencia
---

# Registro de cambios documentales v5.1

## Organización modular de backend y frontend

Esta edición incorpora la definición de modularidad aprobada por el tesista el 2026-10-28
a la arquitectura destinada a revisión docente. Se conserva el monolito modular Django,
PostgreSQL, las plantillas renderizadas en servidor y Bootstrap. La aprobación corresponde
a la convención técnica y no acredita nuevos requisitos ni la entrega completa de módulos.

| Documento | Versión | Cambio | Estado |
|---|---:|---|---|
| [Arquitectura detallada](../arquitectura/arquitectura_v1.2_2026-10-28.md) | 1.2 | Añade responsabilidades del backend, frontend por pantalla, recursos compartidos, descubrimiento de plantillas y estáticos, crecimiento proporcional y transición verificable. Actualiza el estado parcial de la app y corrige la descripción de mensajes de acceso conforme a SPEC-001. | Convención técnica aprobada; edición completa preparada para revisión académica y pendiente de transferencia. |
| [Índice documental](../README.md) | 5.1 | Señala la nueva arquitectura, conserva las ediciones anteriores y explicita la diferencia entre diseño aprobado, cambios locales y entrega comprobada. | Actualizado localmente; revisión y transferencia pendientes. |
| Control de cambios | 5.1 | Registra las fuentes y los límites de esta actualización. | Preparado para revisión académica. |

## Contenido incorporado

- Cada módulo de negocio conserva sus datos, operaciones, permisos, presentación y pruebas.
- El backend mantiene modelos, formularios, vistas, rutas y migraciones en ubicaciones
  reconocibles de Django. Servicios, consultas o políticas separados requieren una necesidad real.
- El frontend reúne el HTML y sus recursos exclusivos bajo una carpeta por pantalla. Se
  configuran por separado las plantillas procesadas y los directorios de recursos públicos.
- Los componentes reutilizados mantienen una fuente compartida; las carpetas `css/` y `js/`
  se incorporan cuando agrupan contenido suficiente, sin fragmentación por número de líneas.
- Cada reorganización conserva lógica, permisos, rutas, datos y comportamiento y verifica
  el descubrimiento de recursos, la presentación y la política de caché afectadas.

## Coherencia de fuentes y alcance

La arquitectura v1.1 indicaba que la app no existía. La v1.2 refleja la implementación local
parcial de acceso y la presencia de la adaptación a `frontend/` observada al preparar la
edición. Las pruebas anteriores no se atribuyen automáticamente a la adaptación más reciente;
esta actualización documental no verifica una entrega completa ni un despliegue.

La descripción anterior de mensajes genéricos se ajusta a los criterios vigentes de
SPEC-001: «Usuario incorrecto» para nombres inexistentes o cuentas inactivas y «Contraseña
incorrecta» para clave incorrecta de una cuenta activa. Se corrige la edición académica;
no se introduce una regla de negocio nueva.

Las fuentes son la arquitectura base aceptada, su convención del 2026-10-28, la constitución
vigente, SPEC-001 y la documentación oficial de Django citada en la nueva edición. Los
documentos de requisitos y superadministración conservan sus estados y decisiones pendientes.
No se copiaron bitácoras, instrucciones de agentes, código de producto ni evidencia interna
a la edición destinada al docente.

Se conservan sin cambios [arquitectura v1.1](../arquitectura/arquitectura_v1.1_2026-10-19.md)
y el [control de cambios v5.0](registro_v5.0_2026-10-27.md). Los formatos Word anteriores
no se modificaron. Esta preparación no incluye commit, transferencia ni publicación al
repositorio del docente.

## Verificación editorial

Se comprobaron los metadatos de versión y estado, los enlaces locales dentro de la carpeta
de entrega, la continuidad de las tablas, los bloques Markdown y los espacios de los tres
archivos de esta actualización. Se revisaron las diferencias frente a arquitectura v1.1,
que permanece sin modificaciones. Los diagramas conservados no acreditan implementación;
esta tarea documental no repite las pruebas funcionales del producto.

## Historial

| Versión | Fecha | Cambio |
|---|---|---|
| [5.0](registro_v5.0_2026-10-27.md) | 2026-10-27 | Sincronización de requisitos, historias y pila; línea base y ampliaciones candidatas diferenciadas. |
| 5.1 | 2026-10-28 | Arquitectura v1.2 con organización modular de backend y frontend y actualización del estado local y de la descripción de acceso. |
