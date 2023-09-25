import django_filters
from spotifyapp.models import SpotifyStats

class SongFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        label="Song Title",
        lookup_expr='icontains'
    )

    class Meta:
        model = SpotifyStats
        fields = ['title']