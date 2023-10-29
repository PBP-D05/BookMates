from django.urls import path
from Komunitas.views import community_main, addInCommunity, community_detail, join_community

app_name = 'Komunitas'

urlpatterns = [
    path('', community_main, name='community_main'),
    path('add-community', addInCommunity, name='get_books_json'),
    path('community_detail', community_detail, name='add_book'),
    path('join-community/<int:join_code>/', join_community, name='join_community'),
]