from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _

from .models import CustomUser


# class CustomUserCreationForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         fields = UserCreationForm.Meta.fields + ("email",)


class CustomUserCreationForm(UserCreationForm):
    # error_css_class = "error"

    password1 = forms.CharField(label=_('Password'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Enter password')}))
    password2 = forms.CharField(label=_('Password confirmation'),
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': _('Repeat password')}))

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'middle_name']

    def clean_password1(self):
        password1 = self.cleaned_data.get("password1")
        valid_password = validate_password(password1)
        if valid_password is not None:
            raise valid_password.ValidationError()
        return password1

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(_("Passwords no match"))
            # self._errors['middle_name'] = self.error_class([
            #     'Passwords no match'])
        else:
            return password2

    def save(self, commit=True):
        pas = self.clean_password2()
        self.cleaned_data.pop('password1')
        self.cleaned_data.pop('password2')
        return CustomUser.objects.create_user(password=pas, **self.cleaned_data)


class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name']
