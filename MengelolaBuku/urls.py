from django.urls import path
from MengelolaBuku.views import show_book, add_book, get_books_json

app_name = 'MengelolaBuku'

urlpatterns = [
    path('', show_book, name='show_book'),
    path('get-books-json', get_books_json, name='get_books_json'),
    path('add-book', add_book, name='add_book')
]