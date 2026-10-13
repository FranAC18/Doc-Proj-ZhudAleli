---
titulo: Historias técnicas de Zhud Alelí adaptadas al formato de cátedra
version: "1.1"
fecha: 2026-10-12
autor: Codex, para revisión del tesista
estado: candidato-interno
fuentes: "CAT-REQ-001 v1.1; constitución 0.2.0; ADR-0006; material de cátedra 2.9"
historias_tecnicas: 9
prioridad: orden-preliminar-por-validar
estimacion: pendiente-del-equipo
revision_directora: pendiente
publicacion: no-autorizada
---

# Historias técnicas — candidato adaptado al material de cátedra

Las historias técnicas describen trabajos que habilitan o protegen las historias
de usuario. Se expresan **directamente como trabajo técnico**, con título,
descripción, criterios verificables, tareas cuando se justifican, pruebas,
dependencias, estimación y prioridad. No usan la fórmula «Como… quiero…».
Su orden en la pila es preliminar y la estimación queda pendiente del equipo.
Ninguna de estas fichas declara trabajo implementado o probado.

## HT-GEN-008 — Explorar despliegue y recuperación

**Tipo:** exploración técnica. **Prioridad preliminar:** posición 1 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** determinar un entorno viable para ejecutar Django con PostgreSQL,
archivos y acceso seguro, y documentar cómo se comprobarían una publicación y su
recuperación. Es necesario antes de comprometer una entrega piloto.

**Criterios de aceptación:**

1. Existe una evaluación documentada de al menos una opción viable que cubre ejecución de Django, conexión a PostgreSQL, archivos, HTTPS, costos y límites conocidos.
2. El plan identifica comprobaciones previas y posteriores a publicar, riesgos de migración y pasos de recuperación pendientes de validar.
3. Las preguntas de política de respaldo de P-11 quedan registradas sin declarar aprobado `RNF-OPS-001`.

**Tareas:** revisar la factibilidad vigente; probar un entorno mínimo cuando se autorice; registrar decisión y dudas.
**Prueba prevista:** comprobación reproducible de arranque y conexión en el entorno elegido, una vez aprobado.
**Dependencias:** constitución 0.2.0 y ADR-0006; P-11 para la política definitiva.

## HT-GEN-001 — Preparar la base modular Django

**Tipo:** arquitectura e infraestructura de producto. **Prioridad preliminar:** posición 2 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** organizar los módulos Django por responsabilidad y crear el usuario
personalizado antes de la primera migración estable. Cada dato y escritura debe
tener propietario para facilitar los incrementos posteriores.

**Criterios de aceptación:**

1. La configuración inicial define el usuario personalizado antes de aplicar la primera migración estable.
2. Los modelos y migraciones se descubren con los mecanismos nativos de Django y cada módulo creado responde a una necesidad de su especificación.
3. Las dependencias entre módulos creados tienen dirección y propietario documentados, sin ciclos detectados.

**Tareas:** configurar proyecto y base; crear solo el módulo de acceso requerido; verificar migraciones.
**Pruebas previstas:** comprobación Django y aplicación de migraciones en PostgreSQL de prueba.
**Dependencias:** SPEC-001 y ADR-0006. Esta historia habilita `HU-ACC-001`.

## HT-GEN-009 — Preparar pruebas y trazabilidad

**Tipo:** infraestructura del equipo. **Prioridad preliminar:** posición 3 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** establecer cómo se enlazan requisitos, historias, especificaciones,
pruebas y evidencia, y automatizar las comprobaciones disponibles para cada
incremento. Permite revisar lo entregado y detectar regresiones.

**Criterios de aceptación:**

1. Cada historia implementada puede rastrearse hasta su requisito, criterio de aceptación, prueba y resultado real.
2. La verificación automatizada ejecuta las comprobaciones Django, migraciones, pruebas y análisis disponibles cuando exista el proyecto.
3. La revisión de un incremento incluye los recorridos anteriores afectados y registra resultados reproducibles.

**Tareas:** definir matriz de trazabilidad; incorporar comprobaciones conforme exista código; registrar evidencia por incremento.
**Prueba prevista:** ejecutar la secuencia de verificación sobre un incremento real y conservar su resultado.
**Dependencias:** `HT-GEN-001` para comprobaciones de aplicación; constitución 0.2.0.

## HT-GEN-002 — Aplicar autorización en el servidor

**Tipo:** arquitectura y seguridad. **Prioridad preliminar:** posición 4 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** centralizar las comprobaciones de identidad y permisos vigentes
en las operaciones sensibles, incluidas entradas de sincronización, y separar
datos privados de contenido público.

**Criterios de aceptación:**

1. Para cada operación sensible implementada, una prueba permitida confirma el resultado y una denegada demuestra ausencia de cambios.
2. Un acceso directo sin permiso no muestra datos ajenos; el sitio público solo recibe contenido autorizado.
3. Un reintento de sincronización no devuelve a otra cuenta el resultado de una operación privada.

**Tareas:** definir permisos por especificación; aplicarlos en operaciones propietarias; probar accesos directos y reintentos.
**Pruebas previstas:** integración con perfiles, cargos y encargos permitidos y denegados.
**Dependencias:** `HT-GEN-001`, `RNF-SEC-001`, `RNF-PRV-001`; permisos particulares pendientes por funcionalidad.

## HT-GEN-004 — Preparar componentes móviles y accesibles

**Tipo:** infraestructura de producto. **Prioridad preliminar:** posición 5 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** establecer patrones de formularios, mensajes y controles con
Bootstrap 5 y plantillas Django que permitan uso móvil, teclado y lenguaje
comprensible, sin convertir el Django Admin en interfaz principal.

**Criterios de aceptación:**

