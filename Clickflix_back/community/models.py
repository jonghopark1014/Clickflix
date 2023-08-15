from django.db import models
from movies.models import Movie
from django.conf import settings

# Create your models here.
class Review(models.Model):  
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='review_user')
    title = models.CharField(max_length=100)
    point = models.FloatField()
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class Comment(models.Model):  
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_comment')
    review = models.ForeignKey(Review, on_delete = models.CASCADE)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class MachineComment(models.Model):  
    content = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class FamousLine(models.Model):  
    content = models.CharField(max_length=100)
    speaker = models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

class SearchHistory(models.Model):  
    context = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)