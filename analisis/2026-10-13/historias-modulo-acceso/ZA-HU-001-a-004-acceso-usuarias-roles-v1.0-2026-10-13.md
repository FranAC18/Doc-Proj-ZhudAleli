---
codigo: ZA-HU-001
titulo: Historias de usuaria y BDD del módulo de acceso
modulo: Acceso de usuarias y roles
fase: Fase 3 — Historias de usuario y BDD
version: 1.0
fecha: 2026-10-13
autor: Franklin Acero (tesista)
analista: Codex (asistencia de redacción)
estado: propuesta-para-revision
sprint: S2
module: acceso
related:
  - "[[../../../documentacion/historias/usuario/historias_usuario_v2.5_2026-10-13]]"
  - "[[../../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13]]"
  - "[[../casos-uso/ZA-CU-001-acceso-usuarias-y-roles-v1.0-2026-10-13]]"
  - "[[../alcances-modulos/ZA-ALC-001-acceso-usuarias-y-roles-v1.1-2026-10-13]]"
tags:
  - proyecto/tesis
  - tipo/requisito
  - sprint/s2
  - modulo/acceso
publicacion: no-preparado
---

<table style="width:100%;border-collapse:collapse;font-family:'Heebo Light',Heebo,Arial,sans-serif;">
<tr><td colspan="2" style="background:#642138;color:#F0EAC8;padding:14px;font-family:'Mallong Regular',Georgia,serif;font-size:22px;"><strong>[LOGO: Isotipo floral de 4 pétalos - ZHUD ALELÍ Productos Naturales]</strong><br>ZA-HU-001 · Historias de usuaria y BDD del módulo de acceso</td></tr>
<tr><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Control documental</th><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Valor</th></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Módulo</td><td style="padding:7px;border:1px solid #AC6E40;">Acceso de usuarias y roles (<code>accounts</code>)</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Fase / entregable</td><td style="padding:7px;border:1px solid #AC6E40;">Fase 3 — Historias de usuario y BDD (Gherkin)</td></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Versión / fecha</td><td style="padding:7px;border:1px solid #AC6E40;">v1.0 / 13 de octubre de 2026</td></tr>
<tr><td style="padding:7px;border:1px solid #AC6E40;">Autor / analista</td><td style="padding:7px;border:1px solid #AC6E40;">Franklin Acero (tesista) / Codex (asistencia de redacción)</td></tr>
<tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Estado</td><td style="padding:7px;border:1px solid #AC6E40;">Propuesta interna para revisión; no aprobada ni publicada</td></tr>
</table>

**Historial de revisiones**

| Versión | Fecha | Descripción | Responsable |
|---|---|---|---|
| v1.0 | 2026-10-13 | Conversión de las cuatro historias generales de acceso a escenarios BDD/Gherkin trazables, sin alterar CAT-REQ-001. | Franklin Acero; redacción asistida por Codex |

## 1. Propósito y relación con las historias generales

Este documento añade criterios verificables en formato Gherkin a las cuatro historias de acceso que ya existen en el compendio general. Conserva sus referencias `HU-ACC-001` a `HU-ACC-004` y las mapea a códigos de presentación `ZA-HU-001` a `ZA-HU-004` para esta secuencia modular. **No crea cuatro requisitos nuevos ni reemplaza la fuente general de historias.**

La importancia se copia de la priorización aprobada v1.3. La clasificación MoSCoW se muestra como propuesta de correspondencia para revisión: `Esencial → Must`, `Alta → Should`, `Complementaria → Could`. No se atribuye aprobación a esa conversión. Los puntos quedan pendientes de estimación del equipo, igual que en la fuente general; el orden de la pila no se usa como estimación.

## 2. Historias de usuario y criterios BDD

### ZA-HU-001 — Entrar y salir de la parte privada

| Campo | Dato |
|---|---|
| Código modular | ZA-HU-001 |
| Código de historia general | HU-ACC-001 |
| Requisito de origen | RF-ACC-001 |
| Caso(s) de uso relacionado(s) | ZA-CU-ACC-001; ZA-CU-ACC-002 |
| Usuario | Usuaria interna con cuenta activa |
| Prioridad de negocio | Esencial |
| MoSCoW | Must — propuesta de correspondencia, pendiente de revisión |
| Puntos estimados | Pendiente de estimación del equipo |
| Riesgo en desarrollo | Pendiente de evaluar |
| Sprint propuesto | S2, según la pila vigente |

**Narrativa:** Como usuaria interna con cuenta activa, quiero iniciar y cerrar sesión, para proteger mi información organizacional.

**Criterios de aceptación**

