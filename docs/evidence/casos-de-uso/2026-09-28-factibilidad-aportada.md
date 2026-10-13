---
title: Factibilidad aportada y exigencia de operación sin conexión
type: evidence
status: recorded
id: EVID-FACT-001
date: 2026-09-28
task_id: CU-REVIEW-001
source_type: user-provided-document-text
source_medium: texto de factibilidad pegado por el tesista durante la revisión
original_file: not-provided
document_date: not-verified
claimed_reference_date: 2026-09-22
phase: pre_commit
commit: pending
module: transversal
sprint: transversal
related:
  - "[[2026-09-28-cronograma-presupuesto-stack]]"
  - "[[2026-09-28-analisis-coherencia]]"
  - "[[../../requirements/proposals/2026-09-28-casos-de-uso]]"
  - "[[../../requirements/CAT-REQ-001]]"
  - "[[../../architecture/PLAN-DESDE-CERO]]"
tags:
  - proyecto/tesis
  - tipo/evidencia
  - modulo/transversal
---

# Factibilidad aportada y exigencia de operación sin conexión

## Actualización posterior de la referencia

El tesista aportó después el nuevo Gantt, dos imágenes de presupuesto y la tabla tecnológica:
[[2026-09-28-cronograma-presupuesto-stack|EVID-PLAN-002]]. La referencia actual para esta
revisión es **16 semanas y USD 2.869,00**. Las menciones de 1.845 y septiembre–febrero
que siguen describen el texto recibido anteriormente; no constituyen alternativas vigentes.
El stack aportado y la exigencia offline también quedan registrados en la nueva evidencia.

## Procedencia y alcance

El 28/09/2026 el tesista respondió a la consulta sobre la factibilidad mencionada por el PDF.
Proporcionó texto con secciones 1, 2.1–2.7 y 3 y marcas de páginas 2 a 8. No se recibió
archivo original, portada, firma ni fecha interna verificable. La fecha 22/09 procede de la
referencia del PDF académico, no de metadatos comprobados de esta nueva fuente.
Este registro es un **extracto estructurado fiel**, no una reproducción íntegra ni un acta
firmada. Permite recuperar los cambios relevantes sin depender del historial de conversación.

## Instrucción explícita del tesista

> guardar y sincronizar registros sin conexión, eso se debe hacer si o si

La instrucción fija una condición obligatoria del trabajo de diseño solicitado. No se
interpreta como aprobación de parámetros no definidos, de todas las operaciones offline,
de una infraestructura ya probada o de la organización/directora. Se registra la necesidad
de reconciliar los artefactos canónicos, conservando su historia y sus puertas de validación.

## Contenido recibido por sección

| Sección | Contenido relevante aportado |
|---|---|
| 1 y 2 | Evalúa viabilidad técnica, operativa, económica, temporal y social/usabilidad; afirma condiciones favorables con recursos disponibles. |
| 2.1 Técnica | Python, Django, PostgreSQL, Django Templates/HTML SSR, Bootstrap 5, CSS y JavaScript. Cinco módulos: administración/acceso, planificación, asistencia, trazabilidad y dashboard/reportes. Arquitectura modular para un estudiante; sin SPA ni API frontend-backend completa. |
| 2.1 Infraestructura | Propone Vercel para componentes compatibles y Supabase para persistencia PostgreSQL. La tabla económica etiqueta Vercel como frontend y Supabase como backend/base de datos. |
| 2.1 PWA | Instalable; continuidad de funcionalidades esenciales durante interrupciones pese al Internet actualmente estable. Manifest y Service Worker; Cache Storage para recursos/interfaz; IndexedDB para asistencias, pesajes u otros pendientes de sincronización. |
| 2.1 Integridad | Transacción completa o reversión para producción, inventario, despachos, cuentas por cobrar y asistencia. Usuarios/grupos/permisos Django para RBAC por cargos. |
| 2.2 Operativa | Centralizar planificación, asistencia, producción, inventario, despachos y cuentas por cobrar. Analizar, diseñar, implementar, probar y validar cada módulo progresivamente. |
| 2.3 Económica | Inversión del investigador; contraparte aporta instalaciones, disponibilidad y equipos. El texto cita presupuesto del anteproyecto USD 1.845; la tabla suma USD 2.869. No cuantifica ahorro sin medición previa/posterior. |
| 2.4 Temporal | Cuatro meses/16 semanas: 1–2 requisitos, 3–4 diseño/PWA, 5–12 módulos con pruebas, 13–14 integración/usabilidad/offline/sincronización, 15–16 validación/capacitación/manuales. |
| 2.5 Social/UX | Teléfonos, interacción táctil, seleccionar/tocar/confirmar, opciones predefinidas, formularios simplificados, teclado numérico para pesos/cantidades, validación con usuarias y paneles comprensibles. |
| 2.6 Beneficios | Organización, trazabilidad y control económico; mejoras potenciales sin prometer ahorros medidos ni resultados de implementación. |
| 2.7 General | Afirma viabilidad dentro de un periodo septiembre de 2026 a febrero de 2027. |
| 3 Conclusión | Declara factible el proyecto con ejecución incremental, 16 semanas y continuidad PWA de operaciones esenciales. |

