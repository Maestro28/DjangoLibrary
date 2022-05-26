from django.shortcuts import render

# Create your views here.


def base_home(request):
    return render(request, "authentication/base_home.html")
