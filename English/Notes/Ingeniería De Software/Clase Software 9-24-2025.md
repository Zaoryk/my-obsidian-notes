![[software 4.wav]]
# ==WEEK 5

| Term | Definition |
| ----------------------------------- | --------------------------------------------------------------------------------- |
| **Requirements analysis** | Determine needs and conditions to meet the objectives of a project.   |
| **System interaction** | Communication and collaboration between the components of a system.                  |
| **Requirements survey** | Compilation and documentation of customer needs and expectations.           |
| **Agile methodologies** | Development practices that promote flexibility and collaboration.                |
| **Development methodologies** | Structured approaches to plan, design, implement and maintain software. |
| **Design patterns** | Reusable solutions to common problems in software design.            |
| **Design proposal** | Document that describes how the system will be built according to the requirements.        |
| **Software quality** | Degree to which software meets user requirements and expectations.        |
| **Software life cycle** | Phases from the conception of the software to its retirement.                           |
| **Co-creation** | Collaboration between developers and users to generate ideas and solutions.    |
| **Class diagram** | Representation of classes, attributes, methods and relationships in a system.          |
| **Sequence diagram** | Interaction of objects over time.                                       |
| **Use case diagram** | Interactions between external actors and the system.                                |
| **Scrum** | Agile framework based on iterations and continuous feedback.                    |
| **Validation with client** | Verification that the final product meets expectations and needs.          |

---

## Life Cycles and Development Methodologies

### Lifecycle of a software project
1. **Requirements**  
2. **Design**  
3. **Implementation**  
4. **Tests**  
5. **Deployment and maintenance**

### Methodologies

| Type | Features | Advantages | Limitations |
|------|----------------|----------|--------------|
| **Traditional (Waterfall)** | Sequential phases, requirements defined at the beginning. | Clarity, complete documentation. | Little flexible in the face of changes. |
| **Agile (Scrum, Kanban)** | Iterative, adaptive, sprint-based. | Flexibility, continuous feedback. | Risk of poor initial planning. |
| **Hybrid** | Combine the best of both approaches. | Flexibility + traceability. | It can be complex to implement. |

### Methodology selection
- Depends on: project size, available resources, client requirements, deadlines and budget.

---

## Requirements Survey and Co-creation

### What is a requirement?
- **Functional** → what the system does.  
- **Non-functional** → restrictions (time, security, usability, storage).

### Techniques
1. Interviews  
2. Co-creation workshops  
3. Surveys and questionnaires  
4. Observation  
5. Prototypes  
6. Mapping user stories  
7. Documentation analysis  
8. Focus groups  

### Actors of the process
- **Users** → They operate the software.  
- **Clients** → They order the software.  
- **Market analysts** → They define market needs.  
- **Regulators** → Require regulatory compliance.  
- **Software engineers** → Development, reuse and maintenance.  

---

## Design Patterns

| Pattern | Description | Usage | Advantages | Disadvantages |
|--------|-------------|-----|----------|-------------|| **Singleton** | A single global instance. | Configuration, logging. | Easy centralized access. | Difficult to test, breaks SRP. |
| **Factory** | Creates objects without specifying a concrete class. | Complex and dynamic creation. | Extendable, flexible. | Increases complexity. |
| **Observer** | 1 to many relationship (subscriber/publisher). | Events, reactive systems. | Low coupling. | Performance risks if there are many observers. |
| **Adapter** | Makes different interfaces compatible. | Legacy code integration. | Reuse without modifying code. | Extra complexity. |

---

## UML diagrams

### Main types
1. **Structural** → Classes, objects, components, deployment.  
2. **Behavioral** → Use cases, sequence, activities, states.

### Examples
- **Use case diagram** → Interactions between actors and the system.  
- **Class diagram** → Static structure (attributes, methods, relationships).  
- **Sequence diagram** → Chronological message flow.  

---

## Software Quality Standards

| Standard | Focus | Application |
|----------|---------|------------|
| **ISO/IEC 12207** | Software life cycle processes. | Projects with a sequential approach (Cascade). |
| **ISO/IEC 33000 (SPICE)** | Process maturity. | Evaluation and continuous improvement. |
| **ISO 9001** | Quality management. | Customer satisfaction, continuous improvement. |
| **ISO/IEC 25000 (SQuaRE)** | Software product quality. | Metrics: functionality, usability, reliability, maintainability. |

---

## Ideas Strength

1. **Appropriate methodology** impacts efficiency and quality.  
2. **Well-defined requirements** are key to avoiding failures.  
3. **Co-creation with the client** ensures that the software meets expectations.  
4. **Design patterns** are proven solutions to common problems.  
5. The **UML facilitates communication** between teams and stakeholders.  
6. **ISO standards** ensure quality and continuous improvement.  

### *Software* Product Lifecycle

# ==WEEK 6

### What is a requirement?

Description of the services offered by a system and its operational restrictions. They also reflect the needs of customers.

Way of discovering the requirements of a system through communication with customers in the development of the system.

### Functional requirements

Declarations of the services that the system should provide, of the way in which it should react to particular inputs. You can also declare what the system should NOT do.

### Non-functional requirements

Restrictions on the services or functions offered by the system. Time constraints, development process and standards. Everything related to reliability, response time and storage capacity. Features that can limit the system.

![[Pasted image 20250924140726.png]]