```gherkin
Característica: Acceso a la parte privada

  Escenario: Acceso con una cuenta activa y credenciales válidas
    Dado que existe una cuenta interna activa asociada a una membresía habilitada
    Y la usuaria dispone de credenciales válidas
    Cuando inicia sesión
    Entonces el sistema permite el acceso autenticado
    Y solo muestra contenido autorizado para esa usuaria

  Escenario: Rechazo de credenciales inválidas o cuenta inactiva
    Dado que la usuaria intenta acceder a la parte privada
    Cuando las credenciales son inválidas o su cuenta/membresía está inactiva
    Entonces el sistema rechaza el acceso
    Y no revela información privada ni confirma si la cuenta existe

  Escenario: La usuaria cierra su sesión
    Dado que la usuaria mantiene una sesión autenticada
    Cuando selecciona cerrar sesión
    Entonces el sistema invalida el contexto autenticado
    Y una nueva solicitud privada exige autenticación y autorización vigentes
```

**Trazabilidad:** RNF-SEC-001; RNF-PRV-001. Dependencias existentes: HT-GEN-001 y HT-GEN-002.

### ZA-HU-002 — Administrar membresías

| Campo | Dato |
|---|---|
| Código modular | ZA-HU-002 |
| Código de historia general | HU-ACC-002 |
| Requisito de origen | RF-ACC-002 |
| Caso(s) de uso relacionado(s) | ZA-CU-ACC-003 |
| Usuario | Integrante autorizada de la Directiva |
| Prioridad de negocio | Alta |
| MoSCoW | Should — propuesta de correspondencia, pendiente de revisión |
| Puntos estimados | Pendiente de estimación del equipo |
| Riesgo en desarrollo | Pendiente de evaluar |
| Sprint propuesto | S2, según la pila vigente |

**Narrativa:** Como integrante autorizada de la Directiva, quiero activar o desactivar membresías de socias, para mantener vigentes los accesos sin perder la historia.

**Criterios de aceptación**

```gherkin
Característica: Administración de membresías

  Escenario: Directiva desactiva una membresía
    Dado que una integrante de la Directiva está autorizada para administrar membresías
    Y la membresía de la socia existe
    Cuando la Directiva la desactiva e indica el motivo
    Entonces el sistema impide nuevos accesos asociados a esa membresía
    Y conserva los registros históricos
    Y registra quién realizó el cambio, cuándo, el estado anterior y el nuevo, la autorización y el motivo

  Escenario: Una usuaria sin permiso intenta cambiar una membresía
    Dado que una usuaria no tiene permiso para administrar membresías
    Cuando intenta cambiar el estado de una membresía, incluso mediante una solicitud directa
    Entonces el sistema deniega la operación en el servidor
    Y no modifica datos ni revela información privada

  Escenario: Falla el registro atómico del cambio
    Dado que una integrante autorizada confirma un cambio de membresía
    Cuando el sistema no puede guardar el cambio junto con su auditoría
    Entonces revierte la operación completa
    Y no comunica que el cambio quedó aplicado
```

**Trazabilidad:** RNF-SEC-001; RNF-AUD-001; RNF-DAT-001. Dependencias existentes: HU-ACC-001 y HT-GEN-002.

### ZA-HU-003 — Usar funciones según responsabilidades

| Campo | Dato |
|---|---|
| Código modular | ZA-HU-003 |
| Código de historia general | HU-ACC-003 |
| Requisito de origen | RF-ACC-003 |
| Caso(s) de uso relacionado(s) | ZA-CU-ACC-004 |
| Usuario | Usuaria interna |
| Prioridad de negocio | Esencial |
| MoSCoW | Must — propuesta de correspondencia, pendiente de revisión |
| Puntos estimados | Pendiente de estimación del equipo |
| Riesgo en desarrollo | Pendiente de evaluar |
| Sprint propuesto | S2, según la pila vigente |

**Narrativa:** Como usuaria interna, quiero realizar solo operaciones permitidas por mi perfil, cargo o encargo, para respetar las responsabilidades de la organización.

**Criterios de aceptación**

```gherkin
Característica: Autorización por responsabilidad

  Escenario: La operación está permitida para la usuaria
    Dado que la usuaria está autenticada
    Y su perfil, cargo o encargo vigente tiene el permiso requerido por esa operación
    Cuando solicita la operación
    Entonces el servidor autoriza únicamente esa operación
    Y el módulo propietario aplica sus reglas de negocio y valida su escritura

  Escenario: El cargo no autoriza la operación
    Dado que una usuaria autenticada no tiene el cargo o permiso requerido
    Cuando intenta realizar una operación restringida
    Entonces el servidor deniega la solicitud
    Y no modifica datos

  Escenario: El encargo ya venció
    Dado que la usuaria tuvo un encargo temporal relacionado con la operación
    Y el periodo del encargo terminó
    Cuando intenta la operación, incluso por acceso directo
    Entonces el servidor deniega la solicitud
    Y no modifica datos

  Escenario: El permiso específico aún no está definido
    Dado que la especificación propietaria de una operación no define el permiso requerido
    Cuando una usuaria intenta esa operación
    Entonces el sistema no infiere ni concede el permiso
    Y registra la falta como una definición pendiente para la especificación responsable
```

