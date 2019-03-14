from django.db import models

from inventory.models import Item

class Sales(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    
    SHOPEE = 'SHP'
    FACEBOOK = 'FB'
    INSTAGRAM = 'IG'
    CAROUSEL = 'CRL'
    GROUPS = 'GRP'

    LISTING_OPTIONS = (
        (SHOPEE, 'Shopee'),
        (FACEBOOK, 'Facebook'),
        (INSTAGRAM, 'Instagram'),
        (CAROUSEL, 'Carousel'),
        (GROUPS, 'GROUPS'),
    )
    listing = models.CharField(
        max_length=3,
        choices=LISTING_OPTIONS,
    )

    BDO = 'BDO'
    BPI = 'BPI'
    PAYMENT_METHOD_OPTIONS = (
        (SHOPEE, 'Shopee'),
        (BDO, 'BDO'),
        (BPI, 'BPI'),
    )
    payment_method = models.CharField(
        max_length=3,
        choices=PAYMENT_METHOD_OPTIONS,
    )


class Customer(models.Model):   
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    NEW = 'NEW'
    REGULAR = 'REG'
    PREFERRED = 'PRE'
    CUSTOMER_TYPE_OPTIONS = (
        (NEW, 'New Customer'),
        (REGULAR, 'Regular Customer'),
        (PREFERRED, 'Preferred'),
    )
    customer_type = models.CharField(
        max_length=3,
        choices=CUSTOMER_TYPE_OPTIONS,
        default=CUSTOMER_TYPE_OPTIONS[0][0],
    )
