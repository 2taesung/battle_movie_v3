from typing import AbstractSet
from django.db import models
from django.conf import settings
from django.db.models.fields import TextField

# Create your models here.
class Movie(models.Model):
    title =  models.CharField(max_length=300)
    overview = models.TextField()
    poster_path = models.TextField(null=True)
    vote_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='vote_movies')

class Community(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    movie_title_1 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='vote_left')
    movie_title_2 = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='vote_right')
    # content = models.TextField()  # 이 친구도 같이 해줘야하나?
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.title



