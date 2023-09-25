import django_filters
from spotifyapp.models import Artist, SpotifyStats

class ArtistFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label="Artist Name",
        lookup_expr='icontains'
    )

    class Meta:
        model = Artist
        fields = ['name']