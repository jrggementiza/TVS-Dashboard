from django.shortcuts import render

from .models import Sales


def sales(request):
    sold_items = Sales.objects.all()
    context = {
        'sold_items': sold_items,
    }
    return render(request, 'sales.html', context)
