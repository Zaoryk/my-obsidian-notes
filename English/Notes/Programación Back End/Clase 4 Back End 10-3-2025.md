### What is an Inline?
Allows you to edit **children** from the **parent** file.  

- EcoEnergy example → from **Product** see and edit your **AlertRules** (ProductAlertRule).  
- Generic example → from **Customer** edit their **Addresses** or **Contacts**.  

Useful in **1:N** or **N:M** relationships with an intermediate table (*through*).

### Usage example

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


Inlines allow you to **optimize editing flows** without leaving the parent model.

---

## Custom actions
They are used to execute **batch operations** from Admin.  

- Example: activate/deactivate selected devices.  
- Example: export products to CSV.  

Each group must define **2 useful actions** for their project.

### Example: Activate devices

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


Custom actions reduce **repetitive tasks** and increase **efficiency**.

---

## Validations in Admin
They allow you to avoid inconsistent data from the interface.  
They are applied with `InlineFormSet` or by overriding `clean` methods in a `ModelForm`.

### Example: Validation in Organization

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


Validations in Admin protect the **consistency of the DB**.