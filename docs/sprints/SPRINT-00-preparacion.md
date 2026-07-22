---
title: Sprint 0 - Preparación del proyecto
type: sprint
status: completed
number: 0
goal: preparar el espacio de trabajo documental y técnico
completed: 2026-07-21
closed_by: tesista
---

# Sprint 0 - Preparación del proyecto

## Objetivo

Dejar preparada una única fuente de contexto para el tesista, Obsidian y Codex. En este
sprint todavía no se programa la aplicación Django.

## Resultado esperado

Al terminar este sprint debe existir:

- Un repositorio/carpeta raíz para la tesis.
- El repositorio abierto como vault de Obsidian.
- `AGENTS.md` en la raíz.
- Contexto del anteproyecto cargado y revisado.
- Lista de decisiones pendientes.
- Bitácora de trabajo.
- Convención para requisitos y sprints.
- Un criterio claro para cerrar el sprint.
- Un flujo de especificaciones y agentes que no dependa de un modelo.

## Tareas

### S0-01 - Preparar la carpeta del proyecto

- [x] Descargar y descomprimir el starter.
- [x] Elegir la carpeta definitiva de la aplicación.
- [x] No guardar claves, contraseñas ni datos sensibles.
- [x] Mantener una copia del anteproyecto original fuera del repositorio.

### S0-02 - Abrir el proyecto como vault de Obsidian

- [x] Instalar Obsidian desde su sitio oficial.
- [x] Abrir la carpeta raíz del proyecto como vault.
- [x] Confirmar que se pueden abrir y editar los archivos Markdown.
- [x] Confirmar que el flujo principal funciona sin depender de plugins comunitarios.

### S0-03 - Revisar el contexto

- [x] Leer `agents/tesis/PROJECT_CONTEXT.md`.
- [x] Leer `agents/tesis/AGENT.md`.
- [x] Leer `agents/tesis/KNOWLEDGE_POLICY.md`.
- [x] Revisar el anteproyecto por separado y conservar el PDF original fuera del repositorio.

### S0-04 - Registrar decisiones pendientes

- [x] Resolver Comité vs. Asociación.
- [x] Confirmar el alcance de ventas y cuentas por cobrar.
- [x] Confirmar variables del proceso de secado.
- [x] Confirmar reglas de corrección y auditoría.
- [x] Confirmar perfiles y permisos reales.
- [x] Confirmar qué reportes necesita la organización.

### S0-05 - Probar Codex en modo lectura

Usar esta instrucción en la aplicación de Codex:

```text
Lee AGENTS.md, docs/00-inicio/00-dashboard.md,
docs/sprints/SPRINT-00-preparacion.md y todos los archivos de agents/tesis/.

La aplicación Django todavía no existe. No crees código ni modifiques archivos.
Devuelve únicamente:
1. Qué entendiste del proyecto.
2. Qué documentos encontró.
3. Qué decisiones siguen pendientes.
4. Qué información necesitas para comenzar el levantamiento de requisitos.
```

Resultado registrado en
[[../evidence/S0/2026-07-21-smoke-test-codex|smoke test de Codex para Sprint 0]].

### S0-06 - Preparar el arnés portable

- [x] Instalar Spec Kit 0.13.2 para Codex en modo skills.
- [x] Usar `.agents/skills/` como directorio común descubierto por Codex y Kimi Code.
- [x] Definir roles multiagente con lectura/escritura limitada.
- [x] Separar el agente Python educativo del camino crítico de la aplicación.
- [x] Crear contratos de fuente de verdad, trazabilidad, UX y cambio de modelo.
- [x] Registrar [[../evidence/S0/2026-07-21-verificacion-base-v3|evidencia técnica de la base]].
- [x] Ejecutar EVAL-01 y EVAL-02 de `evals/providers/SMOKE-TEST.md` con Codex; EVAL-03 a
      EVAL-05 quedan para la preparación de la implementación.
- [ ] (Opcional) Ejecutar EVAL-01 y EVAL-02 con Kimi o GLM, si existe acceso sin costo
      adicional y el tesista decide realizar la comparación.
- [x] Aprobar o corregir la Constitución y ADR-0002.

## Criterio de cierre

El Sprint 0 se cierra cuando el tesista confirme:

- [x] Obsidian abre correctamente la carpeta raíz.
- [x] Los enlaces principales funcionan; la Constitución se consulta desde VS Code por la
      limitación de Obsidian con carpetas ocultas.
- [x] El contexto no contiene datos personales innecesarios.
- [x] Las decisiones pendientes están revisadas.
- [x] Codex pudo leer el contexto sin programar.
- [x] La validación con un motor alternativo queda como opcional y no bloquea el avance;
      si se realiza, debe conservarse la evidencia y no cambiar el significado de la spec.
- [x] La Constitución y ADR-0002 fueron aceptados o reemplazados.

El cierre fue autorizado por el tesista el 2026-07-21 y está respaldado por
[[../evidence/S0/2026-07-21-verificacion-cierre-sprint-0|la verificación final de Sprint 0]].

## Fuera de alcance

- No instalar todavía Django.
- No crear modelos.
- No crear la base de datos.
- No diseñar pantallas definitivas.
- No implementar módulos.
- No depender de plugins comunitarios de Obsidian para el flujo principal.

## Validaciones opcionales posteriores

Kimi Code y GLM no son requisitos para cerrar Sprint 0 ni para iniciar el levantamiento de
requisitos. Podrán evaluarse posteriormente cuando exista acceso gratuito, saldo disponible
o una necesidad académica concreta de comparar motores. La versión del modelo se registrará
en la evidencia de la prueba y no se fija aquí.
