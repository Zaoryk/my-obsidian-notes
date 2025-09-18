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

# INFORMACION EXTRA

---
## Patrones de Diseño

### ¿Qué son?
- Soluciones probadas a problemas recurrentes en desarrollo.
- Nacieron en los 70s, popularizados por el libro **Design Patterns (GoF, 1994)**.
- Beneficios:
  1. **Ahorro de tiempo** → no reinventar la rueda.  
  2. **Seguridad y estabilidad** → ya probados por la comunidad.  
  3. **Lenguaje común** → facilita comunicación entre desarrolladores.

---
## Tipos de Patrones de Diseño (GoF)

### 1. Patrones Creacionales
Simplifican la **creación de objetos** y desacoplan la forma de crearlos de la lógica del software.

| Patrón | Descripción |
|--------|-------------|
| **Abstract Factory** | Interfaz para crear familias de objetos relacionados. |
| **Factory Method** | Las subclases deciden cómo instanciar objetos. |
| **Builder** | Separa creación y estructura, permite distintos productos con mismo proceso. |
| **Singleton** | Asegura que solo exista una instancia global. |
| **Prototype** | Clona objetos existentes como plantillas. |

---
### 2. Patrones Estructurales
Definen cómo se relacionan las clases/objetos entre sí.

| Patrón | Descripción |
|--------|-------------|
| **Adapter** | Permite compatibilidad entre interfaces distintas. |
| **Bridge** | Separa abstracción e implementación para evolucionar por separado. |
| **Composite** | Estructuras jerárquicas tipo árbol. |
| **Decorator** | Añade responsabilidades a objetos dinámicamente. |
| **Facade** | Proporciona interfaz simplificada a subsistemas complejos. |
| **Flyweight** | Reduce uso de memoria compartiendo objetos pesados. |
| **Proxy** | Representa a otro objeto (ej. acceso remoto, diferido). |

---
### 3. Patrones de Comportamiento
Gestionan algoritmos, comunicación y responsabilidades.

| Patrón | Descripción |
|--------|-------------|
| **Command** | Encapsula una operación en un objeto. |
| **Chain of Responsibility** | Mensajes pasan por cadena hasta ser manejados. |
| **Interpreter** | Define gramáticas y procesamiento de expresiones. |
| **Iterator** | Itera sobre colecciones sin exponer su estructura. |
| **Mediator** | Centraliza la comunicación entre objetos. |
| **Memento** | Permite restaurar el estado previo de un objeto. |
| **Observer** | Notifica cambios a objetos suscritos. |
| **State** | Modifica el comportamiento según estado interno. |
| **Strategy** | Selecciona algoritmo en tiempo de ejecución. |
| **Template Method** | Define pasos de un algoritmo, subclases los completan. |
| **Visitor** | Separa operaciones de las estructuras de datos. |

---
## Patrones GRASP

Guían en la **asignación de responsabilidades** dentro del diseño orientado a objetos.

| Patrón | Descripción |
|--------|-------------|
| **Experto en información** | La clase con la info adecuada asume la responsabilidad. |
| **Creador** | Una clase es responsable de instanciar otra bajo ciertos criterios. |
| **Bajo acoplamiento** | Minimizar dependencias entre clases. |
| **Alta cohesión** | Mantener clases enfocadas en una sola responsabilidad. |
| **Controlador** | Clase que gestiona eventos del sistema. |
| **Polimorfismo** | Usar herencia e interfaces para manejar variaciones. |
| **No hables con extraños** | Limitar interacciones a objetos cercanos. |

---
## Ejemplos de Patrones

### Patrón CRUD
- **Completo**: Agrupa **Create, Read, Update, Delete** en un solo caso de uso.  
- **Parcial**: Separa operaciones simples de las más complejas.  

Ventaja: Reduce redundancia y asegura que las 4 operaciones estén contempladas.

### Patrón Adapter
- **Problema**: Dos clases con interfaces incompatibles.  
- **Solución**: Crear una clase adaptadora que traduce llamadas.  
- **Beneficio**: Reutilización de código sin modificar implementaciones existentes.

---

## Diagramas en Modelamiento

### Diferencias Clave

| Aspecto | **Arquitectura** | **Componentes (UML)** | **Despliegue (UML)** |
|----------|------------------|------------------------|-----------------------|
| **Enfoque** | Visión general del sistema | Módulos lógicos de software | Infraestructura física |
| **Nivel de abstracción** | Alto | Medio | Bajo (cercano al hardware) |
| **Qué muestra** | Capas, módulos, relaciones | Servicios, librerías, clases empaquetadas | Nodos físicos y procesos desplegados |
| **Utilidad** | Comunicación con stakeholders | Desarrollo y mantenimiento | Instalación y planificación |
| **Incluye hardware** | ❌ | ❌ | ✅ |
| **Incluye código** | Parcial | Sí | Indica qué se ejecuta, no cómo |
| **Usa UML** | Opcional | ✅ | ✅ |

---
### Ejemplo aplicado (Plataforma de educación online)

1. **Arquitectura**  
   - Usuarios, autenticación, streaming, DB, almacenamiento, notificaciones.  

2. **Componentes**  
   - Frontend, backend con microservicios (cursos, tareas, calificaciones).  
   - Servicios externos (DB, streaming, almacenamiento).  

3. **Despliegue**  
   - Infraestructura en la nube (AWS).  
   - Balanceador de carga + servidores web + DB + almacenamiento + notificaciones.