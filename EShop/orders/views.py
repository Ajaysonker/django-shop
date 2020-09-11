from django.shortcuts import render
from django.views import View
# Create your views here.


def order_checkout(request):
    return render(request, 'orders/order_checkout.html')
