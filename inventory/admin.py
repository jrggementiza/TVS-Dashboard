from django.contrib import admin

from inventory.models import Item, Inventory

admin.site.register(Item)
admin.site.register(Inventory)
