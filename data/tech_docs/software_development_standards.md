# Estándares de Desarrollo de Software

## Control de versiones
Todo el código debe estar en Git, alojado en la organización GitHub corporativa. No se permite código en drives locales sin respaldo en repositorio. Las ramas deben seguir la convención: feature/, bugfix/, hotfix/, release/.

## Code review
Toda rama debe pasar por Pull Request con al menos 1 aprobación antes de hacer merge a main. Los PR deben incluir: descripción del cambio, cómo probarlo, y si aplica, screenshots. El tamaño máximo recomendado de PR es 400 líneas de diferencia.

## Integración continua
Todos los repositorios activos deben tener un pipeline de CI que ejecute al menos: linting, tests unitarios y análisis estático de seguridad (SAST). Los pipelines fallidos bloquean el merge automáticamente.

## Gestión de secretos
Nunca guardes credenciales, API keys o secretos en el código o en variables de entorno visibles en logs. Usa el sistema de gestión de secretos corporativo (HashiCorp Vault o AWS Secrets Manager según el proyecto).

## Documentación
Cada repositorio debe tener un README actualizado con: descripción del proyecto, instrucciones de instalación y ejecución, arquitectura de alto nivel y contacto del equipo responsable.
