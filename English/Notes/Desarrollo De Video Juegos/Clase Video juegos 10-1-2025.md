## Duplicate, Cloning and Camera Tracking

### Presentation of the Base Scene
- Contains:
  - `VEHICULO` (main GameObject with Rigidbody and Script `PlayerControl`).
  - `OBSTACULO` (clonable GameObject).

### Duplicate Objects
1. Select `OBSTACULO` in the **Hierarchy**.
2. Use **CTRL + D** → create duplicate.  
   - Modify `Z` coordinate in the **Transform** (+50 units).  
3. Repeat multiple duplicate: now **x4 obstacles** → spaced every 25 units (`25, 50, 75, 100...`).

**Important marker**: maintain exact separation of **25 units**.

### Group translation of duplicates
- Use the **movement gizmo** to move obstacles as a group.  
- Repeat until you have **x6 obstacles** lined up.

### Position refinement
- Adjust values in `Transform.Z` from **Inspector**.  
- Delete objects outside the `ROAD`.

### Clone collision test
- Press **Play** and verify that the clones inherit parameters from the original.

---

## Scripting: Variable management and Camera Tracking

### Variable `speed`
- Define in `PlayerController`: controls vehicle speed.
- Initially set to `Update()`. Now → define **public variable `speed`**.

 ==`speed` is made **public** to be manipulated from the Inspector.

### Script `FollowPlayer`
1. Create new script `FollowPlayer`.
2. Assign to **Main Camera** (`Add Component` or drag script).
3. Declare variable `GameObject player` in the script.

### Linking
- In the **Inspector**, drag the `VEHICULO` to the variable `player`.  
- The camera follows the vehicle → improve position with `Vector3` for overhead or side view.

## Optimization, Inputs and Movement

### Presentation of the Base Scene
- Project loaded with cloned vehicle and obstacles.
- Components:
  - `Rigidbody`
  - `PlayerControl`
  - `FollowPlayer`

### Script Optimization `FollowPlayer`
- **Problem**: camera and vehicle update at the same time → *stagger* effect.
- **Solution**: change method `Update()` → `LateUpdate()`.

=_`LateUpdate()` ensures smoothness in camera movement.

### Right/Left Movement
1. In `PlayerController`, create public variable:  
   
```csharp
   public float turnSpeed = 5f;
   ```

2. Capture horizontal input with `horizontalInput`:
   
```csharp
   horizontalInput = Input.GetAxis("Horizontal");
   ```


==`turnSpeed` can be set from the **Inspector**.

### Forward/Backward Movement
1. New public variable:  
   
```csharp
   public float forwardInput;
   ```

2. Capture vertical input:  
   
```csharp
   forwardInput = Input.GetAxis("Vertical");
   ```

3. Now the vehicle moves forward only if we press arrows.  

==variables visible from Inspector → test with values.

### Avoid Slide
- Before: vehicle moved on axis `X` (slide).  
- Now: replace with **Y rotation**.  

### Hierarchy Optimization
1. Create **empty GameObject** → name `OBSTACULOS`.
2. Nest all obstacles inside.

### Variable Optimization
- Change variables from `public` → `private`.  
- Define by default:  
   
```csharp
   private float turnSpeed = 45.0f;
   ```