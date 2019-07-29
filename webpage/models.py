from django.db import models


# Create your models here.
class Post(models.Model):
    userid = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=20, unique=True)
    zipcode = models.CharField(max_length=10, unique=True)
    email = models.CharField(max_length=50, unique=True)
    sex = models.CharField(max_length=10, unique=True)
    lang = models.CharField(max_length=20, unique=True)
    desc = models.TextField()
