---
title: Módulos detallados de la aplicación
type: architecture
status: in-progress
date: 2026-08-25
tags:
  - proyecto/tesis
  - tipo/arquitectura
  - modulo/transversal
related:
  - "[[../requirements/CAT-REQ-001]]"
  - "[[ARQUITECTURA-OBJETIVO]]"
  - "[[../../agents/tesis/PROJECT_CONTEXT]]"
  - "[[../ui/SISTEMA-DISENO]]"
  - "[[../traceability/MATRIZ-TRAZABILIDAD]]"
---

# Módulos detallados de la aplicación

Fuente: CAT-REQ-001 v1.0 (`confirmed`), ARQUITECTURA-OBJETIVO, PROJECT_CONTEXT y
SISTEMA-DISENO. Cada módulo indica sus requisitos asignados, actores, entidades clave,
reglas confirmadas y dependencias.

---

## 1. `core` — Utilidades transversales

- **Sprint**: transversal (preparación previa a S1).
- **Responsabilidad**: tipos compartidos, constantes, funciones utilitarias y modelos base
  usados por varias apps.
- **No debe poseer**: reglas de negocio de ningún dominio específico.
- **Requisitos afectados**: transversales (`RNF-UX-001`, `RNF-CON-001`, `RNF-DAT-001`).

### Entidades potenciales

| Concepto | Descripción |
|---|---|
| Configuración general | Parámetros del sistema (nombre visible, zona horaria) |
| Catálogos base | Estados, unidades, tipos repetidos en varias apps |
| Utilidades de auditoría | Funciones para crear registros de cambio (autor, fecha, valores) |

### Reglas confirmadas

- El usuario personalizado se define desde la primera migración.
- Todas las relaciones organizativas usan claves y restricciones explícitas.
- Fechas y zonas horarias usan la configuración Django.
- Los borrados funcionales se deciden por dominio; no hay `soft delete` global.

---

## 2. `accounts` — Administración y acceso (Sprint 1)

- **Requisitos funcionales**: `RF-ACC-001`, `RF-ACC-002`, `RF-ACC-003`, `RF-ACC-004` (4).
- **Requisitos no funcionales**: `RNF-UX-001`, `RNF-UX-002`, `RNF-UX-003`,
  `RNF-CON-001`, `RNF-SEC-001`, `RNF-PRV-001` (6).
- **Spec existente**: `specs/001-acceso-usuarias-internas/spec.md` (`confirmed`).
- **Actores**: Directiva (presidenta, tesorera, secretaria), Socia operaria, Visitante.

### Requisitos funcionales detallados

#### RF-ACC-001 — Inicio y cierre de sesión

- Una cuenta activa puede iniciar sesión con nombre de usuario y contraseña.
- Credenciales inválidas, inexistentes o cuentas inactivas se rechazan sin revelar qué
  dato falló.
- Cerrar sesión impide reutilizar la sesión cerrada.
- Cambio de contraseña propia: demostrar conocimiento de la actual y confirmar nueva válida.
- Credenciales temporales de la primera cuenta deben cambiarse antes de usar el dashboard.
- Dashboard de bienvenida con opciones disponibles reales.
- Sesión vence a los 30 minutos sin actividad.

**Criterios de aceptación**: CA-ACC-001-01 a CA-ACC-001-11.

#### RF-ACC-002 — Gestión de membresías

- Alta, baja y cambio de estado de cuentas internas.
- Solo la Directiva autorizada puede administrar membresías.
- Historial de cambios de estado con autor, fecha y motivo.
- **Pendiente**: P-01 (matriz cargo por operación).

#### RF-ACC-003 — Matriz de cargos y permisos (RBAC)

- Roles: presidenta, tesorera, secretaria, socia operaria.
- Permisos por operación según cargo; herencia de permisos.
- RBAC con grupos/permisos Django y comprobación en backend.
- Pruebas de acceso permitido y denegado.
- **Pendiente**: P-01 (matriz cargo por operación y acceso puntual de soporte).

