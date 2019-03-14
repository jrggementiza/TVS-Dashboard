from django.shortcuts import render

from sales.models import Sales, Customer


def sales(request):
    sold_items = Sales.objects.all()
    customers = Customer.objects.all()
    context = {
        'sold_items': sold_items,
        'customers': customers,
    }
    return render(request, 'sales.html', context)
