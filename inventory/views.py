from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse

from django.views.generic import View, TemplateView, FormView

from inventory.models import Item, Inventory
from inventory.forms import AddItemForm

from sales.models import Sales
from sales.forms import SellItemForm, CustomerForm

from customer.models import Customer


class InventoryView(TemplateView):
    """ View that displays all Items currently on Inventory 
    and can add, sell, and delete items from Inventory.
    """
    template_name = 'inventory/inventory.html'

    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data(**kwargs)
        context['inventory_list'] = self.display_inventory_items()
        context['form'] = AddItemForm()
        context['customer_form'] = CustomerForm()
        context['sell_item_form'] = SellItemForm()
        return context

    def display_inventory_items(self):
        return Inventory.objects.all()


class InventoryAddItem(FormView):
    """ Im creating an endpoint that:
    - accepts a request.post
    - with the form payload
    - validates form
    - creates Item Object, and creates Inventory Object
    - and redirects to success_url with success prompt
    - unsuccessful redirect to unsuccessful_url with fail prompt
    """

    form_class = AddItemForm
    success_url = '/inventory'

    def form_valid(self, form):
        item = form.save(commit=False)
        item.save()
        new_inventory_item = Inventory(item=item)
        new_inventory_item.save()
        return super(InventoryAddItem, self).form_valid(form)


def delete_item(request, item_id):
    if request.method == 'POST':
        selected_item = get_object_or_404(Item, id=item_id)
        selected_item_in_inventory = get_object_or_404(Inventory, item=selected_item)
        selected_item_in_inventory.delete()
        selected_item.delete()
        return redirect('/inventory')
    else:
        return HttpResponse('not the right method')


def sell_item(request, item_id):
    if request.method == 'POST':
        selected_item = get_object_or_404(Inventory, item=item_id)
        item_to_sell = Item.objects.get(id=selected_item.item.id)

        # Load Forms
        customer_form = CustomerForm(request.POST)
        sell_item_form = SellItemForm(request.POST)

        if customer_form.is_valid() and sell_item_form.is_valid():
            
            # Creating a new Sale in Sales Table
            new_sales = sell_item_form.save(commit=False)
            new_sales.item = item_to_sell
            new_sales.save()

            # Checks New Customer / Existing Customer Purchasing the Item
            customer = customer_form.save(commit=False)
            try:
                existing_customer = Customer.objects.get(first_name=customer.first_name, last_name=customer.last_name)
                item_to_sell.customer = existing_customer
                item_to_sell.save()
            except Customer.DoesNotExist:
                print('customer not found. creating new customer!')
                customer.save()
                item_to_sell.customer = customer
                item_to_sell.save()

            # Delete Item in Inventory
            selected_item.delete()

            return redirect('/inventory')
        else:
            return HttpResponse('form not valid')
    else:
        return HttpResponse('not the right method')
