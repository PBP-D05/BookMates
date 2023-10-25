from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pengguna(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isGuru = models.BooleanField()

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    rating = models.FloatField()
    num_of_rating = models.IntegerField()
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    desc = models.TextField()
    user = models.ForeignKey(Pengguna, on_delete=models.CASCADE)