from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

def base(request):
    return render(request, 'base.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('base')

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
