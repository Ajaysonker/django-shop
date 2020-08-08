from django.contrib import admin
from .models import Product, ProductImage, ProductManufacturer


"""Кастомізація сайту адміністратора"""
admin.site.site_header = 'EShop'
admin.site.site_title = 'Адміністрування'
admin.site.index_title = 'Головна'


# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     """Меню Фотографій в адмінці."""
#     list_display = ('__str__', 'image_url', 'created_at', 'updated_at')
#     search_fields = ['product__name']


class ProductImageInline(admin.TabularInline):
    """Меню Фотографій, зв'язаних з обраним товаром в адмінці."""
    model = ProductImage
    extra = 0
    max_num = 3
    readonly_fields = ('admin_product_image',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Меню Товару в адмінці."""
    list_display = ('name', 'admin_product_photo', 'description', 'manufacturer', 'stock', 'price', 'is_active', 'created_at', 'updated_at')
    list_filter = ('created_at', 'manufacturer', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'description', 'manufacturer__name']
    inlines = [
        ProductImageInline,
    ]



@admin.register(ProductManufacturer)
class ProductManufacturerAdmin(admin.ModelAdmin):
    """Меню Виробника в адмінці."""
    list_display = ('name', 'description', 'admin_manufacture_logo')
    readonly_fields = ('admin_manufacture_logo',)
