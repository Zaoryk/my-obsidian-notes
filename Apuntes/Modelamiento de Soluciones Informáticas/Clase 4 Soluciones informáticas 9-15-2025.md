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
## Diagramas de Componentes

### ¿Qué es un componente?
- Elemento físico de software: ejecutable, DLL, librería, base de datos, módulo.
- Es la **materialización de clases**.

### Tipos de componentes
| Tipo | Ejemplos |
|------|----------|
| **Distribución** | Ejecutables, DLLs, ActiveX, Java Beans |
| **Trabajo** | Código fuente, bases de datos |
| **Ejecución** | Objetos dinámicos creados en tiempo de ejecución (índices de un buscador, sesiones) |

### Estereotipos UML de componentes
| Estereotipo | Significado |
|-------------|-------------|
| `<<executable>>` | Programa ejecutable |
| `<<library>>` | Biblioteca (estática o dinámica) |
| `<<table>>` | Tabla de base de datos |
| `<<file>>` | Archivo de datos o código |
| `<<document>>` | Documento |

### Interfaces en componentes
- **Provistas/Requeridas** → lo que ofrece y lo que necesita.  
- Se representan como “puertas de entrada/salida”.  
- Permiten **reutilización**: un componente se puede sustituir por otro si cumple la misma interfaz.

---

## Dependencias y Subsistemas

- **Dependencia**: relación donde un componente usa los servicios de otro.
- **Subsistemas**: agrupaciones lógicas de componentes.  
  - Equivalentes a paquetes en nivel lógico.  
  - Se representan con `<<subsystem>>`.

---

## Diagramas de Despliegue

### Concepto
- Muestran la **disposición física** del sistema:  
  - Nodos (servidores, dispositivos, terminales).  
  - Componentes desplegados en cada nodo.  

### Nodos
| Tipo | Descripción |
|------|-------------|
| **Procesador** | Nodo con capacidad de cómputo, ejecuta componentes. |
| **Dispositivo** | Nodo sin cómputo, representa hardware auxiliar. |

### Conexiones entre nodos
- Se modelan como **asociaciones bidireccionales**.  
- Pueden etiquetarse con protocolos: `<<TCP/IP>>`, `<<RDSI>>`, `<<RS-232>>`, etc.

### Relación Nodo ↔ Componente
- Los **componentes** → empaquetamiento físico.  
- Los **nodos** → despliegue físico.  
- Ejemplo:  
  - Nodo servidor despliega `ventas.exe` y `clientes.exe`.  
  - Nodo cliente despliega `user.exe`.

---

## Arquitecturas Multinivel

- **2 niveles** → Cliente/Servidor (cliente hace el trabajo pesado).  
- **3 niveles** → Separación en:  
  1. Presentación  
  2. Lógica de negocio  
  3. Almacenamiento  

Ventajas:  
- Flexibilidad en mantenimiento.  
- Separación clara de responsabilidades.  
- Facilita reutilización.

---

## Puntos Clave del Modelado

- Los **modelos deben ser útiles, simples y elegantes**.  
- Es importante mantener **trazabilidad** entre niveles de abstracción.  
- Apostar por **orientación a objetos con UML**.  
- Posibles mejoras futuras:  
  - **Evolución**: uso de bases de datos orientadas a objetos.  
  - **Revolución**: generación automática de código a partir de modelos (MDA, Model Driven Architecture).
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

## Bibliografía Recomendada
- Martin Fowler – *UML Distilled (UML Gota a Gota)*  
- Pierre-Alain Muller – *Instant UML*  
- Terry Quatrani – *Visual Modeling*  
- Recursos UML: [OMG UML](https://www.omg.org/spec/UML/)  
