# Plantillas adaptadas a la tesis

Spec Kit resuelve primero este directorio y después sus plantillas administradas. Estos
overrides añaden fuente, validación humana, permisos, UX, evidencia y trazabilidad académica
sin modificar los archivos que una actualización de Spec Kit puede reemplazar.

Verifica la resolución con:

```bash
specify preset resolve spec-template
specify preset resolve plan-template
specify preset resolve tasks-template
```

Al actualizar Spec Kit, compara los cambios de las plantillas base con estos overrides y
ejecuta el smoke test antes de aceptar la versión.
