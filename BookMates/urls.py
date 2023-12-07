"""BookMates URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD

=======
from LoginRegister import views
>>>>>>> bc870955ba334c4cbb605f2dbec8ae1b48ff941c
urlpatterns = [
    path('', include('LoginRegister.urls')),
    path('', views.show_home, name='home'),
    path('admin/', admin.site.urls),
    path('editbuku/', include('MengelolaBuku.urls')),
<<<<<<< HEAD
=======
    path('searchbuku/', include('SearchKatalog.urls')),
    path('challenge/', include('ChallengeLeaderboard.urls')),
    path('',include('Dashboard.urls')),
    path('',include('Komunitas.urls')),
>>>>>>> bc870955ba334c4cbb605f2dbec8ae1b48ff941c
]
