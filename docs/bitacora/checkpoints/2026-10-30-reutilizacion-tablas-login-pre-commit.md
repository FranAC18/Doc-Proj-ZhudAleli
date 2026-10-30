---
fecha: 2026-10-30
fase: pre_commit
tarea: documentación del ER y compatibilidad con las tablas Django existentes
estado: revisado-localmente
commit: pending
publicacion_academica: pendiente
---

# Nota de revisión: reutilización de tablas Django

## Resultado

Se documentó que las 13 tablas actuales de autenticación y Django ya están representadas en el ER integral v2.1. `accounts_user` se reutiliza como identidad de cuenta; `accounts_contactchannel` conserva los canales de contacto; los grupos y permisos de Django permanecen técnicos y separados de los cargos organizacionales. No se propone un segundo sistema de login.

La documentación deja explícita la brecha de integridad en `accounts_authchallenge`: la base no exige que `user_id` sea dueño del `contact_id`. El diseño no se implementó en código ni migraciones.

## Archivos en alcance

- `documentacion/arquitectura/uso_tablas_django_login_en_diseno_v1.0_2026-10-30.md`
- `documentacion/arquitectura/diseno_base_datos_v2.1_2026-10-30.md`
- `documentacion/arquitectura/modelo_er_integral_v2.1_2026-10-30.md`
- `documentacion/control_de_cambios/registro_v5.11_2026-10-30.md`
- `docs/evidence/architecture/2026-10-30-er-integral/postgres-introspeccion.json`

## Verificaciones

- La introspección guardada describe 13 tablas y no leyó filas personales de negocio.
- La verificación anterior registró 18 migraciones aplicadas y `makemigrations --check --dry-run`: `No changes detected`.
- Se revisaron los enlaces locales de los documentos que se incluyen.
- Se ejecutó `git diff --check`; no se detectaron errores de whitespace. Git reportó avisos de normalización de fin de línea en archivos preexistentes ajenos al alcance.
- No se ejecutaron pruebas de producto ni se modificó el repositorio de la aplicación.

## Próximo paso

Crear el commit documental en `docs/requisitos-y-organizacion-del-vault` y hacer push a su upstream `origin`. Registrar el hash y resultado reales en la fase `post_commit`. No publicar al repositorio del docente.
