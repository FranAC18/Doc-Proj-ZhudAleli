---
title: Plan de implementación desde cero
type: roadmap
status: proposed
date: 2026-07-21
tags:
  - proyecto/tesis
  - tipo/plan
---

# Plan de implementación desde cero

Este plan conserva los cinco sprints de desarrollo del anteproyecto. La preparación técnica
es una etapa previa, no un sexto sprint académico.

## Etapa 0 — Preparación y control del proyecto

**Resultado**: repositorio reproducible, memoria Obsidian única, reglas de agentes, CI básico
y decisiones de alcance visibles.

- Integrar esta base en una rama `chore/portable-harness`.
- Abrir la raíz como vault y validar enlaces.
- Aprobar o corregir Constitución y ADR-0002.
- Ejecutar smoke tests con el motor principal. El motor alternativo queda como comparación
  opcional si existe acceso sin costo adicional.
- Resolver dónde se guardará el PDF aprobado fuera del repositorio público.
- Cerrar Sprint 0 solo con la evidencia definida en su documento.

**Puerta**: el agente lee el contexto correctamente; no hay secretos; Git y Obsidian están
operativos; el tesista aprueba el flujo.

## Fase I — Levantamiento de requisitos

**Resultado**: Product Backlog validado y requisitos trazables.

1. Preparar guion de entrevista y ficha de observación a partir de D-001 a D-010.
2. Observar recorridos actuales de planificación, asistencia, acopio, secado, lotes,
   inventario y reportes.
3. Identificar actores, datos mínimos, excepciones, correcciones y responsables.
4. Redactar propuestas con fuente y fecha; separar hechos de hipótesis.
5. Validar con la organización usando lenguaje y ejemplos comprensibles.
6. Convertir cada capacidad aprobada en spec con RF/RNF y criterios Given/When/Then.
7. Priorizar backlog respetando el orden de sprints aprobado.

**Puerta**: no quedan decisiones de alcance críticas ocultas; cada requisito tiene actor,
fuente, criterios y estado.

## Fase II — Diseño del sistema

**Resultado**: arquitectura, datos y sistema visual listos para implementación incremental.

- Confirmar el monolito modular y elaborar diagramas de contexto, módulos y despliegue.
- Crear modelo conceptual y relacional, diccionario de datos y reglas de integridad.
- Definir RBAC real y matriz rol × permiso × operación.
- Diseñar recorridos móviles y prototipos de baja/alta fidelidad.
- Validar sistema visual Bootstrap con usuarias antes de multiplicar pantallas.
- Definir estrategia de pruebas y medición de adecuación funcional ISO/IEC 25010:2023.
- Registrar decisiones relevantes en ADR.

**Puerta**: arquitectura y datos cubren requisitos; prototipo y permisos están validados; los
riesgos tienen mitigación.

## Base técnica de Django

Se crea justo antes del Sprint 1, en la misma rama de preparación técnica aprobada:

- Python 3.12, Django 5.2 LTS y PostgreSQL.
- `config/`, settings por entorno y `.env.example` sin secretos.
- apps vacías únicamente cuando tienen responsabilidad definida.
- usuario personalizado, layout Bootstrap, navegación y componentes base.
- Ruff, pruebas Django/pytest, cobertura orientativa y CI.
- migraciones, datos de demostración anónimos y guía de instalación.
- health check y manejo de errores básico.

No se crean modelos de negocio especulativos para “adelantar trabajo”.

## Sprint 1 — Administración y acceso

**Incremento funcional**: usuarias autenticadas acceden solo a las operaciones de su rol;
visitantes ven contenido público aprobado.

- Usuario, membresía y estados de acceso.
- Login, logout, cambio y recuperación de contraseña únicamente según la spec aprobada.
- Grupos/permisos según matriz validada.
- Gestión mínima de usuarias por la directiva autorizada.
- Shell público mínimo y navegación diferenciada; la gestión y publicación final pertenecen
  al Sprint 5.
- Pruebas positivas/negativas, sesión, CSRF y accesibilidad del flujo.

**Demo**: cada perfil completa su recorrido y recibe denegación correcta en operaciones no
autorizadas.

## Sprint 2 — Planificación de actividades

**Incremento funcional**: la directiva programa jornadas/actividades y asigna responsables;
las socias consultan lo que les corresponde.

- Actividad, fecha, responsable, estado y observaciones validadas.
- Listado y calendario simple si aporta valor en dispositivos reales.
- Cambios de estado con reglas explícitas.
- Notificaciones solo si el canal, consentimiento y conectividad están confirmados.
- Pruebas de solapamientos, fechas límite, permisos y estados vacíos.

## Sprint 3 — Asistencia y participación

**Incremento funcional**: se registra asistencia de forma completa y corregible bajo reglas
aprobadas.

- Entrada, salida, actividad y participación.
- Prevención de duplicados e inconsistencias temporales.
- Corrección autorizada con motivo e historial cuando se confirme.
- Historial individual y resumen por periodo.
- Pruebas de duplicados, ausencias, correcciones y permisos.

## Sprint 4 — Trazabilidad productiva

**Incremento funcional**: una materia prima puede seguirse desde el acopio hasta el lote y
movimiento de inventario con los datos confirmados.

- Recepción/acopio y origen.
- Proceso de secado y variables validadas.
- Transformación, lote, merma y producto resultante.
- Movimientos de inventario y conciliación.
- Transacciones, unidades, redondeo y prohibición de saldos inválidos.
- Pruebas de trazabilidad completa, correcciones, concurrencia e integridad.

Ventas y cuentas por cobrar forman parte del alcance confirmado por D-002 y D-010; sus
recorridos, permisos y datos se concretarán en las especificaciones aprobadas.

## Sprint 5 — Reportes y gestión de información

**Incremento funcional**: la directiva consulta y exporta los reportes priorizados con
fórmula, periodo y fuente entendibles.

- Filtros y resúmenes de asistencia, producción e inventario confirmados.
- Totales derivados de datos operativos, sin duplicación silenciosa.
- Exportación únicamente en formatos necesarios.
- Página pública final con el contenido y los publicadores que se aprueben al resolver P-12.
- Pruebas de fórmulas, permisos, periodos, zonas horarias y conjuntos vacíos.

## Fase IV — Evaluación

- Construir matriz de adecuación funcional: completitud, corrección y pertinencia.
- Enlazar requisito → caso de prueba → resultado → evidencia.
- Ejecutar pruebas del sistema en ambiente controlado.
- Realizar validación con usuarias mediante tareas representativas.
- Registrar método, muestra, instrumento, resultados y limitaciones.
- Corregir defectos o documentar limitaciones sin alterar resultados retrospectivamente.

## Fase V — Documentación y entrega

- Manual técnico reproducible.
- Manual de usuaria con recorridos y lenguaje validado.
- Diccionario de datos y diagramas finales.
- Historial de decisiones y sprints como insumo para capítulos.
- Anexos con instrumentos y evidencia anonimizada.
- Revisión de coherencia entre anteproyecto, sistema y tesis final.
- Respaldo, despliegue, transferencia y plan de mantenimiento.

## Regla de avance

Al final de cada etapa se realiza una revisión humana. No se adelanta el siguiente módulo
solo porque un agente pueda generar código rápidamente. Si una dependencia de campo bloquea
la implementación, se trabaja en pruebas, diseño o infraestructura ya aprobada y se registra
el bloqueo.
