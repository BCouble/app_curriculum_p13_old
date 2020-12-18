from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.urls import reverse


class Zvitae(models.Model):
    """ Model Title & description """
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=255)

    class Meta:
        db_table = 'zvitae'

    def __str__(self):
        return self.title


class Address(models.Model):
    """ Model Food of OpenFoodFact """
    zvitae_link_add = models.ForeignKey(Zvitae, on_delete=models.CASCADE)
    number = models.IntegerField()
    address = models.CharField(max_length=200)
    address2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    postal_code = models.IntegerField()


class CivilState(models.Model):
    """ Model Food of OpenFoodFact """
    zvitae_link_cs = models.ForeignKey(Zvitae, on_delete=models.CASCADE)
    age = models.IntegerField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=12)
    linkedin = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    driving_licence = models.CharField(max_length=200, null=True)
