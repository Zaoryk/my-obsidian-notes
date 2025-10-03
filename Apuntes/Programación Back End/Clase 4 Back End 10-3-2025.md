
### ¿Qué es un Inline?
Permite editar **hijos** desde la ficha del **padre**.  

- Ejemplo EcoEnergy → desde **Product** ver y editar sus **AlertRules** (ProductAlertRule).  
- Ejemplo genérico → desde **Cliente** editar sus **Direcciones** o **Contactos**.  

Útil en relaciones **1:N** o **N:M** con tabla intermedia (*through*).

### Ejemplo de uso
```
# organizations/admin.py
from django.contrib import admin
from .models import Organization
from devices.models import Zone

class ZoneInline(admin.TabularInline):
    model = Zone
    extra = 0                       # No mostrar filas vacías por defecto
    fields = ("name", "status")     # Campos editables en grilla
    show_change_link = True         # Link a la vista propia

    # Importante: NO incluir FK 'organization' en fields
    # Django lo setea automáticamente
    # Si aparece, ocultar con:
    # exclude = ("organization",)

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    ordering = ("name",)
    inlines = [ZoneInline]          # Enganchamos el Inline
```

Los Inlines permiten **optimizar flujos de edición** sin salir del modelo padre.

---

## Acciones personalizadas
Sirven para ejecutar **operaciones en lote** desde Admin.  

- Ejemplo: activar/desactivar dispositivos seleccionados.  
- Ejemplo: exportar productos a CSV.  

Cada grupo debe definir **2 acciones útiles** para su proyecto.

### Ejemplo: Activar dispositivos
```
@admin.action(description="Activar dispositivos seleccionados")
def make_active(modeladmin, request, queryset):
    queryset.update(status="ACTIVE")

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ("name", "organization", "zone", "product", "max_power_w", "status")
    actions = [make_active]
    search_fields = ("name", "serial_number", "organization__name", "zone__name", "product__name")
    list_filter = ("organization", "zone", "product", "status")
    list_select_related = ("organization", "zone", "product")
    ordering = ("organization__name", "zone__name", "name")
    list_per_page = 50
```

Las acciones personalizadas reducen **tareas repetitivas** y aumentan la **eficiencia**.

---

## Validaciones en Admin
Permiten evitar datos inconsistentes desde la interfaz.  
Se aplican con `InlineFormSet` o sobrescribiendo métodos `clean` en un `ModelForm`.

### Ejemplo: Validación en Organization
```
# organizations/forms.py
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        if len(name) > 50:
            raise ValidationError("El nombre no puede tener más de 50 caracteres.")
        return name

    def clean_deleted_at(self):
        deleted_at = self.cleaned_data.get("deleted_at")
        if deleted_at and deleted_at < timezone.now():
            raise ValidationError("La fecha de eliminación no puede ser anterior a hoy.")
        return deleted_at
```

```
# organizations/admin.py
from .forms import OrganizationForm

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    form = OrganizationForm   # usamos el form con validaciones
```

Las validaciones en Admin protegen la **consistencia de la BD**.