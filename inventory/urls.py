from django.urls import path

from inventory.views import InventoryView, InventoryAddItem
from . import views

urlpatterns = [
    path('', InventoryView.as_view(), name='inventory'),
    path('add', InventoryAddItem.as_view(), name='add'),
    path('sell/<int:item_id>/', views.sell_item, name='sell_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]
