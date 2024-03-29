"""
URL configuration for hotroddiner project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from about.views import about
from booking.views import booking
from login.views import login
from menu.views import menu
from register.views import register
from index import views as index_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('booking/', booking, name='booking'),
    path('register/', register, name='register'),
    path('menu/', menu, name='menu'),
    path('', index_views.index, name='index'),
]
