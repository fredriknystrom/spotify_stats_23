from django.urls import path
from spotifyapp.views import artist, song

urlpatterns = [
    path('song-search/', song.SongSearchView.as_view(), name='song-search'),
    path('artist-search/', artist.ArtistSearchView.as_view(), name='artist-search'),
    path('artist-info/<str:artist_name>/', artist.ArtistInfoView.as_view(), name='artist-info'),
    path('song-info/<int:song_pk>/', song.SongInfoView.as_view(), name='song-info'),
]
