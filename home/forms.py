from re import M
from django import forms
from django.contrib.auth.models import User
from .models import Message


class contact_me(forms.ModelForm):
    full_name = forms.CharField()
    email_address = forms.EmailField()
    message = forms.CharField()

    class Meta:
        model = Message
        fields = ['full_name', 'email_address', 'message']