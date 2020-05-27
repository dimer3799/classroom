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
           # Исправить
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
            print(form_login.cleaned_data)
            username = form_login.cleaned_data['user_name']
            password = form_login.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print (user ,'зашел в систему')     
                return HttpResponse(str(user) +' зашел в систему')
               # return render(request, 'account/index.html', context) передать логин на другую страницу
            else:
                return HttpResponse('Неправильный логин или пароль')
    else:
        form = LoginForm()
        
    context = {'form':form}
    return render(request, 'account/index.html', context)