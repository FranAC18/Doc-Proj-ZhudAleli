---
title: Commit y push del aplicativo: contactos e interfaces
date: 2026-10-28
phase: post_commit
status: published-to-feature-branch
repository: FranAC18/App-zhudaleli
branch: feature/RF-ACC-001-base-proyecto
commit: e3cc0718c7b440472e899e3d9fba220a8ded771f
requirement: RF-ACC-001; RF-ACC-006
sprint: S2
task: SB-S2-02; base de contactos de SPEC-003
---

# Commit y push autorizados por el tesista

Solicitud explícita: «vamos a hacer commit y push al repositorio del aplicativo app».
Se publicó únicamente el código del repositorio de la app, en la rama de trabajo existente.

- Raíz: `F:/Tesis/App Tesis/app`.
- Remoto de push: `https://github.com/FranAC18/App-zhudaleli.git`.
- Commit: [e3cc071](https://github.com/FranAC18/App-zhudaleli/commit/e3cc0718c7b440472e899e3d9fba220a8ded771f).
- Mensaje: `feat(accounts): integrar contactos y mejorar interfaces [RF-ACC-001][RF-ACC-006][SPRINT-2]`.
- Resultado: remoto confirmado mediante `git ls-remote`; checkout limpio y sincronizado.
- PR y tag: no creados. No hay integración en main ni cierre de sprint.

## Alcance y verificaciones

Incluye la base de asociación/verificación de contactos y su migración 0003, interfaces
compartidas, adornos, controles de contraseña, mensajes únicos y notificaciones con salida
por la derecha en escritorio y vertical en móvil. Recursos públicos y PWA v17.

Pasaron 31 pruebas PostgreSQL, Django check, comprobación de migraciones sin diferencias,
Ruff y sintaxis JS. Se usó una base de pruebas aislada en la repetición final.
Se actualizó una prueba que esperaba una revisión antigua del CSS y adornos sustituidos;
el control actual verifica el recurso y la plantilla decorativa vigente. README corregido
para describir posición superior, autocierre y direcciones actuales.

El índice se revisó por rutas exactas, ausencia de archivos de proceso, gitlinks, bases,
secretos conocidos y diferencias posteriores al staging. `git diff --check` correcto.
La revisión inicial y la final del remoto mostraron la rama esperada; push sin force.

Evidencia visual conservada: [[../../evidence/frontend/2026-10-28-notificaciones/direcciones]].
El acceso multicanal completo, la entrega SMTP real, passkeys, WhatsApp y recuperación
siguen pendientes. Publicar este incremento no completa RF/HU/HT ni SB-S2-02.
El repositorio general conserva sus cambios locales; no se hizo commit ni push allí.

## Archivos incluidos (44)

- `README.md`
- `apps/accounts/forms.py`
- `apps/accounts/frontend/accounts/cambio_contrasena/password_change_form.html`
- `apps/accounts/frontend/accounts/contactos/contact_settings.html`
- `apps/accounts/frontend/accounts/contactos/contact_verify.html`
- `apps/accounts/frontend/accounts/contactos/recursos/contactos.css`
- `apps/accounts/frontend/accounts/login/login.html`
- `apps/accounts/frontend/accounts/login/recursos/login.css`
- `apps/accounts/frontend/accounts/login/recursos/password-change.css`
- `apps/accounts/migrations/0003_contactchannel_authchallenge_authattempt.py`
- `apps/accounts/models.py`
- `apps/accounts/services.py`
- `apps/accounts/tests/test_contactos.py`
- `apps/accounts/tests/test_flujo_acceso.py`
- `apps/accounts/tests/test_frontend.py`
- `apps/accounts/urls.py`
- `apps/accounts/views.py`
- `apps/portal/frontend/portal/inicio/dashboard.html`
- `config/settings/base.py`
- `static/compartido/adornos-formulario.css`
- `static/compartido/base.css`
- `static/compartido/form-feedback.js`
- `static/compartido/formularios.css`
- `static/compartido/notificaciones.css`
- `static/compartido/notificaciones.js`
- `static/compartido/password-toggle.js`
- `static/manifest.json`
- `static/pwa/offline.html`
- `static/pwa/service-worker.js`
- `templates/base.html`
- `templates/components/adornos/adorno_password.html`
- `templates/components/adornos/capas_vinotinto.html`
- `templates/components/adornos/formulario.html`
- `templates/components/adornos/onda_horizontal.html`
- `templates/components/adornos/onda_vertical.html`
- `templates/components/formularios/alternar_contrasena.html`
- `templates/components/formularios/error_campo.html`
- `templates/components/formularios/estilos.html`
- `templates/components/formularios/resumen_errores.html`
- `templates/components/messages.html`
- `templates/components/notificaciones/cerrar.html`
- `templates/components/panel.html`
- `templates/public_status.html`
- `tests/test_pwa.py`
