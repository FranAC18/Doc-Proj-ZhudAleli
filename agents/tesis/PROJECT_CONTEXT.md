# Contexto del proyecto de tesis

## Identificación

- **Título:** Desarrollo de una aplicación web para la gestión organizacional del Comité
  de Mujeres Indígenas “Tránsito Amaguaña” de la parroquia Zhud, provincia del Cañar.
- **Modalidad:** Proyecto técnico.
- **Organización beneficiaria:** Comité de Mujeres Indígenas “Tránsito Amaguaña” de la
  parroquia Zhud.
- **Unidad productiva:** Zhud Alelí.
- **Escala descrita en el anteproyecto:** 12 socias legales y 6 socias activas.

## Problema

La gestión organizacional se realiza parcialmente de forma empírica: asignación verbal
de tareas, registros de asistencia con omisiones, falta de control técnico sobre pesajes y
tiempos de secado, y poca trazabilidad de materia prima, mermas, lotes e inventario.
Esto dificulta la planificación, la distribución de responsabilidades, el control interno,
la rendición de cuentas y la toma de decisiones.

## Objetivo general

Desarrollar una aplicación web para la gestión organizacional del Comité de Mujeres
Indígenas “Tránsito Amaguaña” de la parroquia Zhud, provincia del Cañar.

## Objetivos específicos

1. Analizar los procesos organizativos y productivos mediante técnicas de levantamiento
   de requerimientos.
2. Desarrollar módulos de gestión organizacional, trazabilidad productiva y control de
   acceso mediante un enfoque ágil basado en Scrum.
3. Evaluar la adecuación funcional con base en ISO/IEC 25010:2023.

## Usuarios previstos

- **Directiva:** un perfil técnico con cargos de presidenta, tesorera y secretaria; la interfaz se
  personaliza según el cargo.
- **Socias operarias:** un perfil técnico para consultar y registrar información productiva; una
  puede recibir temporalmente un encargo de producción o de feria/venta.
- **Visitantes externos:** consultan información pública en una landing page.

## Módulos previstos

### Planificación de actividades

Registro de jornadas, actividades, responsables, fechas y estado.

### Control de asistencia y participación

Registro de entrada y salida, historial individual y participación en actividades.

### Trazabilidad productiva

Acopio de materia prima, socia que entrega, peso, secado, transformación, lotes, mermas,
productos resultantes e inventario.

### Reportes y gestión de información

La primera versión incluirá reportes de asistencia, actividades y encargos, producción,
inventario, ventas y cuentas por cobrar, descargables en PDF con estructura, gráficos y logo
de Zhud Alelí validados.

### Administración y acceso

Autenticación, roles, permisos y página pública.

## Stack y método

- Python y Django.
- PostgreSQL.
- Bootstrap 5 y diseño responsivo.
- Arquitectura MTV de Django.
- Desarrollo iterativo basado en Scrum.
- Evaluación de adecuación funcional según ISO/IEC 25010:2023.

## Restricciones de diseño

- Interfaz sencilla para usuarios con distintos niveles de alfabetización digital.
- Considerar conectividad limitada y dispositivos de acceso variados.
- Respetar dinámicas comunitarias, participación, equidad y rendición de cuentas.
- No asumir que la organización funciona como una empresa corporativa tradicional.
- Confirmar mediante entrevistas las reglas reales de asistencia, producción, inventario,
  cobros y aprobación de cambios.

## Puntos que deben validarse

- El nombre visible confirmado para el sistema y la tesis es “Comité de Mujeres Indígenas
  Tránsito Amaguaña”; la denominación jurídica formal debe respaldarse con evidencia si se
  realiza una afirmación legal.
- El documento menciona “MVP” en una sección, aunque Django emplea habitualmente la
  arquitectura MTV; corregir la terminología académica si corresponde.
- Ventas y cuentas por cobrar forman parte del alcance inicial. D-010 confirmó el valor base fijo
  por producto, el excedente de la socia, los dos tipos de saldo y los pagos parciales; los detalles
  técnicos se definirán en las especificaciones.
- Variables de secado confirmadas: peso inicial, peso final y un valor de temperatura en grados
  Celsius; humedad opcional; inicio y fin con fecha y hora automáticas.
- Las correcciones de registros las realizarán solo la directiva y la encargada; se conservará
  historial con usuario, fecha/hora, valor anterior, valor nuevo y motivo.
- Los reportes prioritarios están confirmados; quedan para diseño los filtros, gráficos, PDFs y logo.
  No se incluirán afirmaciones ni reportes de cumplimiento sanitario.

## Plan oficial de desarrollo tomado del anteproyecto

El anteproyecto define estas fases y sprints. Este orden se conserva como referencia del
proyecto y no debe sustituirse por un orden inventado por el agente.

### Fase I - Levantamiento de requerimientos

- Revisión bibliográfica y documental.
- Visitas de campo y observación directa.
- Entrevistas semiestructuradas.
- Análisis y validación de requerimientos.
- Product Backlog inicial.

### Fase II - Diseño del sistema

- Diagramas UML.
- Arquitectura MTV/Django, usando la terminología correcta del framework.
- Modelo relacional PostgreSQL.
- Diseño de interfaces con Bootstrap 5 e interacción humano-máquina.

### Fase III - Desarrollo iterativo basado en Scrum

1. Sprint 1: administración y acceso, incluyendo RBAC.
2. Sprint 2: planificación de actividades.
3. Sprint 3: control de asistencia y participación.
4. Sprint 4: trazabilidad productiva.
5. Sprint 5: reportes y gestión de información.

### Fase IV - Evaluación

- Pruebas de adecuación funcional.
- Evaluación según ISO/IEC 25010:2023.
- Análisis descriptivo de resultados.

### Fase V - Documentación y entrega

- Manual técnico.
- Manual de usuario.
- Diccionario de datos.
- Capítulos finales.
- Revisión con la directora.
- Preparación de la defensa.

## Fuentes complementarias recibidas

Los archivos `Antecedentes.md`, `Definición del problema..md` y `Metodología.md` son
material de trabajo elaborado a partir de observaciones y análisis previos. Aportan
detalle útil, pero no sustituyen al anteproyecto ni a la validación con la organización.

- El problema general debe consolidarse en una sola versión.
- Los antecedentes de campo deben conservar su fuente y fecha de validación.
- La metodología debe separar investigación, desarrollo y evaluación.
- Los datos no presentes en el anteproyecto quedan como hipótesis o información pendiente
  de confirmar.
