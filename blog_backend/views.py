from django.shortcuts import render
from .models import Article

def blog_masonry(request):
	articles = Article.objects.all()

	return render(request, 'eduport/blog.html', {"articles":articles})