---
title: Revisión del modelo conceptual de datos y correspondencia de nombres a español (Fase 1 y 2)
type: checkpoint
status: completed
date: 2026-10-29
task_id: SB-S1-03
technical_story: HT-PRE-003
requirement_ids:
  - RF-ACC-001
  - RF-ACC-002
  - RF-ACC-003
  - RF-ACC-004
  - RF-ACC-005
  - RF-ACC-006
  - RF-ACC-007
  - RF-PLA-001
  - RF-PLA-002
  - RF-PLA-003
  - RF-PLA-004
  - RF-PLA-005
  - RF-ASI-001
  - RF-ASI-002
  - RF-ASI-003
  - RF-ASI-004
  - RF-ASI-005
  - RF-ASI-006
  - RF-ASI-007
  - RF-CAT-001
  - RF-TRA-001
  - RF-TRA-002
  - RF-TRA-003
  - RF-TRA-004
  - RF-TRA-005
  - RF-INV-001
  - RF-INV-002
  - RF-INV-003
  - RF-INV-004
  - RF-INV-005
  - RF-INV-006
  - RF-VEN-001
  - RF-VEN-002
  - RF-VEN-003
  - RF-VEN-004
  - RF-VEN-005
  - RF-VEN-006
  - RF-VEN-007
  - RF-VEN-008
  - RF-VEN-009
  - RF-GAS-001
  - RF-GAS-002
  - RF-CXC-001
  - RF-CXC-002
  - RF-CXC-003
  - RF-REP-001
  - RF-REP-005
  - RF-PUB-001
  - RF-PUB-002
  - RF-PUB-003
  - RF-DOC-001
  - RF-AST-001
sprint: S1
module: transversal
repository: ZhudAleli
phase: pre_commit
writer: documenter
branch: docs/requisitos-y-organizacion-del-vault
head: dbd0e2207972715ebaf2b7ef2b67f6af63feb6e9
commit: pending
related:
  - "[[../ESTADO-ACTIVO]]"
  - "[[../../architecture/proposals/2026-10-29-diseno-integral-base-datos]]"
  - "[[../../architecture/proposals/2026-10-29-decisiones-pendientes-diseno-datos]]"
  - "[[../../architecture/proposals/2026-10-29-identidad-cargos-encargos]]"
  - "[[../../architecture/proposals/2026-10-29-mapa-conceptual-modulos-y-dependencias]]"
  - "[[../../architecture/proposals/2026-10-29-revision-simplicidad-y-contexto-organizacional]]"
tags:
  - proyecto/tesis
  - tipo/checkpoint
  - fase/pre_commit
  - modulo/transversal
---

# Revisión del modelo conceptual de datos y correspondencia de nombres a español (Fase 1 y 2)

- **Fecha:** 2026-10-29
- **Tarea:** SB-S1-03 / HT-PRE-003 (Modelo conceptual de datos)
- **Rol:** Arquitecto de datos / Documenter
- **Estado:** `completed` (aprobado por el tesista para aplicación de Fase 2)
**Fase Git:** `pre_commit` (`commit: pending`)

---

## 1. Contexto operativo y advertencia Git

Este documento consolida la normalización de la nomenclatura del modelo de datos de Zhud Alelí al español, incorporando los ajustes requeridos por el tesista para reflejar con exactitud el vocabulario de la organización, evitar ambigüedades, añadir los catálogos de texto corrido y respetar las restricciones nativas del framework Django y de PostgreSQL.

> [!WARNING] Estado Git del Vault
> Los archivos de `docs/architecture/proposals/` y este checkpoint permanecen como **archivos sin seguimiento (`untracked`)** en el repositorio del vault `ZhudAleli` (rama `docs/requisitos-y-organizacion-del-vault`, HEAD `dbd0e2207972715ebaf2b7ef2b67f6af63feb6e9`). Conforme a la regla de gobernanza de la tesis, **no se realiza ningún commit automático**; el tesista decidirá cuándo preparar y confirmar estos cambios documentales.

---

## 2. Resultado de la Verificación Bidireccional por Script

Para asegurar que ninguna tabla fuera inventada ni omitida respecto a las propuestas aprobadas y el código existente, se ejecutó el script de verificación automatizado (`scratch/comprehensive_verifier.py`), ampliado con los catálogos de texto corrido de §9:

```text
==================================================
VERIFICACIÓN BIDIRECCIONAL DE TABLAS Y FUENTES
==================================================
Total tablas y catálogos encontrados en fuentes: 162
Total tablas y catálogos en el mapeo propuesto: 162

Chequeo (a): ¿Toda fila de 'actual' existe en las fuentes?
  -> CORRECTO: 100% de las filas de 'actual' existen en las propuestas / código fuente.

Chequeo (b): ¿Toda tabla de las fuentes tiene fila en el mapeo?
  -> CORRECTO: 100% de las tablas de las fuentes tienen fila en la tabla de correspondencia.
```

---

## 3. Conteo Consolidado por Módulo y Tipo de Relación

| Módulo (Opción A) | Heredadas (`models.py`) | Físicas de Dominio | Catálogos Auxiliares | Vistas SQL de Lectura | Aplazadas | Total Relaciones |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| `accounts` | 5 | 9 | 5 | 0 | 1 | **20** |
| `planificacion` | 0 | 10 | 8 | 0 | 0 | **18** |
| `asistencia` | 0 | 15 | 11 | 0 | 0 | **26** |
| `trazabilidad` | 0 | 46 | 31 | 1 | 0 | **78** |
| `sitio_publico` | 0 | 4 | 3 | 0 | 0 | **7** |
| `documentos` *(futuro)* | 0 | 5 | 3 | 0 | 0 | **8** |
| `activos` *(futuro)* | 0 | 2 | 3 | 0 | 0 | **5** |
| **TOTAL SISTEMA** | **5** | **91** | **64** | **1** | **1** | **162** |

---

## 4. Reglas de Nomenclatura, Restricciones y Django ORM

### 4.1 Convención de Prefijos e Índices
1. **Prefijos de integridad:**
   - `ck_`: Restricciones de chequeo (`models.CheckConstraint(name="ck_...")`). Límite PostgreSQL: 63 caracteres.
   - `uq_`: Restricciones de unicidad (`models.UniqueConstraint(name="uq_...")`). Límite PostgreSQL: 63 caracteres.
   - `ix_`: Índices explícitos (`models.Index(name="ix_...")`).
2. **Límite de Django para `models.Index` (Chequeo `models.E034`):**
   - Django valida que `name` en `models.Index` tenga un **máximo estricto de 30 caracteres**.
   - Para no superar este límite, los índices utilizan abreviaturas estándar:
     - `ix_mov_exist_cuenta_fecha` (25 caracteres)
     - `ix_asig_encarg_destinataria` (27 caracteres)
     - `ix_reg_asist_partic_fecha` (26 caracteres)
     - `ix_evento_acceso_suj_fecha` (26 caracteres)
     - `ix_linea_venta_cuenta_exis` (26 caracteres)
3. **Ausencia de prefijo `fk_`:**
   - En Django, las claves foráneas no reciben un parámetro de nombre de constraint en el ORM; Django genera automáticamente el identificador de la foreign key. Por tanto, no se definen nombres con prefijo `fk_`.

### 4.2 Ajustes Específicos de Nombres Aprobados
- `attendance_participation` → `asistencia_participacion_adicional` (evita confusión con `planificacion_participante` y refleja la participación extra de RF-ASI-005).
- `traceability_lot_parent` → `trazabilidad_lote_origen` (alineado con la terminología de D-12 y del vault para mezclas y transformaciones).
- `attendance_business_calendar_day` → `asistencia_calendario_habil` (almacena días del año con indicador `es_feriado` para calcular el plazo de 3 días hábiles de justificación, D-11).
- Cuatro catálogos de texto corrido de §9 incorporados formalmente:
  - `documents.privacy_class` → `documentos_clase_privacidad`
  - `documents.action_type` → `documentos_tipo_accion`
  - `assets.asset_status` → `activos_estado_activo`
  - `assets.asset_event_type` → `activos_tipo_evento_activo`

