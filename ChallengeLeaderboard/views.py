from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import Http404

from . import models

def leaderboard(request):
    context = {
        'komunitas': models.Challenge.objects.get()
    }
    return render(request, 'leaderboard.html')

def challenge(request, name: str):
    if request.method == 'POST':
        challenge_name = request.POST.get('challenge')
        challenge = models.Challenge.objects.get(name=challenge_name)
        challenge.reply += f"<CLS>{request.user.username}<SEP>{request.POST.reply}"
        challenge.save(update_fields=['reply'])
        return HttpResponseRedirect('ChallengeLeaderboard:challenge')
    
    # challenge = models.Challenge.objects.get(name=name)
    # if not challenge:
    #     return Http404()
    
    # my_reply = None
    # username = []
    # replies = []
    # for reply in my_reply.split('<CLS> '):
    #     if reply == '': continue
    #     separator = reply.find("<CLS>")
    #     username.append(reply[:separator])
    #     replies.append(reply[separator+5:])
        
    #     if username[-1] == request.user.username:
    #         my_reply = replies[-1]

    # context = {
    #     'challenge' : challenge,
    #     'my_reply' : my_reply,
    #     'username' : username,
    #     'replies': replies,
    # }
    return render(request, 'challenge.html')