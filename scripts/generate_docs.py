"""
Genera documentos sintéticos realistas para las colecciones HR, Tech y Finance.
Idempotente: no sobreescribe archivos que ya existen.
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent / "data"

HR_DOCS = {
    "vacation_policy.md": """# Política de Vacaciones

## Días disponibles
Todo empleado de tiempo completo tiene derecho a 20 días hábiles de vacaciones anuales. Los empleados a tiempo parcial acumulan días de forma proporcional a su jornada laboral.

## Acumulación
Los días de vacaciones se acumulan mensualmente a razón de 1.67 días por mes trabajado. El saldo máximo acumulable es de 40 días. Los días que excedan este límite se perderán al cierre de cada año fiscal.

## Solicitud de vacaciones
Las vacaciones deben solicitarse con un mínimo de 5 días hábiles de antelación mediante el sistema de RRHH. Para ausencias de 10 o más días consecutivos, se requiere un mínimo de 15 días de anticipación y aprobación del gerente directo.

## Restricciones
No se permiten vacaciones durante los periodos de cierre financiero (últimas dos semanas de junio y diciembre). Durante picos operacionales identificados por la gerencia, las solicitudes pueden ser diferidas hasta 4 semanas.

## Vacaciones no tomadas
Los días no utilizados al final del año fiscal pueden trasladarse al siguiente año hasta un máximo de 10 días. Los días restantes se liquidan a valor de un día de salario bruto por día acumulado.
""",

    "parental_leave.md": """# Licencia por Maternidad y Paternidad

## Licencia de maternidad
Las empleadas que sean madres biológicas tienen derecho a 16 semanas de licencia remunerada al 100% del salario base. Este período comienza a más tardar una semana antes de la fecha estimada de parto y se extiende hasta completar las 16 semanas.

## Licencia de paternidad
Los empleados que sean padres biológicos o adoptivos tienen derecho a 4 semanas de licencia remunerada al 100% del salario base, tomadas dentro de los primeros 3 meses desde el nacimiento o adopción.

## Adopción
Tanto madres como padres adoptivos reciben la misma licencia que en el caso biológico. Se requiere documentación oficial del proceso de adopción.

## Extensión no remunerada
Cualquier empleado puede solicitar hasta 8 semanas adicionales de licencia no remunerada por maternidad o paternidad. Durante este período se mantiene la cobertura de seguro médico.

## Regreso al trabajo
La empresa garantiza el retorno al mismo puesto o uno equivalente. Se ofrece un plan de reinserción gradual: las primeras dos semanas de regreso el empleado puede trabajar a 80% de su jornada normal con remuneración completa.
""",

    "performance_reviews.md": """# Evaluaciones de Desempeño

## Frecuencia
Las evaluaciones formales de desempeño se realizan dos veces al año: en junio y en diciembre. Adicionalmente, cada trimestre se lleva a cabo una revisión informal entre el empleado y su gerente directo.

## Proceso de evaluación
Cada evaluación consta de tres etapas: autoevaluación del empleado, evaluación del gerente y calibración con RRHH. El proceso completo tiene una duración de 3 semanas. La autoevaluación debe completarse antes de que el gerente empiece su revisión.

## Criterios de evaluación
Los empleados son evaluados en cinco dimensiones: resultados (40%), competencias técnicas (25%), trabajo en equipo (15%), iniciativa (10%) e impacto en la cultura (10%). Cada dimensión se puntúa del 1 al 5.

## Escala de calificaciones
- 5: Excepcional — supera consistentemente las expectativas
- 4: Alto desempeño — supera las expectativas frecuentemente
- 3: Cumple expectativas — desempeño sólido y confiable
- 2: En desarrollo — cumple algunas expectativas, requiere mejora
- 1: Por debajo — no cumple expectativas mínimas

## Consecuencias
Calificaciones de 4 o 5 son elegibles para aumentos de mérito y promociones. Calificaciones de 2 activan un Plan de Mejora de Desempeño (PMP) de 90 días. Calificaciones de 1 pueden derivar en acciones disciplinarias o terminación.
""",

    "code_of_conduct.md": """# Código de Conducta

## Principios fundamentales
Todos los empleados deben actuar con integridad, respeto y profesionalismo. Esto incluye interacciones con colegas, clientes, proveedores y cualquier parte interesada. La empresa no tolera ninguna forma de discriminación, acoso o comportamiento intimidatorio.

## Discriminación y acoso
Está prohibida cualquier discriminación basada en raza, género, edad, orientación sexual, religión, discapacidad, origen nacional o cualquier otra característica protegida por la ley. El acoso sexual, ya sea verbal, físico o digital, es motivo de despido inmediato.

## Conflictos de interés
Los empleados deben evitar situaciones donde sus intereses personales puedan interferir con los de la empresa. Cualquier relación comercial con proveedores o clientes donde el empleado tenga un interés financiero debe ser divulgada a RRHH y aprobada por el Director Ejecutivo.

## Uso de recursos de la empresa
Los recursos de la empresa, incluyendo equipos, software, internet y tiempo de trabajo, deben usarse para propósitos laborales. El uso personal moderado del equipo de cómputo es tolerado siempre que no afecte la productividad ni exponga información confidencial.

## Reporte de infracciones
Los empleados pueden reportar violaciones al código de conducta de forma anónima a través del portal de ética en la intranet o contactando directamente al Director de RRHH. No se permiten represalias contra quienes reporten de buena fe.
""",

    "benefits_health.md": """# Beneficios de Salud

## Seguro médico
La empresa cubre el 80% de la prima del seguro médico para el empleado y el 60% para sus dependientes directos (cónyuge e hijos menores de 26 años). El empleado puede elegir entre dos planes: Plan Básico con deducible de $500/año o Plan Plus con deducible de $200/año.

## Seguro dental y visual
Se incluye cobertura dental que cubre limpieza semestral, radiografías anuales y hasta $1,500/año en procedimientos mayores. La cobertura visual incluye examen anual y hasta $300/año en lentes o lentes de contacto.

## Seguro de vida
Todos los empleados de tiempo completo cuentan con un seguro de vida equivalente a 2 veces su salario anual bruto, sin costo para el empleado. Es posible adquirir cobertura adicional de hasta 4 veces el salario anual a costo del empleado.

## Programa de bienestar
La empresa reembolsa hasta $500/año en membresías de gimnasio, aplicaciones de meditación o actividades deportivas debidamente documentadas. Se accede mediante solicitud de reembolso en el portal de RRHH adjuntando recibos.

## Asistencia psicológica
Todos los empleados tienen acceso a 12 sesiones anuales con psicólogo a través del Programa de Asistencia al Empleado (EAP), completamente confidenciales y sin costo. El acceso se gestiona llamando al número de línea de apoyo disponible en la intranet.
""",

    "remote_work.md": """# Política de Trabajo Remoto

