from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Event(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField(default='Roaming Home')
	venue = models.CharField(max_length=100)
	beds = models.IntegerField()
	date = models.DateTimeField()
	duration = models.CharField(
        max_length=20,
        help_text='e.g. 3 hours, 5 days'
    )

	def __str__(self):
		return "%s" % self.title