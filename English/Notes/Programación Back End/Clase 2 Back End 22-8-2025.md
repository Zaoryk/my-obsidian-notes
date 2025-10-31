# Backend with Django – Summary Classes 6 to 8

## Class 6 and 7: Unifying Models

### Context
- **EcoEnergy** Project → energy monitoring system.  
- You need to register: devices, zones, categories, measurements and alerts.  
- Each group designed models, now they are unified into a standard model.  

###BaseModel
- Base class with common attributes:  
  - `estado` (uses constant `ESTADOS = [("ACTIVO","Activo"),("INACTIVO","Inactivo")]`)  
  - `created_at`, `updated_at`, `deleted_at`  
- **Inheritance**: other tables like `Categoria`, `Zona`, `Dispositivo` inherit from `BaseModel`.  

### Date fields
| Field | Function |
| ------------ | -------------------------------- |
| `created_at` | Record creation date.  |
| `updated_at` | Last modification.             |
| `deleted_at` | Soft delete (NULL = not deleted). |

### class Meta
- Extra model configuration.  
- `abstract = True` → does not create a table in the DB, it only serves as a template.  
- Example: there is no table `BaseModel`, but there is `Categoria`, with its own + inherited fields.  

---

## Class 7 and 8: Django Admin + Relationships

### What is Django Admin?

- Web interface included in Django.  
- Allows you to manage data without scheduling views.  
- Ideal for testing and quick administration.  

### Migrations


```bash
python manage.py makemigrations
python manage.py migrate
```


### Register Models in Admin

- Create `admin.py` file in each app.
- Example: `dispositivos/admin.py`
- Register models -> they appear in the `/admin/` panel.

### Access


```bash
python manage.py createsuperuser
http://localhost:8000/admin/
```


### Admin Customization


| Function | Description |
| ----------------- | ------------------------------------------ |
| `list_display` | Show multiple columns in list.             |
| `list_filter` | Side filters (e.g. active/inactive) |
| `search_fields` | Search by specific fields |
| `readonly_fields` | Read-only fields.                       |
| `fieldsets` | Group fields into sections |
| Actions | Example: turn off several devices at the same time. |

### Class 8: Queries and Navigation
#### Objectives
- Query data with the **Django ORM**
- Show dynamic data in **templates**.
- Implement navigation between views and routes.

#### Basic ORM Queries


```bash
Empleado.objects.all()
Empleado.objects.filter(cargo="Admin")
Producto.objects.filter(precio__lte=50)  # Precio menor o igual a 50
```


#### Advanced Operations
- Logical conditions with `Q`.
- Exclusions with `.exclude()`.
- Aggregations and groupings with `annotate`, `aggregate`.
- `F-expressions`: calculations in the database.
- Subqueries and `Exists` (advanced).

###Templates
- Pass data from views with `context`
- Display in HTML with:

```bash
{{ variable }}
```


### Navigation between Views
In `urls.py`

```bash
path("empleados/", views.lista_empleados, name="empleados")
```

in template:

```bash
<a href="{% url 'empleados' %}">Lista de empleados</a>
```

### Practical Example
- Create model `Medicion`.
- View that lists all measurements.
- Template with list.
- Link with ID -> detail of a measurement