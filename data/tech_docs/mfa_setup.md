# Configuración de Autenticación Multifactor (MFA)

## ¿Por qué MFA?
MFA es obligatorio para todos los empleados y agrega una capa de seguridad crítica. Incluso si tu contraseña es comprometida, un atacante no puede acceder sin tu segundo factor.

## Configuración inicial con Duo
1. Descarga la app "Duo Mobile" en tu smartphone (iOS o Android).
2. Ve al IT Portal > Seguridad > Configurar MFA.
3. Escanea el código QR mostrado con la app Duo.
4. Confirma con un código de prueba. Listo.

## Métodos de verificación disponibles
- Push notification (recomendado): aprueba desde la app Duo.
- Código TOTP: usa el código de 6 dígitos que genera la app.
- SMS: solo como respaldo, no recomendado por seguridad.
- Llave de seguridad física (YubiKey): disponible bajo solicitud a IT para roles con acceso a datos sensibles.

## Cambio de teléfono
Si cambias de teléfono, primero instala Duo en el nuevo dispositivo y agrega la cuenta antes de borrar el teléfono anterior. Si ya borraste el anterior, contacta IT para hacer el re-enroll.

## MFA para aplicaciones sin soporte nativo
Para aplicaciones legacy que no soportan MFA, IT puede generar contraseñas de aplicación de un solo uso. Solicítalas en el IT Portal bajo "Contraseñas de aplicación".

## Problemas frecuentes
- "I need help" o no recibes el push: verifica que tengas conexión a internet y notificaciones habilitadas para Duo.
- Códigos incorrectos: asegúrate de que la hora de tu teléfono esté sincronizada automáticamente.
