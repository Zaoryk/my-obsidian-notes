# 4+1 Paradigm and Database Diagrams

---
## 4+1 paradigm
![[Pasted image 20250915104623.png]]
![[Pasted image 20250915110407.png]]
### Concepts
- **View**: Representation of the system from a perspective.  
- **Point of view**: Set of rules to interpret views.  

Proposed by **Philippe Kruchten** (IEEE 1471-000).  
Defines **4 views + 1 scenario** to describe a software system.  

### Views of the 4+1 Paradigm
| View | Purpose | Typical diagrams |
| ----------------------------------- | -------------------------------------------------------- | -------------------------------------------- |
| **Logic** | Static system structure and object relationships. | Class diagrams, communication, sequence.   |
| **Process (operational)** | Concurrent processes, communication, synchronization.     | Activity diagrams, interaction.            |
| **Development (software physics)** | Software organization, components.                  | Component diagrams.                       |
| **Physics (infrastructure)** | Distribution in hardware and execution nodes.           | Deployment diagrams.                        |
| **Scenarios (+1)** | Use cases that integrate the 4 views.                  | Use case diagrams, narrative examples. |

---
## Scenario View
![[Pasted image 20250915104856.png]]
- Describes how a user interacts with the system.  
- Example: Customer in electronic commerce → login → purchase → confirmation → shipping.  

---
## Logical View – Diagrams
- **Class diagrams**: relationships between objects, attributes, methods.  
- **Communication diagrams**: interaction between objects.  
- **Sequence diagrams**: temporal order of messages between objects.  

### Class Notation in UML
| Area | Content |
| -------- | ------------------------------------------ |
| Top | Class name (italics if abstract). |
| Medium | Attributes (ex: `+nombre: String`).            |
| Lower | Methods (ex: `+getNombre(): String`).         |

### Visibility
| Symbol | Type | Description |
| ------- | --------- | ---------------------------------- |
| `+` | Public | Accessible from anywhere.   |
| `-` | Private | Accessible only from the class.     |
| `#` | Protected | Accessible from class and subclasses. |
| `/` | Derived | Calculated.                         |
| `~` | Package | Accessible in the same package.     |

==Static attributes or methods are underlined.  ==

---
## Relationships in UML
| Type | Description |
|------|-------------|
| **Association** | Generic relationship between classes. |
| **Aggregation** | “Has a” relationship, but weak (e.g. Course-Student). |
| **Composition** | Strong relationship, dependent life cycle (e.g. House-Room). |
| **Dependency** | A change in one class affects another. |
| **Inheritance** | A child class inherits attributes/methods from the parent class. |

### Multiplicity (Cardinality)
Example:  
- `1..*` → One class can be associated with many objects of another.  
- `0..1` → A class may not be associated, or only with one object.  

### Bidirectionality
- Navigable relationship in both directions.  
- Example: **User ↔ Loan**.  
- Dependency: **Notifier → User** (not bidirectional).  

---
## UML Mapping → Relational Model
Suggested steps:
1. Model classes.  
2. Identify persistent objects.  
3. Map classes to tables.  
4. Select inheritance strategy.  
5. Define unique identifier (PK).  
6. Map attributes to columns.  
7. Map associations to foreign keys.  
8. Define relationship roles.9. Model behavior.  
10. Create physical model.  

==In UML, a table is represented as a class with stereotype ==`«Table»`. 

---
## Design Patterns

### Definition
- Reusable solutions for common software design problems.  
- They function as **templates** applicable in different contexts.  

### Types
| Group | Features |
|-------|----------------|
| **GRASP** (General Responsibility Assignment Software Patterns) | DOO principles → help decide responsibilities. Examples: Controller, Expert, High Cohesion, Low Coupling, Indirection, Pure Manufacturing. |
| **GoF** (Gang of Four) | Implementable solutions → each pattern includes its own class diagram. Examples: Singleton, Factory, Observer, Decorator, Adapter. |