### 4.3 Verificación de Cero Colisiones de Columnas
Se comprobó mediante script que la unificación de términos en español no genera colisiones en ninguna tabla:
- `actor_id` se traduce como `registrada_por_id` únicamente en tablas de eventos/auditoría (donde no existen columnas de creación u operación separadas).
- `recorded_by_id` se traduce como `registrada_por_id` en transacciones operativas.
- `created_by_id` se traduce como `creada_por_id` en registros maestros.
- **Resultado verificado:** **0 colisiones** en las 162 tablas del monolito.

---

## 5. Tabla Completa de Correspondencia (162 Relaciones)

### 5.1 Módulo `accounts` (Identidad y Membresía) — 20 relaciones
| Nombre Actual | Nombre Propuesto | Tipo | Fuente | Columnas Clave Propuestas |
|---|---|:---:|---|---|
| `accounts_user` | `accounts_user` | Heredada | `models.py` | `id`, `username`, `password`, `email`, `first_name`, `last_name`, `is_active`, `is_staff`, `is_superuser`, `date_joined`, `last_login`, `must_change_password` |
| `accounts_loginthrottle` | `accounts_loginthrottle` | Heredada | `models.py` | `id`, `identifier_digest`, `failed_attempts`, `window_started_at`, `locked_until`, `updated_at` |
| `accounts_contactchannel` | `accounts_contactchannel` | Heredada | `models.py` | `id`, `user_id FK accounts_user`, `type`, `value`, `verified_at`, `created_at`, `updated_at` |
| `accounts_authchallenge` | `accounts_authchallenge` | Heredada | `models.py` | `id`, `user_id FK accounts_user`, `contact_id FK accounts_contactchannel`, `purpose`, `token_digest`, `expires_at`, `consumed_at`, `created_at` |
| `accounts_authattempt` | `accounts_authattempt` | Heredada | `models.py` | `id`, `scope_digest`, `attempts`, `window_started_at`, `locked_until`, `updated_at` |
| `accounts_membership` | `accounts_membresia` | Física | §2 (L42) | `id`, `usuaria_id FK accounts_user UNIQUE`, `fecha_ingreso date`, `fecha_salida date NULL`, `estado_membresia_id FK`, `registrada_por_id FK accounts_user` |
| `accounts_profile_assignment` | `accounts_asignacion_perfil` | Física | §2 (L45) | `id`, `usuaria_id FK accounts_user`, `tipo_perfil_id FK`, `vigente_desde`, `vigente_hasta NULL`, `asignada_por_id FK accounts_user`, `motivo` |
| `accounts_cargo_assignment` | `accounts_designacion_cargo` | Física | §2 (L47) | `id`, `usuaria_id FK accounts_user`, `tipo_cargo_id FK`, `vigente_desde`, `vigente_hasta NULL`, `asignada_por_id FK accounts_user`, `motivo` |
| `accounts_superadmin_grant` | `accounts_concesion_superadministracion` | Física | §2 (L48) | `id`, `usuaria_id FK accounts_user`, `autorizada_por_id FK accounts_user NULL`, `referencia_evidencia`, `otorgada_por_id FK accounts_user NULL`, `vigente_desde`, `revocada_en NULL`, `revocacion_autorizada_por_id FK accounts_user NULL`, `revocada_por_id FK accounts_user NULL`, `motivo` |
| `accounts_passkey_credential` | `accounts_credencial_passkey` | Física | §2 (L50) | `id`, `usuaria_id FK accounts_user`, `id_credencial bytea UNIQUE`, `clave_publica bytea`, `contador_firmas bigint`, `creado_en`, `ultimo_uso_en NULL`, `revocado_en NULL`, `alias NULL` |
| `accounts_access_event` | `accounts_evento_acceso` | Física | §2 (L51) | `id`, `usuaria_id FK accounts_user NULL`, `registrada_por_id FK accounts_user NULL`, `tipo_evento_id FK`, `ocurrio_en`, `sujeto_id FK accounts_user NULL`, `motivo NULL`, `valor_anterior jsonb NULL`, `valor_nuevo jsonb NULL`, `operacion_id uuid UNIQUE` |
| `accounts_login_policy_version` | `accounts_version_politica_login` | Física | §2 (L52) | `id`, `numero_version integer UNIQUE`, `max_intentos`, `segundos_ventana`, `segundos_bloqueo`, `segundos_sesion_inactiva`, `vigente_desde`, `vigente_hasta NULL`, `aprobada_por_id FK accounts_user`, `motivo` |
| `accounts_contact_consent` | `accounts_consentimiento_contacto` | Física | §6 (L178) | `id`, `usuaria_id FK accounts_user`, `canal_contacto_id FK accounts_contactchannel`, `proposito_id FK`, `consentido boolean`, `consentido_en`, `revocado_en NULL`, `evidencia_texto NULL` |
| `accounts_cambio_membresia` | `accounts_evento_cambio_membresia` | Física | Identidad (L79) | `id`, `membresia_id FK accounts_membresia`, `estado_anterior_id FK`, `estado_nuevo_id FK`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `motivo` |
| `accounts_membership_status` | `accounts_estado_membresia` | Catálogo | §2 (L43) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`activa`, `permiso`, `retirada`) |
| `accounts_profile_type` | `accounts_tipo_perfil` | Catálogo | §2 (L44) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`socia_operaria`, `visitante`) |
| `accounts_cargo_type` | `accounts_tipo_cargo` | Catálogo | §2 (L46) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`presidenta`, `secretaria`, `tesorera`) |
| `accounts_access_event_type` | `accounts_tipo_evento_acceso` | Catálogo | §8 (L204) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` |
| `accounts_consent_purpose` | `accounts_proposito_consentimiento` | Catálogo | §8 (L204) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` |
| `accounts_module_grant` | `accounts_concesion_modulo` *(APLAZADA)* | Aplazada | §2 (L49) | *Aplazada por conflicto con RF-ACC-005 y SPEC-002.* |

---

