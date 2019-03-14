from django.db import models


class Supplier(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    id = models.AutoField(primary_key=True) # not needed because auto generate
    name = models.CharField(max_length=30)

    # item_from = models.CharField(max_length=30) # item_from -> supplier
    KOREA = 'KOR'
    SINGAPORE = 'SGP'
    TAIWAN = 'TWN'
    SUPPLIER_CHOICES = (
        (KOREA, 'Korea'),
        (SINGAPORE, 'Singapore'),
        (TAIWAN, 'Taiwan'),
    )
    supplier = models.CharField(
        max_length=3,
        choices=SUPPLIER_CHOICES,
    )

    cost = models.DecimalField(max_digits=8, decimal_places=2) # renamed item_get_price -> to cost
    retail_price = models.DecimalField(max_digits=8, decimal_places=2)  # renamed item_sell_price -> retail_price

    # item_get_date = models.DateField(auto_now=True) # moved from inventory -> Item
    procurement_date = models.DateField(auto_now=True) # renamed from item_get_date -> procurement_date

    PRE_ORDER = 'PO'
    SELF_ORDER = 'SO'
    LOCAL_ACQUISITION = 'LA'
    PROCUREMENT_METHOD_CHOICES = (
        (PRE_ORDER, 'Pre Order'),
        (SELF_ORDER, 'Self Order'),
        (LOCAL_ACQUISITION, 'Local Acquisition'),
    )
    procurement_method = models.CharField(
        max_length=2,
        choices=PROCUREMENT_METHOD_CHOICES,
    )

    #TODO: Date Sold upon selling of item
    # sell_date = models.DateField(auto_now=True)

    # stock_keeping_unit = default is one.
    # view add item default is 1.
    # view sell item default is 1. if greater than 1, sku - 1. if sku == 1, sku delete
    
    
    def __str__(self):
        return self.name


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
