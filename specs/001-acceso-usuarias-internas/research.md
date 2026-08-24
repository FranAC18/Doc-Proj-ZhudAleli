---
title: Investigación técnica de SPEC-001
type: research
status: approved
date: 2026-07-25
spec: "[[spec]]"
plan: "[[plan]]"
write_owner: agente-raiz
tags:
  - proyecto/tesis
  - tipo/investigacion
  - sprint/s1
  - modulo/acceso
---

# Investigación técnica de SPEC-001

## Objetivo

Resolver las decisiones que afectan estructura, datos, sesiones, seguridad, pruebas y
experiencia antes de dividir SPEC-001 en tareas. Las decisiones de este documento forman
parte del [[plan|plan aprobado]]; no son implementación.

## Decisiones

### DTR-001 — Dependencias reproducibles con `uv`

- **Decisión propuesta**: usar `uv`, un `pyproject.toml` en la raíz y `uv.lock` versionado.
  Las herramientas de desarrollo vivirán en el grupo `dev`.
- **Motivo**: ofrece un único flujo reproducible en Windows, Linux y CI; el repositorio ya
  usa `uv` de forma aislada en el laboratorio de agentes.
- **Alternativas consideradas**: `venv` + `pip` + archivo de requisitos requiere sincronizar
  más de una representación; Poetry agrega otro modelo de proyecto sin una necesidad
  demostrada.