### 5.2 Módulo `planificacion` (antes `planning`) — 18 relaciones
| Nombre Actual | Nombre Propuesto | Tipo | Fuente | Columnas Clave Propuestas |
|---|---|:---:|---|---|
| `planning_activity` | `planificacion_actividad` | Física | §3 (L61) | `id`, `tipo_actividad_id FK`, `titulo`, `inicia_en`, `termina_en NULL`, `lugar`, `responsable_id FK accounts_user`, `estado_id FK`, `creada_por_id FK accounts_user` |
| `planning_participant` | `planificacion_participante` | Física | §3 (L63) | `id`, `actividad_id FK planificacion_actividad`, `usuaria_id FK accounts_user`, `estado_asignacion_id FK`, `asignada_por_id FK accounts_user`, `asignada_en`, `retirada_en NULL` |
| `planning_encargo` | `planificacion_encargo` | Física | §3 (L65) | `id`, `actividad_id FK planificacion_actividad NULL`, `tipo_encargo_id FK`, `titulo`, `descripcion NULL`, `estado_id FK`, `creada_por_id FK accounts_user` |
| `planning_encargo_assignment` | `planificacion_asignacion_encargo` | Física | §3 (L66) | `id`, `encargo_id FK planificacion_encargo`, `usuaria_id FK accounts_user`, `asignada_por_id FK accounts_user`, `asignada_en`, `aceptada_en NULL`, `inicia_en NULL`, `termina_en NULL`, `revocada_en NULL`, `estado_id FK`, `reemplazada_por_id FK NULL`, `referencia_evidencia_cierre NULL` |
| `planning_encargo_event` | `planificacion_evento_encargo` | Física | §3 (L67) | `id`, `encargo_id FK planificacion_encargo`, `asignacion_id FK NULL`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `tipo_evento_id FK`, `motivo NULL`, `valor_anterior jsonb NULL`, `valor_nuevo jsonb NULL` |
| `planning_production_plan` | `planificacion_plan_produccion` | Física | §3 (L68) | `id`, `inicio_semana date`, `creada_por_id FK accounts_user`, `estado_id FK`, `aprobada_en NULL` |
| `planning_change_event` | `planificacion_evento_cambio` | Física | §3 (L69) | `id`, `tipo_entidad`, `entidad_id`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `motivo`, `valor_anterior jsonb`, `valor_nuevo jsonb`, `operacion_id uuid` |
| `planning_reminder_policy_version` | `planificacion_version_politica_recordatorio` | Física | §6 (L179) | `id`, `tipo_actividad_id FK`, `dias_anticipacion`, `hora_disparo`, `canal_preferente`, `vigente_desde`, `vigente_hasta NULL` |
| `planning_reminder` | `planificacion_recordatorio` | Física | §6 (L180) | `id`, `actividad_id FK NULL`, `asignacion_encargo_id FK NULL`, `destinataria_id FK accounts_user`, `fecha_limite`, `visto_en NULL`, `estado_id FK` |
| `planning_external_delivery` | `planificacion_envio_externo` | Física | §6 (L181) | `id`, `recordatorio_id FK planificacion_recordatorio`, `consentimiento_id FK accounts_consentimiento_contacto`, `referencia_proveedor NULL`, `numero_intento`, `solicitado_en`, `resultado_en NULL`, `estado_envio_id FK`, `codigo_fallo NULL` |
| `planning_activity_type` | `planificacion_tipo_actividad` | Catálogo | §3 (L60) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`reunion`, `minga`, `feria`, `capacitacion`) |
| `planning_activity_status` | `planificacion_estado_actividad` | Catálogo | §3 (L62) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`programada`, `en_curso`, `completada`, `cancelada`) |
| `planning_encargo_type` | `planificacion_tipo_encargo` | Catálogo | §3 (L64) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`secado`, `feria`, `pesaje`, `acopio`) |
| `planning_participant_status` | `planificacion_estado_participante` | Catálogo | §8 (L205) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`convocada`, `confirmada`, `retirada`) |
| `planning_encargo_status` | `planificacion_estado_encargo` | Catálogo | §8 (L205) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`pendiente`, `asignado`, `en_curso`, `cerrado`) |
| `planning_production_plan_status` | `planificacion_estado_plan_produccion` | Catálogo | §8 (L205) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`borrador`, `aprobado`, `en_ejecucion`, `cerrado`) |
| `planning_reminder_status` | `planificacion_estado_recordatorio` | Catálogo | §8 (L209) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`pendiente`, `visto`, `cancelado`) |
| `planning_delivery_status` | `planificacion_estado_envio` | Catálogo | §8 (L209) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`solicitado`, `entregado`, `fallido`) |

---

