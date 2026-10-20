---
codigo: ZA-ALC-001
titulo: Alcance del módulo de acceso de usuarias y roles
modulo: Acceso de usuarias y roles
fase: Fase 1 — Documento de alcance del módulo
version: 1.1
fecha: 2026-10-13
autor: Franklin Acero (tesista)
analista: Codex (asistencia de redacción)
estado: borrador-pendiente-de-aprobacion-del-tesista
fuentes_requisitos: "CAT-REQ-001 v1.2; requisitos_generales_v2.0; priorizacion_requisitos_v1.3"
revision_directora: pendiente
validacion_organizacional: no-atribuida-por-esta-edicion
publicacion: no-sincronizado
---

<table style="width:100%; border-collapse:collapse; font-family:'Heebo Light',Heebo,Arial,sans-serif;">
  <tr><td colspan="2" style="background:#642138;color:#F0EAC8;padding:14px;font-family:'Mallong Regular',Georgia,serif;font-size:22px;"><strong>[LOGO: Isotipo floral de 4 pétalos - ZHUD ALELÍ Productos Naturales]</strong><br>ZA-ALC-001 · Alcance del módulo de acceso de usuarias y roles</td></tr>
  <tr><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Control documental</th><th style="background:#642138;color:#F0EAC8;text-align:left;padding:8px;">Valor</th></tr>
  <tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Módulo</td><td style="padding:7px;border:1px solid #AC6E40;">Acceso de usuarias y roles (<code>accounts</code>)</td></tr>
  <tr><td style="padding:7px;border:1px solid #AC6E40;">Fase / entregable</td><td style="padding:7px;border:1px solid #AC6E40;">Fase 1 — Documento de alcance del módulo</td></tr>
  <tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Versión / fecha</td><td style="padding:7px;border:1px solid #AC6E40;">v1.1 / 2026-10-13</td></tr>
  <tr><td style="padding:7px;border:1px solid #AC6E40;">Autor / analista</td><td style="padding:7px;border:1px solid #AC6E40;">Franklin Acero (tesista) / Codex (asistencia de redacción)</td></tr>
  <tr style="background:#F0EAC8;"><td style="padding:7px;border:1px solid #AC6E40;">Estado</td><td style="padding:7px;border:1px solid #AC6E40;">Borrador — pendiente de aprobación del tesista</td></tr>
</table>

**Identidad visual:** Verde Bosque `#4C5B4A`, Borgoña `#642138`, Terracota `#AC6E40` y Crema Natural `#F0EAC8`; Mallong Regular para títulos y Heebo Light para texto, con equivalentes serif/sans-serif si no están disponibles.

### Historial de revisiones

| Versión | Fecha | Descripción del cambio | Responsable |
|---|---|---|---|
| v1.0 | 2026-10-13 | Emisión inicial del alcance del módulo, derivada de la línea base confirmada y priorizada. | Franklin Acero (tesista); borrador asistido por Codex |
| v1.1 | 2026-10-13 | Mejora de jerarquía y presentación; se conserva el contenido de alcance y requisitos. | Franklin Acero (tesista); edición documental asistida por Codex |

<h2 style="color:#642138;font-family:'Mallong Regular',Georgia,serif;border-bottom:2px solid #AC6E40;padding-bottom:5px;">1. Propósito y descripción general del módulo</h2>

El módulo proporciona acceso autenticado a las usuarias internas y hace cumplir, en el servidor, los permisos derivados del perfil, cargo organizativo o encargo vigente. También permite que la Directiva administre la vigencia de las membresías y que cada usuaria encuentre en su inicio privado las actividades, pendientes y encargos que le corresponden.

Su límite principal es la identidad y la autorización de acceso. No decide por sí mismo las reglas de asistencia, producción, ventas u otras operaciones: cada módulo de negocio conserva sus reglas y precisa los permisos que necesita. El soporte técnico no adquiere autoridad organizacional por prestar asistencia.

**Actores y perfiles de referencia confirmados:** Directiva, Socia operaria y Visitante. Visitante representa consulta pública, no una cuenta interna ni un rol que permita entrar a información privada. Presidenta, tesorera y secretaria son cargos organizativos; no se crean automáticamente como cuentas o perfiles técnicos distintos. Un encargo temporal puede habilitar únicamente las operaciones que le correspondan durante su vigencia.

<h2 style="color:#642138;font-family:'Mallong Regular',Georgia,serif;border-bottom:2px solid #AC6E40;padding-bottom:5px;">2. Objetivos de negocio y alineación con Zhud Alelí</h2>

