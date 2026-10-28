# Zhud Alelí

Repositorio general de requisitos, diseño, sprints, agentes y documentación académica
para la aplicación web de tesis del Comité de Mujeres Indígenas “Tránsito Amaguaña” de
Zhud y su unidad productiva Zhud Alelí. El código de producto vive en el repositorio
privado [App-zhudaleli](https://github.com/FranAC18/App-zhudaleli).

El objetivo de este repositorio es guiar la construcción de la aplicación sin duplicar su
código. Los requisitos, planes, tareas, decisiones y evidencias viven en archivos
versionados aquí; el código, migraciones y pruebas de producto viven en la app. Codex,
Codex CLI, Kimi Code o GLM son motores intercambiables que
trabajan sobre esos mismos contratos. Codex, Antigravity con Gemini y OpenCode/OpenChamber
pueden alternarse mediante el contrato universal de orquestadores, sin convertir la sesión
privada de una herramienta en fuente de verdad.

## Estado actual

- Etapa: continuidad de requisitos y diseño tras el cierre administrativo parcial de S1.
- Sprint 0: cerrado con evidencia y commit inicial.
- Aplicación Django: todavía no creada.
- Flujo portable: skills de Spec Kit 0.13.2 en `.agents/skills/`, descubiertas por Codex y
  Kimi Code sin mantener dos copias.
- Contexto del anteproyecto: resumido en `agents/tesis/PROJECT_CONTEXT.md`.
- Decisiones D-001 a D-010: revisadas funcionalmente; los recorridos se validan en Fase I.
- Requisitos: CAT-REQ-001 v1.1 es la línea base aprobada, con 60 requisitos `confirmed`,
  2 `proposed` y 12 `superseded`, en `docs/requirements/CAT-REQ-001.md`.
- Arnés Python anterior: conservado únicamente como laboratorio en `tools/agent-lab/`.

Toda la documentación visible en Obsidian permanece dentro de la raíz del repositorio. Las
notas de trabajo se guardan en `docs/bitacora/`, las especificaciones en `specs/` y el
contexto estable en `agents/tesis/`; el laboratorio y la configuración de agentes no son
fuentes documentales del proyecto.

La carpeta `documentacion/` reúne ediciones académicas finales. Permanece ignorada
por defecto; cada archivo revisado puede incorporarse explícitamente a este
repositorio, con control de versión y cambios, sin arrastrar borradores.
`analisis/` conserva borradores y análisis internos; `_archivo/` registra material
sustituido sin borrarlo. Solo el contenido revisado de `documentacion/` se prepara para el
repositorio documental del docente. Cada `commit` y publicación requieren la solicitud o
confirmación expresa del tesista, respectivamente.

Para desarrollar se necesita un requisito y sprint vigentes con alcance verificable. Si
existen spec, plan y tareas aprobados, se respetan; su ausencia no exige crear esos
documentos antes de programar. Una decisión material de comportamiento sí debe estar
resuelta antes de implementarse. La revisión y las pruebas proporcionales siguen siendo
necesarias para declarar terminada una funcionalidad.

## Dos repositorios

| Repositorio | Contenido | Exclusiones |
|---|---|---|
| `ZhudAleli` (este vault) | Constitución, `specs/`, requisitos, sprints, matriz, agentes, skills, proceso y `documentacion/` revisada | `/app/`, código Django, migraciones y pruebas de producto |
| [App-zhudaleli](https://github.com/FranAC18/App-zhudaleli) | Código Django, migraciones, pruebas, plantillas, estáticos fuente, dependencias, configuración de ejecución/CI, `.gitignore` y README técnico | Agentes, specs, requisitos y documentación de proceso |

Consulta [la guía de repositorios y pre-push](docs/git/REPOSITORIOS-Y-PRE-PUSH.md) antes
de preparar un commit o migrar historial. El checkout local `app/` está ignorado aquí.

## Arquitectura de trabajo

```text
anteproyecto + entrevistas
           ↓
requisito validado + sprint de ejecución
           ↓
spec / plan / tareas, si existen o el riesgo los justifica
           ↓
código + migraciones en App-zhudaleli
           ↓
pruebas + revisión + trazabilidad en ZhudAleli
```

La fuente común es Git. Obsidian abre la raíz como vault y muestra los mismos Markdown que
usan los agentes. Las conversaciones de una IA no son fuente de verdad del proyecto.

Documentos principales:

- `ONBOARDING-IA.md`: guía de contexto rápido para iniciar sesión con cualquier IA.
- `AGENTS.md`: contrato común para cualquier agente.
- `.specify/memory/constitution.md`: principios y puertas de calidad.
- `docs/architecture/ARQUITECTURA-OBJETIVO.md`: arquitectura de la aplicación.
- `docs/architecture/PORTABILIDAD-IA.md`: cómo cambiar de motor o modelo.
- `docs/architecture/CONTRATO-UNIVERSAL-ORQUESTADORES.md`: reglas comunes para cambiar de host
  sin perder contexto.
- `docs/architecture/RUTAS-MODELOS-IA.md`: rutas recomendadas por rol y proveedor.
- `docs/bitacora/ESTADO-ACTIVO.md`: estado que debe leer el siguiente host.
- `agents/tesis/roles/`: contratos canónicos de requirements, architect, ux, implementer,
  reviewer, documenter y git-manager.
- `docs/architecture/PLAN-DESDE-CERO.md`: plan completo de construcción.
- `docs/traceability/MATRIZ-TRAZABILIDAD.md`: vínculo entre tesis, requisitos y evidencia.
- `docs/ui/SISTEMA-DISENO.md`: reglas para una interfaz bonita, clara y accesible.

## Motores soportados

| Uso | Motor recomendado | Qué conserva al cambiar |
|---|---|---|
| Desarrollo principal | Codex app o Codex CLI | `AGENTS.md`, specs, tareas, pruebas y documentación |
| Alternativa con Kimi | Kimi Code CLI con Kimi K3 | Los mismos artefactos y skills de Spec Kit |
| Alternativa con GLM | Kimi Code CLI con una versión elegida explícitamente | Los mismos artefactos; cambia solo la configuración local |

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
./scripts/agent.sh antigravity
./scripts/agent.sh openchamber
```

En PowerShell:

```powershell
.\scripts\agent.ps1 codex
.\scripts\agent.ps1 kimi
.\scripts\agent.ps1 antigravity
.\scripts\agent.ps1 openchamber
```

Antes de cambiar de herramienta, ejecuta `status`, registra el handoff de la tarea y abre el
siguiente host desde esta misma raíz. Si PowerShell bloquea scripts no firmados, usa una
ejecución temporal sin cambiar la política global:

```powershell
powershell.exe -NoProfile -ExecutionPolicy Bypass -File .\scripts\agent.ps1 status
```

Para usar opcionalmente un modelo GLM sin guardar la clave en archivos:

```bash
export ZAI_API_KEY="tu-clave-local"
export GLM_MODEL="modelo-disponible"
./scripts/agent.sh glm
```

```powershell
$env:ZAI_API_KEY = "tu-clave-local"
$env:GLM_MODEL = "modelo-disponible"
.\scripts\agent.ps1 glm
```

Los scripts solo validan la raíz y seleccionan el motor. No hacen `commit`, `push`, `merge` ni
modifican la historia de Git.

## Flujo de una funcionalidad

Con Codex, las skills se invocan como `$speckit-*`; con Kimi Code, como
`/skill:speckit-*`.

1. Identificar el requisito aprobado y el sprint vigente en este repositorio.
2. Resolver decisiones materiales de comportamiento para la porción elegida.
3. Usar spec, plan y tareas aprobados cuando existan. Spec Kit puede producirlos
   para trabajo complejo, pero no son un trámite obligatorio para cada porción.
4. Implementar código, migraciones y pruebas en la raíz Git de `App-zhudaleli`.
5. Revisar el diff y las verificaciones proporcionales antes de declarar terminado
   el trabajo; enlazar el PR/tag real en la matriz de este repositorio.

Las plantillas adaptadas a la tesis están en `.specify/templates/overrides/`. No reemplazan
la validación humana ni convierten propuestas en requisitos aprobados.

## Estructura objetivo de la aplicación

En la raíz Git de `App-zhudaleli`:

```text
config/                 configuración Django
apps/
├── core/               utilidades transversales mínimas
├── accounts/           usuarios, membresías y RBAC
├── planning/           jornadas, actividades y responsables
├── attendance/         asistencia y participación
├── traceability/       producción, inventario, ventas, gastos y cuentas por cobrar
├── reports/            consultas y exportaciones
└── public_site/        contenido público
templates/              layout y componentes Bootstrap
static/                 tokens, estilos e imágenes versionables
tests/                  pruebas de integración y recorridos críticos
```

`specs/`, `docs/`, `documentacion/`, `analisis/` y `_archivo/` pertenecen solo a
este repositorio general.

Se mantiene un monolito modular Django con plantillas del servidor y Bootstrap 5, confirmado
por el tesista el 2026-10-08 en [ADR-0006](docs/decisions/ADR-0006-monolito-modular-y-entrega-incremental.md).
[ADR-0008](docs/decisions/ADR-0008-separacion-repositorios-y-flujo-git.md) sustituye
la ubicación en un único repositorio de ADR-0003 y conserva su estructura Django
interna en la raíz de `App-zhudaleli`.
La [guía de arquitectura](docs/architecture/ARQUITECTURA-OBJETIVO.md) explica capas internas,
propiedad de datos/escrituras, dependencias explícitas y versiones piloto incrementales.
Cada módulo agrupa su responsabilidad; servicios/consultas aparecen cuando hay comportamiento
que los justifica. Se conserva el ORM, las relaciones y transacciones nativas; no se crean
capas/apps vacías. La publicación es conjunta y verifica lo anterior afectado. Versionar
código no sustituye ejecutar la aplicación en un entorno accesible a las socias.
SPA, microservicios o infraestructura adicional requieren necesidad y ADR. Las capacidades
futuras, proveedores y Git/publicación conservan sus propias puertas y autorizaciones.

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