### 5.3 Módulo `asistencia` (antes `attendance`) — 26 relaciones
| Nombre Actual | Nombre Propuesto | Tipo | Fuente | Columnas Clave Propuestas |
|---|---|:---:|---|---|
| `attendance_qr_policy_version` | `asistencia_version_politica_qr` | Física | §4 (L77) | `id`, `numero_version integer UNIQUE`, `duracion_segundos`, `rotacion_segundos`, `ventana_entrada_minutos`, `ventana_salida_minutos`, `vigente_desde`, `vigente_hasta NULL` |
| `attendance_qr_phase` | `asistencia_fase_qr` | Física | §4 (L78) | `id`, `actividad_id FK planificacion_actividad`, `tipo_evento_id FK`, `abierta_por_id FK accounts_user`, `abierta_en`, `cerrada_en NULL`, `estado_id FK`, `token_actual_digest`, `token_generado_en`, `motivo_cierre NULL` |
| `attendance_event` | `asistencia_registro` | Física | §4 (L80) | `id`, `participante_id FK planificacion_participante`, `tipo_evento_id FK`, `registrada_por_id FK accounts_user`, `fuente_id FK`, `fase_qr_id FK NULL`, `hora_marcada`, `hora_servidor`, `dispositivo_hash NULL`, `es_valido` |
| `attendance_rectification` | `asistencia_correccion` | Física | §4 (L81) | `id`, `evento_asistencia_id FK asistencia_registro`, `registrada_por_id FK accounts_user`, `autorizada_por_id FK accounts_user`, `ocurrio_en`, `motivo`, `valor_anterior jsonb`, `valor_nuevo jsonb` |
| `attendance_participation` | `asistencia_participacion_adicional` | Física | §4 (L82) | `id`, `participante_id FK planificacion_participante UNIQUE`, `tipo_participacion_id FK`, `calculada_en`, `minutos_presencia`, `observacion NULL` |
| `attendance_absence_case` | `asistencia_caso_falta` | Física | §4 (L83) | `id`, `participante_id FK planificacion_participante UNIQUE`, `cerrada_en NULL`, `estado_id FK`, `generada_en`, `motivo_cierre NULL` |
| `attendance_justification` | `asistencia_justificativo` | Física | §4 (L84) | `id`, `caso_falta_id FK asistencia_caso_falta`, `presentada_por_id FK accounts_user`, `presentada_en`, `fecha_limite`, `motivo_texto`, `decision_id FK`, `resuelta_por_id FK accounts_user NULL`, `resuelta_en NULL`, `motivo_decision NULL` |
| `attendance_business_calendar_day` | `asistencia_calendario_habil` | Física | §4 (L85) | `id`, `fecha_calendario date UNIQUE`, `es_feriado boolean`, `alcance_feriado_id FK`, `descripcion NULL` *(permite cálculo de días hábiles)* |
| `attendance_fine_rule_version` | `asistencia_version_regla_multa` | Física | §4 (L86) | `id`, `numero_version integer UNIQUE`, `monto_falta numeric(18,2)`, `dias_plazo_justificacion`, `dias_plazo_pago`, `dias_plazo_impugnacion`, `vigente_desde`, `vigente_hasta NULL`, `aprobada_por_id FK accounts_user`, `motivo` |
| `attendance_fine` | `asistencia_multa` | Física | §4 (L87) | `id`, `caso_falta_id FK asistencia_caso_falta UNIQUE`, `monto numeric(18,2)`, `fecha_limite`, `estado_id FK`, `generada_en` |
| `attendance_fine_appeal` | `asistencia_impugnacion_multa` | Física | §4 (L88) | `id`, `multa_id FK asistencia_multa`, `presentada_por_id FK accounts_user`, `presentada_en`, `argumento`, `nuevo_monto numeric(18,2) NULL`, `resuelta_por_id FK accounts_user NULL`, `resuelta_en NULL`, `estado_id FK`, `motivo_decision NULL` |
| `attendance_fine_payment` | `asistencia_pago_multa` | Física | §4 (L89) | `id`, `multa_id FK asistencia_multa`, `monto numeric(18,2)`, `pagado_en`, `registrada_por_id FK accounts_user`, `metodo_pago_id FK`, `referencia_evidencia NULL` |
| `attendance_case_event` | `asistencia_evento_caso` | Física | §4 (L90) | `id`, `caso_falta_id FK asistencia_caso_falta`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `tipo_evento_id FK`, `motivo NULL`, `valor_anterior jsonb NULL`, `valor_nuevo jsonb NULL` |
| `attendance_sync_receipt` | `asistencia_recibo_sincronizacion` | Física | §9 (L236) | `id`, `usuaria_id FK accounts_user`, `operacion_cliente_id uuid`, `resumen_carga bytea`, `recibida_en`, `procesada_en NULL`, `resultado_codigo` |
| `attendance_absence_notice` | `asistencia_aviso_falta` | Física | §9 (L239) | `id`, `caso_falta_id FK asistencia_caso_falta`, `destinataria_id FK accounts_user`, `tipo_aviso_id FK`, `fecha_limite`, `creado_en` |
| `attendance_event_kind` | `asistencia_tipo_evento` | Catálogo | §4 (L79) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`llegada`, `salida`, `jornada_completa`) |
| `attendance_source` | `asistencia_fuente_registro` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`qr`, `manual_secretaria`, `offline`) |
| `attendance_qr_phase_status` | `asistencia_estado_fase_qr` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`activa`, `cerrada`, `expirada`) |
| `attendance_participation_type` | `asistencia_tipo_participacion` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`presente`, `atraso`, `permiso`, `comision`) |
| `attendance_absence_status` | `asistencia_estado_falta` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`pendiente`, `justificada`, `injustificada_multada`, `anulada`) |
| `attendance_justification_decision` | `asistencia_decision_justificativo` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`aceptada`, `rechazada`, `solicita_evidencia`) |
| `attendance_fine_status` | `asistencia_estado_multa` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`pendiente`, `impugnada`, `pagada`, `condonada`) |
| `attendance_case_event_type` | `asistencia_tipo_evento_caso` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` |
| `attendance_holiday_scope` | `asistencia_alcance_feriado` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`nacional`, `cantonal`, `parroquial`) |
| `attendance_fine_appeal_status` | `asistencia_estado_impugnacion_multa` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`en_revision`, `aceptada_reduccion`, `ratificada`) |
| `attendance_fine_payment_method` | `asistencia_metodo_pago_multa` | Catálogo | §8 (L206) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`efectivo`, `transferencia`) |

---

### 5.4 Módulo `trazabilidad` (antes `traceability`) — 78 relaciones
| Nombre Actual | Nombre Propuesto | Tipo | Fuente | Columnas Clave Propuestas |
|---|---|:---:|---|---|
| `traceability_unit` | `trazabilidad_unidad` | Física | §5.1 (L100) | `id`, `codigo varchar(20) UNIQUE`, `nombre`, `dimension`, `es_unidad_referencia` |
| `traceability_unit_conversion` | `trazabilidad_conversion_unidad` | Física | §5.1 (L101) | `id`, `unidad_origen_id FK`, `unidad_destino_id FK`, `factor numeric(20,10)`, `aprobada_por_id FK accounts_user` |
| `traceability_material` | `trazabilidad_materia_prima` | Física | §5.1 (L103) | `id`, `categoria_id FK`, `nombre`, `unidad_defecto_id FK`, `requiere_secado`, `merma_tolerada_pct NULL` |
| `traceability_product` | `trazabilidad_producto` | Física | §5.1 (L105) | `id`, `categoria_id FK`, `nombre`, `variante`, `unidad_defecto_id FK`, `es_kit` |
| `traceability_presentation` | `trazabilidad_presentacion` | Física | §5.1 (L106) | `id`, `producto_id FK`, `nombre`, `cantidad_neta numeric(20,6)`, `unidad_id FK`, `codigo_barras NULL`, `requiere_lote` |
| `traceability_value_version` | `trazabilidad_version_valor` | Física | §5.1 (L107) | `id`, `presentacion_id FK`, `tipo_valor_id FK`, `monto numeric(18,2)`, `vigente_desde`, `vigente_hasta NULL`, `aprobada_por_id FK accounts_user`, `motivo` |
| `traceability_recipe_version` | `trazabilidad_version_receta` | Física | §5.1 (L108) | `id`, `producto_id FK`, `numero_version integer`, `vigente_desde`, `vigente_hasta NULL`, `rendimiento_esperado`, `unidad_rendimiento_id FK`, `estado_id FK` |
| `traceability_recipe_input` | `trazabilidad_insumo_receta` | Física | §5.1 (L109) | `id`, `version_receta_id FK`, `materia_prima_id FK NULL`, `producto_insumo_id FK NULL`, `cantidad_proporcional numeric(20,6)`, `unidad_id FK` |
| `traceability_minimum_threshold` | `trazabilidad_umbral_minimo` | Física | §5.1 (L110) | `id`, `materia_prima_id FK NULL`, `producto_id FK NULL`, `cuenta_existencia_id FK NULL`, `cantidad_minima numeric(20,6)`, `unidad_id FK`, `esta_activo` |
| `traceability_production_plan_line` | `trazabilidad_linea_plan_produccion` | Física | §5.1 (L111) | `id`, `plan_id FK planificacion_plan_produccion`, `presentacion_id FK`, `cantidad_planificada numeric(20,6)`, `unidad_id FK` |
| `traceability_plan_material` | `trazabilidad_material_plan` | Física | §5.1 (L112) | `id`, `plan_id FK planificacion_plan_produccion`, `materia_prima_id FK`, `cantidad_estimada numeric(20,6)`, `unidad_id FK` |
| `traceability_inventory_operation` | `trazabilidad_operacion_inventario` | Física | §5.2 (L120) | `id`, `tipo_operacion_id FK`, `estado_id FK`, `registrada_por_id FK accounts_user`, `realizada_en`, `motivo NULL`, `operacion_origen_id uuid UNIQUE` |
| `traceability_stock_account` | `trazabilidad_cuenta_existencia` | Física | §5.2 (L121) | `id`, `tipo_custodia_id FK`, `socia_titular_id FK accounts_user NULL`, `feria_id FK NULL`, `esta_activa` |
| `traceability_stock_movement` | `trazabilidad_movimiento_existencia` | Física | §5.2 (L122) | `id`, `operacion_id FK`, `cuenta_existencia_id FK`, `direccion smallint (-1/1)`, `cantidad numeric(20,6)`, `unidad_id FK`, `creado_en` |
| `traceability_collection` | `trazabilidad_acopio` | Física | §5.2 (L123) | `id`, `operacion_id FK UNIQUE`, `socia_origen_id FK accounts_user`, `materia_prima_id FK`, `cantidad numeric(20,6)`, `unidad_id FK`, `recibida_en`, `responsable_id FK accounts_user`, `monto_valoracion numeric(18,2) NULL`, `observacion NULL` |
| `traceability_drying_batch` | `trazabilidad_lote_secado` | Física | §5.2 (L124) | `id`, `acopio_origen_id FK NULL`, `asignacion_encargo_id FK NULL`, `iniciado_en`, `finalizado_en NULL`, `peso_inicial numeric(20,6)`, `peso_final numeric(20,6) NULL`, `unidad_id FK`, `temperatura_c numeric(6,2) NULL`, `humedad_pct numeric(5,2) NULL`, `estado_id FK`, `motivo_revision NULL` |
| `traceability_weighing_revision` | `trazabilidad_correccion_pesaje` | Física | §5.2 (L125) | `id`, `lote_secado_id FK`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `motivo`, `peso_anterior numeric(20,6)`, `peso_nuevo numeric(20,6)`, `unidad_id FK` |
| `traceability_lot` | `trazabilidad_lote` | Física | §5.2 (L126) | `id`, `codigo_lote varchar(60) UNIQUE`, `presentacion_id FK`, `transformacion_id FK NULL`, `elaborado_en`, `expira_en NULL`, `estado_id FK` |
| `traceability_lot_parent` | `trazabilidad_lote_origen` | Física | §5.2 (L127) | `id`, `lote_hijo_id FK`, `lote_padre_id FK`, `cantidad_aportada numeric(20,6)`, `unidad_id FK` |
| `traceability_transformation` | `trazabilidad_transformacion` | Física | §5.2 (L128) | `id`, `operacion_id FK UNIQUE`, `version_receta_id FK`, `responsable_id FK accounts_user`, `iniciada_en`, `finalizada_en NULL`, `cantidad_resultante numeric(20,6)`, `unidad_id FK` |
| `traceability_transformation_input` | `trazabilidad_insumo_transformacion` | Física | §5.2 (L129) | `id`, `transformacion_id FK`, `cuenta_existencia_origen_id FK`, `lote_origen_id FK NULL`, `cantidad_consumida numeric(20,6)`, `unidad_id FK` |
| `traceability_inventory_exception` | `trazabilidad_excepcion_inventario` | Física | §5.2 (L130) | `id`, `operacion_id FK`, `tipo_excepcion_id FK`, `lote_sujeto_id FK NULL`, `solicitada_por_id FK accounts_user`, `aprobada_por_id FK accounts_user NULL`, `motivo`, `estado_id FK` |
| `traceability_fair` | `trazabilidad_feria` | Física | §5.3 (L138) | `id`, `actividad_id FK planificacion_actividad UNIQUE`, `abierta_por_id FK accounts_user`, `abierta_en`, `cerrada_en NULL`, `estado_id FK`, `notas NULL` |
| `traceability_custody_transfer` | `trazabilidad_transferencia_custodia` | Física | §5.3 (L139) | `id`, `operacion_id FK`, `feria_id FK NULL`, `asignacion_encargo_id FK NULL`, `cuenta_origen_id FK`, `cuenta_destino_id FK`, `responsable_entrega_id FK accounts_user`, `responsable_recepcion_id FK accounts_user`, `recibida_en NULL`, `cantidad_diferencia numeric(20,6) NULL` |
| `traceability_buyer` | `trazabilidad_comprador` | Física | §5.3 (L140) | `id`, `nombre_visible varchar(180)`, `tipo_comprador_id FK`, `valor_contacto NULL`, `creada_por_id FK accounts_user` *(neutro/institucional)* |
| `traceability_sale` | `trazabilidad_venta` | Física | §5.3 (L141) | `id`, `feria_id FK NULL`, `tipo_venta_id FK`, `comprador_id FK NULL`, `vendedora_id FK accounts_user`, `registrada_por_id FK accounts_user`, `vendida_en`, `registrada_en`, `forma_pago_id FK`, `operacion_inventario_id FK UNIQUE`, `comprobante_manual_id FK NULL`, `estado_id FK` |
| `traceability_sale_line` | `trazabilidad_linea_venta` | Física | §5.3 (L142) | `id`, `venta_id FK`, `presentacion_id FK`, `cuenta_existencia_id FK`, `vendedora_id FK accounts_user`, `cantidad numeric(20,6)`, `precio_unitario numeric(18,2)`, `valor_base_unitario numeric(18,2)`, `politica_descuento_id FK NULL`, `autorizacion_bajo_base_id FK accounts_user NULL` |
| `traceability_discount_policy` | `trazabilidad_politica_descuento` | Física | §5.3 (L143) | `id`, `presentacion_id FK`, `cantidad_umbral numeric(20,6)`, `unidad_id FK`, `tipo_descuento_id FK`, `nuevo_precio numeric(18,2) NULL`, `porcentaje numeric(7,4) NULL`, `vigente_desde`, `vigente_hasta NULL`, `aprobada_por_id FK accounts_user`, `estado_id FK` |
| `traceability_price_exception` | `trazabilidad_excepcion_precio` | Física | §5.3 (L144) | `id`, `linea_venta_id FK UNIQUE`, `autorizada_por_id FK accounts_user`, `autorizada_en`, `motivo`, `diferencia_base numeric(18,2)`, `modo_aprobacion_id FK` |
| `traceability_manual_voucher` | `trazabilidad_comprobante_manual` | Física | §5.3 (L145) | `id`, `feria_id FK`, `identificador_interno uuid UNIQUE`, `referencia_papel varchar(80) NULL`, `ocurrio_en`, `digitalizado_en NULL`, `digitalizado_por_id FK accounts_user NULL`, `verificado_en NULL`, `verificado_por_id FK accounts_user NULL`, `estado_id FK` |
| `traceability_member_debt` | `trazabilidad_deuda_socia` | Física | §5.3 (L146) | `id`, `socia_id FK accounts_user`, `linea_venta_origen_id FK NULL`, `retiro_origen_id FK NULL`, `monto_base numeric(18,2)`, `abierta_en`, `estado_id FK` |
| `traceability_external_receivable` | `trazabilidad_cuenta_por_cobrar_externa` | Física | §5.3 (L147) | `id`, `comprador_id FK`, `venta_id FK`, `monto numeric(18,2)`, `abierta_en`, `estado_id FK` |
| `traceability_payment` | `trazabilidad_pago` | Física | §5.3 (L148) | `id`, `monto numeric(18,2)`, `pagado_en`, `registrada_por_id FK accounts_user`, `metodo_pago_id FK`, `referencia_evidencia NULL`, `estado_id FK` |
| `traceability_payment_application` | `trazabilidad_aplicacion_pago` | Física | §5.3 (L149) | `id`, `pago_id FK`, `deuda_socia_id FK NULL`, `cuenta_externa_id FK NULL`, `monto_aplicado numeric(18,2)` |
| `traceability_fair_expense_plan` | `trazabilidad_plan_gasto_feria` | Física | §5.3 (L151) | `id`, `feria_id FK`, `categoria_id FK`, `monto_planificado numeric(18,2)`, `planificado_por_id FK accounts_user`, `planificado_en`, `nota NULL` |
| `traceability_expense` | `trazabilidad_gasto` | Física | §5.3 (L152) | `id`, `feria_id FK NULL`, `categoria_id FK`, `monto numeric(18,2)`, `tipo_pagador_id FK`, `incurrido_en`, `registrada_por_id FK accounts_user`, `aprobada_por_id FK accounts_user NULL`, `concepto text`, `referencia_evidencia NULL`, `estado_id FK` |
| `traceability_sale_adjustment_case` | `trazabilidad_caso_ajuste_venta` | Física | §5.3 (L153) | `id`, `venta_id FK`, `tipo_motivo_id FK`, `solicitada_por_id FK accounts_user`, `solicitada_en`, `operacion_fisica_id FK NULL`, `estado_efecto_monetario_id FK`, `resuelta_por_id FK accounts_user NULL`, `motivo_resolucion NULL` |
| `traceability_fair_reconciliation` | `trazabilidad_conciliacion_feria` | Física | §5.3 (L154) | `id`, `feria_id FK`, `numero_version integer`, `preparada_por_id FK accounts_user`, `preparada_en`, `verificada_por_id FK accounts_user NULL`, `verificada_en NULL`, `dinero_recibido numeric(18,2) NULL`, `estado_id FK`, `nota_diferencia NULL` |
| `traceability_fair_reconciliation_line` | `trazabilidad_linea_conciliacion_feria` | Física | §5.3 (L155) | `id`, `conciliacion_id FK`, `cuenta_existencia_id FK`, `unidad_id FK`, `cantidad_recibida numeric(20,6)`, `cantidad_vendida numeric(20,6)`, `cantidad_devuelta numeric(20,6)`, `cantidad_remanente numeric(20,6)`, `cantidad_diferencia numeric(20,6)` |
| `traceability_fair_rule_version` | `trazabilidad_version_regla_reparto_feria` | Física | §5.3 (L156) | `id`, `numero_version integer UNIQUE`, `codigo_estrategia varchar(40)`, `vigente_desde`, `vigente_hasta NULL`, `aprobada_por_id FK accounts_user`, `motivo` |
| `traceability_fair_distribution` | `trazabilidad_reparto_feria` | Física | §5.3 (L157) | `id`, `feria_id FK`, `version_regla_id FK`, `preparada_por_id FK accounts_user`, `preparada_en`, `modo_reparto_id FK`, `total_ventas_compartidas numeric(18,2)`, `total_base_compartida numeric(18,2)`, `gastos_comunes numeric(18,2)`, `monto_fondo_comun numeric(18,2)`, `numero_version`, `cerrada_en NULL`, `estado_id FK` |
| `traceability_fair_share` | `trazabilidad_cuota_reparto_feria` | Física | §5.3 (L158) | `id`, `reparto_id FK`, `asignacion_encargo_id FK`, `socia_id FK accounts_user`, `base_ventas_compartidas numeric(18,2)`, `monto_cuota numeric(18,2)`, `aprobada_en NULL`, `aprobada_por_id FK accounts_user NULL` |
| `traceability_change_event` | `trazabilidad_evento_cambio` | Física | §5.3 (L160) | `id`, `tipo_entidad`, `entidad_id`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `motivo`, `valor_anterior jsonb`, `valor_nuevo jsonb`, `operacion_id uuid`, `autorizacion_id FK accounts_user NULL` |
| `traceability_sync_receipt` | `trazabilidad_recibo_sincronizacion` | Física | §9 (L237) | `id`, `usuaria_id FK accounts_user`, `operacion_cliente_id uuid`, `resumen_carga bytea`, `recibida_en`, `procesada_en NULL`, `resultado_codigo` |
| `traceability_sale_sync_receipt` | `trazabilidad_recibo_sincronizacion_venta` | Física | §9 (L238) | `id`, `usuaria_id FK accounts_user`, `operacion_cliente_id uuid`, `resumen_carga bytea`, `recibida_en`, `procesada_en NULL`, `resultado_codigo` |
| `traceability_minimum_alert` | `trazabilidad_alerta_minimo` | Física | §9 (L240) | `id`, `umbral_id FK`, `cuenta_existencia_id FK`, `cantidad_observada numeric(20,6)`, `cantidad_umbral numeric(20,6)`, `generada_en`, `resuelta_en NULL` |
| `traceability_material_category` | `trazabilidad_categoria_materia_prima` | Catálogo | §5.1 (L102) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` |
| `traceability_product_category` | `trazabilidad_categoria_producto` | Catálogo | §5.1 (L104) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` |
| `traceability_expense_category` | `trazabilidad_categoria_gasto` | Catálogo | §5.3 (L150) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo`, `es_costo_comun_feria boolean` |
| `traceability_value_kind` | `trazabilidad_tipo_valor` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`costo_base`, `precio_socia`, `precio_publico`, `precio_institucional`) |
| `traceability_recipe_status` | `trazabilidad_estado_receta` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`borrador`, `aprobada`, `obsoleta`) |
| `traceability_inventory_operation_type` | `trazabilidad_tipo_operacion_inventario` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`acopio`, `secado`, `transformacion`, `transferencia`, `venta`, `ajuste`) |
| `traceability_inventory_operation_status` | `trazabilidad_estado_operacion_inventario` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`preparada`, `confirmada`, `anulada`) |
| `traceability_custody_kind` | `trazabilidad_tipo_custodia` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`patrimonial_asociacion`, `custodia_feria`, `individual_socia`) |
| `traceability_drying_status` | `trazabilidad_estado_secado` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`en_proceso`, `completado`, `observado`) |
| `traceability_lot_status` | `trazabilidad_estado_lote` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`en_cuarentena`, `disponible`, `agotado`, `retirado`) |
| `traceability_exception_type` | `trazabilidad_tipo_excepcion` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`peso_anomalo`, `merma_excedida`, `ajuste_conteo`) |
| `traceability_exception_status` | `trazabilidad_estado_excepcion` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`pendiente`, `aprobada`, `rechazada`) |
| `traceability_fair_status` | `trazabilidad_estado_feria` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`abierta`, `en_conciliacion`, `cerrada_liquidada`) |
| `traceability_buyer_type` | `trazabilidad_tipo_comprador` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`publico_general`, `socia`, `institucion`) |
| `traceability_sale_type` | `trazabilidad_tipo_venta` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`feria`, `directa_socia`, `institucional`) |
| `traceability_payment_kind` | `trazabilidad_forma_pago` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo`, `es_inmediato` (`contado_efectivo`, `transferencia`, `credito`) |
| `traceability_sale_status` | `trazabilidad_estado_venta` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`registrada`, `confirmada`, `ajustada`) |
| `traceability_discount_kind` | `trazabilidad_tipo_descuento` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`volumen`, `promocion_feria`) |
| `traceability_discount_status` | `trazabilidad_estado_descuento` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`inactivo`, `vigente`, `expirado`) |
| `traceability_price_approval_mode` | `trazabilidad_modo_aprobacion_precio` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`previa_directiva`, `posterior_contingencia`) |
| `traceability_manual_voucher_status` | `trazabilidad_estado_comprobante_manual` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`emitido_papel`, `digitalizado`, `verificado`) |
| `traceability_debt_status` | `trazabilidad_estado_deuda` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`pendiente`, `parcial`, `liquidada`) |
| `traceability_payment_method` | `trazabilidad_metodo_pago` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`efectivo`, `transferencia_bancaria`) |
| `traceability_payment_status` | `trazabilidad_estado_pago` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`recibido`, `aplicado`, `revertido_auditado`) |
| `traceability_expense_payer_kind` | `trazabilidad_tipo_pagador_gasto` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`asociacion_fondo`, `socia_reembolso`) |
| `traceability_expense_status` | `trazabilidad_estado_gasto` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`registrado`, `aprobado_comun`, `rechazado`) |
| `traceability_adjustment_reason_kind` | `trazabilidad_tipo_motivo_ajuste` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`producto_danado`, `error_digitacion`, `devolucion_cliente`) |
| `traceability_money_effect_status` | `trazabilidad_estado_efecto_monetario` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`sin_efecto`, `pendiente_liquidacion`, `descontado`) |
| `traceability_reconciliation_status` | `trazabilidad_estado_conciliacion` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`borrador`, `verificada_tesorera`, `con_diferencia_aprobada`) |
| `traceability_distribution_mode` | `trazabilidad_modo_reparto` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`igualitario`, `proporcional_ventas_compartidas`) |
| `traceability_distribution_status` | `trazabilidad_estado_reparto` | Catálogo | §8 (L207) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`preparado`, `aprobado_todas`, `liquidado`) |
| `v_traceability_member_month_close` | `trazabilidad_vista_cierre_mensual_socia` | Vista | §5.3 (L159) / D-02 | `socia_id FK accounts_user`, `inicio_periodo date`, `fin_periodo date`, `total_ventas_individuales numeric(18,2)`, `base_debida numeric(18,2)`, `excedente_bruto_individual numeric(18,2)`, `total_cuota_feria_compartida numeric(18,2)`, `total_pagos numeric(18,2)` |

---

### 5.5 Módulo `sitio_publico` (antes `public_site`) — 7 relaciones
| Nombre Actual | Nombre Propuesto | Tipo | Fuente | Columnas Clave Propuestas |
|---|---|:---:|---|---|
| `public_site_content_item` | `sitio_publico_item_contenido` | Física | §6 (L174) | `id`, `tipo_contenido_id FK`, `slug varchar(120) UNIQUE`, `titulo`, `extracto NULL`, `destacada_en NULL`, `estado_id FK` |
| `public_site_content_revision` | `sitio_publico_revision_contenido` | Física | §6 (L175) | `id`, `item_contenido_id FK`, `numero_revision`, `titulo`, `cuerpo_md text`, `publicada_por_id FK accounts_user`, `publicada_en` |
| `public_site_price_publication` | `sitio_publico_publicacion_precio` | Física | §6 (L176) | `id`, `version_valor_id FK trazabilidad_version_valor`, `publicada_por_id FK accounts_user`, `publicada_en`, `retirada_en NULL` |
| `public_site_publication_event` | `sitio_publico_evento_publicacion` | Física | §6 (L177) | `id`, `item_contenido_id FK NULL`, `publicacion_precio_id FK NULL`, `tipo_evento_id FK`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `motivo NULL` |
| `public_site_content_type` | `sitio_publico_tipo_contenido` | Catálogo | §8 (L208) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`noticia`, `historia_organizacion`, `catalogo_producto`) |
| `public_site_content_status` | `sitio_publico_estado_contenido` | Catálogo | §8 (L208) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`borrador`, `publicado`, `retirado`) |
| `public_site_publication_event_type` | `sitio_publico_tipo_evento_publicacion` | Catálogo | §8 (L208) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`publicacion`, `actualizacion`, `retiro`) |

---

### 5.6 Módulos `documentos` y `activos` (futuros, app propia D-08) — 13 relaciones
| Nombre Actual | Nombre Propuesto | Tipo | Fuente | Columnas Clave Propuestas |
|---|---|:---:|---|---|
| `documents.document_record` | `documentos_registro_documento` | Física | §9 (L222) | `id`, `tipo_documento_id FK`, `titulo`, `vigente_desde date NULL`, `vence_en date NULL`, `subido_por_id FK accounts_user`, `clase_privacidad_id FK`, `estado_id FK` |
| `documents.document_version` | `documentos_version_documento` | Física | §9 (L223) | `id`, `registro_documento_id FK`, `numero_version`, `clave_almacenamiento`, `digest_contenido`, `subida_por_id FK accounts_user`, `subida_en` |
| `documents.document_access_grant` | `documentos_concesion_acceso` | Física | §9 (L224) | `id`, `registro_documento_id FK`, `usuaria_id FK accounts_user`, `otorgada_por_id FK accounts_user`, `vigente_desde`, `expira_en NULL`, `motivo` |
| `documents.document_event` | `documentos_evento_documento` | Física | §9 (L225) | `id`, `registro_documento_id FK`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `tipo_accion_id FK`, `motivo NULL` |
| `documents.expiration_notice` | `documentos_aviso_vencimiento` | Física | §9 (L241) | `id`, `registro_documento_id FK`, `destinataria_id FK accounts_user`, `fecha_limite`, `creado_en` |
| `documents.document_type` | `documentos_tipo_documento` | Catálogo | §9 (L221) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo`, `referencia_politica_retencion NULL` |
| `documents.privacy_class` | `documentos_clase_privacidad` | Catálogo | §9 (texto L229) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`publico_general`, `interno_socias`, `restringido_directiva`) |
| `documents.action_type` | `documentos_tipo_accion` | Catálogo | §9 (texto L229) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`subida`, `descarga`, `revocacion`, `eliminacion`) |
| `assets.asset_record` | `activos_registro_activo` | Física | §9 (L227) | `id`, `codigo_activo UNIQUE`, `categoria_id FK`, `nombre`, `adquirido_en date NULL`, `estado_id FK`, `socia_custodia_actual_id FK accounts_user NULL` |
| `assets.asset_event` | `activos_evento_activo` | Física | §9 (L228) | `id`, `activo_id FK`, `registrada_por_id FK accounts_user`, `ocurrio_en`, `tipo_evento_id FK`, `valor_anterior jsonb NULL`, `valor_nuevo jsonb NULL`, `motivo` |
| `assets.asset_category` | `activos_categoria_activo` | Catálogo | §9 (L226) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`secador`, `balanza`, `molino`, `mesa_acero`) |
| `assets.asset_status` | `activos_estado_activo` | Catálogo | §9 (texto L229) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`operativo`, `en_mantenimiento`, `baja`) |
| `assets.asset_event_type` | `activos_tipo_evento_activo` | Catálogo | §9 (texto L229) | `id`, `codigo UNIQUE`, `etiqueta`, `esta_activo` (`adquisicion`, `asignacion_custodia`, `mantenimiento`, `baja`) |

