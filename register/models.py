from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """ Custom User for background profile and genre add """
    FEMALE = 'F'
    MALE = 'M'
    NULL = 'O'
    GENRE_CHOICES = [(FEMALE, 'femme'), (MALE, 'homme'), (NULL, 'non définit'), ]
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES, default=NULL, )
    limit = models.IntegerField(default=1)
