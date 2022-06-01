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