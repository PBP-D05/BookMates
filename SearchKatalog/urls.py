from django.urls import path
from SearchKatalog.views import search_results, get_books_json, get_books_json_id

app_name = 'SearchKatalog'

urlpatterns = [
    path('', search_results, name='search_results'),
    path('get-books-json', get_books_json, name='get_books_json'),
    path('get-books-json-id/<int:id>/', get_books_json_id, name='get_books_json_id'),
]