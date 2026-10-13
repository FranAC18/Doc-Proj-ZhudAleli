---
titulo: Candidato de historias técnicas de Zhud Alelí
version: "1.0"
fecha: 2026-10-12
autor: Codex, para revisión del tesista
estado: candidato-interno
fuentes: "CAT-REQ-001 v1.1; constitución 0.2.0; ADR-0006; arquitectura objetivo"
historias_tecnicas_propuestas: 9
revision_tesista: pendiente
revision_directora: pendiente
publicacion: no-autorizada
---

# Historias técnicas — candidato para revisión

## Propósito y alcance

Estas nueve historias describen el trabajo técnico necesario para sostener las
funciones y los **nueve requisitos no funcionales confirmados**. Son una propuesta
de organización del trabajo: no crean funcionalidades, no aprueban una
especificación de implementación y no afirman que exista una aplicación Django
funcional. Cada historia necesita desglose, responsables y pruebas en el plan de
su funcionalidad. La arquitectura modular vigente procede de ADR-0006 y la
constitución 0.2.0.

## HT-GEN-001 — Base modular y datos de identidad

**Como** equipo de desarrollo, **queremos** iniciar la aplicación con módulos de
responsabilidad clara y un usuario propio de Django desde el comienzo, **para**
evitar migraciones de identidad tardías y mantener comprensible cada cambio.

- **Se relaciona con:** `RF-ACC-001` a `RF-ACC-003`, HU-GEN-001 y HU-GEN-002;
  constitución 0.2.0 y ADR-0006.
- **Comprobación prevista:** antes de una primera migración estable se define el
  usuario propio; modelos, reglas, permisos y pruebas pertenecen al módulo que
  corresponde; una dependencia entre módulos tiene propietario y dirección claros.
- **Límite:** crear únicamente las partes requeridas por la especificación aprobada;
  no adelantar módulos ni capas vacías. SPEC-001 cubre solo acceso básico.

## HT-GEN-002 — Autorización y separación de datos

**Como** equipo de desarrollo, **queremos** comprobar permisos en el servidor en
cada operación sensible y separar datos privados de contenido público, **para**
proteger a las socias aunque alguien intente saltarse una pantalla.

- **Se relaciona con:** `RNF-SEC-001`, `RNF-PRV-001`, HU-GEN-002, HU-GEN-006,
  HU-GEN-011, HU-GEN-016 y HU-GEN-018.
- **Comprobación prevista:** cada operación sensible tiene un caso permitido y uno
  denegado; una denegación no cambia datos; el sitio público y una socia no ven
  información ajena. La sincronización también revalida la autorización vigente.
- **Límite:** las matrices concretas de cargos y encargos se fijan en cada
  especificación; P-01 solo está cerrado para el acceso básico.

## HT-GEN-003 — Integridad, movimientos y auditoría

**Como** equipo de desarrollo, **queremos** registrar movimientos y cambios
sensibles de forma completa, **para** poder reconstruir existencias, correcciones
y operaciones comerciales sin resultados parciales.

- **Se relaciona con:** `RNF-DAT-001`, `RNF-AUD-001`, HU-GEN-006 y HU-GEN-008
  a HU-GEN-014.
- **Comprobación prevista:** un fallo revierte todos los cambios de una operación
  que debe confirmarse junta; las existencias se concilian con movimientos;
  correcciones y excepciones conservan actor, fecha, motivo y valores necesarios.
- **Límite:** entidades, restricciones y concurrencia se precisan por
  funcionalidad; P-04, P-05 y P-09 siguen abiertos en sus detalles.

## HT-GEN-004 — Interfaz móvil, accesible y comprensible

**Como** equipo de diseño y desarrollo, **queremos** ofrecer recorridos breves
que funcionen en móvil y con teclado, **para** que las usuarias completen tareas
sin interpretar permisos técnicos ni calcular a mano.

- **Se relaciona con:** `RNF-UX-001`, `RNF-UX-002`, `RNF-UX-003` y todas las
  historias de la parte privada.
- **Comprobación prevista:** tareas esenciales se recorren desde 360 px sin
  controles ocultos; hay foco visible, contraste AA, etiquetas y errores
  recuperables; el sistema realiza los cálculos aprobados que correspondan.
- **Límite:** los recorridos se validarán con usuarias reales; esta historia no
  equivale a una prueba de usabilidad ya realizada.

## HT-GEN-005 — Captura local protegida

**Como** equipo de desarrollo, **queremos** preparar recursos esenciales y guardar
en el dispositivo únicamente operaciones habilitadas, **para** conservar trabajo
durante un corte sin confundirlo con una aceptación del servidor.