- Restringir la información organizacional y productiva a usuarias autenticadas y autorizadas.
- Reflejar la estructura comunitaria: distinguir perfil, cargo, encargo temporal y apoyo técnico sin convertirlos en autoridades equivalentes.
- Mantener la historia organizativa cuando una membresía o cuenta se desactiva.
- Reducir errores de uso con un inicio privado claro y acciones pertinentes a cada usuaria.
- Proteger la confianza de las socias mediante autorización comprobada en el servidor, minimización de datos, privacidad y trazabilidad de cambios sensibles.
- Permitir que otros módulos consulten la identidad y autorización mediante contratos definidos, sin escribir directamente en los datos que pertenecen a este módulo.

<h2 style="color:#642138;font-family:'Mallong Regular',Georgia,serif;border-bottom:2px solid #AC6E40;padding-bottom:5px;">3. Entregables clave y funcionalidades incluidas (In-Scope)</h2>

<table style="width:100%;border-collapse:collapse;font-family:'Heebo Light',Heebo,Arial,sans-serif;">
  <thead><tr style="background:#642138;color:#F0EAC8;"><th style="padding:8px;border:1px solid #AC6E40;">ID</th><th style="padding:8px;border:1px solid #AC6E40;">Entregable o capacidad incluida</th><th style="padding:8px;border:1px solid #AC6E40;">Importancia</th><th style="padding:8px;border:1px solid #AC6E40;">Requisito(s) relacionado(s)</th></tr></thead>
  <tbody>
    <tr style="background:#F0EAC8;"><td>A1</td><td>Autenticación de usuarias internas: iniciar y cerrar sesión; rechazar credenciales inválidas y cuentas inactivas sin revelar información sensible.</td><td><strong>Esencial</strong></td><td>RF-ACC-001; RNF-SEC-001; RNF-PRV-001</td></tr>
    <tr><td>A2</td><td>Autorización en backend según perfil, cargo, encargo vigente y permiso de la operación; denegar accesos directos no autorizados sin modificar datos.</td><td><strong>Esencial</strong></td><td>RF-ACC-003; RNF-SEC-001</td></tr>
    <tr style="background:#F0EAC8;"><td>A3</td><td>Administración de membresías por la Directiva, incluida activación y desactivación sin borrar la historia; protección frente a cambios por socias sin permiso.</td><td><strong>Alta</strong></td><td>RF-ACC-002; RNF-AUD-001; RNF-DAT-001</td></tr>
    <tr><td>A4</td><td>Inicio privado comprensible que presenta actividades, pendientes y encargos propios con acciones disponibles según la situación vigente.</td><td><strong>Complementaria</strong></td><td>RF-ACC-004; RNF-UX-001; RNF-UX-002; RNF-UX-003</td></tr>
    <tr style="background:#F0EAC8;"><td>A5</td><td>Registro trazable de cambios sensibles de cuenta, membresía y autorización, conservando actor, fecha y resultado conforme al requisito de auditoría.</td><td><strong>Esencial</strong></td><td>RNF-AUD-001; RNF-PRV-001</td></tr>
    <tr><td>A6</td><td>Contrato de integración para que los módulos consumidores consulten identidad y autorización por operaciones explícitas y lecturas autorizadas.</td><td><strong>Esencial</strong> para las operaciones protegidas</td><td>RF-ACC-003; RNF-SEC-001; RNF-DAT-001</td></tr>
    <tr style="background:#F0EAC8;"><td>A7</td><td>Revalidación de sesión, cuenta y permisos en el servidor al recibir operaciones sincronizadas que dependan de identidad autenticada.</td><td><strong>Esencial</strong> para operaciones sincronizadas</td><td>RF-PWA-003; RNF-CON-001; RNF-SEC-001</td></tr>
    <tr><td>A8</td><td>Artefactos verificables del módulo: matriz de perfiles/cargos/encargos y permisos por operación, reglas de acceso, flujos de cuenta y criterios de aceptación, sujetos a las decisiones abiertas indicadas en este documento.</td><td><strong>Esencial</strong> como base de especificación y verificación</td><td>RF-ACC-001 a RF-ACC-004; RNF-SEC-001; RNF-AUD-001; RNF-PRV-001</td></tr>
  </tbody>
</table>

La importancia reproduce la clasificación aprobada por el tesista en la priorización v1.3; sirve para cuidar riesgos y dependencias. No cambia el orden del plan de sprints ni resuelve permisos operativos que los requisitos asignan a especificaciones posteriores.

<h2 style="color:#642138;font-family:'Mallong Regular',Georgia,serif;border-bottom:2px solid #AC6E40;padding-bottom:5px;">4. Exclusiones explícitas (Out-of-Scope)</h2>

