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

---

## Recursos
- SweetAlertDialog GitHub: https://github.com/f0ris/sweet-alert-dialog  
- Lottie: https://lottiefiles.com/  
- Documentación Android Splash Screens: https://developer.android.com/guide/topics/ui/splash-screen  

