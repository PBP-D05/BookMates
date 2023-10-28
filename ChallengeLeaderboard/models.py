from django.db import models

from MengelolaBuku.models import Buku
from django.contrib.auth.models import User

class Challenge(models.Model):
    # community = models.ForeignKey(Community) Model Fathur
    name = models.TextField(primary_key=True)
    point = models.IntegerField()
    deadline = models.DateTimeField()
    description = models.TextField()
    books = models.ForeignKey(Buku, on_delete=models.RESTRICT)
    reply = models.TextField() # encoded <CLS> NAME <SEP> REPLY <CLS>

    