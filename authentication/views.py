# authentication/views.py
import os

from django.contrib.auth.forms import AuthenticationForm
from django.core.checks import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from django_ais import settings
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(request.POST.get('password'))
            user.save()
            login(request, user)
            return redirect('achievements')  # Перенаправление на страницу достижений
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    template_path = os.path.join(settings.BASE_DIR, 'authentication/templates/register.html')
    return render(request, template_path, {'form': form})


def custom_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('achievements')  # Перенаправление на страницу ачивок
            else:
                print(request, 'Неверное имя пользователя или пароль.')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})