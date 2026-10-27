# Checklist de calidad: Administración organizacional y configuración por módulos

- **Propósito**: comprobar si la propuesta está lista para validación y, más adelante, aprobación; el estado actual no supera la puerta de requisitos.
- **Fecha**: 2026-10-27
- **Spec**: [SPEC-002](../spec.md)
- **Estado**: `incomplete`; hay preguntas materiales y validación directa pendiente.

## Fuente y alcance

- [x] Actor y problema reportados; la persona real que tendrá autoridad aún debe definirse.
- [x] Fuente identificada con fecha y atribución correcta: la presidenta es citada por el tesista; falta su validación directa.
- [x] Propuesta separada de requisito confirmado; `RF-ACC-005` es candidato, `SPEC-002` es `proposed`.
- [x] Incluye, excluye, supuestos y dependencias explícitos.
- [ ] Aclarar alcance de «cualquier dato» y las categorías/campos que la Superadministradora podrá consultar.
- [ ] Identificar quién crea y transfiere la autoridad y si se requiere doble aprobación.

## Requisitos

- [x] `RF-ACC-005` se identifica como código candidato, pendiente de confirmación del tesista.
- [x] Los escenarios y criterios propuestos incluyen casos permitidos y denegados.
- [ ] Acordar estado de cuenta, sesiones y efecto temporal de revocación de permisos.
- [ ] Validar rangos y parámetros de acceso; revisar y actualizar SPEC-001 antes de activar cambios.
- [ ] Definir unidades, gramática, precisión, redondeo, validación y vigencia para cada fórmula de cada módulo.
- [ ] Definir reglas de corrección, reversión, efectos derivados y aprobación por categoría de dato.
- [ ] Confirmar prioridad del incremento y su ubicación futura respecto al plan vigente.

## Seguridad y datos

- [x] La matriz identifica acciones, recursos, resultados permitidos y denegaciones; permisos aplicados en backend.
- [x] Se excluyen CRUD genérico, acceso directo a DB, `is_staff`/`is_superuser` como autoridad y autoelevación.
- [x] Se prevén pruebas negativas y conservación de evento original/auditoría.
- [x] Contraseñas existentes, tokens, secretos y edición/borrado de auditoría quedan excluidos.
- [ ] Definir minimización, visibilidad y retención por tipo de dato, especialmente datos personales y consultas de intentos.
- [ ] Acordar proceso de recuperación de cuentas antes de incluirlo en alcance.
- [ ] Definir mecanismo de invalidación de permisos/sesiones, incluidos clientes PWA.
- [x] No se afirma cumplimiento normativo; las referencias OWASP/NIST sustentan contexto, no certificación.

## Experiencia de uso

- [x] Se propone un panel delimitado por módulo, operaciones y permisos disponibles.
- [x] Se identifican estados de éxito, error, denegación, permiso revocado y conflicto de vigencia.
- [ ] Validar móvil, teclado, foco y contraste mediante recorridos con usuarias.
- [ ] Validar lenguaje, nombres de acciones, formularios y ayudas con personas que usarán el panel.
- [ ] Definir tarea y medida observable para prueba de usabilidad.

## Trazabilidad y cierre

- [x] Requisito y fuente reportada enlazados; no se inventa evidencia de aprobación.
- [x] Sprint marcado sin asignación; se conserva intacto el plan S1–S6 y el alcance de S2.
- [x] Plan de verificación indicado como pendiente de diseño tras validar requisitos.
- [ ] Confirmar objetivo de tesis, persona validadora, alcance y evidencia de validación.
- [ ] Revisión de la spec y checklist antes de permitir que `speckit-implement` procese la funcionalidad.

## Hallazgos

| Severidad | Evidencia | Responsable | Resolución |
|---|---|---|---|
| Alta | El pedido amplio de «cualquier dato» no determina lectura, modificación, bajas o correcciones históricas; el tesista excluye una autoridad universal de edición. | Tesista y presidenta | Resolver P-SUP-01; la propuesta bloquea la edición genérica y deja lectura amplia pendiente. |
| Alta | No consta quién origina o transfiere la autoridad administrativa ni si necesita doble aprobación. | Presidenta y tesista | Resolver P-SUP-02/03 antes de emitir autoridad. |
| Alta | Los parámetros configurables contradicen los valores confirmados de SPEC-001 si se activan sin revisión. | Tesista | Conservar 3 fallos/3 minutos/3 minutos; revisar SPEC-001 y validarlo antes de permitir configuración. |
| Alta | No constan propietarios ni reglas validadas para fórmulas/catálogos de módulos futuros. | Tesista y responsables de módulos | Acordar contratos y reglas módulo por módulo antes de exponer configuración. |
| Media | El almacén observado de intentos de login guarda un estado temporal HMAC, no historial por persona. | Tesista y responsable de privacidad | Decidir si se requiere historial y su minimización/retención antes de diseñarlo. |

## Historial de cambios

| Versión | Fecha | Estado | Cambio |
|---|---|---|---|
| 0.1 | 2026-10-27 | `incomplete` | Checklist inicial de calidad para SPEC-002; conserva las decisiones pendientes como hallazgos. |
