---
title: Extracción de recursos reutilizables del login
type: frontend-evidence
status: verified-locally
date: 2026-10-28
requirement: RF-ACC-001
sprint: S2
task: SB-S2-02; porción visual de HT-GEN-004
commit: pending
---

# Recursos reutilizables del login

Por solicitud del tesista se extraen los SVG orgánicos del login a componentes de plantilla
compartidos: capas vinotinto, onda vertical y onda horizontal. El cambio de contraseña
reutiliza los dos primeros mediante un adorno con CSS independiente. Login y cambio comparten
también el botón con iconos de mostrar/ocultar contraseña. Las rutas y reglas de acceso no cambian.

El [inventario](../../../ui/RECURSOS-REUTILIZABLES-LOGIN.md) documenta propietarios,
parámetros, uso y límites. El [catálogo visual](catalogo.png) muestra los tres SVG y una
composición de formulario sin `login.css`. No es una pantalla nueva de producto.

## Verificaciones

- 18 pruebas de PostgreSQL correctas: frontend, recorridos de acceso y PWA. Se actualizan
  las expectativas de clases renombradas y la comprobación del nuevo CSS público.
- Veinte parejas de capturas idénticas en Chrome: login, error de campos obligatorios,
  cambio y primer acceso a 360, 375, 768, 1280 y 1440 px. Sin desbordamiento horizontal,
  errores JavaScript ni recursos fallidos; movimiento reducido para una comparación estable.
- Galería renderizada por Django sin la hoja del login. SVG decorativos con `aria-hidden`
  y `focusable=false`; el adorno no captura eventos ni interrumpe el tabulado.
- Mostrar/ocultar los campos de contraseña funciona mediante clic y teclado, conservando
  `aria-pressed` y el tipo del campo. Animación presente con movimiento permitido y ausente
  con la preferencia de reducirlo.
- PWA v11 instalada sobre las plantillas de prueba: 20 recursos públicos, nuevo CSS
  encontrado, retirada de v10 y alternativa pública disponible al navegar sin red.
- Django `check`, Ruff lint, sintaxis del Service Worker y `git diff --check` correctos.
  Ruff format global señala una línea preexistente en `config/settings/base.py`, ajena a
  esta extracción; no se reformatea ese archivo. Los archivos Python afectados se revisan
  por separado.

Detalle: [verificacion.json](verificacion.json). Las capturas se obtienen sobre plantillas
Django renderizadas con cuentas ficticias sin guardar datos; no son un recorrido de
autenticación en navegador. Las pruebas de PostgreSQL comprueban ese comportamiento
por separado. No se usaron datos de la organización ni se modificó la base de desarrollo.

## Alcance conservado

La foto, la composición del acceso y sus animaciones siguen siendo de esa pantalla.
El botón compartido aún usa los estilos de acceso; el adorno de formulario sí es independiente.
No se generalizan formularios, permisos ni operaciones de módulos futuros. No cambian
requisitos, historias, criterios, prioridades, fechas ni estados de terminación del backlog.
SB-S2-02 y HT-GEN-004 no se declaran completos. Validación con usuarias pendiente.
Cambios locales, sin commit, push ni publicación.
