# Zhud Alelí

Base de ingeniería para desarrollar la aplicación web de tesis del Comité de Mujeres
Indígenas “Tránsito Amaguaña” de Zhud y su unidad productiva Zhud Alelí.

El objetivo de este repositorio es construir la aplicación, no construir otro asistente de
programación. Los requisitos, planes, tareas, pruebas, decisiones y evidencias viven en
archivos versionados; Codex, Codex CLI, Kimi Code o GLM son motores intercambiables que
trabajan sobre esos mismos contratos.

## Estado actual

- Etapa: preparación técnica y documental, fuera de los cinco sprints oficiales.
- Aplicación Django: todavía no creada.
- Flujo portable: skills de Spec Kit 0.13.2 en `.agents/skills/`, descubiertas por Codex y
  Kimi Code sin mantener dos copias.
- Contexto del anteproyecto: resumido en `agents/tesis/PROJECT_CONTEXT.md`.
- Decisiones de campo: pendientes en `docs/00-inicio/01-decisiones-pendientes.md`.
- Arnés Python anterior: conservado únicamente como laboratorio en `tools/agent-lab/`.

No se debe ejecutar una implementación completa mientras el requisito y sus criterios de
aceptación sigan sin validar.

## Arquitectura de trabajo

```text
anteproyecto + entrevistas
           ↓
propuestas → especificación aprobada → plan → tareas
                                            ↓
                                   código + migraciones
                                            ↓
                                pruebas + revisión + evidencia
                                            ↓
                                documentación para la tesis
```

La fuente común es Git. Obsidian abre la raíz como vault y muestra los mismos Markdown que
usan los agentes. Las conversaciones de una IA no son fuente de verdad del proyecto.

Documentos principales:

- `AGENTS.md`: contrato común para cualquier agente.
- `.specify/memory/constitution.md`: principios y puertas de calidad.
- `docs/architecture/ARQUITECTURA-OBJETIVO.md`: arquitectura de la aplicación.
- `docs/architecture/PORTABILIDAD-IA.md`: cómo cambiar de motor o modelo.
- `docs/architecture/PLAN-DESDE-CERO.md`: plan completo de construcción.
- `docs/traceability/MATRIZ-TRAZABILIDAD.md`: vínculo entre tesis, requisitos y evidencia.
- `docs/ui/SISTEMA-DISENO.md`: reglas para una interfaz bonita, clara y accesible.

## Motores soportados

| Uso | Motor recomendado | Qué conserva al cambiar |
|---|---|---|
| Desarrollo principal | Codex app o Codex CLI | `AGENTS.md`, specs, tareas, pruebas y documentación |
| Alternativa con Kimi | Kimi Code CLI con Kimi K3 | Los mismos artefactos y skills de Spec Kit |
| Alternativa con GLM | Kimi Code CLI con GLM-5.2 por protocolo OpenAI compatible | Los mismos artefactos; cambia solo la configuración local |

Los modelos no se fijan dentro del repositorio. Las claves y la configuración de proveedor
son locales para evitar credenciales en Git y permitir que cada motor herede el modelo
seleccionado por el usuario.

## Inicio rápido

Si vienes del ZIP v2 o del repositorio actual, sigue primero `MIGRACION-V2-A-V3.md` para
conservar la historia y revisar el cambio en una rama.

1. Trabaja sobre un clon del repositorio y crea una rama específica, por ejemplo
   `chore/portable-harness`.
2. Abre la raíz del repositorio como vault en Obsidian.
3. Instala el motor que usarás y, para mantener o actualizar las plantillas, instala
   `specify-cli==0.13.2`.
4. Inicia el motor desde la raíz:

```bash
./scripts/agent.sh codex
./scripts/agent.sh kimi
```

En PowerShell:

```powershell
.\scripts\agent.ps1 codex
.\scripts\agent.ps1 kimi
```

Para usar GLM-5.2 sin guardar la clave en archivos:

```bash
export ZAI_API_KEY="tu-clave-local"
./scripts/agent.sh glm
```

```powershell
$env:ZAI_API_KEY = "tu-clave-local"
.\scripts\agent.ps1 glm
```

Los scripts solo seleccionan el motor. No hacen `commit`, `push`, `merge` ni modifican la
historia de Git.

## Flujo de una funcionalidad

Con Codex, las skills se invocan como `$speckit-*`; con Kimi Code, como
`/skill:speckit-*`.

1. Crear una especificación: `speckit-specify`.
2. Resolver ambigüedades: `speckit-clarify`.
3. Confirmar el requisito con el tesista y, cuando corresponda, con la organización.
4. Crear el plan técnico: `speckit-plan`.
5. Generar tareas: `speckit-tasks`.
6. Revisar coherencia: `speckit-analyze`.
7. Implementar una porción verificable: `speckit-implement`.
8. Ejecutar pruebas, revisar el diff y guardar evidencia.

Las plantillas adaptadas a la tesis están en `.specify/templates/overrides/`. No reemplazan
la validación humana ni convierten propuestas en requisitos aprobados.

## Estructura objetivo de la aplicación

```text
config/                 configuración Django
apps/
├── core/               utilidades transversales mínimas
├── accounts/           usuarios, membresías y RBAC
├── planning/           jornadas, actividades y responsables
├── attendance/         asistencia y participación
├── traceability/       acopio, secado, lotes, mermas e inventario
├── reports/            consultas y exportaciones
└── public_site/        contenido público
templates/              layout y componentes Bootstrap
static/                 tokens, estilos e imágenes versionables
tests/                  pruebas de integración y recorridos críticos
specs/                  especificaciones, planes y tareas por funcionalidad
docs/                   memoria Obsidian y evidencia académica
```

Se usará un monolito modular Django con plantillas del servidor y Bootstrap 5. Cualquier
propuesta de SPA, microservicios o infraestructura adicional exige un ADR con una necesidad
demostrable.

## Laboratorio heredado

`tools/agent-lab/` conserva el agente Python educativo recibido. Sirve para estudiar
memoria, llamadas a herramientas y proveedores compatibles con Chat Completions, pero no es
el motor de desarrollo ni forma parte de la aplicación web.

Para verificarlo:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e "tools/agent-lab[dev]"
pytest -q tools/agent-lab/tests
```

## Seguridad básica

- Nunca versionar `.env`, claves, bases locales ni datos personales de las socias.
- Los permisos se validan en backend, no solo ocultando botones.
- Ningún agente puede aprobar requisitos, hacer `push` o fusionar ramas por sí solo.
- Cada cambio de datos productivos debe dejar la trazabilidad definida por el requisito.
- Las afirmaciones sobre ARCSA, LOEPS o ISO requieren fuente oficial y validación humana.
