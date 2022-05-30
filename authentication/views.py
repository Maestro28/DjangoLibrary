from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm, ProfileForm

# Create your views here.


def base_home(request):
    return render(request, "authentication/base_home.html")


def register(request):
    if request.method == "GET":
        return render(
            request, "authentication/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST" or None:
        form = CustomUserCreationForm(request.POST or None)
        if form.is_valid():
            # user = form.save()
            # login(request, user)
            password = form.cleaned_data['password2']
            user = form.save()
            new_user = auth.authenticate(username=user.email, password=password)
            # auth.login(request, new_user, backend='django.contrib.auth.backends.ModelBackend')
            auth.login(request, new_user)
            return redirect('authentication:base_home')
        else:
            return render(request, "authentication/register.html", {"form": form})


@login_required
def profile(request):
    if request.method == "GET":
        user = request.user
        form = ProfileForm(instance=user)
        return render(request, "authentication/profile.html", {'form':form})
    else:
        user = request.user
        form = ProfileForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('authentication:base_home')