#### RF-ACC-004 — Dashboard personalizado

- Opciones según cargo y estado de la usuaria.
- Encargos temporales visibles cuando correspondan.
- **Pendiente**: definición de opciones por perfil.

### Entidades clave

| Concepto | Datos mínimos | Reglas |
|---|---|---|
| Cuenta interna | Username, estado activo/inactivo, credencial hasheada | Sin duplicados; nombre consistente |
| Perfil | Nombre completo, cargo, teléfono, foto | Privacidad; solo datos necesarios |
| Sesión | Cuenta, vigencia, finalización | 30 minutos de inactividad |
| Credencial temporal | Valor conocido por entregadora y receptora | Entrega presencial; cambio obligatorio |

### Matriz mínima de permisos (S1)

| Operación | Directiva | Socia operaria | Visitante |
|---|---|---|---|
| Iniciar sesión | Permitir (cuenta activa) | Permitir (cuenta activa) | Denegar |
| Ver dashboard privado | Permitir | Permitir | Denegar |
| Cambiar contraseña propia | Permitir | Permitir | Denegar |
| Cerrar sesión | Permitir | Permitir | No aplica |
| Administrar cuentas | Según RF-ACC-003 | Denegar | Denegar |

### Decisiones abiertas

| ID | Pregunta | Efecto |
|---|---|---|
| P-01 | Matriz cargo por operación y acceso puntual de soporte | Cerrar antes de specs de permisos sensibles |

---

## 3. `planning` — Planificación de actividades (Sprint 2)

- **Requisitos funcionales**: `RF-PLA-001`, `RF-PLA-002`, `RF-PLA-003`, `RF-PLA-004`,
  `RF-PLA-005` (5).
- **Spec pendiente**: por crear.
- **Actores**: Directiva, Socia operaria (asignada).

### Requisitos funcionales detallados

#### RF-PLA-001 — Registro de jornadas

- Crear, editar y consultar jornadas de trabajo.
- Datos: fecha, hora inicio, hora fin, descripción, estado.
- Solo la Directiva puede crear y modificar jornadas.

#### RF-PLA-002 — Registro de actividades

- Crear actividades dentro de una jornada.
- Datos: nombre, descripción, fecha, hora, duración estimada, estado.
- Relación con jornada y responsables.

#### RF-PLA-003 — Asignación de responsables

- Asignar una o varias socias a una actividad.
- Identificar quién es responsable de qué.
- Cambio de asignación con registro.

#### RF-PLA-004 — Estados de actividad

- Estados: pendiente, en progreso, completada, cancelada.
- Transiciones controladas por permisos.
- Historial de cambios de estado.

#### RF-PLA-005 — Consulta de planificación

- Ver actividades del día, semana o período.
- Filtrar por socia, estado o tipo.
- Vista compatible con móvil.

### Entidades clave

| Concepto | Datos mínimos | Reglas |
|---|---|---|
| Jornada | Fecha, hora inicio/fin, descripción, estado | Solo Directiva crea/edita |
| Actividad | Nombre, descripción, fecha/hora, duración, estado | Pertenecen a una jornada |
| Asignación | Actividad, socia, rol en actividad | Puede haber múltiples por actividad |
| Estado de actividad | Nombre, transiciones permitidas | Historial de cambios |

### Decisiones abiertas

- Ninguna directamente sobre este módulo; avanza con P-01 resuelta para permisos.

---

## 4. `attendance` — Control de asistencia y participación (Sprint 3)

- **Requisitos funcionales**: `RF-ASI-001`, `RF-ASI-002`, `RF-ASI-003`, `RF-ASI-004`,
  `RF-ASI-005`, `RF-ASI-006`, `RF-ASI-007` (7).
- **Spec pendiente**: por crear.
- **Actores**: Directiva (secretaria), Socia operaria.

### Requisitos funcionales detallados

#### RF-ASI-001 — Registro de entrada

- Registrar momento de llegada de cada socia.
- Datos: socia, fecha/hora del servidor, método de registro.
- Métodos: presencial (secretaria), QR, código alternativo, autorregistro.

