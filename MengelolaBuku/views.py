from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse
from .models import Buku, Pengguna
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def show_book(request):
    if Pengguna.objects.get(user=request.user).isGuru == False:
        return redirect('Dashboard:show_main')

    books = Buku.objects.filter(user=Pengguna.objects.get(user=request.user))
    context = {
        books: books,
    }
    return render(request, 'show_book.html', context)

@csrf_exempt
def add_book(request):
    if Pengguna.objects.get(user=request.user).isGuru == False:
        return redirect('Dashboard:show_main')
    
    if request.method == 'POST':
        judul = request.POST.get("judul")
        author = request.POST.get("author")
        rating = request.POST.get("rating")
        num_of_rating = request.POST.get("num_of_rating")
        min_age = request.POST.get("min_age")
        max_age = request.POST.get("max_age")
        image_url = request.POST.get("url_image")
        description = request.POST.get("description")
        user = Pengguna.objects.get(user=request.user)

        new_product = Buku(judul=judul, author=author, rating=rating, 
                           num_of_rating=num_of_rating, min_age=min_age,
                           max_age=max_age, image_url=image_url, desc=description, user=user)
        new_product.save()
        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

def get_books_json(request):
    buku_item = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', buku_item))

def get_books_json_id(request, id):
    buku_item = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', buku_item))

def remove_book(request, id):
    if Pengguna.objects.get(user=request.user).isGuru == False:
        return redirect('Dashboard:show_main')
    
    book = Buku.objects.get(pk=id)
    if (book.user == Pengguna.objects.get(user=request.user)):
        book.delete()
    return redirect('MengelolaBuku:show_book')

@csrf_exempt
def add_book_flutter(request):
    if request.method == 'POST':
        if Pengguna.objects.get(user=request.user).isGuru == False:
            return JsonResponse({"status": "forbidden"}, status=403)
        
        data = json.loads(request.body)

        new_product = Buku.objects.create(
            judul = data["judul"],
            author = data["author"],
            rating = 0,
            num_of_rating = 0,
            min_age = data["min_age"],
            max_age = data["max_age"],
            image_url = data["image_url"],
            description = data["description"],
            user = Pengguna.objects.get(user=request.user)
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

def remove_book_flutter(request):
    if Pengguna.objects.get(user=request.user).isGuru == False:
        return JsonResponse({"status": "error"}, status=403)
    
    data = json.loads(request.body)
    book = Buku.objects.get(pk=data["pk"])
    if (book.user == Pengguna.objects.get(user=request.user)):
        book.delete()
    return JsonResponse({"status": "success"}, status=200)

def show_book_flutter(request):
    if Pengguna.objects.get(user=request.user).isGuru == False:
        return JsonResponse({"status": "error"}, status=403)

    books = Buku.objects.filter(user=Pengguna.objects.get(user=request.user))
    return HttpResponse(serializers.serialize('json', books))