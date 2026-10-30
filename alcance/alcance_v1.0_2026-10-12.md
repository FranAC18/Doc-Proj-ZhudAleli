---
titulo: Alcance del proyecto Zhud Alelí
version: "1.0"
fecha: 2026-10-12
autor: Tesista
estado: final-aprobado-por-tesista
fuente_principal: "CAT-REQ-001 v1.1"
aprobacion_editorial: 2026-10-12
revision_directora: pendiente
validacion_organizacional_de_ajustes_v1_1: no-registrada
publicacion: pendiente-de-confirmacion
---

# Alcance del proyecto

## Propósito y límite de esta edición

El proyecto busca desarrollar una aplicación web para la gestión organizacional y la
trazabilidad productiva del Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud.
La primera versión comprende las capacidades respaldadas por los **51 requisitos
funcionales y 9 no funcionales confirmados** en CAT-REQ-001 v1.1. Este documento
resume sus límites; no confirma que la aplicación esté construida o probada.

La línea base v1.0 fue validada por el tesista, la organización y la presidenta.
Los ajustes v1.1 fueron aprobados por el tesista el 2026-09-28. No consta una
nueva validación de la organización ni revisión de la directora para esos ajustes.

## Personas y uso previstos

| Grupo | Uso previsto |
|---|---|
| Directiva | Organiza actividades, administra información y consulta resultados según cargo y permisos. Presidenta, tesorera y secretaria son cargos organizativos, no cuentas técnicas separadas por defecto. |
| Socias operarias | Consultan lo propio y registran las tareas que les corresponden. Una socia puede recibir un encargo temporal de producción o feria. |
| Visitantes | Ven únicamente información pública aprobada. |

El soporte técnico no obtiene por ese solo hecho autoridad organizacional. Cada
operación privada requiere autorización según perfil, cargo o encargo.

## Capacidades incluidas en la primera versión

| Bloque | Incluye | Referencias de requisitos | Sprint previsto |
|---|---|---|---|
| Acceso y administración | Inicio y cierre de sesión, cuentas, permisos y un inicio privado comprensible. | RF-ACC-001 a 004 | 1 |
| Planificación | Jornadas, actividades, responsables, encargos temporales, consultas y producción semanal planificada. | RF-PLA-001 a 005 | 2 |
| Asistencia y participación | Entrada y salida, consulta y corrección auditada, resolución de inconsistencias, QR temporal y código alternativo. | RF-ASI-001 a 007 | 3 |
| Catálogo, producción e inventario | Materias primas, productos y unidades; acopio, secado, lotes, transformación, existencias, entregas y conciliación física. | RF-CAT-001; RF-TRA-001 a 005; RF-INV-001 a 004 | 4 |
| Ventas y rendición | Ventas individuales, compartidas e institucionales; descuentos configurables, gastos, deudas diferenciadas, abonos, feria y contingencia manual. | RF-VEN-001 a 008; RF-GAS-001 a 002; RF-CXC-001 a 003 | 4 |
| Información y reportes | Reportes de actividades, asistencia, producción, inventario y saldos; resumen privado, recordatorios internos y sitio público con contenido aprobado. | RF-REP-001 a 006; RF-NOT-001; RF-PUB-001 a 002 | 5 |
| Continuidad con conectividad limitada | Interfaz esencial disponible tras preparar el dispositivo, guardado local de operaciones habilitadas y sincronización posterior sin duplicados; asistencia y pesajes son el mínimo identificado. | RF-PWA-001 a 003; RNF-CON-001 | Transversal, especialmente 3 y 4 |

Los nueve requisitos no funcionales atraviesan estos bloques: uso móvil y accesible,
lenguaje comprensible, continuidad, seguridad, auditoría, integridad de datos,
privacidad y PDF claros. Las capacidades de la tabla representan alcance aprobado,
no especificaciones detalladas ni avance de construcción.

## Límites y exclusiones

- No se incluye la gestión ni la afirmación de cumplimiento de registro sanitario.
- No se aplican sanciones automáticas por asistencia. Las inconsistencias esperan
  decisión organizacional registrada; las consecuencias siguen en P-03.
- No se calcula el costo completo mientras P-06 siga abierto ni se distribuye
  automáticamente el excedente de stock compartido mientras P-07 siga abierto.
  El excedente bruto de una venta no se presenta como utilidad neta.
- `RF-COS-001` (registro de consumos y costos directos conocidos) y
  `RNF-OPS-001` (copias protegidas y restauración demostrable) permanecen
  propuestos y no integran los 60 requisitos confirmados.
- Los recordatorios aprobados son internos. Esta edición no incorpora avisos por
  correo o mensajería externa como obligación.
- El sitio público no muestra contenido sin aprobación ni datos internos. P-12
  impide publicar su contenido final hasta definirlo.
- El comprobante manual de feria es una contingencia; no reemplaza el guardado y
  la sincronización sin conexión exigidos para los flujos habilitados. Tampoco
  autoriza por sí solo ventas digitales offline.

## Decisiones que deben cerrarse antes de ciertas funciones

| Grupo | Pendiente | Efecto |
|---|---|---|
| P-02 y P-03 | Parámetros del QR y consecuencias de faltas. | Precisar la especificación de asistencia; no inventar sanciones. |
| P-04 y P-05 | Unidades, presentaciones, plantas y excepciones de lotes. | Precisar conversiones y movimientos que dependen de esos datos. |
| P-06 a P-09 | Costos, reparto compartido, descuentos y ajustes monetarios. | Mantener `RF-COS-001` propuesto y no activar reglas económicas sin valores aprobados. |
| P-10 y P-11 | Comprobante manual y respaldos. | Cerrar el procedimiento de feria; conservar respaldos como propuestos. |
| P-12 | Contenido y responsables del sitio público. | No publicar contenidos finales sin aprobación. |
| P-13 y P-14 | Operaciones habilitadas sin red, tiempos, dispositivo, conflictos y retención. | Completar especificaciones de captura y sincronización antes de implementar esos detalles. |

P-01 está cerrado para el acceso básico; los permisos de otras operaciones se
detallan en sus respectivas especificaciones. La especificación confirmada
SPEC-001 cubre solo una primera porción de acceso, no todo el Sprint 1.

## Criterio de cierre del alcance

Se podrá considerar entregado cada bloque cuando sus funciones aprobadas tengan
especificación, implementación y pruebas verificables, respetando las decisiones
pendientes que le afecten. Esta edición no declara entregas realizadas ni fija
por sí mismo cambios en el catálogo de requisitos.

## Fuentes de esta edición

- CAT-REQ-001 v1.1 y su catálogo R3 incorporado.
- D-001 a D-011 y decisiones P-01 a P-14.
- SPEC-001, alcance de acceso básico.
- Contexto del proyecto y roadmap del anteproyecto.

## Historial de esta edición

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Tesista | Síntesis editorialmente aprobada de alcance, exclusiones y decisiones abiertas. | Final del tesista; revisión de directora pendiente |
