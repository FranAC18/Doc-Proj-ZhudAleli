---
title: Contrato HTTP de SPEC-001
type: interface-contract
status: approved
date: 2026-07-25
spec: "[[../spec]]"
plan: "[[../plan]]"
tags:
  - proyecto/tesis
  - tipo/contrato
  - sprint/s1
  - modulo/acceso
---

# Contrato HTTP de SPEC-001

## Alcance

Contrato de páginas HTML renderizadas por Django. No existe API JSON ni contrato OpenAPI en
esta porción. Las rutas son nombres funcionales propuestos y se vuelven normativos al aprobar
el plan, decisión registrada el 2026-08-24.

## Rutas

| Nombre Django | Método y ruta | Precondición | Resultado principal |
|---|---|---|---|
| `accounts:login` | `GET /acceso/` | anónima | `200`, formulario |
| `accounts:login` | `POST /acceso/` | token CSRF | válido normal: `302 /inicio/`; válido temporal: `302` a cambio; inválido: `200` |
| `accounts:dashboard` | `GET /inicio/` | sesión normal | `200`, dashboard privado |
| `accounts:password_change` | `GET /mi-cuenta/cambiar-contrasena/` | sesión autenticada | `200`, formulario de cambio |
| `accounts:password_change` | `POST /mi-cuenta/cambiar-contrasena/` | sesión y CSRF | válido: `302 /inicio/` con confirmación; inválido: `200` sin cambios |
| `accounts:logout` | `POST /salir/` | CSRF | sesión eliminada y `302 /acceso/` |
| `accounts:logout` | `GET /salir/` | cualquiera | `405 Method Not Allowed` |

## Guardas y redirecciones

| Estado del solicitante | `/acceso/` | `/inicio/` | cambio de contraseña | `/salir/` por `POST` |
|---|---|---|---|---|
| Anónima | formulario | redirección al acceso con `next` seguro | redirección al acceso | respuesta sin contenido privado |
| Sesión normal | redirección al dashboard | permitido | permitido | cerrar |
| Sesión con cambio obligatorio | redirección al cambio | redirección al cambio | cambio permitido | cerrar |
| Sesión vencida | formulario con aviso general | redirección al acceso | redirección al acceso | respuesta sin contenido privado |

`next` solo se utiliza cuando Django valida que el destino es seguro para el host permitido.
Una redirección nunca incluye credenciales ni estados internos.

## Formularios

### Acceso

| Campo | Tipo | Regla visible |
|---|---|---|
| `username` | texto | etiqueta “Nombre de usuario”; conserva el valor normalizado tras error |
| `password` | contraseña | etiqueta “Contraseña”; nunca se repuebla tras error |

Los fallos devuelven la página de acceso y no crean sesión. Un identificador inexistente o
asociado a una cuenta inactiva presenta «Usuario incorrecto» junto al campo de usuario; una
clave errónea de una cuenta activa presenta «Contraseña incorrecta» junto al campo de
contraseña. El tesista acepta que esta distinción permite inferir la existencia de una cuenta
activa. Al tercer fallo del mismo identificador canónico dentro de tres minutos, el acceso para
ese identificador se bloquea durante tres minutos y se muestra un aviso breve con el tiempo
restante. El bloqueo no desactiva la cuenta.

### Cambio de contraseña

| Campo | Tipo | Regla visible |
|---|---|---|
| `old_password` | contraseña | contraseña actual obligatoria |
| `new_password1` | contraseña | aplica validadores configurados de Django |
| `new_password2` | contraseña | debe coincidir con la nueva |

Un error mantiene el hash y la bandera anterior y limpia los tres campos secretos. Un éxito
actualiza el hash, desactiva la bandera temporal, conserva la sesión actual y muestra
confirmación en el dashboard.

## Seguridad de respuesta

- Todo formulario `POST` incluye token CSRF y el middleware correspondiente.
- Las páginas de acceso, cambio y dashboard incluyen cabeceras para impedir
  almacenamiento de contenido sensible en caché.
- La cookie de sesión es `HttpOnly`, `SameSite=Lax` y `Secure` en producción.
- No se incluyen hashes, sesiones, tokens ni detalles técnicos en mensajes de error,
  parámetros de URL o logs de aplicación. La única señal permitida sobre la existencia
  de una cuenta activa es la distinción de mensajes aprobada en CA-ACC-001-02/03.
- Las plantillas escapan texto por defecto y no usan HTML confiable derivado de entradas.

## Comportamiento con conectividad interrumpida

Si un `POST` no recibe respuesta, la interfaz no afirma que el acceso o el cambio se completó.
La usuaria puede reintentar:

- el acceso se revalida y no crea privilegios adicionales;
- el cambio se revalida contra la contraseña actual;
- la salida puede repetirse sin reactivar una sesión.

No se agrega almacenamiento sin conexión de credenciales ni lógica de autenticación en el
navegador.
