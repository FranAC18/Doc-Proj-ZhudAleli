---
title: Repositorios, validación pre-push y migración
type: git-policy
status: active
date: 2026-10-20
decision: ADR-0008
---

# Repositorios, validación pre-push y migración

## Alcance explícito

| Destino | Se versiona | No se versiona |
|---|---|---|
| `FranAC18/ZhudAleli` (general) | `.specify/`, `specs/`, `docs/`, `documentacion/` revisada, `agents/`, `.agents/`, adaptadores `.codex/agents/` y `.opencode/agents/`, `AGENTS.md`, requisitos, sprints, matriz, plantillas y herramientas de proceso | `/app/`, código Django, migraciones, pruebas de producto, secretos y bases locales |
| `FranAC18/App-zhudaleli` (aplicación) | `manage.py`, `config/`, `apps/`, `templates/`, `static/` fuente, `tests/`, migraciones, dependencias, configuración de ejecución/CI, `.gitignore` y README técnico breve, cuando existan | `agents/`, `.agents/`, `.codex/`, `.opencode/`, `specs/`, `docs/`, `documentacion/`, `analisis/`, bitácoras, matriz, secretos y bases locales |

Las herramientas Python de `tools/agent-lab/`, evaluaciones y scripts documentales que ya
existen en el repositorio general son infraestructura del proceso; no son la aplicación
Django ni se migran al repositorio de la app.

`documentacion/` contiene ediciones con estados distintos y sigue ignorada por defecto.
Solo se incorporan al repo general archivos revisados, por ruta exacta mediante
`git add -f <archivo>` y con su control de cambios. Esta excepción no autoriza usar
`git add .` ni sincronizar automáticamente toda la carpeta al docente.

El checkout `app/` dentro del workspace general queda ignorado con `/app/`. Es una raíz
Git independiente cuando se inicialice o clone; jamás se agrega como submódulo. El
`.gitignore` ayuda a evitar staging accidental, pero no sustituye la revisión del índice.

## Identidad y mensajes

- Repositorio general: remoto esperado `https://github.com/FranAC18/ZhudAleli.git`.
- Aplicación: remoto esperado `https://github.com/FranAC18/App-zhudaleli.git`.
- Código: `tipo(scope): descripción [RF-XXX][SPRINT-N]`, por ejemplo
  `feat(accounts): habilitar acceso [RF-ACC-001][SPRINT-2]` si se ejecuta en S2.
- Se usa el ID completo del catálogo vigente; `RF-XXX` en la regla es una muestra de
  posición, no un ID literal. No se fabrican referencias para cambios sin requisito.
- Rama de trabajo: `feature/RF-XXX-descripcion`. `main` se protege y recibe cambios por
  PR. El bootstrap de un repositorio vacío se registra como excepción inicial verificable.
  Tras ese primer commit se activa en GitHub la protección de `main`: PR requerido y
  force push deshabilitado, antes de integrar trabajo funcional.
- En un cierre con código integrado: tag `sprint-N` sobre el commit integrado de `main`
  y matriz general actualizada con requisito, sprint, URL del PR, tag y hash de la app.
  En un cierre sin código: `sin entrega de código`; no se crea un tag ficticio.

`SPRINT-N` en un commit de código identifica el sprint **en que se ejecuta el trabajo**.
Si un RF pendiente de S1 se implementa después del cierre de S1, se registra como
arrastre y el commit usa el sprint de ejecución acordado; la matriz conserva el S1
planificado y agrega la entrega real. El `S1` histórico de SPEC-001 corresponde
al S2 del calendario actual. No se cambia retrospectivamente el cierre.

## Checklist obligatorio antes de cada push de código

1. Identificar la ruta actual y la raíz real con `Get-Location` y
   `git rev-parse --show-toplevel`. Debe ser el checkout de la aplicación.
2. Ejecutar `git remote -v` y `git remote get-url --push origin`. La URL de push debe
   ser exactamente `https://github.com/FranAC18/App-zhudaleli.git`.
3. Confirmar rama con `git branch --show-current`; trabajo normal en
   `feature/RF-XXX-descripcion`, nunca push directo o forzado a `main`.
4. Revisar `git status --short`, `git diff --cached --name-only` y
   `git diff --cached --check`. No debe aparecer ninguna ruta de agentes, specs,
   proceso, secretos, bases locales ni un gitlink/submódulo.
