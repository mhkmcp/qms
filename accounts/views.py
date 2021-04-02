from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def signup_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, 'User Signup Success')
            return redirect('quiz:home')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            # next = request.POST.get('next')
            # print('NEXT: ', next)
            messages.success(request, 'User Signup Success')
            return redirect('quiz:home')
        else:
            messages.error(request, 'Username or Password is Incorrect')

    return render(request, 'accounts/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('accounts:signup')