#### RF-ASI-002 — Registro de salida

- Registrar momento de salida de cada socia.
- Datos: socia, fecha/hora del servidor, método de registro.
- Separación de entrada y salida.

#### RF-ASI-003 — Historial individual de asistencia

- Consultar registros de asistencia de cada socia.
- Filtrar por período, socia, estado.
- Exportar datos básicos.

#### RF-ASI-004 — Control de participación en actividades

- Vincular asistencia con actividades asignadas.
- Registrar participación efectiva.

#### RF-ASI-005 — Correcciones autorizadas

- Solo Directiva y encargada pueden corregir registros.
- Historial: autor, fecha/hora, valor anterior, valor nuevo, motivo.

#### RF-ASI-006 — Gestión de inconsistencias

- Detectar registros incompletos (falta entrada o salida).
- Marcar como pendiente de revisión.
- No generar sanciones automáticas.

#### RF-ASI-007 — Asistencia con QR y métodos alternativos

- **Ajuste confirmado**: la organización puede habilitar fases QR distintas para entrada y
  salida. La socia puede autorregistrar su propio evento.
- Token temporal, hora del servidor, sin datos personales.
- Autorregistro identifica socia y origen `self`.
- Registro delegado identifica autorizante, socia y motivo.
- Código alternativo como respaldo.
- Token vencido, repetido o de otra acción no modifica asistencia.
- QR no se presenta como prueba biométrica o infalible.

**Criterios**: CA-ASI-007-01 a CA-ASI-007-06.

### Entidades clave

| Concepto | Datos mínimos | Reglas |
|---|---|---|
| Registro de asistencia | Socia, tipo (entrada/salida), fecha/hora, método, origen | Hora del servidor; token temporal |
| Token QR | Valor único, expiración, acción permitida | Sin datos personales; vencimiento |
| Inconsistencia | Tipo, socia, fecha, estado, observación | Pendiente; sin sanción automática |
| Corrección | Autor, fecha, campo, valor anterior/nuevo, motivo | Transacción atómica |

### Decisiones abiertas

| ID | Pregunta | Efecto |
|---|---|---|
| P-02 | Duración del QR, habilitación de fases y casos de delegación | Cerrar durante la spec antes de implementar QR |
| P-03 | Consecuencias de faltas y autoridad que las decide | No bloquea asistencia; bloquea sanciones automáticas |

---

## 5. `traceability` — Catálogo, producción e inventario (Sprint 4)

- **Requisitos funcionales (producción/inventario)**: `RF-CAT-001`, `RF-INV-001`,
  `RF-TRA-001`, `RF-TRA-002`, `RF-TRA-003`, `RF-TRA-004`, `RF-TRA-005`, `RF-INV-002`,
  `RF-INV-003`, `RF-INV-004` (10).
- **Requisitos funcionales (ventas/gastos/saldos)**: `RF-VEN-001`, `RF-VEN-002`,
  `RF-VEN-003`, `RF-VEN-004`, `RF-VEN-005`, `RF-VEN-006`, `RF-VEN-007`, `RF-VEN-008`,
  `RF-GAS-001`, `RF-GAS-002`, `RF-CXC-001`, `RF-CXC-002`, `RF-CXC-003` (13).
- **Total S4**: 23 requisitos funcionales.
- **Spec pendiente**: por crear.
- **Actores**: Directiva, Socia operaria, Encargada (asignación temporal).
- **Decisión abierta**: ubicar ventas/gastos/cuentas por cobrar aquí o en app separada
  según cohesión confirmada por specs.

### Catálogo de productos aprobado

