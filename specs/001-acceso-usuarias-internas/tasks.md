---
title: "Tareas: Acceso de usuarias internas"
type: task-list
status: planned
spec: "[[spec]]"
plan: "[[plan]]"
approved: 2026-08-24
approved_by: Tesista
---

# Tareas: Acceso de usuarias internas

## Convención

Formato: `[ID] [P?] [HU] [writer] acción con ruta exacta → verificación`.

- `[P]` solo si no comparte archivos, migraciones, settings ni estado con otra tarea.
- Cada archivo tiene un único escritor.
- Las pruebas no son opcionales para comportamiento funcional.
- Una tarea no puede marcarse `completed` sin resultado de verificación.
- Escritores disponibles: `agente-raiz` (integra y escribe; conserva la propiedad de los
  archivos), `implementer` (código), `reviewer` (revisión, no edita), `coordinator`
  (trazabilidad y dashboard).
- Los agentes `ux` y `architect` son `read-only`: entregan propuestas y el `agente-raiz`
  escribe los artefactos de diseño.

## Fase 1 — Diseño del sistema (Fase II del anteproyecto; sin Django todavía)

### 1.1 Hoja de estilos HTML estática

- [ ] T001 [agente-raiz] Preparar la hoja de estilos estática en `design/style-guide/` con
      `style.css` y carpeta `components/`, consumible en navegador sin Django;
      basada en los tokens provisionales de `docs/ui/SISTEMA-DISENO.md` (marcados como
      propuesta, no identidad aprobada) → la página abre en navegador y lista todos los
      elementos.
- [ ] T002 [P] [agente-raiz] Documentar tokens en `design/style-guide/tokens.html`: paleta
      provisional, tipografía de pila del sistema, espaciado, radios y estados de color con
      contraste AA verificado → tabla de contraste con resultados WCAG AA.
- [ ] T003 [P] [agente-raiz] Crear componentes Bootstrap en `design/style-guide/components/`:
      botones (primario, secundario, enlace, destructivo con focus/disabled/loading), campos,
      tarjetas, badges con texto+icono, tabla responsiva, estado vacío, resumen de errores,
      toast y confirmación → cada componente visible y navegable por teclado.
- [ ] T004 [agente-raiz] Crear la vista de componentes (`design/style-guide/index.html`)
      que enlaza tokens y componentes con ejemplos de uso → revisión a 360 px, zoom 200 % y
      teclado.
- [ ] T005 [ux] [agente-raiz] Revisar la hoja de estilos con criterios UX (móvil primero,
      contraste AA, 44 × 44 px, errores recuperables, una acción principal por pantalla) y
      devolver ajustes → hallazgos registrados y corregidos por el agente raíz.
- [ ] T006 [ux] [agente-raiz] Proponer wireframes textuales de los recorridos de SPEC-001
      (acceso, cambio obligatorio, dashboard, salida) usando los componentes de la hoja de
      estilos → wireframes validados contra los estados del plan (plan.md:163-184).
- [ ] T007 [coordinator] Registrar la validación de la hoja de estilos con el tesista y
      solicitar aprobación antes de usarla en plantillas → checkpoint en
      `docs/bitacora/checkpoints/`.

### 1.2 Modelo relacional completo

- [ ] T008 [architect] [agente-raiz] Elaborar el mapa conceptual inicial del dominio en
      `docs/architecture/MODELO-RELACIONAL.md` a partir de CAT-REQ-001 y las decisiones
      D-001 a D-012: módulos `accounts`, `planning`, `attendance`, `traceability`, `reports` y
      `public_site`; las entidades futuras quedan marcadas como `proposed` y no bloquean S1.
      No se inventan reglas no confirmadas y cada entidad enlaza su requisito fuente.
- [ ] T009 [architect] [agente-raiz] Definir en
      `docs/architecture/DICCIONARIO-DATOS.md` el diccionario aprobado para `accounts` y un
      inventario conceptual, no normativo, de los módulos futuros: campos, tipos, unidades,
      redondeo, restricciones, índices y relaciones solo cuando exista fuente confirmada.
- [ ] T010 [architect] [agente-raiz] Verificar coherencia del modelo de `accounts` con
      SPEC-001 y `data-model.md` (`accounts.User`, sesiones, restricción canónica) → sin
      contradicciones entre el detalle aprobado de acceso y la propuesta conceptual futura.
- [ ] T011 [coordinator] Registrar la validación del modelo de `accounts` con el tesista →
      checkpoint en `docs/bitacora/checkpoints/`; el mapa de módulos futuros queda
      `proposed` hasta contar con sus especificaciones y validación humana.

## Fase 2 — Preparación de la porción vertical (solo después de la Fase 1 aprobada)

