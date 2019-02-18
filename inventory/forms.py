from django import forms
from django.forms import ModelForm
from .models import Item


class AddItemForm(ModelForm):
    item_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. Tumbler',
        }
    ))
    item_from = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. Supplier',
        }
    ))
    item_get_price = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. 300',
        }
    ))
    item_sell_price = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. 800',
        }
    ))
    class Meta:
        model = Item
        fields = ['item_name', 'item_from',
                  'item_get_price', 'item_sell_price']
