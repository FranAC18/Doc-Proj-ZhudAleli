---
title: "Tareas: [FEATURE NAME]"
type: task-list
status: planned
spec: "[link]"
plan: "[link]"
---

# Tareas: [FEATURE NAME]

## Convención

Formato: `[ID] [P?] [HU] [writer] acción con ruta exacta → verificación`.

- `[P]` solo si no comparte archivos, migraciones, settings ni estado con otra tarea.
- Cada archivo tiene un único escritor.
- Las pruebas no son opcionales para comportamiento funcional.
- Una tarea no puede marcarse `completed` sin resultado de verificación.

## Fase 1 — Preparación de la porción vertical

- [ ] T001 [writer] Confirmar spec `confirmed`, IDs y decisiones abiertas → enlaces válidos.
- [ ] T002 [writer] Crear pruebas de aceptación iniciales en `[ruta]` → fallan por el motivo esperado.

## Fase 2 — Datos y reglas mínimas

- [ ] T003 [HU-01] [writer] Implementar entidad/invariante en `[ruta]` → pruebas unitarias.
- [ ] T004 [HU-01] [writer] Crear migración en `[ruta]` → `makemigrations --check --dry-run` limpio.
- [ ] T005 [HU-01] [writer] Implementar operación transaccional en `[ruta]` → prueba de integración.

## Fase 3 — Permisos e interfaz

- [ ] T006 [HU-01] [writer] Aplicar permiso backend en `[ruta]` → caso permitido y denegado.
- [ ] T007 [HU-01] [writer] Crear formulario/vista/URL en `[rutas]` → validación de entradas.
- [ ] T008 [HU-01] [writer] Crear plantilla/componentes en `[rutas]` → móvil, teclado y estados.

## Fase 4 — Revisión del incremento

- [ ] T009 [reviewer] Revisar criterios, autorización, integridad y diff → hallazgos registrados.
- [ ] T010 [writer] Resolver hallazgos aceptados → pruebas pasan.
- [ ] T011 [coordinator] Actualizar matriz y evidencia en `[rutas]` → enlaces comprobados.
- [ ] T012 [coordinator] Preparar checkpoint y solicitud de aprobación → sin commit/push automático.

## Dependencias

```text
T001 → T002 → T003/T004 → T005 → T006/T007 → T008 → T009 → T010 → T011 → T012
```

Reemplaza el ejemplo por dependencias reales. Si dos tareas se marcan `[P]`, explica por qué
no comparten archivos ni una migración ordenada.

## Verificación final

- [ ] Todos los RF/CA de la porción están enlazados a pruebas.
- [ ] Permisos positivos y negativos pasan.
- [ ] `python manage.py check` pasa.
- [ ] `python manage.py makemigrations --check --dry-run` no detecta cambios.
- [ ] Suite relevante pasa.
- [ ] Interfaz revisada en móvil y escritorio.
- [ ] `git diff --check` y diff completo revisados.
- [ ] Evidencia, matriz y documentación actualizadas.
- [ ] No hay credenciales, datos personales ni cambios fuera de alcance.
