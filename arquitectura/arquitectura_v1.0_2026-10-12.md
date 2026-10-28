---
titulo: Arquitectura prevista de Zhud Alelí
version: "1.0"
fecha: 2026-10-12
autor: Tesista
estado: decision-tecnica-vigente
fuentes: constitucion-0.2.0; ADR-0006; ARQUITECTURA-OBJETIVO
revision_directora: pendiente
publicacion: pendiente-de-confirmacion
---

# Arquitectura prevista de Zhud Alelí

La aplicación prevista será una sola aplicación web organizada por módulos.
Usará **Python y Django** para la lógica y las páginas, **PostgreSQL** para los
datos y **Bootstrap 5** para una interfaz adaptable a teléfonos. El tesista
confirmó este enfoque el 8 de octubre de 2026. La aplicación Django aún no
existe: este documento describe el diseño aprobado, no una instalación en uso.

## Partes de la aplicación

| Parte prevista | Responsabilidad principal | Relación importante |
|---|---|---|
| Acceso | Identidad, membresías y permisos. | Toda operación privada comprueba autorización. |
| Planificación | Actividades, responsables y encargos. | Asistencia y producción consultan actividades o encargos permitidos. |
| Asistencia | Entradas, salidas, participación y correcciones. | Conserva origen e historial de correcciones. |
| Trazabilidad | Materia prima, secado, lotes, inventario, ventas y cuentas. | Los saldos provienen de movimientos identificables. |
| Reportes | Consultas y archivos PDF. | Lee datos autorizados sin duplicar la fuente operativa. |
| Sitio público | Información aprobada para visitantes. | No expone datos privados. |

Cada módulo será responsable de sus propios datos y cambios. Las operaciones
que afecten varios registros se confirmarán juntas cuando sea necesario.
Las relaciones entre módulos se documentarán por funcionalidad. Los permisos
se comprueban en el servidor, también al recibir registros sincronizados.

## Uso con conexión intermitente

Las operaciones de asistencia y pesaje habilitadas podrán guardarse en el
dispositivo como **pendientes**. Al volver la conexión, el servidor comprobará
identidad, permiso y reglas antes de aceptarlas. El sistema distinguirá
«guardado localmente», «aceptado» y «necesita revisión»; un reintento no debe
duplicar datos. Las decisiones P-13 y P-14 deben fijar conservación y uso de
dispositivos compartidos antes de completar el diseño.

## Cuestiones por demostrar

| Cuestión | Evidencia necesaria |
|---|---|
| Ejecución de Django y PostgreSQL | Aplicación mínima en un entorno elegido, con conexión, archivos y HTTPS. |
| Recuperación | Política aprobada y prueba de restauración; P-11 sigue abierta. |
| Integridad | Pruebas de permisos, movimientos, transacciones, reintentos y conflictos. |
| Nuevas ideas de entrevista | Aprobar alcance antes de diseñar expediente documental, firma, WhatsApp automático, activos o comisiones nuevas. |

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.0 | 2026-10-12 | Se resume la arquitectura confirmada y sus comprobaciones pendientes. | Diseño técnico vigente; implementación no iniciada |
