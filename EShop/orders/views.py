from django.shortcuts import render
from .models import Customer, Order, ProductInOrder
# Create your views here.


def order_cart(request):
    return render(request, 'orders/order_cart.html')


def order_checkout(request):
    return render(request, 'orders/order_checkout.html')