---
## Component Diagrams

### What is a component?
- Physical software element: executable, DLL, library, database, module.
- It is the **materialization of classes**.

### Component types
| Type | Examples |
|------|----------|
| **Distribution** | Executables, DLLs, ActiveX, Java Beans |
| **Work** | Source code, databases |
| **Execution** | Dynamic objects created at runtime (search engine indexes, sessions) |

### UML Component Stereotypes
| Stereotype | Meaning |
|-------------|-------------|
| `<<executable>>` | Executable program |
| `<<library>>` | Library (static or dynamic) |
| `<<table>>` | Database table |
| `<<file>>` | Data or code file |
| `<<document>>` | Document |

### Interfaces in components
- **Provided/Required** → what you offer and what you need.  
- They are represented as “entry/exit doors”.  
- They allow **reuse**: a component can be replaced by another if it meets the same interface.

---
## Dependencies and Subsystems

- **Dependency**: relationship where one component uses the services of another.
- **Subsystems**: logical groupings of components.  
  - Equivalent to packages at the logical level.  
  - They are represented with `<<subsystem>>`.

---
## Deployment Diagrams

### Concept
- They show the **physical layout** of the system:  
  - Nodes (servers, devices, terminals).  
  - Components deployed in each node.  

### Nodes
| Type | Description |
|------|-------------|
| **Processor** | Node with computing capacity, executes components. |
| **Device** | Node without computation, represents auxiliary hardware. |

### Connections between nodes
- They are modeled as **bidirectional associations**.  
- They can be tagged with protocols: `<<TCP/IP>>`, `<<RDSI>>`, `<<RS-232>>`, etc.

### Node ↔ Component Relationship
- The **components** → physical packaging.  
- The **nodes** → physical deployment.  
- Example:  
  - Server node displays `ventas.exe` and `clientes.exe`.  
  - Client node displays `user.exe`.

---
## Multilevel Architectures

- **2 levels** → Client/Server (client does the heavy lifting).  
- **3 levels** → Separation into:  
  1. Presentation  
  2. Business logic  
  3. Storage  

Advantages:  
- Flexibility in maintenance.  
- Clear separation of responsibilities.  
- Facilitates reuse.

---
## Modeling Key Points

- **Models must be useful, simple and elegant**.  
- It is important to maintain **traceability** between levels of abstraction.  
- Bet on **object orientation with UML**.  
- Possible future improvements:  
  - **Evolution**: use of object-oriented databases.  
  - **Revolution**: automatic code generation from models (MDA, Model Driven Architecture).
# Visual Summary

### 4+1 paradigm
- Logical View → structure and classes.  
- Process View → concurrency and flow.  
- Development View → organization into components.  
- Physical View → hardware deployment.  
- Scenarios View → use cases.  

### UML and DB- Classes = structures with attributes and methods.  
- Relationships: association, aggregation, composition, dependence, inheritance.  
- Cardinality: 1..1, 1..*, 0..1, etc.  
- UML Mapping → Tables, PK, FK.  

### Design Patterns
- GRASP: principles of assignment of responsibilities.  
- GoF: classic implementable patterns (Factory, Singleton, Observer, etc.).  

