from django import forms
from django.forms import ModelForm

from book.models import Book

class SearchingBookForm(forms.Form):
    search = forms.CharField(max_length=20, label='Search book',
                    widget=forms.TextInput(attrs={'placeholder': 'Search...'}))

class BookForm(ModelForm):
    class Meta:
        model = Book
        # fields = ['name', 'description', 'count', 'authors']
        fields = '__all__'