## Modalidades disponibles
La empresa ofrece tres modalidades: presencial (5 días/semana en oficina), híbrida (mínimo 2 días/semana en oficina) y completamente remota (para roles elegibles aprobados por la dirección). La modalidad se define durante el proceso de contratación o mediante solicitud formal al gerente.

## Solicitud de trabajo remoto
Los empleados con más de 6 meses en la empresa pueden solicitar cambio de modalidad. La solicitud debe hacerse por escrito al gerente directo y RRHH. La aprobación depende del rol, historial de desempeño y necesidades del equipo.

## Equipamiento
La empresa proporciona laptop, monitor secundario y auriculares a empleados remotos e híbridos. Una vez al año, se puede solicitar una revisión del equipamiento. El empleado es responsable de mantener el equipo en buen estado y reportar daños.

## Conectividad
Los empleados remotos reciben un subsidio mensual de $50 para Internet. Este se paga con la nómina mensual y no requiere justificación de gastos. No se reembolsa el costo de espacios de coworking salvo autorización expresa del gerente.

## Disponibilidad
Los empleados remotos deben estar disponibles durante el horario laboral establecido (9:00-18:00 hora local) y responder a comunicaciones en un plazo máximo de 2 horas durante este período. Se espera participación en todas las reuniones de equipo, ya sea con cámara encendida o justificación previa.
""",

    "onboarding.md": """# Proceso de Onboarding

## Antes del primer día
RRHH envía al nuevo empleado un correo de bienvenida con credenciales temporales, guía de preparación y agenda de la primera semana. El equipo de IT prepara el equipo de cómputo y accesos a sistemas con al menos 48 horas de anticipación.

## Primera semana
El primer día comienza con una reunión de orientación con RRHH de 3 horas donde se cubren políticas, beneficios y cultura. Los días 2 al 5 son de onboarding técnico con el equipo, incluyendo sesiones con cada área funcional con la que el nuevo empleado interactuará.

## Primeros 30 días
El empleado y su gerente establecen objetivos para los primeros 90 días (plan 30-60-90). Se asigna un buddy de onboarding: un colega experimentado que sirve de guía informal durante los primeros 3 meses.

## Primeros 90 días
Al completar 90 días, se realiza una revisión formal de onboarding entre el empleado, el gerente y RRHH. Esta revisión evalúa si el empleado tiene todo lo necesario para tener éxito y ajusta el plan de desarrollo si es necesario.

## Recursos disponibles
Todos los materiales de onboarding, incluyendo guías, políticas y videos de capacitación, están disponibles en la intranet bajo la sección "Nuevo en la empresa". El portal se actualiza trimestralmente.
""",

    "compensation_structure.md": """# Estructura de Compensación

## Bandas salariales
La empresa opera con bandas salariales por nivel y función. Cada banda tiene un rango con punto mínimo, punto medio (midpoint) y punto máximo. Los salarios de nuevas contrataciones típicamente se ubican entre el 90% y el 105% del midpoint según experiencia.

## Revisiones salariales
Las revisiones de mérito ocurren una vez al año en enero, basadas en la evaluación de desempeño de diciembre. El presupuesto general de mérito se comunica en noviembre. Empleados con calificación de 3 reciben entre 2-3%, calificación 4 entre 4-6%, calificación 5 entre 7-10%.

## Bonos
El bono anual se calcula como porcentaje del salario base y depende del logro de objetivos individuales (60%) y resultados de la empresa (40%). Los objetivos individuales se definen en enero y se revisan semestralmente. El pago del bono se realiza en febrero del año siguiente.

## Equity / Opciones sobre acciones
Los empleados de nivel Senior en adelante reciben un paquete de opciones sobre acciones (stock options) con un vesting de 4 años y un cliff de 1 año. Los detalles del paquete se especifican en la carta de oferta.

## Políticas de equidad salarial
La empresa realiza auditorías anuales de equidad salarial para detectar y corregir brechas de género o diversidad. Los resultados se comparten con el equipo directivo y se toman acciones correctivas dentro del siguiente ciclo de revisión.
""",

    "disciplinary_process.md": """# Proceso Disciplinario

## Principios
El proceso disciplinario busca ser justo, consistente y orientado a la corrección del comportamiento. Antes de escalar cualquier medida, se busca agotar instancias de retroalimentación y apoyo.

## Niveles de acción disciplinaria
1. Conversación informal: el gerente aborda el problema directamente con el empleado. No queda registro formal.
2. Advertencia verbal formal: se documenta en el expediente del empleado con descripción del problema, expectativas y plazo de mejora.
3. Advertencia escrita: documento formal firmado por el empleado, el gerente y RRHH. Puede incluir un Plan de Mejora.
4. Suspensión sin pago: hasta 5 días hábiles, aplicable en casos de infracciones graves.
5. Terminación de la relación laboral: decisión tomada por el gerente y RRHH con revisión legal.

## Faltas graves
Las siguientes conductas pueden derivar en terminación inmediata sin necesidad de seguir los pasos anteriores: robo, violencia física, acoso sexual, divulgación de información confidencial, falsificación de documentos o fraude.

## Derecho a ser escuchado
En toda instancia formal, el empleado tiene derecho a presentar su versión de los hechos antes de que se tome una decisión. Puede ser acompañado por un representante de RRHH o un colega de confianza.
""",

    "time_tracking.md": """# Control de Horas y Asistencia

## Registro de horas
Todos los empleados deben registrar su entrada y salida diaria en el sistema de control de asistencia (disponible en la app móvil y en los terminales de las oficinas). Los empleados remotos registran su asistencia en el sistema interno en línea.

## Horas extras
Las horas trabajadas más allá de la jornada estándar (8 horas/día o 40 horas/semana) se consideran horas extras. Deben ser pre-aprobadas por el gerente directo. Se compensan a 1.5x el valor hora para las primeras 2 horas extras diarias y a 2x para las horas adicionales.

## Ausencias y tardanzas
Tres tardanzas de más de 15 minutos en un mes generan una advertencia informal. Las ausencias no justificadas se descuentan del salario y se registran en el expediente. Las ausencias justificadas (enfermedad, cita médica) requieren documentación entregada dentro de las 48 horas de la ausencia.

## Licencias especiales
La empresa otorga 3 días pagados por fallecimiento de familiar directo (padres, hijos, cónyuge), 1 día por fallecimiento de familiar en segundo grado, y hasta 5 días por mudanza nacional documentada.

## Días festivos
Los empleados tienen libre en todos los días festivos oficiales del país más 2 días flotantes al año que pueden tomarse en cualquier fecha con aprobación del gerente.
""",

    "training_development.md": """# Capacitación y Desarrollo Profesional

