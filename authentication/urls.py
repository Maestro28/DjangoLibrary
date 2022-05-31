from django.urls import path, include
from django.urls import reverse_lazy

from . import views
from django.contrib.auth.views import PasswordChangeDoneView, PasswordChangeView,\
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView
# from django.contrib.auth.urls

app_name = 'authentication'
urlpatterns = [
    path('', views.base_home, name='base_home'),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("accounts/", include("django.contrib.auth.urls"), name='accounts'),

    path('password-change/', PasswordChangeView.as_view(template_name='registration/password_change_form.html',
                                                        success_url=reverse_lazy('authentication:password_change_done')),
         name='password_change'),

    path('password_change_done/', PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),
         name='password_change_done'),

    # PASSWORD RESET URLS
    path('password_reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html',
                                                      success_url=reverse_lazy('authentication:password_reset_done')),
         name='password_reset'),

    path('password_reset_done', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html',),
         name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html',
                                                          success_url=reverse_lazy('authentication:password_reset_complete')),
        name='password_reset_confirm'),
]