---
title: Aceptación del alcance y plan de acceso multicanal
id: EVID-ACC-2026-10-28
type: decision-evidence
status: accepted-by-tesista
date: 2026-10-28
source: instrucción explícita del tesista en esta conversación
sprint: S2
commit: pending
organization_validation: pending
academic_review: pending
---

# Aceptación de acceso multicanal

## Decisión del tesista — 2026-10-28

El tesista aceptó el plan de acceso por passkeys y código por correo, con WhatsApp configurable, tras solicitar expresamente «con biometria y con correo, wpp se implementa». Su respuesta fue: «documentalo, me convence, recuerda cada cambio siempre documentar en requisitos, backlog, pilas, historias y http://127.0.0.1:55478/ que es el gestor de tesis agil».

La aceptación confirma este alcance y el plan por incrementos. No constituye validación de campo, revisión académica, implementación, autorización de gasto ni publicación. Telegram queda fuera del incremento elegido. El acceso usuario/contraseña existente se conserva como respaldo durante la transición.


## Alcance exacto

- Correo con código de seis dígitos; passkeys con WebAuthn; WhatsApp mediante Meta directa y mock.
- Cinco fases: seguridad común, correo, passkeys, WhatsApp y recuperación/verificación integral.
- El correo remitente de pruebas indicado por el tesista es `devkobaia@gmail.com`; los destinatarios son los contactos verificados de cada cuenta. No se proporcionó ni guardó una credencial SMTP.
- La activación real de WhatsApp queda condicionada a cuenta, número emisor, plantilla, consentimiento, comprobación de costo y prueba de entrega. No se contrata ni paga un proveedor con esta aceptación.
- La biometría se verifica en el dispositivo; la aplicación no recibe huellas, rostros ni claves privadas. El dispositivo puede utilizar PIN.
- No se añaden registro público de cuentas, nuevas autoridades organizacionales ni autenticación offline.

## Diferencias frente a la base anterior

SPEC-001 conserva el corte de acceso con contraseña. SPEC-003 añade los métodos y la recuperación y reemplaza, para el objetivo del nuevo incremento, la diferenciación pública de errores de cuenta/contraseña por respuestas genéricas. La implementación existente todavía conserva el comportamiento anterior; se debe adaptar y probar al ejecutar SB-S2-05 y SB-S2-09. No se reescribió una nota aprobada para simular un requisito anterior.

## Trazabilidad

RF-ACC-006 a RF-ACC-009 → SPEC-003 → HU-ACC-010 a HU-ACC-013 → HT-ACC-001/002 → SB-S2-05 a SB-S2-09. La aprobación se atribuye únicamente al tesista. Las reglas de recuperación asistida sin canales verificados, el máximo de envíos por hora y la selección/versionado de biblioteca WebAuthn se precisarán antes de activar los comportamientos dependientes.

## Fuentes técnicas consultadas

- https://web.dev/articles/passkey-registration
- https://web.dev/articles/webauthn-rp-id
- https://whatsappbusiness.com/developers/developer-hub/
- https://whatsappbusiness.com/products/platform-pricing/
- https://support.google.com/accounts/answer/185833?hl=es

Los precios son referencias del análisis, no cotizaciones ni garantías de gratuidad en producción.
