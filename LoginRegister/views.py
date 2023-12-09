from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from Dashboard.views import show_main
from MengelolaBuku.models import Pengguna

# Create your views here.
def show_xml(request):
    data = Pengguna.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Pengguna.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Pengguna.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Pengguna.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_home(request):
    return render(request, 'home.html')

def user_register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        isGuru = request.POST.get('isGuru')
        if form.is_valid():
            new_user = form.save()
            isGuru = request.POST.get('isGuru') == 'on'
            Pengguna.objects.create(user=new_user, isGuru=isGuru, point=0).save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('LoginRegister:show_home')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = RegistrationForm()
    
    context = {'form': form}
    return render(request, 'register.html', context)

def user_login(request):
    if request.method == 'POST':
        print('Welcome')
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Create or get the Pengguna instance for the logged-in user
            created = Pengguna.objects.get_or_create(user=user, defaults={'isGuru': False, 'point': 0})
             # Additional logic if needed based on whether the instance was created or not
            if created:
                messages.success(request, 'Welcome! Your Pengguna instance has been created.')
            else:
                messages.success(request, 'Welcome back!')
            response = HttpResponseRedirect(reverse("Dashboard:show_main"))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

@login_required(login_url='/login')
def user_logout(request):
    logout(request)
    response = HttpResponseRedirect(reverse('LoginRegister:show_home'))
    return response 