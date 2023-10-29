from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from MengelolaBuku.models import Buku
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
# View untuk menampilkan halaman pencarian
def search_results(request):
    return render(request, 'search_results.html')

# View untuk menanggapi permintaan pencarian
def perform_search(request):
    if request.method == 'GET':
        category = request.GET.get('category', '')  # Mendapatkan kategori dari parameter GET
        keyword = request.GET.get('keyword', '')  # Mendapatkan kata kunci pencarian dari parameter GET

        # Lakukan validasi, pastikan kategori dipilih dan keyword tidak kosong
        if category and keyword:
            # Lakukan logika pencarian berdasarkan kategori yang dipilih
            if category == 'age':
                # Lakukan pencarian berdasarkan rentang usia
                min_age, max_age = map(int, keyword.split('-'))
                results = Buku.objects.filter(min_age__lte=max_age, max_age__gte=min_age)
            elif category == 'title':
                # Lakukan pencarian berdasarkan judul
                results = Buku.objects.filter(judul__icontains=keyword)
            elif category == 'author':
                # Lakukan pencarian berdasarkan penulis
                results = Buku.objects.filter(author__icontains=keyword)
            else:
                # Kategori tidak valid
                error_message = 'Invalid category.'
                return render(request, 'search_results.html', {'error_message': error_message})
            
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
                    'image_url': book.image_url.url if book.image_url else '',  # URL gambar jika ada, kosongkan jika tidak
                    'desc': book.desc,
                })
                
            return JsonResponse({'books': books})
        else:
            # Jika kategori tidak dipilih atau keyword kosong, tampilkan pesan error
            error_message = 'Please select a category and enter a keyword.'
            return JsonResponse({'error_message': error_message})
    else:
        # Jika permintaan bukan metode GET, tampilkan pesan error
        error_message = 'Invalid request method.'
        return JsonResponse({'error_message': error_message})

def get_books_json(request):
    buku_item = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', buku_item))

def get_books_json_id(request, id):
    buku_item = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', buku_item))