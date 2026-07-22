---
id: ADR-0002
title: Arnés portable de desarrollo asistido por IA
type: decision
status: accepted
date: 2026-07-21
module: transversal
accepted_by: tesista
accepted_date: 2026-07-21
tags:
  - proyecto/tesis
  - tipo/decision
  - modulo/transversal
---

# ADR-0002: Arnés portable de desarrollo asistido por IA

## Contexto

El starter recibido implementa un bucle educativo de chat, memoria SQLite y cuatro
herramientas. No puede inspeccionar, editar, ejecutar ni revisar la aplicación Django; por
tanto, no es todavía un agente de desarrollo. Además, el proyecto debe poder pasar de Codex
a Codex CLI, Kimi o GLM sin perder el proceso ni la documentación útil para la tesis.

## Decisión

1. Usar Git, Markdown, especificaciones y pruebas como núcleo independiente del proveedor.
2. Adoptar GitHub Spec Kit 0.13.2 para el ciclo especificar → aclarar → planificar → crear
   tareas → analizar → implementar.
3. Versionar una sola copia de las skills en `.agents/skills/`: Codex las usa mediante su
   integración Spec Kit y Kimi Code descubre oficialmente ese directorio genérico.
4. Usar `AGENTS.md` como contrato común y `.codex/agents/` solo como especialización de roles.
5. Mantener selección de modelo, credenciales y proveedor fuera del repositorio.
6. Usar Codex app/CLI como motor principal. Mantener Kimi Code y GLM como caminos
   alternativos opcionales, sin convertirlos en dependencia del proyecto ni del cierre de
   Sprint 0.
7. No hacer obligatorio un gateway. Solo evaluar LiteLLM u otro traductor si existe la
   necesidad comprobada de ejecutar GLM/Kimi dentro de Codex CLI mediante Responses API.
8. Conservar el arnés Python recibido en `tools/agent-lab/` como material educativo, fuera
   del camino crítico de la aplicación.

## Motivos

- Spec Kit guarda artefactos legibles y soporta múltiples agentes sin imponer un modelo.
- Spec Kit mantiene la integración de Codex y Kimi Code admite las skills genéricas de
  `.agents/skills/`, evitando una instalación múltiple que Spec Kit marca como no segura.
- El cambio de motor conserva requisitos, decisiones, tareas, pruebas y memoria Obsidian.
- La configuración local evita filtrar claves y permite probar proveedores sin cambiar Git.
- Se reduce el esfuerzo dedicado a replicar editores, shell, Git, sandboxes y revisión que
  los agentes de código ya implementan.

## Consecuencias

### Positivas

- El trabajo se puede auditar y reutilizar en la tesis.
- Un proveedor distinto puede ejecutar el mismo plan y ser evaluado con los mismos casos.
- Los agentes especializados tienen permisos y responsabilidades explícitas.
- El desarrollo sigue centrado en Django y en valor funcional.

### Costes y riesgos

- Las instrucciones de invocación cambian entre motores.
- Un modelo puede interpretar herramientas de forma distinta; se requieren pruebas de humo.
- Kimi Code y otros agentes evolucionan rápidamente, por lo que las versiones deben
  registrarse si se realiza una comparación posterior.
- La compatibilidad “OpenAI” no garantiza equivalencia completa de tool calling,
  razonamiento o Responses API.

## Alternativas descartadas por ahora

- **Ampliar el arnés Python hasta convertirlo en agente de código**: duplica shell, editor,
  Git, permisos, sandbox, subagentes y trazas antes de construir la aplicación.
- **BMAD completo**: aporta muchos roles y flujos, pero superpone una metodología pesada a
  los sprints ya definidos en el anteproyecto.
- **OpenSpec como flujo principal**: es ligero y válido, pero Spec Kit ofrece skills
  reutilizables por los motores elegidos y personalización de plantillas.
- **Gateway obligatorio**: simplifica una URL, pero agrega operación, transformación y otro
  punto de fallo sin necesidad actual.

## Validación técnica de adopción

- [x] El tesista aprueba este ADR.
- [x] Codex puede leer la constitución y producir una especificación sin implementar.
- [ ] (Opcional) Kimi Code puede leer los mismos artefactos y producir un resultado
      equivalente.
- [ ] (Opcional) GLM, en la versión disponible al momento de la prueba, supera los casos
      mínimos de `evals/providers/SMOKE-TEST.md`.
- [x] Las pruebas obligatorias de adopción no dejan credenciales o datos personales en el
      repositorio.

Las dos validaciones alternativas anteriores son evidencia complementaria: su ausencia no
bloquea Sprint 0, la especificación de requisitos ni la implementación posterior. Si se
ejecutan, deben respetar la política de secretos y registrarse sin exponer claves.

## Referencias

- [GitHub Spec Kit](https://github.com/github/spec-kit)
- [Kimi Code](https://github.com/MoonshotAI/kimi-code)
- [Configuración avanzada de Codex](https://learn.chatgpt.com/docs/config-file/config-advanced)
- [Integración de herramientas de Z.AI](https://docs.z.ai/devpack/tool/others)