- **Se relaciona con:** `RF-PWA-001`, `RF-PWA-002`, `RNF-CON-001`, `RNF-PRV-001`
  y HU-GEN-019.
- **Comprobación prevista:** un dispositivo preparado abre el flujo permitido;
  una operación pendiente persiste al recargar; otra cuenta no puede leer su
  cola; los estados local y remoto se distinguen claramente.
- **Decisiones previas:** P-13 y P-14 deben concretar acciones habilitadas,
  dispositivo, sesión, retención y descarte. Asistencia y pesajes son el mínimo
  identificado, no autorización general para operar todo sin conexión.

## HT-GEN-006 — Sincronización sin duplicados

**Como** equipo de desarrollo, **queremos** enviar pendientes al recuperar la red
y reconocer reintentos, **para** que una respuesta perdida no cree dos registros
ni evite las reglas actuales del servidor.

- **Se relaciona con:** `RF-PWA-003`, `RNF-CON-001`, `RNF-SEC-001`, `RNF-DAT-001`
  y HU-GEN-019.
- **Comprobación prevista:** el servidor revalida identidad, permisos y reglas;
  repetir la misma operación crea un solo resultado; un conflicto o rechazo se
  muestra sin confirmar un cambio parcial.
- **Decisiones previas:** P-13 y P-14 definen tiempos, conflictos, orden,
  recuperación y política de resultados. No se presume válido un QR vencido ni
  una hora local como hora verificada por el servidor.

## HT-GEN-007 — Reportes y PDF claros

**Como** equipo de desarrollo, **queremos** formar reportes desde datos
autorizados y exportaciones comprensibles, **para** que sus totales se puedan
explicar y usar fuera de la pantalla.

- **Se relaciona con:** `RNF-PDF-001`, `RNF-PRV-001`, HU-GEN-015 y HU-GEN-016.
- **Comprobación prevista:** cada PDF muestra título, periodo, filtros, fecha,
  unidades y totales conciliados; no depende solo del color; incluye el logo
  autorizado cuando esté disponible y no expone datos ajenos.
- **Límite:** filtros, gráficos y generación concreta se definen en el diseño;
  este candidato no da por recibido el archivo oficial del logo.

## HT-GEN-008 — Configuración y entrega verificable

**Como** equipo de desarrollo, **queremos** separar la configuración de cada
entorno y comprobar que una versión arranque con sus datos y recursos compatibles,
**para** entregar incrementos utilizables y recuperables.

- **Se relaciona con:** ADR-0006, constitución 0.2.0 y las historias entregadas
  en cada incremento.
- **Comprobación prevista:** configuración y secretos quedan fuera de Git; antes
  de publicar se revisan esquema, migraciones y compatibilidad; después se
  comprueban arranque, acceso y recorridos críticos.
- **Decisiones previas:** entorno de ejecución, archivos, recuperación y política
  de respaldos requieren plan y validación; `RNF-OPS-001` permanece propuesto
  bajo P-11. Esta historia no elige proveedor ni autoriza despliegues.

## HT-GEN-009 — Pruebas, regresión y trazabilidad

**Como** equipo de desarrollo, **queremos** vincular requisitos, historias,
diseño y pruebas, **para** demostrar qué funciona en cada incremento y detectar
efectos sobre recorridos anteriores.

- **Se relaciona con:** los 51 requisitos funcionales confirmados, los nueve no
  funcionales, ADR-0006 y constitución 0.2.0.
- **Comprobación prevista:** cada cambio funcional tiene criterios y pruebas
  proporcionales; los permisos incluyen casos permitidos y denegados; una
  migración se verifica; antes de cerrar un incremento se revisan resultados,
  cambios y recorridos afectados.
- **Límite:** una prueba prevista no se presenta como ejecutada. La evidencia
  se registra cuando realmente exista.

## Estado de las decisiones

`RF-COS-001` y `RNF-OPS-001` continúan propuestos. Estas historias técnicas no
los convierten en trabajo de implementación aprobado. P-02 a P-14 mantienen sus
efectos en las especificaciones correspondientes. La revisión de la directora y
la validación de la organización sobre los ajustes v1.1 no constan realizadas.
Tampoco se fija aquí prioridad o estimación de la pila de producto.

## Historial de esta edición candidata

| Versión | Fecha | Autor | Cambio | Estado |
|---|---|---|---|---|
| 1.0 | 2026-10-12 | Codex | Agrupación de trabajo técnico derivado de requisitos confirmados y arquitectura aceptada para revisión editorial. | Candidato interno |
