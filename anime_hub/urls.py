from django.contrib import admin
from django.urls import path, include
from catalog.views import home, registro, toggle_favorito, toggle_visto, perfil, anime_detalle, ver_episodio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('registro/', registro, name='registro'),
    path('cuentas/', include('django.contrib.auth.urls')),
    
    # Rutas para botones interactivos
    path('favorito/<int:anime_id>/', toggle_favorito, name='toggle_favorito'),
    path('visto/<int:anime_id>/', toggle_visto, name='toggle_visto'),
    path('perfil/', perfil, name='perfil'),
    
    # Rutas para el reproductor y detalles
    path('anime/<int:anime_id>/', anime_detalle, name='anime_detalle'),
    path('episodio/<int:episodio_id>/', ver_episodio, name='ver_episodio'),
]