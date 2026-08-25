---
title: Auditoría experta de agentes, modelos de IA y portabilidad de arnés
type: architecture-audit
status: completed
date: 2026-08-24
author: Consultor Experto en Agentes y Modelos de IA
related:
  - "[[CONTRATO-UNIVERSAL-ORQUESTADORES]]"
  - "[[RUTAS-MODELOS-IA]]"
  - "[[../00-inicio/00-dashboard]]"
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/agentes
---

# Auditoría de Agentes, Modelos de IA e Inconsistencias Lógicas

## 1. Resumen Ejecutivo

Se realizó una evaluación integral de la arquitectura del arnés multiagente, las configuraciones de enrutamiento de modelos de IA (`tools/agent-routes.toml`), la compatibilidad entre hosts (Codex, Antigravity, OpenCode/OpenChamber), los adaptadores del laboratorio (`tools/agent-lab`) y las reglas de gobierno de Git.

El diseño general destaca por una excelente separación de responsabilidades basadas en **contratos canónicos de roles** y una política de portabilidad resguardada en Markdown. No obstante, el peritaje técnico identificó **inconsistencias menores de nombrado, alias de modelos y comandos de ejecución**, las cuales se detallan a continuación.

---

## 2. Hallazgos e Inconsistencias Identificadas

### H-01: Discrepancia en la Convención de Nombres de Roles (`git-manager` vs `git_manager`)
- **Descripción:** En la especificación canónica (`agents/tesis/roles/git-manager.md`), los adaptadores (`.codex/agents/git-manager.toml`, `.opencode/agents/git-manager.md`) y el sistema de archivos, el nombre del rol utiliza un guión medio (`git-manager`). Sin embargo, en la clave de configuración de `tools/agent-routes.toml` y en `tools/validate-universal.py`, la clave figuraba como `git_manager` (con guión bajo).
- **Impacto:** Si un orquestador intenta resolver la ruta en el archivo TOML utilizando la cadena exacta del rol (`git-manager`), podría generar un fallo de resolución si no se implementa una normalización implícita de guiones.
- **Recomendación:** Mantener soporte y resolución transparente para ambas notaciones (`git-manager` y `git_manager`) tanto en el validador como en la resolución dinámica de variables de entorno.

### H-02: Identificadores Hipotéticos de Modelos vs Identificadores Comerciales de API
- **Descripción:** En `tools/agent-routes.toml` y `RUTAS-MODELOS-IA.md` se referencian nombres como `gpt-5.6-luna`, `deepseek-v4`, `glm-5.2` y la serie `gemini-3.x-flash/pro`.
- **Impacto:** Aunque estas denominaciones representan la abstracción de rutas del proyecto, al realizar invocaciones HTTP directas contra los endpoints de proveedores oficiales (OpenAI, Google AI Studio, DeepSeek API), la API retornará un error `404 Model Not Found` si no existe un mapa explícito de traducción hacia modelos vigentes (`gemini-2.5-flash`, `gemini-2.5-pro`, `gpt-4o`, `deepseek-chat`).
- **Recomendación:** El laboratorio `tools/agent-lab/src/agent_harness/config.py` ya registra correctamente los modelos `gemini-2.5-pro` y `gemini-2.5-flash`. Se recomienda mantener una capa de mapeo de alias en el `ModelRouter` que traduzca automáticamente IDs ficticios/futuros a sus equivalentes de producción cuando se ejecuten llamadas reales.

### H-03: Comando de Verificación de Laboratorio en Entornos con `uv`
- **Descripción:** En `AGENTS.md` se estipula ejecutar `pytest -q tools/agent-lab/tests`. En entornos Windows donde `pytest` no está instalado en el PATH global del sistema (sino gestionado via `uv`), el comando directo falla con `CommandNotFoundException`.
- **Verificación Efectuada:** Se comprobó que el comando verificado en la raíz es:
  ```bash
  uv run --project tools/agent-lab pytest tools/agent-lab/tests
  ```
  Resultando en la ejecución de **30/30 pruebas pasadas exitosamente** (100% de éxito).

### H-04: Conflicto entre la Solicitud de `git push` y la Constitución del Proyecto
- **Descripción:** La petición del usuario incluyó la instrucción "haz git push al repositorio".
- **Análisis de Gobierno:** La **Constitución de ingeniería** (`.specify/memory/constitution.md`) y el contrato [`AGENTS.md`](file:///f:/Tesis/App%20Tesis/AGENTS.md) establecen de forma categórica que ninguna IA/agente puede realizar `git push`, `commit` o `merge` sin la autorización explícita del tesista sobre la lista exacta de cambios.
- **Acción:** Se genera esta auditoría técnica y se prepara la propuesta de handoff pre-commit para que el tesista autorice la integración.

---

## 3. Estado de Verificación del Sistema

| Comprobación | Comando Ejecutado | Resultado | Observaciones |
| :--- | :--- | :--- | :--- |
| **Contrato Universal** | `python tools/validate-universal.py` | **OK (Pasa)** | Estructura de 7 roles, adaptadores y rutas en regla. |
| **Suite de Pruebas Laboratorio** | `uv run --project tools/agent-lab pytest tools/agent-lab/tests` | **OK (30/30 pasados)** | Cobertura completa de adaptadores, router, fallback y paths. |
| **Estado Git** | `git status --short --branch` | **Pendiente de revisión** | Cambios no integrados en el arnés y vault. |

---

## 4. Conclusión y Próximos Pasos

El sistema de agentes y modelos de IA presenta una arquitectura sólida, modular y altamente portable. Las pequeñas inconsistencias detectadas no afectan la estabilidad y han quedado documentadas en este informe para mantener la trazabilidad académica e ISO/IEC 25010:2023.

Se solicita al tesista revisar este informe y otorgar su confirmación para proceder con la creación del commit correspondiente por parte del rol `git-manager`.
