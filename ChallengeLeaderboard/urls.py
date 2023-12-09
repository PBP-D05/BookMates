from django.urls import path
from . import views

app_name = 'ChallengeLeaderboard'

urlpatterns = [
    path('challenge/<str:name>', views.challenge, name='challenge'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('ranking/', views.get_ranking, name='get_ranking'),
    path('reviews/<str:book_pk>', views.get_reviews, name='get_reviews'),
    path('get_reply/<str:challenge_name>', views.get_reply, name='get_reply'),
    path('post_reply/', views.post_reply, name='post_reply'),
    path('post_nilai/', views.post_nilai, name='post_nilai'),
    path('get_top10/<str:komunitas>', views.get_top10, name='get_top10'),
    path('get_rank/<str:komunitas>', views.get_rank, name='get_top10')
]