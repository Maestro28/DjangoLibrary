from django.urls import path, include

from . import views

app_name = 'authentication'
urlpatterns = [
    path('', views.base_home, name='base_home'),
    path("register/", views.register, name="register"),
    path("accounts/", include("django.contrib.auth.urls"), name='accounts'),
]