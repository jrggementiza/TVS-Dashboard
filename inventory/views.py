from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.urls import reverse

from django.views.generic import View, TemplateView, FormView, CreateView, DeleteView

from inventory.models import Item, Inventory
from inventory.forms import AddItemForm

from sales.models import Sales
from sales.forms import SellItemForm, NewCustomerForm

from customer.models import Customer


class InventoryView(TemplateView):
    """ View that displays all Items currently on Inventory and has ability to
    add, sell, and delete items from Inventory.
    """
    template_name = 'inventory/inventory.html'

    def get_context_data(self, **kwargs):
        context = super(InventoryView, self).get_context_data(**kwargs)
        context['inventory_list'] = self.display_inventory_items()
        context['form'] = AddItemForm()
        context['new_customer_form'] = NewCustomerForm()
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


# TODO: 404 template
# TODO: Method is only post
def delete_item(request, item_id):
    selected_item = get_object_or_404(Inventory, item=item_id)
    selected_item.delete()
    return redirect('/inventory')


# TODO: FBV with no Template
# class InventorySellItem(View):
#     def post(self, request):
#         print(request)
#         return HttpResponse('sell works!')


# DOING: Refactoring to CBV + FBV w/o Templates
# def inventory(request):
#     form = AddItemForm()
#     sell_item_form, new_customer_form = SellItemForm(), NewCustomerForm()
#     prompt = None
#     if request.method == 'POST':
#         if 'addItem' in request.POST:
#             form = AddItemForm(request.POST)
#             prompt = add_item(form)

#         elif 'deleteItem' in request.POST:
#             selected_item = request.POST.get('deleteItem', None)
#             prompt = delete_item_from_inventory(selected_item)

#         elif 'sellItem' in request.POST:
#             selected_item = request.POST.get('sellItem', None)
#             sell_item_form = SellItemForm(request.POST)
#             new_customer_form = NewCustomerForm(request.POST)
            
#             prompt = sell_item(selected_item, sell_item_form, 
#                                 new_customer_form)

#         # elif 'editItem' in request.POST:
#         #     selected_item = request.POST.get('editItem', None)
#         #     prompt = edit_item(selected_item, form)

#     #         if selected_item == None:
#     #             prompt = 'item not found'
            
    
#     inventory_list = Inventory.objects.all()

#     context = {
#             'inventory_list': inventory_list,
#             'form': form,
#             'sell_item_form': sell_item_form,
#             'new_customer_form': new_customer_form,
#             'prompt': prompt,
#     }
#     return render(request, 'inventory/inventory.html', context)
