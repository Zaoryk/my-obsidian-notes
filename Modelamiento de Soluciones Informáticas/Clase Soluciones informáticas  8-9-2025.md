## Modelamiento de Soluciones Informáticas  
**Área:** Tecnologías De Informacsión Y Ciberseguridad  

---

## Unidad 1: Contenidos
1. Toma de requerimientos  
2. Análisis de requerimientos  
3. Casos de Uso  
4. Diagramas de base de datos  
5. Diagramas de flujo  
6. Lectura: Kanban  

---

## UML – Unified Modeling Language  
### ¿Qué es UML?
- Lenguaje de modelado para **visualizar**, **especificar**, **construir** y **documentar** sistemas software.
- No es propietario, ni un método, ni un proceso.
- Se puede usar en cualquier proceso de desarrollo, ciclo de vida, dominio o plataforma.
- También aplicable en **ingeniería de negocio** y modelado de procesos.

### Orígenes
- Unificación de métodos de modelado de objetos:
  - **Booch**
  - **OMT** (Object Modeling Technique)
  - **OOSE** (Object Oriented Software Engineering)

### Historia
- Versiones desde UML 0.8 hasta **UML 2.5.1** (OMG).
- Estandarización y evolución continua.

---

## Diagramas y Vistas en UML

### Diagramas de Estructura
- Diagrama de clases
- Diagrama de estructuras compuestas
- Diagrama de componentes
- Diagrama de despliegue
- Diagrama de objetos
- Diagrama de paquetes

### Diagramas de Comportamiento
- Diagrama de casos de uso
- Diagrama de actividad
- Diagramas de interacción:
  - Secuencia
  - Colaboración
  - Visión global
  - Tiempo
- Diagrama de estados

---

## Vistas en UML
Cada vista representa un aspecto del sistema mediante subconjuntos de diagramas:

| Vista | Diagramas asociados |
|-------|---------------------|
| Estática | Diagrama de clases |
| Casos de uso | Diagrama de casos de uso |
| Interacción | Diagrama de secuencia, comunicación |
| Actividad | Diagrama de actividad |
| Máquina de estados | Diagrama de estados |
| Diseño | Estructuras compuestas, colaboración, componentes |
| Despliegue | Diagrama de despliegue |
| Gestión del modelo | Diagrama de paquetes |
| Perfiles | Diagrama de paquetes |

---

## Vista de Casos de Uso

### Definición
- Captura la funcionalidad del sistema desde la perspectiva del usuario externo.
- Divide la funcionalidad en transacciones significativas (**casos de uso**).
- Los usuarios se llaman **actores**.

### Componentes principales
- **Escenario**: Sistema que se modela (principal/alternativo).
- **Casos de uso**: Unidades funcionales completas.
- **Actores**: Entidades externas que interactúan.

---

### Actores
- Representan roles de entidades externas.
- Pueden ser humanos, sistemas, dispositivos, temporizadores.
- Notación:
  - Stick man (monigote) + nombre.
  - Clasificador con estereotipo `«actor»`.

#### Tipos de actores
1. **Principales**: Usan servicios del sistema.
2. **De apoyo**: Proporcionan servicios al sistema.
3. **Pasivos**: Interesados en el comportamiento pero no interactúan directamente.

#### Relaciones entre actores
- Solo se asocian con casos de uso, subsistemas, componentes o clases.
- Pueden tener relaciones de **generalización** (herencia).
- Actores abstractos se escriben en *cursiva*.

---

### Casos de Uso
- Conjunto de acciones que producen un resultado observable.
- Se inician por un actor.
- Proporcionan valor a los actores.
- Son completos en funcionalidad.

#### Notación
- Elipse con nombre dentro o debajo.
- Alternativa: clasificador con elipse pequeña en esquina.

---

### Relaciones entre Casos de Uso

| Relación | Símbolo | Descripción |
|----------|---------|-------------|
| Asociación | Línea | Comunicación actor-caso de uso |
| Generalización | Flecha hueca | Especialización de casos de uso |
| Inclusión | `«include»` | Inserción de comportamiento común |
| Extensión | `«extend»` | Comportamiento adicional condicional |
| Realización | Línea punteada | Relación con colaboración que lo implementa |

#### Inclusión
- No condicional.
- Reutiliza comportamiento común.

#### Extensión
- Condicional.
- Añade comportamiento en **puntos de extensión**.
- Se evalúa una condición única.

---

### Organización de Casos de Uso
- Se agrupan en **escenarios** (jerárquicos).
- Pueden pertenecer a múltiples escenarios.
- UML 2 permite que **clasificadores** tengan casos de uso.

---

### Descripción de Casos de Uso
Cada caso de uso debe describirse con:

| Elemento | Descripción |
|----------|-------------|
| Nombre | Identificador del caso de uso |
| Actor principal | Quién inicia la interacción |
| Escenario | Contexto del sistema |
| Interesados | Roles afectados y sus intereses |
| Precondiciones | Condiciones previas |
| Garantías mínimas | Resultados incluso en fallo |
| Escenario principal | Pasos de éxito |
| Excepciones | Flujos alternativos o de error |
| Postcondiciones | Condiciones tras éxito |
| Goal | Objetivo del caso de uso |
| Extensiones | Comportamientos extendidos |

---

### Ejemplo: Validar Usuario Bancario

| Campo | Valor |
|-------|-------|
| Nombre | Validar Usuario Bancario |
| Actor principal | Cliente, Banco, TRANSBANK |
| Escenario | Sistema de cajero automático |
| Interesados | Cliente, Banco, TRANSBANK |
| Precondiciones | Tarjeta válida y operativa |
| Escenario principal | 1. Solicitar tarjeta<br>2. Insertar tarjeta<br>3. Leer código<br>4. Pedir PIN<br>5. Ingresar PIN<br>6. Validar con banco<br>7. Notificar estado |
| Excepciones | E1: Rechazo de validación |
| Postcondiciones | Tarjeta validada |
| Goal | Operación en <30 segundos |
| Extensiones | Consultar saldo, Retirar dinero |

---

### Descripción de Escenarios
Similar a la de casos de uso, pero en formato de **relato** narrativo.