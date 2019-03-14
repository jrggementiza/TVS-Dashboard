from django.db import models

class Customer(models.Model):
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
