from django.urls import path
from . import views

app_name = 'ChallengeLeaderboard'

urlpatterns = [
    path('challenge/<str:name>', views.challenge, name='challenge'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),

    path('get_reply/<str:challenge_name>', views.get_reply, name='get_reply'),
    path('post_reply/<str:challenge_name>', views.post_reply, name='post_reply')

]