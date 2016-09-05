from __future__ import unicode_literals
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
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

class CustomUser(AbstractBaseUser):
    firstname = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    email = models.EmailField(max_length=40, unique=True)
    cell = models.CharField(max_length=12)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname']

    is_admin = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)

    #objects = CustomUserManager()

    def get_full_name(self):
        return "%s %s" %(self.firstname, self.surname)

    def get_short_name(self):
        return self.firstname

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def is_staff(self):
        return self.is_admin

class CustomUserManager(BaseUserManager):
    def create_user(self, firstname, surname, email, cell, password):
        if not email:
            raise ValueError('Please provide a valid email address')
        email = self.normalize_email(email)
        user = self.model(firstname=firstname, surname=surname, email=email, cell=cell, is_active = True, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.is_admin = False
        user.save(using=self._db)
        return user

    def create_superuser(self, firstname, surname, email, cell, password):
        if not email:
            raise ValueError('Please provide a valid email address')
        email = self.normalize_email(email)
        user = self.model(firstname=firstname, surname=surname, email=email, cell=cell, is_active = True, is_staff=is_staff, is_superuser=is_superuser)
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user