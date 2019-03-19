from django.urls import path

from sales.views import SalesIndexView

urlpatterns = [
    path('', SalesIndexView.as_view(), name='sales'),
]
