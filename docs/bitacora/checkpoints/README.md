---
title: Checkpoints de avance
type: index
---

# Checkpoints de avance

Aquí se guardan pausas, avances parciales, bloqueos y cierres de tareas.

Un checkpoint no cierra la tarea por sí solo. Debe indicar evidencia, pendiente y próxima
acción.

## Handoff entre herramientas

Para cambiar de Codex a Antigravity, OpenCode u OpenChamber, usa
`[[../../templates/PLANTILLA-HANDOFF-UNIVERSAL]]`. El handoff debe registrar la tarea, fase,
escritor, rutas permitidas, archivos modificados, pruebas, bloqueos, próxima acción, rama y
estado del commit.

Un proveedor agotado no autoriza a cambiar de alcance. La herramienta siguiente lee el último
handoff, confirma la raíz del vault y verifica `git status` antes de escribir.
