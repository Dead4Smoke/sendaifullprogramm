from django.contrib.messages.api import error
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import Loginsform, CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def signin(request):
    error = ''
    if request.method == 'POST':
        form = Loginsform(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    messages.success(request, 'Добро пожаловать!')
                    # return render(request, 'base/start.html')
                    return redirect('start')
                else:
                     messages.error(request,'Проверьте данные для входа!')
            else:
                 messages.error(request,'Неверный логин или пароль!')
    else:       
        form = Loginsform()
        # form = Loginsform({'username': 'dron','password': 'e103xxmpv'})
        data = {
        'form' : form,
        'error': error,
        }
    return render(request, 'reg/signin.html', {'form': form})

def register(request):
    error = ''
    data = {}
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            new_form = form.save()
            new_form.set_password(form.cleaned_data['password1'])
            new_form.save()
            messages.success(request, 'Ваш аккаунт зарегистрирован!')
            return redirect('signin')
        else:
            messages.error(request,' Проверьте правильность заполненных данных!')
            return redirect( 'register' )
    else: # Иначе
        form = CustomUserCreationForm()
        data['form'] = form
    return render(request, 'reg/register.html', data)

def logout_view(request):
    logout(request)
    return render(request, 'reg/logout.html')
