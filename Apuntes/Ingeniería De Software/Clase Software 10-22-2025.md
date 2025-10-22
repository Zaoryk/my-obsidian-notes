# Cloud Computing

## ¿Qué es Cloud Computing?

Cloud computing, o computación en la nube, es un modelo de prestación de servicios tecnológicos que permite el **acceso remoto** a recursos informáticos (como servidores, almacenamiento, bases de datos, redes, software y más) a través de Internet. En lugar de mantener una infraestructura física propia, las organizaciones **utilizan servicios bajo demanda**, pagando solo por lo que consumen.

El concepto principal es que los recursos informáticos se comportan como un servicio público: se pueden **aprovisionar, escalar y liberar dinámicamente**, al igual que sucede con la energía eléctrica o el agua.

---

## Modelos de servicio

La computación en la nube se clasifica normalmente en tres modelos principales:

| Modelo | Nombre completo | Descripción breve | Ejemplos |
|---------|----------------|-------------------|-----------|
| **SaaS** | Software as a Service | Acceso a aplicaciones a través de Internet sin instalar nada localmente. | Google Workspace, Microsoft 365, Salesforce |
| **PaaS** | Platform as a Service | Proporciona herramientas y entornos de desarrollo manejados por el proveedor. | Heroku, Google App Engine, AWS Elastic Beanstalk |
| **IaaS** | Infrastructure as a Service | Provee infraestructura virtualizada como servidores, redes y almacenamiento. | AWS EC2, Microsoft Azure, Google Cloud Platform |

---

## Características esenciales del Cloud Computing

1. **Autoservicio bajo demanda:** Los usuarios pueden aprovisionar recursos sin intervención humana del proveedor.
2. **Acceso amplio a la red:** Los recursos están disponibles desde cualquier lugar con conexión a Internet.
3. **Agrupamiento de recursos:** Se comparten los mismos recursos físicos entre distintos usuarios mediante virtualización.
4. **Elasticidad rápida:** Se pueden aumentar o disminuir los recursos de forma automática según la demanda.
5. **Medición del servicio:** El consumo se monitorea y factura según el uso real.

---

## Tipos de implementación

| Tipo de nube | Descripción | Uso típico |
|---------------|-------------|-------------|
| **Pública** | Infraestructura ofrecida por proveedores externos accesible al público. | Startups, servicios web globales |
| **Privada** | Infraestructura mantenida para uso exclusivo de una organización. | Grandes empresas, instituciones financieras |
| **Híbrida** | Mezcla de nube pública y privada con interoperabilidad. | Migraciones graduales, respaldo y recuperación |

---

## Beneficios principales

- **Reducción de costos:** Elimina la necesidad de grandes inversiones en hardware y mantenimiento.
- **Escalabilidad:** Permite ajustar la capacidad según el crecimiento o la carga de trabajo.
- **Acceso global:** Los recursos están disponibles desde cualquier dispositivo y lugar.
- **Alta disponibilidad:** Los proveedores garantizan tiempos de funcionamiento de más del 99,9%.
- **Seguridad avanzada:** Medidas de cifrado, autenticación y redundancia implementadas por los proveedores.

---

## Desafíos y consideraciones

- **Dependencia del proveedor:** La migración y portabilidad de datos pueden ser complejas.
- **Privacidad y cumplimiento normativo:** Debe garantizarse el cumplimiento de normas locales y sectoriales (como GDPR o ISO 27001).
- **Conectividad a Internet:** La disponibilidad depende completamente de una conexión estable.


# SaaS, PaaS e IaaS

## Modelos principales

### SaaS (Software as a Service)
- **Definición:** Entrega de software listo para usar a través de Internet.
- **Ejemplos:** Microsoft 365, Google Workspace, Gmail, Netflix, Slack.
- **Ventajas:**
  - Sin inversión inicial.
  - No requiere conocimientos técnicos.
  - El proveedor gestiona el mantenimiento y las actualizaciones.
  - Acceso remoto desde cualquier dispositivo.
  - Implementación rápida.
- **Desventajas:**
  - Dependencia del proveedor y de Internet.
  - Escasa personalización.
  - Riesgo de lock-in tecnológico.
- **Pago:** Por suscripción.
- **Usuario típico:** consumidor final, pymes.

### IaaS (Infrastructure as a Service)
- **Definición:** Proporciona infraestructura virtualizada (servidores, redes, almacenamiento).
- **Ejemplos:** AWS EC2, Microsoft Azure, Google Compute Engine, Digital Ocean.
- **Ventajas:**
  - Máximo control y personalización.
  - No hay inversión inicial en hardware.
  - Escalabilidad inmediata.
  - Pago por uso.
- **Desventajas:**
  - Requiere conocimientos técnicos avanzados.
  - Mayores responsabilidades de seguridad y administración.
  - Costos inesperados si no se controla el uso.
- **Pago:** Por recursos utilizados.
- **Usuario típico:** arquitectos de red, empresas con necesidades complejas.

### PaaS (Platform as a Service) 

- **Definición:** Entorno para desarrollar, testear y desplegar software sin gestionar la infraestructura subyacente.
- **Ejemplos:** Heroku, AWS Elastic Beanstalk, Google App Engine, Azure App Service.
- **Ventajas:**
  - Acelera el desarrollo y despliegue.
  - Reduce costos operativos.
  - Menos responsabilidad de mantenimiento.
- **Desventajas:**
  - Menor personalización que IaaS.
  - Limitaciones en frameworks y lenguajes.

| Característica          | SaaS                          | PaaS                         | IaaS                       |
|------------------------|-------------------------------|------------------------------|----------------------------|
| Control sobre recursos | Bajo                          | Medio                        | Alto                       |
| Gestión               | Totalmente proveedor           | Parcial proveedor            | Mayormente usuario         |
| Ejemplos               | Gmail, Office 365, Netflix    | Heroku, Google App Engine    | AWS EC2, Azure, DigitalOcean|
| Pago                   | Suscripción                   | Suscripción/uso              | Por uso                    |
| Usuario                | Usuario final                  | Desarrollador                | Arquitecto/Administrador   |
| Escalabilidad          | Alta                          | Alta                         | Alta                       |
| Configuración          | Mínima                        | Media                        | Compleja                   |
| Conocimiento requerido | Ninguno                       | Intermedio                   | Alto                       |

---

## Relevancia en proyectos de software

- Permiten ajustar recursos a la demanda del proyecto, optimizando costos.
- Facilitan la colaboración y el acceso remoto.
- El SaaS acelera el acceso a aplicaciones y herramientas estándar.
- El IaaS otorga flexibilidad total para configurar entornos personalizados.
- El PaaS facilita la velocidad de desarrollo y despliegue.
- Son modelos escalables utilizados por startups, pymes y grandes empresas.


