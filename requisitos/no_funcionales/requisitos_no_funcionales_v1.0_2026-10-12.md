---
titulo: Requisitos no funcionales de Zhud Alelí
version: "1.0"
fecha: 2026-10-12
autor: Tesista
estado: final-aprobado-por-tesista
aprobacion_editorial: 2026-10-12
fuente_principal: "CAT-REQ-001 v1.1"
requisitos_confirmados_por_tesista: 9
requisitos_propuestos: 1
revision_directora: pendiente
validacion_organizacional_de_ajustes_v1_1: no-registrada
publicacion: pendiente-de-confirmacion
---

# Requisitos no funcionales

## Control de esta edición

Esta edición reúne los **nueve requisitos no funcionales confirmados por el
tesista** en el catálogo interno CAT-REQ-001 v1.1.
La definición heredada procede del catálogo R3 incorporado,
excepto cuando v1.1 la ajusta. En particular, `RNF-CON-001` incluye ahora
guardar y sincronizar registros habilitados sin conexión mediante una aplicación
web que conserva recursos y pendientes en el dispositivo (PWA). La exclusión offline
que aparece en R3 es histórica y no rige esta edición.

La aprobación de los cambios v1.1 corresponde al tesista. La revisión de la
directora y la validación de la organización para esos cambios no constan
realizadas. Ningún criterio de la tabla constituye evidencia de que el sistema
ya se haya implementado o probado.

## Calidad de uso e interfaz

| ID | Exigencia confirmada | Cómo se comprobará |
|---|---|---|
| RNF-UX-001 | La interfaz debe permitir completar las tareas esenciales en móviles desde 360 px, con acciones claras y formularios breves. | Recorrer tareas críticas en pantallas pequeñas y dispositivos reales sin desplazamiento horizontal accidental ni controles ocultos. |
| RNF-UX-002 | La interfaz debe ser accesible: contraste AA, teclado, foco visible, etiquetas comprensibles y errores recuperables. | Revisar zoom de 200 %, navegación por teclado, foco, resumen de errores y objetivos táctiles de al menos 44 px. |
| RNF-UX-003 | Se usa lenguaje cotidiano y el sistema calcula lo que no corresponde calcular manualmente a las socias. | Usuarias completan recorridos sin seleccionar roles técnicos ni hacer fórmulas manuales. |

## Continuidad, seguridad y datos

| ID | Exigencia confirmada | Cómo se comprobará |
|---|---|---|
| RNF-CON-001 | El sistema debe ser ligero y resistir cortes. Los recursos esenciales y los flujos habilitados funcionan con PWA; distingue guardado local, pendiente, aceptado y rechazado. | Cortar y recuperar conexión durante tareas habilitadas; no mostrar éxito remoto antes de confirmación ni duplicar operaciones al reintentar. Los detalles de P-13/P-14 siguen pendientes. |
| RNF-SEC-001 | Toda operación sensible verifica autorización en el servidor, aunque la interfaz o una petición directa intente eludirla. | Probar casos permitidos y denegados; una denegación no cambia datos. |
| RNF-AUD-001 | Correcciones, aprobaciones y excepciones deben poder reconstruirse con dato original, cambio o reversión, actor, fecha, autorización y motivo. | Un cambio sensible conserva la historia verificable dentro de la operación que lo confirma. |
| RNF-DAT-001 | Los cambios que afectan varias entidades se confirman juntos y las existencias se derivan de movimientos, sin totales editables sin respaldo. | Un error revierte todo; no se produce sobreventa, saldo negativo silencioso ni movimiento parcial. |
| RNF-PRV-001 | Se recoge solo la información necesaria y se separan claramente datos internos de contenido público. | Una persona sin permiso y el sitio público no muestran datos personales u operativos innecesarios. |

## Documentos de salida

| ID | Exigencia confirmada | Cómo se comprobará |
|---|---|---|
| RNF-PDF-001 | Los reportes descargables en PDF deben ser claros, trazables y comprensibles sin depender solo del color. | Cada PDF incluye título, periodo, filtros, fecha, unidades, totales conciliados y logo autorizado cuando esté disponible. |

## Requisito aún propuesto

`RNF-OPS-001` plantea copias protegidas y restauración demostrable. **No forma
parte de los nueve requisitos confirmados.** La política concreta, responsables,
proveedor, frecuencia, retención, pérdida de datos y tiempo de recuperación
tolerables, y autorización de restauración siguen
pendientes en P-11. Esta edición no fija esos valores ni presenta respaldos
ejecutados.

## Historial de esta edición

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Tesista | Edición final del tesista consolidada desde CAT-REQ-001 v1.1 y R3 incorporado; revisión de directora pendiente. | Final aprobado por el tesista |