| Categoría | Producto | Variante | Tratamiento |
|---|---|---|---|
| Shampoo | Atuk sara, cebolla, romero, quinua | Con variantes | Producto elaborado |
| Acondicionador | Romero | — | Producto elaborado |
| Horchata/kit de hierbas | "Zhud Alelí" | Mezcla de plantas | Receta/versiones; nombre final pendiente |
| Mashua seca | — | — | Producto elaborado o seco |
| Tónico capilar | Romero, cebolla | Con variantes | Producto elaborado |
| Libro de recetas | "Zhud Alelí" | — | Inventario comercial sin acopio/secado |
| Kit por contrato | Composición del pedido | — | Vinculado al contrato |

### 5.1 Catálogo de productos (`RF-CAT-001`)

- Mantener catálogo de productos con nombre, categoría, variantes, unidades.
- Registro de presentaciones y conversiones (pendiente P-04).
- Lista cerrada de plantas a configurar con datos aprobados.

### 5.2 Acopio de materia prima (`RF-TRA-001`)

- Registrar entrega de materia prima: socia que entrega, fecha, peso, tipo de planta.
- Cada registro es un movimiento con trazabilidad.
- Peso inicial registrado automáticamente.

### 5.3 Secado (`RF-TRA-002`, `RF-TRA-003`)

- Variables confirmadas: peso inicial, peso final, temperatura (°C), humedad (opcional).
- Inicio y fin con fecha y hora automáticas.
- Control técnico del proceso de secado.

### 5.4 Transformación y lotes (`RF-TRA-004`, `RF-TRA-005`)

- Lote productivo cerrado y stock agotado son conceptos distintos.
- Solo una mezcla física crea un lote derivado con procedencia.
- Operaciones de lote y transformación dentro de `transaction.atomic`.
- Compatibilidades de mezcla/división, bajas, mermas y cierres excepcionales pendientes
  (P-05).

### 5.5 Inventario y movimientos (`RF-INV-001` a `RF-INV-004`)

- Inventario basado en movimientos; no total editable sin evidencia.
- Entradas, salidas, ajustes y conciliaciones registran movimiento.
- Custodia física, deuda propia, deuda externa y excedente son conceptos separados.
- Las existencias se derivan de movimientos o se concilian.

### 5.6 Ventas (`RF-VEN-001` a `RF-VEN-008`)

- Ferias pueden usar stock individual y compartido, identificado por línea de venta.
- Valor base fijo por producto, excedente de la socia, dos tipos de saldo.
- Pagos parciales dentro del alcance.
- Descuento configurable (RF-VEN-005): umbral, precio/porcentaje, vigencia y límite
  pendientes (P-08).
- Venta multiproducto: completa o revierte completa.
- Comprobante manual ante falta de Internet; registro tardío auditado.
- Numeración, custodia y verificación pendientes (P-10).

### 5.7 Gastos (`RF-GAS-001`, `RF-GAS-002`)

- Registrar gastos operativos: monto, categoría, fecha, responsable, descripción.
- Consulta y filtrado por período y categoría.

### 5.8 Cuentas por cobrar (`RF-CXC-001` a `RF-CXC-003`)

- Deuda de socia, cuenta por cobrar externa y excedente bruto son conceptos separados.
- Pagos parciales con registro de cada abono.
- Efecto de devoluciones, pérdidas y sobragos pendiente (P-09).

### Entidades clave

| Concepto | Datos mínimos | Reglas |
|---|---|---|
| Producto | Nombre, categoría, variantes, unidades, estado | Catálogo aprobado |
| Acopio | Socia, planta, peso, fecha, lote destino | Movimiento con trazabilidad |
| Secado | Peso inicial/final, temperatura, humedad, inicio/fin | Automático; hora del servidor |
| Lote | Producto, origen, cantidades, estado (abierto/cerrado/agotado) | Cerrado ≠ agotado; atomicidad |
| Movimiento de inventario | Tipo, producto, lote, cantidad, fecha, responsable | Deriva existencias; sin total editable |
| Venta | Fecha, productos, cantidades, valor, socia/feria, línea | Multiproducto: todo o nada |
| Cuenta por cobrar | Deudor, monto, pagos, saldo | Custodia ≠ deuda ≠ excedente |
| Gasto | Monto, categoría, fecha, responsable | Registro con trazabilidad |

