# Plantillas adaptadas a la tesis

Spec Kit resuelve primero este directorio y después sus plantillas administradas. Estos
overrides añaden fuente, validación humana, permisos, UX, evidencia y trazabilidad académica
como principal adaptación local. Las bases administradas pueden ser reemplazadas al actualizar
Spec Kit; sus guardas locales deben revisarse en esa actualización.

Sincronización 2026-10-20: constitución 1.0.0 y ADR-0007 establecen que el tesista puede cerrar
un periodo con un registro breve y pendientes explícitos, sin aprobación adicional. ADR-0006
conserva las fronteras, capas proporcionales, compatibilidad y entregas incrementales. Las bases
mantienen ejemplos genéricos con guardas locales. Al actualizar Spec Kit, verificar estas guardas
además de los overrides; nunca trasladar ejemplos `src/`
o `backend/frontend` a la raíz Django definida en ADR-0003.

Verifica la resolución con:

```bash
specify preset resolve spec-template
specify preset resolve plan-template
specify preset resolve tasks-template
```

Al actualizar Spec Kit, compara los cambios de las plantillas base con estos overrides y
ejecuta el smoke test antes de aceptar la versión.
