from django import forms
from django.forms import ModelForm
from .models import Item


class AddItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'item_from',
                  'item_get_price', 'item_sell_price']
        labels = {
            'item_name': 'Item Name',
            'item_from': 'Item From',
            'item_get_price': 'Item Get Price',
            'item_sell_price': 'Item Sell Price',
        }
