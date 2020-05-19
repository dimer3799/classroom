from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    user_name = forms.CharField(label ='Логин', max_length=50, widget=forms.TextInput(attrs={'id': 'login', 'class':'input_signin'}))
    password = forms.CharField(label ='Пароль', widget = forms.TextInput(attrs={'id': 'password', 'class':'input_signin','type':'password'}))



class UserRegistrationForm(UserCreationForm):
	user_name = forms.CharField(label ='Логин', max_length=50, widget=forms.TextInput(attrs={'id': 'login', 'class':'input_signin'}))
	first_name = forms.CharField(label ='Имя', max_length=50, widget=forms.TextInput(attrs={'id': 'first_name', 'class':'input_signin'}))
	last_name = forms.CharField(label ='Фамилия', max_length=50, widget=forms.TextInput(attrs={'id': 'last_name', 'class':'input_signin'}))
	password = forms.CharField(label ='Пароль', widget = forms.TextInput(attrs={'id': 'password', 'class':'input_signin','type':'password'}))
	password2 = forms.CharField(label ='Повторите пароль', widget = forms.TextInput(attrs={'id': 'password2', 'class':'input_signin','type':'password'}))

	field_order = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
