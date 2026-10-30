---
title: Revisión de normalización e integridad del modelo de datos
type: architecture-review
status: proposed
date: 2026-10-30
author: Codex por solicitud del tesista
scope: esquema-actual-y-modelo-logico-v2.1
task_reference: SB-S1-03 / HT-PRE-003
implementation: no-realizada
---

# Revisión de normalización e integridad

## Dictamen

El diseño separa adecuadamente muchas entidades del negocio, pero **todavía no permite afirmar que todo el modelo está en tercera forma normal (3FN)**. Hay redundancias identificables, claves naturales por precisar y diferencias entre las reglas escritas y los atributos/cardinalidades del ER. La prioridad es completar esas garantías antes de traducir el diagrama a migraciones.

La base implementada es una base técnica de autenticación, no la implementación del modelo integral. Sus tablas pequeñas de identidad, contactos y contadores tienen una estructura razonable; `AuthChallenge` conserva una dependencia redundante condicionada por la existencia de contacto. No se detectaron datos inconsistentes en la consulta efectuada; las tablas sin registros no permiten demostrar que las reglas funcionen con datos ni bajo concurrencia.

Este informe contiene observaciones y propuestas técnicas. No aprueba cambios de requisitos ni sustituye las ediciones v2.1. No se modificaron código, tablas, registros, migraciones ni estados de requisitos o sprint.

## Alcance y evidencia

Fuentes locales revisadas:

- [ER integral v2.1](../../../documentacion/arquitectura/modelo_er_integral_v2.1_2026-10-30.md), paneles A–F.
- [Base lógica v2.1](../../../documentacion/arquitectura/diseno_base_datos_v2.1_2026-10-30.md), reglas C01–C18 e integridad.
- [Catálogo confirmado](../../requirements/CAT-REQ-001.md), en particular asistencia, invariantes y decisiones abiertas.
- [Consolidación de reglas](../../requirements/proposals/2026-10-30-consolidacion-reglas-diseno-datos.md), conservando su estado propuesto y las discrepancias con el catálogo.
- `app/apps/accounts/models.py`, `services.py`, migraciones `0001`–`0003`, pruebas de modelos/contactos y configuración de conexión.
- Constitución 2.0.0 y arquitectura objetivo: propietario por módulo, transacciones e historial.

Consulta directa del 30/10/2026, usando la conexión de desarrollo dentro de una transacción PostgreSQL `READ ONLY`:

| Verificación | Resultado |
|---|---|
| Motor | PostgreSQL 18.4 |
| Tablas físicas | 13: cinco modelos propios de accounts, dos uniones de usuario y seis tablas de Django/auth |
| Migraciones aplicadas / pendientes | 18 / 0 |
| Usuarios / contactos / desafíos | 1 / 0 / 0 |
| Desafíos con contacto de otra cuenta | 0; no hay desafíos cargados |
| Grupos de contactos verificados duplicados por tipo y `lower(trim(value))` | 0; no hay contactos cargados |
| Usuarios con `email` no vacío | 0 |
| Restricciones inspeccionadas | PK, FK, unicidad, índices y nulabilidad de usuario, contacto y desafío |

No se imprimieron identidades, contactos, contraseñas, tokens ni credenciales de conexión. El agrupamiento SQL por `lower(trim())` es una comprobación acotada; no demuestra equivalencia con todo el `casefold()` de Python.

Corte Git: general `8dfe3141c71c3bae2ff21b12e3aab1d0d17817c9`, rama `docs/requisitos-y-organizacion-del-vault`; app `d208fba3e347bf2fffae1f91ff178a1d33414249`, rama `feature/RF-ACC-001-base-proyecto`. Se encontraron cambios locales previos en ambos repositorios. El HEAD general difiere del registrado en el estado activo; se usa el observado para este informe. Los cambios previos se conservaron.

## Evaluación de las formas normales

La normalización se determina por tabla, claves candidatas y dependencias funcionales, no por el número de tablas ni por tener un campo `id`. Una clave candidata es una combinación mínima de atributos que identifica un registro según el negocio.

