import calendar

from django.shortcuts import render
from django.views.generic import TemplateView

from sales.models import Sales

class SalesIndexView(TemplateView):
    template_name = 'sales/sales.html'

    def get_context_data(self, **kwargs):
        context = super(SalesIndexView, self).get_context_data(**kwargs)
        context['days'] = self.number_of_days_in_month()
        context['sales'] = self.daily_sales(context['days'])
        return context

    def number_of_days_in_month(self):
        current_year = 2019
        current_month = 3
        _, days_in_month = calendar.monthrange(current_year, current_month)
        return [day for day in range(1, days_in_month + 1)]

    def daily_sales(self, number_of_days_in_month):
        daily_sales_for_the_month = []
        for day in number_of_days_in_month:
            sales = Sales.objects.values('item__retail_price').filter(sold_on__month=3, sold_on__day=day)
            daily_sales = 0
            for sale in sales:
                daily_sales = daily_sales + sale['item__retail_price']
            daily_sales_for_the_month.append(int(daily_sales))
        
        return daily_sales_for_the_month
