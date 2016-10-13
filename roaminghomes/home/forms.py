from django import forms

from home.models import Event, Document

class EventForm(forms.ModelForm):
	class Meta:
		model = Event
		exclude = ('guests','duration')

class DocumentForm(forms.ModelForm):
	class Meta:
		model = Document
		exclude = ('description',)

class ContactForm(forms.Form):
	name = forms.CharField(required=True)
	from_email = forms.EmailField(required=True)
	subject = forms.CharField(required=True)
	message = forms.CharField(widget=forms.Textarea)

ROLE_CHOICES = (
    ('role1'),
    ('role2'),
)