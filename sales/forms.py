from django import forms
from django.forms import ModelForm

from sales.models import Sales
from customer.models import Customer


class CustomerForm(ModelForm):
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
    customer_type = forms.ChoiceField(
        choices=Customer.CUSTOMER_TYPE_OPTIONS,
        widget=forms.RadioSelect()
    )
    class Meta:
        model = Customer
        fields = [
            'first_name', 'last_name', 'customer_type',
        ]


class SellItemForm(ModelForm):
    listing = forms.ChoiceField(
        choices=Sales.LISTING_OPTIONS,
        widget=forms.RadioSelect()
        )
    payment_method = forms.ChoiceField(
        choices=Sales.PAYMENT_METHOD_OPTIONS,
        widget=forms.RadioSelect()
        )
    class Meta:
        model = Sales
        fields = [
            'listing', 'payment_method',
        ]