## Presupuesto de desarrollo
Cada empleado dispone de un presupuesto anual de $1,200 para capacitación y desarrollo profesional. Este puede utilizarse en cursos en línea, conferencias, certificaciones o libros técnicos. No es acumulable entre años.

## Plataformas disponibles
La empresa tiene licencias corporativas en Coursera, LinkedIn Learning y Pluralsight. Todos los empleados tienen acceso ilimitado sin cargo a su presupuesto individual. Los accesos se gestionan a través de RRHH.

## Certificaciones
La empresa reembolsa el 100% del costo de exámenes de certificación relevantes para el rol, previa aprobación del gerente. Si el empleado aprueba la certificación, recibe un bono único equivalente a un mes de salario de nivel junior. Si reprueba, puede repetir con 50% de reembolso.

## Plan de carrera
Cada empleado tiene un plan de desarrollo individual (PDI) actualizado semestralmente en conjunto con su gerente. El PDI incluye habilidades a desarrollar, experiencias deseadas, mentores asignados y criterios para la siguiente promoción.

## Programas internos
La empresa ofrece programas de mentoría, grupos de aprendizaje (learning guilds) y un programa de rotación interdepartamental de 3 meses para empleados con más de 2 años de antigüedad.
""",

    "expense_reimbursement_hr.md": """# Política de Reembolso de Gastos (RRHH)

## Gastos elegibles para reembolso
Los gastos de trabajo aprobados incluyen: viajes de negocios (vuelos, hotel, transporte), comidas con clientes o candidatos, materiales de capacitación, equipamiento de oficina en casa (hasta $500/año) y membresías profesionales aprobadas.

## Proceso de solicitud
Los reembolsos se solicitan a través del módulo de gastos en el portal de empleados. Deben adjuntarse los comprobantes originales. Las solicitudes deben presentarse dentro de los 30 días posteriores al gasto.

## Tiempos de pago
Los reembolsos aprobados se procesan en el ciclo de nómina más próximo. El departamento de Finanzas tiene hasta 15 días hábiles para aprobar o rechazar una solicitud. Si hay información faltante, se notifica al empleado para que la corrija dentro de 5 días hábiles.

## Límites
Las comidas de trabajo tienen un límite de $75 por persona. Los hoteles en ciudades principales tienen un límite de $200/noche. Los vuelos deben ser en clase económica salvo trayectos de más de 8 horas. Gastos fuera de límites requieren aprobación previa del Director de Finanzas.
""",

    "workplace_safety.md": """# Seguridad en el Lugar de Trabajo

## Responsabilidades
La empresa es responsable de proveer un ambiente de trabajo seguro y en cumplimiento con la normativa vigente. Cada empleado es responsable de seguir los protocolos de seguridad, reportar condiciones inseguras y participar en las capacitaciones obligatorias.

## Emergencias
En caso de evacuación, todos los empleados deben dirigirse a la zona de reunión designada en el estacionamiento principal. Los coordinadores de piso se identifican con chaleco naranja y son responsables de verificar que nadie quede en el edificio.

## Ergonomía
La empresa realiza evaluaciones ergonómicas a solicitud del empleado. Se puede solicitar silla ajustable, soporte lumbar, reposamuñecas o escritorio de altura variable a través de RRHH, con aprobación del médico laboral en casos de necesidad documentada.

## Incidentes y accidentes
Todo accidente de trabajo, incluso menor, debe reportarse al supervisor inmediato y a RRHH dentro de las 24 horas. La empresa cubre los gastos médicos derivados de accidentes laborales. El no reportar un accidente puede afectar el proceso de reclamación.
""",

    "equal_opportunity.md": """# Igualdad de Oportunidades

## Declaración de principios
La empresa es un empleador que ofrece igualdad de oportunidades. Todas las decisiones de contratación, promoción, compensación y desarrollo se toman en base al mérito, habilidades y resultados, sin discriminación por ningún motivo.

## Proceso de selección
Las vacantes se publican internamente durante al menos 5 días antes de abrir a candidatos externos. Los procesos de selección están estandarizados con entrevistas estructuradas y rúbricas de evaluación para minimizar sesgos. Al menos uno de los entrevistadores debe haber completado el curso de contratación inclusiva.

## Ajustes razonables
La empresa provee ajustes razonables para empleados con discapacidades, tanto en el proceso de selección como en el trabajo diario. Los empleados pueden solicitar ajustes a RRHH de forma confidencial.

## Comité de diversidad e inclusión
Existe un comité de D&I con representantes de todas las áreas que se reúne mensualmente. Sus recomendaciones son presentadas a la dirección trimestralmente. Cualquier empleado puede unirse al comité voluntariamente.
""",
}

TECH_DOCS = {
    "vpn_setup.md": """# Configuración de VPN

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
""",

    "password_reset.md": """# Restablecimiento de Contraseña

## Autoservicio (recomendado)
Si olvidaste tu contraseña de Active Directory, puedes restablecerla sin contactar a IT:
1. Ve a https://aka.empresa.com/reset
2. Ingresa tu correo corporativo.
3. Verifica tu identidad mediante el código enviado a tu teléfono personal registrado.
4. Elige una nueva contraseña que cumpla los requisitos de seguridad.

## Requisitos de contraseña
La nueva contraseña debe: tener al menos 12 caracteres, incluir mayúsculas y minúsculas, al menos un número y un símbolo especial. No puede contener tu nombre, usuario o las últimas 10 contraseñas utilizadas.

## Contraseñas de sistemas específicos
Para restablecer contraseñas de sistemas como Salesforce, Jira o el ERP, usa el enlace "Forgot password" en cada plataforma. Si el sistema usa SSO (Single Sign-On), restablece la contraseña principal de Active Directory y el acceso se actualizará automáticamente.

## Si estás bloqueado
Después de 5 intentos fallidos tu cuenta se bloquea por 30 minutos automáticamente. Si necesitas acceso inmediato, contacta a IT Support por teléfono al ext. 4100 o por WhatsApp corporativo (solo emergencias).

## Expiración de contraseñas
Las contraseñas de Active Directory expiran cada 90 días. Recibirás notificaciones en Windows con 14, 7 y 3 días de anticipación. Es crítico no ignorar estas alertas ya que la expiración puede bloquear el acceso a todos los sistemas.
""",

    "mfa_setup.md": """# Configuración de Autenticación Multifactor (MFA)

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
""",

    "software_requests.md": """# Solicitud de Software

## Software aprobado
Existe un catálogo de software corporativo aprobado disponible en el IT Portal > Catálogo de Software. Este software puede instalarse sin aprobación adicional utilizando el Centro de Software disponible en tu equipo.

## Solicitud de software no catalogado
1. Accede al IT Portal > Solicitudes > Nuevo Software.
2. Completa el formulario: nombre del software, versión, propósito de uso, costo estimado y si requiere licencia.
3. La solicitud pasa por revisión de seguridad (5 días hábiles) y aprobación del gerente.
4. Si es aprobado, IT lo instala de forma remota o te proporciona el instalador.

