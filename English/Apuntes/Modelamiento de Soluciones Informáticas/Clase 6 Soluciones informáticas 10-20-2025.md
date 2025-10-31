### UML Activity Diagrams

They allow complex processes to be modeled in a system, visualizing the workflow and facilitating the identification of inefficiencies and bottlenecks.

## What is an activity diagram?

An activity diagram is a UML tool that represents the flow of operations and dynamic behavior of a system. It is especially used in the Process View to:
- Model complex processes in a simple way.
- Identify data and control flows.
- Optimize internal processes.

---

## Main elements and symbols (Table)

| Element | Symbol/Notation | Description |
| ----------- | --------------------------- | -------------------------------------------------------------------- |
| Activity | Rounded rectangle | Task or action performed in the system.                              |
| Transition | Arrow | Connection between activities showing the flow of control.            |
| Decision | Diamond | Point where a decision is made in the flow.                        |
| Home | Solid circle | Indicates the start of the diagram.                                       |
| End | Circled circle | Indicates the end of the diagram.                                        |
| Fork | Bar (horizontal/vertical) | Indicates parallel activities (fork) or convergence of flows (join). |
| Object | Rectangle | Indicates an object involved in the process.                          |

---

## Practical example: Payment process

![[Pasted image 20251020111741.png]]

---

## UML views and their relationship

| View | Associated diagram | Brief description |
| ---------------- | ----------------------- | ----------------------------------- |
| Logical View | Class diagram | Static system structure |
| Process view | Activity diagram | Process flow and behavior |
| Development view | Component diagram | Physical software organization |
| Deployment view | Deployment diagram | Physical infrastructure and servers |

---

## Differences between flowchart and activity diagram

| Feature | Flowchart | UML Activity Diagram |
| ---------------- | ------------------ | -------------------------- |
| Orientation | General processes | Object-oriented systems |
| Symbols | Traditional | Standard UML |
| Parallelism | Limited | Supported (fork/join) |
| Level of detail | General | Software specific |
| Decisions | Rhombuses | UML Diamonds |

---

## Steps to build UML activity diagrams

1. Analyze the process: Understand each stage and condition.
2. Identify activities: List all key actions.
3. Determine decisions: Point out points where the flow changes.
4. Define objects/interactions: What resources are involved?
5. Add branches/joins: Mark parallel activities/convergence.
6. Set start and end: Use the appropriate symbols.

---

## Example of symbology in flowcharts

![[Pasted image 20251020111712.png]]