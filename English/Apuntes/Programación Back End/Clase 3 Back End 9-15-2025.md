## Authentication in Django - Back-End Summary

### Authentication Objectives
- [x] Understand login/logout flow in Django
- [x] Use `as_view()` with class-based views (CBV)
- [x] Take advantage of `django.contrib.auth.views`
- [x] Protect views with `@login_required` and `LoginRequiredMixin`
- [x] Relate users to Organization and filter data

---

## Basic Configuration

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


### Project urls.py

```python
from django.contrib import admin
from django.urls import path, include
from dispositivos.views import dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", dashboard, name="dashboard"),
    path("", include("accounts.urls")),  # login, logout
]```


## Authentication Views

### LoginView with Custom Form

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


### LogoutView (Always by POST)

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


## View Protection

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


## Filtered by Organization

### UserProfile Model

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


### View with filtering

```python
@login_required
def devices_list(request):
    org = request.user.userprofile.organization
    qs = Device.objects.filter(organization=org).select_related("category", "zone")
    return render(request, "devices/list.html", {"devices": qs})
```


## Password Reset and Change

## URLs for Password Management

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


### Email Configuration (Development)

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


## Image and File Management

### Configuration settings.py

```python
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
```


### Model with ImageField

```python
class Dispositivo(models.Model):
    imagen = models.ImageField(
        upload_to='dispositivos/', 
        null=True, 
        blank=True
    )
    # otros campos...
```


### Media URL Configuration

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


### In Views (don't forget request.FILES)

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


## RESTful API with JsonResponse

### View for JSON Device List

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


### View for Latest Measurements

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


## Common Errors and Solutions

### 405 in /logout/

- **Cause**: GET method instead of POST
    
- **Solution**: Use POST form with CSRF token
    

### TemplateSyntaxError 'add_class'

- **Cause**: Missing django-widget-tweaks
    
- **Solution**: Install or use `attrs.update` in forms
    

### Redirect loop

- **Cause**: LOGIN_REDIRECT_URL incorrectly configured
    
- **Solution**: Verify URL names
    

### Does not show data

- **Cause**: Poorly configured filters by organization
    
- **Solution**: Verify FK/OneToOne relationships