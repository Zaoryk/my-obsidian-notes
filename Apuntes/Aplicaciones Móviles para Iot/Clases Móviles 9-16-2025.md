
##  ¿Qué es Android Studio?
- IDE oficial para desarrollo Android.  
- Basado en IntelliJ IDEA.  
- Soporta Java, Kotlin y C++.  
- Incluye:
  - Editor de código inteligente.  
  - Diseñador visual de interfaces (Layout Editor).  
  - Herramientas de depuración.  
  - Emulador de dispositivos Android.  
---
##  Creación de una Máquina Virtual (AVD)

### ¿Qué es?
- Android Virtual Device (AVD) → emulador que simula un smartphone Android.  

### Pasos
1. Abrir Android Studio → Tools > Device Manager.  
2. Create Device → elegir hardware (Pixel, Nexus, Tablet, WearOS).  
3. Seleccionar imagen del sistema (Android 13, 12, etc.).  
4. Configurar RAM, almacenamiento, orientación.  
5. Guardar y ejecutar → se abre un emulador Android.  

### Configuración recomendada
| Configuración | Valor |
|---------------|-------|
| Device | Pixel 6 / Pixel 4a |
| API Level | 33 (Android 13) |
| RAM | 2 GB mínimo |
| Storage | 4 GB |
| Graphics | Hardware – GLES 2.0 |

 https://developer.android.com/studio/run/emulator
---

## Crear un Proyecto Android

1. Abrir Android Studio → New Project.  
2. Seleccionar plantilla (Empty Activity, Navigation Drawer, etc.).  
3. Configurar:
   - Nombre de la app  
   - Paquete (ej: com.ejemplo.miapp)  
   - Lenguaje: Kotlin o Java  
   - Minimum SDK (ej: API 24 para 90% dispositivos)  

#### Estructura del proyecto:
MiApp/
 ├─ manifests/ (AndroidManifest.xml)
 ├─ java/ (código fuente)
 ├─ res/ (layouts, imágenes, strings)
 ├─ gradle/ (configuración de build)
 
---

## Interfaz Gráfica (Layouts)

- Archivos XML en /res/layout/.  
- Dos formas de diseño:
  1. Design view (arrastrar y soltar).  
  2. Code view (XML).  

Ejemplo de layout (activity_main.xml):
```
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:orientation="vertical">

    <TextView
        android:id="@+id/txtMensaje"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Hola Mundo!" />

    <Button
        android:id="@+id/btnSaludar"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Presionar" />
</LinearLayout>
```

---

## Lógica en Kotlin/Java

#### Ejemplo en Kotlin (MainActivity.kt):

```
package com.ejemplo.miapp

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val txtMensaje: TextView = findViewById(R.id.txtMensaje)
        val btnSaludar: Button = findViewById(R.id.btnSaludar)

        btnSaludar.setOnClickListener {
            txtMensaje.text = "¡Hola desde Kotlin!"
        }
    }
}
```
---

## Ejecutar la App
1. Seleccionar AVD creado.  
2. Presionar Run  en Android Studio.  
3. La app se compila y se abre en el emulador.  

También se puede ejecutar en un dispositivo físico activando:  
- Modo desarrollador → Depuración USB.  

---

## Gradle
- Herramienta de automatización de compilación.  
- Controla dependencias y configuración del proyecto.  

Ejemplo build.gradle:
```
dependencies {
    implementation "androidx.core:core-ktx:1.9.0"
    implementation "com.google.android.material:material:1.8.0"
}
```
https://developer.android.com/studio/build

---

## Recursos de Apoyo

- Documentación oficial: https://developer.android.com/docs  
- Cursos gratuitos: https://codelabs.developers.google.com/?cat=Android  
- GitHub ejemplos: https://github.com/android  

---

# Roadmap

- [x] Instalar Android Studio y SDK.  
- [x] Crear AVD (emulador).  
- [x] Crear proyecto → Empty Activity.  
- [x] Diseñar interfaz en XML o Design view.  
- [ ] Programar lógica en Kotlin/Java.  
- [ ] Ejecutar en emulador o dispositivo físico.  
- [ ] Agregar dependencias con Gradle.  