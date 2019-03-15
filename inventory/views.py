from django.http import HttpResponse
from django.shortcuts import render, redirect

from inventory.models import Item, Inventory
from inventory.forms import AddItemForm
from inventory.utils import display_newest_items, add_item, delete_item_from_inventory, sell_item, edit_item

from sales.models import Sales
from sales.forms import SellItemForm, NewCustomerForm

from customer.models import Customer


def inventory(request):
    form = AddItemForm()
    sell_item_form, new_customer_form = SellItemForm(), NewCustomerForm()
    prompt = None
    if request.method == 'POST':
        if 'addItem' in request.POST:
            form = AddItemForm(request.POST)
            prompt = add_item(form)

        elif 'deleteItem' in request.POST:
            selected_item = request.POST.get('deleteItem', None)
            prompt = delete_item_from_inventory(selected_item)

        elif 'sellItem' in request.POST:
            selected_item = request.POST.get('sellItem', None)
            sell_item_form = SellItemForm(request.POST)
            new_customer_form = NewCustomerForm(request.POST)
            
            prompt = sell_item(selected_item, sell_item_form, 
                                new_customer_form)

        # TODO: Fix double entry bug
        # TODO: Add customer table and modal
        # TODO: Add Form
        # elif 'editItem' in request.POST:
        #     selected_item = request.POST.get('editItem', None)
        #     prompt = edit_item(selected_item, form)

    #         if selected_item == None:
    #             prompt = 'item not found'
            
    
    inventory = display_newest_items()

    context = {
            'inventory': inventory,
            'form': form,
            'sell_item_form': sell_item_form,
            'new_customer_form': new_customer_form,
            'prompt': prompt,
    }
    return render(request, 'inventory/inventory.html', context)
