from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render

# Importa tus modelos (asegúrate de que coincidan con los nombres reales de tus modelos)
from .models import Anime, Capitulo


@login_required
def home(request):
    """Vista principal o catálogo de animes (Protegida)"""
    animes = Anime.objects.all()
    # Si manejas vistos recientemente o favoritos, inclúyelos aquí en el contexto
    return render(request, 'catalog/home.html', {'animes': animes})


@login_required
def anime_detalle(request, anime_id):
    """Vista de detalles del anime seleccionado (Protegida)"""
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, 'catalog/anime_detalle.html', {'anime': anime})


@login_required
def ver_capitulo(request, capitulo_id):
    """Vista del reproductor de episodios (Protegida contra accesos directos sin sesión)"""
    capitulo = get_object_or_404(Capitulo, id=capitulo_id)
    return render(request, 'catalog/ver_episodio.html', {'capitulo': capitulo})


@login_required
def perfil_usuario(request):
    """Vista del perfil de usuario (Protegida)"""
    return render(request, 'catalog/perfil.html')