## Recommended Bibliography
- Martin Fowler – *UML Distilled (UML Drop by Drop)*  
- Pierre-Alain Muller – *Instant UML*  
- Terry Quatrani – *Visual Modeling*  
- UML Resources: [OMG UML](https://www.omg.org/spec/UML/)  

# EXTRA INFORMATION

---
## Design Patterns

### What are they?
- Proven solutions to recurring problems in development.
- They were born in the 70s, popularized by the book **Design Patterns (GoF, 1994)**.
- Benefits:
  1. **Time savings** → don't reinvent the wheel.  
  2. **Security and stability** → already tested by the community.  
  3. **Common language** → facilitates communication between developers.

---
## Types of Design Patterns (GoF)

### 1. Creational Patterns
They simplify **creation of objects** and decouple the way they are created from the software logic.

| Pattern | Description |
|--------|-------------|
| **AbstractFactory** | Interface to create families of related objects. |
| **Factory Method** | Subclasses decide how to instantiate objects. |
| **Builder** | It separates creation and structure, allowing different products with the same process. |
| **Singleton** | Ensures that only one global instance exists. |
| **Prototype** | Clone existing objects as templates. |

---
### 2. Structural Patterns
They define how classes/objects relate to each other.

| Pattern | Description |
|--------|-------------|
| **Adapter** | Allows compatibility between different interfaces. |
| **Bridge** | Separate abstraction and implementation to evolve separately. |
| **Composite** | Tree-like hierarchical structures. |
| **Decorator** | Add responsibilities to objects dynamically. |
| **Facade** | Provides simplified interface to complex subsystems. |
| **Flyweight** | Reduce memory usage by sharing heavy objects. |
| **Proxy** | Represents another object (e.g. remote, deferred access). |

---
### 3. Behavior Patterns
They manage algorithms, communication and responsibilities.

| Pattern | Description |
|--------|-------------|
| **Command** | Encapsulates an operation on an object. |
| **Chain of Responsibility** | Messages pass through the chain until they are handled. |
| **Interpreter** | Defines grammars and expression processing. |
| **Iterator** | Iterates over collections without exposing their structure. |
| **Mediator** | Centralizes communication between objects. |
| **Memento** | Allows you to restore the previous state of an object. |
| **Observer** | Notify changes to subscribed objects. |
| **State** | Modifies behavior according to internal state. |
| **Strategy** | Select algorithm at runtime. |
| **Template Method** | Defines steps of an algorithm, subclasses complete them. |
| **Visitor** | Separates operations from data structures. |

---
## GRASP Patterns

They guide in the **assignment of responsibilities** within object-oriented design.

| Pattern | Description |
|--------|-------------|
| **Information expert** | The class with the appropriate information assumes responsibility. |
| **Creator** | A class is responsible for instantiating another under certain criteria. |
| **Low coupling** | Minimize dependencies between classes. |
| **High cohesion** | Keep classes focused on a single responsibility. |
| **Controller** | Class that manages system events. |
| **Polymorphism** | Use inheritance and interfaces to handle variations. |
| **Don't talk to strangers** | Limit interactions to nearby objects. |

---
## Pattern Examples

### CRUD pattern
- **Complete**: Groups **Create, Read, Update, Delete** into a single use case.  
- **Partial**: Separates simple operations from more complex ones.Advantage: Reduces redundancy and ensures that all 4 operations are covered.

### Adapter Pattern
- **Problem**: Two classes with incompatible interfaces.  
- **Solution**: Create an adapter class that translates calls.  
- **Benefit**: Code reuse without modifying existing implementations.

---

## Diagrams in Modeling

### Key Differences

| Appearance | **Architecture** | **Components (UML)** | **Deployment (UML)** |
|----------|--------|------------------------|-----------------------|
| **Focus** | System Overview | Software logic modules | Physical infrastructure |
| **Level of abstraction** | High | Medium | Low (close to hardware) |
| **What shows** | Layers, modules, relationships | Services, bookstores, packaged classes | Physical nodes and deployed processes |
| **Utility** | Communication with stakeholders | Development and maintenance | Installation and planning |
| **Includes hardware** | ❌ | ❌ | ✅ |
| **Includes code** | Partial | Yes | Tells what is executed, not how |
| **Uses UML** | Optional | ✅ | ✅ |

---
### Applied example (Online education platform)

1. **Architecture**  
   - Users, authentication, streaming, DB, storage, notifications.  

2. **Components**  
   - Frontend, backend with microservices (courses, assignments, grades).  
   - External services (DB, streaming, storage).  

3. **Deployment**  
   - Cloud infrastructure (AWS).  
   - Load balancer + web servers + DB + storage + notifications.