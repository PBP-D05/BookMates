from django.db import models

from MengelolaBuku.models import Buku
from django.contrib.auth.models import User

from Komunitas.models import Community

class Reply(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    datetime = models.DateTimeField()
    point = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.user.username +" : "+ self.text

class Challenge(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE, null=False)
    name = models.TextField(primary_key=True)
    point = models.IntegerField()
    deadline = models.DateTimeField()
    description = models.TextField()
    book = models.ForeignKey(Buku, on_delete=models.CASCADE)
    reply = models.ManyToManyField(Reply, default=set, blank=True)

    def __str__(self) -> str:
        return self.name
    