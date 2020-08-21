from django.shortcuts import render
from .models import Product


# Create your views here.
def products_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'products/products_list.html', context=context)


def product_detail(request, slug):
    product = Product.objects.get(slug__iexact=slug)
    context = {
        'product': product
    }
    return render(request, 'products/product_detail.html', context=context)
