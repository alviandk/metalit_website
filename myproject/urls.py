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
from revamp import views as v
from .views import Home, Metalit

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("metalit/", Metalit.as_view(), name="metalit"),
    path('admin/', admin.site.urls),
    path("revamp/", v.Home, name="home"),
    path("revamp/about", v.About, name="about"),
    path("revamp/contact", v.Contact, name="contact"),
    path("revamp/pelatihan", v.Pelatihan, name="pelatihan"),
    path("revamp/syarat-ketentuan", v.Syarat_Ketentuan, name="syarat_ketentuan"),
    path("revamp/kebijakan-privasi", v.Kebijakan_Privasi, name="kebijakan_privasi"),
    path("revamp/coba", v.Contact_View, name="contact_view"),
]
