---
version: "5.12"
fecha: 2026-10-30
autor: Codex por instrucción expresa del tesista
estado: preparado-para-revision
publicacion: pendiente
---

# Control de cambios 5.12

Solicitud: aplicar las mejoras inmediatas del informe de normalización conservando modularidad. [Base v2.2](../arquitectura/diseno_base_datos_v2.2_2026-10-30.md) y [ER v2.2](../arquitectura/modelo_er_integral_v2.2_2026-10-30.md) corrigen estructura técnica y mantienen reglas C01–C18, fuentes y límites de validación. Las ediciones anteriores permanecen intactas.

Se incorporan [requisitos 2.6](../requisitos/requisitos_generales_v2.6_2026-10-30.md), [HU 3.1](../historias/usuario/historias_usuario_v3.1_2026-10-30.md), [HT 2.2](../historias/tecnicas/historias_tecnicas_v2.2_2026-10-30.md), [pila 2.3](../pila_producto/pila_producto_v2.3_2026-10-30.md) y [backlog 1.9](../sprints/sprint_backlog_v1.9_2026-10-30.md), con avance técnico y sin cambiar criterios de negocio, prioridades, puntos ni aprobaciones. SB-S2-05 pasa a avance parcial; no se cierra. La discrepancia histórica SB-S1-03 se conserva.

En la app se implementan FK compuesta de propietario/contacto, contacto requerido para verificación, unicidad y comparación canónicas PostgreSQL, HMAC con contexto UUID y protección de carreras. Migración accounts.0004 aplicada en desarrollo; 13 tablas, 19 migraciones. Se preservan cuentas, contactos e historia; los códigos pendientes del formato anterior requieren reemisión.

Código publicado bajo autorización permanente: [c5899d37c7886cd2786e66ce75cb76a32eaa05db](https://github.com/FranAC18/App-zhudaleli/commit/c5899d37c7886cd2786e66ce75cb76a32eaa05db), rama de trabajo de la app. 44 pruebas PostgreSQL, controles Django, Ruff, diff-check y revisión independiente. No merge, tag, despliegue, Git del vault ni publicación académica. Los paneles de negocio siguen propuestos y sin tablas.

[Matriz N01–N18](../../docs/architecture/proposals/2026-10-30-correcciones-normalizacion.md), [checkpoint](../../docs/bitacora/checkpoints/2026-10-30-normalizacion.md) y [evidencia](../../docs/evidence/architecture/2026-10-30-normalizacion/verificacion.json). El gestor local se sincroniza por API conservando criterios marcados, orden y estados de sprint.
