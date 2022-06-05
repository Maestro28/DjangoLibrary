from django import forms
from django.forms import ModelForm

from .models import Order


class OrderCreateForm(ModelForm):
    class Meta:
        model = Order
        # fields = '__all__'
        fields = ['book', 'plated_end_at']


class OrderUpdateForm(ModelForm):
    class Meta:
        model = Order
        fields = ['end_at']


class SortForm(forms.Form):
    choices = (
        ('created_at', 'created at ascending'),
        ("-created_at", 'created at descending'),
        ("book", 'book name'),
    )
    sort_field = forms.ChoiceField(choices=choices, label="Change order ordering")
