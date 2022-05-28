from django.shortcuts import render, redirect
from django.contrib import auth
from django.urls import reverse
from django.contrib.auth import login

from .forms import CustomUserCreationForm

# Create your views here.


def base_home(request):
    return render(request, "authentication/base_home.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "authentication/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # user = form.save()
            # login(request, user)
            password = form.cleaned_data['password2']
            user = form.save()
            new_user = auth.authenticate(username=user.email, password=password)
            # auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            auth.login(request, new_user)
            return redirect('authentication:base_home')
