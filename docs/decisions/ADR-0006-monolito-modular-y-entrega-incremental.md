---
id: ADR-0006
title: Monolito modular con alta cohesión y entregas incrementales
type: decision
status: accepted
date: 2026-10-08
accepted_by: tesista
accepted_date: 2026-10-08
task_id: ARCH-ADOPT-001
module: transversal
constitution: 0.2.0
technical_review: completed-no-open-findings
related:
  - "[[../architecture/ARQUITECTURA-OBJETIVO]]"
  - "[[../evidence/architecture/2026-10-08-aceptacion-monolito-modular]]"
  - "[[ADR-0003-estructura-raiz-aplicacion-django]]"
  - "[[proposals/2026-10-07-monolito-modular-con-capas]]"
  - "[[proposals/2026-10-07-alternativas-arquitectura-entrega-incremental]]"
  - "[[proposals/2026-10-08-evolucion-modular-y-versiones-piloto]]"
tags: [proyecto/tesis, tipo/decision, modulo/transversal]
---

# ADR-0006: Monolito modular con alta cohesión y entregas incrementales

## Confirmación y alcance

El tesista confirmó el 2026-10-08: «confirmo que mantenemos monolito modular, alta cohesión
bajo acoplamiento» y pidió documentar comportamiento, mantenimiento, despliegue e incorporación
de capacidades. Se satisface su condición previa para enmendar la constitución. La evidencia
registra esa autorización humana; el agente no aprueba la arquitectura por inferencia.

Se acepta el estilo, sus límites y el flujo de entregas descritos aquí. Facturación electrónica,
gestión de clientes y funciones relacionadas con ARCSA siguen siendo ejemplos futuros, no
requisitos nuevos. No se aprueban proveedores, políticas PWA pendientes, cambios al cronograma,
implementación de SPEC-001 ni acciones Git/publicación por esta confirmación. La revisión
académica se conserva donde corresponda según el anteproyecto y la constitución.

## Contexto y motivo

Se necesita construir recorridos útiles, probarlos con las socias y añadir capacidades sin
rehacer la aplicación ni multiplicar su operación. La base Django/PostgreSQL y sus datos
relacionados permiten hacerlo con una unidad de entrega y límites internos verificables.
Se distingue crecimiento funcional de capacidad de carga y de publicación independiente.

## Decisión

1. Mantener Django, PostgreSQL, plantillas SSR/Bootstrap 5 y JavaScript progresivo; conservar
   la raíz y el descubrimiento nativo de modelos/migraciones de ADR-0003.
2. Organizar apps por responsabilidades de negocio, con capas internas pragmáticas:
   presentación HTTP, reglas/casos de uso y datos. Crear servicios/consultas cuando hay
   comportamiento real que los justifica, sin estructura hexagonal completa obligatoria.
3. Asignar un propietario a modelos, escrituras, invariantes y migraciones. Los demás módulos
   colaboran mediante operaciones públicas y lecturas autorizadas explícitas.
4. Conservar relaciones, claves foráneas y JOIN justificados. Evitar ciclos y depender de
   detalles internos; documentar consumidores y composición de operaciones entre módulos.
5. Mantener en una transacción común lo que debe confirmarse conjuntamente. Auditar y controlar
   concurrencia según los requisitos; una frontera de app no rompe la atomicidad de venta.
6. Comprobar permisos vigentes en backend desde cualquier entrada. La sincronización comparte
   reglas con SSR y revalida acceso también a resultados de reintentos/deduplicación.
7. Entregar versiones piloto conjuntas por incrementos, conservando compatibilidad y probando
   recorridos anteriores afectados. El código versionado y el despliegue son pasos distintos.
8. Incorporar un módulo nuevo mediante requisito/spec/plan/tareas, datos, permisos, integración,
   pruebas y migraciones delimitados. Ampliar un módulo existente cuando comparte responsabilidad.
9. Mantener `core` pequeño, dependencias externas aisladas donde aporten valor y configuraciones
   por entorno. No generar apps, APIs, repositorios o capas vacías por anticipación.
10. Evaluar carga y disponibilidad con escenarios y mediciones. Microservicios, colas de
    servidor, proyecciones persistidas y aislamiento genérico adicional requieren otro ADR
    y necesidad comprobada; la captura offline aprobada conserva sus specs propias.

## Consecuencias

Se busca localizar cambios y facilitar comprensión, pruebas y recuperación con una aplicación
integrada. No se promete tiempo fijo de implementación ni ausencia de cambios compartidos:
un esquema, permiso o significado usado por varios módulos exige revisar esos consumidores.

La aplicación se entrega conjuntamente y comparte recursos y radio de fallo. Puede ejecutarse
con varios workers o instancias; monolito no significa un único proceso. La independencia
de servicios continúa siendo una alternativa posterior que requeriría datos, contratos y
operación propios; extraer una capacidad no queda garantizado como un cambio automático.

## Tratamiento de alternativas y antecedentes

Las propuestas PRO-ARCH-002/003/004 se conservan como análisis previo; esta decisión recoge
el monolito con capas pragmáticas y entregas incrementales. Puertos/adaptadores pueden aislar
una integración real, sin imponerse a todo el dominio. Servicios independientes no se adoptan.

La propuesta de septiembre sobre aislamiento estricto se conserva como antecedente parcialmente
superado: no se adoptan prohibición universal de FK/JOIN, modelos/migraciones ocultos bajo
`infrastructure`, eventos/outbox de servidor o proyecciones obligatorias. PLAN-DESDE-CERO se
reconcilia sin cambiar el roadmap académico ni aprobar todas sus decisiones PWA.

## Aplicación y verificación

- Constitución 0.1.0 → 0.2.0, MINOR por expansión material de guía; ratificación original
  2026-07-21 conservada. Resumen operativo y templates se sincronizan.
- La guía canónica [[../architecture/ARQUITECTURA-OBJETIVO|ARQUITECTURA-OBJETIVO]] define flujo
  de peticiones, propietarios, dependencias, incorporación y publicación.
- SPEC-001 mantiene acceso básico y su plan nativo sin servicios/capas vacías. La aceptación
  de arquitectura no completa tareas ni reemplaza su puerta de diseño validado.
- Cada plan declara fronteras, consumidores, permisos, punto transaccional y regresión.
  Cada publicación verifica artefacto, migraciones, arranque, permisos y recuperación.
- La [[../evidence/architecture/2026-10-08-aceptacion-monolito-modular|evidencia]] y el
  [[../bitacora/checkpoints/2026-10-08-aceptacion-monolito-modular|checkpoint]] registran
  revisión y comprobaciones reales, sin atribuir código o pruebas funcionales inexistentes.
