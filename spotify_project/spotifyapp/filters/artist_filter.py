import django_filters
from spotifyapp.models import Artist, SpotifyStats
from django import forms

class ArtistFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        label="Artist Name",
        lookup_expr='icontains',
        widget=forms.TextInput(
        attrs={ "class":"form-control",
               "placeholder": "Enter artist here...",
               "style": "width: 636px;"}
        )
    )

    class Meta:
        model = Artist
        fields = ['name']