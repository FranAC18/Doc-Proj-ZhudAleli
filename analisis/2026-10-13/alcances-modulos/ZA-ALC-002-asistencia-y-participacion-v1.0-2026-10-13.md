---
codigo: ZA-ALC-002
titulo: Alcance del módulo de asistencia y participación
modulo: Asistencia y participación
fase: Fase 1 — Documento de alcance del módulo
version: 1.0
fecha: 2026-10-13
autor: Franklin Acero (tesista)
analista: Codex (asistencia de redacción)
estado: propuesta-para-revision
publicacion: no-preparado
prioridad_modulo: siguiente-por-importancia
related:
  - "[[../../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13]]"
  - "[[../../../documentacion/requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13]]"
  - "[[../../../documentacion/historias/usuario/historias_usuario_v2.5_2026-10-13]]"
  - "[[../../../docs/requirements/CAT-REQ-001]]"
  - "[[ZA-ALC-001-acceso-usuarias-y-roles-v1.1-2026-10-13]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - sprint/s4
  - modulo/asistencia
---

<table style="width:100%;border-collapse:collapse;font-family:'Heebo Light',Heebo,Arial,sans-serif;">
<tr><td colspan="2" style="background:#642138;color:#F0EAC8;padding:14px;font-family:'Mallong Regular',Georgia,serif;font-size:22px;"><strong>[LOGO: Isotipo floral de 4 pétalos - ZHUD ALELÍ Productos Naturales]</strong><br>ZA-ALC-002 · Alcance del módulo de asistencia y participación</td></tr>
<tr><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Control documental</th><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Valor</th></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Módulo</td><td style="padding:7px;border:1px solid #AC6E40;">Asistencia y participación (<code>attendance</code>)</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Fase / entregable</td><td style="padding:7px;border:1px solid #AC6E40;">Fase 1 — Documento de alcance del módulo</td></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Versión / fecha</td><td style="padding:7px;border:1px solid #AC6E40;">v1.0 / 13 de octubre de 2026</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Autor / analista</td><td style="padding:7px;border:1px solid #AC6E40;">Franklin Acero (tesista) / Codex (asistencia de redacción)</td></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Estado</td><td style="padding:7px;border:1px solid #AC6E40;">Propuesta interna para revisión; no aprobada ni publicada</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Criterio de orden</td><td style="padding:7px;border:1px solid #AC6E40;">Siguiente módulo por importancia: cuatro RF esenciales, un RF alto y dos complementarios</td></tr>
</table>

**Historial de revisiones**

| Versión | Fecha | Descripción | Responsable |
|---|---|---|---|
| v1.0 | 2026-10-13 | Se establece el alcance modular de asistencia y participación a partir de RF-ASI-001 a RF-ASI-007 y la prioridad aprobada. | Franklin Acero; redacción asistida por Codex |

## 1. Propósito y descripción general del módulo

El módulo **Asistencia y participación** registra la entrada y salida de las socias en actividades organizacionales, conserva correcciones e inconsistencias para revisión, y distingue la asistencia de otras formas de participación. También registra automáticamente las faltas al cierre de una actividad, recibe justificaciones dentro del plazo acordado y mantiene la validación de multas a cargo de la Tesorera como paso previo a su aplicación.

El alcance incluye siete requisitos funcionales confirmados: cuatro esenciales, uno de importancia alta y dos complementarios. La selección de este módulo después de Acceso se basa en su mayor concentración de requisitos esenciales. La planificación de actividades es una dependencia: sus registros son el contexto de la asistencia, pero su administración pertenece al módulo de planificación.

## 2. Objetivos de negocio y alineación con Zhud Alelí

- Mantener registros verificables de asistencia, separados por entrada y salida, socia y actividad.
- Evitar registros duplicados y no inventar horas, salidas ni datos que no se hayan capturado.
- Permitir que las personas autorizadas corrijan registros conservando motivo e historial.
- Registrar una falta automáticamente cuando cierre la actividad y no exista asistencia válida de una participante asignada.
- Dar a la socia hasta tres días hábiles para presentar una justificación, con el evento inicial del cómputo todavía pendiente de precisión.
- Separar el registro de una falta de una multa; la Tesorera valida la procedencia de la multa antes de que se aplique.
- Facilitar la participación organizacional con captura móvil y controles comprensibles, sin exponer el historial de otras socias.
- Conservar la continuidad de los recorridos de asistencia habilitados sin presentar una captura local como aceptación definitiva del servidor.

## 3. Entregables clave y funcionalidades incluidas

| ID de requisito | Funcionalidad incluida | Importancia aprobada | Límite o condición |
|---|---|---|---|
| RF-ASI-001 | Registrar entrada y salida como eventos separados, con hora del servidor cuando hay conexión, socia, actividad y origen del registro. Una captura sin conexión permanece provisional. | Esencial | La aceptación tardía y las reglas completas offline dependen de P-13 y P-14. |
| RF-ASI-002 | Evitar duplicados por socia, actividad e instancia de evento; conservar inconsistencias para revisión. | Esencial | No completar una salida olvidada con una hora inventada. |
| RF-ASI-003 | Corregir registros sensibles mediante Directiva o encargada autorizada, con motivo e historial auditable. | Esencial | La matriz específica de permisos se concreta en la especificación del módulo. |
| RF-ASI-004 | Consultar historial propio de asistencia y permitir consultas de Directiva según autorización y periodo. | Complementaria | Cada consulta respeta privacidad y permisos. |
| RF-ASI-005 | Registrar participación adicional únicamente cuando la actividad necesite un dato distinto de la asistencia. | Complementaria | Una actividad simple no exige datos de participación adicionales. |
| RF-ASI-006 | Al cerrar la actividad, registrar automáticamente una falta para cada participante asignada sin asistencia válida; admitir justificación dentro de un máximo de tres días hábiles; conservar la revisión y validación de la Tesorera antes de aplicar multas. | Esencial | Falta y multa son estados distintos. El inicio del plazo, canal, decisión del justificativo, redondeo, impugnación y cobro siguen sujetos a P-03. |
| RF-ASI-007 | Habilitar captura con QR para fases distintas, alternativa de código y registro delegado auditable; el token temporal no contiene datos personales. | Alta | P-02 debe precisar duración, responsables y delegaciones; QR offline depende de P-13. |

