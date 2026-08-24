---
title: "Agente — Arquitecto"
canonical_id: architect
type: agent
kind: host-role
status: active
sandbox: read-only
tags:
  - proyecto/tesis
  - tipo/agente
  - estado/activo
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
source_path: ".codex/agents/architect.toml"
---

# Agente — Arquitecto

## Propósito

Revisar límites del monolito Django, datos, RBAC, transacciones, migraciones, auditoría y estrategia de pruebas.

## Entradas y salidas

- Entradas: `AGENTS.md`, constitución, especificaciones, plan, código y políticas.
- Salidas: decisiones, riesgos, opciones y borradores ADR para el agente raíz.

## Skills relacionadas

- [[skill-speckit-plan]]
- [[skill-speckit-analyze]]

La relación es documental; el TOML no declara una lista ejecutable de skills.

## Límites

- Solo lectura.
- No implementa.
- No propone microservicios, SPA ni capas genéricas sin necesidad demostrada.

## Ubicación real

- Configuración: `.codex/agents/architect.toml`.
- Nota: `docs/01-agentes/agente-architect.md`.
