from catalog.views import (
    anime_detalle,
    home,
    perfil,
    registro,
    toggle_favorito,
    toggle_visto,
    ver_episodio,
)
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Pantalla de Login personalizada usando tu login.html
    path(
        'login/',
        auth_views.LoginView.as_view(template_name='catalog/login.html'),
        name='login',
    ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('registro/', registro, name='registro'),
    # Ruta principal protegida (o que redirige si no hay sesión)
    path('', home, name='home'),
    # Rutas para botones interactivos
    path('favorito/<int:anime_id>/', toggle_favorito, name='toggle_favorito'),
    path('visto/<int:anime_id>/', toggle_visto, name='toggle_visto'),
    path('perfil/', perfil, name='perfil'),
    # Rutas para el reproductor y detalles
    path('anime/<int:anime_id>/', anime_detalle, name='anime_detalle'),
    path('episodio/<int:episodio_id>/', ver_episodio, name='ver_episodio'),
]