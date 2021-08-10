from django import forms
from django.forms import ModelForm
from django.utils import timezone

from . import models
from .models import Contact, VirtualReception

GENDER_CHOICES = (
    ('male', 'Male'),
    ('female', 'Female'),
)

STATUS_CHOICES = (
    ('single', 'Single'),
    ('married', 'Married'),
)

REGION_CHOICES = (
    ('andijan', ("Andijan")),
    ('bukhara', ("Bukhara")),
    ('fergana', ("Fergana")),
    ('jizzakh', ("Jizzakh")),
    ('khorezm', ("Khorezm")),
    ('namangan', ("Namangan")),
    ('navoiy', ("Navoiy")),
    ('kashkadarya', ("Kashkadarya")),
    ('samarkand', ("Samarkand")),
    ('sirdarya', ("Sirdarya")),
    ('surkhandarya', ("Surkhandarya")),
    ('tashkent', ("Tashkent")),
    ('tashkent_city', ("Tashkent city")),
    ('karakalpakstan', ("Karakalpakstan")),
)


class VirtualReceptionForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
