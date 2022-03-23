import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):

    email = forms.EmailField(label="", widget=forms.EmailInput
                             (attrs={'placeholder': 'Enter your email :'}))

    username = forms.CharField(label="", widget=forms.TextInput
                               (attrs={'placeholder': 'Enter your Username :'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter your Password :'}))
    password2 = forms.CharField(
        label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your Password :'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
