---
fecha: 2026-10-30
fase: post_commit
tarea: documentación del ER y compatibilidad con las tablas Django existentes
estado: registrado-postcommit
repositorio: ZhudAleli
rama: docs/requisitos-y-organizacion-del-vault
commit: a35363d
push: realizado
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

El commit `a35363d` se creó y publicó en `origin/docs/requisitos-y-organizacion-del-vault`; `git ls-remote` confirmó ese mismo hash en la rama. Incluyó la base consolidada v2.1, el ER integral v2.1, la nota de reutilización de tablas, el control 5.11, la introspección PostgreSQL y el checkpoint pre_commit. `git diff --cached --check` no reportó errores; no se ejecutaron pruebas de producto ni se modificó la app. La publicación al repositorio del docente sigue pendiente.
