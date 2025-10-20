
### Diagramas de Actividad UML

Permiten modelar procesos complejos en un sistema, visualizando el flujo de trabajo y facilitando la identificación de ineficiencias y cuellos de botella.

## ¿Qué es un diagrama de actividad?

Un diagrama de actividad es una herramienta UML que representa el flujo de operaciones y el comportamiento dinámico de un sistema. Se usa especialmente en la Vista de Procesos para:
- Modelar procesos complejos de forma sencilla.
- Identificar flujos de datos y control.
- Optimizar procesos internos.

---

## Elementos principales y simbología (Tabla)

| Elemento    | Símbolo/Notación            | Descripción                                                          |
| ----------- | --------------------------- | -------------------------------------------------------------------- |
| Actividad   | Rectángulo redondeado       | Tarea o acción realizada en el sistema.                              |
| Transición  | Flecha                      | Conexión entre actividades mostrando el flujo de control.            |
| Decisión    | Diamante                    | Punto donde se toma una decisión en el flujo.                        |
| Inicio      | Círculo sólido              | Indica el inicio del diagrama.                                       |
| Fin         | Círculo circundado          | Indica el final del diagrama.                                        |
| Bifurcación | Barra (horizontal/vertical) | Indica actividades paralelas (fork) o convergencia de flujos (join). |
| Objeto      | Rectángulo                  | Indica un objeto involucrado en el proceso.                          |

---

## Ejemplo práctico: Proceso de pago

![[Pasted image 20251020111741.png]]

---

## Vistas UML y su relación

| Vista            | Diagrama asociado       | Descripción breve                   |
| ---------------- | ----------------------- | ----------------------------------- |
| Vista lógica     | Diagrama de clases      | Estructura estática del sistema     |
| Vista proceso    | Diagrama de actividad   | Flujo de procesos y comportamiento  |
| Vista desarrollo | Diagrama de componentes | Organización física de software     |
| Vista despliegue | Diagrama de despliegue  | Infraestructura física y servidores |

---

## Diferencias entre diagrama de flujo y diagrama de actividad

| Característica   | Diagrama de flujo  | Diagrama de actividad UML     |
| ---------------- | ------------------ | ----------------------------- |
| Orientación      | Procesos generales | Sistemas orientados a objetos |
| Símbolos         | Tradicionales      | UML estándar                  |
| Paralelismo      | Limitado           | Soportado (fork/join)         |
| Nivel de detalle | General            | Específico para software      |
| Decisiones       | Rombos             | Diamantes UML                 |

---

## Pasos para construir diagramas de actividad UML

1. Analizar el proceso: Entiende cada etapa y condición.
2. Identificar actividades: Lista todas las acciones clave.
3. Determinar decisiones: Señala puntos donde cambia el flujo.
4. Definir objetos/interacciones: ¿Qué recursos intervienen?
5. Agregar bifurcaciones/uniones: Marca actividades paralelas/convergencia.
6. Establecer inicio y fin: Usa los símbolos apropiados.

---

## Ejemplo de simbología en diagramas de flujo

![[Pasted image 20251020111712.png]]