## Software de código abierto
El software open source de uso profesional puede instalarse previa revisión de la licencia. Licencias MIT, Apache 2.0 y BSD son generalmente aceptadas. Licencias GPL requieren revisión legal antes de ser aprobadas.

## Actualizaciones
Las actualizaciones de seguridad críticas se instalan automáticamente fuera del horario laboral. Las actualizaciones de versión mayor requieren aprobación del usuario. Nunca posponer las actualizaciones de seguridad más de 48 horas.

## Software personal en equipos corporativos
Instalar software personal no aprobado en equipos de la empresa está prohibido y puede derivar en acciones disciplinarias. Los equipos son monitoreados por IT para garantizar el cumplimiento de esta política.
""",

    "incident_response.md": """# Respuesta a Incidentes de Seguridad

## Qué es un incidente
Un incidente de seguridad es cualquier evento que comprometa o pueda comprometer la confidencialidad, integridad o disponibilidad de datos o sistemas. Ejemplos: correo de phishing recibido, laptop perdida, acceso no autorizado detectado, malware.

## Reportar un incidente
Inmediatamente reporta cualquier incidente sospechoso a:
- Correo: security@empresa.com
- Teléfono emergencias IT: ext. 4911
- IT Portal > Incidentes > Nuevo incidente de seguridad

No intentes resolver el incidente por tu cuenta. No apagues el equipo afectado a menos que IT lo indique.

## Clasificación de severidad
- Crítico: acceso a datos de clientes, ransomware activo, credenciales comprometidas de administrador.
- Alto: equipo con malware, acceso no autorizado a sistemas internos.
- Medio: phishing sin clic, dispositivo perdido sin datos sensibles.
- Bajo: spam, intento fallido de acceso.

## Proceso de respuesta
IT Security tiene 15 minutos para responder a incidentes críticos, 2 horas para altos. Se asigna un incident manager que coordina la respuesta, comunicaciones y documentación post-incidente.

## Después del incidente
Se elabora un informe post-mortem con análisis de causa raíz y acciones preventivas. Los incidentes críticos se comunican a la dirección dentro de las 24 horas. Se revisan los controles para prevenir recurrencia.
""",

    "github_access.md": """# Acceso a GitHub Corporativo

## Organización en GitHub
La empresa utiliza la organización privada github.com/empresa-corp. Todos los repositorios de código fuente, infraestructura como código y documentación técnica están alojados aquí.

## Solicitar acceso
1. IT Portal > Solicitudes > Acceso a Sistemas > GitHub.
2. Selecciona los repositorios o equipos que necesitas.
3. El gerente aprueba y el equipo de DevOps procesa la solicitud en 1 día hábil.
4. Recibirás una invitación al correo corporativo para unirte a la organización.

## Políticas de uso
- Nunca subas código con secretos, contraseñas, API keys o datos de clientes.
- Todos los repositorios de producción requieren protección de rama main/master (no push directo).
- Las Pull Requests deben tener al menos 1 aprobación antes de hacer merge.
- Usa commits semánticos: feat:, fix:, docs:, refactor:, etc.

## Autenticación
Usa SSH o tokens de acceso personal (PAT) para autenticarte. Nunca uses tu contraseña de Active Directory en GitHub. Los PAT deben tener expiración máxima de 90 días y alcance mínimo necesario.

## Salida de la empresa
Al terminar la relación laboral, el acceso a GitHub se revoca el último día de trabajo. Es responsabilidad del empleado no llevarse código propietario.
""",

    "laptop_setup.md": """# Configuración de Laptop Corporativa

## Entrega inicial
Las laptops se entregan con Windows 11 Pro o macOS (según el rol) preconfigurado con: cliente de dominio/MDM, VPN, antivirus, herramientas de cifrado de disco y el catálogo de software estándar.

## Primer inicio
1. Conecta la laptop a la red corporativa (Wi-Fi corporativo o cable Ethernet).
2. Inicia sesión con tu usuario y contraseña de Active Directory.
3. El sistema descargará automáticamente las políticas y configuraciones durante los primeros 30 minutos.
4. Reinicia cuando se solicite.

## Cifrado de disco
Todos los discos corporativos deben estar cifrados: BitLocker en Windows, FileVault en Mac. La clave de recuperación se guarda en el directorio corporativo automáticamente. Si pierdes acceso, contacta IT con tu ID de empleado.

## Cuidado del equipo
El empleado es responsable de cuidar el equipo. Los daños por descuido pueden ser cobrados parcialmente al empleado según política de activos. Reporta cualquier daño físico a IT inmediatamente, incluso si el equipo sigue funcionando.

## Devolución
Al término de la relación laboral o al recibir un equipo de reemplazo, el equipo debe devolverse a IT en las primeras 48 horas. IT realiza un borrado certificado del equipo antes de reasignarlo.
""",

    "it_support_channels.md": """# Canales de Soporte de IT

## IT Portal (principal)
Accede a https://itportal.empresa.com para: abrir tickets de soporte, solicitar accesos, descargar software aprobado, consultar el estado de tus tickets y acceder a la base de conocimiento.

## Chat en vivo
Disponible en horario hábil (8:00-18:00) a través del IT Portal o el canal #it-help en Slack. Ideal para consultas rápidas o cuando necesitas guía en tiempo real.

## Teléfono
Extensión interna 4100. Para urgencias fuera de horario: +1-555-IT-HELP. Solo para incidentes que impiden trabajar completamente.

## Soporte presencial
Mesa de ayuda física en la planta baja del edificio A, disponible de lunes a viernes de 9:00 a 17:00. Sin cita previa para problemas de hardware.

## Tiempos de respuesta (SLA)
- Crítico (sistema caído, no puedes trabajar): 1 hora hábil.
- Alto (funcionalidad importante afectada): 4 horas hábiles.
- Medio (problema con workaround disponible): 1 día hábil.
- Bajo (consulta, solicitud de mejora): 3 días hábiles.

## Buenas prácticas al abrir un ticket
Incluye siempre: descripción detallada del problema, pasos para reproducirlo, capturas de pantalla si aplica, y el ID de tu equipo (visible en la etiqueta inferior de la laptop).
""",

    "data_backup.md": """# Respaldo de Datos

## Qué se respalda automáticamente
Todos los archivos guardados en OneDrive o en drives de red corporativos (\\\\fileserver) se respaldan automáticamente cada 24 horas con retención de 90 días. Los archivos borrados pueden recuperarse en el portal de OneDrive o mediante un ticket a IT.

