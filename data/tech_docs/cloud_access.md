# Acceso a Recursos Cloud

## Proveedores cloud
La empresa utiliza AWS como proveedor principal y GCP de forma secundaria. El acceso se gestiona mediante roles IAM, nunca con credenciales de usuario root o de larga duración.

## Solicitar acceso a AWS
1. IT Portal > Solicitudes > Acceso Cloud > AWS.
2. Especifica: cuenta AWS, roles necesarios, propósito y duración.
3. Aprobación del gerente y del equipo de Cloud Security.
4. El acceso se otorga mediante AWS SSO con tu cuenta corporativa.

## Buenas prácticas de seguridad cloud
- Nunca crees recursos en la cuenta root.
- Todas las instancias EC2 deben tener etiquetas: Owner, Project, Environment.
- Desactiva cualquier recurso no utilizado para evitar costos innecesarios.
- Habilita CloudTrail y AWS Config en todos los entornos.

## Costos
Los gastos cloud son monitoreados semanalmente. Los equipos reciben alertas si superan el presupuesto asignado. Recursos no etiquetados correctamente pueden ser terminados automáticamente.

## Ambientes
Existen tres ambientes: dev (sandbox, costo limitado, menor restricción), staging (espejo de producción, datos anonimizados) y prod (máximas restricciones, cambios requieren change request aprobado).
