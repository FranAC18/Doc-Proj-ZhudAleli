---
titulo: "Criterios y secuencia de acceso y superadministración"
version: "1.4"
fecha: 2026-10-27
autor: Franklin Acero
estado: preparado-para-revision-academica
alcance_aprobacion: "El tesista definió autoridad transversal de Superadministradora en todos los módulos; RF-ACC-005 y operaciones detalladas por módulo permanecen propuestos"
evidencia_validacion_presidencial: "pendiente de adjuntar"
publicacion: pendiente-de-transferencia
fuentes: "Plan de superadministración v1.3; plan de sprints v1.6; CAT-REQ-001 v1.2 y RF-ACC-005 propuesto; SPEC-001 vigente; decisiones expresas del tesista del 2026-10-27"
---

# Criterios y secuencia de acceso y superadministración

El tesista comunicó que la presidenta validó el rol de superadministradora con
autoridad para gestionar el sistema; falta adjuntar la referencia de esa validación.
La decisión de secuencia ubica definición documental en S1 y acceso, cuentas,
superadministración y estructura de permisos en S2. Las operaciones de los módulos de
gestión organizacional y trazabilidad se entregan en S3–S5 según sus requisitos.
Esta edición **define criterios candidatos** para revisión; no aprueba por sí sola
`RF-ACC-005` ni cambia SPEC-001.

## Alcance transversal decidido por el tesista

Una Superadministradora activa puede hacer **todo lo que una usuaria normal puede
hacer en cada módulo**. Además, desde un panel administrativo puede gestionar cuentas
y accesos, crear o corregir registros de asistencia y otros datos operativos,
modificar cantidades y valores, y editar las opciones y parámetros de los campos
existentes que cada módulo publique. Su rol da acceso transversal a esas operaciones:
no requiere asignar individualmente cada módulo a la propia Superadministradora.

«Editar campos» significa cambiar el **valor de campos existentes** en un registro o
configurar sus opciones permitidas, como catálogos, rangos o fórmulas cuando el módulo
las ofrezca. El panel no crea campos físicos, columnas o tablas ni cambia el esquema de
la base de datos. Si una función o campo aún no existe, se incorpora mediante desarrollo
del módulo y, cuando corresponda, migración y pruebas. El panel no es el Django Admin
ni una consola de acceso directo a tablas.

Cada módulo conserva sus validaciones, restricciones de datos, aprobaciones aplicables
y dueño de escritura. Los cambios históricos se corrigen mediante rectificaciones
trazables; la Superadministradora no borra auditoría ni altera silenciosamente el
origen. El acceso se verifica en servidor y cada acción sensible conserva actor,
fecha, recurso, resultado y motivo cuando corresponde. Las excepciones sobre datos
personales sensibles se precisan con la organización.

## Criterios verificables propuestos para S2

| ID | Criterio y prueba de aceptación | Dependencia |
|---|---|---|
| SA-S2-01 | Una persona autorizada crea una cuenta interna y se comprueba unicidad y estado inicial; una persona sin permiso no crea cuentas. No hay autorregistro. | Alta inicial según SA-S2-08. |
| SA-S2-02 | Se puede activar o desactivar otra cuenta con permiso; una cuenta inactiva no inicia sesión y sus registros permanecen. Al desactivarla se cierran de inmediato todas sus sesiones abiertas; se comprueba con dos sesiones. | Autorización detallada de la operación pendiente. |
| SA-S2-03 | Se concede o retira acceso a un módulo concreto; cada operación consulta el permiso vigente en servidor. Revocar acceso administrativo cierra de inmediato todas las sesiones abiertas; se comprueba con dos sesiones. | Regla de delegación y alcance del módulo. |
| SA-S2-04 | El panel prepara navegación para todos los módulos previstos y muestra a la Superadministradora las operaciones ya publicadas. Una URL o petición directa sin autoridad es denegada sin mostrar datos privados ni cambiar registros. | Operaciones concretas se añaden con cada módulo. |
| SA-S2-05 | Altas, cambios de estado y permisos registran actor, fecha, acción, recurso, resultado y motivo cuando corresponde. El panel no edita auditoría. | Retención y lectura de auditoría. |
| SA-S2-06 | La política de acceso muestra valores actuales; cambios sin permiso, sin motivo o fuera de límites validados son rechazados. Un cambio aceptado registra valor anterior, nuevo y vigencia. | Validar rangos y actualizar SPEC-001 antes de habilitar cambios. |
| SA-S2-07 | Una recuperación nunca muestra la contraseña anterior; identidad, caducidad, uso único y auditoría se prueban antes de aceptar el flujo. | Canal y autoridad aún no definidos; fuera del incremento hasta validar. |
| SA-S2-08 | Durante la instalación, el tesista designa la primera superadministradora solo con autorización registrada de la presidenta. El procedimiento es reproducible y los atributos técnicos de Django no conceden autoridad organizacional. | Decidido por el tesista; constancia y formato de autorización pendientes antes del alta. |

