from django.urls import path

from . import views

urlpatterns = [
    path('', views.inventory, name='inventory'),
    path('add', views.add, name='add'),
]
