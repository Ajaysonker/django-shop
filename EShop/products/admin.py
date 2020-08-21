from django.contrib import admin
from django.utils.safestring import mark_safe

from mptt.admin import DraggableMPTTAdmin
from mptt.admin import TreeRelatedFieldListFilter

from .models import Product, ProductImage, ProductManufacturer, Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    fields = ('parent', 'name', 'slug', 'short_desc')
    list_display = ('tree_actions', 'indented_title')
    prepopulated_fields = {'slug': ('name',)}
    mptt_level_indent = 20


# @admin.register(ProductImage)
# class ProductImageAdmin(admin.ModelAdmin):
#     pass


class ProductImageInline(admin.TabularInline):
    """Меню Фотографій, зв'язаних з обраним товаром в адмінці."""
    model = ProductImage
    extra = 0
    max_num = 6
    min_num = 1
    readonly_fields = ('admin_product_image',)

    def admin_product_image(self, instanse):
        """Надає можливість відобразити всі фотографії обраного товару в адмінці."""
        return mark_safe(f'<img src="{instanse.imageURL}" width="150" />')

    admin_product_image.short_description = 'логотип'


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """Меню Товару в адмінці."""
    fields = ('name', 'slug', 'description', 'manufacturer', 'categories', 'price', 'stock', 'is_active')
    list_display = ('id', 'name', 'admin_product_photo', 'description', 'manufacturer', 'stock', 'price', 'is_active', 'created_at', 'updated_at')
    list_display_links = ('name', 'admin_product_photo')
    list_filter = ('created_at', ('categories', TreeRelatedFieldListFilter), 'manufacturer', 'is_active')
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'description', 'manufacturer__name']
    inlines = [
        ProductImageInline,
    ]
    filter_horizontal = ('categories',)

    def admin_product_photo(self, instanse):
        """Надає можливість відобразити 'основне' фото обраного товару адмінці."""
        product_photo = ProductImage.objects.filter(product__id=instanse.id)[0]
        return mark_safe(f'<img src="{product_photo.imageURL}" width="100" />')

    admin_product_photo.short_description = 'фото продукту'


@admin.register(ProductManufacturer)
class ProductManufacturerAdmin(admin.ModelAdmin):
    """Меню Виробника в адмінці."""
    list_display = ('name', 'description', 'admin_manufacture_logo')
    readonly_fields = ('admin_manufacture_logo',)

    def admin_manufacture_logo(self, instanse):
        """Надає можливість відобразити логотип виробника в адмінці."""
        return mark_safe(f'<img src="{instanse.logoURL}" width="250" />')

    admin_manufacture_logo.short_description = 'логотип'
