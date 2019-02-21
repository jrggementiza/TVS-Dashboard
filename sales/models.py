from django.db import models

from inventory.models import Item

class Sales(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_sell_date = models.DateField(auto_now=True)
