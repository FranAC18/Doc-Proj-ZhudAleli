---
title: Revisión de simplicidad y contexto organizacional del modelo de datos
type: architecture-proposal
status: proposed
date: 2026-10-29
author: Codex / Antigravity
task_id: SB-S1-03
technical_story: HT-PRE-003
scope: evaluacion-simplicidad-y-contexto
module: transversal
related:
  - "[[2026-10-29-diseno-integral-base-datos]]"
  - "[[2026-10-29-decisiones-pendientes-diseno-datos]]"
  - "[[2026-10-29-identidad-cargos-encargos]]"
  - "[[2026-10-29-mapa-conceptual-modulos-y-dependencias]]"
  - "[[../../bitacora/checkpoints/2026-10-29-modelo-datos-correspondencia-nombres-pre-commit]]"
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[../../../documentacion/arquitectura/arquitectura_v1.2_2026-10-28]]"
tags:
  - proyecto/tesis
  - tipo/decision
  - modulo/transversal
  - contexto/organizacional
---

# Revisión de Simplicidad y Contexto Organizacional del Modelo de Datos

> Referencia de trabajo actual — 2026-10-30: [consolidación de datos v2.0](../../../documentacion/arquitectura/diseno_base_datos_v2.0_2026-10-30.md). Este archivo conserva el antecedente; las reglas incompatibles sobre Superadministración, devoluciones, reparto, rendición periódica, contingencia offline y kits están sustituidas. Las decisiones no modificadas conservan su evidencia.

- **Fecha:** 2026-10-29
- **Organización comunitaria:** Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud (Cañar, Ecuador)
- **Marco metodológico:** Monolito modular (PostgreSQL + Django 5.2), arquitectura aprobada en ADR-0006 y diseño integral en español.

**Revisión 0.2:** esta nota evalúa una propuesta, no tablas ni pantallas de negocio implementadas. D-24 a D-30 corrigen crédito, alcance administrativo y secado. Las afirmaciones incompatibles del corte anterior se sustituyen abajo; requisitos aprobados y evidencia de organización se conservan en sus fuentes.

---

## 1. Propósito de esta revisión

El Comité de Mujeres Indígenas “Tránsito Amaguaña” de Zhud gestiona la producción agroecológica comunitaria de plantas medicinales, infusiones (horchata, té medicinal) y derivados. Sus socias operarias poseen baja familiaridad con herramientas informáticas complejas y acceden al sistema mediante teléfonos móviles particulares en condiciones de conectividad intermitente.

El software no debe ser una carga burocrática ni un laberinto técnico que cree dependencia perpetua del tesista o de una persona administradora externa. Por tanto, esta nota evalúa el modelo conceptual y físico propuesto frente a la realidad operativa del Comité, formula propuestas de simplificación (sin alterarlas de facto) y separa claramente los hechos documentados de las hipótesis pendientes de validación comunitaria.

---

## 2. Evaluación de los 10 Criterios Organizacionales

### 2.1 Accesibilidad para personas con baja familiaridad tecnológica
- **Evidencia del vault:** La mayoría de las socias interactúan mediante escaneo QR, confirmación con botones táctiles grandes y notas físicas en papel (RF-ASI-001, RF-VEN-008). No navegan tablas complejas ni administran claves complejas.
- **Análisis del modelo:**
  - El modelo separa el registro en papel (`trazabilidad_comprobante_manual`) del ingreso al sistema, permitiendo que en ferias rurales la socia anote el recibo físico y se digite posteriormente sin presiones de tiempo en el campo (D-14, D-21).
  - La autenticación multicanal (passkeys con huella/rostro en `accounts_credencial_passkey` y código numérico temporal vía WhatsApp en `accounts_authchallenge`) evita que las socias recuerden contraseñas alfanuméricas complejas (SPEC-003, RF-ACC-006/007).
