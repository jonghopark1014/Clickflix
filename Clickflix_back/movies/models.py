from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name = models.CharField(max_length=50)

class Keyword(models.Model):  
    name = models.CharField(max_length = 1000)

class Provider(models.Model):  
    logo_path= models.CharField(max_length=1000)
    provider_name = models.CharField(max_length = 500)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField(null = True)
    popularity = models.FloatField(null = True)
    vote_count = models.IntegerField(null = True)
    vote_average = models.FloatField(null = True)
    overview = models.TextField(null = True)
    adult = models.BooleanField(null=True)
    runtime = models.IntegerField(null=True)
    poster_path = models.CharField(max_length=200, null = True)
    backdrop_path = models.CharField(max_length=300, null = True)
    youtube_key = models.CharField(max_length=100, null = True)
    genres = models.ManyToManyField(Genre, related_name='genres_movie')
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie')
    actors = models.ManyToManyField(Actor, related_name='actors_movie')
    keywords = models.ManyToManyField(Keyword, related_name='keywords_movie')
    providers = models.ManyToManyField(Provider, related_name='provider_movie')
    wish_watch = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'wish_movie')
    is_watched = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'watched_movie')

class LikeGenre(models.Model):  
    point = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    check_movie = models.ManyToManyField(Movie)

class LikeKeyword(models.Model):  
    point = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    keyword = models.ForeignKey(Keyword, on_delete=models.CASCADE)
    check_movie = models.ManyToManyField(Movie)

class LikeActor(models.Model):  
    point = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    check_movie = models.ManyToManyField(Movie)

class Actorcharacter(models.Model):  
    actor = models.ManyToManyField(Actor)
    character = models.CharField(max_length = 1000)

class Actorasknown(models.Model):  
    actor = models.ManyToManyField(Actor)
    asknown = models.CharField(max_length= 1000)