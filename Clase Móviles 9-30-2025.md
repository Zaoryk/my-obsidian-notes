# Desarrollo de Aplicaciones en Android

---

## Implementación de SweetAlertDialog

### ¿Qué es?
Librería que permite mostrar **alertas personalizadas** con mejor diseño y experiencia de usuario (UX).  
Tipos: advertencia, éxito, error, progreso, confirmación.

### Pasos de implementación
1. Crear una nueva `Activity` con 6 botones (uno por tipo de alerta).  
2. Declarar variables de tipo `Button` y enlazarlas con `findViewById()`.  
3. Asignar eventos `OnClickListener` a cada botón.  
4. Crear métodos individuales para cada tipo de alerta usando **SweetAlertDialog**.  

### Ejemplos de Alertas

**Advertencia**
```
private fun mostrarAdvertencia() {
    SweetAlertDialog(this, SweetAlertDialog.WARNING_TYPE)
        .setTitleText("Advertencia")
        .setContentText("Este cambio no se puede deshacer.")
        .setConfirmText("Entiendo")
        .setConfirmClickListener { dialog -> dialog.dismissWithAnimation() }
        .show()
}
```

**Éxito**
```
private fun mostrarExito() {
    SweetAlertDialog(this, SweetAlertDialog.SUCCESS_TYPE)
        .setTitleText("¡Éxito!")
        .setContentText("La operación fue realizada correctamente.")
        .setConfirmText("Aceptar")
        .setConfirmClickListener { dialog -> dialog.dismissWithAnimation() }
        .show()
}
```

**Error**
```
private fun mostrarError() {
    SweetAlertDialog(this, SweetAlertDialog.ERROR_TYPE)
        .setTitleText("Error")
        .setContentText("Algo salió mal. Intenta nuevamente.")
        .setConfirmText("Cerrar")
        .setConfirmClickListener { dialog -> dialog.dismissWithAnimation() }
        .show()
}
```

**Progreso**
```
private fun mostrarCargando() {
    val pDialog = SweetAlertDialog(this, SweetAlertDialog.PROGRESS_TYPE)
    pDialog.titleText = "Cargando..."
    pDialog.setCancelable(false)
    pDialog.show()

    Handler(Looper.getMainLooper()).postDelayed({
        pDialog.dismissWithAnimation()
    }, 3000)
}
```

**Confirmación**
```
private fun mostrarConfirmacion() {
    SweetAlertDialog(this, SweetAlertDialog.WARNING_TYPE)
        .setTitleText("¿Estás seguro?")
        .setContentText("Esta acción eliminará los datos.")
        .setConfirmText("Sí")
        .setCancelText("No")
        .setConfirmClickListener { dialog -> 
            dialog.dismissWithAnimation()
            mostrarExito()
        }
        .setCancelClickListener { dialog -> dialog.dismissWithAnimation() }
        .show()
}
```

**Proceso con carga y éxito**
```
private fun procesoConCargandoYExito() {
    val pDialog = SweetAlertDialog(this, SweetAlertDialog.PROGRESS_TYPE)
    pDialog.titleText = "Cargando..."
    pDialog.setCancelable(false)
    pDialog.show()

    Handler(Looper.getMainLooper()).postDelayed({
        pDialog.changeAlertType(SweetAlertDialog.SUCCESS_TYPE)
        pDialog.titleText = "¡Éxito!"
        pDialog.contentText = "La operación se completó correctamente."
        pDialog.confirmText = "Aceptar"
        pDialog.setConfirmClickListener { dialog -> dialog.dismissWithAnimation() }
    }, 3000)
}
```

### Configuración en Gradle
En `settings.gradle`:
```
maven(url = "https://jitpack.io")
```

En `build.gradle (Module: app)`:
```
implementation("com.github.f0ris.sweetalert:library:1.6.2")
```

---

## Creación de SplashScreen (Estático y Dinámico)

### ¿Qué es?
Pantalla de inicio que se muestra al abrir la app antes de cargar el contenido principal.  
Sirve como transición y mejora la experiencia de usuario.

### Tipos
- **Estático** → Imagen + texto fijo (logo, nombre app).  
- **Dinámico** → Animaciones vectoriales con Lottie.

---

### SplashScreen Estático
1. Crear dos `Activity` (Splash y Principal).  
2. En el `onCreate()` del Splash usar **pantalla completa**:
```
this.getWindow().setFlags(
    WindowManager.LayoutParams.FLAG_FULLSCREEN,
    WindowManager.LayoutParams.FLAG_FULLSCREEN
)
```
3. Usar `Handler` para esperar 5 segundos y abrir `Principal`:
```
Handler(Looper.getMainLooper()).postDelayed({
    val intent = Intent(this, Principal::class.java)
    startActivity(intent)
    finish()
}, 5000)
```

---

### SplashScreen Dinámico con Lottie