| Nivel | Evaluación del proyecto |
|---|---|
| 1FN | Los campos de negocio mostrados son escalares; contactos, líneas e insumos están separados. No se observan columnas repetidas como `producto_1`, `producto_2`. Las sesiones serializadas de Django se tratan como infraestructura. |
| 2FN | La estructura es favorable, pero faltan claves candidatas explícitas en varias entidades propuestas. Una PK artificial no elimina por sí sola dependencias parciales respecto de otras claves candidatas. |
| 3FN | No puede certificarse globalmente. `presentacion_id → product_id` en la línea comercial repite una dependencia del catálogo; `contact_id → user_id` se repite en desafíos con contacto, si ambos identifican al mismo propietario. |
| FNBC | No evaluable de manera completa sin las dependencias y claves naturales. No hay evidencia que justifique exigir una normalización superior para todo el sistema. |

La 3FN exige revisar dependencias transitivas y atributos que describen otra entidad; [Cornell presenta este criterio y un ejemplo de descomposición](https://cvw.cac.cornell.edu/RelationalDBs/design-create/third_normal_form). El dictamen anterior aplica ese criterio a las reglas específicas del proyecto.

No toda repetición entre tablas demuestra una violación formal: puede tratarse de una referencia a la misma entidad, una clave alternativa, un hecho diferente o una copia histórica deliberada. Las dependencias con nulos o condicionadas por el tipo requieren analizar la rama correspondiente; no equivalen automáticamente a una prueba clásica de 3FN para toda la tabla SQL.

## Hallazgos del esquema implementado

### N01 — Propietario repetido en AuthChallenge — prioridad alta

Evidencia: `models.py:98–99` guarda usuario y contacto; el contacto ya tiene usuario (`models.py:67`). Las FK físicas son independientes. El servicio normal crea el desafío con `user=contact.user` (`services.py:94–99`), pero la base admite una pareja cruzada por otra ruta.

Dependencia en desafíos con contacto: `contact_id → ContactChannel.user_id`. Si `AuthChallenge.user_id` significa ese propietario, se está almacenando el mismo hecho por dos caminos.

Propuesta: para una tabla exclusivamente de desafíos de contacto, derivar usuario del contacto. Si también admite desafíos de cuenta sin contacto, mantener esa capacidad y evaluar subtipos o una FK compuesta `(contact_id, user_id)` hacia una clave única `(id, user_id)` del contacto. Conservar los campos y añadir una garantía resuelve integridad, aunque mantiene la redundancia. Una validación de formulario o servicio aislada no equivale a una restricción de base. Validar también qué propósitos exigen contacto.

### N02 — Unicidad del contacto y normalización textual — prioridad alta

Evidencia: las restricciones actuales comparan `(user,type,value)` y, para verificados, `(type,value)` de forma exacta. El servicio normaliza correo con `strip().casefold()` y busca colisiones con `iexact`. Esos contratos no son idénticos para todos los valores ni quedan impuestos a SQL directo o escrituras que eviten el servicio.

Propuesta: establecer una representación canónica por canal y hacer coincidir normalización, comparación y unicidad. Un índice de expresión puede servir para una regla simple de correo; si se adopta un valor canónico persistido, garantizar su cálculo y su coherencia. No agregar otra columna como copia editable sin control. Mantener formato internacional canónico para teléfono y no inventar equivalencias entre direcciones de distintos proveedores. Probar dos verificaciones concurrentes y la respuesta al conflicto de unicidad.

### N03 — Dos lugares posibles para correo — prioridad media

`User` hereda `email`; `ContactChannel` guarda correo con estado de verificación. Hoy no hay datos poblados en ninguno. Es una duplicación potencial entre entidades, no una inconsistencia observada.

Propuesta: que el canal verificado sea la fuente de verdad del contacto usado para acceso/avisos. Definir el uso de `User.email` y de las integraciones Django antes de poblarlo. No sincronizar ambos como campos editables independientes ni eliminar el heredado sin revisar consumidores. Si luego hay varias direcciones, definir selección o preferencia cuando el recorrido lo requiera.

### N04 — Digest global único de códigos de seis cifras — prioridad media

`services.py:48–50` calcula HMAC solamente sobre el código; `issue_contact_challenge` genera seis cifras y `AuthChallenge.token_digest` es globalmente único. Repetir el mismo código, incluso para otra cuenta o frente a un desafío histórico, produce el mismo digest y puede causar `IntegrityError`. No se observó un incidente; se deduce del código. No es una colisión criptográfica del HMAC, sino reutilización de un espacio pequeño de códigos.

Propuesta: ligar el digest al identificador/nonce del desafío y conservar consumo único, expiración y límites de intentos. Revisar si el digest necesita unicidad global cuando el flujo ya identifica el desafío por PK. Agregar una prueba determinista con el mismo código emitido a dos desafíos independientes. No debilitar la protección del código almacenado.

## Campos repetidos y redundancias del modelo lógico

| ID / prioridad | Datos involucrados | Diagnóstico y propuesta |
|---|---|---|
| N05 / alta | `LINEA_COMERCIAL.presentation_id` y `product_id` | La presentación ya identifica el producto. Una línea podría apuntar a presentación de shampoo y producto de colada. Preferir una sola referencia a la identidad vendible. Si se conserva producto por necesidad demostrada, imponer coherencia; no mantener dos selecciones libres. |
| N06 / media | `ACEPTACION_CUOTA.person_id` y beneficiaria de `quota_id` | Si persona significa beneficiaria, es derivable y debe coincidir. Si significa quien manifestó el acuerdo, nombrar y modelar ese papel expresamente y separar de quien registra la evidencia. No convertir un registro de acuerdo verbal en una firma atribuida falsamente. |
| N07 / media | `CUSTODIA.custodian_person_id` y persona de `assignment_id`; cuota y asignación representativa | Hay dos caminos hacia la persona. Definir si necesariamente coinciden o representan responsabilidades distintas. Si coinciden, derivar o restringir. En cuotas, documentar claves candidatas antes de afirmar una violación formal de 3FN; la redundancia puede afectar FNBC según las claves. El ER enlaza custodia con ENCARGO, mientras el atributo dice asignación: corregir esa ambigüedad. |
| N08 / media | Fechas de `ACTIVIDAD` y de `FERIA` | Es correcto conservar horario de feria distinto del de la actividad si tiene significado operativo. Si son exactamente el mismo hecho, elegir una fuente. No sincronizar dos pares editables sin semántica. |
| N09 / alta | `LOTE.quantity`, movimientos y linaje/consumos | Definir `quantity` como cantidad original producida/recibida, no saldo mutable. El stock disponible procede de movimientos. Linaje y consumos deben nacer de la misma operación; no dos registros independientes del mismo consumo. En procesos con varias entradas y salidas, precisar si el linaje expresa asociación o asignación cuantitativa para evitar multiplicar cantidades. |

La tabla siguiente identifica repeticiones que conviene conservar o delimitar:

| Datos | Tratamiento recomendado |
|---|---|
| Dueña, vendedora y registradora | Conservar separados: C03 distingue beneficiaria económica, ejecutora de venta y actor del sistema. Pueden coincidir sin ser el mismo papel. |
| Precio/base aplicados y política vigente al vender | Conservar historia y procedencia. No recalcular una venta con el precio actual. Distinguir versión de tarifa y precio realmente pactado. |
| Cantidad, precio y total de línea | El total es calculable si la fórmula está cerrada. Calcular en consulta o persistir como importe histórico validado e inmutable; documentar redondeo. No ofrecer tres valores independientes. |
| Total de liquidación y fondo de reparto | Son agregados o instantáneas de cierre. Justificar persistencia por versión y enlazar el desglose; no tratarlos como saldos editables paralelos. |
| Aprobación, aceptación y pago | Conservar como hechos distintos. Una autorización no demuestra que el dinero se haya entregado. |
| LoginThrottle y AuthAttempt | Usan alcances y ventanas distintos en el código. Su parecido no demuestra duplicidad accidental. No unificar solo por compartir campos. |
| Stubs de entidades repetidos en paneles ER | Referencian la misma entidad; no crean varias tablas de usuario, persona o producto. |

## Brechas de negocio y cardinalidad

### N10 — Una ausencia no puede depender de un marcaje existente — prioridad alta

El ER exige `FALTA.attendance_id → REGISTRO_ASISTENCIA`. El catálogo confirmado, sección «Solución organizacional aprobada», punto 3, y RF-ASI-006 exigen crear faltas para participantes sin asistencia válida. Si no hubo marcaje, no hay registro al cual apuntar.

Propuesta: que la falta se origine en la participante convocada y el cierre/evaluación de la actividad. Un marcaje puede ser evidencia opcional para atraso u otro caso. No crear una asistencia ficticia para satisfacer la FK. Definir unicidad por origen y tipo sin multiplicar multas. También falta explicitar el tipo entrada/salida de fase/marcaje y la rama manual/delegada sin QR; validar que participante y fase correspondan a la misma actividad.

### N11 — Variante y condición del stock incompletas — prioridad alta

VARIANTE se relaciona con producto y kit, pero no aparece una identidad de variante consistente en presentación, lote terminado y venta. Dos variantes podrían resultar indistinguibles en catálogo comercial o mezclarse en existencias si solo se usa producto/presentación. Definir una identidad vendible que distinga variante y tamaño de envase; enlazar los lotes correspondientes y evitar almacenar producto/variante/presentación incompatibles.

La descripción de CUENTA_EXISTENCIAS exige unidad y condición vendible/segregada, pero su bloque de atributos solo muestra lote, presentación, titular, feria y tipo de custodia. Es una diferencia documental, no una columna física perdida: el modelo todavía es propuesto. Completar esos atributos y la clave natural. Permitir cuentas de materia prima/granel sin presentación envasada cuando corresponda; el diagrama actual dibuja presentación obligatoria para toda cuenta.

RECEPCION_SEGREGADA apunta a una cuenta que exige lote, aunque C11 permite recibir un artículo con lote no verificable. Modelar recepción física pendiente de identificación y su vinculación posterior a inventario segregado; no inventar lote u origen para hacer pasar una FK.

### N12 — Anticipos antes de la liquidación — prioridad alta

La regla C05 permite entregar dinero durante la jornada. Sin embargo, APLICACION_RENDICION solo muestra `settlement_id`; la liquidación nace al cierre. El ER omite el vínculo a periodo/fuente anunciado en la base lógica.

Propuesta: identificar desde el comienzo el movimiento y su periodo; al cerrar, aplicar ese mismo dinero a la obligación con trazabilidad y límite de importe. Precisar la relación entre FUENTE_LIQUIDACION y LIQUIDACION: no basta compartir un periodo con varias socias; debe poder reconstruirse qué fuente satisface qué obligación y quién rinde cuando dueña y vendedora difieren. No crear un segundo ingreso para representar el anticipo ya recibido.

### N13 — Cobro, dinero y aplicaciones sin unión suficiente — prioridad alta

COBRO contiene importe/medio/estado, mientras MOVIMIENTO_DINERO también contiene importe/estado y el texto admite tipo cobro. El ER no muestra un enlace que permita saber si son el mismo hecho monetario. Además, vincula cada cobro a una sola línea, aunque la base lógica describe aplicaciones y un compromiso comercial puede contener varios productos.

Propuesta: elegir una única representación del dinero recibido y modelar su aplicación a líneas o documento. Si COBRO es subtipo de MOVIMIENTO_DINERO, enlazarlo 1:1 y no permitir que los importes discrepen. Un pago de varios productos no debe multiplicarse al repartirlo entre líneas. Precisar también la FK entre ejecución y ORDEN_REEMBOLSO, que aparece como relación pero no como atributo en el bloque de movimiento. Las rendiciones internas son transferencias del dinero cobrado, no otra venta ni ingreso comercial.

### N14 — Capturas agregadas e idempotencia — prioridad alta

La arista `CAPTURA_PROVISIONAL ||--o| REGISTRO_COMERCIAL` expresa una captura por registro incorporado y no representa varias capturas que alimentan un resumen; tampoco permite registros digitales sin captura como origen en esa relación. Falta el vínculo de incorporación descrito en la base lógica.

Propuesta: expresar captura → línea/resumen destino mediante una FK o una entidad de incorporación, según se permita o no dividir una captura. Cada captura se contabiliza una vez; el resumen y su evidencia no generan dos ventas. La clave de sincronización y el digest deben cubrir actor/tipo/UUID y contenido según el contrato, con resultado persistido atómicamente. Un UUID único aislado no resuelve la conciliación ni valida stock compartido.

### N15 — Cardinalidad de cuenta/persona invertida — prioridad media

La relación escrita es `ACCOUNTS_USER o|--|| PERSONA_ORGANIZACIONAL`. En notación Mermaid representa una persona por cuenta y cero/una cuenta por persona, contrario al texto. La intención descrita es una cuenta obligatoria para cada persona y cero/una persona asociada para una cuenta externa: `ACCOUNTS_USER ||--o| PERSONA_ORGANIZACIONAL`. En físico: `account_user_id NOT NULL UNIQUE` y FK. No fijar seis socias ni siete cuentas mediante restricciones.

### N16 — Tarifa, kit y conversiones requieren claves semánticas — prioridad alta

- VERSION_VALOR no muestra `tipo` base/precio, aunque la base lógica lo exige. Sin esa distinción, la vigencia por presentación no permite dos valores simultáneos de naturaleza distinta. Explicitar tipo y no solapar intervalos dentro de cada clave.
- KIT_LOTE.reference_liters puede ser una propiedad de especificación/versión del kit, no de cada lote de proveedor. Si es común, ubicarla en su definición y referenciarla; si cambia por lote, documentar ese hecho. Los 50 L son referencia por kit, no rendimiento real garantizado.
- CONVERSION_UNIDAD guarda factores por pareja. Eso permite factores incompatibles por diferentes caminos. Para conversiones multiplicativas simples kg/g y L/mL, evaluar factor a unidad base por magnitud y derivar las parejas. No convertir masa en volumen sin información física adicional; esa capacidad no está autorizada por C16.

### N17 — Claves naturales y restricciones por definir — prioridad alta

El ER utiliza PK artificiales, pero no enumera todas las restricciones de negocio. Propuestas mínimas a concretar en el diseño físico:

| Entidad | Restricción o clave candidata a verificar |
|---|---|
| Participante | Única por actividad y persona/cuenta participante, según población permitida. Usar persona si el padrón es obligatorio; no permitir por accidente la cuenta externa. |
| Cargo / membresía / perfil | Fechas coherentes e intervalos sin solape según la regla de exclusividad de cada vínculo; una fila vigente no basta para impedir solapes históricos. |
| Versión de receta/documento/reparto | Unicidad de entidad propietaria y número de versión; indicar cuándo una revisión sustituye otra. |
| Receta e insumo | Definir si un mismo insumo puede aparecer en etapas distintas antes de imponer unicidad receta/insumo. |
| Feria | `activity_id UNIQUE` si una actividad define como máximo una feria. |
| Cuenta de existencias | Lote + presentación/unidad + propiedad/custodia + titular + feria + condición; nulos equivalentes y ramas válidas. Separar custodia física de propiedad económica. |
| Línea/salidas | Todas las cuentas abastecedoras compatibles con identidad vendible, dueña y origen de la línea. |
| Cuota | Una beneficiaria por versión, coherente con asignaciones elegibles y fuentes de cálculo. |
| Fuente de liquidación | Exactamente línea o decisión de faltante; vinculación inequívoca a obligación y consumo de origen sin doble liquidación entre periodos/versiones. |
| Caso de ajuste | Orígenes excluyentes por tipo; responsable económico explícito cuando la decisión lo requiera. |
| Publicación | Una revisión efectivamente publicada por ítem; publicar una versión no publica automáticamente las demás. |

Una tabla genérica de estados no sustituye el catálogo de cada dominio. Para conjuntos fijos pequeños, `TextChoices` y CHECK pueden ser suficientes; para opciones configurables/versionadas, usar catálogo propio. No crear catálogos sin responsabilidad real ni almacenar listas de roles en una columna.

### N18 — Identidad institucional y autoría — prioridad media

RF-VEN-007 exige identificación mínima de venta institucional y excluye excedente individual. El bloque de registro solo muestra tipo detalle/resumen y el de línea vendedora/dueña/origen. Falta explicitar modalidad institucional y la identificación necesaria, sin hacer obligatorio un comprador en ventas ordinarias ni inventar un CRM.

Las decisiones, concesiones y cierres deben referenciar al actor real y registrar autoridad usada. Cuando sea relevante, enlazar la designación/concesión que acreditaba esa autoridad en ese instante. Cambiar un cargo hoy no debe cambiar la autoría histórica. La Superadministradora externa puede registrar o sustituir una operación autorizada sin convertirse en la socia vendedora.

## Reglas transaccionales que la normalización no resuelve

Una base en 3FN aún puede vender dos veces la última unidad o pagar dos veces una cuota. Para el proyecto se necesitan, además:

1. Stock: movimientos confirmados atómicos, bloqueo de una cuenta/entidad existente y clave idempotente; capturas provisionales conflictivas conservadas como incidencias.
2. Venta: documento multiproducto atómico, pago completo antes de entrega y salidas compatibles con stock y titularidad.
3. Dinero: suma de aplicaciones no mayor que el movimiento; transferencias pendientes no saldan; reembolso ejecutado no mayor que lo autorizado.
4. Cierre: fuentes congeladas, anticipos aplicados una vez, incidencias resueltas y versiones pagadas preservadas.
5. Reparto: sumar cuotas exactamente al fondo, redondear según C18 y separar aceptación de pago.
6. Historia: FK protegidas en hechos económicos, sin borrado en cascada desde personas/productos hacia historia financiera. La caducidad de datos técnicos de autenticación tiene otra política.

PostgreSQL permite FK compuestas, restricciones de exclusión e igualdad de nulos mediante `NULLS NOT DISTINCT`. Los agregados entre filas no deben implementarse con un CHECK ordinario: requieren un diseño transaccional y, cuando proceda, garantías adicionales de base. [Documentación PostgreSQL 18](https://www.postgresql.org/docs/18/ddl-constraints.html).

Los validadores y `clean()` de Django tampoco se ejecutan automáticamente en todo `save()`. Una validación de formulario no demuestra protección de SQL directo ni de otros escritores. [Referencia de modelos Django 5.2](https://docs.djangoproject.com/en/5.2/ref/models/instances/#validating-objects).

## Orden recomendado y verificación

Este orden es una propuesta de corrección técnica; no cambia prioridades ni compromisos del sprint:

1. En el incremento de acceso, atender N01–N02 y N04; fijar la fuente de correo N03.
2. Antes de migrar asistencia, resolver N10 y N15, población participante y restricciones temporales.
3. Antes de inventario/comercio, completar identidad vendible/variante, cuenta segregada, tarifa y origen productivo: N05, N09, N11 y N16.
4. Antes de flujos económicos, cerrar relaciones de cobro/aplicación/anticipo/fuente: N12–N14 y N17.
5. Verificar el recorrido institucional, autoría y vigencias; conservar las decisiones de negocio aún pendientes como tales.

Casos mínimos para demostrar las correcciones cuando se implementen:

- Desafío de usuario A con contacto de B rechazado; mismo código aleatorio permitido en desafíos independientes sin pérdida de seguridad.
- Contacto equivalente intentado simultáneamente por dos cuentas: solo una verificación efectiva según la regla vigente.
- Participante sin ningún marcaje: falta real creada al cierre, sin inventar asistencia ni sanción automática sin validación.
- Venta con presentación/producto o variante incompatibles: rechazada; dos variantes mantienen lotes y stock identificables.
- Anticipo antes del cierre: una sola entrada monetaria, correctamente aplicada después de liquidar.
- Un pago aplicado a varias líneas: su importe total no se multiplica; reintento no genera otro cobro ni otra salida.
- Varias capturas incorporadas a un resumen: unidades e importes suman una sola vez.
- Artículo devuelto sin lote verificable: recepción segregada pendiente de identificación, sin origen ficticio ni stock vendible.
- Dos ventas concurrentes de última unidad: una sola confirma stock; cierre/reparto reintentado no duplica pagos.

No se ejecutaron pruebas de producto durante esta revisión ni se añadieron pruebas: no hubo implementación. Se inspeccionaron pruebas existentes y se realizaron consultas de esquema/conteos de solo lectura. `git diff --check` pasó en ambos repositorios antes de registrar el informe; los avisos de conversión LF/CRLF corresponden a archivos locales previos.

## Límites de la conclusión

El ER v2.1 es un diseño lógico con bloques resumidos, no un DDL completo: las omisiones señaladas son cuestiones por resolver/documentar antes del esquema físico, no defectos ya desplegados. Las restricciones implementadas se contrastaron con PostgreSQL; las del negocio futuro no existen todavía.

El catálogo confirmado conserva reglas históricas sobre perfiles, excedentes y saldos que difieren de la consolidación del 30/10. Esta última reconoce esa discrepancia y la evidencia organizacional pendiente. Se puede evaluar su consistencia técnica, pero no atribuirle una aprobación organizacional nueva ni automatizar reglas contradictorias sin reconciliar la fuente específica.

No hay una necesidad demostrada de rehacer toda la base ni de añadir tablas para cada dato. La propuesta es conservar las separaciones útiles, eliminar referencias redundantes sin significado propio y completar claves, relaciones y transacciones por módulo.
