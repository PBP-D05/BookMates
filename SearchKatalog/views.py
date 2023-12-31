from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from MengelolaBuku.models import Buku
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from django.db.models import Q
# Create your views here.

@csrf_exempt
# View untuk menampilkan halaman pencarian
def search_results(request):
    return render(request, 'search_results.html')

@csrf_exempt
# View untuk menanggapi permintaan pencarian
def perform_search(request):
    if request.method == 'POST':
        category = request.POST.get('category', '')
        keyword = request.POST.get('keyword', '')
        print(category)
        print(keyword)

        # Print debug information
        print(f"Received request with category: {category}, keyword: {keyword}")

        # Lakukan validasi, pastikan kategori dipilih dan keyword tidak kosong
        if category and keyword:
            # Lakukan logika pencarian berdasarkan kategori yang dipilih
            if category == 'age':
                if '-' in keyword:
                    # Lakukan pencarian berdasarkan rentang usia
                    min_age, max_age = map(int, keyword.split('-'))
                    results = Buku.objects.filter(Q(min_age__gte=min_age) & Q(max_age__lte=max_age))
                else:
                    # Lakukan pencarian dengan rentang max < keyword
                    min_age, max_age = 0, int(keyword)
                    results = Buku.objects.filter(Q(max_age__lte=max_age))

                # print("KEY:", min_age, ' ', max_age)
                # for res in results:
                #     print(res.min_age, res.max_age, res.judul)
            elif category == 'title':
                # Lakukan pencarian berdasarkan judul
                results = Buku.objects.filter(judul__icontains=keyword)
            elif category == 'author':
                # Lakukan pencarian berdasarkan penulis
                results = Buku.objects.filter(author__icontains=keyword)
            else:
                # Kategori tidak valid
                error_message = 'Invalid category.'
                return JsonResponse({'error_message': error_message})

            return HttpResponse(serializers.serialize('json', results), content_type="application/json")

        else:
            # Jika kategori tidak dipilih atau keyword kosong, tampilkan pesan error
            error_message = 'Please select a category and enter a keyword.'
            return JsonResponse({'error_message': error_message})

    else:
        # Metode request tidak diizinkan (bukan GET atau POST)
        error_message = 'Invalid request method.'
        return JsonResponse({'error_message': error_message})

def get_books_json(request):
    buku_item = Buku.objects.all()
    return HttpResponse(serializers.serialize('json', buku_item))

def get_books_json_id(request, id):
    buku_item = Buku.objects.filter(pk=id)
    return HttpResponse(serializers.serialize('json', buku_item))