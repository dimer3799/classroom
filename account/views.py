from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm

# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
            	return HttpResponse('Пользователь зарегистрирован')            
            else:
                return HttpResponse('Пользователь зарегистрирован')
    else:
        form = UserRegistrationForm()
        
    context = {'form':form}
    return render(request,'account/reg.html', context)



def index(request):
    if request.method == 'POST':
        form_login = LoginForm(request.POST)
        if form_login.is_valid():
           # user = form_login.save(commit=False)
            #form.save()
            print(form_login.cleaned_data)
            username = form_login.cleaned_data['user_name']
            password = form_login.cleaned_data['password']
            #user.save()
            user = authenticate(username=username, password=password)
            if user is not None:
            	return HttpResponse('Пользователь зашел в систему')            
            else:
                return HttpResponse('Ошибка: нет такого пользователя')
    else:
        form = LoginForm()
        
    context = {'form':form}
    return render(request, 'account/index.html', context)