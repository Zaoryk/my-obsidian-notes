# Android Application Development

---

##SweetAlertDialog implementation

### What is it?
Library that allows you to display **custom alerts** with better design and user experience (UX).  
Types: warning, success, error, progress, confirmation.

### Implementation steps
1. Create a new `Activity` with 6 buttons (one per alert type).  
2. Declare variables of type `Button` and link them with `findViewById()`.  
3. Assign `OnClickListener` events to each button.  
4. Create individual methods for each alert type using **SweetAlertDialog**.  

### Examples of Alerts

**Warning**

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


**Success**

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


**Progress**

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


**Confirmation**

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


**Process with loading and success**

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


### Configuration in Gradle
In `settings.gradle`:

```
maven(url = "https://jitpack.io")
```


In `build.gradle (Module: app)`:

```
implementation("com.github.f0ris.sweetalert:library:1.6.2")
```


---

## Creation of SplashScreen (Static and Dynamic)

### What is it?
Home screen displayed when you open the app before loading the main content.  
It serves as a transition and improves the user experience.

### Types
- **Static** → Image + fixed text (logo, app name).  
- **Dynamic** → Vector animations with Lottie.

---

### Static SplashScreen
1. Create two `Activity` (Splash and Main).  
2. In the `onCreate()` of the Splash use **full screen**:

```
this.getWindow().setFlags(
    WindowManager.LayoutParams.FLAG_FULLSCREEN,
    WindowManager.LayoutParams.FLAG_FULLSCREEN
)
```

3. Use `Handler` to wait 5 seconds and open `Principal`:

```
Handler(Looper.getMainLooper()).postDelayed({
    val intent = Intent(this, Principal::class.java)
    startActivity(intent)
    finish()
}, 5000)
```


---

### Dynamic SplashScreen with Lottie

1. Download animation in JSON format from: https://lottiefiles.com/  
2. Create **assets** folder in `app/src/main/` and save JSON there.  
3. Add dependency on `build.gradle`:

```
implementation 'com.airbnb.android:lottie:1.5.3'
```

4. Insert animation in the XML layout:

```
<com.airbnb.lottie.LottieAnimationView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    app:lottie_autoPlay="true"
    app:lottie_loop="true"
    app:lottie_fileName="animacion.json"/>
```

5. Control time with `Handler` (ex: 7 seconds).

# Example project in Android Studio
## SweetAlertDialog + SplashScreen

---
##AndroidManifest.xml

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


## Useful resources
- SweetAlertDialog GitHub: https://github.com/f0ris/sweet-alert-dialog  
- Lottie: https://lottiefiles.com/  
- Android Splash Screens Documentation: https://developer.android.com/guide/topics/ui/splash-screen