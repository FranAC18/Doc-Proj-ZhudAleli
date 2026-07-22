---
title: Flujo de versionamiento con GitHub
type: guide
status: completed
tags:
  - proyecto/tesis
  - tipo/guia
  - herramienta/git
---

# Flujo de versionamiento con GitHub

## Ramas

```text
main                         rama estable
docs/sprint-0-preparacion    documentación inicial
feat/s1-acceso               funcionalidad del Sprint 1
feat/s2-planificacion        funcionalidad del Sprint 2
feat/s3-asistencia           funcionalidad del Sprint 3
feat/s4-trazabilidad         funcionalidad del Sprint 4
feat/s5-reportes             funcionalidad del Sprint 5
```

Para un proyecto individual no necesitamos una rama `develop` al inicio. `main` y ramas
pequeñas por tarea son suficientes y reducen complejidad.

## Flujo de una tarea

1. Confirmar el sprint y la tarea.
2. Crear una rama.
3. Implementar un cambio pequeño.
4. Ejecutar pruebas.
5. Revisar el diff.
6. Crear un checkpoint en Obsidian.
7. Mostrar el diff y proponer el mensaje de commit.
8. Crear el commit únicamente con solicitud explícita del tesista.
9. Revisar o fusionar hacia `main` únicamente con confirmación.
10. Hacer `push` únicamente con confirmación.

## Commits

Usar mensajes concretos:

```text
docs: define contexto del proyecto
chore: initialize django project
feat(access): add role permissions
test(attendance): prevent duplicate records
fix(inventory): preserve stock movement history
```

## Autoría de commits

La identidad del commit será la del tesista. GitHub muestra coautores únicamente cuando el
mensaje incluye un trailer explícito como:

```text
Co-authored-by: Nombre Apellido <correo@ejemplo.com>
```

El agente no debe añadir ese trailer por defecto. La colaboración de la IA se documentará
en la bitácora de Obsidian cuando sea relevante.

Configura Git con un nombre y un correo asociados a tu cuenta de GitHub:

```powershell
git config --global user.name "Tu Nombre"
git config --global user.email "tu-correo@ejemplo.com"
git config --global --list
```

## Regla para el agente

El agente puede consultar Git, trabajar en una rama/worktree autorizado y revisar
diferencias. Debe detenerse antes de `commit`, `push`, `merge`, `rebase`, eliminar ramas o
reescribir historia, salvo que el tesista solicite explícitamente la acción concreta.

## Repositorio remoto existente

```powershell
git status
git branch --show-current
git remote -v
```

No ejecutes `git init` ni vuelvas a agregar `origin` dentro de un clon existente. El remoto
esperado es `https://github.com/FranAC18/ZhudAleli.git`; confirma antes de modificarlo.
