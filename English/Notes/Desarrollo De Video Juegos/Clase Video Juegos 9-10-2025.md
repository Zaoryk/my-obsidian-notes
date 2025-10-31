## Introduction to Unity (Video Game Engine)

### What is Unity?
- Generic engine to create 2D and 3D video games.  
- Smooth learning curve (simpler than Unreal Engine).  
- Ideal for prototyping and rapid development.  
- Editions:  
  - **Personal**: Free, all functions, for income < $100,000 annually.  
  - **Professional**: Subscription $75/month or one-time payment $1500.  
- Export to: iOS, Android, Windows Phone, WebGL, PS4, Xbox, Wii U, Mac, Windows, Linux.  

---

## Unity Editor Environment

| Dashboard | Function |
|-------|--------|
| **Project** | Contains all resources (assets: textures, audios, scripts, scenes). |
| **Hierarchy** | Object tree of the current scene. |
| **Scene** | Visual view of the scene (2D/3D). |
| **Inspector** | Shows and edits properties of the selected object or asset. |

---

## 3D Scene and Objects

- Empty or predefined objects (Cube, Sphere, Capsule, Plane) can be added.  
- Basic objects include components:  

| Component | Function |
|---------|---------|
| **Transform** | Position, rotation and scale in the scene. |
| **Renderer** | Renders the object on the screen with its material/mesh. |
| **Collider** | Defines collision geometry (e.g. Box Collider). |

---

## Object Transformations
- **Translation**: move in X, Y, Z axes.  
- **Rotation**: rotations on the three axes.  
- **Scaling**: change size on each axis.  

---

## Scene Navigation
- **View an object**: double click on Hierarchy.  
- **Alignment with object**: `GameObject > Align View To Selected`.  

---

## Object Hierarchy
- Drag objects in **Hierarchy** → parent-child relationships.  
- Empty objects are used to group.  
- Give meaningful names for the organization.  

---

## Component Oriented Architecture
- All objects are **GameObjects**.  
- Functionality depends on added components.  
- Camera example:  
  - Transform (position)  
  - Camera (renders scene)  
  - GUILayer (on-screen GUI)  
  - FlareLayer (flare effect)  
  - AudioListener (capture sound)  

---

## Key Concepts in Unity

| Concept | Definition |
|----------|------------|
| **Assets** | Resources used in the project (textures, models, audios, scripts, etc.). |
| **Prefabs** | Collections of configured and reusable GameObjects. Changes in prefab → apply to all its instances. |
| **Asset Packages** | Exportable/importable collections (standard or custom). |
| **Asset Store** | Unity store with free or paid assets, created by Unity or the community. |

---

## Unity Learning Roadmap

### Initial
- [x] Install Unity (LTS version recommended).  
- [x] Create first project (2D or 3D).  
- [x] Explore basic panels (Project, Hierarchy, Scene, Inspector).  

### Objects and Scenes
- [x] Add basic GameObjects (Cube, Sphere, Plane).  
- [x] Apply materials and textures.  
- [x] Configure collisions with Colliders.  
- [x] Manipulate transformations (position, rotation, scale).  

### Key Components
- [x] Set up a camera.  
- [x] Add lights and visual effects.  
- [x] Integrate audios.  

### Resource Management
- [x] Create and use Prefabs.  
- [x] Import external assets (3D models, audios).  
- [x] Download packages from the Asset Store.  

### Final Project
- [x] Build playable scene.  
- [ ] Export to PC or mobile.  
- [ ] Publish demo version.