"""myproject URL Configuration

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
from django.urls import path
from revamp import views
from .views import Home, Metalit

urlpatterns = [
    #path("", Home.as_view(), name="home"),
    #path("metalit/", Metalit.as_view(), name="metalit"),
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("pelatihan", views.pelatihan, name="pelatihan"),
    path("syarat-ketentuan", views.syarat_ketentuan, name="syarat_ketentuan"),
    path("kebijakan-privasi", views.kebijakan_privasi, name="kebijakan_privasi"),
    path("coba", views.contact_view, name="contact_view"),
    path("help", views.help, name="help"),
]
