---
title: "Wireframes textuales: Acceso de usuarias internas"
type: design
status: proposed
date: 2026-08-24
spec: "[[../../../specs/001-acceso-usuarias-internas/spec]]"
plan: "[[../../../specs/001-acceso-usuarias-internas/plan]]"
source_flows: plan.md:163-184
styleguide: "[[index]]"
tags:
  - proyecto/tesis
  - tipo/diseno
  - sprint/s1
  - modulo/acceso
---

# Wireframes textuales — SPEC-001 (acceso)

Wireframes en texto basados en los componentes de la hoja de estilos (`design/style-guide/`).
Estructura de una pantalla: `ZONA SUPERIOR` (título, contexto y una acción principal),
`CONTENIDO` (ancho legible) y, en escritorio, `BARRA LATERAL`; en móvil, `NAVEGACIÓN INFERIOR`.
Componentes usados: `btn`, `field`, `card`, `badge`, `error-summary`, `alert`, `dialog`, `empty-state`.

La identidad visual es provisional; no se usan colores, logotipo ni símbolos culturales hasta su validación.

## Convención

```text
[componente]
  texto o control
--> siguiente recorrido
```

- `[ZONA SUPERIOR]` encabezado con nombre del sistema, perfil y salida.
- `[BARRA LATERAL]` solo escritorio; `[NAV INFERIOR]` solo móvil.
- Orden de foco = orden visual. Control principal ≥ 44 × 44 px.

---

## 1. Acceso (`/acceso/`)

```text
[ZONA SUPERIOR]
  Zhud Alelí — Ingreso interno

[CONTENIDO]
  h1 "Inicia sesión"
  p  "Ingresa para ver la organización y el avance de tu trabajo."

  [error-summary] (solo si hay error)
      ! "No pudimos iniciar la sesión"
        - "El usuario o la contraseña son incorrectos." (mensaje genérico)

  [field]Nombre de usuaria
      [input text]  (valor conservado tras error)
  [field]Contraseña
      [input password]  (siempre vacía tras error)
      [control] mostrar / ocultar

  [btn--primary] "Ingresar"

  p (solo si sesión vencida, sin detalles internos)
    "Por seguridad, tu sesión venció. Ingresa de nuevo."

[NAV INFERIOR]  -- no aplica en pantalla pública

--> credenciales válidas (cuenta normal) → Dashboard
--> credencial temporal → Cambio obligatorio
--> error → permanece en Acceso (datos no secretos conservados)
```

## 2. Cambio obligatorio (`/mi-cuenta/cambiar-contrasena/`, credencial temporal)

```text
[ZONA SUPERIOR]
  Zhud Alelí — Cambio de contraseña
  [btn--link] "Cerrar sesión"

[CONTENIDO]
  h1 "Crea tu nueva contraseña"
  p  "Debes cambiarla antes de continuar. Elige una que solo tú conozcas."

  [error-summary] (si hay error)
      ! "Revisa los datos e inténtalo de nuevo"
        - <enlace a cada campo inválido>

  [field]Contraseña actual    → [input password]
  [field]Nueva contraseña     → [input password]  [control] mostrar/ocultar
  [field]Repite la contraseña → [input password]

  [btn--primary] "Guardar nueva contraseña"

[NAV INFERIOR]  -- sin acceso a otros destinos hasta completar
p  "Si pasas más de 30 minutos sin actividad, deberás iniciar sesión de nuevo."

--> cambio válido + confirmación → Dashboard
--> cerrar sesión → Acceso
--> cualquier otra vista privada → redirigido a este cambio
```

## 3. Dashboard privado (`/inicio/`)

```text
[ZONA SUPERIOR]
  Zhud Alelí
  [badge: cuenta] "Activa"   (texto + icono; nunca color solo)

[NAVEGACIÓN / BARRA LATERAL]
  [btn--link] Cambiar contraseña
  [btn--link] Cerrar sesión

[CONTENIDO]
  h1 "Bienvenida"   ("Bienvenida, María." — dato mínimo, sin datos personales innecesarios)
  p  "Este es tu espacio. Desde aquí puedes cambiar tu contraseña o cerrar la sesión."

  [alert--success] (persistente, solo después de un cambio válido)
      "Cambiaste tu contraseña correctamente."

  [empty-state] (no aplica todavía: el dashboard aún no muestra operaciones)
      "Sin operaciones disponibles"
      p  "En esta primera versión solo puedes cambiar tu contraseña y cerrar sesión."
```

> Nota de alcance: el dashboard muestra únicamente bienvenida y las dos opciones reales
> (CA-ACC-001-09). No existen tarjetas de negocio ni datos de lotes en esta porción.

--> "Cambiar contraseña" → Cambio (opcional, cuenta normal)
--> "Cerrar sesión" (POST) → Acceso
--> anónimo → redirigido a Acceso
--> credencial temporal → redirigido a Cambio obligatorio
```

## 4. Salida (`POST /salir/`)

```text
[ZONA SUPERIOR]  -- transición, sin contenido privado renderizado
[POST con CSRF]  "Cerrar sesión"  (LogoutView; solo POST)

--> sesión invalidada → Acceso
--> GET /salir/ → 405 (no se renderiza contenido privado al retroceder)
```

---

## Recorridos validados contra el plan

| Recorrido | Origen | Estado |
|---|---|---|
| Acceso → dashboard (cuenta normal) | plan.md:157-165 | cubierto |
| Acceso → cambio obligatorio (temporal) | plan.md:160-161 | cubierto |
| Cambio obligatorio → dashboard con confirmación | plan.md:160-162 | cubierto |
| Dashboard → cambio | plan.md:162 | cubierto |
| Dashboard / cambio → cierre (POST) → acceso | plan.md:163-164 | cubierto |
| Privada con temporal → cambio; anónima → acceso | plan.md:167-184 | cubierto |

Componentes reutilizados: `btn`, `field`, `error-summary`, `alert`, `badge`, `empty-state`, control
mostrar/ocultar. El orden de foco sigue el orden visual; el control principal mide ≥ 44 × 44 px; no hay
desplazamiento horizontal desde 360 px ni al 200 % de zoom (RNF-UX-001/002).
