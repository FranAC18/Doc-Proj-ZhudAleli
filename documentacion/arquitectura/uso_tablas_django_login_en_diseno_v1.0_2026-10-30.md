---
titulo: Reutilización de tablas de login de Django en el diseño de Zhud Alelí
version: "1.0"
fecha: 2026-10-30
autor: Codex por solicitud del tesista
estado: preparado-para-revision
validacion_organizacional: pendiente
implementacion: sin-cambios-de-codigo-ni-migraciones
publicacion: pendiente
commit: a35363d
---

# Reutilización de las tablas de login de Django

## Respuesta

Sí. Las 13 tablas que aparecen en la captura del administrador de base de datos están contempladas en el [modelo ER integral v2.1](modelo_er_integral_v2.1_2026-10-30.md) como el esquema físico que ya existe. El diseño las reutiliza cuando corresponde y no propone crear un segundo sistema de usuarios, login o permisos. Las tablas de negocio que aún faltan se añadirán mediante modelos y migraciones propias.

El [diseño consolidado v2.1](diseno_base_datos_v2.1_2026-10-30.md) separa la cuenta técnica de la persona organizacional. Según la información del tesista, las seis socias tienen cuenta y la Superadministradora tiene una cuenta externa al padrón. Las cuentas usan el mismo `accounts_user`; cada socia se vinculará a una entidad de persona organizacional propuesta, y la Superadministradora externa no tendrá membresía. Los roles de negocio no se deducen de las tablas de grupos de Django.

## Correspondencia de las tablas actuales

| Tabla física existente | Tratamiento en el diseño |
|---|---|
| `accounts_user` | Se conserva como identidad de autenticación (`AUTH_USER_MODEL`). Las nuevas entidades organizacionales referencian esta cuenta; no se crea otra tabla de usuarios. |
| `accounts_contactchannel` | Se reutiliza para los canales de contacto de la cuenta, su verificación, consentimiento y avisos. No se duplica correo o teléfono en la entidad organizacional. |
| `accounts_authchallenge` | Sigue siendo parte de autenticación. Sus desafíos no se convierten en entidades de negocio. |
| `accounts_authattempt` y `accounts_loginthrottle` | Se conservan para sus límites de intentos de autenticación, con alcances distintos ya definidos por la aplicación. No sustituyen auditoría ni controles de negocio. |
| `accounts_user_groups`, `accounts_user_user_permissions`, `auth_group`, `auth_group_permissions`, `auth_permission` | Se conservan para los permisos técnicos de Django. No representan membresía, Presidencia, Tesorería, Secretaría ni Superadministración organizacional. |
| `django_content_type` | Metadato interno que permite asociar permisos con modelos Django. No es catálogo de negocio. |
| `django_session` | Estado técnico de sesión. No se usa como historial de acceso, auditoría ni registro organizacional. |
| `django_migrations` | Historial técnico de migraciones aplicadas. No representa datos de negocio. |

El nombre físico de la tabla de permisos directos del usuario es `accounts_user_user_permissions`; la captura puede mostrarlo truncado visualmente.

## Brecha detectada y estado del entorno

`accounts_authchallenge` contiene por separado una FK hacia la cuenta y otra hacia el canal de contacto. La base valida que ambos registros existan, pero no garantiza por sí sola que el canal pertenezca a la misma cuenta del desafío. El servicio revisado asigna la cuenta propietaria del canal, aunque una inserción por otra ruta podría crear el cruce. En el entorno de desarrollo consultado no había desafíos; el diseño ER registra esta brecha y recomienda evaluar una restricción de integridad antes de reforzarla con una migración.

La introspección de PostgreSQL encontró las 13 tablas mostradas en el ER y las migraciones visibles aplicadas. Solo había una cuenta de usuario en esa base de desarrollo; por tanto, no contiene todavía las seis cuentas de socias ni la cuenta externa comunicadas por el tesista. Tampoco contiene las tablas de dominio propuestas. Este conteo no limita el diseño ni acredita el padrón de producción.

## Resultado para el diseño

- Reutilizar `accounts_user` como la FK de identidad técnica de cada cuenta.
- Mantener grupos y permisos Django separados de los cargos y roles de negocio.
- Añadir las entidades de persona, membresía y designación organizacional según el diseño por módulos, sin duplicar el login.
- Revisar la integridad de `accounts_authchallenge` antes de implementar su futura restricción; no se encontró una colisión de nombres con las tablas de negocio propuestas.

Esta nota aclara el alcance de las tablas de login; no modifica modelos, migraciones, datos ni permisos de la aplicación. La revisión organizacional y la publicación académica de esta edición siguen pendientes.

## Fuentes

- [Modelo ER integral v2.1](modelo_er_integral_v2.1_2026-10-30.md).
- [Base consolidada para el diseño de datos v2.1](diseno_base_datos_v2.1_2026-10-30.md).