## Qué NO se respalda
Los archivos guardados únicamente en el escritorio o en la carpeta de Descargas de tu laptop NO se respaldan. Si tu laptop falla, esos archivos se perderían. Siempre guarda trabajo importante en OneDrive o en un drive compartido.

## Recuperación de archivos
Para recuperar versiones anteriores de archivos: clic derecho sobre el archivo en OneDrive > "Historial de versiones". Para archivos borrados: papelera de reciclaje de OneDrive (disponible hasta 90 días después). Para recuperaciones masivas o fuera del portal: abre un ticket a IT.

## Respaldo de bases de datos
Los respaldos de bases de datos de producción se realizan cada hora con retención de 30 días para puntos horarios, 90 días para respaldos diarios, y 1 año para respaldos mensuales. Las pruebas de restauración se ejecutan mensualmente.

## Dispositivos externos
El uso de USB y discos duros externos en equipos corporativos está restringido. Solo dispositivos aprobados y cifrados pueden conectarse. Los dispositivos no aprobados serán bloqueados automáticamente por el sistema de endpoint protection.
""",

    "network_access.md": """# Acceso a la Red

## Redes Wi-Fi disponibles
- **CorpWifi**: red principal para empleados, requiere autenticación con credenciales corporativas. Acceso completo a recursos internos.
- **CorpGuest**: red para visitantes y dispositivos personales. Solo acceso a internet, sin acceso a sistemas internos.
- **CorpMDM**: red exclusiva para dispositivos móviles gestionados por MDM.

## Acceso desde casa (VPN)
Toda conexión remota a sistemas internos debe realizarse a través de VPN. Ver guía de configuración de VPN para instrucciones detalladas.

## Puertos y protocolos bloqueados
Por políticas de seguridad, los siguientes puertos están bloqueados en la red corporativa: torrents, IRC, RDP (salvo a servidores autorizados). El tráfico web es inspeccionado mediante proxy. Los sitios bloqueados incluyen: pornografía, apuestas, y sitios de malware conocido.

## Dispositivos personales en red corporativa
Los dispositivos personales no pueden conectarse a CorpWifi. Deben usar CorpGuest. Conectar un dispositivo personal a CorpWifi es una violación de seguridad y puede resultar en acción disciplinaria.

## Problemas de conectividad
Para problemas de red: verifica físicamente el cable Ethernet o si el punto de acceso Wi-Fi tiene la luz indicadora correcta, reinicia el adaptador de red, y si persiste, abre un ticket de IT con tu ubicación exacta y el nombre de la red a la que intentas conectarte.
""",

    "software_development_standards.md": """# Estándares de Desarrollo de Software

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
""",

    "cloud_access.md": """# Acceso a Recursos Cloud

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
""",

    "printing_scanning.md": """# Impresoras y Escáneres

## Impresoras disponibles
Cada planta tiene al menos dos impresoras multifunción HP Enterprise. Los modelos disponibles por planta están listados en el IT Portal > Inventario > Impresoras. Las impresoras corporativas soportan impresión segura (el trabajo espera hasta que el usuario se autentique en la impresora).

## Instalación de impresora en Windows
1. Ve a Configuración > Impresoras y escáneres.
2. Haz clic en "Agregar impresora".
3. El sistema detectará automáticamente las impresoras de red disponibles.
4. Si no aparece la impresora, ve al IT Portal y descarga el driver correspondiente.

## Impresión segura
Para documentos confidenciales, usa la opción "Secure Print" en el diálogo de impresión. Ingresa un PIN de 4 dígitos. Ve a la impresora, selecciona tu trabajo en la pantalla e ingresa el PIN. El trabajo se borra si no se recoge en 4 horas.

## Escaneo
Todas las impresoras multifunción tienen función de escaneo a email y a OneDrive. Coloca el documento, selecciona "Scan" en la pantalla de la impresora, elige el destino y autentícate con tu usuario corporativo.

## Problemas comunes
- Papel atascado: sigue las instrucciones en la pantalla de la impresora. Si no puedes resolverlo, llama a IT.
- Cartucho vacío: reporta en IT Portal > Solicitudes > Consumibles > Cartuchos.
""",

    "endpoint_security.md": """# Seguridad de Endpoints

## Antivirus y EDR
Todos los equipos corporativos tienen instalado CrowdStrike Falcon, que provee antivirus de nueva generación y detección y respuesta en endpoints (EDR). Este software no puede desinstalarse ni desactivarse.

## Escaneos automáticos
Los escaneos de seguridad se ejecutan automáticamente fuera del horario laboral. Si se detecta una amenaza, el equipo puede ser aislado automáticamente de la red hasta que IT lo inspeccione. Recibirás una notificación y deberás contactar a IT Security.

## Parches y actualizaciones
Las actualizaciones de seguridad del sistema operativo se instalan automáticamente. El equipo solicitará un reinicio; debes hacerlo dentro de las 48 horas para evitar una actualización forzada. Las actualizaciones de aplicaciones se gestionan mediante el Centro de Software.

## USB y medios externos
El uso de USB está restringido por política de DLP (Data Loss Prevention). Solo dispositivos USB aprobados y registrados en IT funcionarán en los equipos. Los intentos de conectar un USB no autorizado generan una alerta en IT Security.

## Pérdida o robo de equipo
Reporta inmediatamente (dentro de 1 hora) la pérdida o robo de un equipo corporativo al número de emergencias de IT y al gerente. IT puede activar borrado remoto del equipo. La demora en reportar puede resultar en responsabilidad por los datos expuestos.
""",
}

FINANCE_DOCS = {
    "expense_policy.md": """# Política de Gastos Corporativos

## Principios generales
Todos los gastos de la empresa deben ser necesarios para el negocio, razonables en monto y apropiadamente documentados. El empleado que genera el gasto es responsable de cumplir esta política y de obtener las aprobaciones necesarias antes de incurrir en gastos significativos.

## Límites por categoría
- Comidas de trabajo: $75 por persona (almuerzo), $150 por persona (cena con cliente).
- Transporte local: Uber/taxi razonable; no se reembolsan viajes de más de $100 sin justificación.
- Hotel: $200/noche en ciudades principales, $150 en ciudades secundarias.
- Vuelos: clase económica para trayectos menores a 8 horas; business permitido para trayectos mayores.
- Entretenimiento de clientes: requiere aprobación previa del VP del área y no puede superar $500 por evento.

## Gastos no elegibles
No se reembolsan: bebidas alcohólicas (salvo eventos corporativos aprobados), minibar, servicio a cuarto, cargos por llegada tardía al hotel, multas de tráfico, gastos de cónyuge/familia salvo autorización explícita del CEO.

## Proceso de solicitud
Ingresa los gastos en el sistema de gestión de gastos (Concur) dentro de los 30 días de realizados. Adjunta los comprobantes originales. Gastos sin comprobante no serán reembolsados salvo propinas de hasta $20.

