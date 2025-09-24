# ==SEMANA 5

| Término | Definición |
|---------|------------|
| **Análisis de requerimientos** | Determinar necesidades y condiciones para cumplir los objetivos de un proyecto. |
| **Interacción del sistema** | Comunicación y colaboración entre los componentes de un sistema. |
| **Levantamiento de requerimientos** | Recopilación y documentación de necesidades y expectativas del cliente. |
| **Metodologías ágiles** | Prácticas de desarrollo que promueven flexibilidad y colaboración. |
| **Metodologías de desarrollo** | Enfoques estructurados para planificar, diseñar, implementar y mantener software. |
| **Patrones de diseño** | Soluciones reutilizables a problemas comunes en el diseño de software. |
| **Propuesta de diseño** | Documento que describe cómo se construirá el sistema según los requisitos. |
| **Calidad del software** | Grado en que un software cumple con requisitos y expectativas del usuario. |
| **Ciclo de vida del software** | Fases desde la concepción del software hasta su retiro. |
| **Cocreación** | Colaboración entre desarrolladores y usuarios para generar ideas y soluciones. |
| **Diagrama de clases** | Representación de clases, atributos, métodos y relaciones en un sistema. |
| **Diagrama de secuencia** | Interacción de objetos a través del tiempo. |
| **Diagrama de casos de uso** | Interacciones entre actores externos y el sistema. |
| **Scrum** | Marco ágil basado en iteraciones y retroalimentación continua. |
| **Validación con cliente** | Verificación de que el producto final cumple expectativas y necesidades. |

---

## Ciclos de Vida y Metodologías de Desarrollo

### Ciclo de vida de un proyecto de software
1. **Requisitos**  
2. **Diseño**  
3. **Implementación**  
4. **Pruebas**  
5. **Despliegue y mantenimiento**

### Metodologías

| Tipo | Características | Ventajas | Limitaciones |
|------|----------------|----------|--------------|
| **Tradicional (Cascada)** | Fases secuenciales, requisitos definidos al inicio. | Claridad, documentación completa. | Poco flexible ante cambios. |
| **Ágil (Scrum, Kanban)** | Iterativo, adaptable, basado en sprints. | Flexibilidad, retroalimentación continua. | Riesgo de poca planificación inicial. |
| **Híbrido** | Combina lo mejor de ambos enfoques. | Flexibilidad + trazabilidad. | Puede ser complejo de implementar. |

### Selección de metodología
- Depende de: tamaño del proyecto, recursos disponibles, requisitos del cliente, plazos y presupuesto.

---

## Levantamiento de Requerimientos y Cocreación

### ¿Qué es un requerimiento?
- **Funcional** → qué hace el sistema.  
- **No funcional** → restricciones (tiempo, seguridad, usabilidad, almacenamiento).

### Técnicas
1. Entrevistas  
2. Talleres de cocreación  
3. Encuestas y cuestionarios  
4. Observación  
5. Prototipos  
6. Mapeo de historias de usuario  
7. Análisis de documentación  
8. Focus groups  

### Actores del proceso
- **Usuarios** → Operan el software.  
- **Clientes** → Encargan el software.  
- **Analistas de mercado** → Definen necesidades de mercado.  
- **Reguladores** → Exigen cumplimiento normativo.  
- **Ingenieros de software** → Desarrollo, reutilización y mantenimiento.  

---

## Patrones de Diseño

| Patrón | Descripción | Uso | Ventajas | Desventajas |
|--------|-------------|-----|----------|-------------|
| **Singleton** | Una sola instancia global. | Configuración, logging. | Fácil acceso centralizado. | Difícil de testear, rompe SRP. |
| **Factory** | Crea objetos sin especificar clase concreta. | Creación compleja y dinámica. | Extensible, flexible. | Aumenta complejidad. |
| **Observer** | Relación 1 a muchos (suscriptor/publicador). | Eventos, sistemas reactivos. | Bajo acoplamiento. | Riesgos de rendimiento si hay muchos observadores. |
| **Adapter** | Hace compatibles interfaces distintas. | Integración de código legado. | Reutilización sin modificar código. | Complejidad extra. |

---

## Diagramas UML

### Tipos principales
1. **Estructurales** → Clases, objetos, componentes, despliegue.  
2. **De comportamiento** → Casos de uso, secuencia, actividades, estados.

### Ejemplos
- **Diagrama de casos de uso** → Interacciones entre actores y el sistema.  
- **Diagrama de clases** → Estructura estática (atributos, métodos, relaciones).  
- **Diagrama de secuencia** → Flujo de mensajes cronológico.  

