# Backend con Django – Resumen Clases 6 a 8

## Clase 6 y 7: Unificando Models

### Contexto
- Proyecto **EcoEnergy** → sistema de monitoreo energético.  
- Necesita registrar: dispositivos, zonas, categorías, mediciones y alertas.  
- Cada grupo diseñó modelos, ahora se unifican en un modelo estándar.  

### BaseModel
- Clase base con atributos comunes:  
  - `estado` (usa constante `ESTADOS = [("ACTIVO","Activo"),("INACTIVO","Inactivo")]`)  
  - `created_at`, `updated_at`, `deleted_at`  
- **Herencia**: otras tablas como `Categoria`, `Zona`, `Dispositivo` heredan de `BaseModel`.  

### Campos de fechas
| Campo | Función |
|-------|----------|
| `created_at` | Fecha de creación del registro. |
| `updated_at` | Última modificación. |
| `deleted_at` | Soft delete (NULL = no borrado). |

### class Meta
- Configuración extra de modelos.  
- `abstract = True` → no crea tabla en la BD, solo sirve como plantilla.  
- Ejemplo: no existe tabla `BaseModel`, pero sí `Categoria`, con sus propios campos + heredados.  

---

## Clase 7 y 8: Django Admin + Relaciones

### ¿Qué es Django Admin?

- Interfaz web incluida en Django.  
- Permite gestionar datos sin programar vistas.  
- Ideal para pruebas y administración rápida.  

### Migraciones

```bash
python manage.py makemigrations
python manage.py migrate
```

### Registrar Modelos en Admin

- Crear archivo `admin.py` en cada app.
- Ejemplo: `dispositivos/admin.py`
- Registar modelos -> aparecen en el panel `/admin/`.

### Acceso

```bash
python manage.py createsuperuser
http://localhost:8000/admin/
```