## Aprobación
Los gastos bajo $500 son aprobados por el gerente directo. Entre $500 y $2,000 requieren aprobación del Director del área. Sobre $2,000 requieren aprobación del CFO.
""",

    "reimbursement_process.md": """# Proceso de Reembolso de Gastos

## Pasos para solicitar un reembolso
1. Reúne todos los comprobantes originales (facturas, recibos).
2. Ingresa al sistema Concur en https://concur.empresa.com con tus credenciales corporativas.
3. Crea un nuevo informe de gastos con nombre descriptivo (ej: "Viaje Cliente NYC - Marzo 2025").
4. Agrega cada gasto individualmente con fecha, categoría, monto y descripción del propósito de negocio.
5. Adjunta las fotos o PDFs de los comprobantes.
6. Envía el informe a tu gerente para aprobación.

## Plazo de presentación
Los gastos deben reportarse dentro de los 30 días de realizados. Gastos presentados después de 60 días no serán reembolsados salvo autorización excepcional del CFO. Los gastos de diciembre deben presentarse antes del 20 de diciembre para ser procesados en el año fiscal corriente.

## Tiempos de pago
Una vez aprobado por el gerente, el pago se procesa en el siguiente ciclo de nómina. El ciclo de nómina cierra los días 15 y último de cada mes. El pago se realiza por transferencia bancaria a la cuenta registrada en el sistema de RRHH.

## Gastos en moneda extranjera
Ingresa el monto en la moneda local de la transacción. Concur convertirá automáticamente usando el tipo de cambio del día del gasto según el proveedor de datos financieros. No se aceptan conversiones manuales del empleado.

## Rechazo de gastos
Si un gasto es rechazado, recibirás una notificación con el motivo. Puedes corregir y re-someter dentro de los 15 días. Después de dos rechazos, el gasto requiere escalación al Director de Finanzas.
""",

    "corporate_card.md": """# Tarjeta Corporativa

## Quién puede tener tarjeta
Las tarjetas corporativas VISA Empresa se asignan a empleados que viajan frecuentemente o tienen necesidades de gasto regular aprobadas por el Director Financiero. Los gerentes pueden solicitar una tarjeta para un empleado a través del IT Portal > Finanzas > Solicitud de Tarjeta Corporativa.

## Límites de la tarjeta
- Tarjeta estándar: $3,000/mes.
- Tarjeta gerencial: $10,000/mes.
- Tarjeta ejecutiva: $25,000/mes.
Los límites pueden incrementarse temporalmente para proyectos o eventos específicos mediante solicitud aprobada.

## Uso correcto
La tarjeta corporativa es exclusiva para gastos de negocio aprobados. Nunca la uses para gastos personales. Cada transacción debe ser registrada en Concur dentro de los 7 días de realizada. Las transacciones no conciliadas al cierre de mes generan alertas automáticas.

## Transacciones sospechosas
Si detectas una transacción que no reconoces en tu tarjeta corporativa, repórtala inmediatamente a treasury@empresa.com y al banco emisor al número al reverso de la tarjeta. La tarjeta puede ser bloqueada temporalmente mientras se investiga.

## Pérdida o robo
Reporta inmediatamente la pérdida o robo llamando al número de emergencias del banco emisor (al reverso de la tarjeta) y notifica a treasury@empresa.com. La tarjeta se cancela y emite una de reemplazo en 3-5 días hábiles.
""",

    "invoicing.md": """# Proceso de Facturación a Clientes

## Responsabilidades
El equipo de Account Management es responsable de generar las facturas según los contratos vigentes. El equipo de Finanzas las revisa, aprueba y envía al cliente. Las disputas de facturación se escalan a Account Management para resolución.

## Ciclo de facturación
La mayoría de los clientes son facturados mensualmente los primeros 5 días del mes por el período vencido. Los clientes con contrato anual reciben una factura única al inicio del período (o al renovar). Clientes con condiciones especiales se gestionan según lo acordado en el contrato.

## Generación de facturas
Las facturas se generan automáticamente desde el sistema ERP basadas en los contratos activos. Variaciones de consumo (usuarios adicionales, módulos, servicios profesionales) deben ser ingresadas por Account Management antes del día 28 del mes.

## Términos de pago estándar
El plazo de pago estándar es Net 30 (30 días desde la fecha de la factura). Clientes enterprise pueden negociar Net 45 o Net 60 con aprobación del CFO. Los pagos tardíos generan intereses del 1.5% mensual sobre el saldo vencido.

## Disputas
Si un cliente disputa una factura, Account Management tiene 5 días hábiles para investigar y responder. Si la disputa es válida, se emite una nota de crédito. Si es inválida, se documenta la decisión y se solicita el pago al cliente.

## Facturas internacionales
Las facturas en moneda extranjera se emiten en la moneda del contrato. El tipo de cambio se fija al inicio del contrato y se revisa anualmente. Los impuestos locales son responsabilidad del cliente según las leyes de su jurisdicción.
""",

    "travel_budget.md": """# Presupuesto y Gestión de Viajes

## Aprobación previa de viajes
Todo viaje de negocios requiere aprobación previa del gerente directo antes de reservar. Para viajes internacionales o de más de $2,000 en costo total, se requiere también aprobación del Director del área. Los viajes no aprobados previamente no serán reembolsados.

## Reservas
Utiliza la plataforma corporativa de viajes (TravelPerk) para reservar vuelos, hoteles y autos. Las reservas fuera de la plataforma sin justificación pueden no ser reembolsadas. TravelPerk garantiza tarifas negociadas y cumplimiento automático de la política de viajes.

## Vuelos
Reserva con al menos 14 días de anticipación para obtener las mejores tarifas. Los cambios de vuelo de último minuto deben justificarse. Las millas de viajero frecuente son personales del empleado. Los asientos de ventana o pasillo con costo adicional no se reembolsan.

## Alojamiento
Usa hoteles de la lista preferida de TravelPerk para obtener tarifas preferenciales. Si el hotel preferido no está disponible, selecciona uno dentro del límite diario autorizado. No se reembolsan hoteles de categoría superior al límite sin aprobación previa.

## Viáticos de alimentación
Cuando no se provee alimentación por la empresa o el cliente, se aplican viáticos diarios: $30 desayuno, $50 almuerzo, $80 cena. Estos son máximos, no montos fijos. Presenta los comprobantes reales.

## Transporte local en destino
Usa opciones razonables: transporte público, Uber/Lyft o auto del hotel. Los autos de alquiler requieren aprobación previa. Los autos premium no se reembolsan. Estacionamientos en hoteles se reembolsan si no hay alternativa más económica.
""",

    "vendor_payments.md": """# Pago a Proveedores