### Decisiones abiertas

| ID | Pregunta | Efecto |
|---|---|---|
| P-04 | Presentaciones, unidades, conversiones, nombre de horchata/kit y lista de plantas | Cerrar antes de fórmulas y movimientos |
| P-05 | Compatibilidades de mezcla/división, bajas, mermas y cierres excepcionales | Cerrar antes de implementar excepciones de lote |
| P-06 | Fórmula de costo completo | Mantiene `RF-COS-001` en `proposed` |
| P-07 | Distribución del excedente de stock compartido | No bloquea ventas; bloquea distribución automática |
| P-08 | Umbral, precio/porcentaje, vigencia y límite de descuentos | Datos completos antes de activar políticas |
| P-09 | Efecto de devoluciones, pérdidas, bajas, anulaciones y sobrepagos | Cerrar antes de automatizar ajustes monetarios |
| P-10 | Numeración, custodia, digitación, verificación y plazo de contingencia | Cerrar en spec de feria |

---

## 6. `reports` — Reportes, recordatorios y sitio público (Sprint 5)

- **Requisitos funcionales**: `RF-REP-001`, `RF-REP-002`, `RF-REP-003`, `RF-REP-004`,
  `RF-REP-005`, `RF-REP-006`, `RF-NOT-001`, `RF-PUB-001`, `RF-PUB-002` (9).
- **Spec pendiente**: por crear.
- **Actores**: Directiva, Socia operaria (consulta), Visitante (público).

### 6.1 Reportes (`RF-REP-001` a `RF-REP-006`)

#### Reportes prioritarios confirmados

| Reporte | Contenido | Filtros esperados |
|---|---|---|
| Asistencia | Registros de entrada/salida, inconsistencias | Socia, período, estado |
| Actividades | Jornadas, actividades, asignaciones, estados | Fecha, socia, estado |
| Producción | Acopios, secados, lotes, transformaciones | Período, producto, socia |
| Inventario | Stock actual, movimientos, conciliaciones | Producto, lote, fecha |
| Ventas | Ventas realizadas, montos, líneas | Período, producto, feria |
| Cuentas por cobrar | Saldos, pagos, deudores | Período, deudor, estado |

#### Características de reportes

- Descargables en PDF con estructura, gráficos y logo de Zhud Alelí validados.
- No incluir afirmaciones ni reportes de cumplimiento sanitario.
- Filtros, gráficos y PDF pendientes de diseño (P-08, P-12).

### 6.2 Recordatorios/notificaciones (`RF-NOT-001`)

- Notificaciones internas para tareas pendientes, vencimientos y estados.
- Sin dependencia de servicios externos de push.

### 6.3 Sitio público (`RF-PUB-001`, `RF-PUB-002`)

- Contenido aprobado únicamente; no datos internos ni personales.
- No mostrar recursos sin aprobación.
- Textos, imágenes, dirección, redes, teléfono y publicadores pendientes (P-12).
- No incluir afirmaciones sanitarias.

### Decisiones abiertas

| ID | Pregunta | Efecto |
|---|---|---|
| P-12 | Textos, imágenes, dirección, redes, teléfono y publicadores autorizados | No bloquea estructura; bloquea contenido final |

---

## 7. `public_site` — Sitio público (Sprint 5, parte de `reports`)

> **Nota**: La arquitectura objetivo define `public_site` como app separada. Los
> requisitos `RF-PUB-001` y `RF-PUB-002` están asignados a Sprint 5 junto con reportes.
> La decisión de separar o integrar se confirma durante la spec de S5.

- **Contenido**: información del Comité, productos, actividades públicas.
- **No expone**: datos internos, información personal, afirmaciones sanitarias.
- **Control**: solo contenido aprobado por la Directiva.

---

## Requisitos no funcionales transversales

