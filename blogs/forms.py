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

    # full_name = forms.CharField(max_length=255)
    # email = forms.EmailField
    # phone_number = forms.CharField(max_length=255)
    # # region = forms.CharField(max_length=255, choices=REGION_CHOICES, default='tashkent')
    # region = forms.ChoiceField(choices=REGION_CHOICES)
    # address = forms.CharField(max_length=255)
    # date_of_birth = forms.DateField()
    # # gender = forms.CharField(max_length=255, choices=GENDER_CHOICES, default='male')
    # gender = forms.ChoiceField(choices=GENDER_CHOICES)
    # marital_status = forms.CharField(max_length=255, choices=STATUS_CHOICES)
    # # marital_status = forms.ChoiceField(choices=STATUS_CHOICES)
    # file_upload = forms.FileField()
    # message = forms.Textarea()


# def validate_phone_number(val):
#     """ +998901002030 """
#     b = str(val.replace('-', '').replace('+', '').replace(' ', ''))
#
#     print(val)
#     return True
#
#
# def validate_email(val):
#     print(val)
#     return True


class ContactForm(ModelForm):
    # phone_number = forms.CharField(validators=[validate_phone_number])

    class Meta:
        model = Contact
        fields = '__all__'
