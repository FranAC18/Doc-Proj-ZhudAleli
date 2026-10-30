---
title: Direcciones de notificaciones por dispositivo
date: 2026-10-28
status: verified-locally
requirement: RF-ACC-001
sprint: S2
task: SB-S2-02
---

# Direcciones corregidas

El tesista precisa el comportamiento posterior a la corrección de suavidad:

- Escritorio (desde 768 px): entra desde la derecha hacia su posición y sale hacia la derecha.
- Móvil (menos de 768 px): entra de arriba hacia abajo y sale de abajo hacia arriba.

Se conservan 640 ms, las curvas de suavizado, ausencia de scroll horizontal, radio compartido
de 12 px, overlay, autocierre de 3 segundos, pausa por interacción, Escape, retorno de foco
y movimiento reducido. La salida anticipada sigue desde la posición actual. En móvil, se
calcula la distancia hasta el borde superior para que la tarjeta siga visible durante el
recorrido y los avisos apilados salgan completamente. CSS y JS públicos v6; caché PWA v17.

La fuente vigente del componente es el sistema de diseño y el inventario v1.7.
[Movimiento suave](movimiento-suave.md) conserva el corte anterior y sus límites de evaluación.
Esta nota sustituye únicamente las direcciones allí indicadas.

## Verificación de esta corrección

Script de navegador [verificar-movimiento.cjs](verificar-movimiento.cjs), adaptado para
comprobar el eje y sentido correctos en 360, 375, 768, 1280 y 1440 px. Resultados y capturas:
[direcciones-verificacion.json](direcciones-verificacion.json),
[escritorio a mitad de salida](direcciones-salida-1440.png) y
[móvil a mitad de salida](direcciones-salida-375.png).

Resultado: 11 escenarios correctos, sin errores JavaScript ni de recursos. Durante el
muestreo manual de frames se amplían los temporizadores para evitar que el autocierre
interrumpa las capturas; los casos de autocierre y pausa conservan los tiempos reales.

Se verifica también radio, falta de scroll horizontal, cierre al terminar, teclado,
retorno de foco, autocierre/pausa, movimiento reducido, cierre anticipado y texto largo.
No se repite la suite de backend: sus reglas y archivos conservan el contenido.

UI-01 no aplica (sin carga nueva). UI-02/04/05 verifican adaptación, tokens y componente
consistente; UI-03 conserva jerarquía y textos. UI-06 verifica teclado, reflujo y movimiento
reducido; contraste y zoom nativo siguen con los límites de la evidencia anterior.
UI-07/08 verifican error, recuperación y acciones de cierre, sin operaciones nuevas.

No cambia RF/HU/HT/pila/backlog ni se cierra SB-S2-02. Se enlaza la evidencia en el gestor
local preservando avances. Sin commit, push ni publicación académica.
