from django.urls import path
from .views import order_cart, order_checkout

urlpatterns = [
    path('cart/', order_cart, name='order_cart_url'),
    path('checkout/', order_checkout, name='order_checkout')
]
