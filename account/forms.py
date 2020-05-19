from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    user_name = forms.CharField(label ='Логин', max_length=50, widget=forms.TextInput(attrs={'id': 'login', 'class':'input_signin'}))
    password = forms.CharField(label ='Пароль', widget = forms.TextInput(attrs={'id': 'password', 'class':'input_signin','type':'password'}))



class UserRegistrationForm(UserCreationForm):
	#user_name = forms.CharField(label ='Логин', max_length=50, widget=forms.TextInput(attrs={'id': 'login', 'class':'input_signin'}))
	email = forms.EmailField(max_length=254, help_text='Это поле обязательно', label = 'Электронный адрес')
	#first_name = forms.CharField(label ='Имя', max_length=50, widget=forms.TextInput(attrs={'id': 'first_name', 'class':'input_signin'}))
	#last_name = forms.CharField(label ='Фамилия', max_length=50, widget=forms.TextInput(attrs={'id': 'last_name', 'class':'input_signin'}))
	#password = forms.CharField(label ='Пароль', widget = forms.TextInput(attrs={'id': 'password', 'class':'input_signin','type':'password'}))
	#password2 = forms.CharField(label ='Повторите пароль', widget = forms.TextInput(attrs={'id': 'password2', 'class':'input_signin','type':'password'}))

	field_order = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

	def __init__(self, *args, **kwargs):
		super(UserRegistrationForm, self).__init__(*args, **kwargs)
		self.fields['email'].help_text = 'Введите e-mail'
		self.fields['username'].help_text = "Может содержать только буквы, цифры и символы @ . + - _"
		self.fields['password1'].help_text = """
        Пароль не может быть похож на имя пользователя.
        Пароль должен содержать как минимум 8 символов.
        Пароль не должен быть простым и часто используемым.
        
        Пароль не должен содержать только цифры.
        """
		self.fields['password2'].help_text = 'Для подтверждения введите, пожалуйста, пароль ещё раз.'
		self.fields['username'].widget.attrs['maxlength'] = 20
