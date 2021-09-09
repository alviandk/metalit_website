from django.conf import settings

def blog_url(request):
	return {'react_blog_url':settings.BLOG_URL}
