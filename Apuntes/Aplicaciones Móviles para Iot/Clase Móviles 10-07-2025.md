# Android + Backend — WebService, CRUD y Login (Kotlin, PHP, MySQL)

## WebService en Android con Kotlin
### ¿Qué es un WebService?
Un **WebService** permite que aplicaciones distintas se comuniquen entre sí mediante **protocolos y formatos estándar** (principalmente JSON y HTTP).  
**Ventajas:**
- Interoperabilidad entre aplicaciones de distintos lenguajes o plataformas.  
- Basado en texto (JSON/XML), lo que facilita su interpretación.  
- Compatible con cortafuegos y protocolos estándar.  
- Permite combinar servicios distribuidos.  
#### Dependencias y permisos
Agregar en `build.gradle`:
```
implementation("com.android.volley:volley:1.2.1")
```
Y en `AndroidManifest.xml`:
```
<uses-permission android:name="android.permission.INTERNET" />
```

#### Variables principales
```
lateinit var fecha: TextView
lateinit var temp: TextView
lateinit var hum: TextView
lateinit var imagenTemp: ImageView
lateinit var datos: RequestQueue
```
Casteo en `onCreate()` y llamada a funciones:
```
fecha.text = fechahora()
datos = Volley.newRequestQueue(this)
obtenerDatos()
```

#### Función de fecha
```
fun fechahora(): String {
    val c = Calendar.getInstance()
    val sdf = SimpleDateFormat("dd MMMM YYYY, hh:mm:ss a")
    return sdf.format(c.getTime())
}
```

#### Obtener datos del WebService
```
private fun obtenerDatos() {
    val url = "https://www.pnk.cl/muestra_datos.php"
    val request = JsonObjectRequest(
        Request.Method.GET, url, null,
        { response ->
            temp.text = "${response.getString("temperatura")} C"
            hum.text = "${response.getString("humedad")} %"
            val valor = response.getString("temperatura").toFloat()
            cambiarImagen(valor)
        },
        { error -> error.printStackTrace() }
    )
    datos.add(request)
}
```

#### Cambio dinámico de imagen
```
private fun cambiarImagen(valor: Float) {
    if (valor >= 20) {
        imagenTemp.setImageResource(R.drawable.tempalta)
    } else {
        imagenTemp.setImageResource(R.drawable.tempbaja)
    }
}
```

#### Actualización automática (Handler)
```
val mHandler = Handler(Looper.getMainLooper())
private val refrescar = object : Runnable {
    override fun run() {
        fecha.text = fechahora()
        obtenerDatos()
        mHandler.postDelayed(this, 1000)
    }
}
mHandler.post(refrescar)
```

Volley + Handler permiten **consultas automáticas y dinámicas** al servidor remoto.

---

## CRUD con SQLite
### Creación de la base local
Clase `ConexionDbHelper`:
```
class ConexionDbHelper(context: Context)
: SQLiteOpenHelper(context, "CRUD", null, 1) {

    val sql = "CREATE TABLE USUARIOS (ID INTEGER PRIMARY KEY, NOMBRE TEXT, APELLIDO TEXT, EMAIL TEXT, CLAVE TEXT)"
    override fun onCreate(db: SQLiteDatabase) = db.execSQL(sql)
    override fun onUpgrade(db: SQLiteDatabase, oldVersion: Int, newVersion: Int) {
        db.execSQL("DROP TABLE IF EXISTS USUARIOS")
        onCreate(db)
    }
}
```

### Insertar datos
```
fun guardar(nom: String, ape: String, mai: String, cla: String) {
    val helper = ConexionDbHelper(this)
    val db = helper.writableDatabase
    val datos = ContentValues().apply {
        put("Nombre", nom); put("Apellido", ape)
        put("Email", mai); put("Clave", cla)
    }
    db.insert("USUARIOS", null, datos)
    db.close()
}
```

### Listar datos
```
private fun listaUsuario(): ArrayList<String> {
    val lista = ArrayList<String>()
    val db = ConexionDbHelper(this).readableDatabase
    val c = db.rawQuery("SELECT * FROM USUARIOS", null)
    while (c.moveToNext()) {
        lista.add("${c.getInt(0)} ${c.getString(1)} ${c.getString(2)}")
    }
    c.close(); db.close()
    return lista
}
```

### Modificar y eliminar
```
private fun modificar(id: Int, nombre: String, apellido: String) {
    val db = ConexionDbHelper(this).writableDatabase
    db.execSQL("UPDATE USUARIOS SET NOMBRE='$nombre', APELLIDO='$apellido' WHERE ID=$id")
}

private fun eliminar(id: Int) {
    val db = ConexionDbHelper(this).writableDatabase
    db.execSQL("DELETE FROM USUARIOS WHERE ID=$id")
}
```

 SQLite permite **persistencia local** y operaciones CRUD sin conexión.

---

## Login con AWS + PHP + MySQL
### Configuración inicial
Agregar permisos en `AndroidManifest.xml`:
```
<uses-permission android:name="android.permission.INTERNET" />
<application android:usesCleartextTraffic="true">
```

Y dependencia en `build.gradle`:
```
implementation("com.android.volley:volley:1.2.1")
```

### Función de login
```
fun consultarDatos(usu: String, pass: String) {
    val url = "http://52.2.255.205/apiconsultausu.php?usu=$usu&pass=$pass"
    val request = JsonObjectRequest(Request.Method.GET, url, null,
        { response ->
            val estado = response.getString("estado")
            if (estado == "0") {
                Toast.makeText(this, "Usuario no existe", Toast.LENGTH_LONG).show()
            } else {
                val ventana = Intent(this, Principal::class.java)
                startActivity(ventana)
            }
        },
        { error -> error.printStackTrace() }
    )
    datos.add(request)
}
```

### Código PHP del backend
```php
<?php
$cont = mysqli_connect('localhost','root','clave','pnkcl_iot');
$sql = "SELECT * FROM Usuarios WHERE Usuario='".$_GET['usu']."' AND Clave='".$_GET['pass']."'";
$result = mysqli_query($cont, $sql);
$num = mysqli_num_rows($result);
$val = array('estado' => $num == null ? '0' : $num);
echo json_encode($val);
?>
```

 El login combina **Volley en Android** con un **WebService PHP** en AWS, comunicándose en formato JSON.

---

## Documentación
- 📚 [Documentación oficial de Volley](https://developer.android.com/training/volley)
- 💾 [SQLite en Android](https://developer.android.com/training/data-storage/sqlite)
- ☁️ [AWS EC2 - Servicios Web](https://aws.amazon.com/ec2/)
- 🔒 [Android Manifest Permissions](https://developer.android.com/guide/topics/manifest/manifest-intro)

---

## Conclusión general
| Componente              | Tecnología            | Propósito                              |
| ----------------------- | --------------------- | -------------------------------------- |
| **WebService**          | Kotlin + Volley + PHP | Consultar datos remotos en tiempo real |
| **SQLite CRUD**         | Kotlin                | Almacenamiento local persistente       |
| **Login AWS**           | Kotlin + PHP + MySQL  | Autenticación en servidor remoto       |
| **Interfaz y permisos** | XML + Manifest        | Control de recursos y permisos         |
| **Mensajería UI**       | SweetAlertDialog      | Notificaciones visuales y validaciones |
