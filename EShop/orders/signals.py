from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import ProductInOrder


@receiver(post_delete, sender=ProductInOrder)
def post_delete_order_total_price(sender, instance, **kwargs):
    all_product_in_order = ProductInOrder.objects.filter(order=instance.order)
    total_price = 0
    for order in all_product_in_order:
        total_price += order.total_price
    order.total_price = total_price
    order.save()
