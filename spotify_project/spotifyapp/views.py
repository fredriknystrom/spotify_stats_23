from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse

from .models import Artist

def artist_search(request):
    artists = Artist.objects.all()
    return render(request, 'spotifyapp/search_artist.html', {'artists': artists})

def song_search(request):
    return render(request, 'spotifyapp/search_song.html', {})
