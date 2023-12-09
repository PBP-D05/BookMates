from django.urls import path
from MengelolaBuku.views import show_book, add_book, get_books_json, get_books_json_id, remove_book
from MengelolaBuku.views import add_book_flutter, remove_book_flutter, show_book_flutter, get_pengguna_json

app_name = 'MengelolaBuku'

urlpatterns = [
    path('', show_book, name='show_book'),
    path('get-books-json', get_books_json, name='get_books_json'),
    path('get-pengguna-json', get_pengguna_json, name='get_pengguna_json'),
    path('add-book', add_book, name='add_book'),
    path('get-books-json-id/<int:id>/', get_books_json_id, name='get_books_json_id'),
    path('remove_book/<int:id>/', remove_book, name='remove_book'),
    path('add-book-flutter', add_book_flutter, name='add_book-flutter'),
    path('show-book-flutter', show_book_flutter, name='show_book-flutter'),
    path('remove-book-flutter/', remove_book_flutter, name='remove_book_flutter')
]