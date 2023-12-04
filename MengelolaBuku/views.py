from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound
from .models import Buku, Pengguna
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

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