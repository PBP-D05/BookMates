from django.db import models
import random
import string
from django.contrib.auth.models import User

# Create your models here.
def generate_join_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

class Community(models.Model):
    name = models.CharField(max_length = 255, default="anonymous" )
    title = models.CharField(max_length = 255)
    description = models.CharField(max_length = 1000, blank = True)
    date_created = models.DateTimeField(auto_now_add = True, null = True)
    join_code = models.CharField(max_length=6, default=generate_join_code, unique=True)
    members = models.ManyToManyField(User, related_name="communities_joined")
    
    def __str__(self):
        return str(self.title)