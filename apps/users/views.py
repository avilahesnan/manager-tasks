from django.shortcuts import render, redirect
from apps.users.forms import LoginForm, RegisterForm
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


def login(request):
    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in!')
        return redirect('tasks:index')
    
    form = LoginForm
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            name = form['name_login'].value()
            password = form['password'].value()

        user = auth.authenticate(
            request,
            username=name,
            password=password
        )
        if user is not None:
            auth.login(request, user)
            messages.success(request, f'{name} logged in successfully!')
            return redirect('tasks:index') 
        else:
            messages.error(request, 'Error! Unable to log in!')
            return redirect('users:login')

    return render(request, 'users/login.html', {'form': form})


def logout(request):
    auth.logout(request)
    messages.success(request, 'Logout done successfully!')
    return redirect('users:login')


def register(request):
    if request.user.is_authenticated:
        messages.error(request, 'You are already logged in!')
        return redirect('tasks:index')
    
    form = RegisterForm
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            name = form['name_register'].value()
            email = form['email'].value()
            password = form['password_1'].value()
            
            if User.objects.filter(username=name).exists():
                messages.error(request, 'Error! User already has registration!')
                return redirect('users:register')
            
            user = User.objects.create_user(
                username=name,
                email=email,
                password=password
            )
            user.save()
            messages.success(request, f'{name} you have been successfully registered!')
            return redirect('users:login')

    return render(request, 'users/register.html', {'form': form})
