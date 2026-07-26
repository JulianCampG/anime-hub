from django.db import models
from django.contrib.auth.models import User

class Anime(models.Model):
    titulo = models.CharField(max_length=200)
    sinopsis = models.TextField()
    fecha_estreno = models.DateField()
    genero = models.CharField(max_length=100)
    calificacion = models.FloatField(default=0.0)
    imagen_url = models.URLField(max_length=500, blank=True, null=True, help_text="Enlace URL de la imagen de portada")
    trailer_url = models.URLField(max_length=500, blank=True, null=True, help_text="URL de YouTube (ej. https://www.youtube.com/embed/...)")
    
    # Relaciones con Usuarios (Favoritos y Vistos)
    favoritos = models.ManyToManyField(User, related_name='animes_favoritos', blank=True)
    vistos = models.ManyToManyField(User, related_name='animes_vistos', blank=True)
    
    def __str__(self):
        return self.titulo

class Episodio(models.Model):
    # Esto conecta cada episodio con su anime correspondiente
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE, related_name='episodios')
    numero = models.IntegerField(help_text="Número del episodio (ej. 1)")
    titulo = models.CharField(max_length=200, help_text="Título del episodio")
    video_url = models.URLField(max_length=700, help_text="Enlace del video o Embed Code")

    def __str__(self):
        return f"{self.anime.titulo} - Episodio {self.numero}: {self.titulo}"