---
codigo: ZA-CU-003
titulo: Diagramas generales de casos de uso por proceso
version: 1.0
fecha: 2026-10-13
autor: Franklin Acero (tesista)
analista: Codex (asistencia de redacción)
estado: propuesta-interna
fuente: CAT-REQ-001 v1.2
publicacion: no-preparado
---

# ZA-CU-003 — Diagramas generales de casos de uso por proceso

**Estado:** propuesta interna de representación visual, pendiente de revisión.

Este catálogo reúne diagramas UML generales para los procesos principales definidos en el alcance y CAT-REQ-001 v1.2. Los diagramas muestran actores y casos de uso asociados a requisitos confirmados. No sustituyen los casos de uso detallados, historias, especificaciones ni la definición de permisos. No agregan requisitos.

La asistencia se presenta en dos diagramas generales ya incluidos en ZA-CU-002 v1.2. Se agregan los ocho procesos generales restantes. Las etiquetas RF dentro de los óvalos indican trazabilidad, no una decisión adicional de alcance.

**Control documental:** código ZA-CU-003 · Fase 2, catálogo visual general · v1.0 · 13-10-2026 · Franklin Acero / Codex · propuesta interna.

## Historial de revisiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| v1.0 | 2026-10-13 | Catálogo de ocho diagramas nuevos por proceso, trazabilidad RF y dos diagramas generales de asistencia reutilizados de ZA-CU-002 v1.2. | Franklin Acero; redacción asistida por Codex |

## Correspondencia de cobertura

| Diagrama | Requisitos base | Casos de uso representados |
|---|---|---|
| Acceso, membresías y permisos | RF-ACC-001 a RF-ACC-004 | Iniciar y cerrar sesión; Administrar membresías y estado de cuentas; Autorizar operaciones según perfil, cargo y encargo; Consultar inicio y pendientes personales |
| Planificación de actividades y encargos | RF-PLA-001 a RF-PLA-005 | Registrar jornadas y actividades; Asignar responsables y participantes; Gestionar encargo temporal y su cierre; Consultar actividades y pendientes; Planificar producción semanal |
| Producción y trazabilidad | RF-CAT-001; RF-INV-001; RF-TRA-001 a RF-TRA-005 | Mantener materias, productos, unidades y valores históricos; Registrar acopio y pesaje; Registrar secado, temperatura y pesos; Consultar duración y merma; Transformar según receta y conservar lotes de origen |
| Inventario, entregas y conciliación física | RF-INV-002 a RF-INV-006 | Registrar movimientos de existencias; Asignar y confirmar entregas de feria; Conciliar devoluciones y diferencias físicas; Transferir entre custodia individual y organizacional; Consultar alertas de mínimos aprobados |
| Ventas, tesorería y rendición | RF-VEN-001 a RF-VEN-009; RF-GAS-001/002; RF-CXC-001 a RF-CXC-003 | Registrar ventas y aplicar precios vigentes; Registrar ventas de feria, institucionales o contingencia; Registrar gastos y consultar resumen de ingresos; Consultar saldos y registrar abonos; Conciliar encargo de feria y preparar comisiones |
| Reportes, recordatorios y sitio público | RF-REP-001 a RF-REP-006; RF-NOT-001/002; RF-PUB-001 a RF-PUB-003 | Consultar reportes de asistencia y actividades; Consultar reportes de producción, inventario y saldos; Consultar resumen privado y recordatorios; Consultar información pública y precios aprobados; Preparar, aprobar, publicar o retirar contenido |
| Gestión documental y activos | RF-DOC-001; RF-AST-001 | Registrar, consultar y versionar documentos; Recibir avisos internos de vencimiento; Mantener el registro e historial de activos |
| Continuidad y sincronización sin conexión | RF-PWA-001 a RF-PWA-003; RNF-CON-001 | Abrir la experiencia preparada para uso sin red; Guardar asistencia o pesaje habilitado como pendiente; Sincronizar, reintentar y revisar resultados |
| Asistencia: captura, consulta y participación | RF-ASI-001 a RF-ASI-005; RF-ASI-007 | Registrar y consultar asistencia; QR/código; corrección; historial; participación adicional |
| Asistencia: faltas y multas | RF-ASI-006 | Generar falta al cierre; presentar justificación; validar multa por Tesorera |

Los diagramas de asistencia conservan el detalle y notas de su fuente: ZA-CU-002 v1.2.

## ZA-DG-01 — Acceso, membresías y permisos

