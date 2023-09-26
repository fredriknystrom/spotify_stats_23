from django.db import models
from django.utils import timezone

class Artist(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

PERCENTAGE_CHOICES = (
    (1, 'Low'),
    (2, 'Medium'),
    (3, 'High')
)

class SpotifyStats(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    artists = models.ManyToManyField(Artist)
    released_date = models.DateField(default=timezone.now)
    in_spotify_playlists = models.PositiveIntegerField()
    in_spotify_charts = models.PositiveIntegerField()
    streams = models.PositiveIntegerField()
    bpm = models.PositiveIntegerField()
    danceability_percentage = models.PositiveSmallIntegerField(choices=PERCENTAGE_CHOICES)
    energy_percentage = models.PositiveSmallIntegerField(choices=PERCENTAGE_CHOICES)
    acousticness_percentage = models.PositiveSmallIntegerField(choices=PERCENTAGE_CHOICES)
    speechiness_percentage = models.PositiveSmallIntegerField(choices=PERCENTAGE_CHOICES)

    def __str__(self):
        return f"{self.title}, {self.artists}"