from django.shortcuts import render, redirect
from .forms import ContactForm, PelatihantForm
from django.contrib import messages


# Create your views here.
def Home(request):
	return render(request, 'revamp/index.html')

def About(request):
	return render(request, 'revamp/about.html')

def Contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Message sent successfully')
			return render(request, 'revamp/contact.html')
		else:
			messages.error(request, 'message not sent successfully')
	form = ContactForm()
	context = {'form': form}
	return render(request, 'revamp/contact.html', context)

def Pelatihan(request):
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

def Syarat_Ketentuan(request):
	return render(request, 'revamp/syarat_ketentuan.html')

def Kebijakan_Privasi(request):
	return render(request, 'revamp/kebijakan_privasi.html')

def Contact_View(request):
	return render(request, 'revamp/coba.html', context)