---
title: Resumen Ejecutivo de Requisitos (Estado Actual)
type: proposal
status: draft
date: 2026-09-28
commit: pending
---

# Resumen del Estado Actual de Requisitos

Este documento presenta de forma clara y ordenada la situación actual de los requisitos funcionales (RF) y no funcionales (RNF) del proyecto Zhud Alelí, basados en la línea base aprobada en **CAT-REQ-001 v1.1**.

## 📊 1. Vista Global

- **Requisitos Confirmados:** 60 (Listos para ser especificados y desarrollados).
- **Requisitos Propuestos:** 2 (Pendientes de decisiones de negocio).
- **Requisitos Históricos (Sustituidos):** 12 (Reemplazados por capacidades modernas, ej. PWA).
- **Decisiones Pendientes (Parámetros):** 13 abiertas (P-02 a P-14), 1 cerrada (P-01).

---

## ✅ 2. Requisitos Confirmados (Listos para desarrollo)

### Sprint 1: Administración y Acceso
- **RF-ACC-001**: Usuaria interna necesita acceso seguro (inicio/cierre de sesión).
- **RF-ACC-002**: Directiva necesita administrar membresía.
- **RF-ACC-003**: Personas necesitan funciones según perfil, cargo y encargo.
- **RF-ACC-004**: Cada usuaria necesita un inicio comprensible (dashboard privado).

### Sprint 2: Planificación
- **RF-PLA-001**: Directiva necesita organizar jornadas y eventos.
- **RF-PLA-002**: Socias necesitan conocer su responsabilidad y participación.
- **RF-PLA-003**: Una socia puede asumir trabajo temporal (encargos).
- **RF-PLA-004**: Directiva y socias necesitan consultar pendientes.
- **RF-PLA-005**: La producción semanal necesita previsión sin crear existencias ficticias.

### Sprint 3: Asistencia y Participación
- **RF-ASI-001**: Socia necesita registrar presencia por instancia (entrada/salida separadas).
- **RF-ASI-002**: La organización necesita registros coherentes.
- **RF-ASI-003**: Registros sensibles requieren corrección controlada.
- **RF-ASI-004**: Socia y Directiva necesitan consultar el historial.
- **RF-ASI-005**: Algunas actividades requieren describir la participación adicional.
- **RF-ASI-006**: Faltantes deben resolverse sin proceso individual costoso (decisión en asamblea).
- **RF-ASI-007**: Autorregistro rápido en celulares mediante QR temporal y códigos alternativos.

### Sprint 4: Catálogo, Inventario, Trazabilidad y Comercial
- **RF-CAT-001**: Directiva y Tesorera necesitan catálogos históricos para configuración base.
- **RF-INV-001**: Catálogo comercial requiere valores vigentes e históricos.
- **RF-TRA-001**: El acopio de materia prima necesita origen y peso explícito.
- **RF-TRA-002**: El secado necesita datos mínimos reales (peso inicial/final y temperatura).
- **RF-TRA-003**: La organización necesita duración y merma calculada sin trabajo manual.
- **RF-TRA-004**: Lotes necesitan linaje trazable y estados no ambiguos.
- **RF-TRA-005**: La transformación de insumos no debe quedar implícita.
- **RF-INV-002**: Las existencias necesitan evidencia inmutable (mediante historial de movimientos).
- **RF-INV-003**: Entregas de feria necesitan origen y responsabilidad explícita.
- **RF-INV-004**: Productos físicos necesitan conciliación (recibido vs vendido).
- **RF-VEN-001**: Socia encargada necesita registrar ventas simples desde su stock.
- **RF-VEN-002**: La venta necesita diferenciar al comprador según el riesgo (crédito vs contado).
- **RF-VEN-003**: Organización y socia necesitan separar sus valores y ganancias.
- **RF-VEN-004**: Precio bajo valor base requiere control excepcional de la directiva.
- **RF-VEN-005**: Tesorera necesita aplicar políticas por volumen.
- **RF-VEN-006**: Feria multisocia necesita trazabilidad por persona.
- **RF-VEN-007**: La organización realiza ventas grandes propias (institucionales).
- **RF-VEN-008**: Pérdida de Internet no debe perder ventas (contingencia mediante comprobante manual).
- **RF-GAS-001**: Tesorera necesita registrar gastos generales.
- **RF-GAS-002**: Directiva necesita un resumen de gastos entendible.
- **RF-CXC-001**: Deben separarse los conceptos de custodia y dos tipos de deuda (socia vs externa).
- **RF-CXC-002**: Se necesitan permitir pagos parciales o abonos.
- **RF-CXC-003**: La feria necesita una rendición final verificable y calculable.

