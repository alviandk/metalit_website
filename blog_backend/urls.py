from django.urls import path
from . import views

urlpatterns = [
	path("blog-masonry", views.blog_masonry, name="blog"),
]