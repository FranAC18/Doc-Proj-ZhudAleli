# ADR-0001: Base documental y técnica del proyecto

## Estado

Aceptada como plantilla inicial; validar con la directora y la organización.

## Decisión

La aplicación se desarrollará con Django, PostgreSQL y Bootstrap 5, usando una estructura
documental versionada para requisitos, decisiones y evaluación.

El agente de desarrollo utilizará `AGENTS.md` como guía del repositorio y los archivos de
`agents/tesis/` como contexto específico del dominio.

## Motivo

Separar reglas permanentes, conocimiento del proyecto, memoria dinámica y código permite
revisar cambios, migrar de modelo y detectar supuestos no confirmados.

## Consecuencias

- Las decisiones importantes quedan auditables.
- El contexto puede actualizarse sin modificar el arnés.
- Los requisitos deben validarse antes de convertirse en código.
- El agente no sustituye entrevistas, revisión académica ni pruebas del sistema.
