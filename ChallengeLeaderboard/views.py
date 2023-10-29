from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import datetime

from . import models
from MengelolaBuku.models import Pengguna

def leaderboard(request):

    # TODO: CONFIGURE SET USER 
    USER = 'root'
    user = models.User.objects.get(username=USER)

    komunitas_joined = []
    for komunitas in models.Community.objects.all():
        if user in komunitas.members.all():
            komunitas_joined.append(komunitas)

    context = {
        'komunities' : komunitas_joined,
    }
    return render(request, 'leaderboard.html', context=context)

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
def post_nilai(request):
    if request.method != 'POST' or request.POST.get('user') is None or request.POST.get('value') is None or request.POST.get('challenge_name') is None:
        return HttpResponseBadRequest('Not a Valid request')
    username = request.POST.get('user')
    new_point = request.POST.get('value')
    challenge_name = request.POST.get('challenge_name')


    user = models.User.objects.get(username=username)
    # print("USER", user)
    pengguna = Pengguna.objects.get(user=user)
    # print("PENGGUNA", pengguna)
    # print("CHALLENGE_NAME", challenge_name)
    reply = models.Challenge(name=challenge_name).reply
    # print("REPLY", reply)
    myReply = reply.get(user=user)
    # print("PENGGUNA", pengguna)

    old_point = myReply.point
    myReply.point = new_point
    myReply.save(update_fields=['point'])

    pengguna.point -= old_point
    pengguna.point += int(new_point)
    pengguna.save(update_fields=['point'])

    return HttpResponse(f"Old Point {old_point}, New Point {myReply.point}, Pengguna Point {pengguna.point}")

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