- **Riesgo detectado:** El exceso de catálogos y clasificaciones en pantallas cotidianas puede abrumar. La interfaz debe seleccionar valores predeterminados sensatos y no forzar elecciones de múltiples menús en tareas de campo.

### 2.2 Sostenibilidad del sistema sin dependencia del tesista
- **Principio constitucional:** El sistema debe sostenerse por la Presidenta, Tesorera, Secretaria y socias una vez terminada la tesis.
- **Análisis del modelo:**
  - El diseño propone precios, montos y parámetros en tablas versionadas; las invariantes, autorizaciones y clases de fórmula permanecen en código revisado. Las tablas propuestas incluyen (`asistencia_version_regla_multa`, `trazabilidad_version_valor`, `trazabilidad_version_regla_reparto_feria`, D-17).
  - Los futuros formularios permitirán modificar parámetros aprobados con versiones y auditoría. Una nueva fórmula, permiso o tipo de operación puede requerir desarrollo y revisión; no existe evidencia de esos formularios implementados.
- **Salvaguarda:** Las relaciones operativas sensibles usan FKs explícitas. Las bitácoras del módulo sí proponen localizadores tipo/ID para historia; estos no sustituyen integridad referencial ni autorización de los registros operativos.

### 2.3 Minimización de datos y privacidad (RNF-PRV-001)
- **Principio:** No almacenar cédulas, direcciones exactas de domicilios, datos biométricos en bruto ni datos financieros ajenos sin justificación estricta.
- **Análisis del modelo:**
  - `accounts_credencial_passkey` almacena únicamente la clave pública y el `credential_id` generado por el dispositivo; la biometría permanece en el enclave seguro del teléfono de la usuaria.
  - `trazabilidad_comprador` admite la figura de comprador anónimo mediante el código universal `publico_general`, sin obligar a registrar nombres ni contactos de clientes en ventas al contado de feria (RF-VEN-002).
  - Se eliminaron del diseño columnas no sustentadas en requisitos, tales como `codigo_socia` o `datos_adicionales`.

### 2.4 Trazabilidad sin sobrecarga operativa ni digitación excesiva
- **Tensión detectada:** Exigir registrar cada pesada parcial o cada movimiento físico puede paralizar las jornadas de acopio y secado.
- **Solución del modelo:**
  - El acopio (`trazabilidad_acopio`) registra el ingreso por socia en la recepción diaria de plantas.
  - Cada secado (`trazabilidad_lote_secado`) referencia **un solo acopio**, conforme D-26, y conserva peso inicial/final. El diseño enlaza consumo del lote húmedo y resultado seco sin mezclar acopios. La merma se deriva de pesajes; peso final mayor queda en revisión. Las tolerancias no se inventan (RF-TRA-002/003, P-05).
  - En feria, la venta individual puede registrarse por producto y cantidad; el sistema congela el precio unitario y deriva el total sin que la vendedora calcule multiplicaciones complejas.

### 2.5 Roles reales y autoridad comunitaria vs superadministración técnica
- **Jerarquía legítima:** La autoridad suprema emana de la Asamblea y la Directiva elegida (Presidenta, Secretaria, Tesorera). D-25/D-28 delimitan Superadministradora como administración de cuentas, permisos y parámetros y correcciones auditadas; no ejecuta ni aprueba operaciones de negocio. SPEC-002 aún conserva una regla transversal incompatible, registrada en la enmienda propuesta.
- **Traducción en el modelo:**
  - `accounts_designacion_cargo`: Administra los cargos estatutarios. Solo la Presidenta vigente puede autorizar la concesión o revocación de una Superadministradora (`accounts_concesion_superadministracion`, D-19).
  - La Presidenta resuelve justificativos (D-11) y la Tesorera decide impugnaciones de multas (D-18). Superadministradora no vende, no obtiene cuota por ese rol y no firma aprobaciones de negocio; se retira la hipótesis de autoaprobación de una comisión (D-25/D-28).

