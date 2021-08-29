from django.shortcuts import render, redirect
from .forms import ContactForm, PelatihantForm
from django.contrib import messages


# Create your views here.
def home(request):
	return render(request, 'revamp/home.html')

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

def course(request):
	if request.method == 'POST':
		form = PelatihantForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Message sent successfully')
			return render(request, 'revamp/course.html')
		else:
			messages.error(request, 'message not sent successfully')
	form = PelatihantForm()
	context = {'form': form}
	return render(request, 'revamp/course.html', context)

def term_conditions(request):
	return render(request, 'revamp/term_conditions.html')

def privacy_policy(request):
	return render(request, 'revamp/privacy_policy.html')

def help(request):
	return render(request, 'revamp/help.html')