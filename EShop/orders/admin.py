from django.contrib import admin
from .models import Customer, Order, ProductInOrder
# Register your models here.

class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    """Меню Клієнта в адмінці"""
    list_display = ('customer_name', 'customer_phone', 'customer_email', 'customer_address')
    search_fields = ['customer_name', 'customer_phone', 'customer_email']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Меню Замовлення в адмінці"""
    list_display = ('id', 'customer', 'order_status', 'total_price', 'create_at', 'update_at')
    list_filter = ('create_at', 'order_status')
    inlines = [
        ProductInOrderInline
    ]

# @admin.register(ProductInOrder)
# class ProductInOrderAdmin(admin.ModelAdmin):
#     """Меню Замовлення в адмінці"""
#     list_display = ('order', 'product', 'quantity', 'price_per_item', 'total_price')
