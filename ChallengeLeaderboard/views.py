from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, HttpResponseBadRequest, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import json
import datetime

from . import models
from MengelolaBuku.models import Pengguna, Buku, User

USERNAME = 'root'

@csrf_exempt
def get_username(request, pk: int):
    user = Pengguna.objects.get(pk=pk)
    return JsonResponse(json.dumps({'username': user.user.username}), safe=False, status=200)

@csrf_exempt
def get_current_username(request):
    user = request.user
    return JsonResponse(json.dumps({'username': user.username}), safe=False, status=200)

# NEW ENDPOINT 
def get_ranking(request):
    """
        Return JSON list contains Nama, banyak yang direview, status, banyak bintang total
    """
    all_pengguna = Pengguna.objects.all()
    return JsonResponse(serializers.serialize('json', all_pengguna), safe=False)

@csrf_exempt
def get_reviews(request, book_pk:str):
    """
        Return JSON list of reviews
    """
    buku = Buku.objects.get(pk=book_pk)
    all_reviews = models.Reviews.objects.filter(buku=buku)
    return JsonResponse(serializers.serialize('json', all_reviews), safe=False)

@csrf_exempt
def post_reviews(request):
    """
        Body:
            pk: pk a book
            text: review's  text
            rating: int [1, 5] of rating
    """
    try:
        data = json.loads(request.body)

        pk = int(data['pk'])
        text = data['text']
        rating = float(data['rating'])
        user = Pengguna.objects.get(user=request.user)

        buku = Buku.objects.get(pk=pk)
        new_review = models.Reviews.objects.create(buku=buku, user=user, text=text, rating=rating).save()

        user.banyak_bintang += rating
        user.banyak_review += 1
        user.save(update_fields=['banyak_bintang', 'banyak_review'])
        return JsonResponse({'status': 'ok'}, status=200)
    except ValueError as e:
        print(e)
        return JsonResponse({'status': 'error'}, status=401)

########################

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
    print('CHALLENGE', challenge, challenge.reply.all())
    for reply in challenge.reply.all():
        dct.append({
            'user': reply.user.username,
            'text': reply.text,
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

    print(f'EDIT NILAI REQUEST on {username}')
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
    
    print('Halo halo')
    my_reply, created = models.NewReply.objects.get_or_create(user=user, text=text, point= 0)
    print('CREATED', created)

    if created:
        challenge.reply.add(my_reply)
    else:
        my_reply.text = text
        my_reply.save(update_fields=['text'])

        if my_reply not in challenge.reply.all():
            challenge.reply.add(my_reply)
    

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