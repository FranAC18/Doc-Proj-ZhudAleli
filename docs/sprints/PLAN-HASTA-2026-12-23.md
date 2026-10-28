---
title: Hoja de ruta viva hasta el 23 de diciembre de 2026
type: sprint-roadmap
status: proposed-for-intermediate-dates-and-scope
updated: 2026-10-27
source: decisión del tesista del 2026-10-27; CAT-REQ-001 v1.2; arquitectura objetivo
owner: tesista y Codex
---

# Hoja de ruta viva hasta el 23 de diciembre de 2026

## Ampliación de acceso aceptada — 2026-10-28

El tesista aceptó correo por código, passkeys y WhatsApp configurable para S2, con recuperación y seguridad común. SPEC-003 y RF-ACC-006 a 009 gobiernan este incremento; SB-S2-05 a 09 descomponen las cinco fases. La activación real de WhatsApp depende de proveedor, plantilla, consentimiento, costo y prueba de entrega. El ingreso necesita conexión y el registro WebAuthn se verifica en dispositivos con HTTPS. Las exclusiones históricas de recuperación y los mensajes diferenciados de SB-S2-02 no vetan el alcance nuevo aceptado; la implementación actual se adaptará con regresión.

Se conserva el avance anterior y el cierre propuesto de S2; no se inventan nuevas fechas, estimaciones ni terminaciones. El backlog v1.5 registra las tareas pendientes. Cada cambio relevante sincroniza requisitos, historias, pila, backlog y gestor local.

## Resultado buscado

Priorizar el objetivo específico 2 comunicado por el tesista: módulos de gestión
organizacional, trazabilidad productiva y control de acceso mediante Scrum. El 23 de
diciembre de 2026 es la fecha objetivo. El alcance entregable se selecciona por recorridos
completos y verificados; la ubicación de una historia en la pila no demuestra que quepa
en el plazo ni que esté terminada.

## Decisiones vigentes y fechas de trabajo propuestas

S1 conserva documentación, requisitos, arquitectura, diseño y aspectos técnicos. Su
periodo llegó hasta el 2026-10-27 por decisión del tesista; los entregables incompletos
conservan su estado. S2 comenzó durante S1 según el registro anterior. La nueva decisión
incluye en S2 login, cuentas, superadministración, estructura y permisos para los módulos
previstos. Las funciones de esos módulos se construyen en S3-S5.

| Periodo | Fechas de trabajo propuestas | Resultado principal | Límite de compromiso |
|---|---|---|---|
| S1 | hasta 27 oct | Fuentes, criterios, mapa conceptual del negocio y límites de datos por módulo. | Cierre de periodo no equivale a completar lo pendiente. |
| S2 | en curso; cierre propuesto 8 nov | Acceso probado; cuentas, membresías y autorización base; operaciones y configuración de login de superadministración cuando sus criterios estén validados; mapa de módulos y permisos. | Preparar navegación y contratos, sin apps vacías ni funciones futuras simuladas. |
| S3 | 9–19 nov | Planificación: actividades, asignaciones y encargos en un recorrido usable; administración mediante operaciones del módulo. | Dejar variantes y automatizaciones sin decisión en la pila. |
| S4 | 20–30 nov | Asistencia y participación: registro, prevención de duplicados, corrección e historial; continuidad sin red solo para operaciones y políticas aprobadas. | QR, multas y sincronización se limitan por P-02/P-03/P-13/P-14. |
| S5 | 1–20 dic | Trazabilidad productiva: catálogo, acopio, secado, lotes y movimientos de existencias como primera cadena íntegra; ampliar comercio y rendición por capacidad y reglas aprobadas. | Las 23 historias hoy agrupadas en S5 no quedan comprometidas automáticamente. |
| Integración y entrega | 21–23 dic | Regresión, recorridos entre módulos, evidencia de uso, documentación de entrega y pendientes explícitos. | No declarar completado lo que carezca de prueba o validación. |

El tesista estima una dedicación propia de **16–25 horas por semana** desde el
2026-10-27 hasta la fecha objetivo. Son unas 8,3 semanas, equivalentes a unas
**130–205 horas disponibles** antes de descontar otras obligaciones, validaciones
y contingencias. Las fechas intermedias son una **propuesta de distribución**, no
una aprobación ni una promesa de terminar toda la pila. S2 ya contiene trabajo local
de acceso. Al inicio de cada sprint
se seleccionan pocas historias según disponibilidad real, dependencias y riesgo; cada
semana se contrasta plan con trabajo verificado. Si el plazo no admite una historia,
se reduce el alcance del incremento o se traslada la historia, sin rebajar las pruebas.

| Periodo restante | Horas orientativas del tesista | Complejidad relativa |
|---|---:|---|
| S2, 27 oct–8 nov | 30–46 h | Alta: identidad, autorización y configuración sensible. |
| S3, 9–19 nov | 25–39 h | Media: planificación y asignaciones. |
| S4, 20–30 nov | 25–39 h | Alta: asistencia, correcciones y política offline. |
| S5, 1–20 dic | 46–71 h | Muy alta: datos productivos, lotes y existencias. |
| Integración, 21–23 dic | 7–11 h | Regresión, evidencia y entrega. |

Prorrateo simple de 16–25 h/semana: no son horas comprometidas ni estimaciones de
desarrollo por historia. La capacidad real se comprueba cada semana.

