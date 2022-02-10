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
from django.urls import path, include
from revamp import views
from blog_backend import views as v
#from .views import Home, Metalit
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView

urlpatterns = [
    #path("", Home.as_view(), name="home"),
    #path("metalit/", Metalit.as_view(), name="metalit"),
    path('admin/', admin.site.urls),
    path("", views.home, name="home"),
    path("coba", views.coba, name="coba"),
    path("video-player", views.video_player, name="video_player"),
    path("empty-cart", views.empty_cart, name="empty_cart"),
    path("edit-profile", views.edit_profile, name="edit_profile"),
    path("error", views.error, name="error"),
    path("dashboard", views.dashboard, name="dashboard"),
    path("about", views.about, name="about"),
    path("cart", views.cart, name="cart"),
    path("blog-masonry", v.blog_masonry, name="blog"),
    path("contact", views.contact, name="contact"),
    path("course", views.course, name="course"),
    path("term-conditions", views.term_conditions, name="term-conditions"),
    path("privacy-policy", views.privacy_policy, name="privacy-policy"),
    path("help", views.help, name="help"),
    path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('api/', include('upload_cv.urls')),
    path("accounts/", include("allauth.urls")),
    path('api/', include('course.urls')),
    
]