---

## 6. Mapa de Columnas Comunes (3 o Más Tablas)

| Columna Actual (Inglés) | Columna Propuesta (Español) | Frecuencia | Tipo de Dato PostgreSQL | Significado Organizacional y Regla de Uso |
|---|---|:---:|---|---|
| `user_id` | `usuaria_id` | 13 tablas | `bigint FK accounts_user` | Cuenta de socia o integrante involucrada en el hecho. |
| `status_id` | `estado_id` | 24 tablas | `bigint FK catálogo` | Estado operativo de la entidad según catálogo del módulo. |
| `reason` | `motivo` | 25 tablas | `text` | Justificación humana exigida para acciones sensibles (RNF-AUD-001). |
| `is_active` | `esta_activo` | 16 tablas | `boolean` | Bandera de vigencia en catálogos auxiliares (no borrado lógico de hechos). |
| `code` | `codigo` | 13 tablas | `varchar UNIQUE` | Código mnemotécnico único e inmutable en catálogos. |
| `label` | `etiqueta` | 12 tablas | `varchar(80)` | Texto legible para presentación en interfaz de usuaria. |
| `valid_from` | `vigente_desde` | 15 tablas | `timestamptz` | Inicio de periodo de validez de una regla, cargo o permiso. |
| `valid_to` | `vigente_hasta` | 14 tablas | `timestamptz NULL` | Fin de periodo de validez (`NULL` indica vigencia activa). |
| `occurred_at` | `ocurrio_en` | 13 tablas | `timestamptz` | Instante real del evento (declarado en móvil o registrado en servidor). |
| `old_value` | `valor_anterior` | 9 tablas | `jsonb NULL` | Snapshot inmutable del estado previo para auditoría histórica. |
| `new_value` | `valor_nuevo` | 9 tablas | `jsonb NULL` | Snapshot inmutable del estado posterior para auditoría histórica. |
| `actor_id` / `recorded_by_id` | `registrada_por_id` | 19 tablas | `bigint FK accounts_user` | Usuaria autenticada que materializó la transacción o registro. |
| `approved_by_id` | `aprobada_por_id` | 12 tablas | `bigint FK accounts_user` | Usuaria con rol/cargo que autorizó formalmente el registro. |
| `approved_at` | `aprobada_en` | 6 tablas | `timestamptz NULL` | Instante en que se emitió la autorización formal. |
| `operation_id` | `operacion_id` | 8 tablas | `uuid UNIQUE` | Clave de idempotencia y coordinación transaccional. |
| `client_operation_id` | `operacion_cliente_id` | 3 tablas | `uuid` | Clave UUID generada offline en el dispositivo cliente móvil. |
| `version_no` | `numero_version` | 8 tablas | `integer` | Secuencial ascendente en tablas de reglas parametrizadas (D-17). |
| `created_at` | `creado_en` | 7 tablas | `timestamptz NOT NULL` | Marca temporal automática de inserción de fila. |
| `created_by_id` | `creada_por_id` | 7 tablas | `bigint FK accounts_user` | Usuaria creadora del registro original. |
| `unit_id` | `unidad_id` | 16 tablas | `bigint FK unidad` | Unidad de medida física explícita para la cantidad almacenada. |
| `product_id` | `producto_id` | 7 tablas | `bigint FK producto` | Referencia al catálogo de producto terminado. |
| `material_id` | `materia_prima_id` | 5 tablas | `bigint FK materia_prima`| Referencia al catálogo de materia prima acopiada. |
| `category_id` | `categoria_id` | 5 tablas | `bigint FK catálogo` | Clasificación por familia de material, producto o activo. |
| `name` | `nombre` | 5 tablas | `varchar(150)` | Denominación formal del producto, material o unidad. |
| `title` | `titulo` | 4 tablas | `varchar(180)` | Título descriptivo de actividad, encargo o documento. |
| `amount` | `monto` | 6 tablas | `numeric(18,2)` | Importe monetario exacto en dólares de Estados Unidos (USD). |
| `quantity` | `cantidad` | 6 tablas | `numeric(20,6)` | Magnitud física con precisión decimal protegida. |
| `opened_at` | `abierta_en` | 5 tablas | `timestamptz` | Instante de apertura operativa (feria, fase QR, deuda). |
| `closed_at` | `cerrada_en` | 5 tablas | `timestamptz NULL` | Instante de cierre operativo (`NULL` si continúa abierta). |
| `stock_account_id` | `cuenta_existencia_id` | 5 tablas | `bigint FK cuenta` | Cuenta patrimonial o de custodia que respalda el saldo. |
| `received_at` | `recibida_en` | 5 tablas | `timestamptz` | Instante de recepción física de lote, dinero o acopio. |
| `recipient_id` | `destinataria_id` | 5 tablas | `bigint FK accounts_user` | Usuaria que recibe un aviso, encargo o transferencia. |
| `assigned_by_id` | `asignada_por_id` | 4 tablas | `bigint FK accounts_user` | Usuaria que delega o asigna un encargo o rol. |
| `declared_at` | `declarada_en` | 4 tablas | `timestamptz` | Hora declarada localmente en contingencia offline. |
| `absence_case_id` | `caso_falta_id` | 4 tablas | `bigint FK falta` | Vinculación directa al expediente de falta estatutaria. |
| `evidence_ref` | `referencia_evidencia` | 4 tablas | `text / varchar NULL` | Identificador documental o ruta de comprobante físico. |
| `responsible_id` | `responsable_id` | 4 tablas | `bigint FK accounts_user` | Usuaria responsable de la ejecución técnica o custodia. |
| `encargo_assignment_id`| `asignacion_encargo_id` | 4 tablas | `bigint FK asignacion`| Asignación vigente del encargo bajo el cual se actuó. |
| `sale_id` | `venta_id` | 4 tablas | `bigint FK venta` | Transacción comercial origen de la línea, deuda o cobro. |
| `record_id` | `registro_documento_id` | 4 tablas | `bigint FK documento` | Expediente documental titular de versiones y accesos. |
| `revoked_at` | `revocada_en` | 3 tablas | `timestamptz NULL` | Instante de retiro formal de una autorización o encargo. |
| `participant_id` | `participante_id` | 3 tablas | `bigint FK participante`| Vinculación de la socia a la actividad programada. |
| `recorded_at` | `registrada_en` | 3 tablas | `timestamptz` | Instante de digitación en el sistema. |
| `presentation_id` | `presentacion_id` | 3 tablas | `bigint FK presentacion`| Presentación comercial del producto (frasco, funda, etc.). |
| `member_id` | `socia_id` | 3 tablas | `bigint FK accounts_user` | Socia titular en cuentas personales o cuotas de feria. |
| `prepared_by_id` | `preparada_por_id` | 3 tablas | `bigint FK accounts_user` | Socia encargada que elabora la propuesta de reparto. |
| `prepared_at` | `preparada_en` | 3 tablas | `timestamptz` | Instante de generación del borrador de conciliación/reparto. |
| `seen_at` | `visto_en` | 3 tablas | `timestamptz NULL` | Confirmación de lectura del aviso en el portal de la socia. |
| `payload_digest` | `resumen_carga` | 3 tablas | `bytea / varchar(64)` | Hash SHA-256 de integridad para sincronización offline. |
| `result_code` | `resultado_codigo` | 3 tablas | `varchar(32)` | Código de respuesta de la idempotencia (éxito/conflicto). |