### 2.6 Reglas de feria y liquidación del fondo común (D-04 a D-09, D-14, D-21, D-22)
- **Fórmula comunicada por el tesista (D-05), con validación organizacional pendiente según el registro de decisiones:**
  $$\text{Fondo común} = \text{Ventas cobradas de stock compartido} - \text{Valor base de esas líneas} - \text{Gastos comunes de la asociación}$$
- **Estructura de datos correspondiente:**
  - `trazabilidad_reparto_feria`: Contiene la cabecera de la liquidación, garantizando que si el fondo común resulta negativo o cero, no se liquida comisión y la diferencia queda registrada como pérdida de la asociación pendiente de conciliar.
  - `trazabilidad_cuota_reparto_feria`: Refleja la cuota de cada encargada de feria. Se aplican las modalidades aprobadas (igualitaria o proporcional al valor compartido vendido) y la regla de centavos por mayor resto y desempate por encargo menor (D-09).
  - `trazabilidad_conciliacion_feria`: Documenta el cierre físico y monetario conjunto entre la socia encargada de feria y la Tesorera (D-22).

### 2.7 Faltas y justificaciones con la Presidenta como autoridad estatutaria (D-11, D-18, D-23)
- **Regla del estatuto:** Quien no asiste a una minga o reunión obligatoria incurre en falta. Solo la Presidenta evalúa los justificativos presentados en el plazo de 3 días hábiles.
- **Estructura en el modelo:**
  - `asistencia_caso_falta`: Representa el expediente de la falta.
  - `asistencia_justificativo`: Vincula el motivo presentado por la socia y la decisión formal tomada exclusivamente por la Presidenta (`resuelta_por_id FK accounts_user`, `decision_id FK`).
  - `asistencia_multa` e `asistencia_impugnacion_multa`: La multa requiere validación de Tesorera. La socia presenta su impugnación ante la **Tesorera**, quien decide caso por caso un monto entre cero y el original, con motivo/evidencia; mientras esté abierta no se cobra. Los justificativos de falta corresponden a la Presidenta. No se inventa un plazo de pago (D-11/D-18).

### 2.8 Compras y ventas individuales de excedentes vs compartidas (D-02, D-05)
- **Distinción comunitaria clave:** La organización transfiere producto a custodia de socias para venta individual y puede destinar stock compartido a feria. La entrega en custodia no transfiere propiedad por inferencia ni crea deuda; la socia rinde después de vender (D-27).
- **Mapeo:**
  - `trazabilidad_cuenta_existencia`: Clasifica las cuentas en patrimoniales (`patrimonial_asociacion`), de feria compartida (`custodia_feria`) o de custodia personal (`individual_socia`).
  - La venta de stock individual atribuye el excedente (`precio_venta - costo_base`) íntegramente a la socia titular y no forma parte del fondo común divisible de la feria (D-04).
  - La vista `trazabilidad_vista_cierre_mensual_socia` expone a cada socia el desglose transparente de sus ventas individuales, su base adeudada a la asociación y su cuota recibida de ferias.

### 2.9 Catálogos y parámetros versionados (D-17)
- **Principio:** No admitir cambios de reglas que alteren retroactivamente transacciones pasadas.
- **Mapeo:**
  - Cada política de precios (`trazabilidad_version_valor`), recetas (`trazabilidad_version_receta`), políticas de login (`accounts_version_politica_login`) y reglas de multas (`asistencia_version_regla_multa`) posee `numero_version`, `vigente_desde` y `vigente_hasta NULL`.
  - Cuando la Asamblea de Zhud aprueba un nuevo valor, se cierra la versión vigente y se inserta una nueva fila; las ventas y multas del año anterior conservan intacta la referencia a la regla con la que fueron causadas.

