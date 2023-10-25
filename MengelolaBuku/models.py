from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Guru(models.Model):
    user = models.OneToOneField(User)
    isGuru = models.BooleanField()

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    min_age = models.IntegerField()
    max_age = models.IntegerField()
    desc = models.TextField()
    user = models.ForeignKey(Guru, on_delete=models.CASCADE)