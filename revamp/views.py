from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm, PelatihantForm
from .models import QA, PrivacyPolicy, TermCondition

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

def term_conditions(request):
	context = {}
	try:
		context['content'] = TermCondition.objects.last().Description
	except:
		context['content'] = ""
	return render(request, 'revamp/term-conditions.html', context)

def privacy_policy(request):
	context = {}
	try:
		context['content'] = PrivacyPolicy.objects.last().description
	except:
		context['content'] = ""
	return render(request, 'revamp/privacy-policy.html', context)

def help(request):
	qa = QA.objects.all()
	context = {"qna": qa}
	return render(request, 'revamp/help.html', context)

"""def course(request):
	# if request.method == 'POST':
	# 	form = PelatihantForm(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		messages.success(request, 'Pengisian formulir berhasil disimpan')
	# 		return render(request, 'revamp/course.html')
	# 	else:
	# 		messages.error(request, 'pesan tidak berhasil terkirim')
	# form = PelatihantForm()
	# context = {'form': form}
	# return render(request, 'revamp/course.html', context)
	#return render(request, 'revamp/coming_soon.html')
	return render(request, 'eduport/course.html')"""

def dashboard(request):
	return render(request, 'eduport/dashboard.html')
	#return render(request, 'revamp/coming_soon.html')

def video_player(request):
	return render(request, 'eduport/video-player.html')

def error(request):
	return render(request, 'eduport/error-404.html')

def slider(request):
	return render(request, 'eduport/slider.html')

def edit_profile(request):
	return render(request, 'eduport/edit-profile.html')