---

## 7. Verificación de Longitudes de Identificadores

### 7.1 Regla Django `models.E034` para Índices (`ix_` <= 30 caracteres)
| # | Nombre de Índice Propuesto | Longitud Real | Límite Django | Estado |
|:---:|---|:---:|:---:|:---:|
| 1 | `ix_mov_exist_cuenta_fecha` | **25** | 30 | **VÁLIDO** |
| 2 | `ix_asig_encarg_destinataria` | **27** | 30 | **VÁLIDO** |
| 3 | `ix_reg_asist_partic_fecha` | **26** | 30 | **VÁLIDO** |
| 4 | `ix_evento_acceso_suj_fecha` | **26** | 30 | **VÁLIDO** |
| 5 | `ix_linea_venta_cuenta_exis` | **26** | 30 | **VÁLIDO** |
| 6 | `ix_recibo_sinc_usuaria_op` | **26** | 30 | **VÁLIDO** |
| 7 | `ix_caso_falta_partic_est` | **25** | 30 | **VÁLIDO** |
| 8 | `ix_reparto_feria_estado` | **24** | 30 | **VÁLIDO** |
| 9 | `ix_multa_socia_estado` | **22** | 30 | **VÁLIDO** |
| 10 | `ix_actividad_inicio` | **19** | 30 | **VÁLIDO** |

