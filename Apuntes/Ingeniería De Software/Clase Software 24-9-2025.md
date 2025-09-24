# ==SEMANA 5

### ¿Qué es un requerimiento?

Descripción de los servicios que ofrece un sistema y sus restricciones operativas. También reflejan las necesidades de los clientes.

Forma de descubrir los requisitos de un sistema a través de la comunicación con los clientes en el desarrollo del sistema.

### Requerimientos funcionales

Declaraciones de los servicios que debe proporcionar el sistema, de la manera en que éste debe reaccionar a entradas particulares. También puede declarar lo que el sistema NO debe hacer.

### Requerimientos no funcionales

Restricciones del servicios o funciones ofrecidos por el sistema. Restricciones de tiempo, proceso de desarrollo y estándares. Todo lo referente a fiabilidad, el tiempo de respuesta y la capacidad del almacenamiento. Características que pueden limitar al sistema.

![[Pasted image 20250924140726.png]]


| Requerimientos del producto                                                                                                         | Requerimientos organizacionales                                                                        | Requerimientos externos | Requerimientos de interoperabilidad                                       | Requerimientos legislativos                                            |
| ----------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ | ----------------------- | ------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| Rendimiento en la **rapidez** de ejecución del sistema y cuánta memoria se requiere;                                                | Estándares en los procesos que deben utilizarse;                                                       | no hay info :(          | La manera que el sistema interactúa con sistemas de otras organizaciones. | Deben seguirse para asegurar que el sistema funcione dentro de la ley. |
| Requerimientos de **fiabilidad**, que fijan la tasa de fallos para que el sistema sea aceptable. Requerimientos de **portabilidad** | Requerimientos de implementación, como los lenguajes de programación o el método de diseño a utilizar. |                         |                                                                           |                                                                        |
| Requerimientos de **usabilidad**                                                                                                    | Requerimientos de entrega que especifican cuándo se entregará el producto y su documentación           |                         |                                                                           |                                                                        |

#### En resumen:

| **Usabilidad**     | Factores humanos, ayuda, documentación                                    |
| ------------------ | ------------------------------------------------------------------------- |
| **Confiabilidad**  | Frecuencia de fallas, tiempo de recuperación                              |
| **Performance**    | Tiempo de respuesta, tasa de procesamiento, precision, capacidad de carga |
| **Soportabilidad** | Adaptabilidad, mantenibilidad, configurabilidad                           |
| **Interfaz**       | Restricciones en la comunicación con sistemas externos                    |
### Requerimientos del software

**Prioridad** que debe ser exhibida por algo, con el fin de **resolver** algún **problema en el mundo real**

Se trata de automatizar parte de una tarea dirigida a alguien que permita apoyar los procesos de negocio de una organización, para corregir defectos de software existente o para controlar un dispositivo, por nombrar solo algunos de los muchos problemas que son posibles de solucionar gracias a los softwares.

Que sean **verificables** aun cuando sea difícil o costoso verificarlos. La verificación del requisito de productividad en un centro de llamadas puede requerir el desarrollo de software de simulación.

Los requerimientos tienen otros atributos, además de propiedades de comportamiento.

### Técnicas de cocreación y levantamiento de requerimientos

Recopila información precisa sobre las necesidades de los usuarios y los objetivos del proyecto.


| Entrevistas                                                                                                                                                                                      | Talleres de cocreación                                                                                                                                                                                                        | Encuestas y cuestionarios                                                                                                                         | Observación                                                                                                                                                                    |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Reuniones estructuradas o semi estructuradas con los *stakeholders* para obtener información detallada sobre sus necesidades y expectativas. Las entrevistas pueden ser individuales o grupales. | Sesiones colaborativas donde los desarrolladores y los clientes trabajan juntos para generar ideas y soluciones. Estos talleres fomentan la creatividad y aseguran que todas las partes interesadas tengan voz en el proceso. | Recopilar información de un gran número de usuarios. Obtener datos cuantitativos y cualitativos sobre las necesidades y preferencias del cliente. | Estudio del entorno y las actividades del usuario para comprender mejor sus necesidades y cómo interactúan con el sistema. Puede ser directa o mediante el uso de grabaciones. |

| Focus groups                                                                                                                                                                                                                      | Análisis de documentación                                                                                                                               | Mapeo de historias de usuario                                                                                                                                                                                        | Prototipos                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reuniones con un grupo de usuarios representativos para discutir sus necesidades y obtener retroalimentación sobre ideas y prototipos. Los *focus groups* permiten explorar diferentes perspectivas y obtener *insights* valiosos | Revisión de documentos existentes, como manuales, reportes y especificaciones, para extraer información relevante sobre los requerimientos del sistema. | Técnica que organiza las historias de usuario en un mapa visual, mostrando cómo se relacionan entre sí y con los objetivos del proyecto. Ayuda a priorizar las funcionalidades y a entender el **flujo del sistema** | Creación de versiones preliminares del sistema que permiten a los clientes visualizar y probar funcionalidades antes de implementaciones final. Los prototipos facilitan la retroalimentación temprana y la validación de los requerimientos |
### Validación y participación del cliente


| Revisiones periódicas                                                                                                                              | Feedback iterativo                                                                                                                           | Documentación clara                                                                                                                                                                         | Beneficios de la validación y participación del cliente                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Programar reuniones regulares con el cliente es crucial para mantener una comunicación abierta y continua.                                         | Implementar ciclos de retroalimentación continua es fundamental para asegurar que el producto final cumpla con las expectativas del cliente. | Mantener una documentación detallada y actualizada es esencial para asegurar que todas las partes tengan una comprensión común del proyecto.<br>                                            | La validación continua y la participación del cliente ofrecen varios beneficios.<br>                                                              |
| **Revisar el progreso**: evaluar el estado actual del proyecto y comparar los avances con el plan inicial.                                         | **Prototipos y demostraciones**: presentar versiones preliminares del producto para que el cliente pueda probar y proporcionar comentarios.  | **Registro de requerimientos**: documentar todos los requerimientos capturados, incluyendo detalles específicos y cualquier cambio acordado.<br>                                            | <br>**Alineación de expectativas**: asegura que el producto final cumpla con las expectativas y necesidades del cliente.<br>                      |
| **Validar requerimientos**: confirmar que los requerimientos capturados siguen siendo relevantes y completos, y ajustar cualquier cambio necesario | **Ciclos de retroalimentación**: recoger y analizar el feedback del cliente en cada iteración, y realizar ajustes según sea necesario.<br>   | **Historial de cambios**: mantener un registro de todas las modificaciones realizadas a los requerimientos originales, junto con las razones y aprobaciones correspondientes.<br>           | **Reducción de riesgos**: identifica y mitiga riesgos potenciales desde las primeras etapas del proyecto.<br>                                     |
| **Identificar problemas tempranos**: detectar y resolver problemas potenciales antes que se conviertan en obstáculos mayores                       | **Adaptabilidad**: estar dispuesto a modificar los requerimientos y el diseño del sistema en función de la retroalimentación recibida.<br>   | **Accesibilidad**: asegurar que la documentación esté fácilmente accesible para todos los miembros del equipo y el cliente.<br>                                                             | **Mejora de la calidad**: aumenta la calidad del producto final al incorporar feedback y realizar ajustes continuos.<br>                          |
| **fomentar la transparencia**: Mantener al cliente informado sobre el desarrollo del proyecto, lo que ayuda a construir confianza y colaboración   | **Mejora continua**: utilizar el feedback para mejorar continuamente el producto y el proceso de desarrollo.                                 | **Claridad y precisión**: redactar la documentación de manera clara y precisa para evitar malentendidos y asegurar que todos los stakeholders tengan la misma comprensión del proyecto.<br> | **Satisfacción del cliente**: fomenta una relación positiva con el cliente, aumentando su satisfacción y confianza en el equipo de desarrollo<br> |

### Actores del proceso

Cada uno de los cuales tiene una participación en el _software._ Las partes interesadas podrán variar a través de proyectos, pero siempre incluirán los usuarios, operadores y clientes.


|     |     |     |     |     |
| --- | --- | --- | --- | --- |
|     |     |     |     |     |

# ==SEMANA 6