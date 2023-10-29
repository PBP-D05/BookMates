from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import datetime

from . import models
from MengelolaBuku.models import Pengguna

def leaderboard(request):
    return render(request, 'leaderboard.html')

@csrf_exempt
def get_reply(request, challenge_name: str):
    challenge = _get_or_404(models.Challenge, name=challenge_name)
    if type(challenge) is HttpResponseNotFound:
        return challenge

    dct = []
    for reply in challenge.reply.all():
        dct.append(json.dumps({'user': reply.user.username, 'text': reply.text, 'datetime': reply.datetime.strftime("%B %d, %Y %H:%M"), 'point': reply.point}))

    return HttpResponse(dct, content_type='application/json')

@csrf_exempt
def post_reply(request, challenge_name: str, text: str):
    challenge: models.Challenge = _get_or_404(models.Challenge, name=challenge_name)
    if type(challenge) is HttpResponseNotFound:
        return challenge
    
    challenge = challenge.reply.get_or_create(user=request.user)
    challenge.text = text
    challenge.save()
    return HttpResponse("OK")

def challenge(request, name: str):
    if request.method == 'POST':
        challenge_name = request.POST.get('challenge')
        challenge = models.Challenge.objects.get(name=challenge_name)
        challenge.reply += f"<CLS>{request.user.username}<SEP>{request.POST.reply}"
        challenge.save(update_fields=['reply'])
        return HttpResponseRedirect('ChallengeLeaderboard:challenge')
    
    challenge: models.Challenge = _get_or_404(models.Challenge, name=name)
    if type(challenge) is HttpResponseNotFound:
        return challenge
    
    # TODO: CONFIGURE SET USER 
    USER = 1
    isreply = _get_or_404(challenge.reply, user=USER)
    isreply = None if type(isreply) is HttpResponseNotFound else isreply

    isguru = Pengguna.objects.get(user=USER).isGuru

    context = dict(
        name = challenge.name,
        datetime = challenge.deadline.strftime("%B %d, %Y %H:%M"),
        point = challenge.point,
        description = challenge.description,
        book = challenge.book,
        showReply = not isreply,
        isguru = isguru
    )
    return render(request, 'challenge.html', context=context)


#################### HELPER FUNCTION ####################
def _get_or_404(model, **kwargs):
    try:
        if hasattr(model, 'objects'):
            data = model.objects.get(**kwargs)
        elif hasattr(model, 'get'):
            data = model.get(**kwargs)
        else:
            raise NotImplementedError('Model type not implemented')
    except Exception as e:
        return HttpResponseNotFound()
    return HttpResponseNotFound() if data is None else data