**Trazabilidad:** RNF-SEC-001; RNF-PRV-001. Dependencias existentes: HU-ACC-001 y HT-GEN-002. Los permisos concretos por operación se definirán en la especificación del módulo propietario; esta historia no los fija universalmente.

### ZA-HU-004 — Ver mis opciones disponibles

| Campo | Dato |
|---|---|
| Código modular | ZA-HU-004 |
| Código de historia general | HU-ACC-004 |
| Requisito de origen | RF-ACC-004 |
| Caso(s) de uso relacionado(s) | ZA-CU-ACC-005 |
| Usuario | Usuaria interna |
| Prioridad de negocio | Complementaria |
| MoSCoW | Could — propuesta de correspondencia, pendiente de revisión |
| Puntos estimados | Pendiente de estimación del equipo |
| Riesgo en desarrollo | Pendiente de evaluar |
| Sprint propuesto | S2, según la pila vigente |

**Narrativa:** Como usuaria interna, quiero consultar mis actividades, pendientes y encargos disponibles, para saber qué puedo hacer ahora.

**Criterios de aceptación**

```gherkin
Característica: Inicio privado personalizado

  Escenario: La usuaria consulta su información actual
    Dado que la usuaria mantiene una sesión autenticada
    Cuando abre su inicio privado
    Entonces ve únicamente actividades, pendientes y encargos que le corresponden
    Y ve solo acciones disponibles para su situación actual

  Escenario: La usuaria no tiene actividades ni pendientes
    Dado que la usuaria tiene una sesión autenticada
    Y no existen actividades, pendientes ni encargos asignados a ella
    Cuando abre su inicio privado
    Entonces el sistema presenta un estado vacío comprensible
    Y no lo muestra como un error

  Escenario: La autorización cambia antes de ejecutar una acción
    Dado que una acción se mostró como disponible en el inicio privado
    Y el permiso deja de estar vigente antes de ejecutarla
    Cuando la usuaria selecciona la acción
    Entonces el servidor vuelve a comprobar la autorización y deniega el acceso
    Y mantiene los datos sin cambios
```

**Trazabilidad:** RNF-UX-001, RNF-UX-002, RNF-UX-003 y RNF-PRV-001. Dependencias existentes: HU-ACC-001 y HU-ACC-003.

## 3. Cobertura y controles de alcance

| Historia general | Requisito confirmado | Casos BDD incluidos | Estado de la cobertura |
|---|---|---|---|
| HU-ACC-001 | RF-ACC-001 | ZA-HU-001 | Inicio con acceso válido, rechazo seguro y salida. |
| HU-ACC-002 | RF-ACC-002 | ZA-HU-002 | Activación/desactivación, permiso denegado e integridad de auditoría. |
| HU-ACC-003 | RF-ACC-003 | ZA-HU-003 | Operación permitida, cargo incorrecto, encargo vencido y permiso sin definir. |
| HU-ACC-004 | RF-ACC-004 | ZA-HU-004 | Inicio privado, estado vacío y revalidación de la acción. |

No se especifican alta de cuentas, recuperación/cambio de contraseña, políticas de sesión, roles universales por cargo, acceso privado de visitantes, autenticación offline ni reglas propias de asistencia, multas, producción, ventas o reportes. Las faltas y multas aprobadas pertenecen al módulo de asistencia.

## 4. Fuentes y decisiones propuestas

- [[../../../documentacion/historias/usuario/historias_usuario_v2.5_2026-10-13|Historias de usuario v2.5]]: cuatro historias generales de acceso y sus criterios existentes; prioridad y estimación según estado publicado.
- [[../../../documentacion/requisitos/requisitos_generales_v2.0_2026-10-13|Requisitos generales v2.0]]: RF-ACC-001 a RF-ACC-004 y RNF asociados.
- [[../../../documentacion/requisitos/priorizacion/priorizacion_requisitos_v1.3_2026-10-13|Priorización v1.3]]: importancia Esencial/Alta/Complementaria.
- [[../casos-uso/ZA-CU-001-acceso-usuarias-y-roles-v1.0-2026-10-13|ZA-CU-001 v1.0]], propuesta de casos detallados.
- [[../alcances-modulos/ZA-ALC-001-acceso-usuarias-y-roles-v1.1-2026-10-13|ZA-ALC-001 v1.1]], alcance modular base.

**Pendiente de decisión del tesista:** confirmar si desea adoptar la conversión MoSCoW propuesta o mantener únicamente los niveles de importancia existentes. Los puntos, riesgo y responsable requieren estimación/asignación del equipo. Esta propuesta no cambia el estado de aprobación de las historias generales ni se incorpora todavía a `documentacion/`.
