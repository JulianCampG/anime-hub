from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Anime, Episodio

def home(request):
    # Capturamos lo que el usuario busque en la barra
    query = request.GET.get('q', '')
    if query:
        animes = Anime.objects.filter(titulo__icontains=query)
    else:
        animes = Anime.objects.all()
        
    return render(request, 'catalog/home.html', {
        'animes': animes,
        'query': query
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
def toggle_favorito(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    if request.user in anime.favoritos.all():
        anime.favoritos.remove(request.user)
    else:
        anime.favoritos.add(request.user)
    return redirect('home')

@login_required
def toggle_visto(request, anime_id):
    anime = get_object_or_404(Anime, id=anime_id)
    if request.user in anime.vistos.all():
        anime.vistos.remove(request.user)
    else:
        anime.vistos.add(request.user)
    return redirect('home')

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
    # Trae todos los episodios de ese anime, ordenados por número
    episodios = anime.episodios.all().order_by('numero')
    
    return render(request, 'catalog/anime_detalle.html', {
        'anime': anime,
        'episodios': episodios
    })

@login_required
def ver_episodio(request, episodio_id):
    episodio = get_object_or_404(Episodio, id=episodio_id)
    return render(request, 'catalog/ver_episodio.html', {
        'episodio': episodio
    })