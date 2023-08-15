from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):  
    # 추가 필드 followings, point
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    point_genre = models.IntegerField(null = True)
    point_keyword = models.IntegerField(null = True)
    nickname = models.CharField(max_length = 100)
    birthday = models.DateField()
    username = models.EmailField(max_length=247, blank=False, unique=True, error_messages={
            'unique': ('A user with this email already exists.'),
            'invalid': ('Invalid e-mail address detected.'),
            'blank': ('this field may not be blank.')
            })
    
    def __str__(self):
        return self.username