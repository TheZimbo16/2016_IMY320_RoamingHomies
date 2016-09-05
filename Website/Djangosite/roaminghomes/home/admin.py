from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import Group

# Register your models here.
from .models import Event
from .models import CustomUser
from .forms import UserCreationForm

