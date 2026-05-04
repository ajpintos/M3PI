# Configuración de VPN

## Descripción general
La empresa utiliza Cisco AnyConnect como cliente VPN. La VPN es obligatoria para acceder a sistemas internos (Jira, Confluence, servidores de desarrollo, repositorios privados) desde fuera de la red corporativa.

## Instalación en Windows
1. Descarga el instalador desde la intranet: IT Portal > Software > VPN > AnyConnect.
2. Ejecuta el instalador como administrador y sigue el asistente.
3. Al finalizar, busca "Cisco AnyConnect" en el menú de inicio.
4. En el campo "Connect to" ingresa: vpn.empresa.com
5. Usa tus credenciales de Active Directory (usuario y contraseña de Windows).

## Instalación en macOS
1. Descarga el paquete .dmg desde el IT Portal.
2. Abre el archivo y ejecuta el instalador.
3. Ve a Preferencias del Sistema > Seguridad y permite la extensión del sistema si se solicita.
4. Abre AnyConnect, ingresa vpn.empresa.com y autentícate con tus credenciales.

## Autenticación de dos factores
Después de ingresar tu contraseña, recibirás un push de Duo Security en tu teléfono. Debes aprobar la solicitud en menos de 60 segundos. Si no tienes la app de Duo configurada, contacta a IT Support.

## Problemas comunes
- "Unable to connect": verifica que tengas internet activo y que el servidor vpn.empresa.com sea correcto.
- La autenticación falla: asegúrate de que tu contraseña de Windows no haya expirado.
- Conexión lenta: desconéctate y reconéctate seleccionando el servidor regional más cercano.

## Soporte
Tickets de VPN: abre un caso en el IT Portal con categoría "VPN / Acceso Remoto". Tiempo de respuesta esperado: 4 horas hábiles.
