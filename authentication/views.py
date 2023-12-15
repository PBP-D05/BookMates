from django.http import JsonResponse

from .models import Pengguna
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Pengguna

@csrf_exempt
def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    is_teacher = True if request.POST.get('is_teacher') else False  # Assuming is_teacher is sent from Flutter

    # Check if the username already exists
    if User.objects.filter(username=username).exists():
        return JsonResponse({"status": False, "message": "Username sudah digunakan."}, status=400)

    # Create a new User instance
    user = User.objects.create_user(username=username, password=password)
    user.save()

    # Create a new Pengguna instance and associate it with the user
    Pengguna.objects.create(user=user, isGuru=is_teacher, point=0, banyak_review=0, banyak_bintang=0).save()
    
    return JsonResponse({"username": user.username, "status": True, "message": "Register successful!"}, status=201)

@csrf_exempt
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    
    user = authenticate(username=username, password=password)

    if user is not None:
        auth_login(request, user)
        try:
            pengguna = Pengguna.objects.get(user=user)
            return JsonResponse({
                "username": user.username,
                "is_teacher": pengguna.isGuru,
                "point": pengguna.point,
                "banyakReview": pengguna.banyak_review,
                "banyakBintang" : pengguna.banyak_bintang,
                "status": True,
                "message": "Login sukses!"
            }, status=200)
        except Pengguna.DoesNotExist:
            return JsonResponse({
                "status": False,
                "message": "Pengguna tidak ditemukan."
            }, status=401)
    else:
        return JsonResponse({
            "status": False,
            "message": "Login gagal, periksa kembali username atau password."
        }, status=401)


@login_required
@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout berhasil!"
        }, status=200)
    except:
        return JsonResponse({
            "status": False,
            "message": "Logout gagal."
        }, status=401)
