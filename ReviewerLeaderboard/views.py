from django.shortcuts import render
from .models import Leaderboard

def leaderboard_view(request):
    leaderboard_entries = Leaderboard.objects.all()
    return render(request, 'LeaderboardReviewer.html', {'leaderboard_entries': leaderboard_entries})

from django.shortcuts import render
from .models import Leaderboard

def leaderboard_view(request):
    leaderboard_entries = Leaderboard.objects.all()
    return render(request, 'leaderboard.html', {'leaderboard_entries': leaderboard_entries})
