from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import datetime

from . import models
from MengelolaBuku.models import Pengguna

USERNAME = 'root'

def leaderboard(request):
    # TODO: CONFIGURE SET USER 
    user = models.User.objects.get(username=USERNAME)

    komunitas_joined = []
    for komunitas in models.Community.objects.all():
        if user in komunitas.members.all():
            komunitas_joined.append(komunitas)

    context = {
        'komunities' : komunitas_joined,
        'user' : user
    }
    return render(request, 'leaderboard.html', context=context)

@csrf_exempt
def get_rank(request, komunitas):
    # TODO: CONFIGURE USERNAME
    # username = request.user.username
    username = USERNAME

    komunitas = models.Community.objects.get(name=komunitas)
    pengguna_all = [Pengguna.objects.get(user=user) for user in komunitas.members.all()]
    pengguna_point = sorted([(pengguna, pengguna.point) for pengguna in pengguna_all], key=lambda x: x[1], reverse=True)
    for position, (pengguna, point) in enumerate(pengguna_point):
        if pengguna.user.username == username:
            return JsonResponse({'position': position+1, 'name': username, 'point': point})
    return JsonResponse({'position': '-', 'name': username, 'point': 0})

@csrf_exempt
def get_top10(request, komunitas):
    komunitas = models.Community.objects.get(name=komunitas)
    member_point = []
    for member in komunitas.members.all():
        pengguna = Pengguna.objects.get(user=member)
        member_point.append((member, pengguna.point))
    member_point = sorted(member_point, key=lambda x: x[1], reverse=True)
    data = [{'name': member.username, 'point': point} for member, point in member_point]

    return JsonResponse(data, safe=False)  # Use JsonResponse to return JSON data

@csrf_exempt
def get_teacher(request):
    # TODO
    komunitas_name = request.GET.get('komunitas')
    komunitas = models.Community.objects.get(name=komunitas_name)
    return HttpResponseNotFound("Page not Implemented")

@csrf_exempt
def get_reply(request, challenge_name: str):
    challenge = _get_or_404(models.Challenge, name=challenge_name)
    if type(challenge) is HttpResponseNotFound:
        return challenge

    dct = []
    for reply in challenge.reply.all():
        dct.append({
            'user': reply.user.username,
            'text': reply.text,
            'datetime': reply.datetime.strftime("%B %d, %Y %H:%M"),
            'point': reply.point
        })

    return JsonResponse(dct, safe=False)


@csrf_exempt
def post_nilai(request):
    if request.method != 'POST' or request.POST.get('user') is None or request.POST.get('value') is None or request.POST.get('challenge_name') is None:
        return HttpResponseBadRequest('Not a Valid request')
    username = request.POST.get('user')
    new_point = request.POST.get('value')
    challenge_name = request.POST.get('challenge_name')


    user = models.User.objects.get(username=username)
    pengguna = Pengguna.objects.get(user=user)
    reply = models.Challenge(name=challenge_name).reply
    myReply = reply.get(user=user)

    old_point = myReply.point
    myReply.point = new_point
    myReply.save(update_fields=['point'])

    pengguna.point -= old_point
    pengguna.point += int(new_point)
    pengguna.save(update_fields=['point'])

    return HttpResponse(f"Old Point {old_point}, New Point {myReply.point}, Pengguna Point {pengguna.point}")

@csrf_exempt
def post_reply(request):
    challenge_name = request.POST.get('challenge_name')
    text = request.POST.get('text')
    # TODO: CONFIGURE USERNAME
    # user = request.user
    user = models.User.objects.get(username=USERNAME)

    print("DATA SUBMITTED : ", challenge_name, text)

    challenge: models.Challenge = _get_or_404(models.Challenge, name=challenge_name)
    if type(challenge) is HttpResponseNotFound:
        return challenge
    
    my_reply = None
    for reply in challenge.reply.all():
        if reply.user == user:
            my_reply = reply
            break

    if my_reply is None:
        reply = models.Reply.objects.create(user=user, text=text, datetime=datetime.datetime.now(), point=0)
        challenge.reply.add(reply)
    else:
        my_reply.text = text
        my_reply.save(update_fields=['text'])
    return HttpResponse("OK")

def challenge(request, name: str):
    challenge: models.Challenge = _get_or_404(models.Challenge, name=name)
    if type(challenge) is HttpResponseNotFound:
        return challenge
    
    # TODO: CONFIGURE SET USER 
    # request.user
    user = models.User.objects.get(username=USERNAME)
    isreply = _get_or_404(challenge.reply, user=user)
    isreply = None if type(isreply) is HttpResponseNotFound else isreply

    isguru = Pengguna.objects.get(user=user).isGuru

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