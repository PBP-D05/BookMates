from django.urls import path
from Komunitas.views import *

app_name = 'Komunitas'

urlpatterns = [
    path('komunitas/', community_detail, name='community_detail'),
]