1. Un recorrido esencial implementado funciona desde 360 px sin desplazamiento horizontal accidental ni controles ocultos.
2. Los controles de ese recorrido tienen etiqueta, foco visible, contraste AA y errores recuperables, comprobados con teclado y zoom al 200 %.
3. Los estados se expresan con texto además de color y no exigen que la socia seleccione permisos técnicos.

**Tareas:** definir patrones compartidos necesarios; aplicarlos a un recorrido real; recoger observaciones de usuarias.
**Pruebas previstas:** revisión de accesibilidad y prueba de recorrido con usuarias cuando haya una versión utilizable.
**Dependencias:** `HT-GEN-001`, `RNF-UX-001`, `RNF-UX-002`, `RNF-UX-003`.

## HT-GEN-003 — Asegurar integridad y auditoría

**Tipo:** arquitectura de datos. **Prioridad preliminar:** posición 16 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** hacer que correcciones, movimientos y operaciones que afectan
varias entidades se confirmen de forma íntegra y con historia suficiente para
reconstruirlas.

**Criterios de aceptación:**

1. Si falla una parte de una operación que debe confirmarse junta, la prueba demuestra que no permanece un cambio parcial.
2. La existencia consultada se deriva de movimientos y una corrección sensible conserva actor, momento, motivo y valores necesarios.
3. Las pruebas de concurrencia de los recorridos afectados no permiten sobreventa ni saldo negativo silencioso.

**Tareas:** fijar propietario de cada dato; definir restricciones y límites transaccionales por funcionalidad; añadir auditoría donde el requisito la exige.
**Pruebas previstas:** integración PostgreSQL, reversión de fallos y concurrencia proporcional al riesgo.
**Dependencias:** `HT-GEN-001`, `RNF-DAT-001`, `RNF-AUD-001`; P-04, P-05 y P-09 para excepciones dependientes.

## HT-GEN-005 — Preparar captura local protegida

**Tipo:** infraestructura de producto. **Prioridad preliminar:** posición 17 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** preparar recursos esenciales y persistir operaciones habilitadas
en el dispositivo como pendientes, aisladas por cuenta y diferenciadas de una
confirmación remota.

**Criterios de aceptación:**

1. En un dispositivo preparado, un flujo habilitado permanece disponible durante un corte de red.
2. Una operación habilitada guardada localmente sigue pendiente tras recargar y no se presenta como aceptada por el servidor.
3. Una cuenta distinta no puede consultar la cola local de otra usuaria.

**Tareas:** precisar acciones y datos mínimos; diseñar almacenamiento y estados; probar corte y cambio de cuenta.
**Pruebas previstas:** recorrido sin red y aislamiento en dispositivo compartido.
**Dependencias:** `HT-GEN-002`, `RF-PWA-001`, `RF-PWA-002`, `RNF-CON-001`; decisiones P-13 y P-14 antes de cerrar el diseño.

## HT-GEN-006 — Sincronizar sin duplicados

**Tipo:** arquitectura e infraestructura de producto. **Prioridad preliminar:** posición 18 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** enviar operaciones pendientes al volver la conexión, reconocer
reintentos y volver a comprobar reglas y permisos en el servidor. El resultado
debe distinguir aceptación, rechazo y conflicto.

**Criterios de aceptación:**

1. Reenviar una operación con la misma identidad después de perder la respuesta produce un único registro.
2. Un permiso revocado o dato inválido causa rechazo sin cambios parciales ni lectura de resultados ajenos.
3. La persona puede distinguir qué operaciones siguen pendientes, cuáles fueron aceptadas y cuáles requieren revisión.

**Tareas:** definir identidad y contrato de operación; aplicar reglas propietarias; probar reintentos, conflictos y revocación.
**Pruebas previstas:** integración con respuesta perdida, reintento y cambio de permisos.
**Dependencias:** `HT-GEN-003`, `HT-GEN-005`, `RF-PWA-003`; P-13 y P-14 para tiempos, orden y conflictos.

## HT-GEN-007 — Generar reportes PDF verificables

**Tipo:** infraestructura de producto. **Prioridad preliminar:** posición 51 de 60.
**Estimación:** pendiente del equipo.

**Descripción:** obtener reportes desde datos autorizados y generar PDF con
periodo, filtros, unidades y totales que puedan conciliarse con su origen.

**Criterios de aceptación:**

1. Un PDF generado contiene título, fecha, periodo, filtros, unidades y totales que coinciden con los registros fuente.
2. La información se entiende sin depender solo del color y no incluye datos fuera del permiso de quien lo solicita.
3. El logo aparece únicamente si se dispone del archivo autorizado.

**Tareas:** definir consultas por reporte; preparar formato común; verificar totales y permisos.
**Pruebas previstas:** comparar PDF con registros conocidos y revisar legibilidad visual.
**Dependencias:** `RNF-PDF-001`, `HT-GEN-002` y datos confirmados de las funciones que cada reporte consulta. Habilita `HU-REP-001` a `HU-REP-005`.

## Límites de esta propuesta

`RNF-OPS-001` y `RF-COS-001` permanecen propuestos. La exploración de despliegue
no decide proveedor ni fija una política de respaldo; P-11 sigue abierto. Las
políticas P-13 y P-14 limitan el cierre de las historias de continuidad. El
material de cátedra aporta **formato y clasificación**; los requisitos y la
arquitectura aprobada aportan el contenido específico de Zhud Alelí.

## Historial de esta edición candidata

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Codex | Primera agrupación técnica interna. | Candidato conservado |
| 1.1 | 2026-10-12 | Codex | Reescritura como enablers con descripción, criterios, pruebas, dependencias, prioridad y estimación pendiente. | Candidato interno |
