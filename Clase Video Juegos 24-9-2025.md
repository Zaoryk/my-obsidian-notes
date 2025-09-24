## Unity - Player Control (Parte 1)
### Objetos, Cámara, Desplazamiento y Colisión

---

## Checklist de Progreso

### Configuración del Proyecto
- [x] Crear nuevo proyecto 3D en Unity Hub
- [x] Seleccionar template "3D Core"
- [x] Definir nombre y ubicación del proyecto
- [x] Esperar carga completa del proyecto
- [x] Importar assets del curso (Unity Package)

### Configuración de la Escena
- [x] Abrir escena "PROTOTYPE 1"
- [x] Eliminar escena vacía "SAMPLESCENE"
- [x] Agregar vehículo desde Course Library > Vehicles
- [x] Agregar obstáculo desde Course Library > Obstacles
- [x] Renombrar Game Objects apropiadamente

### Posicionamiento de Objetos
- [x] Posicionar obstáculo 25 metros delante del vehículo
- [x] Ajustar transformaciones usando Inspector
- [x] Recordar: 1 unidad Unity = 1 metro

### Configuración de Cámara
- [x] Seleccionar MAIN CAMERA en Hierarchy
- [x] Reposicionar cámara detrás del vehículo
- [x] Ajustar rotación para vista en tercera persona
- [x] Usar herramienta de rotación (gizmo verde)
- [x] Verificar vista en pestaña GAME

### Scripting y Programación
- [x] Crear carpeta "SCRIPTS" en Assets
- [x] Crear script C# "PlayerController" (camelCase)
- [x] Arrastrar script al Game Object del vehículo
- [x] Editar script en Visual Studio

---

## Creación del Proyecto

### Pasos Iniciales
1. Abrir Unity Hub → Pestaña "Projects"
2. Click "New Project"
3. Seleccionar template: "3D Core"
4. Nombre del proyecto: "N4 – PlayerControl" (o elegir nombre)
5. Definir ubicación: Carpeta previamente creada
6. Esperar carga (puede tomar varios minutos)

### Importación de Assets
- Descargar Starter Files del curso
- Descomprimir en carpeta del proyecto
- En Unity: Assets > Import Package > Custom Package
- Seleccionar archivo .unitypackage
- Click "Import"

---

## Configuración de la Escena


### Game Objects en Hierarchy
- Vehículo: Arrastrar desde COURSE LIBRARY > VEHICLES
- Obstáculo: Arrastrar desde COURSE LIBRARY > OBSTACLES
- MAIN CAMERA: Cámara principal del jugador

### Ajustes de Posición
 
 ``` Obstáculo  : 25 unidades en Z (frente al vehículo)
Transform obstacleTransform = obstacle.GetComponent<Transform>();
obstacleTransform.position = new Vector3(0, 0, 25);
```
---

## Configuración de la Cámara

### Vista del Jugador
1. Doble click en MAIN CAMERA en Hierarchy
2. Usar herramienta Move (tecla W)
3. Posicionar detrás del vehículo
4. Usar herramienta Rotate (tecla E)
5. Ajustar ángulo para vista en tercera persona

### Herramientas de Transformación
- Move (W): Traslación en ejes X, Y, Z
- Rotate (E): Rotación en ejes
- Scale (R): Escala (no usado para cámara)
- Rect Transform (T): Para UI

### Vista en Tercera Persona
- Cámara detrás del vehículo
- Angulada ligeramente hacia abajo
- Verificar en pestaña GAME

---

## Programación del PlayerController

### Creación del Script
En carpeta SCRIPTS: Click derecho > Create > C# Script
Nombre: PlayerController (camelCase)

### Código Básico de Movimiento
using UnityEngine;

```
public class PlayerController : MonoBehaviour
{
    public float speed = 20.0f;
    
    void Update()
    {
        // Movimiento hacia adelante en eje Z
        // Time.deltaTime para frame-rate independence
        transform.Translate(Vector3.forward * speed * Time.deltaTime);
    }
}
```
### Explicación del Código
- Vector3.forward: Dirección hacia adelante (eje Z)
- speed: Velocidad en unidades/segundo (20 m/s)
- Time.deltaTime: Tiempo entre frames → movimiento suave
- Frame-rate independence: Misma velocidad en cualquier hardware

---

## Físicas y Colisiones

### Componente Rigidbody
Para habilitar colisiones físicas:

Vehículo:
1. Seleccionar vehículo en Hierarchy
2. Inspector → Add Component → Physics → Rigidbody
3. Configurar Mass: 2000 kg (ejemplo)

Obstáculo:
1. Seleccionar obstáculo en Hierarchy
2. Add Component → Rigidbody
3. Configurar Mass: 20 kg (ejemplo)

### Propiedades de Rigidbody
- Mass: Masa del objeto (kg)
- Drag: Resistencia al movimiento
- Angular Drag: Resistencia a la rotación
- Use Gravity: Aplicar gravedad (activado)

---

##  Pruebas y Ajustes

### Verificaciones Importantes
- [x] Vehículo se mueve automáticamente hacia adelante
- [x] Movimiento es suave y constante (20 m/s)
- [x] Cámara sigue al vehículo en tercera persona
- [x] Colisión entre vehículo y obstáculo funciona
- [x] Obstáculo reacciona al impacto (física)

### Solución de Problemas Comunes
Movimiento Irregular
Asegurar uso de Time.deltaTime
```
transform.Translate(Vector3.forward * speed * Time.deltaTime);
```
Sin Colisión
- Verificar que ambos objetos tengan Rigidbody
- Verificar que no sean Triggers
- Revisar Mass de los objetos

Cámara No Sigue
- Asegurar que cámara es child del vehículo
- O implementar script de seguimiento

---

## Actividad Práctica Asincrónica

### Objetivo
Simular choque de dos vehículos en movimiento

### Requisitos
- [x] Dos vehículos con PlayerController
- [x] Diferentes velocidades y masas
- [x] Colisión frontal o lateral
- [x] Efectos físicos visibles

### Código Extendido para Dos Vehículos
```
public class VehicleController : MonoBehaviour
{
    public float speed = 20.0f;
    public bool isMoving = true;
    
    void Update()
    {
        if (isMoving)
        {
            transform.Translate(Vector3.forward * speed * Time.deltaTime);
        }
    }
    
    void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.CompareTag("Vehicle"))
        {
            // Detener movimiento al chocar
            isMoving = false;
        }
    }
}
```
---