**Entregables de análisis para la siguiente fase:** especificación de casos de uso por recorrido; historias y escenarios de aceptación trazados a estos siete RF; matriz de decisiones abiertas y dependencias; criterios de permiso, auditoría, privacidad y continuidad que correspondan a cada flujo.

## 4. Exclusiones explícitas

- Crear, modificar o cerrar actividades, jornadas, participantes, encargos o planes de producción; estos datos pertenecen al módulo de planificación.
- Administrar cuentas, membresías o perfiles de acceso; pertenece a Acceso (`accounts`). Este módulo consume su autorización.
- Aplicar una multa sin la validación de la Tesorera, ni automatizar cobro, recaudación o descuentos.
- Definir por inferencia el inicio del plazo de tres días hábiles, el canal de justificación, quién acepta o rechaza un justificativo, el método de redondeo o el procedimiento de impugnación; son precisiones abiertas de P-03.
- Aceptar un QR vencido, reutilizado o destinado a otra fase; definir la duración definitiva de QR o nuevos tipos de delegación antes de resolver P-02.
- Declarar definitiva una operación capturada offline o diseñar una política de conflictos, caducidad o sincronización no aprobada; se precisará con P-13/P-14.
- Enviar recordatorios externos por WhatsApp, SMS, correo u otro proveedor. Cualquier comunicación externa requiere alcance y autorización propios.
- Generar reportes generales de gestión o integrar cálculos económicos y cierres de caja.

## 5. Restricciones, supuestos y dependencias técnicas

### 5.1 Restricciones y supuestos

- La aplicación aún no está implementada; este documento delimita el alcance y no afirma que exista una función operativa.
- El producto previsto es una aplicación web Django modular con PostgreSQL, plantillas Bootstrap 5 y uso móvil. El módulo no introduce una arquitectura diferente.
- La autorización se comprueba en el servidor, incluso ante solicitudes directas. Las denegaciones no alteran datos.
- Correcciones, validaciones y excepciones conservan actor, fecha, autorización, motivo y valores previos/nuevos cuando corresponda.
- Las operaciones que guardan conjuntamente asistencia, falta, justificación o validación y su auditoría conservan integridad atómica.
- Las reglas de interfaz deben atender móvil desde 360 px, lenguaje cotidiano, accesibilidad y recuperación comprensible de errores.
- Las cantidades comunicadas para sanciones se conservan como aparecen en la fuente general; el módulo no completa reglas de cálculo o cobro que continúan abiertas en P-03.

### 5.2 Dependencias

| Dependencia | Relación con el módulo | Resolución requerida |
|---|---|---|
| Planificación (`planning`) / RF-PLA-001 | Proporciona la actividad y su periodo de asistencia. | La actividad debe estar vigente y tener sus participantes definidos antes de registrar asistencia. |
| Acceso (`accounts`) / RF-ACC-001 a RF-ACC-003 | Proporciona identidad, estado de membresía y autorización de cada operación. | Reutilizar las reglas de autorización existentes; el módulo no define roles universales. |
| P-02 | Limita QR, fases y delegación. | Precisarlo antes de cerrar la especificación e implementar QR. |
| P-03 | Limita la resolución de justificativos y consecuencias monetarias. | No automatizar sanciones ni cobros con los detalles pendientes. |
| P-13 y P-14 | Limitan captura, tiempo, QR y sincronización offline. | Precisar reglas de aceptación y reconciliación antes de tratar capturas locales como definitivas. |
| RNF transversales | Seguridad, auditoría, integridad, privacidad, accesibilidad y continuidad. | Aplicarlos a cada flujo, prueba y artefacto de diseño del módulo. |

**Estado de validación:** los requisitos funcionales y su importancia constan en las ediciones vigentes aprobadas por el tesista. La revisión académica de la directora y la validación directa de la organización que corresponda aún deben registrarse; los detalles abiertos de P-02, P-03, P-13 y P-14 no se consideran resueltos por este alcance.

## 6. Trazabilidad y fuentes

- [[../../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13|Requisitos generales v2.0]]: redacción actual de RF-ASI-001 a RF-ASI-007, estado y decisiones de detalle.
- [[../../../documentacion/requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13|Priorización v1.3]]: nivel de importancia aprobado para cada requisito.
- [[../../../documentacion/historias/usuario/historias_usuario_v2.5_2026-10-13|Historias de usuario v2.5]]: actores, criterios y sprint propuesto de los recorridos de asistencia.
- [[../../../docs/requirements/CAT-REQ-001|CAT-REQ-001]]: fuente canónica de estado y decisiones abiertas.
- [[ZA-ALC-001-acceso-usuarias-y-roles-v1.1-2026-10-13|ZA-ALC-001 v1.1]]: alcance del módulo predecesor y contrato de autorización.

**Aprobación pendiente:** confirmar este alcance antes de avanzar a la Fase 2 (casos de uso detallados). El registro no modifica requisitos confirmados ni publica una edición en `documentacion/`.
