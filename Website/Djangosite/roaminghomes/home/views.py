from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import Event

# Create your views here.
def index(request):
	return render(request, 'home/index.html')

def about(request):
	return render(request, 'home/about.html')
	
def contact(request):
	return render(request, 'home/contact.html')

def calendar(request):
	return render(request, 'home/calendar.html')
	
def register(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			new_user = form.save()
			return HttpResponseRedirect("/")
	else:
		form = UserCreationForm()
	return render(request, "users/register.html", {'form': form,})
	
def list(request):
	event_list = Event.objects.all().order_by('date');
	return render(request, 'home/events_list.html', {'event_list': event_list})