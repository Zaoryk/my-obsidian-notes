# Cloud Computing

## What is Cloud Computing?

Cloud computing, or cloud computing, is a technological service delivery model that allows **remote access** to computing resources (such as servers, storage, databases, networks, software and more) over the Internet. Instead of maintaining their own physical infrastructure, organizations **use on-demand services**, paying only for what they consume.

The main concept is that computing resources behave like a public utility: they can be dynamically provisioned, scaled and released, just like electricity or water.

---

## Service models

Cloud computing is typically classified into three main models:

| Model | Full name | Brief description | Examples |
|---------|----------------|-------------------|-----------|
| **SaaS** | Software as a Service | Access to applications over the Internet without installing anything locally. | Google Workspace, Microsoft 365, Salesforce |
| **PaaS** | Platform as a Service | Provides vendor-managed development tools and environments. | Heroku, Google App Engine, AWS Elastic Beanstalk |
| **IaaS** | Infrastructure as a Service | Provides virtualized infrastructure such as servers, networks and storage. | AWS EC2, Microsoft Azure, Google Cloud Platform |

---

## Essential features of Cloud Computing

1. **Self-service on demand:** Users can provision resources without human intervention from the provider.
2. **Wide network access:** Resources are available from anywhere with an Internet connection.
3. **Resource Pooling:** The same physical resources are shared between different users through virtualization.
4. **Rapid elasticity:** Resources can be increased or decreased automatically according to demand.
5. **Service metering:** Consumption is monitored and billed based on actual usage.

---

## Implementation types

| Cloud type | Description | Typical use |
|-------------|-------------|-------------|
| **Public** | Infrastructure offered by external providers accessible to the public. | Startups, global web services |
| **Private** | Infrastructure maintained for the exclusive use of an organization. | Large companies, financial institutions |
| **Hybrid** | Mix of public and private cloud with interoperability. | Rolling migrations, backup and recovery |

---

## Main benefits

- **Cost reduction:** Eliminates the need for large investments in hardware and maintenance.
- **Scalability:** Allows capacity to be adjusted according to growth or workload.
- **Global access:** Resources are available from any device and location.
- **High availability:** Suppliers guarantee uptime of more than 99.9%.
- **Advanced security:** Encryption, authentication and redundancy measures implemented by providers.

---

## Challenges and considerations

- **Vendor dependency:** Data migration and portability can be complex.
- **Privacy and regulatory compliance:** Compliance with local and sectoral regulations (such as GDPR or ISO 27001) must be guaranteed.
- **Internet Connectivity:** Availability depends entirely on a stable connection.


# SaaS, PaaS and IaaS

## Main models

### SaaS (Software as a Service)
- **Definition:** Delivery of ready-to-use software over the Internet.
- **Examples:** Microsoft 365, Google Workspace, Gmail, Netflix, Slack.
- **Advantages:**
  - No initial investment.
  - Does not require technical knowledge.
  - The provider manages maintenance and updates.
  - Remote access from any device.
  - Quick implementation.
- **Disadvantages:**
  - Dependence on the provider and the Internet.
  - Little customization.
  - Risk of technological lock-in.
- **Payment:** By subscription.- **Typical user:** final consumer, SMEs.

### IaaS (Infrastructure as a Service)
- **Definition:** Provides virtualized infrastructure (servers, networks, storage).
- **Examples:** AWS EC2, Microsoft Azure, Google Compute Engine, Digital Ocean.
- **Advantages:**
  - Maximum control and customization.
  - There is no initial investment in hardware.
  - Immediate scalability.
  - Pay per use.
- **Disadvantages:**
  - Requires advanced technical knowledge.
  - Increased security and administration responsibilities.
  - Unexpected costs if use is not controlled.
- **Payment:** For resources used.
- **Typical user:** network architects, companies with complex needs.

### PaaS (Platform as a Service) 

- **Definition:** Environment for developing, testing and deploying software without managing the underlying infrastructure.
- **Examples:** Heroku, AWS Elastic Beanstalk, Google App Engine, Azure App Service.
- **Advantages:**
  - Accelerates development and deployment.
  - Reduces operating costs.
  - Less maintenance responsibility.
- **Disadvantages:**
  - Less customization than IaaS.
  - Limitations in frameworks and languages.

| Feature | SaaS | PaaS | IaaS |
|-------------------------|----------------------------|---------------------------|---------------------------|
| Control over resources | Low | Medium | High |
| Management | Fully supplier | Partial provider | Mostly user |
| Examples | Gmail, Office 365, Netflix | Heroku, Google App Engine | AWS EC2, Azure, DigitalOcean|
| Payment | Subscription | Subscription/usage | By use |
| User | End user | Developer | Architect/Administrator |
| Scalability | High | High | High |
| Settings | Minimum | Medium | Complex |
| Required knowledge | None | Intermediate | High |

---

## Relevance in software projects

- They allow resources to be adjusted to the demand of the project, optimizing costs.
- They facilitate collaboration and remote access.
- SaaS accelerates access to standard applications and tools.
- IaaS provides total flexibility to configure custom environments.
- PaaS facilitates the speed of development and deployment.
- They are scalable models used by startups, SMEs and large companies.