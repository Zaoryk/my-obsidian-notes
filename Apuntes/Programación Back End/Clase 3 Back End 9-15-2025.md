## Autenticación en Django - Resumen Back-End

###  Objetivos de Autenticación
- [ ] Comprender flujo de login/logout en Django
- [ ] Usar `as_view()` con vistas basadas en clases (CBV)
- [ ] Aprovechar `django.contrib.auth.views`
- [ ] Proteger vistas con `@login_required` y `LoginRequiredMixin`
- [ ] Relacionar usuarios con Organization y filtrar datos

---

## Configuración Básica

### settings.py
```python
LOGIN_URL = "login"
LOGIN_REDIRECT_URL = "dashboard" 
LOGOUT_REDIRECT_URL = "login"

# Para mensajes en templates
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]```

### urls.py del Proyecto
```python
from django.contrib import admin
from django.urls import path, include
from dispositivos.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("", include("accounts.urls")),  # login, logout
]```

## Vistas de Autenticación

### LoginView con Formulario Personalizado
```python
# accounts/urls.py
from django.contrib.auth.views import LoginView
from .forms import LoginForm

urlpatterns = [
    path("login/", LoginView.as_view(
        template_name="accounts/login.html",
        redirect_authenticated_user=True,
        authentication_form=LoginForm
    ), name="login"),
]

# accounts/forms.py
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs.update({
            "class": "form-control", "placeholder": "Usuario o email"
        })
        self.fields["password"].widget.attrs.update({
            "class": "form-control", "placeholder": "Contraseña"
        })
        ```

### LogoutView (Siempre por POST)
```python
# accounts/urls.py
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("logout/", LogoutView.as_view(), name="logout"),
]

# Template (navbar.html)
<form action="{% url 'logout' %}" method="post" class="d-inline">
  {% csrf_token %}
  <button type="submit" class="btn btn-link nav-link">Salir</button>
</form>
```

## Protección de Vistas

### FBV - Function Based Views
```python
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, "dispositivos/dashboard.html")
```

### CBV - Class Based Views
```python
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "dispositivos/dashboard.html"
    login_url = "login"
    redirect_field_name = "next"
```

## Filtrado por Organizacion

### Modelo UserProfile
```python
# models.py
from django.contrib.auth.models import User
from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=100)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
```

### Vista con filtrado
```python
@login_required
def devices_list(request):
    org = request.user.userprofile.organization
    qs = Device.objects.filter(organization=org).select_related("category", "zone")
    return render(request, "devices/list.html", {"devices": qs})
```

## Password Reset y Change

## URLs para Password Management
```python
# accounts/urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Password Change
    path("password/change/", auth_views.PasswordChangeView.as_view(
        template_name="accounts/password_change_form.html",
        success_url="/accounts/password/change/done/"
    ), name="password_change"),
    
    path("password/change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name="accounts/password_change_done.html"
    ), name="password_change_done"),
    
    # Password Reset
    path("password/reset/", auth_views.PasswordResetView.as_view(
        template_name="accounts/password_reset_form.html",
        email_template_name="accounts/email/password_reset_email.txt",
        subject_template_name="accounts/email/password_reset_subject.txt",
        success_url="/accounts/password/reset/done/"
    ), name="password_reset"),
    
    # ... más paths para reset
]
```

### Configuracion de Email (Desarrollo)
```python
# settings.py
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Para producción (Mailtrap ejemplo)
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "sandbox.smtp.mailtrap.io"
EMAIL_PORT = 2525
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
```

## Manejo de Imágenes y Archivos

### Configuracion settings.py
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### Modelo con ImageField
```python
class Dispositivo(models.Model):
    imagen = models.ImageField(
        upload_to='dispositivos/', 
        null=True, 
        blank=True
    )
    # otros campos...
```

### Configuracion de URLs para Media
```python
# urls.py
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... tus paths
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT
    )
```

### En Views (no olvidar request.FILES)
```python
def crear_dispositivo(request):
    if request.method == 'POST':
        form = DispositivoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_dispositivos')
    else:
        form = DispositivoForm()
    return render(request, 'form.html', {'form': form})
```

## API RESTful con JsonResponse

### Vista para Lista de Dispositivos JSON
```python
from django.http import JsonResponse
from .models import Dispositivo

def dispositivos_json(request):
    dispositivos = Dispositivo.objects.all()[:10]  # Últimos 10
    data = [
        {
            'id': d.id,
            'nombre': d.nombre,
            'imagen_url': d.imagen.url if d.imagen else None,
            'fecha_creacion': d.fecha_creacion.isoformat()
        }
        for d in dispositivos
    ]
    return JsonResponse(data, safe=False)
```

### Vista para Ultimas Mediciones
```python
def ultimas_mediciones_json(request, dispositivo_id):
    mediciones = Medicion.objects.filter(
        dispositivo_id=dispositivo_id
    ).order_by('-fecha')[:10]
    
    data = [
        {
            'valor': m.valor,
            'unidad': m.unidad,
            'fecha': m.fecha.isoformat()
        }
        for m in mediciones
    ]
    return JsonResponse(data, safe=False)
```

## Errores Comunes y Soluciones

### 405 en /logout/

- **Causa**: Método GET en vez de POST
    
- **Solución**: Usar formulario POST con CSRF token
    

### TemplateSyntaxError 'add_class'

- **Causa**: Falta django-widget-tweaks
    
- **Solución**: Instalar o usar `attrs.update` en forms
    

### Bucle de redirección

- **Causa**: LOGIN_REDIRECT_URL mal configurado
    
- **Solución**: Verificar nombres de URLs
    

### No muestra datos

- **Causa**: Filtros por organización mal configurados
    
- **Solución**: Verificar relaciones FK/OneToOne

## Próximos Pasos Recomendados

1. Implementar autenticación completa
    
2. Configurar manejo de imágenes
    
3. Crear endpoints API básicos
    
4. Implementar tests automatizados
    
5. Configurar email en producción
    
6. Optimizar queries con `select_related` y `prefetch_related`
    
7. Implementar paginación en APIs
    
8. Agregar documentación API con Swagger