---

## Estándares de Calidad en Software

| Estándar | Enfoque | Aplicación |
|----------|---------|------------|
| **ISO/IEC 12207** | Procesos del ciclo de vida del software. | Proyectos con enfoque secuencial (Cascada). |
| **ISO/IEC 33000 (SPICE)** | Madurez de procesos. | Evaluación y mejora continua. |
| **ISO 9001** | Gestión de la calidad. | Satisfacción del cliente, mejora continua. |
| **ISO/IEC 25000 (SQuaRE)** | Calidad del producto de software. | Métricas: funcionalidad, usabilidad, fiabilidad, mantenibilidad. |

---

## Ideas Fuerza

1. La **metodología adecuada** impacta la eficiencia y calidad.  
2. Los **requerimientos bien levantados** son clave para evitar fallos.  
3. La **cocreación con el cliente** asegura que el software cumpla expectativas.  
4. Los **patrones de diseño** son soluciones probadas para problemas comunes.  
5. El **UML facilita la comunicación** entre equipos y stakeholders.  
6. Los **estándares ISO** aseguran calidad y mejora continua.  

### Ciclo de vida de producto de *software*

# ==SEMANA 6

### ¿Qué es un requerimiento?

Descripción de los servicios que ofrece un sistema y sus restricciones operativas. También reflejan las necesidades de los clientes.

Forma de descubrir los requisitos de un sistema a través de la comunicación con los clientes en el desarrollo del sistema.

### Requerimientos funcionales

Declaraciones de los servicios que debe proporcionar el sistema, de la manera en que éste debe reaccionar a entradas particulares. También puede declarar lo que el sistema NO debe hacer.

### Requerimientos no funcionales

Restricciones del servicios o funciones ofrecidos por el sistema. Restricciones de tiempo, proceso de desarrollo y estándares. Todo lo referente a fiabilidad, el tiempo de respuesta y la capacidad del almacenamiento. Características que pueden limitar al sistema.

![[Pasted image 20250924140726.png]]

| Requerimientos del producto | Requerimientos organizacionales | Requerimientos externos | Requerimientos de interoperabilidad | Requerimientos legislativos |
|-----------------------------|---------------------------------|-------------------------|-------------------------------------|-----------------------------|
| Rendimiento en la **rapidez** de ejecución del sistema y cuánta memoria se requiere. | Estándares en los procesos que deben utilizarse. | Requerimientos de seguridad física (ej: condiciones del entorno donde operará el sistema). | La manera en que el sistema interactúa con sistemas de otras organizaciones. | Deben seguirse para asegurar que el sistema funcione dentro de la ley. |
| Requerimientos de **fiabilidad**, que fijan la tasa de fallos aceptable. Requerimientos de **portabilidad**. | Requerimientos de implementación: lenguajes de programación o método de diseño a utilizar. | Requerimientos contractuales con clientes o proveedores (ej: plazos de entrega, niveles de servicio). | Compatibilidad con protocolos estándar (ej: HTTP, SOAP, REST, ISO/OSI). | Cumplimiento de normativas de protección de datos (ej: Ley 19.628 en Chile, GDPR en Europa). |
| Requerimientos de **usabilidad**, facilidad de uso y accesibilidad. | Requerimientos de entrega: cuándo se entregará el producto y su documentación. | Requerimientos impuestos por el mercado o usuarios externos (ej: soporte multi-idioma, integración con apps de terceros). | Requerimientos de comunicación entre distintos módulos de software y hardware. | Requerimientos de licencias de software, propiedad intelectual, normas de accesibilidad (ej: WCAG). |

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


| Usuarios                                                                                      | Clientes                                                                         | Los analistas de mercado                                                                                                       | Reguladores                                                                                         | Los ingenieros de software                                                                                                                                                                                                            |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A menudo es un grupo heterogéneo que involucra a personas con diferentes roles y necesidades. | Han encargado el _software_ o que representan el mercado objetivo de _software_. | la gente de marketing es necesaria para establecer las necesidades del mercado y para actuar como clientes de prueba o filtro. | El _software_ en estos dominios debe cumplir con los requerimientos de las autoridades reguladoras. | Un cliente de un producto en particular tiene requerimientos específicos que comprometen las posibilidades de reutilización de componentes, los ingenieros de _software_ deben sopesar sus intereses con respecto de los del cliente. |
Es el trabajo del ingeniero de _software_ **negociar compensaciones** que sean aceptables para los principales grupos de interés y dentro de las limitaciones presupuestarias, técnicas, normativas y otros.