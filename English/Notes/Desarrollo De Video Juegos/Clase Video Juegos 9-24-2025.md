## Unity - Player Control (Part 1)
### Objects, Camera, Movement and Collision

---
## Progress Checklist

### Project Configuration
- [x] Create new 3D project in Unity Hub
- [x] Select template "3D Core"
- [x] Define project name and location
- [x] Wait for complete loading of the project
- [x] Import course assets (Unity Package)

### Scene Settings
- [x] Open scene "PROTOTYPE 1"
- [x] Delete empty scene "SAMPLESCENE"
- [x] Add vehicle from Course Library > Vehicles
- [x] Add obstacle from Course Library > Obstacles
- [x] Rename Game Objects appropriately

### Object Positioning
- [x] Position obstacle 25 meters in front of the vehicle
- [x] Adjust transformations using Inspector
- [x] Remember: 1 Unity unit = 1 meter

### Camera Settings
- [x] Select MAIN CAMERA in Hierarchy
- [x] Reposition camera behind the vehicle
- [x] Adjust rotation for third person view
- [x] Use rotation tool (green gizmo)
- [x] Check view in GAME tab

### Scripting and Programming
- [x] Create "SCRIPTS" folder in Assets
- [x] Create C# script "PlayerController" (camelCase)
- [x] Drag script to the vehicle's Game Object
- [x] Edit script in Visual Studio

---
### Initial Steps
1. Open Unity Hub → "Projects" tab
2. Click "New Project"
3. Select template: "3D Core"
4. Project name: "N4 – PlayerControl" (or choose name)
5. Define location: Previously created folder
6. Wait for loading (may take several minutes)

### Asset Import
- Download Course Starter Files
- Unzip to project folder
- In Unity: Assets > Import Package > Custom Package
- Select .unitypackage file
- Click "Import"

---
### Game Objects in Hierarchy
- Vehicle: Drag from COURSE LIBRARY > VEHICLES
- Obstacle: Drag from COURSE LIBRARY > OBSTACLES
- MAIN CAMERA: Player's main camera

### Position Adjustments
 
 
``` Obstáculo  : 25 unidades en Z (frente al vehículo)
Transform obstacleTransform = obstacle.GetComponent<Transform>();
obstacleTransform.position = new Vector3(0, 0, 25);
```

---

## Camera Settings

### Player View
1. Double click on MAIN CAMERA in Hierarchy
2. Use Move Tool (W key)
3. Position behind the vehicle
4. Use Rotate Tool (E key)
5. Adjust angle for third person view

### Transformation Tools
- Move (W): Translation in X, Y, Z axes
- Rotate (E): Rotation in axes
- Scale (R): Scale (not used for camera)
- Rect Transform (T): For UI

### Third Person View
- Camera behind the vehicle
- Angled slightly downwards
- Check in GAME tab

---

## PlayerController programming

### Script Creation
In SCRIPTS folder: Right click > Create > C# Script
Name: PlayerController (camelCase)

### Basic Movement Code
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

### Code Explanation
- Vector3.forward: Forward direction (Z axis)
- speed: Speed in units/second (20 m/s)
- Time.deltaTime: Time between frames → smooth movement
- Frame-rate independence: Same speed on any hardware

---

## Physics and Collisions

### Rigidbody component
To enable physical collisions:

Vehicle:
1. Select vehicle in Hierarchy
2. Inspector → Add Component → Physics → Rigidbody
3. Set Mass: 2000 kg (example)

Obstacle:
1. Select obstacle in Hierarchy
2. Add Component → Rigidbody
3. Set Mass: 20 kg (example)

### Rigidbody Properties
- Mass: Mass of the object (kg)
- Drag: Resistance to movement
- Angular Drag: Rotation resistance
- Use Gravity: Apply gravity (on)

---

## Tests and Adjustments

### Important Verifications
- [x] Vehicle automatically moves forward
- [x] Movement is smooth and constant (20 m/s)
- [x] Camera follows the vehicle in third person
- [x] Collision between vehicle and obstacle works
- [x] Obstacle reacts to impact (physics)

### Common Problem Solving
Irregular Movement
Ensure use of Time.deltaTime

```
transform.Translate(Vector3.forward * speed * Time.deltaTime);
```

No Collision- Verify that both objects have Rigidbody
- Verify that they are not Triggers
- Check Mass of objects

Camera Does Not Follow
- Make sure which camera is the vehicle's camera
- Or implement tracking script

---

## Asynchronous Practical Activity

### Objective
Simulate collision of two moving vehicles

### Requirements
- [x] Two vehicles with PlayerController
- [x] Different speeds and masses
- [x] Frontal or side collision
- [x] Visible physical effects

### Extended Code for Two Vehicles

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