---
version: "5.11"
fecha: 2026-10-30
autor: Codex por solicitud del tesista
estado: preparado-para-revision
publicacion: pendiente
commit: pending
---

# Control de cambios 5.11

Se añade la [nota sobre reutilización de las tablas de login de Django](../arquitectura/uso_tablas_django_login_en_diseno_v1.0_2026-10-30.md). Confirma que las 13 tablas actuales ya aparecen en el ER integral v2.1 y precisa cuáles conserva el sistema de autenticación, cuáles siguen siendo infraestructura técnica de Django y cuáles se reutilizan como identidad/contacto. Se mantiene la separación entre permisos Django y cargos organizacionales.

La nota también deja visible la brecha entre `accounts_authchallenge.user_id` y `contact_id`: las dos FK existen, pero la base no fuerza que el canal pertenezca a la misma cuenta. No se encontraron filas de desafío en la base de desarrollo consultada. No se modificaron código, modelos ni migraciones; la validación organizacional y la publicación académica siguen pendientes.

La [base consolidada v2.1](../arquitectura/diseno_base_datos_v2.1_2026-10-30.md) y el [ER integral v2.1](../arquitectura/modelo_er_integral_v2.1_2026-10-30.md) se incluyen como referencias de esta edición.
