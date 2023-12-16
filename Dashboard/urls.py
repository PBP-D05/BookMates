from django.urls import path
from Dashboard.views import *

app_name = 'Dashboard'

urlpatterns = [
    path('dashboard/', show_main, name='show_main'),
    path('sortajax/',sort_ajax,name='sort_ajax'),
    path('perform_search/', perform_search),
    path('update_user_name/', update_user_name)
]

