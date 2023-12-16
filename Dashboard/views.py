from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Community, Pengguna
from django.db.models.functions import Lower
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import JsonResponse
from MengelolaBuku.models import Buku
from django.contrib.auth.models import User


from django.db.models import Q

# Create your views here.

#@login_required(login_url='/login')
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

def get_books_json(request):
    buku_item = Buku.objects.all()
    return HttpResponse(serializers.serialize("json", buku_item), content_type="application/json")

def perform_search(request):
    
    results = Buku.objects.all()
    
    # Ubah hasil pencarian ke dalam format yang sesuai untuk ditampilkan di halaman
    books = []
    for book in results:
        books.append({
            'judul': book.judul,
            'author': book.author,
            'rating': book.rating,
            'num_of_rating': book.num_of_rating,
            'min_age': book.min_age,
            'max_age': book.max_age,
            'image_url': book.image_url if book.image_url else '',  # URL gambar jika ada, kosongkan jika tidak
            'desc': book.desc,
        })
        
    return JsonResponse({'books': books})
    

@csrf_exempt
def update_user_name (request):
    if request.method == 'POST':
        usernameBaru = request.POST.get('name')
        id = request.POST.get('id') 
        user = User.objects.get(pk=id)
        
        user.username = usernameBaru
        user.save()
        return JsonResponse({"status": True, "message": "Username berhasil diubah!","username":user.username}, status=201)
    
    return JsonResponse({"status": False, "message": "Username gagal diubah!"}, status=400)