### 2.10 Contingencia offline y sincronización idempotente (D-15, D-20)
- **Realidad de campo:** En el páramo o en recintos feriales remotos no hay señal celular estable.
- **Mapeo:**
  - `asistencia_recibo_sincronizacion`, `trazabilidad_recibo_sincronizacion` y `trazabilidad_recibo_sincronizacion_venta`: Permiten recibir cargas en cola desde IndexedDB utilizando `operacion_cliente_id uuid` y `resumen_carga bytea` (hash SHA-256).
  - Si una socia reintenta la sincronización al volver la señal, la restricción `UNIQUE(usuaria_id, operacion_cliente_id)` garantiza que no se dupliquen ventas ni asistencias (idempotencia estricta).
  - La hora declarada en el teléfono (`declarada_en`) se almacena separada de la hora de recepción en el servidor (`recibida_en`) para auditoría de desfases horarios.

---

## 3. Propuestas de Simplificación No Aplicadas (Para Futuros Sprints)

> [!NOTE] Criterio de Gobierno
> Las siguientes alternativas no se aplican al diseño actual. No hay tablas físicas de estos módulos verificadas. D-24 a D-30 prevalecen sobre los supuestos incompatibles anteriores; cualquier simplificación conserva sus invariantes.

| Propuesta de Simplificación | Tablas Involucradas | Impacto Operativo y Técnico Positivo | Riesgo o Motivo de Aplazamiento |
|---|---|---|---|
| **P-SIMP-01: Fusión de Perfil en Membresía** | `accounts_tipo_perfil`, `accounts_asignacion_perfil` → `accounts_membresia` | Reduciría 2 tablas a una simple columna `tipo_perfil` en la membresía de la socia. Simplifica el alta de socias a un solo formulario. | Aplazada porque el diseño actual contempla la figura de visitantes no socias (`visitante`) que podrían no tener membresía comunitaria. |
| **P-SIMP-02: Consolidación de Recibos Offline** | `asistencia_recibo_sincronizacion`, `trazabilidad_recibo_sincronizacion`, `trazabilidad_recibo_sincronizacion_venta` → `nucleo_recibo_sincronizacion` | Evita duplicar 3 tablas de estructura casi idéntica para idempotencia en distintos módulos. | Aplazada para mantener la estricta autonomía modular establecida en ADR-0006 (§4 de arquitectura), donde cada app posee sus propias escrituras y migraciones. |
| **P-SIMP-03: Fusión de Líneas de Receta en Receta Maestra** | `trazabilidad_version_receta` + `trazabilidad_insumo_receta` | Para mezclas tradicionales simples (ej. horchata estándar con proporciones fijas), podría manejarse con un campo estructurado si no hay variabilidad frecuente de ingredientes. | Aplazada porque RF-TRA-004 y P-04 exigen controlar el consumo exacto de materia prima por lote para deducir mermas y costos de acopio. |
| **P-SIMP-04: Eliminación de Categorías Jerárquicas Separadas** | `trazabilidad_categoria_materia_prima` y `trazabilidad_categoria_producto` | Unificar en un catálogo genérico de categorías `trazabilidad_categoria_item`. | Aplazada para evitar mezclar las taxonomías botánicas de plantas cosechadas con las líneas comerciales de producto terminado (infusiones, pomadas, extractos). |

---

## 4. Glosario de Términos Organizacionales de Zhud Alelí

Para evitar tecnicismos ajenos a la comunidad, el modelo y la interfaz adoptan el siguiente vocabulario aprobado:

