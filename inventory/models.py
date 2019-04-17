from django.db import models

from customer.models import Customer


class Supplier(models.Model):
    name = models.CharField(max_length=30)


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)

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

    cost = models.DecimalField(max_digits=8, decimal_places=2)
    retail_price = models.DecimalField(max_digits=8, decimal_places=2)
    procurement_date = models.DateField(auto_now=True)
    
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
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
