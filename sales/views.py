import calendar

from django.shortcuts import render
from django.views.generic import TemplateView

from sales.models import Sales

class SalesIndexView(TemplateView):
    template_name = 'sales/sales.html'

    def get_context_data(self, **kwargs):
        context = super(SalesIndexView, self).get_context_data(**kwargs)
        context['days'], context['sales'] = self.sales()
        
        return context


    def sales(self):
        _, days_in_month = calendar.monthrange(2019, 3)
        number_of_dates_for_the_month = [day for day in range(1, days_in_month + 1)]

        daily_sales_for_the_month = []
        
        for day in number_of_dates_for_the_month:
            sales = Sales.objects.values('item__retail_price').filter(sold_on__month=3, sold_on__day=day)
            daily_sales = 0
            for sale in sales:
                daily_sales = daily_sales + sale['item__retail_price']
            daily_sales_for_the_month.append(int(daily_sales))
        
        return number_of_dates_for_the_month, daily_sales_for_the_month