### 7.2 Restricciones `ck_` y `uq_` (PostgreSQL <= 63 caracteres)
| # | Nombre de Restricción Propuesta | Longitud Real | Límite PostgreSQL | Estado |
|:---:|---|:---:|:---:|:---:|
| 1 | `ck_trazabilidad_movimiento_existencia_cantidad` | **46** | 63 | **VÁLIDO** |
| 2 | `uq_trazabilidad_reparto_feria_feria_version` | **43** | 63 | **VÁLIDO** |
| 3 | `uq_planificacion_asignacion_encargo_activa` | **42** | 63 | **VÁLIDO** |
| 4 | `uq_accounts_designacion_cargo_tipo_vigente` | **42** | 63 | **VÁLIDO** |
| 5 | `ck_asistencia_registro_hora_valida` | **34** | 63 | **VÁLIDO** |

### 7.3 Top 10 Nombres de Tablas/Vistas Nuevas Más Largos
| # | Nombre de Tabla o Vista Propuesta | Longitud Real | Límite PostgreSQL | Estado |
|:---:|---|:---:|:---:|:---:|
| 1 | `planificacion_version_politica_recordatorio` | **43** | 63 | **VÁLIDO** |
| 2 | `trazabilidad_recibo_sincronizacion_venta` | **40** | 63 | **VÁLIDO** |
| 3 | `trazabilidad_version_regla_reparto_feria` | **40** | 63 | **VÁLIDO** |
| 4 | `trazabilidad_estado_operacion_inventario` | **40** | 63 | **VÁLIDO** |
| 5 | `trazabilidad_vista_cierre_mensual_socia` | **39** | 63 | **VÁLIDO** |
| 6 | `trazabilidad_cuenta_por_cobrar_externa` | **38** | 63 | **VÁLIDO** |
| 7 | `trazabilidad_tipo_operacion_inventario` | **38** | 63 | **VÁLIDO** |
| 8 | `accounts_concesion_superadministracion` | **38** | 63 | **VÁLIDO** |
| 9 | `trazabilidad_estado_comprobante_manual` | **38** | 63 | **VÁLIDO** |
| 10 | `sitio_publico_tipo_evento_publicacion` | **37** | 63 | **VÁLIDO** |

---

## 8. Trazabilidad con Documentos Externos

Los siguientes documentos fuera de `docs/architecture/proposals/` conservan referencias a los nombres en inglés y deberán sincronizarse cuando se consolide la entrega académica:
- `documentacion/arquitectura/arquitectura_v1.2_2026-10-28.md`
- `docs/architecture/ARQUITECTURA-OBJETIVO.md`
- `docs/decisions/ADR-0006-monolito-modular-y-entrega-incremental.md`
- `docs/requirements/CAT-REQ-001.md`
- `documentacion/requisitos/requisitos_generales_v2.3_2026-10-28.md`
- `specs/001-acceso-usuarias-internas/spec.md` y `plan.md`
- `specs/002-superadministracion/spec.md`
- `app/config/settings/base.py`