## Proceso de alta de proveedores
Antes de realizar cualquier pago, el proveedor debe estar dado de alta en el sistema. Para dar de alta un proveedor: Finanzas > Proveedores > Nuevo Proveedor. Se requiere: razón social, RFC/NIT/EIN, cuenta bancaria, datos de contacto y documentación legal (acta constitutiva, identificación del representante legal).

## Proceso de pago
1. El área solicitante recibe la factura del proveedor y la envía a accounts.payable@empresa.com con el número de orden de compra.
2. Finanzas verifica que la factura corresponda a la OC aprobada y que los servicios/productos fueron recibidos.
3. Si todo es correcto, el pago se programa para el siguiente ciclo de pagos (lunes y jueves).
4. Si hay discrepancias, se devuelve la factura al área solicitante para resolución con el proveedor.

## Términos de pago
Los términos estándar son Net 30 desde la recepción de la factura correcta. Proveedores estratégicos pueden negociar Net 15 con el CFO. Los pagos anticipados (prepago) requieren aprobación del CFO y son la excepción.

## Órdenes de compra
Todo gasto con proveedor mayor a $500 requiere una orden de compra (OC) emitida por Finanzas antes de que el proveedor entregue el servicio o producto. Las OC se solicitan en el ERP con aprobación del gerente correspondiente.

## Controles anti-fraude
Los datos bancarios de proveedores solo pueden ser modificados por personal autorizado de Finanzas, previa verificación telefónica con el proveedor. Los intentos de modificar cuentas bancarias por email sin verificación adicional deben reportarse inmediatamente como posible fraude.
""",

    "budget_planning.md": """# Planeación y Control Presupuestal

## Ciclo presupuestal
El proceso de planeación presupuestal anual inicia en octubre. Los directores de área reciben un template de Finanzas para proyectar sus gastos del año siguiente. Las propuestas se consolidan, revisan y aprueban en noviembre para que el presupuesto quede listo en diciembre.

## Estructura del presupuesto
El presupuesto se organiza por centro de costo y categoría de gasto. Cada área tiene un centro de costo único. Las categorías principales son: personal, tecnología, marketing, ventas, operaciones e I+D.

## Control de gastos vs. presupuesto
Finanzas publica un reporte mensual de gastos vs. presupuesto por área. Las desviaciones superiores al 10% del presupuesto mensual requieren explicación escrita del Director del área. Desviaciones superiores al 20% requieren plan de acción aprobado por el CFO.

## Transferencias presupuestal
Si un área necesita gastar más en una categoría pero tiene margen en otra, puede solicitar una transferencia presupuestal interna. Las transferencias hasta $10,000 las aprueba el Director del área. Las mayores requieren aprobación del CFO.

## Solicitudes fuera de presupuesto
Los gastos no contemplados en el presupuesto aprobado requieren un Business Case que justifique el ROI o la necesidad. Se presentan al CFO mensualmente en el comité de gastos extraordinarios.
""",

    "financial_reporting.md": """# Reporte Financiero Interno

## Estados financieros mensuales
Finanzas publica los estados financieros internos (P&L, Balance General, Flujo de Caja) los primeros 10 días hábiles de cada mes para el período anterior. El acceso a los estados financieros completos está restringido a directores y arriba.

## KPIs financieros
Los KPIs financieros clave (MRR, ARR, Churn, CAC, LTV, Burn Rate) se actualizan semanalmente en el dashboard ejecutivo. Los jefes de área tienen acceso a los KPIs relevantes para su función.

## Cierre mensual
El proceso de cierre contable ocurre durante los primeros 5 días hábiles del mes siguiente. Durante este período, Finanzas puede solicitar aclaraciones urgentes sobre gastos o transacciones. Los empleados deben responder en máximo 24 horas para no retrasar el cierre.

## Auditoría externa
La empresa realiza una auditoría financiera anual con un despacho externo. La auditoría ocurre en enero/febrero para el año fiscal anterior. Los departamentos pueden ser contactados por los auditores para validar transacciones. Coopera activamente y provee la documentación solicitada.

## Confidencialidad
La información financiera interna es confidencial. Compartir datos financieros con personas externas o en redes sociales es una violación grave al código de conducta y puede derivar en acciones legales.
""",

    "accounts_receivable.md": """# Cuentas por Cobrar

## Seguimiento de facturas
El equipo de Cuentas por Cobrar monitorea el estado de todas las facturas emitidas. Las facturas vencidas (más de 30 días desde la fecha límite de pago) se envían a una cola de seguimiento.

## Proceso de cobranza
- 1-15 días de retraso: recordatorio automático por email.
- 16-30 días: el equipo de AR contacta al cliente por email y teléfono.
- 31-60 días: Account Management se involucra para entender la situación del cliente.
- Más de 60 días: el caso se escala al CFO y puede derivar en suspensión del servicio.
- Más de 90 días: se evalúa enviar a un despacho de cobranza externo o iniciar acción legal.

## Acuerdos de pago
Si un cliente tiene dificultades para pagar, AR puede negociar un plan de pagos previa aprobación del CFO. Los planes de pago deben documentarse por escrito y firmarse por ambas partes.

## Notas de crédito
Las notas de crédito se emiten cuando hay un error en la facturación o cuando se aprueba un descuento post-factura. Deben ser aprobadas por el Director de Finanzas. Se aplican a la siguiente factura del cliente o se reembolsan si el cliente lo solicita.

## Cuentas incobrables
Las cuentas que superen 180 días de vencimiento sin acuerdo de pago son evaluadas para castigo contable. El proceso requiere aprobación del CFO y documentación de todos los intentos de cobro realizados.
""",

    "tax_compliance.md": """# Cumplimiento Fiscal

## Responsabilidades
El equipo de Finanzas es responsable del cumplimiento de todas las obligaciones fiscales de la empresa: declaraciones de impuestos, retenciones, IVA/VAT, impuesto sobre la renta e impuestos especiales según la jurisdicción.

## Calendario fiscal
Finanzas mantiene un calendario con todas las fechas límite de declaraciones y pagos fiscales. Los directores son notificados con 15 días de anticipación cuando necesitan información o firmas para cumplir obligaciones fiscales.

## Retenciones a proveedores
Ciertos pagos a proveedores (servicios profesionales, arrendamiento, etc.) requieren retención de impuestos según la legislación local. Finanzas configura las retenciones automáticamente en el sistema de pagos.

## Facturación electrónica
Todas las facturas emitidas deben cumplir con los requisitos de facturación electrónica de cada país donde opera la empresa. Los sistemas están configurados para generar y timbrar facturas automáticamente conforme a la normativa vigente.

## IVA/VAT en compras internacionales
Los gastos con proveedores internacionales pueden tener implicaciones de IVA/VAT. El área debe consultar a Finanzas antes de contratar servicios fuera del país para evaluar el tratamiento fiscal correcto.

