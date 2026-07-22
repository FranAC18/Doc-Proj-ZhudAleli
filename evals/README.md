# Evaluaciones del agente

Antes de cambiar el modelo o las instrucciones, conserva casos representativos.

Cada evaluación debería indicar:

- Entrada del usuario.
- Contexto que el agente puede usar.
- Resultado esperado o propiedades obligatorias.
- Herramientas permitidas.
- Si necesita aprobación humana.

Casos iniciales recomendados:

1. Distinguir Comité de Asociación y pedir confirmación.
2. Proponer un modelo de asistencia sin duplicar registros.
3. Rechazar una afirmación no verificada sobre ARCSA.
4. Exigir auditoría para modificar inventario.
5. Ejecutar `manage.py check` después de una modificación.
