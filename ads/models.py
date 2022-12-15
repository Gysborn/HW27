from django.db import models


class Ad(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    price= models.PositiveIntegerField()
    description = models.TextField()
    address = models.TextField(max_length=500)
    is_published = models.BooleanField()


class Categories(models.Model):
    name = models.CharField(max_length=200, unique=True)