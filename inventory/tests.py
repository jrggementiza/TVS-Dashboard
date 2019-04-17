from datetime import datetime

from django.test import TestCase, RequestFactory

from inventory.models import Item, Inventory
from inventory.views import InventoryView


class InventoryTest(TestCase):
    def setUp(self):
        self.item_red = Item.objects.create(name='Red Tumbler',
                            supplier='KOR',
                            cost=1200,
                            retail_price=2500, 
                            procurement_date=datetime.now(),
                            procurement_method='PO',
                            )
        self.item_blue = Item.objects.create(name='Blue Tumbler',
                            supplier='SGP',
                            cost=1000,
                            retail_price=2200,
                            procurement_date=datetime.now(),
                            procurement_method='SO',
                            )
        Inventory.objects.create(item=self.item_red)
        Inventory.objects.create(item=self.item_blue)

        self.inventory = Inventory.objects.all()

    def test_inventory_displays_items(self):
        inventory_view = InventoryView()
        test_inventory = inventory_view.get_context_data()['inventory_list']
        self.assertEqual(list(test_inventory), list(self.inventory)),

    def test_inventory_contains_individual_items(self):
        inventory_item = Inventory.objects.get(id=1)
        self.assertEqual(inventory_item.item.name, 'Red Tumbler')
        inventory_item = Inventory.objects.get(id=2)
        self.assertEqual(inventory_item.item.name, 'Blue Tumbler')