**Requisitos:** RF-ACC-001 a RF-ACC-004

![ZA-DG-01 Acceso, membresías y permisos](figuras/za-dg-01-acceso-membresias-y-permisos.png)

**Nota de alcance:** Los permisos organizacionales se asignan por operación; el soporte técnico no adquiere autoridad de negocio.

## ZA-DG-02 — Planificación de actividades y encargos

**Requisitos:** RF-PLA-001 a RF-PLA-005

![ZA-DG-02 Planificación de actividades y encargos](figuras/za-dg-02-planificacion-de-actividades-y-encargos.png)

**Nota de alcance:** La planificación no crea lotes ni existencias; los encargos conservan aceptación, cambios y evidencia de cierre.

## ZA-DG-03 — Producción y trazabilidad

**Requisitos:** RF-CAT-001; RF-INV-001; RF-TRA-001 a RF-TRA-005

![ZA-DG-03 Producción y trazabilidad](figuras/za-dg-03-produccion-y-trazabilidad.png)

**Nota de alcance:** El agotamiento de stock no cierra por sí solo un lote. Solo una mezcla física crea un lote derivado.

## ZA-DG-04 — Inventario, entregas y conciliación física

**Requisitos:** RF-INV-002 a RF-INV-006

![ZA-DG-04 Inventario, entregas y conciliación física](figuras/za-dg-04-inventario-entregas-y-conciliacion-fisica.png)

**Nota de alcance:** Las existencias se derivan de movimientos. Custodia individual, propiedad y deuda monetaria se mantienen diferenciadas.

## ZA-DG-05 — Ventas, tesorería y rendición

**Requisitos:** RF-VEN-001 a RF-VEN-009; RF-GAS-001/002; RF-CXC-001 a RF-CXC-003

![ZA-DG-05 Ventas, tesorería y rendición](figuras/za-dg-05-ventas-tesoreria-y-rendicion.png)

**Nota de alcance:** Los precios, saldos, gastos y comisiones conservan sus bases separadas. Los importes no se distribuyen mientras falten reglas aprobadas.

## ZA-DG-06 — Reportes, recordatorios y sitio público

**Requisitos:** RF-REP-001 a RF-REP-006; RF-NOT-001/002; RF-PUB-001 a RF-PUB-003

![ZA-DG-06 Reportes, recordatorios y sitio público](figuras/za-dg-06-reportes-recordatorios-y-sitio-público.png)

**Nota de alcance:** Publicadora autorizada representa un permiso, no un rol adicional. El contenido público debe estar aprobado y no revela datos internos.

## ZA-DG-07 — Gestión documental y activos

**Requisitos:** RF-DOC-001; RF-AST-001

![ZA-DG-07 Gestión documental y activos](figuras/za-dg-07-gestion-documental-y-activos.png)

**Nota de alcance:** El acceso, los tipos documentales, la conservación y los metadatos aún requieren definición antes de implementar datos sensibles.

## ZA-DG-08 — Continuidad y sincronización sin conexión

**Requisitos:** RF-PWA-001 a RF-PWA-003; RNF-CON-001

![ZA-DG-08 Continuidad y sincronización sin conexión](figuras/za-dg-08-continuidad-y-sincronizacion-sin-conexion.png)

**Nota de alcance:** La sincronización revalida sesión, permisos y reglas en servidor; un guardado local no se muestra como aceptación remota.

## Diagramas de asistencia

### Captura, consulta y participación

![Diagrama general UML de asistencia: captura, consulta y participación](../casos-uso/figuras/ZA-CU-ASI-diagrama-registro-consulta.png)

### Faltas y multas

![Diagrama general UML de asistencia: faltas, justificativos y multas](../casos-uso/figuras/ZA-CU-ASI-diagrama-faltas-multas.png)

## Límites y decisiones abiertas

Los procesos se derivan de requisitos confirmados de CAT-REQ-001 v1.2. Los roles se representan con nombres funcionales; no se define aquí la matriz de autorización. Las reglas P-01 a P-14 continúan abiertas donde la línea base las identifica. Antes de tratar estos esquemas como diseño detallado, cada módulo requiere casos de uso completos, revisión de trazabilidad y cierre de decisiones que afecten sus flujos.

**Fuentes:** CAT-REQ-001 v1.2; alcance del proyecto v1.2; ZA-CU-002 asistencia v1.2; diagramas de referencia de 2026-09-28. No se ha modificado el catálogo aprobado ni publicado contenido al repositorio docente.
