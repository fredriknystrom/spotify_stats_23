from django.views.generic import DetailView
from django_filters.views import FilterView
from spotifyapp.models import SpotifyStats
from spotifyapp.filters.song_filter import SongFilter

class SongSearchView(FilterView):
    model = SpotifyStats
    filterset_class = SongFilter
    template_name = 'spotifyapp/song_search.html'

    def get_queryset(self):
        # Get the queryset based on the filter settings
        queryset = super().get_queryset()

        # Order the queryset by the "streams" field in ascending order
        queryset = queryset.order_by('-streams')

        return queryset

class SongInfoView(DetailView):
    model = SpotifyStats
    template_name = 'spotifyapp/song_info.html'
    context_object_name = 'song'
    pk_url_kwarg = 'song_pk'  # Define the URL keyword for the song's primary key

    def get_queryset(self):
        return SpotifyStats.objects.all()