- **Fuente**: [proyectos y sincronización de uv](https://docs.astral.sh/uv/concepts/projects/sync/).

### DTR-002 — Django 5.2 LTS, PostgreSQL y Psycopg 3

- **Decisión propuesta**: Python 3.12, la última corrección disponible de Django 5.2 LTS,
  PostgreSQL 14 o posterior y Psycopg 3.
- **Motivo**: coincide con la constitución, evita diseñar contra una base distinta y permite
  probar la restricción canónica del nombre de usuario.
- **Alternativas consideradas**: SQLite no se usará en CI ni en pruebas que puedan ocultar
  diferencias de restricciones; otra rama de Django requeriría cambiar la constitución.
- **Fuentes**:
  [bases de datos compatibles con Django 5.2](https://docs.djangoproject.com/en/5.2/ref/databases/)
  y [notas de Django 5.2](https://docs.djangoproject.com/en/5.2/releases/5.2/).

### DTR-003 — Usuario personalizado mínimo desde la primera migración

- **Decisión propuesta**: `accounts.User(AbstractUser)` con
  `must_change_password=True` como único campo nuevo. Se declarará `AUTH_USER_MODEL` antes
  de migrar y el modelo vivirá en `accounts/0001_initial.py`.
- **Motivo**: conserva formularios y mecanismos probados de Django, habilita la credencial
  temporal y evita el cambio costoso de usuario después de crear tablas.
- **Alternativas consideradas**: un perfil separado no gobierna la autenticación; un usuario
  desde `AbstractBaseUser` exige reimplementar campos y formularios sin beneficio para esta
  spec; el usuario predeterminado impediría cumplir la restricción arquitectónica.
- **Fuente**:
  [personalización del usuario en Django](https://docs.djangoproject.com/en/5.2/topics/auth/customizing/).

### DTR-004 — Nombre de usuario canónico

- **Decisión propuesta**: aplicar NFKC, quitar espacios externos y usar `casefold()` mediante
  `User.normalize_username()` en la creación controlada y el acceso. Añadir
  `UniqueConstraint(Lower(Trim("username")))` para impedir colisiones aunque una escritura
  futura omita la normalización.
- **Motivo**: cumple el borde aprobado para mayúsculas y espacios y deja la integridad en la
  base de datos, no solo en la interfaz.
- **Alternativas consideradas**: un backend de autenticación propio aumenta superficie de
  seguridad; `CIText` o una colación especial agregan requisitos de PostgreSQL; confiar
  únicamente en formularios permite duplicados por escrituras directas.
- **Riesgo residual**: `casefold()` de Python y `lower()` de PostgreSQL no son idénticos para
  todo Unicode. Se almacena siempre la forma Python y se prueban NFKC, `ñ` y acentos.

### DTR-005 — Sesiones nativas con vencimiento deslizante

- **Decisión propuesta**: backend de sesiones en base de datos,
  `SESSION_COOKIE_AGE=1800`, `SESSION_SAVE_EVERY_REQUEST=True` y
  `SESSION_EXPIRE_AT_BROWSER_CLOSE=False`.
- **Definición verificable de actividad**: una solicitud autenticada que llega a Django y
  termina sin error 500 renueva la vigencia. Cargar archivos estáticos o mantener la pantalla
  abierta sin solicitar al servidor no cuenta como actividad. No se agregan pulsos en
  segundo plano.
- **Operación**: programar `clearsessions` en el entorno desplegado para eliminar registros
  vencidos.
- **Cierre del navegador**: no se interpreta como cierre de sesión porque no forma parte del
  requisito y los navegadores pueden restaurar sesiones. La interfaz recuerda usar “Cerrar
  sesión” en equipos compartidos.
- **Alternativas consideradas**: una sesión o reloj propios duplicarían comportamiento
  nativo; un vencimiento absoluto no satisface “sin actividad”; el almacenamiento solo en
  cookie dificulta la invalidación operativa.
- **Fuente**:
  [sesiones de Django](https://docs.djangoproject.com/en/5.2/topics/http/sessions/).

### DTR-006 — Cambio obligatorio mediante una guarda reutilizable

- **Decisión propuesta**: un decorador o mixin pequeño de `accounts`, aplicado junto con la
  exigencia de autenticación a cada vista privada de esta porción, redirige al cambio cuando
  `must_change_password=True`.
- **Motivo**: existe una sola vista privada —el dashboard— y la guarda explícita es suficiente
  y fácil de probar sin mantener exclusiones globales para acceso, salida o futuro sitio
  público.
- **Alternativas consideradas**: ocultar enlaces no es autorización; un middleware global y
  un sistema genérico de políticas son prematuros. Cualquier nueva vista privada futura debe
  declarar y probar la guarda antes de integrarse.

### DTR-007 — Vistas y formularios nativos de autenticación

- **Decisión propuesta**: especializar `LoginView`, `AuthenticationForm`,
  `PasswordChangeView` y `PasswordChangeForm` solo donde la experiencia o la normalización lo
  requieren. El cambio correcto redirige al dashboard con confirmación persistente;
  `LogoutView` acepta únicamente `POST` protegido por CSRF.
- **Concurrencia**: la vista abre `transaction.atomic()`, vuelve a cargar la usuaria con
  `select_for_update()` y construye el formulario sobre esa instancia antes de validar la
  contraseña actual. Una segunda solicitud espera; al continuar ve el hash nuevo y su
  contraseña anterior ya no valida. El guardado de hash y bandera ocurre una sola vez.
- **Efecto del cambio**: Django mantiene la sesión actual mediante
  `update_session_auth_hash`; las otras sesiones quedan invalidadas al cambiar el hash de
  autenticación.
- **Alternativas consideradas**: vistas completamente propias replicarían validaciones
  sensibles; salida por `GET` permite acciones involuntarias o inducidas.
- **Fuente**:
  [vistas y formularios de autenticación de Django](https://docs.djangoproject.com/en/5.2/topics/auth/default/).

### DTR-008 — Primera cuenta mediante comando interactivo

- **Decisión propuesta**: `create_initial_account` se niega si ya existe cualquier cuenta,
  solicita usuario y contraseña de forma interactiva, valida la contraseña, crea una cuenta
  activa no administrativa y activa `must_change_password`. La contraseña no se acepta en
  argumentos, variables ni archivos y la salida no imprime el usuario.
- **Exclusión mutua**: dentro de `transaction.atomic()`, el comando ejecuta
  `pg_advisory_xact_lock()` con una constante documentada exclusiva de esta operación,
  vuelve a consultar si existe una cuenta y solo entonces crea. PostgreSQL libera el bloqueo
  al confirmar o revertir; una segunda ejecución espera y después se rechaza.
- **Motivo**: permite la entrega presencial aprobada sin crear un formulario público ni
  registrar el secreto en historial, fixtures o documentación; el bloqueo asesor funciona
  incluso cuando la tabla está vacía y no añade una entidad artificial.
- **Alternativas consideradas**: `createsuperuser` concede privilegios innecesarios; una
  migración de datos no puede guardar un secreto seguro; una interfaz de alta pertenece a
  `RF-ACC-002`; `select_for_update()` sobre una consulta vacía no bloquearía otra creación y
  una tabla singleton solo para el arranque sería complejidad permanente.

### DTR-009 — Seguridad por defecto y riesgo residual explícito

- **Decisión propuesta**: CSRF en todo `POST`, cookies `HttpOnly` y `SameSite=Lax`, cookie
  segura y HTTPS en producción, redirecciones validadas por Django, mensajes equivalentes y
  `never_cache`/no almacenamiento en respuestas privadas.
- **Prueba especial**: el cliente con `enforce_csrf_checks=True` cubre acceso, cambio y salida.
- **Riesgo residual**: SPEC-001 no define bloqueo, tasa, duración ni recuperación ante
  intentos automatizados. No se inventará un bloqueo de cuentas. Antes de exposición pública
  se debe levantar y aprobar esa política si el análisis de despliegue la requiere.
- **Fuente**:
  [protección CSRF de Django](https://docs.djangoproject.com/en/5.2/howto/csrf/).

### DTR-010 — Configuración por entorno

- **Decisión propuesta**: `config/settings/base.py`, `development.py`, `test.py` y
  `production.py`; `python-dotenv` carga `.env` solo como conveniencia local. Producción y CI
  reciben variables del entorno. `.env.example` contiene nombres y valores no secretos.
- **Variables mínimas previstas**: `DJANGO_SETTINGS_MODULE`, `DJANGO_SECRET_KEY`,
  `DJANGO_DEBUG`, `DJANGO_ALLOWED_HOSTS`, `POSTGRES_DB`, `POSTGRES_USER`,
  `POSTGRES_PASSWORD`, `POSTGRES_HOST`, `POSTGRES_PORT` y parámetros seguros de proxy/HTTPS
  cuando el despliegue los defina.
- **Alternativas consideradas**: un único archivo mezcla valores inseguros; guardar `.env`
  en Git vulnera la constitución; una plataforma de secretos específica todavía no está
  seleccionada.

### DTR-011 — Pruebas nativas y PostgreSQL en CI

- **Decisión propuesta**: pruebas de Django con su runner nativo y PostgreSQL tanto en CI
  como en los casos de integridad; Ruff para revisión estática. `pytest` sigue limitado al
  laboratorio existente.
- **Motivo**: reduce dependencias en la primera porción y cubre el comportamiento real de la
  base aprobada.
- **Alternativas consideradas**: `pytest-django` es viable, pero no aporta una necesidad
  demostrada ahora; SQLite ocultaría la restricción funcional y diferencias de migración.
- **Fuente**:
  [visión general de pruebas en Django](https://docs.djangoproject.com/en/5.2/topics/testing/overview/).

### DTR-012 — Interfaz servida localmente

- **Decisión propuesta**: HTML renderizado por Django, Bootstrap 5.3 minificado y su licencia
  dentro de `static/vendor/`, CSS propio pequeño y JavaScript progresivo para
  mostrar/ocultar contraseña, evitar doble activación visual y explicar un resultado no
  confirmado cuando se corta la conexión. El servidor sigue siendo la autoridad y los
  formularios funcionan sin JavaScript.
- **Motivo**: cumple conectividad limitada y evita depender de una CDN o de Node para esta
  porción.
- **Alternativas consideradas**: CDN contradice RNF-CON-001; SPA, Service Worker y toolchain
  de frontend añaden complejidad o riesgo de caché privada; Django Admin no es la interfaz
  aprobada.
- **Fuente**:
  [distribución compilada de Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/download/).

### Revisiones especializadas incorporadas

- **Arquitectura y seguridad**: usuario mínimo, sesiones, CSRF, caché, primera cuenta y
  riesgos de fuerza bruta.
- **Datos y migraciones**: orden de arranque, normalización, restricción PostgreSQL,
  herramientas y reversión.
- **Experiencia y pruebas**: recorridos, estados, contrato HTTP, accesibilidad, conexión
  limitada y protocolo para SC-002.

Las revisiones fueron de solo lectura y no sustituyen la aprobación del tesista ni las
pruebas futuras.

## Conclusión de investigación

No quedan aclaraciones técnicas materiales. Las decisiones cubren las preguntas de SPEC-001
sin ampliar su alcance. En el entorno actual Python 3.12.2 y `uv` 0.10.9 están
disponibles; `psql` y `pg_isready` no se detectaron en `PATH`. La única decisión que necesita
confirmación humana antes de volverse normativa es la aprobación integral de [[plan]],
incluida la elección de `uv`; PostgreSQL debe localizarse o instalarse antes de verificar la
aplicación.
