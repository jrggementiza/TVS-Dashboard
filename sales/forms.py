from django import forms
from django.forms import ModelForm

from sales.models import Sales
from customer.models import Customer


class NewCustomerForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ex. Steve',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'ex. Stevenson',
        }
    ))

    class Meta:
        model = Customer
        fields = [
            'first_name', 'last_name', 'customer_type',
        ]


class SellItemForm(ModelForm):
    class Meta:
        model = Sales
        fields = [
            'listing', 'payment_method',
        ]
