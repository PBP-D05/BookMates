from django.urls import path
from .views import show_home, user_login, user_register, user_logout
app_name = 'LoginRegister'

urlpatterns = [
    path('', show_home, name='show_home'),
    path('register/', user_register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