| Bloque de pila | Ubicación de trabajo | Primer recorrido priorizado |
|---|---|---|
| `HU-ACC-001/002/003/004`; `RF-ACC-005` propuesto | S2 | Acceso y administración de identidad con permisos comprobables. |
| `HU-PLA-001` a `HU-PLA-005` | S3 | Programar, asignar y consultar trabajo organizacional. |
| `HU-ASI-001` a `HU-ASI-007`; `HU-PWA-001/002/003` | S4, con continuidad transversal | Registrar y corregir asistencia sin duplicados; habilitar offline solo tras resolver su política. |
| `HU-CAT-001`, `HU-TRA-001` a `HU-TRA-005`, `HU-INV-001` a `HU-INV-004`; comercio relacionado | S5 | Seguir un lote desde materia recibida hasta existencia comprobable; venta y rendición por capacidad validada. |
| Reportes de cada módulo | Dentro del incremento que produce los datos | Mostrar resultados verificables sin esperar un sprint separado. |

La pila completa mantiene sus IDs y prioridades documentadas. Esta tabla cambia el
orden de ejecución propuesto, no aprueba requisitos nuevos ni compromete todas las
historias de cada bloque para diciembre.

## Base de datos sólida y evolutiva

1. **S1, modelo conceptual:** identificar entidades del negocio, significado, dueño de
   escritura, relaciones entre módulos, reglas que no pueden romperse y decisiones de
   campo pendientes. `SB-S1-03` exige este mapa, pero su cobertura sigue por verificar.
2. **S2, base física compartida:** conservar `accounts.User` y sus migraciones existentes;
   diseñar membresía, autoridad y políticas de acceso con criterios validados antes de
   añadir tablas. Separar identidad de cuenta, pertenencia organizacional y permisos.
3. **S3-S5, modelo por recorrido:** antes de cada función se precisan datos, claves,
   restricciones, historia y operación propietaria. Se crea una migración hacia adelante,
   se prueba desde una base PostgreSQL vacía y se verifica el recorrido con datos de
   prueba. Las relaciones entre módulos se añaden cuando el caso de uso las necesita.
4. **Cambios posteriores:** conservar los datos y significados históricos; revisar
   consumidores, compatibilidad, transacciones y regresión del módulo afectado. No se
   congela en S1 un esquema físico de todos los módulos ni se pospone todo el diseño de
   datos hasta S5.

El mapa conceptual y las invariantes se basan en el catálogo vigente y en la
[[../architecture/ARQUITECTURA-OBJETIVO|arquitectura objetivo]]. Fórmulas, unidades,
políticas offline y reglas económicas abiertas se deciden antes de sus cálculos y
movimientos, no por conveniencia del modelo.

## Flujo de una idea a un incremento

1. Ubicar la idea en un requisito vigente o registrar el cambio concreto de requisito.
   Una instrucción nueva del tesista desplaza propuestas y planes no implementados;
   una regla validada en conflicto se resuelve con su fuente y autoridad correspondientes.
2. Definir actor, resultado observable, datos, permiso y prueba del recorrido en pocas
   líneas. Solo se abre una spec o ADR cuando el riesgo o la decisión lo justifican.
3. Implementar una porción vertical en la app, con migración y pruebas cuando apliquen.
   Revisar diff, seguridad, accesibilidad y regresión del recorrido afectado.
4. Actualizar una vez la fuente del cambio: requisito si cambió la regla, historia si
   cambió el criterio, pila si cambió prioridad, sprint backlog si cambió compromiso
   o estado. Registrar evidencia real y sincronizar la edición académica en hitos
   revisados, sin convertirla en requisito previo de cada cambio de código.

El trabajo ordinario lo hacen el tesista y Codex. Una revisión adicional se usa por
riesgo alto o para una entrega, sin crear una cadena fija de agentes. Los repositorios
mantienen sus responsabilidades: código de producto en `App-zhudaleli`, fuentes y
trazabilidad en `ZhudAleli`, y transferencia documental separada tras revisión y
confirmación de publicación.

## Limpieza gradual del contexto

Este archivo es la entrada operativa del calendario vigente. El plan de sprints v1.4,
la pila v1.7, las historias y la hoja anterior de S2 conservan su valor como fuentes
e historial. Antes de fusionar o archivar un archivo se revisan referencias y estado;
no se elimina evidencia, aprobación ni edición académica publicada. Las ediciones de
`documentacion/` se preparan desde el estado interno cuando su contenido esté revisado.

## Decisiones aún necesarias para comprometer fechas y alcance

- Medir la disponibilidad semanal real del tesista y de las personas que validan
  recorridos. La banda inicial es 16–25 h/semana; las fechas intermedias se revisarán
  con las horas efectivas y los resultados de cada semana.
- Delimitar y validar `RF-ACC-005` y `SPEC-002` antes de implementar las operaciones nuevas
  de superadministración. El rol fue validado por la presidenta según el tesista;
  la evidencia de esa validación sigue pendiente de adjuntar.
- Ordenar las historias de comercio y rendición dentro de S5 después de fijar la cadena
  productiva mínima. Los detalles P-04/P-05/P-07/P-08/P-09/P-10 se resuelven solo cuando
  el recorrido correspondiente los necesita.
- Precisar P-13/P-14 para cada operación offline antes de activarla.
