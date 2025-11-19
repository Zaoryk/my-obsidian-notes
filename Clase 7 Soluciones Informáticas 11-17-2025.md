## 1. ¿Qué es BPMN?

BPMN (Business Process Model and Notation) es un estándar gráfico para modelar procesos de negocio. Su objetivo es permitir una comunicación clara entre analistas, técnicos y responsables de negocio mediante diagramas accesibles y estandarizados.  

---
## 2. Objetos principales de BPMN
### Objetos de Flujo

- **Actividades**  
  Representan trabajo que debe realizarse.  
  - *Tareas*: unidades mínimas de trabajo.  
  - *Subprocesos*: actividades compuestas que pueden expandirse o colapsarse.  
  
- **Eventos**  
  Momentos que inician, interrumpen o finalizan el proceso.  
  Ejemplos: inicio, fin, mensaje, temporizador, error, señal.

- **Gateways (Compuertas)**  
  Permiten tomar decisiones o dividir caminos.  
  - Exclusiva (XOR)  
  - Inclusiva (OR)  
  - Paralela (AND)  
  - Basada en eventos  

### Conectores

- **Flujo de Secuencia** → Orden de las actividades.  
- **Flujo de Mensaje** → Comunicación entre pools.  
- **Asociación** → Relación con artefactos.
### Swimlanes (Responsabilidades)

- **Pool**: entidad o proceso completo.  
- **Lane**: roles, áreas o actores dentro del pool.

### Artefactos

- Objetos de datos  
- Depósitos de datos  
- Grupos  
- Anotaciones
---
## 3. Subprocesos

- **Embebidos**: pertenecen al proceso padre.  
- **Reusables**: se pueden invocar desde múltiples procesos.  
- **Paralelos o secuenciales**: múltiples instancias del mismo subproceso.
