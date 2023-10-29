from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Community, Pengguna
from django.db.models.functions import Lower

# Create your views here.

def show_main(request):
    community = list(Community.objects.filter(members=request.user.id).order_by('name'))
    pengguna = Pengguna.objects.get(user=request.user)
    is_guru = pengguna.isGuru
    context = {
        'name': request.user,
        'community': community,
        'is_guru' : is_guru,
    }
    return render(request, "dashboard_user.html", context)

def cek_guru(request):
    if request.user.isGuru == True:
        return True
    else :
        return False

def get_community(request, order_by):
    if order_by == "ascending":
        
        community = list(Community.objects.filter(members=request.user.id).order_by(Lower('name')))
        
        return community
    elif order_by == "descending":
        community = list(Community.objects.filter(members=request.user.id).order_by(Lower('name').desc()))
        
        return community
    else:
        return []

@csrf_exempt
def sort_ajax(request):
    order_by = ""
    if request.method == 'POST':
        order_by_value = request.POST.get('order_by')
        if order_by_value == '1':
            order_by = "ascending"
        elif order_by_value == '2':
            order_by = "descending"
        else:
            order_by = request.GET.get('order_by', 'ascending')
    else:
        order_by = request.GET.get('order_by', 'ascending')

    sorted_community = get_community(request,order_by)
    if sorted_community:
        return HttpResponse(serializers.serialize('json', sorted_community), content_type="application/json")
    else:
        return HttpResponseNotFound('Community not found')
