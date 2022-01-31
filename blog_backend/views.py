from django.shortcuts import render
from .models import Article

# Create your views here.
def blog_masonry(request):
	articles = Article.objects.all()
	return render(request,"blog.html",{"articles":articles})
	#return render(request, 'blog.html')