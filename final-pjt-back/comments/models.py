from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator

# Create your models here.
class Review(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='like_reviews', blank=True
    )

class Comment(models.Model):
    content = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True
    )