from django.db import models

# Create your models here.
class Movies(models.Model):
    movie_name=models.CharField(max_length=64)
    type=models.CharField(max_length=64)
    rank=models.CharField(max_length=64)
    casting=models.CharField(max_length=64)
    release_date=models.CharField(max_length=64)
