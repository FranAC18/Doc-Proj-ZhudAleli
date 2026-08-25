---
title: Flujo multiagente del proyecto
type: architecture
status: accepted
date: 2026-07-21
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
---

# Flujo multiagente del proyecto

## Objetivo

Usar especialización y revisión independiente sin convertir el proyecto en un conjunto de
agentes que modifican los mismos archivos. El coordinador conserva contexto, asigna límites
y presenta el resultado al tesista.

```mermaid
flowchart TD
    C["Codex / coordinador"] --> R["Requirements: solo lectura"]
    C --> A["Architect o UX: solo lectura"]
    R --> C
    A --> C
    C --> G1["Handoff de diseño"]
    G1 --> AG["Antigravity + Gemini: análisis opcional"]
    AG --> C
    C --> I["OpenCode / OpenChamber: implementer"]
    I --> V["Reviewer: solo lectura"]
    V --> C
    C --> D["Documenter: pre_commit"]
    D --> G["Git-manager: autorización y commit"]
    G --> P["Documenter: post_commit con hash"]
    P --> H["Cierre humano"]
```

No se ejecutan todos los roles en cada tarea. Un cambio de texto puede necesitar solo
coordinador y reviewer; una funcionalidad sensible puede necesitar análisis, UX,
implementación y revisión.

El diagrama muestra hosts posibles, no una obligación de usar todos. OpenChamber es la
interfaz visual de OpenCode; Antigravity es un carril de análisis/documentación con Gemini;
Codex mantiene la coordinación y las puertas de cierre hasta que otro host supere el smoke
test universal.

## Cuándo paralelizar

Es seguro paralelizar:

- análisis de requisitos y revisión UX, ambos sin editar;
- exploración de módulos diferentes sin archivos compartidos;
- pruebas de distintos recorridos después de una implementación estable;
- implementaciones en worktrees separados cuando no comparten migraciones, settings,
  plantillas base ni contratos.

No es seguro paralelizar:

- dos cambios al mismo modelo o migración;
- navegación base y pantallas que dependen de esa navegación;
- varios escritores de dashboard, matriz, sprint o ADR;
- implementación mientras el requisito todavía cambia;
- cambios de dependencias o settings por más de un agente.

## Contrato de asignación

Toda tarea delegada incluye:

```yaml
task_id: TXXX
requirement_ids: [RF-XXX]
objective: resultado observable
allowed_paths: []
forbidden_paths: []
inputs: []
expected_tests: []
write_owner: nombre-del-agente
handoff_to: coordinator
```

Si falta alguno de estos datos y el vacío puede alterar alcance o archivos, el agente debe
detenerse y pedir precisión.

La misma asignación se persiste en `docs/templates/PLANTILLA-HANDOFF-UNIVERSAL.md` para que
otra herramienta pueda continuar sin el historial privado del host anterior.

## Contrato de entrega

El agente devuelve:

- estado: `completed`, `partially-complete` o `blocked`;
- archivos leídos y, si aplica, modificados;
- decisiones y supuestos;
- comandos ejecutados con resultado real;
- criterios cubiertos y no cubiertos;
- riesgos, conflictos y próximo paso.

Solo el coordinador actualiza la matriz y propone el cierre. El documenter registra el
handoff pre_commit y la evidencia post_commit. El git-manager requiere autorización expresa
para cada commit. Solo el tesista autoriza Git externo, acepta cambios de alcance y decide
si un documento aprobado debe modificarse.

## Cambio de proveedor o cuota

Si Codex, Google AI Pro u OpenCode Go llega a un límite, se detiene el escritor actual y se
registra `partially-complete`, `commit: pending`, archivos, pruebas y `next_action`. El host
siguiente lee el handoff, confirma la raíz y continúa la misma tarea. No se cambia de host con
dos escritores activos en el mismo worktree.

## Roles adicionales

- `documenter`: registra sesiones, checkpoints, evidencias y propuestas en rutas permitidas;
  no modifica documentos aprobados.
- `git-manager`: valida el diff y crea commits solo con autorización explícita; no hace push
  ni reescribe historia.

## Límites iniciales

- Máximo tres hilos de agente abiertos.
- Profundidad uno: los subagentes no delegan.
- Un implementador por worktree.
- Ninguna fusión automática.
- Revisión independiente obligatoria para autenticación, permisos, asistencia, trazabilidad,
  inventario y migraciones de datos.
