# Paradigma 4+1 y Diagramas de Base de Datos

---
## Paradigma 4+1
![[Pasted image 20250915104623.png]]
![[Pasted image 20250915110407.png]]
### Conceptos
- **Vista**: Representación del sistema desde una perspectiva.  
- **Punto de vista**: Conjunto de reglas para interpretar las vistas.  

Propuesto por **Philippe Kruchten** (IEEE 1471-000).  
Define **4 vistas + 1 escenario** para describir un sistema software.  

### Vistas del Paradigma 4+1
| Vista                               | Propósito                                                | Diagramas típicos                               |
| ----------------------------------- | -------------------------------------------------------- | ----------------------------------------------- |
| **Lógica**                          | Estructura estática del sistema y relaciones de objetos. | Diagramas de clases, comunicación, secuencia.   |
| **Proceso (operacional)**           | Procesos concurrentes, comunicación, sincronización.     | Diagramas de actividad, interacción.            |
| **Desarrollo (física de software)** | Organización del software, componentes.                  | Diagramas de componentes.                       |
| **Física (infraestructura)**        | Distribución en hardware y nodos de ejecución.           | Diagramas de despliegue.                        |
| **Escenarios (+1)**                 | Casos de uso que integran las 4 vistas.                  | Diagramas de casos de uso, ejemplos narrativos. |

---
## Vista de Escenarios
![[Pasted image 20250915104856.png]]
- Describe cómo interactúa un usuario con el sistema.  
- Ejemplo: Cliente en comercio electrónico → login → compra → confirmación → envío.  

---

## Vista Lógica – Diagramas
- **Diagramas de clase**: relaciones entre objetos, atributos, métodos.  
- **Diagramas de comunicación**: interacción entre objetos.  
- **Diagramas de secuencia**: orden temporal de mensajes entre objetos.  

### Notación de Clase en UML
| Zona     | Contenido                                     |
| -------- | --------------------------------------------- |
| Superior | Nombre de la clase (cursiva si es abstracta). |
| Media    | Atributos (ej: `+nombre: String`).            |
| Inferior | Métodos (ej: `+getNombre(): String`).         |

### Visibilidad
| Símbolo | Tipo      | Descripción                        |
| ------- | --------- | ---------------------------------- |
| `+`     | Público   | Accesible desde cualquier parte.   |
| `-`     | Privado   | Accesible solo desde la clase.     |
| `#`     | Protegido | Accesible desde clase y subclases. |
| `/`     | Derivado  | Calculado.                         |
| `~`     | Paquete   | Accesible en el mismo paquete.     |

==Los atributos o métodos estáticos se subrayan.  ==

---

## Relaciones en UML
| Tipo | Descripción |
|------|-------------|
| **Asociación** | Relación genérica entre clases. |
| **Agregación** | Relación “tiene un”, pero débil (ej: Curso–Alumno). |
| **Composición** | Relación fuerte, ciclo de vida dependiente (ej: Casa–Habitación). |
| **Dependencia** | Un cambio en una clase afecta a otra. |
| **Herencia** | Una clase hija hereda atributos/métodos de la clase padre. |

### Multiplicidad (Cardinalidad)
Ejemplo:  
- `1..*` → Una clase puede estar asociada a muchos objetos de otra.  
- `0..1` → Una clase puede no estar asociada, o solo a un objeto.  

### Bidireccionalidad
- Relación navegable en ambos sentidos.  
- Ejemplo: **Usuario ↔ Préstamo**.  
- Dependencia: **Notificador → Usuario** (no bidireccional).  

---

## Mapeo UML → Modelo Relacional
Pasos sugeridos:
1. Modelar clases.  
2. Identificar objetos persistentes.  
3. Mapear clases a tablas.  
4. Seleccionar estrategia de herencia.  
5. Definir identificador único (PK).  
6. Mapear atributos a columnas.  
7. Mapear asociaciones a claves foráneas.  
8. Definir roles de relación.  
9. Modelar comportamiento.  
10. Crear modelo físico.  

==En UML, una tabla se representa como clase con estereotipo ==`«Table»`. 

---

## Patrones de Diseño

### Definición
- Soluciones reutilizables para problemas comunes de diseño software.  
- Funcionan como **plantillas** aplicables en distintos contextos.  

### Tipos
| Grupo | Características |
|-------|----------------|
| **GRASP** (General Responsibility Assignment Software Patterns) | Principios de DOO → ayudan a decidir responsabilidades. Ejemplos: Controlador, Experto, Alta Cohesión, Bajo Acoplamiento, Indirección, Fabricación Pura. |
| **GoF** (Gang of Four) | Soluciones implementables → cada patrón incluye su propio diagrama de clases. Ejemplos: Singleton, Factory, Observer, Decorator, Adapter. |

---

# Resumen Visual

### Paradigma 4+1
- Vista Lógica → estructura y clases.  
- Vista de Proceso → concurrencia y flujo.  
- Vista de Desarrollo → organización en componentes.  
- Vista Física → despliegue en hardware.  
- Vista de Escenarios → casos de uso.  

### UML y BD
- Clases = estructuras con atributos y métodos.  
- Relaciones: asociación, agregación, composición, dependencia, herencia.  
- Cardinalidad: 1..1, 1..*, 0..1, etc.  
- Mapeo UML → Tablas, PK, FK.  

### Patrones de Diseño
- GRASP: principios de asignación de responsabilidades.  
- GoF: patrones clásicos implementables (Factory, Singleton, Observer, etc.).  