1. **Acopio:** Recepción y pesaje de la materia prima vegetal entregada por las socias en el centro de acopio comunal.
2. **Lote de Secado:** Masa homogénea de plantas medicinales colocadas en marquesinas o deshidratadores solares; experimenta merma por pérdida de humedad.
3. **Merma:** Pérdida natural de peso ocurrida durante el secado o procesamiento. No constituye merma culposa si está dentro de la tolerancia técnica de la especie.
4. **Transformación:** Proceso artesanal de molienda, mezclado, fraccionamiento y envasado de insumos secos para convertirlos en presentaciones comerciales de horchata o té.
5. **Feria:** Espacio de comercialización comunitaria (ferias agroecológicas locales, cantonales o provinciales) gestionado por una delegación de socias encargadas.
6. **Encargo:** Responsabilidad temporal concreta asignada a una socia para una jornada o feria (ej. encargada de pesaje, encargada de ventas en feria).
7. **Designación de Cargo:** Nombramiento estatutario formal en la directiva (Presidenta, Secretaria, Tesorera) derivado de una elección en Asamblea.
8. **Fondo Común:** Masa dineraria neta de una feria resultante de restar el costo base de los productos compartidos y los gastos asociativos del total recaudado; base para liquidar la compensación comunitaria.
9. **Excedente Individual:** Margen económico obtenido por la venta de un producto de stock propio de una socia, atribuido íntegramente a ella sin ingresar al fondo común.
10. **Falta:** Inasistencia no comunicada previamente a una minga, sesión o feria comunitaria obligatoria.
11. **Justificativo:** Escrito o comunicación formal remitida a la Presidenta para eximir una falta por causa de fuerza mayor (salud, calamidad doméstica).
12. **Minga:** Trabajo colectivo no remunerado de las socias para mantenimiento de infraestructura, cosecha o limpieza comunal.

---

## 5. Hipótesis a Validar con la Organización

Las siguientes afirmaciones son supuestos técnicos razonables, pero **deben ser convalidadas formalmente con la Presidenta y la Asamblea**:

1. *[Hipótesis]* Las socias aceptan recibir avisos de convocatoria a mingas y recordatorios de turnos por WhatsApp mediante un bot o pasarela comunitaria, sin considerar que vulnera su privacidad (RF-NOT-002, P-14).
2. *[Hipótesis]* El plazo de 3 días hábiles para presentar justificativos ante la Presidenta (D-11) computa sábados y domingos como inhábiles, aun cuando las ferias suelen celebrarse los fines de semana.
3. *[Hipótesis]* La asociación considera viable que una feria cuente con notas de venta en papel numeradas manualmente que luego se transcriban al sistema hasta las 23:59 del día posterior (D-14, D-21).
4. *[Hipótesis]* Toda socia activa tiene autorización para vender productos de su stock individual de manera directa fuera de feria sin requerir permiso previo de la Directiva (D-02).

---

## 6. Preguntas Abiertas de Detalle

1. **Parámetros exactos de recetas (P-04):** ¿Cuáles son las proporciones porcentuales oficiales de las 10 presentaciones comerciales aprobadas en D-10?
2. **Proveedor de notificaciones externas:** Proveedor, presupuesto y condiciones de entrega no están definidos. Mantener adaptador deshabilitado hasta verificarlos; no presuponer servicio gratuito ni automatización no autorizada.
3. **Versión final de PostgreSQL en producción:** Confirmar soporte de `NULLS NOT DISTINCT` o implementar índices únicos parciales equivalentes. Un bloqueo sobre una búsqueda vacía no sustituye unicidad. Para intervalos, bloquear el padre existente o usar exclusión con extensión disponible (§16.5 del diseño integral).

## 7. Correcciones verificables de esta revisión

- Cero crédito al comprador en todos los canales; pago antes de entrega (D-24).
- Custodia individual y rendición interna posteriores conservadas (D-27).
- Superadministradora administra/corrige y no ejecuta/aprueba negocio (D-25/D-28).
- Secado de un solo acopio y linaje explícito (D-26).
- Impugnación ante Tesorera; justificativo ante Presidenta (D-18/D-11).
- Devoluciones y reembolsos pendientes sin efecto automático (D-29).
- Las tablas, permisos y casos DAT-01 a DAT-15 del [[2026-10-29-diseno-integral-base-datos|diseño integral revisión 0.2]] son el contrato propuesto; pruebas de producto pendientes.
