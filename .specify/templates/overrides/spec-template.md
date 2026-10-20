---
id: "[SPEC-ID]"
title: "[FEATURE NAME]"
type: feature-spec
status: draft
created: "[DATE]"
source:
  - "[anteproyecto|entrevista-fecha|observacion-fecha|decision]"
sprint: "[S1|S2|S3|S4|S5|fase-previa]"
module: "[acceso|planificacion|asistencia|trazabilidad|reportes|transversal]"
actors: []
validated_by: []
related: []
---

# Especificación: [FEATURE NAME]

- **Rama propuesta**: `[branch-name]`
- **Entrada del usuario**: "$ARGUMENTS"

## Control de validación

| Elemento | Valor |
|---|---|
| Estado | `draft` o `proposed`; nunca confirmar automáticamente |
| Fuente primaria | [fuente identificable] |
| Preparó | [persona/agente] |
| Debe validar | [tesista/directora/organización] |
| Fecha de validación | Pendiente |
| Evidencia | Pendiente |

## Problema, valor y alcance

- **Actor afectado**: [actor]
- **Problema observable**: [qué ocurre hoy]
- **Valor esperado**: [resultado útil, sin describir tecnología]
- **Incluye**: [límites]
- **No incluye**: [límites explícitos]
- **Incremento utilizable**: [recorrido y dependencias disponibles; no confundir con módulo completo].
- **Capacidades anteriores afectadas**: [comportamiento que debe conservarse o N/A justificado].

## Escenarios de usuario y pruebas (User Scenarios & Testing)

### HU-01 — [recorrido prioritario] (P1)

**Como** [actor], **quiero** [acción], **para** [valor].

**Prueba independiente**: [cómo demostrar valor sin depender de historias posteriores].

**Criterios de aceptación**:

1. **Dado** [estado], **cuando** [acción], **entonces** [resultado observable].
2. **Dado** [estado o rol no autorizado], **cuando** [acción], **entonces** [denegación/resultado].

### HU-02 — [recorrido] (P2)

[Repetir estructura solo si aporta un incremento independiente.]

### Excepciones y bordes

- [duplicado, dato ausente, valor límite, concurrencia, corrección, conectividad].
- [qué ve la usuaria y cómo se recupera].

## Requisitos (Requirements)

### Requisitos funcionales

- **RF-[MOD]-001**: El sistema debe [comportamiento comprobable].
  - **Fuente**: [fuente].
  - **Actor/permiso**: [actor autorizado y denegado].
  - **Criterios**: CA-RF-[MOD]-001-01, CA-RF-[MOD]-001-02.

### Requisitos no funcionales

- **RNF-[MOD]-001**: [atributo medible de usabilidad, seguridad, rendimiento o confiabilidad].
  - **Método de verificación**: [prueba o instrumento].

### Reglas de negocio

- **RN-[MOD]-001**: [regla validada, fuente y excepción].

### Datos y entidades clave

| Concepto | Significado para el negocio | Datos mínimos | Reglas/retención pendientes |
|---|---|---|---|
| [Entidad] | [significado] | [campos conceptuales] | [reglas] |

### Matriz mínima de permisos

| Operación | Directiva | Socia operaria | Visitante | Evidencia/fuente |
|---|---|---|---|---|
| [operación] | [permitir/denegar/pendiente] | [valor] | [valor] | [fuente] |

## Interfaz y experiencia

- Recorrido principal y número de pasos esperado.
- Estados vacío, carga, éxito, error y sin permiso.
- Comportamiento móvil y escritorio.
- Lenguaje, unidades y ayudas que deben validar las usuarias.
- Criterios de teclado, contraste y foco.

## Criterios de éxito (Success Criteria)

- **SC-001**: [resultado medible y agnóstico a la tecnología].
- **SC-002**: [tasa/tiempo/precisión/éxito de tarea].
- **SC-003**: [criterio de validación con usuarias].

## Trazabilidad académica

| Elemento | Enlace/ID |
|---|---|
| Objetivo específico | [OE-01/OE-02/OE-03] |
| Sprint | [Sx] |
| Requisitos | [RF/RNF] |
| ADR | [si aplica] |
| Casos de prueba | Pendiente de plan |
| Evidencia | Pendiente |
| ISO/IEC 25010:2023 | [completitud/corrección/pertinencia o N/A] |

## Supuestos y dependencias (Assumptions)

- [Supuesto explícito; no convertir en hecho].
- [Dependencia de decisión, dato, rol o infraestructura].
- [Dependencias de capacidades existentes; ejemplos de módulos futuros no amplían esta spec].
- [Necesidad de versiones coexistentes/offline, si existe; el detalle técnico pertenece al plan].

## Preguntas pendientes

- [NEEDS CLARIFICATION: pregunta material, responsable y fecha objetivo].

## Registro de validación

| Fecha | Participantes/rol | Decisión | Cambios | Evidencia |
|---|---|---|---|---|
| Pendiente | — | — | — | — |
