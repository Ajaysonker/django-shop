from django.urls import path
from .views import products_list, product_detail

urlpatterns = [
    path('products/', products_list, name='products_list_url'),
    path('products/<str:slug>/', product_detail, name='product_detail_url'),
]