---
titulo: Criterios de diseño de la interfaz
version: "1.0"
fecha: 2026-10-12
autor: Tesista
estado: criterios-confirmados-y-propuestas-identificadas
fuentes: CAT-REQ-001-v1.1; constitucion-0.2.0; SISTEMA-DISENO
revision_usuarias: pendiente
publicacion: pendiente-de-confirmacion
---

# Criterios de diseño de la interfaz

La interfaz se diseñará para teléfonos, conectividad variable y distintos
niveles de experiencia digital. Debe mostrar con palabras claras qué puede
hacer cada persona y qué sucedió después de cada acción. La identidad visual
concreta y las pantallas todavía requieren revisión con las usuarias.

| Criterio | Aplicación prevista | Comprobación |
|---|---|---|
| Móvil | Formularios cortos, controles fáciles de tocar y tablas que se lean en pantalla estrecha. | Recorrido esencial desde 360 px sin desplazamiento horizontal accidental. |
| Accesibilidad | Etiquetas visibles, foco de teclado y texto además de color. | Contraste AA, teclado y zoom al 200 %. |
| Errores | Explicar el problema y conservar los datos válidos. | Una persona puede corregir y reenviar sin repetir todo. |
| Permisos | Mostrar acciones propias del cargo o encargo, y verificar permiso en servidor. | Casos permitidos y denegados. |
| Sin conexión | Distinguir registro local pendiente de registro confirmado. | Corte de red, recarga, reintento y cambio de cuenta en dispositivo compartido. |
| Documentos y avisos | Si se aprueba la ampliación, indicar vencimiento, responsable y resultado del envío. | Diseño posterior a la validación de alcance y privacidad. |

Los colores, símbolos, textos e imágenes culturales son una **propuesta
visual**, pendiente de validación con la organización. El prototipo no prueba
que la aplicación funcione. Cada recorrido implementado necesitará evidencia
de uso móvil, acceso permitido y denegado, error, recuperación y observaciones
de las usuarias.

## Historial de cambios

| Versión | Fecha | Cambio | Estado |
|---|---|---|---|
| 1.0 | 2026-10-12 | Se consolidan criterios de uso y se identifica lo que aún debe validarse. | Criterios documentados; identidad visual pendiente |
