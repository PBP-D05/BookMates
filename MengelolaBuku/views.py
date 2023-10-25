from django.shortcuts import render
from .models import Buku

# Create your views here.
def show_book(request):
    books = Buku.objects.filter(user=request.user)
    context ={
        books: books,
    }
    return render('show_book.html', context)