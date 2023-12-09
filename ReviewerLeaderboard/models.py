from django.db import models
from MengelolaBuku.models import Pengguna

class Leaderboard(models.Model):
    user = models.OneToOneField(Pengguna, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    is_guru = models.BooleanField()
    banyak_review = models.IntegerField(default=0)
    banyak_bintang = models.IntegerField(default=0)

    def __str__(self):
        return self.user.user.username  # Display username in the admin panel

    class Meta:
        ordering = ['-points']  # Order the leaderboard by points in descending order
