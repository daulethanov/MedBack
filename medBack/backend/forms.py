from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Blog


class RegisterUserForm(UserCreationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    numbers = forms.IntegerField(label='Номер телефона', widget=forms.TextInput(attrs={'class': 'form-input'}))


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput())
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())

#
# class FormSubmit(forms.Form):
#     # question = forms.CharField(label='Text', widget=forms.Textarea(attrs={'class': 'form-input'}))
#
#     class Meta:
#         model = Blog
#         fields = ['question', ]

