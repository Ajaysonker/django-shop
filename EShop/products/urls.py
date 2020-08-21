from django.urls import path
from .views import products_list, product_detail

urlpatterns = [
    path('', products_list, name='products_list_url'),
    path('<str:slug>/', product_detail, name='product_detail_url'),
]