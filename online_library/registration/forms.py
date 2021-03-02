from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
from django.db import models
from django import forms

class UserCreate(UserCreationForm):
            class Meta:
                model = User
                fields=['username', 'password1', 'password2', 'email']
                help_texts = {'username': None, 'password1': (""), 'password2': ("")}

class Profile(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = '__all__'
        exclude = ('user', 'books',)