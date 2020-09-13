from django.shortcuts import render
from django.views import View
from .forms import CustomerForm, OrderForm
# Create your views here.


def order_checkout(request):
    form = CustomerForm
    sub_form = OrderForm
    context = {
        'form': form,
        'sub_form': sub_form,
    }
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        sub_form = OrderForm(request.POST)
        print(request.POST)
        if form.is_valid() and sub_form.is_valid():
            order = sub_form.save(commit=False)
            order.customer = form.save()
            order.save()

    return render(request, 'orders/order_checkout.html', context)
