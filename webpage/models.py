from django.db import models


# Create your models here.
class Post(models.Model):
    userid = models.CharField(max_length=12, unique=True)
    password = models.CharField(max_length=12, unique=False)
    name = models.CharField(max_length=50, unique=False)
    address = models.CharField(max_length=50, unique=False)
    country = models.CharField(max_length=20, unique=False)
    zipcode = models.CharField(max_length=10, unique=False)
    email = models.CharField(max_length=50, unique=True)
    sex = models.CharField(max_length=10, unique=False)
    lang = models.CharField(max_length=20, unique=False)
    desc = models.TextField()
