from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(max_length=140,default='Roaming Home')
	venue = models.CharField(max_length=100)
	beds = models.IntegerField()
	date = models.DateField(blank=True, null=True)
	duration = models.CharField(
        max_length=20,
        help_text='e.g. 3 hours, 5 days'
    )
	
	guests = models.ManyToManyField(User, blank=True)

	def __str__(self):
		return "%s" % self.title
		
class Document(models.Model):
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')
	description = models.CharField(max_length=255, blank=True)
	uploaded_at = models.DateTimeField(auto_now_add=True)