from django.contrib.auth.base_user import AbstractBaseUser
from django.conf import settings
from django.db import models

class CustomUser(AbstractBaseUser):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.CharField(max_length=40, unique=True)
    cell = models.CharField(max_length=12)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    is_active = False

    def get_full_name(self):
        return "%s %s" %(name, surname)

    def get_short_name(self):
        return name