## Tabla económica recuperada para comprobación

| Rubro | Cantidad | Unitario USD | Total USD |
|---|---:|---:|---:|
| Laptop de desarrollo | 1 | 1.512,00 | 1.512,00 |
| Computadoras existentes | 2 | 0,00 | 0,00 |
| Cable Ethernet | 2 | 7,50 | 15,00 |
| Stack tecnológico | 1 | 0,00 | 0,00 |
| Vercel | 4 meses | 0,00 | 0,00 |
| Supabase | 4 meses | 0,00 | 0,00 |
| Dominio | 1 año | 20,00 | 20,00 |
| Desarrollo | 4 meses | 300,00 | 1.200,00 |
| Papel | 1 | 5,00 | 5,00 |
| Impresiones | 100 | 0,04 | 4,00 |
| Útiles | 1 | 10,00 | 10,00 |
| Energía | 4 meses | 10,00 | 40,00 |
| Internet | 4 meses | 12,00 | 48,00 |
| Transporte | 6 viajes | 2,50 | 15,00 |
| **Total** | | | **2.869,00** |

Los importes son datos de la fuente, no precios actuales verificados. La diferencia frente
a USD 1.845 es **USD 1.024**. La aportación posterior del tesista identifica USD 2.869 como
presupuesto actualizado; la selección de la referencia queda resuelta en EVID-PLAN-002.

## Cambios que exige al conjunto documental

1. Versionar la revisión de la exclusión offline de CAT-REQ-001; no cambiar los IDs históricos
   `superseded` sin registrar su sustitución/reactivación y los criterios nuevos.
2. Mantener CU-OFF-01 y CU-OFF-02 en el diseño solicitado. Asistencia y pesajes están
   mencionados expresamente; «otros registros» no autoriza automáticamente inventario,
   ventas, pagos o administración de permisos sin red.
3. Precisar políticas de tiempo y QR, sesión local, cuenta compartida, revalidación de permisos,
   reintentos, idempotencia, conflictos, dependencias y retención. Son detalles propuestos
   para la spec; no fueron resueltos por el texto de factibilidad.
4. Distinguir la página inicial y autenticación de SPEC-001 del shell PWA y el almacenamiento
   local de datos de negocio; no cachear indiscriminadamente contenido privado.
5. Propagar la referencia actualizada de EVID-PLAN-002: 16 semanas y USD 2.869; conservar
   septiembre–febrero y USD 1.845 únicamente como antecedentes del texto anterior.
6. Documentar dónde se ejecuta Django y sus tareas de sincronización; Supabase PostgreSQL
   no sustituye por sí mismo al código backend Django. Ver fuentes oficiales del informe.

La factibilidad afirma viabilidad; esta sesión no la demuestra mediante despliegue,
pruebas con dispositivos o mediciones de costo. El análisis conserva esa distinción.
