---
title: "Auditoría de agentes y skills — 2026-08-24"
type: audit
status: completed
tags:
  - proyecto/tesis
  - tipo/auditoria
  - estado/completado
verified_at: "2026-08-24"
verified_against_commit: "9bb3d50"
related:
  - "[[moc-agentes-y-skills]]"
  - "[[moc-agentes]]"
  - "[[moc-skills]]"
---

# Auditoría de arquitectura de agentes y skills

## Alcance

Auditoría documental y estructural previa a Django. No se instaló Django, no se agregaron funcionalidades y no se modificó el código del laboratorio.

## Hechos verificados

- Existen cinco roles en `.codex/agents/`.
- Existen diez skills en `.agents/skills/`.
- Las diez skills aparecen en el manifiesto de Codex y sus hashes son correctos.
- El identificador técnico del agente redactor es `requirements`.
- No existe un archivo de agente llamado `redactor`.
- No hay una matriz ejecutable que relacione agentes y skills.
- El laboratorio Python y el arnés host son capas distintas.
- El árbol local contiene cambios de código sin commit.
- La rama local contiene dos commits documentales que aún no están en `origin/main`.

## Inconsistencias

| Área | Problema | Severidad | Acción |
|---|---|---|---|
| Rutas del vault | `ObsidianStore` y la configuración usan rutas relativas que dependen del directorio de ejecución. | Alta | Fijar la raíz del proyecto y proteger los destinos de escritura. |
| Fuente de verdad | ADR-0004 describe como aceptado código que todavía no está integrado al remoto. | Alta | Separar estado local, commiteado y remoto. |
| Aprobaciones | Las herramientas de escritura no aplican de forma central la aprobación declarada. | Alta | Definir y probar una política efectiva. |
| Modelos | La matriz documental y el registro actual no coinciden completamente. | Media | Mantener una única lista verificada. |
| Agentes | Las skills usadas por cada agente no están declaradas en los TOML. | Media | Mantener la relación en la matriz documental. |
| Vault | No existían notas individuales para agentes y skills. | Media | Crear notas canónicas y MOCs. |
| Enlaces | Tres enlaces parecen ejemplos no resueltos: `RF-001-autenticacion`, `Tarea-configurar-rbac` y `SPRINT-01-acceso`. | Baja | Marcarlos como ejemplos o crear las notas. |

## Decisiones confirmadas

- `requirements` será el único nombre técnico.
- “Redactor de requisitos” será el nombre visible.
- Las rutas físicas actuales se conservan.
- La navegación se organiza con MOCs en el vault.
- El primer problema técnico posterior será la determinación segura de la raíz del vault.

## Plan posterior condicionado

1. Separar formalmente las capas host, skills, laboratorio y vault.
2. Hacer deterministas las rutas del vault.
3. Aplicar aprobación efectiva a las herramientas de escritura.
4. Alinear modelos, validación de configuración y documentación.
5. Integrar el código seleccionado y verificar un clon limpio.

## Estado de verificación

Esta nota refleja el análisis del árbol local al 2026-08-24. El código no commiteado no debe considerarse parte del estado portable hasta integrarse y verificarse desde un clon limpio.
