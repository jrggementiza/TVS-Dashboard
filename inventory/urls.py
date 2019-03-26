from django.urls import path

from inventory.views import InventoryView, InventoryAddItem #, InventorySellItem
from . import views

urlpatterns = [
    # path('', views.inventory, name='inventory'),
    path('', InventoryView.as_view(), name='inventory'),
    path('add', InventoryAddItem.as_view(), name='add'),
    # path('sell', InventorySellItem.as_view(), name='sell'),
    # path('edit', InventoryEditItem.as_view(), name='inventory'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
