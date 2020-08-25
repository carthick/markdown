from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render

from .forms import LoginForm

def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('successfully Logged In')
                else:
                    return HttpResponse('Account Disabled')
            else:
                return HttpResponse('Login not valid')
    else:
        form = LoginForm()
    return render(request, 'user_profile/login.html', {'form': form})

def signout(request):
    logout(request)
    return render(request, "user_profile/signout.html")