El cierre de S2 exige recorridos permitidos y denegados, migraciones reproducibles en
PostgreSQL, regresión de SPEC-001 y evidencia de autorización. Una pantalla o tabla
creada no satisface por sí sola los criterios. El mapa de módulos y permisos prepara
S3–S5; no representa funcionalidades de negocio construidas.

## Criterios candidatos para cada módulo de S3–S5

| ID | Resultado observable | Prueba mínima |
|---|---|---|
| SA-MOD-01 | La Superadministradora puede ejecutar cada acción ordinaria del módulo sin asignación individual. | Comparar una acción permitida de usuaria normal con la misma acción de Superadministradora y una petición de cuenta sin permiso. |
| SA-MOD-02 | Puede crear o corregir asistencia, cantidades, valores y otros registros que el módulo ofrezca, mediante sus formularios y reglas. | Guardar un caso válido; rechazar duplicado o valor inválido; comprobar original, rectificación y auditoría. |
| SA-MOD-03 | Puede editar opciones, catálogos, parámetros y valores de campos existentes que el módulo declare configurables. | Cambiar un valor válido; rechazar uno fuera de rango; consultar valor anterior, nuevo, actor y vigencia. |
| SA-MOD-04 | Una necesidad de campo u operación nueva se canaliza como cambio del módulo con migración y pruebas cuando aplique. | El panel rechaza cambios de estructura y código arbitrario; las opciones visibles corresponden a funciones implementadas. |

Estos criterios se completan con el catálogo exacto de operaciones y reglas de cada
módulo al construirlo. La autoridad transversal no convierte en implementadas las
funciones de S3–S5.

La trazabilidad académica de esta propuesta está en [requisitos generales v2.1](../requisitos/requisitos_generales_v2.1_2026-10-27.md),
[historias de usuario v2.6](../historias/usuario/historias_usuario_v2.6_2026-10-27.md)
y [pila de producto v1.8](../pila_producto/pila_producto_v1.8_2026-10-27.md).

## Reglas que se conservan y decisiones pendientes

- SPEC-001 conserva tres fallos en tres minutos, bloqueo de tres minutos, sesión de
  30 minutos de inactividad y sus mensajes de error específicos aprobados. El tesista
  decidió mantenerlos; la propuesta posterior de mensajes genéricos queda descartada.
- El tesista designará la primera autoridad durante la instalación con autorización
  de la presidenta registrada. Se debe precisar quién delega o revoca después y cómo
  se transfiere la autoridad cuando cambia la presidencia.
- La desactivación de cuenta y la revocación de acceso administrativo cierran de inmediato
  todas sus sesiones abiertas, por decisión del tesista. Las operaciones verifican el
  permiso vigente en servidor. El tratamiento del estado de una PWA sin conexión sigue
  pendiente antes de habilitar administración fuera de línea.
- La Superadministradora accede transversalmente a las vistas y operaciones que cada
  módulo publique. La organización debe precisar excepciones para datos personales
  sensibles. Cada módulo declara sus catálogos, fórmulas, correcciones y responsables
  antes de implementarlos. No hay cambio de esquema, borrado del historial ni ejecución
  de código arbitrario desde el panel.
- Los rangos de política, la recuperación de cuenta, la visibilidad de intentos y
  la retención de auditoría requieren validación antes de habilitar esas funciones.

## Calendario y estado

El periodo de S1 llegó al 27 de octubre por decisión del tesista; sus pendientes
conservan su estado. S2 ya estaba en curso y su **cierre propuesto** es el 8 de
noviembre. El detalle actualizado está en el [plan de sprints
v1.6](plan_sprints_v1.6_2026-10-27.md). La capacidad comunicada de 16–25 horas
semanales no equivale a horas comprometidas por tarea. Este documento está preparado
localmente para revisión académica; no se ha transferido ni publicado.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| [1.2](plan_implementacion_superadmin_v1.2_2026-10-27.md) | 2026-10-27 | Plan S1/S2 aprobado por el tesista, con fechas comunicadas antes de la replanificación. | Edición anterior conservada. |
| [1.3](plan_implementacion_superadmin_v1.3_2026-10-27.md) | 2026-10-27 | Se añaden criterios de aceptación candidatos de S2 y se sincroniza el calendario propuesto S2–S5. | Edición anterior conservada. |
| 1.4 | 2026-10-27 | Se incorpora la autoridad transversal en todos los módulos, con edición de registros, valores y opciones desde el panel y sin cambio de esquema; criterios por módulo S3–S5. | Preparado para revisión académica; no publicado. |
