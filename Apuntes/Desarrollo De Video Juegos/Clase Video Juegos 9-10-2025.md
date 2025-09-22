## Introducción a Unity (Motor de Videojuegos)

### ¿Qué es Unity?
- Motor genérico para crear videojuegos 2D y 3D.  
- Curva de aprendizaje suave (más simple que Unreal Engine).  
- Ideal para prototipos y desarrollo rápido.  
- Ediciones:  
  - **Personal**: Gratis, todas las funciones, para ingresos < $100.000 anuales.  
  - **Profesional**: Suscripción $75/mes o pago único $1500.  
- Exporta a: iOS, Android, Windows Phone, WebGL, PS4, Xbox, Wii U, Mac, Windows, Linux.  

---

## Entorno del Editor de Unity

| Panel | Función |
|-------|---------|
| **Project** | Contiene todos los recursos (assets: texturas, audios, scripts, escenas). |
| **Hierarchy** | Árbol de objetos de la escena actual. |
| **Scene** | Vista visual de la escena (2D/3D). |
| **Inspector** | Muestra y edita propiedades del objeto o asset seleccionado. |

---

## Scene 3D y Objetos

- Se pueden añadir objetos vacíos o predefinidos (Cube, Sphere, Capsule, Plane).  
- Los objetos básicos incluyen componentes:  

| Componente | Función |
|------------|---------|
| **Transform** | Posición, rotación y escala en la escena. |
| **Renderer** | Renderiza el objeto en pantalla con su material/mesh. |
| **Collider** | Define geometría de colisión (ej. Box Collider). |

---

## Transformaciones de Objetos
- **Traslación**: mover en ejes X, Y, Z.  
- **Rotación**: giros sobre los tres ejes.  
- **Escalado**: cambiar tamaño en cada eje.  

---

## Navegación en la Escena
- **Ver un objeto**: doble clic en Hierarchy.  
- **Alineación con objeto**: `GameObject > Align View To Selected`.  

---

## Jerarquía de Objetos
- Arrastrar objetos en **Hierarchy** → relaciones padre-hijo.  
- Objetos vacíos sirven para agrupar.  
- Dar nombres significativos para organización.  

---

## Arquitectura Orientada a Componentes
- Todos los objetos son **GameObjects**.  
- La funcionalidad depende de los componentes añadidos.  
- Ejemplo de cámara:  
  - Transform (posición)  
  - Camera (renderiza escena)  
  - GUILayer (GUI en pantalla)  
  - FlareLayer (efecto de destello)  
  - AudioListener (captura sonido)  

---

## Conceptos Clave en Unity

| Concepto | Definición |
|----------|------------|
| **Assets** | Recursos usados en el proyecto (texturas, modelos, audios, scripts, etc.). |
| **Prefabs** | Colecciones de GameObjects configurados y reutilizables. Cambios en prefab → se aplican a todas sus instancias. |
| **Paquetes de Assets** | Colecciones exportables/importables (standard o personalizados). |
| **Asset Store** | Tienda de Unity con assets gratis o de pago, creados por Unity o la comunidad. |

---

## Roadmap de Aprendizaje en Unity

###  Inicial
- [x] Instalar Unity (versión LTS recomendada).  
- [x] Crear primer proyecto (2D o 3D).  
- [x] Explorar paneles básicos (Project, Hierarchy, Scene, Inspector).  

###  Objetos y Escenas
- [x] Añadir GameObjects básicos (Cube, Sphere, Plane).  
- [x] Aplicar materiales y texturas.  
- [x] Configurar colisiones con Colliders.  
- [x] Manipular transformaciones (posición, rotación, escala).  

###  Componentes Clave
- [x] Configurar una cámara.  
- [x] Añadir luces y efectos visuales.  
- [x] Integrar audios.  

###  Gestión de Recursos
- [x] Crear y usar Prefabs.  
- [x] Importar assets externos (modelos 3D, audios).  
- [x] Descargar paquetes de la Asset Store.  

###  Proyecto Final
- [x] Construir escena jugable.  
- [ ] Exportar a PC o móvil.  
- [ ] Publicar versión demo.  