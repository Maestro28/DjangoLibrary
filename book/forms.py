from django import forms
from django.forms import ModelForm

from book.models import Book


class SearchingBookForm(forms.Form):
    search = forms.CharField(max_length=20, label='Search book',
                             widget=forms.TextInput(attrs={'placeholder': 'Search...'}))

class IdForm(forms.Form):

    choices = ()
    authors_id = []
    for book in Book.objects.all():
        for author in book.authors.all():
            if author.id not in authors_id:
                authors_id.append(author.id)
    for id in authors_id:
        a = list(choices)
        a.append((id, id))
        choices = tuple(a)

    id_field = forms.ChoiceField(choices=choices, label="Find book by author id")


class SortForm(forms.Form):
    choices = (
        ('count', 'count ascending'),
        ("-count", 'count descending'),
        ("name", 'name'),
    )
    sort_field = forms.ChoiceField(choices=choices, label="Change books order")


class BookForm(ModelForm):
    class Meta:
        model = Book
        # fields = ['name', 'description', 'count', 'authors']
        fields = '__all__'
