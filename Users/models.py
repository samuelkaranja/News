from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    country = CountryField(multiple=True)

    def __str__(self):
        return self.firstName
