

## Duplicado, Clonación y Camera Tracking

### Presentación de la Scena Base
- Contiene:
  - `VEHICULO` (GameObject principal con Rigidbody y Script `PlayerControl`).
  - `OBSTACULO` (GameObject clonable).

### Duplicado de Objetos
1. Seleccionar `OBSTACULO` en la **Hierarchy**.
2. Usar **CTRL + D** → crea duplicado.  
   - Modificar coordenada `Z` en el **Transform** (+50 unidades).  
3. Repetir duplicado múltiple: ahora **x4 obstáculos** → separados cada 25 unidades (`25, 50, 75, 100...`).

**Marcador importante**: mantener separación exacta de **25 unidades**.

### Traslación grupal de duplicados
- Usar el **gizmo de movimiento** para mover obstáculos en grupo.  
- Repetir hasta tener **x6 obstáculos** alineados.

### Refinamiento de posición
- Ajustar valores en `Transform.Z` desde el **Inspector**.  
- Eliminar objetos fuera del `ROAD`.

### Prueba de colisión de clones
- Presionar **Play** y verificar que los clones hereden parámetros del original.

---

## Scripting: Manejo de variables y Camera Tracking

### Variable `speed`
- Definir en `PlayerController`: controla velocidad del vehículo.
- Inicialmente fija en `Update()`. Ahora → definir **variable pública `speed`**.

 ==`speed` se hace **pública** para manipularla desde el Inspector.

### Script `FollowPlayer`
1. Crear nuevo script `FollowPlayer`.
2. Asignar a **Main Camera** (`Add Component` o arrastrar script).
3. Declarar variable `GameObject player` en el script.

### Vinculación
- En el **Inspector**, arrastrar el `VEHICULO` a la variable `player`.  
- La cámara sigue al vehículo → mejorar posición con `Vector3` para vista cenital o lateral.

## Optimización, Inputs y Movimiento

### Presentación de la Scena Base
- Proyecto cargado con vehículo y obstáculos clonados.
- Componentes:
  - `Rigidbody`
  - `PlayerControl`
  - `FollowPlayer`

### Optimización de Script `FollowPlayer`
- **Problema**: cámara y vehículo se actualizan al mismo tiempo → efecto *stagger*.
- **Solución**: cambiar método `Update()` → `LateUpdate()`.

===`LateUpdate()` asegura suavidad en movimiento de cámara.

### Movimiento Derecha/Izquierda
1. En `PlayerController`, crear variable pública:  
   ```csharp
   public float turnSpeed = 5f;
   ```
2. Capturar input horizontal con `horizontalInput`:
   ```csharp
   horizontalInput = Input.GetAxis("Horizontal");
   ```

==`turnSpeed` se puede ajustar desde el **Inspector**.

### Movimiento Forward/Backward
1. Nueva variable pública:  
   ```csharp
   public float forwardInput;
   ```
2. Capturar input vertical:  
   ```csharp
   forwardInput = Input.GetAxis("Vertical");
   ```
3. Ahora el vehículo avanza solo si presionamos flechas.  

==variables visibles desde Inspector → probar con valores.

### Evitar Slide (efecto deslizamiento)
- Antes: vehículo se movía en eje `X` (deslizar).  
- Ahora: reemplazar por **rotación en Y**.  

### Optimización de Hierarchy
1. Crear **GameObject vacío** → nombrar `OBSTACULOS`.
2. Anidar todos los obstáculos dentro.

### Optimización de Variables
- Cambiar variables de `public` → `private`.  
- Definir por defecto:  
   ```csharp
   private float turnSpeed = 45.0f;
   ```
