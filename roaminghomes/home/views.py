from __future__ import print_function
import httplib2
from httplib2 import Http
import os

from apiclient.discovery import build
from oauth2client import file, client, tools
import datetime

from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .forms import EventForm, DocumentForm, ContactForm
from django.contrib.auth.decorators import login_required
from .models import Event, Document

from django.conf import settings
from django.core.files.storage import FileSystemStorage

from django.core.mail import send_mail, BadHeaderError

# Create your views here.
def index(request):
	return render(request, 'home/index.html')

def about(request):
	return render(request, 'home/about.html')
	
def contact(request):
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['name']
			subject = form.cleaned_data['subject']
			from_email = form.cleaned_data['from_email']
			message = form.cleaned_data['message']
			try:
				send_mail(subject, message, from_email, ['hello@roaminghomes.co.za'])
			except BadHeaderError:
				return HttpResponse('Invalid header found.')
			return HttpResponseRedirect('index')
	return render(request, 'home/contact.html', {'form': form})

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
	
def detail(request, id):
   event = Event.objects.get(id=id)
   joined = event.guests.filter(id=request.user.id)
   return render(request, 'home/events_detail.html', {'event': event, 'joined': joined})

@login_required
def volunteer(request, event_id):
	try:
		# Need to check if already joined
		event = Event.objects.get(id=event_id, guests=request.user)
	except Event.DoesNotExist as e:
		# Event exists and not yet joined so attempt to join
		try:
			event = Event.objects.get(id=event_id)
			event.guests.add(request.user)
			event.save()
		except Event.DoesNotExist as e:
			print(e)
	
	event = Event.objects.get(id=event_id)
	joined = event.guests.filter(id=request.user.id)
	return render(request, 'home/events_detail.html', {
        'event': event,
        'joined': joined
    })

@login_required
def cancel(request, event_id):
	try:
		# Need to check if already joined before cancelling
		event = Event.objects.get(id=event_id, guests=request.user)
		event.guests.remove(request.user)
		event.save()
	except Event.DoesNotExist as e:
		pass
	
	event = Event.objects.get(id=event_id)
	joined = event.guests.filter(id=request.user.id)
	return render(request, 'home/events_detail.html', {
        'event': event,
        'joined': joined
    })

try:
	import argparse
	flags = tools.argparser.parse_args([])
except ImportError:
	flags = None

SCOPES = 'https://www.googleapis.com/auth/calendar'
APPLICATION_NAME = 'Google Calendar API Python Quickstart'

def get_credentials():
	store = file.Storage('storage.json')
	credentials = store.get()
	if not credentials or credentials.invalid:
		flow = client.flow_from_clientsecrets('/home/lethalpapercut/roaminghomes/home/client_secret.json', SCOPES)
		flow.user_agent = APPLICATION_NAME
		if flags:
			credentials = tools.run_flow(flow, store, flags)
		else: # Needed only for compatibility with Python 2.6
			credentials = tools.run(flow, store)
	return credentials

@login_required
def add_event(request):
	if request.method == "POST":
		form = EventForm(request.POST)
		if form.is_valid():
			# commit=False means the form doesn't save at this time.
			# commit defaults to True which means it normally saves.
			event_instance = form.save(commit=False)
			try:
				#connect with google calendar here
				store = file.Storage('storage.json')
				creds = get_credentials()
				if not creds or creds.invalid:
					flow = client.flow_from_clientsecrets('/home/lethalpapercut/roaminghomes/home/client_secret.json', SCOPES)
					creds = tools.run_flow(flow, store, flags)
				#authorize calendar
				CAL = build('calendar', 'v3', http=creds.authorize(Http()))
				# create EVENT gcal json here
				GMT_OFF = '+02:00'
				eventDate = event_instance.date
				EVENT = {
					'summary': event_instance.title,
					'start':	{'dateTime': '%sT08:00:00%s' % (eventDate,GMT_OFF)},
					'end':		{'dateTime': '%sT22:00:00%s' % (eventDate,GMT_OFF)},
				}
				e = CAL.events().insert(calendarId='1lms34tto2koargucg7s7s3o2g@group.calendar.google.com',sendNotifications=True, body=EVENT).execute()
				event_instance.save()
			except Event.DoesNotExist as e:
				pass
				
			return HttpResponseRedirect('/events')
	else:
		form = EventForm()
	return render(request, "home/add_event.html", {'form': form})
	
def listUploads(request):
	uploads_list = Document.objects.all().order_by('-uploaded_at');
	return render(request, 'home/uploads_list.html', {'uploads_list': uploads_list})

@login_required	
def uploadFile(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			# Redirect to the document list after POST
			return HttpResponseRedirect('/uploads') #VERY IMPORTANT
	else:
		form = DocumentForm() # A empty, unbound form

    # Render list page with the documents and the form
	return render(request, 'home/uploads.html', {'form': form})