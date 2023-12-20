from django.urls import path
from authentication.views import leaderboard, login,register, logout

app_name = 'authentication'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('leaderboard/', leaderboard, name='leaderboard'),
    path('logout/', logout, name='logout'),
]