## Conservación de documentos
Todos los documentos fiscales (facturas, contratos, comprobantes de pago) deben conservarse por un mínimo de 5 años, o el plazo que establezca la legislación local. Los documentos digitales son aceptados si están debidamente respaldados.
""",

    "payroll.md": """# Nómina

## Fechas de pago
La nómina se paga dos veces al mes: el día 15 y el último día hábil de cada mes. El pago se realiza por transferencia bancaria directa a la cuenta registrada en RRHH. Si el día de pago cae en fin de semana o festivo, se paga el día hábil anterior.

## Composición del pago
El recibo de nómina detalla: salario bruto, deducciones legales (impuesto sobre la renta, seguridad social), deducciones voluntarias (préstamos, seguros adicionales), reembolsos aprobados del período, y el neto a pagar.

## Cambios de cuenta bancaria
Para actualizar tu cuenta bancaria de nómina, envía la documentación al correo payroll@empresa.com con al menos 10 días hábiles de anticipación. Los cambios recibidos después del cierre del período se aplican al siguiente.

## Errores en la nómina
Si detectas un error en tu recibo de nómina, notifica a RRHH dentro de los 5 días hábiles siguientes al pago. Los errores confirmados se corrigen en el siguiente ciclo de nómina o mediante un pago especial si el monto es significativo.

## Décimotercero y prestaciones anuales
El pago de prestaciones anuales (décimotercero, participación de utilidades, prima vacacional, etc.) se realiza según la legislación local. Las fechas y montos se comunican por RRHH con al menos 30 días de anticipación.

## Anticipo de nómina
En casos de emergencia comprobada, los empleados pueden solicitar un anticipo de hasta el 50% de su quincena a través de RRHH. Los anticipos se descuentan en el siguiente ciclo de nómina. No se otorgan más de 2 anticipos por año.
""",

    "financial_controls.md": """# Controles Financieros Internos

## Segregación de funciones
Ningún empleado debe tener control total sobre una transacción financiera desde su inicio hasta su registro. Por ejemplo, quien solicita un gasto no puede ser quien lo aprueba, y quien genera el pago no puede ser quien lo contabiliza.

## Autorización de pagos
Los pagos requieren autorización según los montos: hasta $1,000 el gerente de área; $1,001-$10,000 el Director; $10,001-$50,000 el CFO; más de $50,000 requiere firma del CFO y el CEO.

## Conciliaciones bancarias
El equipo de Finanzas realiza conciliaciones bancarias diarias para cuentas operativas y mensuales para cuentas de reserva. Las diferencias se investigan y resuelven dentro de los 2 días hábiles siguientes.

## Acceso a sistemas financieros
El acceso al ERP y sistemas contables se otorga con principio de mínimo privilegio. Las contraseñas no se comparten. Los accesos inactivos por más de 90 días se revocan automáticamente.

## Auditoría interna
El equipo de Auditoría Interna realiza revisiones periódicas de los procesos financieros. Los hallazgos se reportan al Comité de Auditoría del Consejo. Toda área está sujeta a ser auditada sin previo aviso en áreas de alto riesgo.

## Fraude y irregularidades
Cualquier sospecha de fraude, malversación o irregularidad financiera debe reportarse inmediatamente al CFO o al canal anónimo de ética. Las investigaciones de fraude son manejadas por Auditoría Interna y Legal.
""",

    "procurement.md": """# Adquisiciones y Compras

## Proceso de adquisición
Para cualquier compra mayor a $500, se requiere una Orden de Compra (OC). Para generar una OC: accede al ERP > Compras > Nueva Orden de Compra. Incluye: proveedor, descripción detallada, cantidad, precio unitario y centro de costo.

## Selección de proveedores
Para compras mayores a $5,000, se deben solicitar cotizaciones a al menos 3 proveedores. Se selecciona la mejor propuesta evaluando precio, calidad, tiempo de entrega y condiciones. La selección debe documentarse.

## Proveedores preferidos
Existe un catálogo de proveedores preferidos con contratos marco negociados. Para categorías cubiertas por el catálogo (tecnología, papelería, limpieza, etc.), se debe usar el proveedor preferido salvo justificación documentada.

## Compras de emergencia
Las compras de emergencia (situaciones que impiden operar) pueden realizarse sin OC previa con autorización verbal del Director y formalización en el sistema dentro de las 24 horas siguientes.

## Recepción de bienes y servicios
Quien recibe los bienes o servicios debe registrar la recepción en el ERP. Esto confirma a Finanzas que el pago puede procesarse. No se pagan facturas sin confirmación de recepción en el sistema.

## Devoluciones
Si los bienes recibidos no cumplen con las especificaciones, se coordina la devolución con el proveedor y se anota en el ERP. El pago de la factura se suspende hasta que el proveedor corrija la entrega.
""",

    "cash_management.md": """# Gestión de Efectivo y Tesorería

## Fondo fijo de caja chica
Cada oficina tiene un fondo fijo de caja chica de $500 para gastos menores urgentes. El custodio de la caja chica es designado por el Director del área. Los gastos se documentan con comprobante y se reponen mensualmente o cuando el fondo llega al 20% de su valor.

## Manejo de efectivo
El efectivo corporativo solo debe ser manejado por personal de tesorería autorizado. Ningún empleado debe guardar efectivo corporativo en su domicilio o en cuentas personales bajo ninguna circunstancia.

## Cuentas bancarias corporativas
La apertura de cuentas bancarias corporativas requiere aprobación del Consejo. El CFO es el titular de todas las cuentas. Los empleados con firma en cuentas bancarias son designados formalmente y deben ser revocados al cambiar de rol.

## Inversiones de corto plazo
Los excedentes de tesorería superiores a $100,000 por más de 30 días se invierten en instrumentos de bajo riesgo (CETES, fondos de money market) aprobados por el CFO. Las inversiones se reportan mensualmente al Consejo.

## Proyecciones de flujo de caja
Finanzas actualiza semanalmente la proyección de flujo de caja a 13 semanas. Esta proyección guía las decisiones de inversión de excedentes y la gestión de líneas de crédito.
""",
}


def write_doc(path: Path, content: str) -> None:
    if not path.exists():
        path.write_text(content, encoding="utf-8")
        print(f"  Creado: {path.name}")
    else:
        print(f"  Ya existe: {path.name} (omitido)")


def main() -> None:
    collections = [
        ("hr_docs", HR_DOCS),
        ("tech_docs", TECH_DOCS),
        ("finance_docs", FINANCE_DOCS),
    ]

    for folder, docs in collections:
        dest = BASE_DIR / folder
        dest.mkdir(parents=True, exist_ok=True)
        print(f"\n[{folder}]")
        for filename, content in docs.items():
            write_doc(dest / filename, content)

    print("\nDocs generados correctamente.")


if __name__ == "__main__":
    main()
