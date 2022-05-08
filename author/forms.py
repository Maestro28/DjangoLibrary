from django import forms
from django.forms import ModelForm

from author.models import Author


class SearchingAuthorForm(forms.Form):
    search = forms.CharField(max_length=20, label='Search author',
                             widget=forms.TextInput(attrs={'placeholder': 'Search...'}))


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        # fields = ['name', 'surname', 'patronymic', 'books']

