from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=20)
    liked_movies = models.ManyToManyField("movies.Movie", related_name='liked_users')
    following = models.ManyToManyField("self", symmetrical=False, related_name='followers')
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