- [ ] T012 [agente-raiz] Confirmar spec `confirmed`, plan `approved` y entregables de diseño
      aprobados; IDs `RF-ACC-001` y RNF aplicables → enlaces válidos en `spec.md` y `plan.md`.
      Confirmar además que la implementación de S1 se limita a `accounts` y acceso; no se
      crean apps ni reglas operativas de sprints futuros.
- [ ] T013 [P] [implementer] Inicializar proyecto Django en la raíz: `pyproject.toml`,
      `uv.lock`, `manage.py`, `config/__init__.py`, `config/urls.py`, `config/asgi.py`,
      `config/wsgi.py`, `apps/__init__.py`, `.env.example` y el esqueleto de CI en
      `.github/workflows/ci.yml` → `uv run python manage.py check` pasa sin aplicación de
      negocio y el workflow queda preparado para instalar el proyecto raíz.
- [ ] T014 [implementer] Crear settings por entorno en `config/settings/base.py`,
      `development.py`, `test.py`, `production.py` e `__init__.py` con carga `python-dotenv`
      y secretos fuera de Git → `uv run python manage.py check --settings=config.settings.development`.
- [ ] T015 [implementer] Verificar PostgreSQL local (servicio, cliente, conexión y base de
      pruebas) y Bootstrap local en `static/vendor/bootstrap/` con su `LICENSE` →
      `psql`/`pg_isready` o rutas documentadas disponibles, conexión reproducible y hoja de
      estilos servida desde `static/vendor/`.

## Fase 3 — Datos y reglas mínimas (bloqueante para HU-01/02/03)

- [ ] T016 [implementer] Crear la app `accounts` en `apps/accounts/__init__.py`, `apps.py`,
      `admin.py` (sin exponer datos en Admin) y `decorators.py` → `makemigrations` no muestra
      errores.
- [ ] T017 [implementer] Definir `accounts.User(AbstractUser)` con
      `must_change_password=True`, nombres ASCII controlados (letras, números, punto, guion y
      guion bajo) y `normalize_username` en `apps/accounts/models.py` → pruebas unitarias en
      `apps/accounts/tests/test_models.py`.
- [ ] T018 [implementer] Configurar `AUTH_USER_MODEL = "accounts.User"` en
      `config/settings/base.py` y la restricción funcional PostgreSQL
      `accounts_user_username_canon_uniq` sobre `Lower(Trim("username"))` → migración
      `apps/accounts/migrations/0001_initial.py`.
- [ ] T019 [implementer] Revisar `0001_initial.py`, aplicar migraciones en PostgreSQL vacía y
      verificar unicidad canónica → `makemigrations --check --dry-run` limpio y prueba en
      `test_models.py`.
- [ ] T020 [implementer] Implementar comando `create_initial_account` en
      `apps/accounts/management/commands/create_initial_account.py` con bloqueo asesor
      transaccional, segunda comprobación `User.objects.exists()`, validadores de contraseña,
      entrada oculta y rechazo si existe otra cuenta → pruebas en
      `apps/accounts/tests/test_management_command.py`.

## Fase 4 — HU-01 (P1): Iniciar y cerrar sesión interna (CA-01, CA-05, CA-09)

- [ ] T021 [implementer] Crear formulario de acceso en `apps/accounts/forms.py` que conserve
      el username normalizado tras error y no repueble la contraseña → validación de entradas.
- [ ] T022 [implementer] Implementar vistas `login`, `dashboard` y `logout` en
      `apps/accounts/views.py` y sus rutas en `apps/accounts/urls.py` y `config/urls.py`
      (`/acceso/`, `/inicio/`, `/salir/`) → pruebas de integración en
      `apps/accounts/tests/test_authentication.py`.
- [ ] T023 [implementer] Crear plantillas `templates/base.html` (basada en la hoja de
      estilos aprobada), `templates/components/messages.html` y
      `apps/accounts/templates/accounts/dashboard.html` con bienvenida y solo “Cambiar
      contraseña” y “Cerrar sesión” → CA-09 en `test_authentication.py`.
- [ ] T024 [implementer] Configurar logout solo por `POST` con CSRF y vencimiento deslizante
      de sesión (1 800 s, guardado por solicitud autenticada) en `config/settings/base.py` →
      `GET /salir/` devuelve `405` y pruebas en `test_authentication.py` y `test_sessions.py`.

## Fase 5 — HU-02 (P1): Proteger el acceso privado (CA-02, CA-03, CA-04)

- [ ] T025 [implementer] Implementar guarda reutilizable para credencial temporal y proteger
      cada vista privada en `apps/accounts/decorators.py` y `views.py` → CA-08 parcial y
      acceso directo redirigido al cambio en `apps/accounts/tests/test_security.py`.
