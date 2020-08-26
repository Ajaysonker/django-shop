from django.shortcuts import render
from django.db.models import Q
from .models import Product


# Create your views here.
def products_list(request):
    products = Product.objects.filter(is_active=True)
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

def products_category(request, slug):
    products = Product.objects.filter(Q(categories__parent__slug__iexact=slug) | Q(categories__slug__iexact=slug), is_active=True)
    print(products)
    context = {
        'products': products
    }
    return render(request, 'products/products_list.html', context=context)