- Registro de asistencia, faltas, justificativos y multas; pertenecen al módulo de asistencia, que consumirá identidad y permisos. La validación de multas por la Tesorera no se implementa aquí.
- Registro o aprobación de jornadas, producción, pesajes, inventario, ventas, gastos, pagos, reportes o contenido público; sus reglas pertenecen a los módulos respectivos.
- Autoregistro público de cuentas, cuentas de visitantes y exposición de información privada a visitantes.
- Concesión de autoridad de negocio al soporte técnico, permisos ilimitados o acceso privilegiado implícito.
- Reglas no confirmadas de alta/invitación, recuperación o cambio de contraseña, complejidad/rotación de credenciales, caducidad y duración de sesión, bloqueo tras intentos, factores adicionales, nombres de usuario o granularidad final de permisos. No se inventarán en este alcance.
- Inicio de sesión sin conexión, administración local offline de cuentas o aceptación de permisos en el dispositivo sin revalidación del servidor. La disponibilidad de una interfaz PWA no equivale a autenticar o autorizar offline.
- Construcción o despliegue de la aplicación. Este documento define alcance; no afirma que exista una aplicación Django funcional ni que el módulo esté implementado o probado.

<h2 style="color:#642138;font-family:'Mallong Regular',Georgia,serif;border-bottom:2px solid #AC6E40;padding-bottom:5px;">5. Restricciones, supuestos y dependencias técnicas</h2>

### Restricciones

- Tecnología prevista por la constitución: Python 3.12, Django 5.2 LTS, PostgreSQL, Bootstrap 5 y plantillas Django con JavaScript progresivo mínimo. La cuenta de usuario personalizada se define antes de la primera migración estable.
- La autorización vive en backend y se comprueba también en accesos directos y operaciones sincronizadas. Ocultar una opción en la interfaz no constituye control de acceso.
- El módulo posee las escrituras de cuentas, membresías y asignaciones que se le definan. Otros módulos usan operaciones públicas y lecturas autorizadas; no modifican directamente sus tablas internas.
- Las operaciones que deban cambiar varias entidades de manera indivisible usan una transacción común y preservan sus invariantes.
- La interfaz debe ser clara en móvil desde 360 px, navegable por teclado, con contraste AA, foco visible, texto además de color y errores recuperables.
- Se minimizan los datos personales. El inicio privado y los datos de cuenta no se exponen en el sitio público ni en cachés públicas.

### Supuestos explícitos

- Una usuaria interna necesita una cuenta vigente asociada a una membresía habilitada; desactivar no elimina operaciones o evidencias históricas.
- Directiva, Socia operaria y Visitante son los perfiles de referencia; cargos y encargos se representan por separado y limitan operaciones según vigencia.
- El visitante consulta únicamente contenido público aprobado y no requiere autenticación interna.
- Cada especificación de negocio indicará las operaciones, cargos y encargos autorizados que consume. Este documento no crea un permiso general para toda una categoría.

### Dependencias y decisiones abiertas

| Dependencia o decisión | Estado conocido | Efecto sobre este módulo |
|---|---|---|
| CAT-REQ-001 v1.2 y documento general de requisitos v2.0 | Línea base confirmada por el tesista; revisión académica de la directora y validación directa de la organización para los ajustes no se atribuyen aquí. | Son la fuente de requisitos funcionales y no funcionales del alcance. |
| P-01 — acceso básico | Cerrada para acceso básico según el catálogo. | No cierra la matriz detallada de permisos de cada operación de negocio. |
| SPEC-001 — acceso de usuarias internas | El índice de funcionalidades la registra confirmada, con plan aprobado y tareas planificadas; su alcance es acceso básico. | Debe conservarse y revisarse su compatibilidad al elaborar casos de uso; esta edición no la reemplaza ni amplía automáticamente. |
| Permisos por cargo, encargo y operación | Requieren detalle en cada especificación de negocio. | No puede completarse aquí una matriz definitiva para asistencia, producción, finanzas y publicación. |
| Reglas de credenciales, sesión y recuperación | No quedan fijadas por RF-ACC-001 a 004. | Deben decidirse antes de especificar o implementar el comportamiento afectado. |
| Integración PWA y sincronización | RF-PWA-003 exige revalidar sesión, permisos y reglas en el servidor; los detalles de retención y dispositivo compartido dependen de P-13/P-14. | La cola local no extiende permisos revocados ni elude controles al sincronizar. |

## Fuentes y trazabilidad

- CAT-REQ-001 v1.2, fuente interna canónica, en particular perfiles organizacionales, RF-ACC-001 a RF-ACC-004, RNF de seguridad/auditoría/privacidad e invariantes de sincronización.
- Requisitos generales v2.0, edición completa en tablas.
- Priorización de requisitos v1.3, clasificación de importancia aprobada por el tesista.
- Índice de funcionalidades activas, estado y límite declarado de SPEC-001.
- Manual de marca Zhud Alelí suministrado por el tesista; la plantilla de control visual de este documento sigue además los colores y tipografías indicados directamente por el tesista en su solicitud.

**Puerta de avance:** este entregable permanece en borrador hasta que el tesista revise y apruebe el alcance. Tras esa aprobación se elaborará la Fase 2 (casos de uso detallados) para este mismo módulo; no se inicia otro módulo antes de cerrar la secuencia solicitada.