| ID | Requisito | Módulos afectados | Verificación |
|---|---|---|---|
| `RNF-UX-001` | Formularios funcionales desde 360px sin desplazamiento horizontal | Todos | Revisión móvil real o representativo |
| `RNF-UX-002` | Contraste AA, foco visible, zoom 200%, acciones ≥44×44px | Todos | Revisión por teclado, contraste, zoom |
| `RNF-UX-003` | Lenguaje cotidiano, sin términos técnicos, sin elegir roles | Todos | Prueba de comprensión con usuarias |
| `RNF-CON-001` | Ligero, sin recursos remotos obligatorios, recuperación ante corte | Todos | Prueba con conexión limitada |
| `RNF-SEC-001` | Sesión autorizada en cada contenido privado; denegaciones seguras | Todos | Pruebas positivas y negativas |
| `RNF-AUD-001` | Auditoría en transacción; historia de cambios con autor/fecha/valores | Todos los de escritura | Revisión de registros de auditoría |
| `RNF-DAT-001` | Existencias derivadas de movimientos; sin total editable | Inventario, lotes | Pruebas de conciliación |
| `RNF-PRV-001` | Datos mínimos necesarios; sin exposición de cuentas ni contenido interno | Todos | Revisión de pantallas y respuestas |
| `RNF-PDF-001` | Reportes en PDF con estructura, gráficos y logo validados | Reportes | Generación y revisión de PDF |

---

## Resumen por sprint

| Sprint | App | Requisitos funcionales | Requisitos no funcionales | Total |
|---|---|---|---|---:|
| S1 | `accounts` | 4 (`RF-ACC-*`) | 6 (`RNF-*`) | 10 |
| S2 | `planning` | 5 (`RF-PLA-*`) | — | 5 |
| S3 | `attendance` | 7 (`RF-ASI-*`) | — | 7 |
| S4 | `traceability` | 23 (`RF-CAT/INV/TRA/VEN/GAS/CXC-*`) | — | 23 |
| S5 | `reports` + `public_site` | 9 (`RF-REP/NOT/PUB-*`) | — | 9 |
| Transversal | `core` | — | 9 (`RNF-*`) | 9 |
| **Total** | | **48** | **15** | **63** |

>Nota: Los 9 `RNF-*` se asignan transversalmente y se verifican en cada sprint donde
>aplican.

---

## Decisiones abiertas globales

| ID | Pregunta | Módulos afectados |
|---|---|---|
| P-01 | Matriz cargo por operación y acceso puntual de soporte | `accounts` |
| P-02 | Duración del QR, habilitación de fases y casos de delegación | `attendance` |
| P-03 | Consecuencias de faltas y autoridad que las decide | `attendance` |
| P-04 | Presentaciones, unidades, conversiones, nombre horchata/kit, lista de plantas | `traceability` |
| P-05 | Compatibilidades de mezcla/división, bajas, mermas y cierres | `traceability` |
| P-06 | Fórmula de costo completo | `traceability` (proposed) |
| P-07 | Distribución del excedente de stock compartido | `traceability` |
| P-08 | Umbral, precio/porcentaje, vigencia y límite de descuentos | `traceability` |
| P-09 | Efecto de devoluciones, pérdidas, bajas, anulaciones y sobrepagos | `traceability` |
| P-10 | Numeración, custodia, digitación, verificación y plazo de contingencia | `traceability` |
| P-11 | Política y operación de respaldos | Transversal (proposed) |
| P-12 | Textos, imágenes, dirección, redes, teléfono, publicadores | `public_site` |

---

## Fuentes

- `docs/requirements/CAT-REQ-001.md` — Catálogo canónico v1.0 (`confirmed`).
- `docs/architecture/ARQUITECTURA-OBJETIVO.md` — Arquitectura objetivo.
- `agents/tesis/PROJECT_CONTEXT.md` — Contexto del proyecto.
- `docs/ui/SISTEMA-DISENO.md` — Sistema de diseño y criterios UX.
- `specs/001-acceso-usuarias-internas/spec.md` — SPEC-001 (`confirmed`).
- `docs/traceability/MATRIZ-TRAZABILIDAD.md` — Matriz de trazabilidad.
