from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import Anime, Episodio


@login_required
def home(request):
    """Vista principal o catálogo de animes (Protegida)"""
    animes = Anime.objects.all()
    return render(request, "catalog/home.html", {"animes": animes})


@login_required
def anime_detalle(request, anime_id):
    """Vista de detalles y lista de episodios de un anime"""
    anime = get_object_or_404(Anime, id=anime_id)
    return render(request, "catalog/anime_detalle.html", {"anime": anime})


@login_required
def ver_episodio(request, episodio_id):
    """Vista para reproducir el episodio seleccionado"""
    episodio = get_object_or_404(Episodio, id=episodio_id)
    return render(request, "catalog/ver_episodio.html", {"episodio": episodio})


@login_required
def perfil(request):
    """Vista del perfil de usuario con sus favoritos y vistos"""
    return render(request, "catalog/perfil.html")


@login_required
def registro(request):
    """Vista de registro (puedes ajustarla según tu formulario de registro)"""
    # Si usas un formulario de registro personalizado, colócalo aquí
    return render(request, "catalog/registro.html")


@login_required
def toggle_favorito(request, anime_id):
    """Agregar o quitar de favoritos"""
    anime = get_object_or_404(Anime, id=anime_id)
    if request.user in anime.favoritos.all():
        anime.favoritos.remove(request.user)
    else:
        anime.favoritos.add(request.user)
    return redirect("anime_detalle", anime_id=anime.id)


@login_required
def toggle_visto(request, anime_id):
    """Marcar como visto o no visto"""
    anime = get_object_or_404(Anime, id=anime_id)
    if request.user in anime.vistos.all():
        anime.vistos.remove(request.user)
    else:
        anime.vistos.add(request.user)
    return redirect("anime_detalle", anime_id=anime.id)