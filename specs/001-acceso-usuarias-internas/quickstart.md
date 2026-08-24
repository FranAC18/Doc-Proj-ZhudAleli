---
title: Guía de verificación prevista para SPEC-001
type: quickstart
status: approved
date: 2026-07-25
spec: "[[spec]]"
plan: "[[plan]]"
tags:
  - proyecto/tesis
  - tipo/verificacion
  - sprint/s1
  - modulo/acceso
---

# Guía de verificación prevista para SPEC-001

## Uso

Esta es la guía que deberá funcionar después de implementar las tareas aprobadas. En el estado
actual no existe `manage.py`, por lo que estos comandos son criterios reproducibles del plan
aprobado, no resultados ya obtenidos.

## Preparación prevista

1. Instalar Python 3.12, `uv` y PostgreSQL 14 o posterior.
2. Confirmar que el servicio PostgreSQL esté activo y que `psql` y `pg_isready` estén
   disponibles o tengan su ruta documentada en el entorno. En el equipo actual PostgreSQL 18
   está instalado y activo, pero sus clientes aún no están directamente en `PATH`.
3. Copiar `.env.example` a `.env` sin versionar el archivo resultante.
4. Crear una base y un usuario PostgreSQL exclusivos para desarrollo, con permiso para crear
   la base temporal de pruebas.
5. Completar en `.env` los valores PostgreSQL y una clave Django solo local.
6. Desde `F:\Tesis\App Tesis`, sincronizar exactamente el bloqueo:

```powershell
uv sync --locked
```

## Comprobaciones previstas

```powershell
uv run ruff check .
uv run python manage.py check
uv run python manage.py check --deploy --settings=config.settings.production
uv run python manage.py makemigrations --check --dry-run
uv run python manage.py migrate
uv run python manage.py test
git diff --check
```

Para `check --deploy`, la configuración local contiene valores ficticios válidos y seguros;
en CI se inyectan como variables del paso. Cada advertencia se resuelve o justifica antes de
desplegar, y HSTS se activa solo al confirmar HTTPS y el proxy reales. La evidencia debe
registrar versión, comando, resultado y fecha, pero no valores de `.env`, cookies, tokens,
hashes ni contraseñas.

## Creación controlada de la primera cuenta

Solo cuando el recorrido y las pruebas estén funcionales:

```powershell
uv run python manage.py create_initial_account
```

El comando solicita la contraseña de forma oculta y repetida, no la acepta como argumento y
no la imprime. La cuenta se entrega presencialmente a la representante designada por la
Directiva y debe cambiar su contraseña antes de ver el dashboard.

## Recorrido manual previsto

Iniciar el entorno local:

```powershell
uv run python manage.py runserver
```

Verificar los siguientes escenarios con datos ficticios:

1. Cuenta activa normal → acceso → bienvenida → salida → URL privada exige autenticación.
2. Usuario inexistente, contraseña incorrecta y cuenta inactiva → mismo mensaje general,
   sin sesión y sin diferencia visible.
3. Cuenta temporal → cualquier URL privada redirige al cambio; tras cambiar, abre dashboard.
4. Cambio inválido → explica el error, no altera la contraseña ni la bandera.
5. Cambio válido → la contraseña anterior ya no inicia sesión.
6. Dos navegadores autenticados → el cambio conserva el actual e invalida el otro.
7. Sesión sin actividad → válida a los 29:59 y vencida a los 30:00; una solicitud
   autenticada intermedia renueva el plazo.
8. Salida por `POST` funciona; `GET /salir/` se rechaza; solicitudes sin CSRF se rechazan.
9. Volver atrás después de salir no muestra el contenido privado almacenado.
10. `Usuaria`, ` usuaria ` y `USUARIA` resuelven al mismo identificador canónico; no se
    pueden crear duplicados equivalentes.
11. Interrumpir la conexión durante acceso, cambio y salida no muestra un éxito inventado y
    permite reintentar de forma segura.
12. Lanzar dos cambios de contraseña simultáneos con conexiones separadas produce un solo
    éxito, un rechazo y un único hash final; la sesión ganadora permanece válida.
13. Lanzar dos comandos de primera cuenta simultáneos sobre una base vacía produce exactamente
    una cuenta regular; la segunda ejecución no altera ni revela la existente.

## Revisión de interfaz prevista

En cada pantalla y estado:

- ancho de 360 px sin desplazamiento horizontal accidental;
- zoom del navegador al 200 % sin pérdida de contenido o acciones;
- recorrido completo solo con teclado, foco siempre visible y orden lógico;
- contraste AA y mensajes que no dependan solo del color;
- controles principales de al menos 44 × 44 px;
- etiquetas visibles y errores asociados a los campos;
- recursos críticos disponibles con la red desactivada después de cargar el servidor local;
- texto comprensible para una usuaria no técnica.

## Validación de SC-002

Preparar un protocolo con cinco usuarias representativas —propuesta: dos integrantes de la
Directiva y tres socias operarias— y cuatro tareas: iniciar sesión, reconocer el dashboard,
cambiar la contraseña y cerrar sesión. Confirmar la composición al convocar. Registrar solo
resultados agregados, tiempo, ayuda requerida y hallazgos, sin nombres ni credenciales. El
criterio se cumple si al menos cuatro de cinco completan el recorrido sin ayuda en un máximo
de tres minutos.
