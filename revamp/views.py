from django.shortcuts import render, redirect
from .forms import ContactForm, PelatihantForm
from django.contrib import messages


# Create your views here.
def beranda(request):
	return render(request, 'revamp/index.html')

def tentang_kami(request):
	return render(request, 'revamp/tentang_kami.html')

def hubungi_kami(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Message sent successfully')
			return render(request, 'revamp/hubungi_kami.html')
		else:
			messages.error(request, 'message not sent successfully')
	form = ContactForm()
	context = {'form': form}
	return render(request, 'revamp/hubungi_kami.html', context)

def pelatihan(request):
	if request.method == 'POST':
		form = PelatihantForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Message sent successfully')
			return render(request, 'revamp/pelatihan.html')
		else:
			messages.error(request, 'message not sent successfully')
	form = PelatihantForm()
	context = {'form': form}
	return render(request, 'revamp/pelatihan.html', context)

def syarat_ketentuan(request):
	return render(request, 'revamp/syarat_ketentuan.html')

def kebijakan_privasi(request):
	return render(request, 'revamp/kebijakan_privasi.html')

def pusat_bantuan(request):
	return render(request, 'revamp/pusat_bantuan.html')