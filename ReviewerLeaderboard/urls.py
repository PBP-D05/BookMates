from django.urls import path
from . import views

app_name = 'ReviewerLeaderboard'

urlpatterns = [
    path('leaderboard/', views.leaderboard_view, name='leaderboard'),
]
