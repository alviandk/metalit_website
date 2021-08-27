from django.shortcuts import render, redirect
from .forms import ContactForm, PelatihantForm
from django.contrib import messages


# Create your views here.
def home(request):
	return render(request, 'revamp/index.html')

def about(request):
	return render(request, 'revamp/about.html')

def contact(request):
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

def contact_view(request):
	return render(request, 'revamp/coba.html')

def help(request):
	return render(request, 'revamp/help.html')