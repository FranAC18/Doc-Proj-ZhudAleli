---
version: "5.14"
fecha: 2026-11-01
autor: Codex por instrucción del tesista
estado: aprobado-por-tesista-en-alcance-de-ferias
validacion_organizacional: pendiente
publicacion: publicada-para-revision-documental
---

# Control de cambios 5.14

## Solicitud y alcance

El tesista aprobó que el inventario de lotes de fábrica sea el modo ordinario de feria, que el acopio individual y su venta se habiliten juntos mediante una opción de la Superadministradora, y que únicamente la ganancia neta se reparta en partes iguales entre las encargadas: total recaudado menos el valor base correspondiente a las cantidades vendidas y los gastos de feria.

La regla afecta RF-INV-003, RF-VEN-001/006, RF-CXC-003, HU-INV-003/004, HU-VEN-006, HU-CXC-003, HT-PRE-003 y las tareas futuras SB-S5-02/05/06. Se publican requisitos 2.9, HU 3.4, HT 2.5, pila 2.6 y backlog 2.2 sin modificar IDs, prioridades, estimaciones, fechas ni estados de trabajo. Se sincronizaron al gestor local 9 registros, notas para SB-S5-02/05/06 y seis enlaces; la verificación confirmó que no cambiaron estados, prioridades, fechas, estimaciones, cierres de sprint ni criterios completados.

## Límites y pendientes

La aprobación se atribuye al tesista, no a la organización. CAT-REQ-001 v1.3 continúa como línea base y P-07 sigue abierto hasta validación organizacional directa. Esta publicación no acredita implementación ni validación de campo. Quedan por precisar el alcance global o por feria de la opción, la cantidad de lotes de fábrica, el tratamiento de centavos y saldos no positivos, la composición de encargadas si cambia durante la feria y el destino del importe base descontado.

La sincronización al gestor local se completó tras iniciar el servidor en `http://127.0.0.1:55478/`. La discrepancia y la evidencia interna de aprobación se conservan en el vault general. La publicación se verificará en el registro post-commit del vault.
