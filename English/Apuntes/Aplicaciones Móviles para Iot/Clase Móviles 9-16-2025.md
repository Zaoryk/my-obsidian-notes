## What is Android Studio?
- Official IDE for Android development.  
- Based on IntelliJ IDEA.  
- Supports Java, Kotlin and C++.  
- Includes:
  - Smart code editor.  
  - Visual interface designer (Layout Editor).  
  - Debugging tools.  
  - Android device emulator.  
---
## Creating a Virtual Machine (AVD)

### What is it?
- Android Virtual Device (AVD) → emulator that simulates an Android smartphone.  

### Steps
1. Open Android Studio → Tools > Device Manager.  
2. Create Device → choose hardware (Pixel, Nexus, Tablet, WearOS).  
3. Select system image (Android 13, 12, etc.).  
4. Configure RAM, storage, orientation.  
5. Save and run → an Android emulator opens.  

### Recommended settings
| Settings | Value |
|---------------|-------|
| Device | Pixel 6 / Pixel 4a |
| APILevel | 33 (Android 13) |
| RAM | 2GB minimum |
| Storage | 4GB |
| Graphics | Hardware – GLES 2.0 |

 https://developer.android.com/studio/run/emulator
---

## Create an Android Project

1. Open Android Studio → New Project.  
2. Select template (Empty Activity, Navigation Drawer, etc.).  
3. Configure:
   - App name  
   - Package (ex: com.example.myapp)  
   - Language: Kotlin or Java  
   - Minimum SDK (ex: API 24 for 90% devices)  

#### Project structure:
MyApp/
 ├─ manifests/ (AndroidManifest.xml)
 ├─ java/ (source code)
 ├─ res/ (layouts, images, strings)
 ├─ gradle/ (build configuration)
 
---

## Graphical Interface (Layouts)

- XML files in /res/layout/.  
- Two forms of design:
  1. Design view (drag and drop).  
  2. Code view (XML).  

Layout example (activity_main.xml):

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

## Logic in Kotlin/Java

#### Example in Kotlin (MainActivity.kt):


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

## Run the App
1. Select created AVD.  
2. Press Run in Android Studio.  
3. The app is compiled and opened in the emulator.  

It can also be run on a physical device by enabling:  
- Developer mode → USB debugging.  

---

##Gradle
- Build automation tool.  
- Control project dependencies and configuration.  

build.gradle example:

```
dependencies {
    implementation "androidx.core:core-ktx:1.9.0"
    implementation "com.google.android.material:material:1.8.0"
}
```

https://developer.android.com/studio/build

---

## Support Resources

- Official documentation: https://developer.android.com/docs  
- Free courses: https://codelabs.developers.google.com/?cat=Android  
- GitHub examples: https://github.com/android  

---

#Roadmap

- [x] Install Android Studio and SDK.  
- [x] Create AVD (emulator).  
- [x] Create project → Empty Activity.  
- [x] Design interface in XML or Design view.  
- [x] Program logic in Kotlin/Java.  
- [x] Run on emulator or physical device.  
- [x] Add dependencies with Gradle.