1. Descargar animación en formato JSON desde: https://lottiefiles.com/  
2. Crear carpeta **assets** en `app/src/main/` y guardar JSON ahí.  
3. Agregar dependencia en `build.gradle`:
```
implementation 'com.airbnb.android:lottie:1.5.3'
```
4. Insertar animación en el layout XML:
```
<com.airbnb.lottie.LottieAnimationView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:lottie_autoPlay="true"
    app:lottie_loop="true"
    app:lottie_fileName="animacion.json"/>
```
5. Controlar tiempo con `Handler` (ej: 7 segundos).

# Proyecto de ejemplo en Android Studio
## SweetAlertDialog + SplashScreen

---
## AndroidManifest.xml
```
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.ejemplo.miapp">

    <application
        android:allowBackup="true"
        android:label="MiApp"
        android:supportsRtl="true"
        android:theme="@style/Theme.AppCompat.Light.NoActionBar">

        <activity android:name=".MainActivity" />

        <activity android:name=".SplashActivity">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>
</manifest>
```

---

## Layouts

### activity_splash.xml
```
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical"
    android:background="#2196F3">

    <ImageView
        android:layout_width="150dp"
        android:layout_height="150dp"
        android:src="@mipmap/ic_launcher" />

    <TextView
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Bienvenido a MiApp"
        android:textColor="#FFFFFF"
        android:textSize="20sp"
        android:layout_marginTop="20dp"/>
</LinearLayout>
```

### activity_main.xml
```
<LinearLayout xmlns:android="http://schemas.android.com/apk/res/android"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    android:gravity="center"
    android:orientation="vertical"
    android:padding="20dp">

    <Button
        android:id="@+id/btnAdvertencia"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Advertencia" />

    <Button
        android:id="@+id/btnExito"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Éxito"
        android:layout_marginTop="10dp"/>

    <Button
        android:id="@+id/btnError"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Error"
        android:layout_marginTop="10dp"/>

    <Button
        android:id="@+id/btnConfirmacion"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Confirmación"
        android:layout_marginTop="10dp"/>

</LinearLayout>
```

---

## SplashActivity.kt
```
package com.ejemplo.miapp

import android.content.Intent
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import androidx.appcompat.app.AppCompatActivity

class SplashActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)

        Handler(Looper.getMainLooper()).postDelayed({
            startActivity(Intent(this, MainActivity::class.java))
            finish()
        }, 3000)
    }
}
```

---

## MainActivity.kt
```
package com.ejemplo.miapp

import android.os.Bundle
import android.widget.Button
import cn.pedant.SweetAlert.SweetAlertDialog
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val btnAdvertencia: Button = findViewById(R.id.btnAdvertencia)
        val btnExito: Button = findViewById(R.id.btnExito)
        val btnError: Button = findViewById(R.id.btnError)
        val btnConfirmacion: Button = findViewById(R.id.btnConfirmacion)

        btnAdvertencia.setOnClickListener { mostrarAdvertencia() }
        btnExito.setOnClickListener { mostrarExito() }
        btnError.setOnClickListener { mostrarError() }
        btnConfirmacion.setOnClickListener { mostrarConfirmacion() }
    }

    private fun mostrarAdvertencia() {
        SweetAlertDialog(this, SweetAlertDialog.WARNING_TYPE)
            .setTitleText("Advertencia")
            .setContentText("Este cambio no se puede deshacer.")
            .setConfirmText("Entiendo")
            .setConfirmClickListener { dialog -> dialog.dismissWithAnimation() }
            .show()
    }

    private fun mostrarExito() {
        SweetAlertDialog(this, SweetAlertDialog.SUCCESS_TYPE)
            .setTitleText("¡Éxito!")
            .setContentText("La operación fue realizada correctamente.")
            .setConfirmText("Aceptar")
            .setConfirmClickListener { dialog -> dialog.dismissWithAnimation() }
            .show()
    }

    private fun mostrarError() {
        SweetAlertDialog(this, SweetAlertDialog.ERROR_TYPE)
            .setTitleText("Error")
            .setContentText("Algo salió mal. Intenta nuevamente.")
            .setConfirmText("Cerrar")
            .setConfirmClickListener { dialog -> dialog.dismissWithAnimation() }
            .show()
    }

    private fun mostrarConfirmacion() {
        SweetAlertDialog(this, SweetAlertDialog.WARNING_TYPE)
            .setTitleText("¿Estás seguro?")
            .setContentText("Esta acción eliminará los datos.")
            .setConfirmText("Sí")
            .setCancelText("No")
            .setConfirmClickListener { dialog -> 
                dialog.dismissWithAnimation()
                mostrarExito()
            }
            .setCancelClickListener { dialog -> dialog.dismissWithAnimation() }
            .show()
    }
}
```

---

## build.gradle (Module: app)
```
dependencies {
    implementation "androidx.core:core-ktx:1.9.0"
    implementation "androidx.appcompat:appcompat:1.6.1"
    implementation "com.google.android.material:material:1.8.0"
    implementation "com.github.f0ris.sweetalert:library:1.6.2"
}
```

## Recursos útiles
- SweetAlertDialog GitHub: https://github.com/f0ris/sweet-alert-dialog  
- Lottie: https://lottiefiles.com/  
- Documentación Android Splash Screens: https://developer.android.com/guide/topics/ui/splash-screen  
