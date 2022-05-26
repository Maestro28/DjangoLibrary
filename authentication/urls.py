from django.urls import path, include

from . import views

app_name = 'authentication'
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path("accounts/", include("django.contrib.auth.urls"), name='accounts'),
]