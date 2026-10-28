---
title: Requisitos de seguridad de la aplicación
type: requirement-proposal
status: proposed
id: PRO-SEC-001
version: 0.2
created: 2026-10-20
updated: 2026-10-20
approval: pending
stack: Django 5.2, PostgreSQL, plantillas Bootstrap 5 y PWA
actors:
  - Directiva
  - Socia operaria
  - Visitante
  - Soporte técnico separado de permisos de negocio
protected_data:
  - Credenciales y sesiones
  - Datos personales y documentos
  - Asistencia y registros organizacionales
  - Producción, inventario y datos financieros
sources:
  - docs/requirements/CAT-REQ-001.md
  - specs/001-acceso-usuarias-internas/spec.md
confirmed_codes:
  - RF-ACC-001
  - RF-ACC-001.8
  - RF-ACC-003
  - RNF-SEC-001
  - RNF-PRV-001
  - RF-PWA-001
  - RF-PWA-002
  - RNF-DAT-001
  - RNF-AUD-001
proposed_codes:
  - RF-SEC-001
  - RNF-SEC-002
  - RNF-SEC-003
  - RNF-SEC-004
  - RNF-SEC-005
  - RNF-SEC-006
  - RNF-SEC-007
  - RNF-SEC-008
  - RNF-SEC-009
  - RNF-SEC-010
tags:
  - proyecto/tesis
  - tipo/requisito
  - estado/propuesto
---

# Requisitos de seguridad de la aplicación

## Autenticación/Sesiones

### Requisitos funcionales

#### RF-ACC-001

