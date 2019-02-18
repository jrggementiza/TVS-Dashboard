from django.db import models


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=30)
    item_from = models.CharField(max_length=30)
    item_get_price = models.DecimalField(max_digits=8, decimal_places=2)
    item_sell_price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.item_name


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    item_get_date = models.DateField(auto_now=True)
