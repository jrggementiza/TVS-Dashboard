from inventory.models import Supplier, Item, Inventory
from sales.models import Sales, Customer


def display_newest_items():
    items = Inventory.objects.all()
    return items


def add_item(form):
    if form.is_valid():
        item = form.save(commit=False)
        item.save()
        new_inventory_item = Inventory(item=item)
        new_inventory_item.save()
    else:
        return 'Form Values Invalid!'


def delete_item_from_inventory(selected_item):
    if selected_item != None:
        item_query = Inventory.objects.get(item=selected_item)
        item_query.delete()
    else:
        return 'Selected Item not Found!'


def new_customer(parameter_list):
    pass

def existing_customer(parameter_list):
    pass


def sell_item(selected_item, sell_item_form, new_customer_form):
	if selected_item != None:
		if sell_item_form.is_valid() and new_customer_form.is_valid():
			item_to_sell = Item.objects.get(id=selected_item)

			new_sales = sell_item_form.save(commit=False)
			new_sales.item = item_to_sell	
			new_sales.save()

			new_customer = new_customer_form.save(commit=False)
			new_customer.item = item_to_sell
			new_customer.save()

			delete_item_from_inventory(selected_item)
		else:
			return 'Form Invalid!'
	else:
		return 'Selected Item not Found!'


def edit_item(selected_item, form):
    # if form.is_valid():
    #     item_updates = form.save(commit=False)
        # Item.objects.get(item=selected_item).update(item=item_updates)
    pass


