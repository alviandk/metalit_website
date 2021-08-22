from django.shortcuts import render, redirect

# Create your views here.
def home(request):
	return render(request, 'revamp/index.html')
def about(request):
	return render(request, 'revamp/about.html')
def contact(request):
	return render(request, 'revamp/contact.html')
def pelatihan(request):
	return render(request, 'revamp/pelatihan.html')
def syaratketentuan(request):
	return render(request, 'revamp/syarat-ketentuan.html')
def kebijakanprivasi(request):
	return render(request, 'revamp/kebijakan-privasi.html')