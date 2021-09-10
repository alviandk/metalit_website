from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, PelatihantForm
from .models import QA, PrivacyPolicy, TermConditions

def home(request):
	return render(request, 'revamp/home.html')

def about(request):
	return render(request, 'revamp/about.html')

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'pesan berhasil terkirim')
			return render(request, 'revamp/contact.html')
		else:
			messages.error(request, 'pesan tidak berhasil terkirim')
	form = ContactForm()
	context = {'form': form}
	return render(request, 'revamp/contact.html', context)

def course(request):
	if request.method == 'POST':
		form = PelatihantForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'pesan berhasil terkirim')
			return render(request, 'revamp/course.html')
		else:
			messages.error(request, 'pesan tidak berhasil terkirim')
	form = PelatihantForm()
	context = {'form': form}
	return render(request, 'revamp/course.html', context)

def term_conditions(request):
	termconditions = TermConditions.objects.all()
	context = {"termconditions": termconditions}
	return render(request, 'revamp/term-conditions.html', context)

def privacy_policy(request):
	privacypolicy = PrivacyPolicy.objects.all()
	context = {"privacypolicy": privacypolicy}
	return render(request, 'revamp/privacy-policy.html', context)

def help(request):
	qa = QA.objects.all()
	context = {"qna": qa}
	return render(request, 'revamp/help.html', context)