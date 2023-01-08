from django.db import models


# Create your models here.

class Users(models.Model):
    ID = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=33)
    LastName = models.CharField(max_length=33)
    Email = models.EmailField(max_length=33)
    PassWord = models.CharField(max_length=33)