### Sprint 5: Reportes, Notificaciones y Sitio Público
- **RF-REP-001**: Directiva necesita reporte detallado de asistencia.
- **RF-REP-002**: Directiva necesita reporte de actividades y encargos.
- **RF-REP-003**: Directiva necesita reporte de producción trazable.
- **RF-REP-004**: Directiva necesita reporte de inventario y movimientos.
- **RF-REP-005**: Tesorera necesita reporte de ventas y cuentas por cobrar.
- **RF-REP-006**: Cada socia necesita su propio resumen privado de operaciones y deudas.
- **RF-NOT-001**: Usuarias necesitan recordar tareas y pendientes dentro del sistema.
- **RF-PUB-001**: Visitante necesita información pública básica y confiable.
- **RF-PUB-002**: Organización necesita controlar estrictamente las publicaciones externas.

### Requisitos No Funcionales (Transversales)
- **RNF-UX-001**: Funcionalidad completa y usable en pantallas pequeñas de 360px.
- **RNF-UX-002**: Accesibilidad técnica visual con contraste AA.
- **RNF-UX-003**: Interfaces en lenguaje cotidiano, no técnico.
- **RNF-CON-001**: Operación muy ligera, recursos de caché y resiliencia ante cortes.
- **RNF-SEC-001**: Autorización robusta implementada en backend, no solo oculta en la UI.
- **RNF-AUD-001**: Todo cambio sensible conserva un historial de la transacción (auditoría).
- **RNF-DAT-001**: Existencias físicas se derivan estrictamente de movimientos.
- **RNF-PRV-001**: Solo personal autorizado visualiza información interna.
- **RNF-PDF-001**: Los reportes y estados se deben descargar en formato PDF.

### Continuidad Operativa Offline (PWA)
- **RF-PWA-001**: Acceso a la interfaz web esencial sin conexión a red.
- **RF-PWA-002**: Capacidad de guardar registros esenciales directamente en el dispositivo.
- **RF-PWA-003**: Sincronización sin duplicados y con validación robusta al recuperar conectividad.

---

## 🟡 3. Requisitos Propuestos (Bloqueados)

No pueden ser desarrollados hasta que se resuelva la regla de negocio que los bloquea:

- **RF-COS-001**: La organización necesita conocer costos de producción directos. *(Bloqueado por P-06)*
- **RNF-OPS-001**: Copias de respaldo protegidas y restauración demostrable. *(Bloqueado por P-11)*

---

## 📝 4. Decisiones Operativas Pendientes (Parámetros)

Estos parámetros ("P-xx") determinan *cómo* funcionarán ciertas pantallas. Aunque la capacidad general esté aprobada, no se puede programar esa función específica sin conocer este dato:

- **P-02**: Duración del QR y autoridad de habilitación.
- **P-03**: Consecuencias reales de las faltas.
- **P-04**: Presentaciones, unidades, fórmulas y plantas.
- **P-05**: Compatibilidades, mermas y divisiones en producción.
- **P-06**: *(Propuesto)* Fórmula del costo completo y valoración de trabajo comunitario.
- **P-07**: Distribución equitativa de excedentes de stock compartido.
- **P-08**: Reglas, precios y límites de los descuentos por volumen.
- **P-09**: Impacto monetario de devoluciones y pérdida de inventario.
- **P-10**: Plazos y contingencia en comprobantes físicos durante ferias.
- **P-11**: *(Propuesto)* Política exacta, frecuencia y responsables de respaldos.
- **P-12**: Publicadores y recursos autorizados para el sitio web público.
- **P-13**: Lista de todas las acciones admitidas sin conexión (offline).
- **P-14**: Políticas de almacenamiento local, seguridad compartida y descarte en dispositivos.

*(Nota: P-01 ya fue cerrada y resuelta para el módulo de acceso básico).*
