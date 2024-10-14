from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Movie(models.Model):
    movie_id = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=200, null=True)
    backdrop_path = models.CharField(max_length=200, null=True)
    vote_avg = models.FloatField()
    vote_count = models.IntegerField()
    adult = models.BooleanField()
    released_date = models.DateField()
    now_playing = models.BooleanField()
    coming_soon = models.BooleanField()
    runtime = models.IntegerField(default=-1)
    belongs_to_collection = models.JSONField(null=True)
    box_office = models.BooleanField()
    popularity = models.FloatField()

    def __str__(self):
        return self.title