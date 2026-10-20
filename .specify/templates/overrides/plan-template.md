---
title: "Plan de implementación: [FEATURE]"
type: implementation-plan
status: draft
date: "[DATE]"
spec: "[link-to-spec]"
branch: "[branch-name]"
write_owner: "[owner]"
---

# Plan de implementación: [FEATURE]

## Resumen

[Requisito principal, valor y enfoque técnico mínimo.]

## Contexto técnico (Technical Context)

- **Lenguaje/runtime**: Python 3.12.
- **Framework**: Django 5.2 LTS, plantillas Django y Bootstrap 5.
- **Persistencia**: PostgreSQL y ORM Django.
- **Pruebas**: [Django TestCase/pytest-django, integración y recorrido].
- **Módulo propietario**: [app Django].
- **Escala y datos**: [volumen esperado y sensibilidad].
- **Restricciones**: móvil, conectividad, accesibilidad, permisos y otras confirmadas.
- **Dudas técnicas**: [NEEDS CLARIFICATION o ninguna].

## Comprobación de la constitución (Constitution Check)

| Puerta | Evidencia en este plan | Resultado |
|---|---|---|
| Requisito confirmado | [enlace/registro] | [pass/fail] |
| Portabilidad | no depende del historial/modelo | [pass/fail] |
| Pruebas y permisos | [secciones] | [pass/fail] |
| Simplicidad e integridad | [decisión] | [pass/fail] |
| Cohesión y dependencias | [propietarios, contratos, consumidores y composición] | [pass/fail] |
| Entrega incremental | [alcance, compatibilidad, regresión y publicación si aplica] | [pass/fail] |
| UX/accesibilidad | [criterios] | [pass/fail] |
| Trazabilidad | [IDs] | [pass/fail] |
| Control humano/privacidad | [medidas] | [pass/fail] |

Un `fail` bloquea la implementación del trabajo afectado o requiere ADR y aprobación
explícita. No impide que el tesista cierre administrativamente el sprint y traslade pendientes.

## Fronteras y evolución modular

Referencia: constitución vigente y ADR-0006. Registrar:

- Responsabilidad del módulo y dueño de entidades, escrituras y migraciones.
- Dependencias, operaciones públicas/lecturas autorizadas y consumidores afectados; sin ciclos.
- Separación HTTP/reglas/datos necesaria; justificar servicios/consultas sin capas vacías.
- Composición y punto transaccional cuando varios cambios deban confirmar juntos.
- Incremento utilizable, dependencias disponibles y porciones del módulo todavía pendientes.
- Compatibilidad de esquema/contratos, regresión y operaciones PWA antiguas si aplica.
- Publicación conjunta y recuperación, si esta funcionalidad incluye una entrega piloto.

## Diseño de dominio y datos

- Entidades y responsabilidad de cada app.
- Invariantes, unicidad, unidades, precisión y zonas horarias.
- Relaciones y política de borrado/retención.
- Operaciones transaccionales y riesgo de concurrencia.
- Migración, compatibilidad hacia atrás y reversión.
- Auditoría: quién, cuándo, qué cambió y motivo, solo donde esté validado.

## Autorización y privacidad

| Operación | Permiso backend | Rol permitido | Rol denegado | Prueba negativa |
|---|---|---|---|---|
| [operación] | [permiso/policy] | [rol] | [rol] | [test] |

Lista los datos personales involucrados, minimización, visibilidad y registros que no deben
aparecer en logs o evidencias.

## Interfaz

- Mapa del recorrido y vistas.
- Formularios, mensajes y componentes reutilizados/nuevos.
- Estados vacío, error, éxito, sin permiso y carga.
- Adaptación móvil/escritorio y conectividad limitada.
- Validación de teclado, contraste, foco y lenguaje.

## Estructura del proyecto (Project Structure)

```text
apps/<module>/
├── models.py
├── migrations/
├── forms.py
├── views.py
├── urls.py
├── services.py        # solo si coordina reglas/transacciones reales
├── templates/<module>/
└── tests/
templates/components/
static/
specs/[###-feature]/
docs/evidence/
```

Sustituye el árbol por rutas reales y elimina archivos innecesarios.
Conservar descubrimiento nativo de modelos/migraciones; no crear apps futuras o `core` vacío.

## Estrategia de pruebas

- Criterio → prueba unitaria/integración/sistema.
- Permisos positivos y negativos.
- Límites, duplicados, concurrencia y recuperación.
- Migraciones y datos de demostración anónimos.
- Recorrido visual y accesibilidad.
- Comandos exactos a ejecutar.
- Recorridos anteriores e integración con consumidores afectados; límites de dependencia
  verificables cuando exista código. No interpretar pruebas locales como piloto integrado.

## Entrega y validación del incremento

- Versión/contenido disponible y entorno piloto, si forma parte del alcance.
- Migraciones, recursos, arranque, permisos, respaldo y recuperación antes de publicar.
- Tareas y evidencia de prueba con socias, sin convertir hallazgos en requisitos aprobados.
- Autorización concreta para Git/publicación; aceptar arquitectura no autoriza estas acciones.

## Evidencia y documentación

- Rutas que actualizarán la matriz, ADR, diccionario de datos, manual y bitácora.
- Evidencia esperada, formato, responsable y anonimización.
- Aporte previsto a capítulos/metodología/evaluación de la tesis.

## Riesgos y reversión

| Riesgo | Probabilidad/impacto | Mitigación | Señal | Reversión |
|---|---|---|---|---|
| [riesgo] | [valor] | [acción] | [detección] | [paso seguro] |

## Complejidad excepcional

| Excepción a la constitución | Necesidad demostrada | Alternativa simple descartada | ADR/aprobación |
|---|---|---|---|
| Ninguna prevista | — | — | — |
