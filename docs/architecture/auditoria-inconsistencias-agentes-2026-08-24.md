---
title: Auditoría experta de agentes, modelos de IA y portabilidad de arnés
type: architecture-audit
status: completed
date: 2026-08-24
author: Consultor Experto en Agentes y Modelos de IA
verified_against_commit: "62dadf5"
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

### H-01: Discrepancia en la Convención de Nombres de Roles (`git-manager` vs `git_manager`) — resuelta
- **Descripción original:** El rol canónico utiliza guion medio (`git-manager`), mientras que la
  clave de rutas usaba guion bajo (`git_manager`).
- **Resolución aplicada:** `tools/agent-routes.toml`, `tools/validate-universal.py` y la prueba
  del contrato usan ahora exclusivamente `git-manager`. No se mantiene un alias alternativo que
  pueda ocultar errores de resolución.
- **Estado:** resuelto el 2026-08-24; pendiente únicamente verificarlo en la sesión real de cada
  host.

### H-02: Identificadores Hipotéticos de Modelos vs Identificadores Comerciales de API
- **Descripción:** En `tools/agent-routes.toml` y `RUTAS-MODELOS-IA.md` se referencian nombres como `gpt-5.6-luna`, `deepseek-v4`, `glm-5.2` y la serie `gemini-3.x-flash/pro`.
- **Impacto:** Aunque estas denominaciones representan la abstracción de rutas del proyecto, al realizar invocaciones HTTP directas contra los endpoints de proveedores oficiales (OpenAI, Google AI Studio, DeepSeek API), la API retornará un error `404 Model Not Found` si no existe un mapa explícito de traducción hacia modelos vigentes (`gemini-2.5-flash`, `gemini-2.5-pro`, `gpt-4o`, `deepseek-chat`).
- **Resolución aplicada:** El laboratorio conserva los IDs declarados sin traducirlos
  silenciosamente. La disponibilidad real del modelo y el acceso por API quedan explícitamente
  como `por verificar`; el `ModelRouter` no convierte un ID de Antigravity, OpenCode Go o Google
  AI Pro en un ID de API diferente. Las capacidades declaradas y verificadas también se separaron
  en los adaptadores.
- **Pendiente:** Ejecutar una prueba controlada por proveedor y registrar el endpoint, modelo,
  credencial usada sin exponerla, respuesta y fecha. Una suscripción de un host no se toma como
  evidencia de acceso al endpoint directo del laboratorio.

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

**Actualización post-commit:** El commit `62dadf58c56a33874d5b6e37949bd0a4b5845977` ya existe
en la rama `codex/001-acceso-usuarias-internas`; esta auditoría no autoriza ningún push nuevo.
El siguiente control pendiente es el smoke test real entre hosts.

---

## 3. Estado de Verificación del Sistema

| Comprobación | Comando Ejecutado | Resultado | Observaciones |
| :--- | :--- | :--- | :--- |
| **Contrato Universal** | `python tools/validate-universal.py` | **OK (Pasa)** | Estructura de 7 roles, adaptadores y rutas en regla. |
| **Suite de Pruebas Laboratorio** | `uv run --project tools/agent-lab pytest tools/agent-lab/tests` | **OK (30/30 pasados)** | Cobertura completa de adaptadores, router, fallback y paths. |
| **Commit del contrato** | `62dadf58c56a33874d5b6e37949bd0a4b5845977` | **Registrado** | El hash real está en el checkpoint `post_commit`; queda un cambio local de vista en `.obsidian/graph.json`. |

---

## 4. Conclusión y Próximos Pasos

El sistema de agentes y modelos de IA presenta una arquitectura sólida, modular y altamente portable. Las pequeñas inconsistencias detectadas no afectan la estabilidad y han quedado documentadas en este informe para mantener la trazabilidad académica e ISO/IEC 25010:2023.

El informe queda actualizado contra `62dadf5`. Se solicita al tesista revisar el smoke test real
de Codex, Antigravity y OpenChamber antes de considerar cerrado el contrato universal.
