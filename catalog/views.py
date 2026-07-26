from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Anime, Episodio

def home(request):
    query = request.GET.get('q', '')
    animes = Anime.objects.filter(titulo__icontains=query) if query else Anime.objects.all()

    favorito_ids = set()
    visto_ids = set()
    if request.user.is_authenticated:
        favorito_ids = set(request.user.animes_favoritos.values_list('id', flat=True))
        visto_ids = set(request.user.animes_vistos.values_list('id', flat=True))

    return render(request, 'catalog/home.html', {
        'animes': animes,
        'query': query,
        'favorito_ids': favorito_ids,
        'visto_ids': visto_ids,
    })

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
@require_POST
def toggle_favorito(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    if anime.favoritos.filter(id=request.user.id).exists():
        anime.favoritos.remove(request.user)
        messages.success(request, f'"{anime.titulo}" eliminado de favoritos.')
    else:
        anime.favoritos.add(request.user)
        messages.success(request, f'"{anime.titulo}" agregado a favoritos ❤️')
    return redirect(request.POST.get('next') or 'home')

@login_required
@require_POST
def toggle_visto(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    if anime.vistos.filter(id=request.user.id).exists():
        anime.vistos.remove(request.user)
        messages.success(request, f'"{anime.titulo}" desmarcado como visto.')
    else:
        anime.vistos.add(request.user)
        messages.success(request, f'"{anime.titulo}" marcado como visto 👁️')
    return redirect(request.POST.get('next') or 'home')

@login_required
def perfil(request):
    favoritos = request.user.animes_favoritos.all()
    vistos = request.user.animes_vistos.all()
    
    return render(request, 'catalog/perfil.html', {
        'favoritos': favoritos,
        'vistos': vistos
    })

def anime_detalle(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    episodios = anime.episodios.all().order_by('numero')

    favorito_ids = set()
    visto_ids = set()
    if request.user.is_authenticated:
        favorito_ids = {anime.id} if anime.favoritos.filter(id=request.user.id).exists() else set()
        visto_ids = {anime.id} if anime.vistos.filter(id=request.user.id).exists() else set()

    return render(request, 'catalog/anime_detalle.html', {
        'anime': anime,
        'episodios': episodios,
        'favorito_ids': favorito_ids,
        'visto_ids': visto_ids,
    })

@login_required
def ver_episodio(request, episodio_id):
    episodio = get_object_or_404(Episodio, id=episodio_id)
    anime = episodio.anime
    episodios = anime.episodios.order_by('numero')
    prev_episodio = anime.episodios.filter(numero__lt=episodio.numero).order_by('-numero').first()
    next_episodio = anime.episodios.filter(numero__gt=episodio.numero).order_by('numero').first()

    return render(request, 'catalog/ver_episodio.html', {
        'episodio': episodio,
        'episodios': episodios,
        'prev_episodio': prev_episodio,
        'next_episodio': next_episodio,
    })