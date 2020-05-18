from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    user_name = forms.CharField(label ='Логин', max_length=50, widget=forms.TextInput(attrs={'id': 'login', 'class':'input_signin'}))
    password = forms.CharField(label ='Пароль', widget = forms.TextInput(attrs={'id': 'password', 'class':'input_signin','type':'password'}))


class UserRegistrationForm(forms.Form):
	user_name = forms.CharField(label ='Логин', max_length=50, widget=forms.TextInput(attrs={'id': 'login', 'class':'input_signin'}))
	password = forms.CharField(label ='Пароль', widget = forms.TextInput(attrs={'id': 'password', 'class':'input_signin','type':'password'}))
	password2 = forms.CharField(label ='Повторите пароль', widget = forms.TextInput(attrs={'id': 'password2', 'class':'input_signin','type':'password'}))


	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError('Passwords don\'t match.')
		return cd['password2']