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

    sold_on = models.DateField(auto_now=True)
