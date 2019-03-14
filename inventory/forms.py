from django import forms
from django.forms import ModelForm
from .models import Item


class AddItemForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. Tumbler',
        }
    ))
    cost = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. 300',
        }
    ))
    retail_price = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control input-sm',
            'placeholder': 'ex. 800',
        }
    ))
    class Meta:
        model = Item
        fields = ['name', 'cost', 'retail_price',
                'supplier', 'procurement_method']