5. Verificar que el mensaje usa Conventional Commits, el RF real y el sprint vigente
   del repositorio general. Consultarlos allí; no copiarlos a la app.
6. Revisar el diff y las verificaciones proporcionales ejecutadas. Un commit de trabajo
   parcial puede existir, pero no se presenta como funcionalidad terminada.
7. Confirmar la acción Git autorizada por el tesista, el conjunto exacto de archivos y
   la rama de destino. Si el diff cambió desde la autorización, volver a revisar.

Nunca ejecutar `git add .` desde la raíz general ni force push a `main`. Usar staging
explícito por rutas después de revisar el destino. Un `.gitignore` no impide `git add -f`.

## Migración con respaldo e historial

Estado auditado el 2026-10-20: no hay `app/` versionada ni historial local de esa ruta;
la app Django todavía no existe. El repositorio nuevo existe, es privado y figura vacío
en la consulta de GitHub. Por tanto, hoy no hay historial de aplicación que extraer.
La secuencia siguiente se usa solo si una auditoría posterior encuentra código de app
histórico en `app/` u otra ruta concreta:

1. Antes de cualquier reescritura, comprobar `git status --short`, registrar HEAD y
   remotos, y conservar por separado los cambios sin commit. Crear un respaldo completo
   y verificarlo:

   ```powershell
   git bundle create .\_backups\ZhudAleli-pre-split.bundle --all
   git bundle verify .\_backups\ZhudAleli-pre-split.bundle
   ```

   Crear previamente `_backups/`; esa carpeta está ignorada en el repo general.

2. Identificar la ruta histórica exacta con `git log --all -- app/` y el inventario de
   archivos versionados. Si la ruta cambió, documentar los nombres anteriores antes
   de construir el filtro. Si no hay commits de código de app, detener la extracción.
3. Crear un clon desechable desde el repositorio general, fuera de su índice Git. En
   ese clon únicamente, ejecutar `git filter-repo --subdirectory-filter app/` cuando
   `app/` sea la ruta histórica correcta. Para rutas renombradas, definir un filtro
   explícito de rutas y renombres; no asumir que el comando de `app/` cubre todo.
   Ejemplo para una ruta histórica `app/` confirmada:

   ```powershell
   $generalRoot = (git rev-parse --show-toplevel).Trim()
   $extractRoot = Join-Path $generalRoot '_backups\app-extract'
   git clone --no-local $generalRoot $extractRoot
   git -C $extractRoot filter-repo --subdirectory-filter app/
   git -C $extractRoot log --oneline --all
   git -C $extractRoot ls-tree -r --name-only HEAD
   ```

   El ejemplo solo se ejecuta tras confirmar que `app/` tiene commits de producto;
   `git filter-repo` puede retirar el remoto original del clon por seguridad.
4. Comparar commits y archivos extraídos contra la auditoría, revisar secretos y
   confirmar que no quedaron agentes ni documentos de proceso. Conservar el bundle
   y una copia del resultado filtrado antes de configurar el remoto nuevo.
5. Verificar el estado del remoto de app. Solo si está vacío y el resultado fue
   autorizado, preparar la rama inicial y publicar sin force push. Si ya tiene
   commits, diseñar la integración de ambas historias antes de cualquier push.
   En el caso vacío y tras autorización del tesista para el conjunto exacto:

   ```powershell
   git -C $extractRoot remote add app-origin https://github.com/FranAC18/App-zhudaleli.git
   git -C $extractRoot remote -v
   git -C $extractRoot push -u app-origin HEAD:refs/heads/main
   ```

   El push inicial establece `main`; se activa entonces la protección de rama
   antes del primer PR funcional. El bloque no debe ejecutarse cuando la
   extracción esté vacía ni cuando el remoto ya tenga commits.
6. En el repositorio general, añadir `/app/` a `.gitignore`. Ejecutar
   `git rm --cached` sobre archivos de app únicamente si realmente están versionados;
   no reescribir su historia general. Revisar por separado ambos diffs.
7. Clonar o inicializar la aplicación en `app/`, comprobar su raíz Git y remoto,
   aplicar el checklist pre-push y actualizar la matriz con los PR/tags reales.

`git filter-repo` reescribe los identificadores de commit del clon filtrado; el
historial original permanece en el repositorio general y en el respaldo. Nunca se
ejecuta sobre el checkout de trabajo general ni se fuerza `main` para completar la
migración.
