from django.contrib import admin
from .models import Anime, Episodio

admin.site.register(Anime)
admin.site.register(Episodio) # Habilitamos los episodios en el panel