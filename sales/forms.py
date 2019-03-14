from django import forms
from django.forms import ModelForm

from sales.models import Sales
from customer.models import Customer


class SellItemForm(ModelForm):
    class Meta:
        model = Sales
        fields = [
            'listing', 'payment_method',
        ]


class NewCustomerForm(ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. Tumbler',
        }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. 300',
        }
    ))
    class Meta:
        model = Customer
        fields = [
            'first_name', 'last_name', 'customer_type',
        ]