- **Redacción formal:** El sistema DEBE permitir que una usuaria interna con cuenta activa se autentique con su nombre de usuario y contraseña, rechazar credenciales inválidas o cuentas inactivas con una respuesta que no revele cuál condición falló, permitir el cambio autenticado de su contraseña y terminar la sesión cuando cierre sesión.
- **Criterio de verificación:** Probar credenciales válidas, contraseña incorrecta, usuario inexistente y cuenta inactiva. Las tres denegaciones deben producir respuestas equivalentes y no exponer contenido privado. Tras cerrar sesión, reutilizar la cookie y abrir una URL privada debe requerir autenticación. El cambio de contraseña debe rechazar una contraseña actual incorrecta y aceptar una nueva válida.
- **Implementación técnica recomendada:** Usar el sistema de autenticación de Django, formularios validados en servidor y los validadores y hashers de contraseña del framework. [Gestión de contraseñas en Django](https://docs.djangoproject.com/en/5.2/topics/auth/passwords/).

#### RF-ACC-001.8

- **Redacción formal:** El sistema DEBE dejar de permitir el acceso privado después de treinta minutos consecutivos sin actividad y solicitar una nueva autenticación.
- **Criterio de verificación:** Con una sesión activa, comprobar que una solicitud privada se permite antes del vencimiento y que, después de treinta minutos sin actividad, la siguiente solicitud exige autenticación y no devuelve contenido protegido.
- **Implementación técnica recomendada:** Configurar vencimiento por inactividad y renovación de las sesiones nativas de Django; probar el comportamiento con el backend de sesiones usado por PostgreSQL. [Sesiones de Django](https://docs.djangoproject.com/en/5.2/topics/http/sessions/) y [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).

### Requisitos no funcionales

#### RNF-SEC-002

- **Redacción formal:** El sistema DEBE limitar los intentos repetidos de autenticación fallida por cuenta y origen de solicitud, conforme a umbrales y periodos temporales aprobados, sin revelar la existencia ni el estado de una cuenta.
- **Criterio de verificación:** Con los umbrales de prueba configurados, superar el límite debe impedir o demorar nuevos intentos durante el periodo establecido y generar un evento de seguridad. Al finalizar el periodo, debe permitirse intentar nuevamente según la política aprobada.
- **Implementación técnica recomendada:** Aplicar limitación de frecuencia en el servidor o en un proxy confiable, con contadores temporales por cuenta y origen. Aprobar los umbrales antes de implementar. [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).

#### RNF-SEC-003

- **Redacción formal:** El sistema DEBE proteger las sesiones autenticadas mediante HTTPS y cookies con los atributos Secure, HttpOnly y SameSite, generar una nueva sesión al autenticar y revocarla al cerrar sesión o expirar.
- **Criterio de verificación:** En producción, comprobar HTTPS, los atributos de la cookie, la renovación del identificador al autenticar e imposibilidad de reutilizar una sesión cerrada o vencida.
- **Implementación técnica recomendada:** Configurar SecurityMiddleware, HTTPS y SESSION_COOKIE_SECURE, SESSION_COOKIE_HTTPONLY y SESSION_COOKIE_SAMESITE de Django. No guardar identificadores de sesión en almacenamiento accesible por JavaScript. [Seguridad en Django](https://docs.djangoproject.com/en/5.2/topics/security/) y [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).

## Control de Acceso

### Requisitos funcionales

#### RF-ACC-003

- **Redacción formal:** El sistema DEBE autorizar las operaciones internas según los perfiles organizacionales Directiva y Socia operaria, el perfil Visitante para contenido público y las asignaciones vigentes definidas en la matriz aprobada. El soporte técnico DEBE permanecer separado de la autoridad organizacional y de los permisos de negocio.
- **Criterio de verificación:** Para cada operación protegida, probar actores autorizados y denegados, solicitudes directas a URL y asignaciones vencidas. La denegación no debe modificar datos. Completar la verificación cuando se apruebe la matriz pendiente P-01.
- **Implementación técnica recomendada:** Aplicar permisos y grupos de Django con verificaciones en cada vista y operación del módulo propietario; restringir también los objetos consultados según actor y recurso. La visibilidad de controles en la interfaz no sustituye autorización en backend. [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

### Requisitos no funcionales

#### RNF-SEC-001

- **Redacción formal:** El sistema DEBE verificar en el servidor que cada operación sensible cuenta con autorización vigente, incluso ante una URL directa o una solicitud que omita la interfaz; una denegación DEBE dejar los datos sin cambios.
- **Criterio de verificación:** Mantener pruebas positivas y negativas para cada operación sensible, incluyendo acceso directo, objeto de otra usuaria y permiso vencido; comprobar que las denegaciones no producen mutaciones.
- **Implementación técnica recomendada:** Denegar por defecto y validar permisos en cada solicitud, tanto en las vistas como en los casos de uso. [OWASP Authorization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

## Protección de Datos

### Requisitos funcionales

#### RF-PWA-001

- **Redacción formal:** El sistema DEBE permitir que el Service Worker almacene localmente solo recursos esenciales y contenido expresamente público; las páginas, respuestas y datos privados no deben quedar disponibles desde cachés compartidas ni después de cerrar sesión.
- **Criterio de verificación:** Abrir una página privada, cerrar sesión, volver atrás, desconectar la red y solicitar directamente la página; no debe mostrarse contenido privado desde el navegador ni desde Cache Storage.
- **Implementación técnica recomendada:** Usar una lista explícita de recursos públicos en Cache Storage, excluir rutas privadas y devolver Cache-Control: no-store en respuestas con sesión o datos sensibles. [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).

#### RF-PWA-002

- **Redacción formal:** El sistema DEBE aislar por cuenta los registros pendientes guardados localmente e impedir que otra usuaria autenticada acceda a ellos.
- **Criterio de verificación:** Guardar un registro pendiente con una cuenta, cerrar sesión e iniciar otra cuenta en el mismo dispositivo. La segunda cuenta no debe poder consultarlo, modificarlo ni enviarlo.
- **Implementación técnica recomendada:** Guardar en IndexedDB solo los campos mínimos, asociar cada registro a su identidad y contexto de origen y filtrar por la cuenta autenticada. Aplicar la política de cierre, retención y descarte cuando se resuelva P-14.

### Requisitos no funcionales

#### RNF-PRV-001

- **Redacción formal:** El sistema DEBE recopilar solo los datos necesarios, separar contenido público de datos internos y restringir expedientes, justificativos y documentos personales a personas autorizadas. Cada clase documental DEBE tener responsables, conservación y retiro definidos antes de habilitar su almacenamiento.
- **Criterio de verificación:** Revisar formularios, pantallas, reportes, rutas de descarga y sitio público; comprobar que personas sin autorización no puedan consultar ni descargar datos personales u operativos.
- **Implementación técnica recomendada:** Minimizar los datos solicitados y consultados; mantener documentos fuera de directorios públicos y servirlos mediante vistas que comprueben autorización.

#### RNF-SEC-004

- **Redacción formal:** El sistema DEBE almacenar las contraseñas únicamente como verificadores criptográficos unidireccionales y mantener claves, credenciales de PostgreSQL y demás secretos fuera del código fuente, los registros y los artefactos versionados.
- **Criterio de verificación:** Inspeccionar cuentas de prueba, repositorio y registros; confirmar que no contienen contraseñas en texto claro, SECRET_KEY, credenciales de base de datos ni tokens.
- **Implementación técnica recomendada:** Usar set_password, check_password y hashers de Django; suministrar secretos mediante configuración protegida del entorno o un gestor de secretos y limitar los permisos de la cuenta PostgreSQL. [Gestión de contraseñas en Django](https://docs.djangoproject.com/en/5.2/topics/auth/passwords/), [lista de despliegue de Django](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/) y [OWASP Secrets Management](https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html).

#### RNF-SEC-005

- **Redacción formal:** El sistema DEBE proteger mediante cifrado el tráfico entre navegador y servidor y el almacenamiento persistente en producción de datos personales y organizacionales, manteniendo las claves protegidas y separadas de los datos cifrados.
- **Criterio de verificación:** Comprobar HTTPS con certificado válido y revisar la configuración de PostgreSQL y su almacenamiento para confirmar cifrado en reposo y acceso restringido a las claves.
- **Implementación técnica recomendada:** Usar TLS en el proxy y la aplicación; habilitar cifrado del volumen o servicio donde resida PostgreSQL. No implementar cifrado criptográfico propio en Django. [Seguridad en Django](https://docs.djangoproject.com/en/5.2/topics/security/) y [OWASP Cryptographic Storage](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html).

#### RNF-DAT-001

- **Redacción formal:** El sistema DEBE confirmar atómicamente los cambios que afecten varias entidades y derivar las existencias de movimientos registrados, sin permitir totales editables sin respaldo.
- **Criterio de verificación:** Forzar errores en puntos intermedios de una operación de varias entidades y comprobar que se revierte por completo, sin movimientos parciales, sobreventa ni saldo negativo silencioso.
- **Implementación técnica recomendada:** Usar transaction.atomic(), restricciones de base de datos e invariantes de dominio en el módulo propietario; aplicar control de concurrencia a operaciones que dependan de existencias o saldos.

## Validación/OWASP

### Requisitos no funcionales

#### RNF-SEC-006

- **Redacción formal:** El sistema DEBE exigir protección CSRF válida en toda solicitud autenticada que modifique el estado y no procesar mutaciones ante un token ausente o inválido.
- **Criterio de verificación:** Enviar solicitudes de modificación con token válido, ausente, inválido y de otro origen; solo la solicitud válida debe efectuar cambios.
- **Implementación técnica recomendada:** Mantener CsrfViewMiddleware, incluir csrf_token en formularios POST y evitar csrf_exempt salvo excepción revisada y documentada. [Protección CSRF en Django](https://docs.djangoproject.com/en/5.2/topics/security/) y [OWASP CSRF Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html).

#### RNF-SEC-007

- **Redacción formal:** El sistema DEBE validar en el servidor la sintaxis, el rango y la coherencia de cada dato recibido, parametrizar las consultas a PostgreSQL y codificar la salida según el contexto antes de mostrar datos no confiables.
- **Criterio de verificación:** Probar campos ausentes, tipos incorrectos, límites, valores no permitidos y entradas de prueba para SQL injection o XSS; la entrada inválida debe rechazarse sin mutaciones, errores internos ni ejecución de contenido en el navegador.
- **Implementación técnica recomendada:** Usar Django Forms, validadores de modelo, QuerySets del ORM y autoescape de plantillas; revisar todo uso de SQL crudo, mark_safe, safe o autoescape off. [Seguridad en Django](https://docs.djangoproject.com/en/5.2/topics/security/) y [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html).

#### RNF-SEC-008

- **Redacción formal:** Cuando se habilite la carga de archivos, el sistema DEBE aceptar solo formatos, tamaños y contenidos permitidos, almacenarlos fuera de rutas públicas y autorizar cada consulta o descarga según la cuenta y el recurso.
- **Criterio de verificación:** Probar formatos permitidos y rechazados, extensión que no coincide con el contenido, archivo que excede el límite, nombre manipulado y descarga por una cuenta no autorizada. Los rechazos no deben crear archivos accesibles.
- **Implementación técnica recomendada:** Definir listas permitidas y límites por clase documental, validar contenido y extensión, generar nombres internos, almacenar en destino privado y servir mediante una vista autorizada. [OWASP File Upload Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html).

#### RNF-SEC-009

- **Redacción formal:** El sistema DEBE aplicar una configuración de producción segura que desactive DEBUG, restrinja los hosts válidos, fuerce HTTPS y establezca cabeceras de protección compatibles con la interfaz.
- **Criterio de verificación:** Ejecutar manage.py check --deploy con la configuración de producción y resolver las advertencias de seguridad aplicables; verificar las cabeceras HTTP configuradas y el rechazo de hosts no autorizados.
- **Implementación técnica recomendada:** Configurar SecurityMiddleware, ALLOWED_HOSTS, redirección HTTPS, HSTS solo para dominios que ya operen exclusivamente por HTTPS, X-Content-Type-Options, protección contra framing y Referrer-Policy. [Lista de despliegue de Django](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/) y [System checks de Django](https://docs.djangoproject.com/en/5.2/ref/checks/).

## Auditoría/Logs

### Requisitos funcionales

#### RF-SEC-001

- **Redacción formal:** El sistema DEBE registrar los eventos de autenticación exitosa y fallida, cierre y vencimiento de sesión, denegaciones de autorización, cambios de cuenta o permisos y operaciones sensibles, con fecha, actor cuando sea conocido, tipo de evento, recurso y resultado.
- **Criterio de verificación:** Ejecutar cada evento contemplado y comprobar que existe un registro atribuible y cronológico, sin contraseñas, tokens, cookies de sesión ni datos personales innecesarios.
- **Implementación técnica recomendada:** Usar logging de Python/Django con eventos estructurados, redacción de campos sensibles, acceso restringido y una política de conservación aprobada. [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).

### Requisitos no funcionales

#### RNF-AUD-001

- **Redacción formal:** El sistema DEBE permitir reconstruir correcciones, aprobaciones y excepciones mediante el dato original, el cambio o reversión, el actor, la fecha, la autorización y el motivo.
- **Criterio de verificación:** Ejecutar una operación sensible autorizada y comprobar que el historial conserva los elementos requeridos y se confirma en la misma operación; ante un error, no debe quedar un cambio sin evidencia de auditoría.
- **Implementación técnica recomendada:** Mantener registros de auditoría propios del módulo, creados en la misma transacción Django que la operación, con lectura restringida a perfiles autorizados.

#### RNF-SEC-010

- **Redacción formal:** Los registros de seguridad y auditoría DEBEN protegerse contra lectura, modificación y eliminación por personas no autorizadas y excluir secretos, contraseñas, cookies, identificadores de sesión y cuerpos completos de solicitudes.
- **Criterio de verificación:** Probar permisos de consulta y modificación, revisar los eventos emitidos y confirmar que no contienen campos prohibidos ni entradas que alteren la estructura del registro.
- **Implementación técnica recomendada:** Separar permisos de lectura y escritura, sanitizar valores no confiables, correlacionar eventos sin guardar identificadores de sesión en claro y aplicar una política de conservación aprobada. [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html) y [OWASP Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html).
