from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Item, Inventory
from .forms import AddItemForm


def inventory(request):
    form = AddItemForm()
    prompt = None
    if request.method == 'POST':
        if 'sellItem' in request.POST:
            selected_item = request.POST.get('sellItem', None)
            if selected_item == None:
                prompt = 'item not found'
            item_query = Inventory.objects.get(item=selected_item)
            print(item_query)

        elif 'editItem' in request.POST:
            selected_item = request.POST.get('editItem', None)
            if selected_item == None:
                prompt = 'item not found'
            
        elif 'deleteItem' in request.POST:
            selected_item = request.POST.get('deleteItem', None)
            if selected_item == None:
                prompt = 'item not found'
            item_query = Inventory.objects.get(item=selected_item)
            item_query.delete()

        elif 'addItem' in request.POST:
            form = AddItemForm(request.POST)
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
                new_inventory_item = Inventory(item=item)
                new_inventory_item.save()

    inventory = Inventory.objects.all()
    context = {
            'inventory': inventory,
            'form': form,
            'prompt': prompt,
    }
    return render(request, 'inventory.html', context)


def add(request):
    if request.method == 'POST':
        form = AddItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            new_inventory_item = Inventory(item=item)
            new_inventory_item.save()
            if form is not None:
                redirect_url = '/inventory'
                return redirect(redirect_url)
    else:
        form = AddItemForm()
    context = {
            'form': form,
    }
    return render(request, 'add.html', context)
