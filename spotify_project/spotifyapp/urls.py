from django.urls import path
from . import views

urlpatterns = [
    path('search-song/', views.song_search, name='song-search'),
    path('search-artist/', views.artist_search, name='artist-search'),
]