- [ ] T026 [implementer] Asegurar mensaje único equivalente para usuario inexistente, clave
      incorrecta y cuenta inactiva en el formulario de acceso → CA-02 y CA-03 en
      `test_authentication.py`.
- [ ] T027 [implementer] Redirigir acceso anónimo a cada URL privada con `next` seguro y sin
      contenido privado → CA-04 en `test_security.py`.
- [ ] T028 [implementer] Agregar cabeceras de no-caché en respuestas privadas y de
      autenticación; `never_cache` → prueba de ausencia de contenido privado al retroceder en
      `test_security.py`.

## Fase 6 — HU-03 (P2): Cambiar la contraseña propia (CA-06, CA-07, CA-08, CA-10)

- [ ] T029 [implementer] Implementar formulario de cambio (old_password, new_password1,
      new_password2) en `apps/accounts/forms.py` → validación y errores por campo.
- [ ] T030 [implementer] Implementar vista `password_change` con `select_for_update()` antes de
      validar, rotación de sesión ganadora e invalidación de las demás en
      `apps/accounts/views.py` y ruta `/mi-cuenta/cambiar-contrasena/` → CA-06, CA-07 y
      concurrencia en `apps/accounts/tests/test_password_change.py`.
- [ ] T031 [implementer] Desactivar `must_change_password` en el cambio válido y redirigir al
      dashboard con confirmación → CA-08 en `test_password_change.py` y `test_security.py`.
- [ ] T032 [implementer] Crear plantillas `login.html` y `password_change_form.html` en
      `apps/accounts/templates/accounts/` usando los componentes de la hoja de estilos
      (control mostrar/ocultar, resumen accesible y foco) → RNF-UX-001/002/003 en recorrido
      manual.

## Fase 7 — Revisión del incremento y cierre

- [ ] T033 [reviewer] Revisar criterios CA-01 a CA-11, RNF aplicables, SC-001 a SC-005,
      matriz de autorización (positivos y negativos), integridad y diff → hallazgos registrados
      sin editar.
- [ ] T034 [implementer] Resolver hallazgos aceptados → pruebas pasan.
- [ ] T035 [coordinator] Ejecutar el protocolo manual de accesibilidad, comprensión y
      conectividad limitada; actualizar `docs/traceability/MATRIZ-TRAZABILIDAD.md` y crear
      evidencia `docs/evidence/S1/RF-ACC-001/verification.md`, `security.md` y
      `ux-validation.md` → enlaces comprobados, sin datos personales ni credenciales.
- [ ] T036 [coordinator] Actualizar `docs/00-inicio/00-dashboard.md`, crear checkpoint y
      preparar solicitud de aprobación → sin commit/push automático.

## Dependencias

```text
T001 → T002/T003 → T004 → T005 → T006 → T007
T001 → T008 → T009 → T010 → T011
T007/T011 → T012 → T013 → T014 → T015
T015 → T016 → T017 → T018 → T019 → T020
T020 → T021 → T022 → T023 → T024
T021 → T025 → T026 → T027 → T028
T022 → T029 → T030 → T031 → T032
T024/T028/T031 → T033 → T034 → T035 → T036
```

`[P]` (no comparten archivos ni estado):
- T002 y T003: subentregables independientes de la misma hoja de estilos, cada uno con
  archivos propios; T004 depende de ambos y es el único escritor de `index.html`.
- T013: inicialización de Django no comparte archivos con las tareas de diseño.

## Verificación final

- [ ] Hoja de estilos aprobada y usada en todas las plantillas de la porción.
- [ ] Modelo relacional validado y coherente con `data-model.md` de SPEC-001.
- [ ] Todos los RF/CA de la porción están enlazados a pruebas (CA-ACC-001-01 a CA-11).
- [ ] Permisos positivos y negativos pasan (RNF-SEC-001).
- [ ] `uv run python manage.py check` pasa.
- [ ] `uv run python manage.py check --deploy --settings=config.settings.production` sin
      advertencias sin resolver.
- [ ] `uv run python manage.py makemigrations --check --dry-run` no detecta cambios.
- [ ] `uv run python manage.py test` pasa (incluida concurrencia y canonicidad en PostgreSQL).
- [ ] Interfaz revisada en móvil 360 px, zoom 200 %, teclado y contraste AA.
- [ ] SC-002 y RNF-CON-001 tienen protocolo, resultado agregado y evidencia en el vault.
- [ ] CI instala el proyecto raíz y ejecuta sus comprobaciones con PostgreSQL.
- [ ] `git diff --check` y diff completo revisados.
- [ ] Evidencia, matriz y documentación actualizadas.
- [ ] No hay credenciales, datos personales ni cambios fuera de alcance.
