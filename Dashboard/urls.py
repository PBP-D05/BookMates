from django.urls import path
from Dashboard.views import show_main

app_name = 'Dashboard'

urlpatterns = [
    path('', show_main, name='show_main'),
]