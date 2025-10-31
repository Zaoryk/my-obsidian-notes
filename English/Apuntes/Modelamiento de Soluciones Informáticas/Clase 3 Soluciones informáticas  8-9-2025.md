## Modeling of IT Solutions  
**Area:** Information Technologies and Cybersecurity  

---

## Unit 1: Contents
1. Requirements gathering  
2. Requirements analysis  
3. Use Cases  
4. Database diagrams  
5. Flowcharts  
6. Reading: Kanban  

---

## UML – Unified Modeling Language  
### What is UML?
- Modeling language to **visualize**, **specify**, **build** and **document** software systems.
- It is not proprietary, nor a method, nor a process.
- Can be used in any development process, life cycle, domain or platform.
- Also applicable in **business engineering** and process modeling.

### Origins
- Unification of object modeling methods:
  - **Booch**
  - **OMT** (Object Modeling Technique)
  - **OOSE** (Object Oriented Software Engineering)

### History
- Versions from UML 0.8 to **UML 2.5.1** (OMG).
- Standardization and continuous evolution.

---

## Diagrams and Views in UML

### Structure Diagrams
- Class diagram
- Diagram of composite structures
- Component diagram
- Deployment diagram
- Object diagram
- Package diagram

### Behavior Diagrams
- Use case diagram
- Activity diagram
- Interaction diagrams:
  - Sequence
  - Collaboration
  - Global vision
  - Time
- State diagram

---

## Views in UML
Each view represents an aspect of the system using subsets of diagrams:

| View | Associated diagrams |
|-------|----------|
| Static | Class diagram |
| Use cases | Use case diagram |
| Interaction | Sequence diagram, communication |
| Activity | Activity diagram |
| State machine | State diagram |
| Design | Composite structures, collaboration, components |
| Deployment | Deployment diagram |
| Model management | Package diagram |
| Profiles | Package diagram |

---

## Use Case View

### Definition
- Captures system functionality from the external user's perspective.
- Divide functionality into meaningful transactions (**use cases**).
- Users are called **actors**.

### Main components
- **Scenario**: System that is modeled (main/alternative).
- **Use cases**: Complete functional units.
- **Actors**: External entities that interact.

---

### Actors
- They represent roles of external entities.
- They can be humans, systems, devices, timers.
- Notation:
  - Stick man (stickman) + name.
  - Classifier with stereotype `«actor»`.

#### Types of actors
1. **Main**: They use system services.
2. **Support**: They provide services to the system.
3. **Passive**: Interested in the behavior but do not interact directly.

#### Relationships between actors
- They are only associated with use cases, subsystems, components or classes.
- They can have **generalization** relationships (inheritance).
- Abstract actors are written in *italics*.

---

### Use Cases
- Set of actions that produce an observable result.
- They are started by an actor.
- They provide value to actors.
- They are complete in functionality.

#### Notation
- Ellipse with name inside or below.
- Alternative: classifier with small ellipse in the corner.

---

### Relationships between Use Cases

| Relationship | Symbol | Description |
|----------|---------|-------------|
| Association | Line | Actor-use case communication |
| Generalization | Hollow arrow | Use case specialization |
| Inclusion | `«include»` | Common Behavior Insertion |
| Extension | `«extend»` | Conditional additional behavior |
| Realization | Dotted line | Relationship with collaboration that implements it |

#### Inclusion
- Not conditional.
- Reuse common behavior.

#### Extension
- Conditional.
- Add behavior at **extension points**.
- A single condition is evaluated.

---

### Use Case Organization- They are grouped into **scenarios** (hierarchical).
- They can belong to multiple scenarios.
- UML 2 allows **classifiers** to have use cases.

---

### Description of Use Cases
Each use case should be described with:

| Element | Description |
|----------|-------------|
| Name | Use case identifier |
| Main actor | Who initiates the interaction |
| Scenario | System context |
| Interested | Affected roles and their interests |
| Preconditions | Preconditions |
| Minimum guarantees | Results even in failure |
| Main stage | Success steps |
| Exceptions | Alternative or error flows |
| Postconditions | Conditions after success |
| Goal | Use case objective |
| Extensions | Extended behaviors |

---

### Example: Validate Bank User

| Field | Value |
|-------|-------|
| Name | Validate Banking User |
| Main actor | Client, Bank, TRANSBANK |
| Scenario | ATM system |
| Interested | Client, Bank, TRANSBANK |
| Preconditions | Valid and operational card |
| Main stage | 1. Request card<br>2. Insert card<br>3. Read code<br>4. Request PIN<br>5. Enter PIN<br>6. Validate with bank<br>7. Notify status |
| Exceptions | E1: Validation rejection |
| Postconditions | Validated card |
| Goal | Operation in <30 seconds |
| Extensions | Check balance, Withdraw money |