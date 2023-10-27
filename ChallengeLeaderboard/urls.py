from django.urls import path
from . import views

appname = 'ChallengeLeaderboard'

urlpatterns = [
    path('challenge/<str:name>', views.challenge, name='challenge'),
    path('leaderboard/', views.leaderboard, name='leaderboard')
]