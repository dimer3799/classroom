from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm, UserRegistrationForm

# Create your views here.

def test(request):
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
    return render(request, 'registration/reg.html', context)



def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        login_user = request.POST.get('login')
        password_user = request.POST.get('password')
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
            	return HttpResponse('Вы вошли')            
            else:
                return HttpResponse('Неверный логин')
    else:
        form = LoginForm()
    return render(request, 'account/index.html', {'form': form})

'''
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, user_name = cd['user_name'], password = cd['password'])
            # Проверка если пользователь 
            if user is not None:
            	return HttpResponse('Такой пользователь уже есть')
            else:
            	user = User.objects.create_user(cd['user_name'], 'test@localhost',cd['password'])
            	#user.save()
            	return HttpResponse('Пользователь зарегистрирован')
            	
            	
            	
    else:
        form = LoginForm()
    return render(request, 'account/sign_in.html', {'form': form})
    '''
def user_login(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = form.save()
            # Set the chosen password
            # new_user.set_password(form.cleaned_data['password'])
            # Save the User object
            # new_user.save()
            #profile = Profile.objects.create(user=new_user)
            return HttpResponse('Пользователь зарегистрирован')
           
           # return redirect('/account/login/')

    else:
        form = UserRegistrationForm()
    return render(request, 'account/sign_in.html', {'form': form})