| Product requirements | Organizational requirements | External requirements | Interoperability requirements | Legislative requirements |
|--------------------------|------------------------------|-------------------------|------------------------------------------|--------------------------|
| Performance in how **fast** the system executes and how much memory is required. | Standards in the processes that must be used. | Physical security requirements (e.g. conditions of the environment where the system will operate). | The way the system interacts with systems of other organizations. | They must be followed to ensure that the system operates within the law. || **Reliability** requirements, which set the acceptable failure rate. **portability** requirements. | Implementation requirements: programming languages ​​or design method to use. | Contractual requirements with clients or suppliers (e.g. delivery times, service levels). | Compatibility with standard protocols (e.g. HTTP, SOAP, REST, ISO/OSI). | Compliance with data protection regulations (e.g. Law 19,628 in Chile, GDPR in Europe). |
| Requirements for **usability**, ease of use and accessibility. | Delivery requirements: when the product and its documentation will be delivered. | Requirements imposed by the market or external users (e.g. multi-language support, integration with third-party apps). | Communication requirements between different software and hardware modules. | Software licensing requirements, intellectual property, accessibility standards (e.g. WCAG). |

#### In summary:

| **Usability** | Human factors, help, documentation |
| ------------------ | ------------------------------------------------------------------------- |
| **Reliability** | Failure frequency, recovery time |
| **Performance** | Response time, processing rate, precision, load capacity |
| **Supportability** | Adaptability, maintainability, configurability |
| **Interface** | Restrictions on communication with external systems |
### Software requirements

**Priority** that must be exhibited by something, in order to **solve** some **problem in the real world**

It is about automating part of a task aimed at someone to support the business processes of an organization, to correct defects in existing software or to control a device, to name just a few of the many problems that can be solved thanks to software.

That they are **verifiable** even when it is difficult or expensive to verify them. Verifying the productivity requirement in a call center may require the development of simulation software.

Requirements have other attributes in addition to behavioral properties.

### Co-creation techniques and requirements gathering

Collects accurate information about user needs and project objectives.


| Interviews | Co-creation workshops | Surveys and questionnaires | Observation |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ || Structured or semi-structured meetings with stakeholders to obtain detailed information about their needs and expectations. Interviews can be individual or group. | Collaborative sessions where developers and clients work together to generate ideas and solutions. These workshops encourage creativity and ensure that all stakeholders have a voice in the process. | Collect information from a large number of users. Obtain quantitative and qualitative data on customer needs and preferences. | Study of the user's environment and activities to better understand their needs and how they interact with the system. It can be direct or through the use of recordings. |

| Focus groups | Documentation analysis | User Story Mapping | Prototypes |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Meetings with a group of representative users to discuss their needs and obtain feedback on ideas and prototypes. *Focus groups* allow you to explore different perspectives and obtain valuable *insights* | Review of existing documents, such as manuals, reports and specifications, to extract relevant information about the system requirements. | Technique that organizes user stories in a visual map, showing how they relate to each other and to the project objectives. Helps prioritize features and understand **system flow** | Creation of preliminary versions of the system that allow clients to visualize and test functionalities before final implementations. Prototypes facilitate early feedback and validation of requirements |
### Customer Validation and Engagement


| Periodic reviews | Iterative feedback | Clear documentation | Benefits of customer validation and engagement || -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scheduling regular client meetings is crucial to maintaining open and ongoing communication.                                         | Implementing continuous feedback loops is essential to ensure that the final product meets customer expectations. | Maintaining detailed and up-to-date documentation is essential to ensure that all parties have a common understanding of the project.<br> | Continuous validation and customer engagement offer several benefits.<br> |
| **Review progress**: Evaluate the current status of the project and compare progress with the initial plan.                                         | **Prototypes and demos** – Present preliminary versions of the product so the customer can test and provide feedback.  | **Requirements Recording**: Document all requirements captured, including specific details and any agreed changes.<br> | <br>**Expectation Alignment**: Ensures the final product meets the customer's expectations and needs.<br> |
| **Validate requirements**: confirm that the captured requirements are still relevant and complete, and adjust any necessary changes | **Feedback Loops** – Collect and analyze customer feedback at each iteration, and make adjustments as necessary.<br> | **Change History** – Maintain a record of all modifications made to the original requirements, along with the corresponding reasons and approvals.<br> | **Risk Reduction** – Identifies and mitigates potential risks from the early stages of the project.<br> |
| **Identify problems early**: detect and resolve potential problems before they become major obstacles | **Adaptability**: Be willing to modify system requirements and design based on feedback received.<br> | **Accessibility** – Ensure documentation is easily accessible to all team members and the client.<br> | **Quality Improvement** – Increase the quality of the final product by incorporating feedback and making continuous adjustments.<br> |
| **encourage transparency**: Keep the client informed about project development, which helps build trust and collaboration | **Continuous Improvement** – Use feedback to continually improve the product and development process.                                 | **Clarity and precision** – Write documentation clearly and precisely to avoid misunderstandings and ensure that all stakeholders have the same understanding of the project.<br> | **Customer Satisfaction** – Fosters a positive relationship with the customer, increasing their satisfaction and trust in the development team<br> |

### Actors of the processEach of whom has a stake in the software. Stakeholders may vary across projects, but will always include users, operators, and customers.


| Users | Clients | Market analysts | Regulators | Software engineers |
| --------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| It is often a heterogeneous group involving people with different roles and needs. | They have commissioned the _software_ or represent the target market for the _software_. | Marketing people are needed to establish market needs and to act as test or filter customers. | The software in these domains must comply with the requirements of regulatory authorities. | A customer for a particular product has specific requirements that compromise the possibilities of component reuse, software engineers must weigh their interests against those of the customer. |
It is the software engineer's job to **negotiate trade-offs** that are acceptable to key stakeholders and within budgetary, technical, regulatory and other constraints.